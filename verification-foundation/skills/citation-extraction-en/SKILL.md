---
name: citation-extraction-en
description: >
  Deterministically extracts every legal citation from an English-language text - ECLI
  (CJEU and national), EU act identifiers (CELEX, Official Journal references, Regulation/
  Directive numbers), case names, and cited provisions (Article/section) - then normalises,
  deduplicates and resolves short references (ibid., id., supra, op. cit., the above-cited
  judgment) to their antecedent. The front-end to verification: find every citation first,
  then check it. Mechanical (patterns + rules, no LLM at extraction). Jurisdiction-neutral,
  EU-aware. Pairs with output-scoring-en and eu-sparql-search. Use when: "list every
  citation in this text", "what authorities are cited", "extract the provisions", "pull the
  case references", "what is cited here" - before verification or before sending.
metadata:
  author: Wiesław Mazur / MateMatic
  version: 1.0.0
  inspiration: >
    The extraction -> aggregation -> annotation architecture is based on eyecite (Free Law
    Project), BSD-2-Clause (https://github.com/freelawproject/eyecite). US reporter regexes
    dropped; ECLI, CELEX/OJ and EU-citation patterns and antecedent rules written from
    scratch. English counterpart of ekstraktor-cytatow-pl.
  companion_skills: output-scoring-en, eu-sparql-search, legal-syllogism-en
---

# Citation extraction - find every citation before you check it

## Philosophy

**You can only verify what you first find.** Grounding a citation checks whether it exists in the
source - but it runs on a list that someone has to assemble first. This skill is that front-end: it
walks the text and lists every authority, so none slips past verification. A missed citation is an
unverified one.

Extraction is **mechanical** (patterns + rules, not an LLM) on purpose - a model asked to find
citations might miss one or invent one. Local, jurisdiction-neutral, EU-aware.

## Three steps (after eyecite)

1. **Extraction** - recognise and capture every reference by the patterns below.
2. **Aggregation** - resolve short references (ibid. / id. / supra / op. cit. / "the above-cited
   judgment") to their full antecedent, so they count as one citation, not several.
3. **Hand-off** - pass the structured list to verification (grounding) and, for EU sources, to
   eu-sparql-search for retrieval.

## Citation patterns

### Case law
- **ECLI (EU)**: `ECLI:EU:C:2020:559` (Court of Justice), `ECLI:EU:T:2019:...` (General Court).
- **ECLI (national)**: `ECLI:NL:HR:2021:...`, `ECLI:DE:BGH:...`, `ECLI:PL:SN:...`.
- **Case names / numbers**: `Party v Party`; CJEU case numbers `C-123/20`, `C-123/20 P` (appeal),
  joined cases `C-123/20 and C-124/20`; General Court `T-456/19`.

### EU legislation
- **CELEX**: `32016R0679`, `32019L0790` (sector + year + type + number).
- **Named acts**: `Regulation (EU) 2016/679`, `Directive 2019/790`, `Regulation (EC) No 1/2003`.
- **Official Journal**: `OJ L 119`, `OJ C 326`.

### Provisions
- `Article 5(1)(a) GDPR`, `Art. 263 TFEU`, `section 12`, `§ 3(2)`.

## Aggregation - short references (antecedents)

Resolve to the full citation given earlier: `ibid.`, `id.`, `supra`, `op. cit.`, `the cited
judgment`, `the above-cited`, `loc. cit.`. Each points to the nearest matching antecedent in the
text - count it as the same citation, but keep where it occurs.

## Output format

```
CITATIONS FOUND (n):
| # | Type | Citation (normalised) | Occurrences (offset/page) | Antecedent (if short ref) |
| 1 | EU case law | C-311/18 (Schrems II) | p.3, p.7 (ibid.) | - |
| 2 | EU legislation | Regulation (EU) 2016/679 | p.2 | - |
| 3 | provision | Article 5(1)(a) GDPR | p.4 | - |

TO VERIFY: pass the "Citation" column to grounding; EU sources to eu-sparql-search.
```

## Limits

- Extraction catches references in a known format. A descriptive reference with no identifier ("the
  Court's data-protection case law") has nothing to match - mark it "no identifier, manual check".
- This is not existence verification - it says what is cited, not whether the citation is real.
- Patterns cover the common EU/ECLI formats; an unusual citation style may slip - at high stakes,
  review by hand as well.

## Attribution

The extraction -> aggregation -> annotation architecture is based on **eyecite** (Free Law Project),
**BSD-2-Clause**. US reporter regexes dropped; ECLI, CELEX/OJ and EU-citation patterns and the
antecedent rules are MateMatic's own. MateMatic interpretation, not the position of any bar or regulator.
