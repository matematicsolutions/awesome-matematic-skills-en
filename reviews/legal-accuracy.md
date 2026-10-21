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
- Art. 35(4) - FIXED then ok - the supervisory authority "shall establish and make public a list of the kind of processing operations which are subject to the requirement for a data protection impact assessment pursuant to paragraph 1". The skill had called these lists of operations "always requiring a DPIA"; checking the Polish twin against the Polish list (Komunikat Prezesa UODO of 17 June 2019, M.P. 2019 poz. 666, read via Repertorium eli:MP/2019/666 on 2026-10-10) showed a criteria list where a DPIA is required "as a rule" when at least two criteria are met and sometimes one, with examples that are "only illustrative". The skill now says to read each national list on its own terms and cites the Polish one as the example. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 35(7) - ok - "at least" (a) systematic description and purposes incl., where applicable, the legitimate interest, (b) necessity and proportionality, (c) risks to rights and freedoms, (d) measures incl. safeguards and mechanisms to demonstrate compliance. The skill's detail under (b) (minimisation, legal basis, retention...) is elaboration, not a claim about the article's wording. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 35(9) - ok - "where appropriate", the views of data subjects or their representatives; condition and representatives added. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 36 - ok - prior consultation; heading and scope match. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- Art. 36(1) - ok with attribution - text: consult "where a data protection impact assessment ... indicates that the processing would result in a high risk in the absence of measures taken by the controller to mitigate the risk". The skill's "residual risk remains high" is WP248's reading ("Whenever the data controller cannot find sufficient measures to reduce the risks to an acceptable level (i.e. the residual risks are still high), consultation with the supervisory authority is required"); the skill now attributes it to WP248. EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present); WP29 WP248 rev.01 (adopted 4 April 2017, revised 4 October 2017), PDF from ec.europa.eu, full text read 2026-10-10.
- Art. 36(3) - ok - content of the consultation request (a)-(f), cited only as "scope per Art. 36(3)". EUR-Lex CELEX:32016R0679 (EN HTML, fetched 2026-10-10, all 99 articles present).
- WP248 - FIXED then ok - nine criteria confirmed (evaluation or scoring; automated decision-making with legal or similar significant effect; systematic monitoring; sensitive or highly personal data; large scale; matching or combining datasets; vulnerable data subjects incl. children and employees; innovative use or new technological or organisational solutions; processing that prevents exercising a right or using a service or contract). Rule: "In most cases ... meeting two criteria would require a DPIA", and "in some cases ... only one". Fixed: the skill and script attributed WP248 to the EDPB (it is an Article 29 Working Party document); the ">=2" rule now says "in most cases"; criterion 8's examples are now WP248's own (combined fingerprint and face recognition, Internet of Things) instead of an added "AI". The script's verdict logic (one criterion = recommended, two or more = required) matches. WP29 WP248 rev.01 (adopted 4 April 2017, revised 4 October 2017), PDF from ec.europa.eu, full text read 2026-10-10.
- Article 29 - ok - not a statutory unit: "Article 29 Working Party", the author of WP248 (title page of WP248 rev.01). WP29 WP248 rev.01 (adopted 4 April 2017, revised 4 October 2017), PDF from ec.europa.eu, full text read 2026-10-10.

## eu-ai-act-triage-en

Reviewed 2026-10-19 (Regulation (EU) 2026/1744 "Digital Omnibus on AI" amending Regulation (EU) 2024/1689; every unit in the changed lines read in the amending act and in the consolidated text). Sources: A = CELEX 32026R1744, EN XHTML from Cellar, fetched 2026-10-19 (Article 1 points (1)-(43) present); C = consolidated CELEX 02024R1689-20260727, EN XHTML from Cellar, fetched 2026-10-19. Cellar lists 32026R1744 as the only act amending 32024R1689 (SPARQL, cdm:resource_legal_amends_resource_legal, 2026-10-19).

- Regulation (EU) 2026/1744 - ok - title "of 8 July 2026 amending Regulations (EU) 2024/1689, (EU) 2018/1139 ..."; entry into force on the third day after publication (A, final article). The skill now tells step 0 to use the consolidated text.
- Art. 113 - FIXED then ok - general date "It shall apply from 2 August 2026"; (a) Chapters I and II from 2 February 2025 except Art. 5(1)(ba),(bb) and 5(1a),(1b) from 2 December 2026; (c) Chapter III Sections 1-3 (except 6(5)) from 2 December 2027 for Art. 6(2)/Annex III and 2 August 2028 for Art. 6(1)/Annex I; (d) Articles 102-110 from 27 July 2026 (A point (40); C Art. 113). The skill had Annex III from 2 August 2026 and Annex I until 2 August 2027.
- Art. 4 - FIXED then ok - replaced: providers and deployers "shall take measures to support the development of AI literacy"; "does not require ... to guarantee any specific level" (A point (5)). Still applies from 2 February 2025 (Chapter I).
- Art. 5(1) - ok - new points (ba) intimate images of an identifiable person without explicit consent and (bb) material within Art. 2(c) and (e) of Directive 2011/93/EU, except a "without right" defence (A point (7)(a)).
- Art. 5(1a) - ok - placing on the market prohibited only where the generation is the intended purpose or a foreseeable and reproducible outcome without adequate safeguards; use only where the deployer uses it for that purpose; 5(1b) excludes manipulation that does not increase exposure (A point (7)(b)).
- Art. 3(14) - FIXED then ok - "safety component" redefined: fulfils a safety function or its failure endangers health and safety of persons or property (A point (4)(a)).
- Art. 6(1) - ok - Path A reference; unchanged paragraph, read in C.
- Art. 6(1)(b) - ok - the third-party conformity assessment condition, referenced by the new 6(1c) (A point (8)).
- Art. 6(1a) - ok - user assistance, performance optimisation, efficiency, automation, convenience or quality control are not safety components; 6(1b) unless failure endangers health and safety (A point (8)).
- Art. 6(1c) - ok - third-party assessment required solely for risks other than health and safety (e.g. radio spectrum, electromagnetic interference) does not meet 6(1)(b) (A point (8)).
- Art. 6(2) - ok - Path B / Annex III reference in the timeline; matches Art. 113(c)(i) (C).
- Art. 2(2) - FIXED then ok - Section B of Annex I: "only Article 6(1), Article 60a and Articles 102 to 112 shall apply"; Articles 57-59 only in so far as the requirements are integrated (C Art. 2(2), marker M1). Was [TO VERIFY].
- Regulation (EU) 2023/1230 - ok - added to Annex I Section B as point 21; Section A point 1 (Directive 2006/42/EC) deleted (A point (41); C Annex I Section A shows point 1 removed).
- Art. 50 - ok - Chapter IV, not among the Art. 113 exceptions, so it applies from the general date 2 August 2026 (C Art. 113).
- Art. 50(2) - ok - transitional rule for synthetic-content systems placed on the market before 2 August 2026: comply by 2 December 2026 (A point (39)(b), new Art. 111(4)).
- Art. 111(2) - ok - public-authority high-risk systems on the market before the Chapter III date: comply by 2 August 2030 (A point (39)(a)).
- Art. 111(4) - ok - see Art. 50(2) (A point (39)(b)).
- Art. 27(4) - ok - FRIA may cross-reference or include parts of the DPIA under Art. 35 GDPR or Art. 27 of Directive (EU) 2016/680 (A point (13)(a)).
- Art. 35 - ok - GDPR Art. 35 (DPIA), as named in the new Art. 27(4) (A point (13)(a)).
- Art. 60a - ok - named in Art. 2(2) as applying to Section B acts (C Art. 2(2)); the skill only names it, no claim on content.

Reviewed 2026-10-21 (1.2.0: mirror of the CodeRabbit fixes made in the mike-workflows fork, branch `fix/eu-ai-governance-coderabbit`, EU AI Governance Pack PR #18; every unit in the changed lines re-read, full denominator 39). Source: C2 = consolidated CELEX 02024R1689-20260727, EN XHTML from Cellar (publications.europa.eu/resource/celex), fetched 2026-10-21; ▼M1 markers read as the 2026/1744 amendments.

- Regulation (EU) 2026/1744 - ok - step 0 now names the consolidated version 02024R1689-20260727 as the verification text and forbids verifying against the 2024 original; C2 carries ▼M1 markers in Art. 2 (paragraphs 2, 7, 13), Art. 4, Art. 4a, Art. 5, Art. 25(2), Art. 50(7), Art. 111, Art. 113, so "among others Articles 2 ... and added Article 4a" holds. No later consolidated version checked in this pass - the skill tells the user to check.
- Article 2 - ok - in the AI Act section of step 0: Art. 2 is amended (▼M1 in C2 Art. 2(2), (7), (13)). In step 2 the same token is "Article 2, points (c) and (e), of Directive 2011/93/EU", reproduced verbatim from C2 Art. 5(1)(bb); the content of Directive 2011/93/EU itself was not read.
- Article 4a - ok - C2 Art. 4a "Processing of special categories of personal data for bias detection and correction", ▼M1 (added by 2026/1744). The skill only says it was added.
- Art. 2 - ok - step 0a heading "scope gate (Art. 2)"; C2 Art. 2 "Scope".
- Art. 2(1) - ok - seven limbs (a)-(g) in C2: providers in or outside the Union; deployers established or located in the Union; third-country providers and deployers where the output is used in the Union; importers and distributors; product manufacturers with their product under their own name or trademark; authorised representatives of non-Union providers; affected persons located in the Union. All seven on the skill's list.
- Art. 2(3) - ok - C2: not applicable to areas outside the scope of Union law; not applicable to AI systems used exclusively for military, defence or national security purposes.
- Art. 2(4) - ok - C2: third-country public authorities and international organisations using AI in international cooperation or agreements for law enforcement and judicial cooperation, "provided that" adequate safeguards for fundamental rights are given. The skill keeps the safeguards condition.
- Art. 2(6) - ok - C2: AI systems or models, including their output, "specifically developed and put into service for the sole purpose of scientific research and development".
- Art. 2(8) - ok - C2: research, testing or development before placing on the market or putting into service; "Testing in real world conditions shall not be covered by that exclusion".
- Art. 2(10) - FIXED then ok - C2: "does not apply to obligations of deployers who are natural persons using AI systems in the course of a purely personal non-professional activity". The fork text said "natural persons using AI"; mirrored as "obligations of deployers who are natural persons", which is what the paragraph excludes.
- Art. 2(12) - ok - C2: free and open-source licences excluded "unless they are placed on the market or put into service as high-risk AI systems or as an AI system that falls under Article 5 or 50".
- Art. 3 - ok - definitions, named in step 6 ("Definitions in Art. 3"); no claim on a specific point.
- Art. 3(1) - ok - unchanged claim (AI-system definition), line only re-wrapped in the description.
- Art. 4 - FIXED then ok - C2 Art. 4(1): measures to support AI literacy "of their staff and other persons dealing with the operation and use of AI systems on their behalf"; "does not require ... to guarantee any specific level". The skill had only "their staff"; now both groups.
- Art. 5 - ok - heading of step 2 and the Art. 5 tokens in step 6 and the description; C2 Art. 5 "Prohibited AI practices".
- Art. 5(1) - ok - extracted from "Art. 5(1)(ba)" and "(bb)": C2 (ba) realistic images, videos, audio or similar material of an identifiable natural person's intimate parts or of an identifiable person engaged in sexually explicit activities, without "freely-given, specific, informed, unambiguous and explicit consent"; (bb) material or performance within Art. 2(c) and (e) of Directive 2011/93/EU, "except where a 'without right' defence applies under national law". Both now quoted element by element; the earlier "child sexual abuse material" label and "explicit consent" alone were shortcuts.
- Art. 5(1)(a) - ok - C2: subliminal techniques beyond a person's consciousness or purposefully manipulative or deceptive techniques, objective or effect of materially distorting behaviour by appreciably impairing the ability to make an informed decision, causing or reasonably likely to cause significant harm. The skill lists every element.
- Art. 5(1)(b) - ok - C2: exploits vulnerabilities due to age, disability or a specific social or economic situation, objective or effect of materially distorting behaviour, causing or reasonably likely to cause significant harm.
- Art. 5(1a) - ok - C2 ▼M1: applies "for the purposes of paragraph 1, first subparagraph, points (ba) and (bb)"; applies from 2 December 2026 per C2 Art. 113(a).
- Art. 5(1a)(a) - FIXED then ok - C2: placing on the market or putting into service prohibited only where (i) the generation is the intended purpose, or (ii) design, training, architecture, capabilities or user-facing functionalities make it a reasonably foreseeable and reproducible outcome without significant technical modification, and the system lacks reasonable and adequate technical safety measures and other safeguards, taking into account reasonably foreseeable misuse, "and to correct observed or reported misuse". FIXED then ok: the fork text dropped the correction limb, which would let a system with prevention measures but no correction measures look compliant; the mirror carries it. The mike-workflows fork still lacks it - flagged in the hand-over.
- Art. 5(1a)(b) - ok - C2: use prohibited only where the deployer uses the system for the purpose of generating or manipulating such material or performance.
- Art. 5(1b) - FIXED then ok - C2: "For the purposes of paragraph 1, first subparagraph, point (ba)", manipulation that does not increase the exposure of any depicted intimate parts or alter the nature of any depicted sexually explicit activities is not manipulation. The fork text applied it to "these points" (ba and bb); the mirror limits it to point (ba). The mike-workflows fork still carries "these points" - flagged in the hand-over.
- Art. 6 - ok - description token (Art. 6 plus Annexes I and III), unchanged claim.
- Art. 6(1) - ok - Annex I path; C2 Art. 113(c)(ii) and Art. 27(1) both tie the Annex I route to Art. 6(1).
- Art. 6(2) - ok - Annex III path; C2 Art. 27(1) "high-risk AI system referred to in Article 6(2)".
- Art. 25 - ok - heading of step 6 and the card field.
- Art. 25(1) - ok - C2: "Any distributor, importer, deployer or other third-party" becomes the provider under (a) name or trademark on a high-risk AI system already placed on the market or put into service, "without prejudice to contractual arrangements stipulating that the obligations are otherwise allocated"; (b) substantial modification of a high-risk system that remains high-risk; (c) modification of the intended purpose so that a system becomes high-risk.
- Art. 25(2) - ok - C2 ▼M1: the initial provider "shall no longer be considered to be a provider of that specific AI system" and "shall closely cooperate with new providers"; the cooperation duty does not apply where the initial provider clearly specified the system is not to be changed into a high-risk system. The skill states the main rule only; the carve-out is not claimed away.
- Art. 25(3) - ok - C2: high-risk AI systems that are safety components of products under Annex I Section A; the product manufacturer is the provider where (a) placed on the market together with the product under its name or trademark, or (b) put into service under its name or trademark after the product has been placed on the market.
- Art. 27 - ok - card heading "FRIA (Art. 27)".
- Art. 27(1) - FIXED then ok - C2: "Prior to deploying a high-risk AI system referred to in Article 6(2), with the exception of high-risk AI systems intended to be used in the area listed in point 2 of Annex III, deployers that are bodies governed by public law, or are private entities providing public services, and deployers of high-risk AI systems referred to in points 5 (b) and (c) of Annex III". The skill had no Art. 6(2) condition and no point 2 exclusion, and "letters [TO VERIFY]". Annex III point 5(b) (creditworthiness / credit score, except detecting financial fraud) and 5(c) (risk assessment and pricing in life and health insurance) read in C2 Annex III.
- Art. 27(4) - ok - now also names Art. 27 of Directive (EU) 2016/680 next to the GDPR DPIA, as in the 2026-10-19 entry above.
- Art. 35 - ok - GDPR Art. 35, unchanged reference.
- Directive (EU) 2016/680 - ok - named in C2 Art. 27(4) as the second assessment that can be reused.
- Art. 50 - FIXED then ok - C2 Art. 50(1)-(4), exceptions now listed per row: (1) obvious to a reasonably well-informed, observant and circumspect person; systems authorised by law for criminal offences unless available for the public to report a criminal offence; (2) assistive function for standard editing, or no substantial alteration of the input data or its semantics, or authorised by law for criminal offences; (3) biometric categorisation and emotion recognition permitted by law to detect, prevent or investigate criminal offences; (4) deep fakes - authorised by law for criminal offences; evidently artistic, creative, satirical, fictional or analogous work limited to disclosing the existence of the content; (4) second subparagraph, text on matters of public interest - authorised by law, or human review or editorial control "and where" a natural or legal person holds editorial responsibility (both conditions). The skill had "unless the content underwent human editorial control" - one condition of two.
- Art. 50(2) - ok - transitional rule unchanged (Art. 111(4)).
- Art. 78 - ok - C2 Art. 113(b): "Chapter III Section 4, Chapter V, Chapter VII and Chapter XII and Article 78 shall apply from 2 August 2025, with the exception of Article 101"; C2 Art. 78 "Confidentiality"; Chapter III Section 4 "Notifying authorities and notified bodies".
- Art. 101 - FIXED then ok - C2 Art. 101 "Fines for providers of general-purpose AI models"; excepted from Art. 113(b), so it applies from the general date 2 August 2026. The skill said "since 2 August 2025: GPAI, governance, penalties" with no exception.
- Art. 111(4) - ok - now cited next to the 2 December 2026 Art. 50(2) row; unchanged content.

## nis2-compliance-triage-en

Reviewed 2026-10-19 (Step 0 transposition facts only; the rest of the skill unchanged in this pass).

- art. 49 - ok - Polish amending act of 23 January 2026 (Dz.U. 2026 poz. 252), art. 49: "Ustawa wchodzi w życie po upływie miesiąca od dnia ogłoszenia"; act status in force. Read in Repertorium `eli:DU/2026/252` (Sejm ELI source), text offset 320000-321500, 2026-10-19. Entry into force 2026-04-03 per ISAP (api.sejm.gov.pl/eli/acts/DU/2026/252, field entryIntoForce; promulgation 2026-03-02), checked 2026-10-19 - added to the skill in a second pass.
- Directive (EU) 2022/2555 - ok - no amending act in Cellar (SPARQL cdm:resource_legal_amends_resource_legal on CELEX 32022L2555 returned nothing; only corrigenda R(01)-R(09) and consolidated 02022L2555-20221227), 2026-10-19. Commission proposal 52026PC0013 of 2026-01-20 ("amending Directive (EU) 2022/2555 as regards simplification measures") found as a proposal (COM document, no adopted act).

Reviewed 2026-10-21 (1.1.0: mirror of the CodeRabbit fixes made in the mike-workflows fork, branch `fix/eu-ai-governance-coderabbit`, EU AI Governance Pack PR #18; full denominator 32). Sources: D = Directive (EU) 2022/2555, CELEX 32022L2555, EN XHTML from Cellar, fetched 2026-10-21; R = Commission Recommendation 2003/361/EC, CELEX 32003H0361, EN HTML from EUR-Lex, fetched 2026-10-21 (Annex, Title I).

- Art. 26 - FIXED then ok - D Art. 26 "Jurisdiction and territoriality". The skill had "main establishment rule for digital infrastructure and digital providers - verify against Art. 26 [TO VERIFY]"; the rule covers only the closed list in 26(1)(b), so "digital infrastructure" was too wide (IXPs, trust service providers and electronic communications providers are not on that list).
- Art. 26(1) - ok - D: default jurisdiction is the member state where the entity is established, except (a)-(c).
- Art. 26(1)(a) - ok - D: providers of public electronic communications networks or publicly available electronic communications services - the member state in which they provide their services.
- Art. 26(1)(b) - ok - D: DNS service providers, TLD name registries, entities providing domain name registration services, cloud computing, data centre, content delivery network, managed service and managed security service providers, providers of online marketplaces, online search engines and social networking services platforms - main establishment under paragraph 2. The table lists all eleven.
- Art. 26(1)(c) - ok - D: public administration entities - the member state which established them.
- Art. 26(2) - ok - D: where cybersecurity risk-management decisions are predominantly taken; if undeterminable or not in the Union, where cybersecurity operations are carried out; if still undeterminable, the establishment with the highest number of employees in the Union.
- Art. 26(3) - ok - D: a 26(1)(b) entity not established in the Union but offering services within it "shall designate a representative in the Union".
- Art. 2(1) - FIXED then ok - D: entities of a type in Annex I or II "which qualify as medium-sized enterprises under Article 2 of the Annex to Recommendation 2003/361/EC, or exceed the ceilings for medium-sized enterprises provided for in paragraph 1 of that Article"; second subparagraph: "Article 3(4) of the Annex to that Recommendation shall not apply". The skill had "50+ employees, or annual turnover / balance sheet above EUR 10 million", which reads the financial test as either figure; R requires both to exceed EUR 10 million (see Article 2 below).
- Article 2 - FIXED then ok - R Annex Art. 2: SME = fewer than 250 persons and turnover not exceeding EUR 50 million "and/or" balance sheet not exceeding EUR 43 million; small = fewer than 50 persons and turnover "and/or" balance sheet not exceeding EUR 10 million. Because of "and/or", an entity leaves a category only when headcount is over OR both financial figures are over. The skill's derived test (at least medium: 50+ persons, or turnover AND balance sheet over EUR 10 million; over medium: 250+ persons, or turnover over EUR 50 million AND balance sheet over EUR 43 million) matches.
- Article 3(4) - ok - R Annex Art. 3(4): not an SME if 25% or more of capital or voting rights is controlled by public bodies; disapplied for NIS2 by D Art. 2(1) second subparagraph.
- Article 4(2) - ok - R Annex Art. 4(2): status changes only if the ceilings are exceeded "over two consecutive accounting periods".
- Aggregation (R Annex Art. 6(2), recital 16) - ok - R Annex Art. 6(2): partner enterprises immediately upstream or downstream added "proportional to the percentage interest in the capital or voting rights (whichever is greater)"; linked enterprises 100%. The mirror adds "whichever is greater", which the fork text omits. D recital 16: member states "are able to take into account the degree of independence an entity enjoys in relation to its partner or linked enterprises when applying Article 6(2) of the Annex". Not an extracted unit; recorded for completeness.
- Art. 2(2) - FIXED then ok - D: regardless of size, entities of a type in Annex I or II where (a) services are provided by (i) public electronic communications providers, (ii) trust service providers, (iii) TLD name registries and DNS service providers; (b) sole provider in a member state of an essential service; (c) disruption could significantly impact public safety, public security or public health; (d) significant systemic risk, in particular cross-border; (e) critical at national or regional level; (f) public administration entity of central government, or regional after a risk-based assessment. The skill had dropped the "entity of a type in Annex I or II" condition and merged (c) and (d).
- Art. 2(2)(b) - ok - as above; cited in Step 3 as "Art. 2(2)(b) to (e)" for member-state identification, matching D Art. 3(1)(e) and 3(2).
- Art. 2(2)(f) - ok - D 2(2)(f)(i) central government; (ii) regional level following a risk-based assessment.
- Art. 2(3) - ok - D: "Regardless of their size, this Directive applies to entities identified as critical entities under Directive (EU) 2022/2557".
- Directive (EU) 2022/2557 - ok - the CER Directive, as named in D Art. 2(3) and 3(1)(f).
- Art. 2(4) - FIXED then ok - D: "Regardless of their size, this Directive applies to entities providing domain name registration services" - no Annex I/II condition, so an independent path. The skill did not list it.
- Art. 2(5) - ok - D: member states may provide for the directive to apply to (a) public administration entities at local level, (b) education institutions, in particular where they carry out critical research activities.
- Art. 3(1) - FIXED then ok - D Art. 3(1) points (a)-(g) now listed one by one with the deciding path recorded on the card; the skill had an "indicative" summary without (d) central-government public administration and (g) NIS1 operators of essential services.
- Art. 3(1)(a) - ok - D: Annex I entities which exceed the ceilings for medium-sized enterprises.
- Art. 3(1)(b) - ok - D: qualified trust service providers, TLD name registries and DNS service providers, regardless of size.
- Art. 3(1)(c) - ok - D: public electronic communications providers "which qualify as medium-sized enterprises".
- Art. 3(1)(d) - ok - D: public administration entities referred to in Art. 2(2)(f)(i).
- Art. 3(1)(e) - ok - D: other Annex I or II entities identified by a member state as essential pursuant to Art. 2(2)(b) to (e).
- Art. 3(1)(f) - ok - D: critical entities under Directive (EU) 2022/2557 referred to in Art. 2(3).
- Art. 3(1)(g) - ok - D: "if the Member State so provides", entities identified before 16 January 2023 as operators of essential services under Directive (EU) 2016/1148 or national law.
- Art. 3(2) - ok - D: Annex I or II entities not qualifying as essential are important, including those identified as important under Art. 2(2)(b) to (e). "Non-qualified trust service providers" follows: they are Annex I entities not listed in 3(1)(b).
- Art. 4 - FIXED then ok - D Art. 4(1): where sector-specific Union acts require risk-management measures or significant-incident notification "at least equivalent in effect", the relevant provisions of the directive, "including the provisions on supervision and enforcement laid down in Chapter VII, shall not apply to such entities"; Art. 4(2) sets the equivalence test. The skill had no Art. 4 pre-check. (Note: the gate counts this unit as covered by the existing "art. 49" line - a substring match; this explicit entry is the real coverage.)
- Art. 21 - ok - heading token; the measures list itself unchanged.
- Art. 21(2) - ok - unchanged ten-measure list; heading re-worded only.
- Art. 23 - ok - heading token "significant incident reporting (Art. 23)".
- Art. 23(4) - FIXED then ok - D 23(4)(a) "without undue delay and in any event within 24 hours of becoming aware" (early warning); (b) "without undue delay and in any event within 72 hours" (incident notification); (d) final report "not later than one month after the submission of the incident notification under point (b)"; final subparagraph: by way of derogation from point (b), a trust service provider notifies significant incidents affecting its trust services "without undue delay and in any event within 24 hours". The skill presented 24h/72h as the deadlines themselves and had no trust-service derogation; the card now counts the final report from submission of the notification.
- Art. 34 (ceilings scope) - FIXED then ok - D Art. 34(4) and (5): the EUR 10 000 000 / 2% and EUR 7 000 000 / 1.4% maxima apply "where they infringe Article 21 or 23", turnover "in the preceding financial year of the undertaking to which the ... entity belongs". The skill stated the ceilings without the Art. 21/23 scope. Not in the extracted list for this pass (the "Art. 34" token sits in an unchanged heading); recorded because the claim changed.


## privilege-preflight-en

Reviewed 2026-10-21 (1.1.0: mirror of the CodeRabbit fixes made in the mike-workflows fork, branch `fix/eu-ai-governance-coderabbit`, EU AI Governance Pack PR #18; full denominator 5). Source: G = Regulation (EU) 2016/679, CELEX 32016R0679, EN XHTML from Cellar, fetched 2026-10-21.

- Art. 4(1) - ok - definition of personal data; unchanged reference, re-read in G.
- Art. 4(7) - ok - G: controller "alone or jointly with others, determines the purposes and means of the processing of personal data". Used for the provider as independent controller.
- Art. 4(8) - ok - G: processor "processes personal data on behalf of the controller". Used for the provider acting on the firm's behalf.
- Art. 26 - ok - G Art. 26(1): "Where two or more controllers jointly determine the purposes and means of processing, they shall be joint controllers".
- Art. 28 - FIXED then ok - G Art. 28(1): "Where processing is to be carried out on behalf of a controller", the controller uses only processors with sufficient guarantees (the Art. 28(3) contract governs that processing); Art. 28(10): a processor that determines purposes and means "shall be considered to be a controller in respect of that processing". The skill presented the AI provider as a processor needing a DPA without classifying its role; processing for the provider's own purposes (training, product improvement) sits outside the Art. 28 contract.
