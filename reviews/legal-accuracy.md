# Legal-accuracy review ledger

Machine-checked by `scripts/legal-accuracy-gate.py`: every statutory unit
appearing in changed SKILL.md lines must be covered by a line in the matching
`## <skill-name>` section below. Coverage is the mechanical part; the verdict
on each line is the human/adversarial-review layer and must reflect a check
actually performed against the source text, not memory.

Entry format: `- <unit> - <verdict> - <how it was checked>`

## gdpr-dsar-en

Reviewed 2026-08-07 (backport of codex flags from mike-workflows PR #16).

- Art. 12(6) - ok - identity verification ground; GDPR text confirms it authorises requesting additional information, says nothing about unconditional suspension.
- EDPB Guidelines 01/2022 - ok - verified via EDPB source 2026-08-07: suspension only where the information is necessary AND requested without undue delay; guidelines adopted 18.01.2022.
- Art. 12(1) - ok - plain-language requirement for the response; unchanged claim, re-read against text.
- Art. 15 - ok - access right requires a copy of personal data undergoing processing (art. 15(3)); RoPA metadata alone is not a copy.
- Art. 15(1)(g) - ok - "any available information as to their source" where data not collected from the subject - hence "available source information", not an unconditional source list.

## gdpr-ropa-dpa-en

Reviewed 2026-08-07 (backport of codex flags from mike-workflows PR #16).

- Art. 30(2) - ok - processor register scope; field list rewritten to the full statutory enumeration.
- Art. 30(2)(a) - ok - names AND contact details of processor(s), each controller, applicable representatives and DPO; verified against GDPR text.
- Art. 30(5) - ok - exemption test; each disqualifier independent ("occasional", "risk", art. 9(1), art. 10).
- Art. 9(1) - ok - special categories reference as one 30(5) disqualifier.
- Art. 10 - ok - criminal convictions and offences data; separate 30(5) disqualifier previously missing - the codex flag that triggered this ledger.

## adversarial-legal-review-en

Review 2026-08-17 (v1.1.0 - port from the Polish twin: deterministic verdict function, UNCERTAIN as a first-class verdict, dissent panel).

- art. 12 - ok - AI Act (Regulation (EU) 2024/1689) art. 12(1): "High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system"; art. 12(2) ties logging to traceability of the system's functioning. The skill's claim: explicit weights and thresholds let an auditor reproduce the verdict from the numbers alone - record-keeping turned into arithmetic. Consistent. Verified at source: EUR-Lex CELEX:32024R1689 (consolidated HTML), 2026-08-17.

## legal-request-router-en

Reviewed 2026-09-23 (new skill).

- Article 14 - ok with a scope caveat - AI Act art. 14 is headed "Human oversight"; verified 2026-09-23 against the consolidated text fetched from CELLAR (CELEX 32024R1689, `Accept: application/xhtml+xml`), not from memory. Paragraph 1 binds the duty to **high-risk** AI systems ("High-risk AI systems shall be designed and developed in such a way ... that they can be effectively overseen by natural persons"). The skill originally implied its routing trace satisfies art. 14; rewritten to state that the article covers high-risk systems, that classification is a separate question (`eu-ai-act-triage-en`), and that running the router discharges no obligation.
- Regulation (EU) 2024/1689 - ok - full title and number confirmed in the same CELLAR fetch (2026-09-23): Regulation (EU) 2024/1689 of the European Parliament and of the Council, the AI Act. Cited only to identify the instrument the scope caveat refers to; no substantive claim rests on it.

## intake-sufficiency-en

Reviewed 2026-09-23 (new skill).

- Article 14 - ok with a scope caveat - same source and same check as above (CELEX 32024R1689 via CELLAR, 2026-09-23). Wording changed from "is part of human oversight under Article 14" to a plain statement that naming gaps keeps the decision with a person, plus an explicit note that art. 14 applies to high-risk systems and that this skill neither answers nor presumes that classification.
- Regulation (EU) 2024/1689 - ok - full title and number confirmed in the same CELLAR fetch (2026-09-23): Regulation (EU) 2024/1689 of the European Parliament and of the Council, the AI Act. Cited only to identify the instrument the scope caveat refers to; no substantive claim rests on it.

Note on method: EUR-Lex HTML document URLs returned an empty shell for this CELEX id, so the text was retrieved through the CELLAR content-negotiation endpoint instead. Recorded here because the same trap will recur on the next AI Act check.

