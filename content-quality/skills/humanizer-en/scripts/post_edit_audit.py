"""Post-edit audit: compares the text before and after editing.

Editing changes wording, not content. The audit checks deterministically (stdlib, no network)
that nothing that carries content was lost or added along the way:

  input             - both texts non-empty; an unchanged text is a valid result, not an error
  sensitive_values  - multiset: provisions, dates, case numbers, numbers and amounts, quotations,
                      fields to fill in; anything missing or new = BLOCK
  deontic_profile   - count of obligations, prohibitions, permissions and recommendations before
                      and after; discourse frames ("it should be noted") do not count; "can" and
                      "cannot" do not count either (in prose they mostly mean ability)
  certainty         - "likely" / "provisionally" removed with no trace of uncertainty = BLOCK;
                      thinning stacked hedges is allowed
  tool_traces       - unfilled fields and chat formulas in the output = the text is not ready
  protected_terms   - legal terms of art, terms defined in the text, terms passed as a parameter
                      (verbatim); swapping one for a "synonym" = BLOCK
  shortening_limit  - word loss above the limit (default 30%) = BLOCK; the limit is a ceiling,
                      not a target

The result is OK / WARN / BLOCK with the full denominator (every check is listed, passed ones
too). Exit code: 0 OK, 10 WARN, 20 BLOCK, 2 bad call.

Usage:  python post_edit_audit.py BEFORE.txt AFTER.txt [--max-cut 0.3]
            [--protected "term1;term2"] [--json]
"""
import argparse
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

CHECKS = ("input", "sensitive_values", "deontic_profile", "certainty", "tool_traces",
          "protected_terms", "shortening_limit")
LEVEL = {"OK": 0, "WARN": 1, "BLOCK": 2}
EXIT = {"OK": 0, "WARN": 10, "BLOCK": 20}
SHORT_TEXT = 40  # below this many words the shortening limit is indicative (WARN), not hard

MONTHS = {m: i for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july", "august", "september",
     "october", "november", "december"], start=1)}
MON = "|".join(list(MONTHS) + ["jan", "feb", "mar", "apr", "jun", "jul", "aug", "sep", "sept",
                               "oct", "nov", "dec"])
L = r"[A-Za-z]"
WB = rf"(?<!{L})"  # word boundary on the left
WE = rf"(?!{L})"   # word boundary on the right

# --- normalisation ------------------------------------------------------------------------

def norm(t: str) -> str:
    t = unicodedata.normalize("NFC", t)
    t = re.sub(r"[‐-―−]", "-", t)
    t = t.replace("’", "'").replace("‘", "'")
    t = re.sub(r"[   \t\r\n ]+", " ", t)
    return t.strip()


def words(t: str) -> list:
    return re.findall(r"\w+", t)


def _month(name: str) -> int:
    n = name.lower().rstrip(".")
    return next(v for k, v in MONTHS.items() if k.startswith(n[:3]))

# --- sensitive values ---------------------------------------------------------------------

RE_QUOTE = re.compile(r"[\"“]([^\"“”]{2,400})[\"”]")
RE_MARKER = re.compile(r"\[to be completed:[^\]\n]*\]", re.I)  # the skill's own marker: not a value, but not ready
# a field to fill in has a letter in it: "[2026] EWHC 1432" and footnote "[1]" are not fields
RE_FIELD = re.compile(r"\[(?=[^\]\n]*[A-Za-z])[^\]\n]{1,60}\]|\{\{[^}\n]{1,60}\}\}|<[^<>\n]{1,40}>")
RE_PROV = re.compile(
    WB + r"(?:article|art\.|section|sec\.|s\.|clause|cl\.|rule|schedule|paragraph|para\.|regulation|§)"
    r"\s*\d+[A-Za-z]?(?:\(\w{1,4}\))*(?:\s*(?:and|or|,)?\s*\(\w{1,4}\))*", re.I)
RE_CASE = re.compile(r"\b[A-Z]{1,4}-\d+/\d{2,4}\b|\[\d{4}\]\s+[A-Z]{2,8}(?:\s+\([A-Za-z]+\))?\s+\d+"
                     r"|\b\d{1,2}:\d{2}-[a-z]{2}-\d+\b|\b[A-Z]{2,4}-\d{4}-\d{3,8}\b")
RE_ECLI = re.compile(r"ECLI:[A-Z]{2}:[A-Z0-9.]+:\d{4}:[A-Z0-9.]+")
RE_DATE_DMY = re.compile(rf"\b(\d{{1,2}})(?:st|nd|rd|th)?\s+(?:of\s+)?({MON})\.?,?\s+(\d{{4}})\b", re.I)
RE_DATE_MDY = re.compile(rf"\b({MON})\.?\s+(\d{{1,2}})(?:st|nd|rd|th)?,?\s+(\d{{4}})\b", re.I)
RE_DATE_NUM = re.compile(r"(?<!\d)(\d{1,2})[./](\d{1,2})[./](\d{4})(?!\d)")
RE_DATE_ISO = re.compile(r"(?<!\d)(\d{4})-(\d{2})-(\d{2})(?!\d)")
RE_NUM = re.compile(r"(?<![\d.])\d{1,3}(?:,\d{3})+(?:\.\d+)?(?!\d)|(?<![\d.,])\d+(?:\.\d+)?(?!\d)")


def _mask(t, rx, found, label, canon=lambda m: norm(m.group(0))):
    def sub(m):
        found.append((label, canon(m)))
        return " \u0000 "
    return rx.sub(sub, t)


def _prov_canon(m):
    s = re.sub(r"\s+", "", m.group(0).lower())
    for a, b in (("article", "art."), ("section", "s."), ("sec.", "s."), ("clause", "cl."),
                 ("paragraph", "para."), ("and", ""), ("or", ""), (",", "")):
        s = s.replace(a, b)
    return s


def values(t: str) -> Counter:
    """Multiset of values an edit must neither lose nor add."""
    t = RE_MARKER.sub(" ", norm(t))
    found = []
    t = _mask(t, RE_QUOTE, found, "quote", lambda m: norm(m.group(1)))
    t = _mask(t, RE_FIELD, found, "field")
    t = _mask(t, RE_ECLI, found, "ECLI")
    t = _mask(t, RE_CASE, found, "case", lambda m: re.sub(r"\s+", " ", m.group(0)))
    t = _mask(t, RE_PROV, found, "provision", _prov_canon)
    t = _mask(t, RE_DATE_DMY, found, "date", lambda m: "%s-%02d-%02d" % (m.group(3), _month(m.group(2)), int(m.group(1))))
    t = _mask(t, RE_DATE_MDY, found, "date", lambda m: "%s-%02d-%02d" % (m.group(3), _month(m.group(1)), int(m.group(2))))
    t = _mask(t, RE_DATE_NUM, found, "date", lambda m: "%s-%02d-%02d" % (m.group(3), int(m.group(2)), int(m.group(1))))
    t = _mask(t, RE_DATE_ISO, found, "date", lambda m: m.group(0))
    _mask(t, RE_NUM, found, "number", lambda m: m.group(0).replace(",", ""))
    return Counter(found)

# --- deontic profile ----------------------------------------------------------------------

FRAMES = [r"it\s+(?:should|must|may|can)\s+be\s+(?:noted|said|emphasi[sz]ed|stressed|remembered|added|mentioned|observed)",
          r"it\s+is\s+worth\s+\w+", r"needless\s+to\s+say", r"may\s+well\s+be", r"it\s+may\s+seem"]
NEG = {
    "permission": [r"might\s+not", r"need\s+not", r"needn't", r"(?:does|do|did)\s+not\s+have\s+to", r"(?:doesn't|don't)\s+have\s+to",
                   r"(?:is|are)\s+not\s+(?:required|obliged|obligated|bound)\s+to", r"(?:is|are)\s+under\s+no\s+obligation"],
    "prohibition": [r"must\s+not", r"mustn't", r"may\s+not", r"shall\s+not", r"shan't",
                    r"(?:is|are)\s+not\s+(?:permitted|allowed|entitled)\s+to", r"(?:has|have)\s+no\s+right\s+to"],
}
POS = {
    "prohibition": [r"(?:is|are)\s+prohibited", r"(?:is|are)\s+forbidden", r"prohibited\s+from", r"forbidden\s+to"],
    "obligation": [r"must", r"shall", r"(?:has|have)\s+to", r"(?:is|are|will\s+be)\s+(?:required|obliged|obligated|bound)\s+to",
                   r"(?:is|are)\s+under\s+an?\s+obligation", r"undertakes?\s+to", r"needs?\s+to"],
    # "might" counts with "may": both are the modal of possibility, and editors swap them freely
    "permission": [r"may", r"might", r"(?:is|are)\s+(?:entitled|permitted|allowed)\s+to", r"(?:has|have)\s+the\s+right\s+to",
                   r"entitled\s+to"],
    "recommendation": [r"should", r"ought\s+to", r"(?:is|are)\s+recommended", r"we\s+recommend", r"it\s+is\s+advisable"],
}


def _rx(patterns):
    return re.compile(WB + "(?:" + "|".join(patterns) + ")" + WE, re.I)


def deontic_profile(t: str) -> dict:
    t = _rx(FRAMES).sub(" ", norm(t))
    out = Counter({k: 0 for k in ("obligation", "prohibition", "permission", "recommendation")})
    for group in (NEG, POS):
        for cat, pats in group.items():
            rx = _rx(pats)
            out[cat] += len(rx.findall(t))
            t = rx.sub(" ", t)
    return dict(out)

# --- certainty ----------------------------------------------------------------------------

RE_UNCERTAIN = re.compile(WB + "(?:" + "|".join([
    r"likely", r"unlikely", r"probabl\w*", r"possibl[ey]", r"perhaps", r"presumabl[ey]", r"provisional\w*",
    r"preliminar\w*", r"tentativ\w*", r"potentially", r"approximately", r"roughly", r"estimated",
    r"(?:it\s+is\s+)?(?:still\s+|not\s+yet\s+)?unclear", r"not\s+yet\s+(?:known|clear|decided|confirmed|certain)",
    r"it\s+appears", r"appears?\s+to", r"seems?", r"might", r"it\s+is\s+possible",
]) + ")" + WE, re.I)
RE_MAY = re.compile(WB + r"(?:may|might|could)" + WE, re.I)


def uncertainty(t: str) -> int:
    return len(RE_UNCERTAIN.findall(norm(t)))

# --- tool traces --------------------------------------------------------------------------

START = re.compile(r"^\s*(?:here's|here\s+is|here\s+are|certainly[!,.]|sure[!,.]|of\s+course[!,.]|"
                   r"great\s+question|absolutely[!,.])", re.I)
FORMULAS = re.compile(r"(?:i\s+)?hope\s+(?:this|that|it)\s+helps|let\s+me\s+know\s+if\s+you(?:'d)?\s+(?:like|want)\s+me\s+to|"
                      r"would\s+you\s+like\s+me\s+to|as\s+an?\s+(?:ai|language\s+model|ai\s+assistant)|"
                      r"i'd\s+be\s+(?:happy|glad)\s+to\s+(?:help|expand|adjust|draft)", re.I)
OFFER = re.compile(r"you\s+can\s+(?:easily\s+)?(?:adjust|tweak|modify|customi[sz]e|edit|adapt|copy|paste|fill\s+in)|"
                   r"i\s+can\s+(?:also\s+)?(?:prepare|draft|expand|shorten|translate|adjust|help|create|write)|"
                   r"if\s+you(?:'d)?\s+(?:like|want)\s+(?:me|a\s+(?:shorter|longer|different))", re.I)
DISCLAIMER = re.compile(r"(?:does\s+not|doesn't)\s+constitute\s+legal\s+advice|not\s+legal\s+advice", re.I)


def without_wrapper(t: str) -> str:
    """Text without chat-wrapper sentences ("Here's...", "You can adjust...", "I hope this helps").

    Modals and terms inside the wrapper are not document content: removing them changes neither
    a norm nor terminology, so it must not block the profile.
    """
    sentences = re.split(r"(?<=[.!?:])\s+", norm(t))
    return " ".join(s for s in sentences if not (START.match(s) or FORMULAS.search(s) or OFFER.search(s)))

# --- protected terms ----------------------------------------------------------------------

# Pairs that a lay editor takes for synonyms and the law does not. Key = name, value = stem.
TERMS = {
    "deposit": r"deposits?", "advance payment": r"advance\s+payments?", "down payment": r"down\s+payments?",
    "termination": r"terminat\w*", "rescission": r"rescission|rescind\w*", "cancellation": r"cancell?\w*",
    "warranty": r"warrant(?:y|ies)", "guarantee": r"guarant\w*", "indemnity": r"indemn\w*",
    "void": r"void(?!able)", "voidable": r"voidable", "unenforceable": r"unenforceab\w*",
    "liquidated damages": r"liquidated\s+damages", "penalty": r"penalt\w*", "damages": r"damages",
    "limitation period": r"limitation\s+periods?|time[- ]barred", "set-off": r"set[- ]off",
    "assignment": r"assignments?", "novation": r"novat\w*", "power of attorney": r"powers?\s+of\s+attorney",
    "lien": r"liens?", "pledge": r"pledg\w*", "mortgage": r"mortgag\w*",
    "judgment": r"judge?ments?", "order": r"court\s+orders?", "injunction": r"injunct\w*",
    "appeal": r"appeal\w*", "lease": r"leas(?:e|es|ed|ing)", "licence": r"licen[cs]\w*",
    "claimant": r"claimants?|plaintiffs?", "defendant": r"defendants?|respondents?",
}
_TERM_RX = {k: re.compile(WB + "(?:" + v + ")" + WE, re.I) for k, v in TERMS.items()}
RE_DEF = re.compile(
    r"\((?:the\s+)?[\"“]([^\"“”]{2,40})[\"”]\)"
    r"|hereinafter(?:\s+referred\s+to\s+as)?\s+(?:the\s+)?[\"“]([^\"“”]{2,40})[\"”]"
    r"|[\"“]([^\"“”]{2,40})[\"”]\s+(?:means|shall\s+mean|refers\s+to)", re.I)


def defined_terms(t: str) -> list:
    out = []
    for m in RE_DEF.finditer(norm(t)):
        term = next(g for g in m.groups() if g).strip()
        if term not in out:
            out.append(term)
    return out


def _count_verbatim(t: str, term: str) -> int:
    return len(re.findall(WB + re.escape(term) + WE, t))

# --- audit --------------------------------------------------------------------------------

def _c(name, status, details):
    return {"name": name, "status": status, "details": details}


def audit(before: str, after: str, max_cut: float = 0.30, protected=()) -> dict:
    a, b = norm(before or ""), norm(after or "")
    checks = []
    if not a or not b:
        checks.append(_c("input", "BLOCK", "empty text " + ("before editing" if not a else "after editing")
                         + " - nothing to compare, which is not a pass"))
        checks += [_c(n, "BLOCK", "not run: empty input") for n in CHECKS[1:]]
        return {"status": "BLOCK", "unchanged": False, "checks": checks}

    unchanged = a == b
    checks.append(_c("input", "OK", "no change - a valid result when the text needed no editing"
                     if unchanged else f"words before: {len(words(a))}, after: {len(words(b))}"))

    va, vb = values(a), values(b)
    lost, added = va - vb, vb - va
    if lost or added:
        parts = []
        if lost:
            parts.append("lost: " + "; ".join(f"{k} {v}" for (k, v) in sorted(lost.elements())))
        if added:
            parts.append("added: " + "; ".join(f"{k} {v}" for (k, v) in sorted(added.elements())))
        checks.append(_c("sensitive_values", "BLOCK", " | ".join(parts)))
    else:
        checks.append(_c("sensitive_values", "OK", f"matching: {sum(va.values())} values"))

    ta, tb = without_wrapper(a), without_wrapper(b)  # the chat wrapper is not document content
    pa, pb = deontic_profile(ta), deontic_profile(tb)
    diff = {k: (pa[k], pb[k]) for k in pa if pa[k] != pb[k]}
    if diff:
        checks.append(_c("deontic_profile", "BLOCK", "force of a norm changed: " + ", ".join(
            f"{k} {x}->{y}" for k, (x, y) in diff.items()) + " (check every 'may', 'must', 'must not', 'should')"))
    else:
        checks.append(_c("deontic_profile", "OK", ", ".join(f"{k} {v}" for k, v in pa.items())))

    ua, ub = uncertainty(ta), uncertainty(tb)
    if ua and not ub and not RE_MAY.search(tb):
        checks.append(_c("certainty", "BLOCK", f"uncertainty markers {ua}->0: the text now claims more than the "
                         "original ('likely', 'provisionally' are content, not padding)"))
    elif ub > ua:
        checks.append(_c("certainty", "WARN", f"uncertainty added {ua}->{ub} - did the original leave it out on purpose?"))
    else:
        checks.append(_c("certainty", "OK", f"uncertainty markers {ua}->{ub}"
                         + (" (stacked hedges thinned, uncertainty kept)" if ub < ua else "")))

    traces = [m.group(0) for m in RE_MARKER.finditer(b)]
    traces += [m.group(0) for m in RE_FIELD.finditer(RE_MARKER.sub(" ", b))]
    traces += [m.group(0).strip() for m in START.finditer(b)]
    traces += [m.group(0) for m in FORMULAS.finditer(b)]
    traces += [m.group(0) for m in OFFER.finditer(b)]
    if traces:
        checks.append(_c("tool_traces", "BLOCK", "text not ready to send: " + "; ".join(traces)
                         + " (a person fills the fields - do not invent values; remove chat formulas)"))
    elif DISCLAIMER.search(b) and not DISCLAIMER.search(a):
        checks.append(_c("tool_traces", "WARN", "'not legal advice' added - intended?"))
    else:
        checks.append(_c("tool_traces", "OK", "no fields to fill in and no chat formulas"))

    block, warn = [], []
    for name, rx in _TERM_RX.items():
        # A listed term that APPEARS is a swap (deposit -> advance payment): BLOCK. One that only
        # disappears is often an everyday word ("human judgment", "we guarantee"): WARN.
        x, y = len(rx.findall(ta)), len(rx.findall(tb))
        if x == 0 and y > 0:
            block.append(f"{name} {x}->{y}")
        elif x != y:
            warn.append(f"{name} {x}->{y}")
    for term in list(defined_terms(a)) + [p for p in protected if p]:
        x, y = _count_verbatim(ta, term), _count_verbatim(tb, term)
        if x and not y:
            block.append(f'"{term}" {x}->0')
        elif x != y:
            warn.append(f'"{term}" {x}->{y}')
    if block:
        checks.append(_c("protected_terms", "BLOCK", "a term disappeared or appeared in place of another: "
                         + "; ".join(block) + ("; warnings: " + "; ".join(warn) if warn else "")))
    elif warn:
        checks.append(_c("protected_terms", "WARN", "number of uses changed: " + "; ".join(warn)))
    else:
        checks.append(_c("protected_terms", "OK", "terms unchanged"))

    # measured without the chat wrapper: cutting "Here's..." / "I hope this helps" is not a loss,
    # and counting it pushes the editor to keep filler just to stay under the limit
    na, nb = len(words(ta)), len(words(tb))
    cut = (na - nb) / na if na else 0.0
    if cut > max_cut:
        short = na < SHORT_TEXT
        checks.append(_c("shortening_limit", "WARN" if short else "BLOCK",
                         f"cut {cut:.0%} > limit {max_cut:.0%} - a shorter text is not the goal"
                         + (f" (text under {SHORT_TEXT} words: the limit is indicative; the values check"
                            " guards the facts)" if short else "")))
    else:
        checks.append(_c("shortening_limit", "OK", f"length change {-cut:+.0%} (cut limit {max_cut:.0%})"))

    status = max((k["status"] for k in checks), key=LEVEL.get)
    return {"status": status, "unchanged": unchanged, "checks": checks}


def report(r: dict) -> str:
    n = Counter(k["status"] for k in r["checks"])
    lines = [f"POST-EDIT AUDIT: {r['status']} (checks {len(r['checks'])}: OK {n['OK']}, "
             f"WARN {n['WARN']}, BLOCK {n['BLOCK']})"]
    lines += [f"  [{k['status']}] {k['name']}: {k['details']}" for k in r["checks"]]
    return "\n".join(lines)


def main(argv=None) -> int:
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    p = argparse.ArgumentParser(description="Post-edit audit (humanizer-en)")
    p.add_argument("before")
    p.add_argument("after")
    p.add_argument("--max-cut", type=float, default=0.30, help="maximum word loss (0-1), default 0.30")
    p.add_argument("--protected", default="", help="terms protected verbatim, separated by ';'")
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    r = audit(Path(a.before).read_text(encoding="utf-8"), Path(a.after).read_text(encoding="utf-8"),
              max_cut=a.max_cut, protected=[x.strip() for x in a.protected.split(";")])
    print(json.dumps(r, ensure_ascii=False, indent=1) if a.json else report(r))
    return EXIT[r["status"]]


if __name__ == "__main__":
    sys.exit(main())
