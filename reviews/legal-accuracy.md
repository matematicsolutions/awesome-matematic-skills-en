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

Reviewed 2026-10-10 (directory-readiness pass: all statutory units in the skill and its script, full denominator, checked against the source text; defects fixed in the same pass).

- Art. 12(3) - FIXED then ok - text: "without undue delay and in any event within one month of receipt"; extension "by two further months where necessary, taking into account the complexity and number of the requests", the person informed within one month "together with the reasons for the delay". The skill said "one month" without "without undue delay", and the script note said "for complexity" only; both now carry the full condition. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 12(4) - FIXED then ok - if no action is taken: inform "without delay and at the latest within one month of receipt" of the reasons, the complaint to a supervisory authority and a judicial remedy. The skill had the content but not the time limit; added. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 12(5) - ok - free of charge; where requests are "manifestly unfounded or excessive, in particular because of their repetitive character", a reasonable fee or refusal; the controller bears the burden of demonstrating it. "Reasonable" and the repetitive example added. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 17(3) - FIXED then ok - five exemptions (a) freedom of expression and information, (b) legal obligation / public task / official authority, (c) public health under Art. 9(2)(h),(i) and 9(3), (d) archiving, research, statistics under Art. 89(1), (e) legal claims. The table listed three, read as complete; now all five. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Regulation (EEC) No 1182/71 - ok - art. 3(2)(c): a period in months ends with the last hour of the day in the last month that falls on the same date as the start day; if that day does not exist, the last day of that month. The script's add_months matches (31 Jan -> 28/29 Feb, +3 months -> 30 Apr; run 2026-10-10). EUR-Lex CELEX:31971R1182 (EN HTML, fetched 2026-10-10, all 6 articles present).
- art. 3(4) - ok (stated limitation) - Regulation 1182/71 art. 3(4): a period expressed otherwise than in hours that ends on a public holiday, Sunday or Saturday ends with the last hour of the following working day. The script does not apply it; the skill and script now say so and that the result can only be earlier than the legal limit. EUR-Lex CELEX:31971R1182 (EN HTML, fetched 2026-10-10, all 6 articles present).

## gdpr-ropa-dpa-en

Reviewed 2026-08-07 (backport of codex flags from mike-workflows PR #16).

- Art. 30(2) - ok - processor register scope; field list rewritten to the full statutory enumeration.
- Art. 30(2)(a) - ok - names AND contact details of processor(s), each controller, applicable representatives and DPO; verified against GDPR text.
- Art. 30(5) - ok - exemption test; each disqualifier independent ("occasional", "risk", art. 9(1), art. 10).
- Art. 9(1) - ok - special categories reference as one 30(5) disqualifier.
- Art. 10 - ok - criminal convictions and offences data; separate 30(5) disqualifier previously missing - the codex flag that triggered this ledger.

Reviewed 2026-10-10 (directory-readiness pass: all statutory units in the skill and its script, full denominator, checked against the source text; defects fixed in the same pass).

- Art. 30(1) - FIXED then ok - the record "shall contain all of the following information" (a)-(g), but (e) is "where applicable" and (f), (g) are "where possible". The skill called all seven unconditional "mandatory fields"; now each carries its own condition. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 30(1)(a) - FIXED then ok - name and contact details of the controller and, where applicable, the joint controller, the controller's representative and the DPO. The representative was missing; added. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 49(1) - ok - Art. 30(1)(e) requires, for transfers under the second subparagraph of Art. 49(1), documentation of suitable safeguards; the skill now names exactly that case. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 32 - ok - security of processing; referenced as the content of 28(3)(c) ("takes all measures required pursuant to Article 32") and of 28(3)(f) (Arts 32-36). EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 32(1) - ok - Art. 30(1)(g) refers to "the technical and organisational security measures referred to in Article 32(1)"; the skill now cites 32(1). EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 28 - ok - "a DPA without them breaches Art. 28": Art. 28(3) requires the contract or other legal act and its listed content; a contract missing a mandatory stipulation does not meet Art. 28(3). EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 28(3) - FIXED then ok - first sentence: subject-matter and duration, nature and purpose, type of personal data and categories of data subjects "and the obligations and rights of the controller" - the last item was missing (skill and script note); added. (g) "at the choice of the controller", delete or return all data "and deletes existing copies unless Union or Member State law requires storage" - added. Second subparagraph: the processor "shall immediately inform the controller if, in its opinion, an instruction infringes" data protection law - added under (h). (b)-(f), (h) otherwise match. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 28(3)(a) - FIXED then ok - documented instructions incl. transfers, "unless required to do so by Union or Member State law", in which case the processor informs the controller first "unless that law prohibits such information on important grounds of public interest". The exception was missing; added. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).

## adversarial-legal-review-en

Review 2026-08-17 (v1.1.0 - port from the Polish twin: deterministic verdict function, UNCERTAIN as a first-class verdict, dissent panel).

- art. 12 - ok - AI Act (Regulation (EU) 2024/1689) art. 12(1): "High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system"; art. 12(2) ties logging to traceability of the system's functioning. The skill's claim: explicit weights and thresholds let an auditor reproduce the verdict from the numbers alone - record-keeping turned into arithmetic. Consistent. Verified at source: EUR-Lex CELEX:32024R1689 (consolidated HTML), 2026-08-17.
- Art. 6 - ok - appears only as the format example of a Verified tag, `(GDPR Art. 6)`, in the verification-foundation shared rules block (SHARED-RULES.md, copied into every skill 2026-10-06). Checked at source 2026-10-06 via Repertorium: celex:32016R0679:en, Article 6 "Lawfulness of processing", act in force, no known amendments, locator offset 168462-168702 (EUR-Lex CELEX:32016R0679). The example claims no legal content beyond the provision's existence and number.

## legal-request-router-en

Reviewed 2026-09-23 (new skill).

- Article 14 - ok with a scope caveat - AI Act art. 14 is headed "Human oversight"; verified 2026-09-23 against the consolidated text fetched from CELLAR (CELEX 32024R1689, `Accept: application/xhtml+xml`), not from memory. Paragraph 1 binds the duty to **high-risk** AI systems ("High-risk AI systems shall be designed and developed in such a way ... that they can be effectively overseen by natural persons"). The skill originally implied its routing trace satisfies art. 14; rewritten to state that the article covers high-risk systems, that classification is a separate question (`eu-ai-act-triage-en`), and that running the router discharges no obligation.
- Regulation (EU) 2024/1689 - ok - full title and number confirmed in the same CELLAR fetch (2026-09-23): Regulation (EU) 2024/1689 of the European Parliament and of the Council, the AI Act. Cited only to identify the instrument the scope caveat refers to; no substantive claim rests on it.
- Art. 6 - ok - appears only as the format example of a Verified tag, `(GDPR Art. 6)`, in the verification-foundation shared rules block (SHARED-RULES.md, copied into every skill 2026-10-06). Checked at source 2026-10-06 via Repertorium: celex:32016R0679:en, Article 6 "Lawfulness of processing", act in force, no known amendments, locator offset 168462-168702 (EUR-Lex CELEX:32016R0679). The example claims no legal content beyond the provision's existence and number.

## intake-sufficiency-en

Reviewed 2026-09-23 (new skill).

- Article 14 - ok with a scope caveat - same source and same check as above (CELEX 32024R1689 via CELLAR, 2026-09-23). Wording changed from "is part of human oversight under Article 14" to a plain statement that naming gaps keeps the decision with a person, plus an explicit note that art. 14 applies to high-risk systems and that this skill neither answers nor presumes that classification.
- Regulation (EU) 2024/1689 - ok - full title and number confirmed in the same CELLAR fetch (2026-09-23): Regulation (EU) 2024/1689 of the European Parliament and of the Council, the AI Act. Cited only to identify the instrument the scope caveat refers to; no substantive claim rests on it.

Note on method: EUR-Lex HTML document URLs returned an empty shell for this CELEX id, so the text was retrieved through the CELLAR content-negotiation endpoint instead. Recorded here because the same trap will recur on the next AI Act check.
- Art. 6 - ok - appears only as the format example of a Verified tag, `(GDPR Art. 6)`, in the verification-foundation shared rules block (SHARED-RULES.md, copied into every skill 2026-10-06). Checked at source 2026-10-06 via Repertorium: celex:32016R0679:en, Article 6 "Lawfulness of processing", act in force, no known amendments, locator offset 168462-168702 (EUR-Lex CELEX:32016R0679). The example claims no legal content beyond the provision's existence and number.

## citation-extraction-en

Reviewed 2026-10-06 (shared rules block added).

- Art. 6 - ok - appears only as the format example of a Verified tag, `(GDPR Art. 6)`, in the verification-foundation shared rules block (SHARED-RULES.md, copied into every skill 2026-10-06). Checked at source 2026-10-06 via Repertorium: celex:32016R0679:en, Article 6 "Lawfulness of processing", act in force, no known amendments, locator offset 168462-168702 (EUR-Lex CELEX:32016R0679). The example claims no legal content beyond the provision's existence and number.

## clause-checklist-en

Reviewed 2026-10-06 (shared rules block added).

- Art. 6 - ok - appears only as the format example of a Verified tag, `(GDPR Art. 6)`, in the verification-foundation shared rules block (SHARED-RULES.md, copied into every skill 2026-10-06). Checked at source 2026-10-06 via Repertorium: celex:32016R0679:en, Article 6 "Lawfulness of processing", act in force, no known amendments, locator offset 168462-168702 (EUR-Lex CELEX:32016R0679). The example claims no legal content beyond the provision's existence and number.

## deliverable-fidelity-en

Reviewed 2026-10-06 (shared rules block added).

- Art. 6 - ok - appears only as the format example of a Verified tag, `(GDPR Art. 6)`, in the verification-foundation shared rules block (SHARED-RULES.md, copied into every skill 2026-10-06). Checked at source 2026-10-06 via Repertorium: celex:32016R0679:en, Article 6 "Lawfulness of processing", act in force, no known amendments, locator offset 168462-168702 (EUR-Lex CELEX:32016R0679). The example claims no legal content beyond the provision's existence and number.

## judicial-first-impression-en

Reviewed 2026-10-06 (shared rules block added).

- Art. 6 - ok - appears only as the format example of a Verified tag, `(GDPR Art. 6)`, in the verification-foundation shared rules block (SHARED-RULES.md, copied into every skill 2026-10-06). Checked at source 2026-10-06 via Repertorium: celex:32016R0679:en, Article 6 "Lawfulness of processing", act in force, no known amendments, locator offset 168462-168702 (EUR-Lex CELEX:32016R0679). The example claims no legal content beyond the provision's existence and number.

## legal-syllogism-en

Reviewed 2026-10-06 (shared rules block added).

- Art. 6 - ok - appears only as the format example of a Verified tag, `(GDPR Art. 6)`, in the verification-foundation shared rules block (SHARED-RULES.md, copied into every skill 2026-10-06). Checked at source 2026-10-06 via Repertorium: celex:32016R0679:en, Article 6 "Lawfulness of processing", act in force, no known amendments, locator offset 168462-168702 (EUR-Lex CELEX:32016R0679). The example claims no legal content beyond the provision's existence and number.

## opposing-counsel-attack-en

Reviewed 2026-10-06 (shared rules block added).

- Art. 6 - ok - appears only as the format example of a Verified tag, `(GDPR Art. 6)`, in the verification-foundation shared rules block (SHARED-RULES.md, copied into every skill 2026-10-06). Checked at source 2026-10-06 via Repertorium: celex:32016R0679:en, Article 6 "Lawfulness of processing", act in force, no known amendments, locator offset 168462-168702 (EUR-Lex CELEX:32016R0679). The example claims no legal content beyond the provision's existence and number.

## output-scoring-en

Reviewed 2026-10-06 (shared rules block added).

- Art. 6 - ok - appears only as the format example of a Verified tag, `(GDPR Art. 6)`, in the verification-foundation shared rules block (SHARED-RULES.md, copied into every skill 2026-10-06). Checked at source 2026-10-06 via Repertorium: celex:32016R0679:en, Article 6 "Lawfulness of processing", act in force, no known amendments, locator offset 168462-168702 (EUR-Lex CELEX:32016R0679). The example claims no legal content beyond the provision's existence and number.

## gdpr-breach-72h-en

Reviewed 2026-10-10 (directory-readiness pass: all statutory units in the skill and its script, full denominator, checked against the source text; defects fixed in the same pass).

- Art. 4(12) - ok - definition: "a breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, personal data transmitted, stored or otherwise processed"; the skill's wording and its confidentiality/integrity/availability split (from the EDPB guidelines) match. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 33 - ok - notification to the supervisory authority; heading and scope match. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 33(1) - FIXED then ok - "without undue delay and, where feasible, not later than 72 hours after having become aware of it ... unless the personal data breach is unlikely to result in a risk"; late notification "shall be accompanied by reasons for the delay". The skill and script said "Deadline: 72 hours" unconditionally - a conditional duty written as a flat 72h target. Now: without undue delay, 72h as the outer limit. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 33(3) - FIXED then ok - "shall at least": (a) nature incl. "where possible" categories and approximate numbers of data subjects and records, (b) "name and contact details of the data protection officer or other contact point", (c) likely consequences, (d) measures taken or proposed incl. "where appropriate" mitigation. The skill had "DPO contact" (no other contact point, so a controller without a DPO had no field) and dropped "where possible"; both fixed. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 33(4) - ok - information "may be provided in phases without undue further delay" where not possible at the same time; "without undue further delay" added. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 33(5) - ok - document any breach: facts, effects, remedial action, so the authority can verify compliance - matches "record EVERY breach (even unreported ones)". EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 34 - ok - communication to the data subject where the breach is "likely to result in a high risk", "without undue delay". EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 34(2) - ok - clear and plain language, the nature of the breach and at least the information in Art. 33(3)(b), (c), (d) - so "DPO or other contact point", as now written. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 34(3) - FIXED then ok - (a) protection measures "applied to the personal data affected" (e.g. encryption), (b) subsequent measures ensuring the high risk "is no longer likely to materialise", (c) disproportionate effort - then "a public communication or similar measure whereby the data subjects are informed in an equally effective manner". Applied-to-the-affected-data and the equal-effectiveness condition added. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- EDPB Guidelines 9/2022 - FIXED then ok - section "B. Factors to consider when assessing risk" lists: type of breach; nature, sensitivity and volume; ease of identification; severity of consequences; special characteristics of the individual; special characteristics of the data controller (para. 117: "a medical organisation"); number of affected individuals; general points. The skill omitted the controller factor; added with the guidelines' own example. The guidelines describe themselves as the updated version of WP250 (rev.01). EDPB Guidelines 9/2022 v2.0 (adopted 28 March 2023), PDF from edpb.europa.eu, full text read 2026-10-10.
- WP250 - ok - named only as the predecessor of Guidelines 9/2022 ("updated version of the previous guidelines WP250 (rev.01)", version history of the EDPB document). EDPB Guidelines 9/2022 v2.0 (adopted 28 March 2023), PDF from edpb.europa.eu, full text read 2026-10-10.
- art. 3(1) - ok (stated limitation) - Regulation 1182/71 art. 3(1): where a period in hours runs from an event, "the hour during which that event occurs ... shall not be considered as falling within the period". The script computes awareness + 72h, which is never later than the limit counted this way; skill and script now say the result errs early. Whether 1182/71 governs GDPR periods is not asserted. EUR-Lex CELEX:31971R1182 (EN HTML, fetched 2026-10-10, all 6 articles present).

## gdpr-dpia-en

Reviewed 2026-10-10 (directory-readiness pass: all statutory units in the skill and its script, full denominator, checked against the source text; defects fixed in the same pass).

- Art. 35 - ok - data protection impact assessment; heading and scope match. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 35(1) - ok - where processing "is likely to result in a high risk", the controller carries out the assessment "prior to the processing"; "prior to the processing" added. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 35(2) - ok - the controller seeks the DPO's advice "where designated"; condition added. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 35(3) - FIXED then ok - (a) "a systematic and extensive evaluation of personal aspects ... based on automated processing, including profiling, and on which decisions are based that produce legal effects ... or similarly significantly affect"; (b) large-scale special categories under Art. 9(1) or criminal data under Art. 10; (c) "systematic monitoring of a publicly accessible area on a large scale". The skill and the script's label had (a) as "systematic and extensive evaluation (profiling)" - the decision-effects condition was missing, which over-triggers the mandatory case. Fixed in both. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 9(1) - ok - special categories, cited as the 35(3)(b) category. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 10 - ok - criminal convictions and offences, cited as the 35(3)(b) category. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 22 - ok - cited for WP248 criterion 2 ("automated-decision making with legal or similar significant effect"); WP248 itself refers to Art. 22 for criterion 9. WP29 WP248 rev.01 (adopted 4 April 2017, revised 4 October 2017), PDF from ec.europa.eu, full text read 2026-10-10.
- Art. 35(4) - ok - the supervisory authority "shall establish and make public a list" of processing operations subject to the DPIA requirement. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 35(7) - ok - "at least" (a) systematic description and purposes incl., where applicable, the legitimate interest, (b) necessity and proportionality, (c) risks to rights and freedoms, (d) measures incl. safeguards and mechanisms to demonstrate compliance. The skill's detail under (b) (minimisation, legal basis, retention...) is elaboration, not a claim about the article's wording. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 35(9) - ok - "where appropriate", the views of data subjects or their representatives; condition and representatives added. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 36 - ok - prior consultation; heading and scope match. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 36(1) - ok with attribution - text: consult "where a data protection impact assessment ... indicates that the processing would result in a high risk in the absence of measures taken by the controller to mitigate the risk". The skill's "residual risk remains high" is WP248's reading ("Whenever the data controller cannot find sufficient measures to reduce the risks to an acceptable level (i.e. the residual risks are still high), consultation with the supervisory authority is required"); the skill now attributes it to WP248. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present); WP29 WP248 rev.01 (adopted 4 April 2017, revised 4 October 2017), PDF from ec.europa.eu, full text read 2026-10-10.
- Art. 36(3) - ok - content of the consultation request (a)-(f), cited only as "scope per Art. 36(3)". EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- WP248 - FIXED then ok - nine criteria confirmed (evaluation or scoring; automated decision-making with legal or similar significant effect; systematic monitoring; sensitive or highly personal data; large scale; matching or combining datasets; vulnerable data subjects incl. children and employees; innovative use or new technological or organisational solutions; processing that prevents exercising a right or using a service or contract). Rule: "In most cases ... meeting two criteria would require a DPIA", and "in some cases ... only one". Fixed: the skill and script attributed WP248 to the EDPB (it is an Article 29 Working Party document); the ">=2" rule now says "in most cases"; criterion 8's examples are now WP248's own (combined fingerprint and face recognition, Internet of Things) instead of an added "AI". The script's verdict logic (one criterion = recommended, two or more = required) matches. WP29 WP248 rev.01 (adopted 4 April 2017, revised 4 October 2017), PDF from ec.europa.eu, full text read 2026-10-10.
- Article 29 - ok - not a statutory unit: "Article 29 Working Party", the author of WP248 (title page of WP248 rev.01). WP29 WP248 rev.01 (adopted 4 April 2017, revised 4 October 2017), PDF from ec.europa.eu, full text read 2026-10-10.
