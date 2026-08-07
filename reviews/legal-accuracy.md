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
