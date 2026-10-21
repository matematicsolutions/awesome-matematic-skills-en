# CHANGELOG

All notable changes to this hub are recorded here.
Format follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/).
Versioning: CalVer for the hub (`YYYY.MM.DD`), SemVer per skill.

## [2026.10.21b] - 2026-10-21

### Changed

- `eu-ai-act-triage-en`, `nis2-compliance-triage-en` (`ai-governance`): wording pass after an
  editorial review of the 2026.10.21 changes - negative parallelisms and a sentence describing the
  previous version replaced by plain rules; the Art. 23(4) clock no longer repeats "without undue
  delay" in capitals; the partner-enterprise aggregation states the cross-holdings rule
  (Recommendation 2003/361/EC, Annex Art. 6(2)). No change to any legal determination, so skill
  versions stay at 1.2.0 and 1.1.0.

## [2026.10.21] - 2026-10-21

### Fixed

Mirror of the fixes made in the mike-workflows fork after CodeRabbit reviewed the EU AI Governance
Pack (open-legal-products/mike-workflows PR #18, merged before the fixes; fork branch
`fix/eu-ai-governance-coderabbit`). Without this mirror the source and the upstream copy would
drift. Every changed unit re-read in the act text (`reviews/legal-accuracy.md`, 76/76).

- `eu-ai-act-triage-en` 1.2.0 (`ai-governance`): new step 0a, a scope gate on Art. 2 (the seven
  limbs of Art. 2(1) and the exclusions in Art. 2(3), (4), (6), (8), (10), (12)); step 0 verifies
  against the consolidated version 02024R1689-20260727, not the 2024 original, and lists Art. 2
  and the new Art. 4a among the 2026/1744 changes; Art. 5 points are recorded element by element
  (MET / NOT MET / UNKNOWN) with a decision rule, and (a), (b), (ba), (bb), 5(1a) and 5(1b) quote
  the statutory elements; each Art. 50 row carries its exceptions, including the two-condition
  editorial-responsibility exception; the product manufacturer is a role (Art. 2(1)(e), Art. 25(3))
  and Art. 25(1)-(2) are stated in full; the Art. 113 timeline separates Art. 5(1)(ba)/(bb) from
  Chapters I-II and Art. 101 from the 2025 block; the FRIA trigger in Art. 27(1) is two conditions
  (Art. 6(2) system, excluding Annex III point 2; deployer type or Annex III point 5(b)/(c)).
  Beyond the fork: Art. 5(1b) is limited to point (ba), Art. 5(1a)(a) keeps the "correct observed
  or reported misuse" limb, and Art. 2(10) excludes the obligations of personal-use deployers, as
  the consolidated text says.
- `nis2-compliance-triage-en` 1.1.0 (`ai-governance`): Art. 26 jurisdiction table (the
  main-establishment rule covers only the closed list in Art. 26(1)(b)); the size-cap test follows
  Recommendation 2003/361/EC (headcount OR both financial figures, aggregation, the Art. 3(4)
  public-ownership rule disapplied, two accounting periods); size-independent paths include the
  Art. 2(4) domain-registration path; Art. 3(1)(a)-(g) as ordered paths with the deciding path on
  the card; an Art. 4 pre-check for sector-specific Union acts; the Art. 23(4) deadlines are
  "without undue delay" outer limits, with the 24-hour notification for trust service providers;
  the Art. 34 ceilings are scoped to infringements of Art. 21 or 23. The verified Polish
  transposition in Step 0 (1.0.1-1.0.2) is unchanged.
- `privilege-preflight-en` 1.1.0 (`ai-governance`): the AI provider's GDPR role is classified
  (processor Art. 4(8), controller Art. 4(7), joint controller Art. 26), and an Art. 28 agreement
  covers only processing on the firm's behalf; SAFE now reads "no risk factor identified - human
  approval still required before sending" instead of "clear to send".

## [2026.10.19e] - 2026-10-19

### Added

- `scripts/wachta-zmian-aktow.mjs` + `seuranta/akty-zrodlowe.json` + monthly workflow
  `wachta-zmian-aktow.yml`: a watch for NEW amending acts of the source acts behind the skills -
  EU acts in Cellar (Publications Office SPARQL), Polish acts in ISAP. A new amendment fails the
  run and lists the skills that cite the act. Origin: Regulation (EU) 2026/1744 moved the AI Act
  deadlines in July 2026 and the AI Act skill kept the old dates for three months; nothing in the
  hub watched EU acts. Six acts at start (AI Act, NIS2, GDPR, DORA, CER, Polish KSC Act); red
  control: with the pre-July state the watch flags 32026R1744; an empty registry fails.

### Changed

- `nis2-compliance-triage-en` 1.0.2: the Polish KSC amendment entered into force on 3 April 2026
  (ISAP).

## [2026.10.19d] - 2026-10-19

### Changed

- `nis2-compliance-triage-en` 1.0.1 (`ai-governance`): Step 0 now states the verified Polish
  transposition - the Act of 23 January 2026 amending the KSC Act (Dz.U. 2026 item 252), in force
  per ISAP, entering into force one month after publication (its art. 49) - instead of
  "[TO VERIFY]", and notes that no act amending Directive (EU) 2022/2555 had been adopted as of
  2026-10-19 (Commission proposal COM(2026) 13 pending). The rule to re-check at the time of use
  stays.

## [2026.10.19c] - 2026-10-19

### Fixed

- `eu-ai-act-triage-en` 1.1.0 (`ai-governance`): updated to Regulation (EU) 2026/1744 of 8 July 2026
  (the "Digital Omnibus on AI"), which amended the AI Act. The skill still said that Annex III
  high-risk obligations apply from 2 August 2026 and Annex I obligations by 2 August 2027; the
  amended Art. 113 moves them to 2 December 2027 and 2 August 2028. Also carried into the skill: the
  new prohibitions in Art. 5(1)(ba) and (bb) from 2 December 2026, the replaced Art. 4 (AI literacy),
  the narrower "safety component" (Art. 3(14), Art. 6(1a)-(1c)), the machinery move from Annex I
  Section A to Section B with the Art. 2(2) regime, the Art. 50(2) and public-authority transitional
  rules (Art. 111(2) and (4)), and DPIA reuse in the FRIA (Art. 27(4)). Step 0 now points to the
  consolidated text. Every unit read in the amending act and the consolidated text
  (`reviews/legal-accuracy.md`).

### Added

- `eu-ai-act-triage-en`: freshness fields (`last_verified`, `freshness_window: 6 months`,
  `freshness_category: regulatory`, `verified_against`).

## [2026.10.19b] - 2026-10-19

### Fixed

- `eu-sparql-search` 1.1.0 (`eu-law-sources`): 10 of the 24 resource-type codes in
  `references/resource-types.md` did not exist in the Publications Office authority table, among
  them `ORDER_CJEU` and `CASELAW`, which SKILL.md listed as "most common". A query with a
  non-existent code returns an empty result, not an error, so the model could report that no such
  documents exist. Every code is now checked against the live SPARQL endpoint (2026-10-19), the
  wrong ones are replaced (`ORDER`, `OPIN_AG`, `DEC_FRAMW`, `PROP_REG` ...) or removed, and the
  reference shows the lookup query for any code not listed.
- `eu-sparql-search`: the advice to disable TLS verification on a certificate error is gone. It
  now says to retry, update the CA bundle, or stop and report the source as unreachable - without
  verification any network on the path can serve forged legislation text. The Polish hub had this
  fix; this hub did not.

### Added

- A `LICENSE` file in every skill directory (Apache-2.0 or MIT, as declared in the skill's
  `license:` field). Installers that check the licence of the fetched skill folder, such as the
  `legal-builder-hub` skill installer in restrictive mode, refuse a skill without one.
- `eu-sparql-search`: freshness fields (`last_verified`, `freshness_window`, `freshness_category`,
  `verified_against`) and a version.

### Changed

- `eu-sparql-search` and `authority-triage-en` 1.0.1: the description opens with when to use the
  skill and says what it is not for.

## [2026.10.19] - 2026-10-19

### Changed

- `reviewer-en` (`content-quality`): the description now opens with when to use it (typical
  requests such as "review my post" or "is this ready to publish"), says what it returns and what
  it is not for (code review, grammar-only proofreading, translation). The previous description
  relied on trigger words only we used ("reviewer?"), and the directory listing showed installs
  with no uses. Text sources reordered: pasted text first, then a named file, then `git diff HEAD`;
  before, a pasted text could lose to unrelated uncommitted changes in the repository.

## [2026.10.13] - 2026-10-13

### Changed

- `humanizer-en` 2.8.0 (`content-quality` 1.2.0) - minimal edits: it changes only what really
  grates and checks that the content survives the rewrite:
  - **inventory before rewriting** and a "What must not change" section: values, force of norms,
    certainty, reasons and conditions, who does what, legal and defined terms; "no change is a
    valid result";
  - **legal-register mode**: in contracts and pleadings defined terms, the passive voice in a
    statement of the legal position and numbered sub-clauses stay; the rest is pointed out, not
    rewritten;
  - **post-edit check `scripts/post_edit_audit.py`** (stdlib, no network): sensitive values,
    deontic profile, certainty, chat traces, protected and defined terms, shortening limit;
    OK/WARN/BLOCK with the full denominator; tests in `tests/`, each seen failing first;
  - "Personality and soul" no longer asks for opinions the author did not express, and the full
    example no longer invents a study, people or a percentage; its post-edit result is measured;
  - #7, #13 and #14 react to clusters, not single signals; #30-#34 as editing rules, without
    figures or promises about detectors.

## [2026.10.10] - 2026-10-10

### Fixed

- `data-protection`: every statutory reference in the four skills and their scripts (52 units)
  checked against the GDPR text on EUR-Lex, Regulation 1182/71, EDPB Guidelines 9/2022 and
  WP248 rev.01, and logged in `reviews/legal-accuracy.md`. Conditions that had been dropped are
  back: breach notification is "without undue delay and, where feasible, not later than 72 hours"
  (72h is the outer limit, not the target); a DSAR answer is due without undue delay and within one
  month at the latest; Art. 35(3)(a) requires decisions with legal or similarly significant effects,
  not profiling alone; the Art. 30(1) record items (e)-(g) carry their "where applicable / where
  possible" conditions. Lists that read as complete but were not are now complete: all five
  Art. 17(3) exemptions, the DPO "or other contact point", the controller's representative, the
  controller's obligations and rights in Art. 28(3), the legal-requirement exception in 28(3)(a),
  the copy-deletion and infringing-instruction duties, and the EDPB's controller risk factor.
- `gdpr-dpia-en`: WP248 is attributed to the Article 29 Working Party, not the EDPB; criterion 8
  uses WP248's own examples.
- The deadline calculator says what it computes: the outer limit, erring early, with Regulation
  1182/71 art. 3(1) and 3(4) named as not applied.

### Changed

- `data-protection` 1.1.0: `Bash` removed from `allowed-tools` in all four skills; Claude Code asks
  before running each calculator.

### Added

- `data-protection`: icon, Apache-2.0 `LICENSE`, `README.md` with a Data section, directory links
  in `plugin.json`.

## [2026.10.06] - 2026-10-06

### Fixed

- Shared rules now reach users. Claude Code does not load a `CLAUDE.md` placed at a plugin's
  root (stated by `claude plugin validate` and the Claude directory checks), so each bundle's
  safety rules never reached anyone - neither after `/plugin install` nor in a single-skill
  install. Each bundle's rules now live in `SHARED-RULES.md` and are copied into the end of
  every skill by `scripts/shared-rules-sync.py`, which also fails on any drift. 21 skills in
  5 bundles carry the block; `eu-multi-jurisdiction` ships connectors only and is pending.
- README and TRUST.md no longer claim that a plugin's `CLAUDE.md` carries its rules.
- `deliverable-fidelity-en`: `Bash` removed from `allowed-tools`; each command now asks the
  user first.

### Added

- `verification-foundation`: icon, Apache-2.0 `LICENSE`, `README.md` with a Data section,
  directory links in `plugin.json`.

### Changed

- `reviewer-en`: `allowed-tools` pre-approves only `git diff` and `git status` instead of any shell
  command. Reading files and pasted text works as before.

## [2026.09.23] - 2026-09-23

### Added

- `legal-request-router-en` 1.0.0 - triage for a legal request: classifies complexity, risk and
  audience, then returns an ordered verification path. Routes only to skills this hub actually
  ships, and states plainly what `privilege-preflight-en` does not do (it never performs the
  final redaction, and this hub ships no pseudonymisation engine).
- `intake-sufficiency-en` 1.0.0 - scores whether an instruction is complete enough to start on
  (six dimensions, 0-100), turns gaps into client-ready questions, and separates the client's
  legal premises from facts so an unverified premise cannot silently carry an analysis.
- `deliverable-fidelity-en` 1.0.0 - checks that the final document still carries what the
  analysis found. Bundled zero-dependency script for mechanical coverage, LLM spot-check for
  RED findings downgraded in tone, deterministic verdict from published weights. An omitted
  RED finding exits 1.

### Changed

- `verification-foundation` 1.1.0 to 1.2.0: seven skills to ten. README and marketplace counts
  updated (19 to 22 skills in the hub).

### Notes

The three skills are counterparts of Polish originals, rebuilt rather than translated. The
fidelity engine is the clearest case: the Polish script truncates word endings to absorb
inflection, which in English manufactures false matches ("clause" truncated to "clau" matches
"claustrophobia"). The English engine expands terms into surface forms instead. A false match
is the dangerous direction, because it silently passes an omitted RED finding.

## [2026.09.21c] - 2026-09-21

### Added

- `searchable-case-files-en` 0.1.2 - `--check`: environment check before work (Python, OCR library
  with a smoke test, Smart App Control read-only, language model, disk space), exit 0/10/20.
  Pattern from `doctor --smoke` in jerryjliu/docjev.

## [2026.09.21b] - 2026-09-21

### Fixed

- `searchable-case-files-en` 0.1.1 - shared code with the Polish twin: Polish report strings now
  carry diacritics; resuming a 0.1.0 output still recognises its unreadable-page marker.
  No change for English or Portuguese output.

## [2026.09.21] - 2026-09-21

### Added

- Plugin `documents` 1.0.0 with `searchable-case-files-en` 0.1.0 - a folder of case files,
  including scans, becomes text with page numbers, a local search tool and a report of
  unreadable pages and files with identical text under different names. Local OCR on the
  CPU (LiteParse, Apache-2.0). Twin of `akta-przeszukiwalne-pl`; the code is shared.
- README: 19 skills in six plugins.

## [2026.08.17] - 2026-08-17

Twin parity with the Polish line, plus two patterns adopted the same day.

### Added

- `output-scoring-en` v1.1.0 - UNCERTAIN as a first-class score (INSUFFICIENT_EVIDENCE /
  SOURCE_AMBIGUOUS, kept out of the average, capping the decision). The Polish twin has
  carried this since v1.1.0; the attribution gate surfaced the gap as a twin divergence.
- `output-scoring-en` - re-scoring section: raising a decision requires new evidence, not
  new argument; anchors cap the decision at Full verification.
- `humanizer-en` v2.7.0 - DOCUMENTATION MODE (#35-#42): one home per fact, narrated history,
  status annotations, hand-restated inventories, reasoning transcripts, emphasis inflation,
  spec-speak for shipped behaviour, catch-all words; plus the "preserve the complete
  proposition" shortening rule. Ported alongside humanizer-pl 1.2.0.

- `adversarial-legal-review-en` v1.1.0 - **twin merge**: deterministic verdict function with
  explicit weights (Step A critical / B weighted / C conditional), UNCERTAIN as a fourth
  synthesizer verdict with INSUFFICIENT_EVIDENCE / SOURCE_AMBIGUOUS, and the optional dissent
  panel (multiple-choice question to independent votes, split shown verbatim, one re-vote round,
  human gate). Until today PL and EN evolved apart; each lacked the other's mechanisms. The
  attribution gate's twin check is now silent in both repos. Legal-accuracy ledger: art. 12
  verified at source (EUR-Lex CELEX:32024R1689).

### Changed

- Attributions moved to list form; `AnttiHero/lavern` (Apache-2.0) credited on
  output-scoring-en, `deepseek-ai/deepseek-harness` (MIT, pattern-only) on humanizer-en.
- `NOTICE` - generated upstream block regenerated.

## [2026.08.07] - 2026-08-07

Legal-accuracy fixes prompted by external review (codex flags on the
mike-workflows eu-gdpr-pack PR, all seven confirmed against source texts).

### Fixed

- `gdpr-ropa-dpa-en` 1.2.0: processor register now lists the full
  Art. 30(2)(a) field set (processor(s), each controller, representatives,
  DPO, contact details); Art. 10 criminal-convictions data added as a
  separate Art. 30(5) disqualifier.
- `gdpr-dsar-en` 1.2.0: identity verification no longer pauses the deadline
  unconditionally (EDPB Guidelines 01/2022 conditions spelled out, original
  receipt date preserved); Art. 15 response requires a copy of the data from
  operational systems, not the RoPA; Art. 22 restated - primary right is not
  to be subject to a solely automated decision, 22(2) exceptions and 22(3)
  safeguards named.
- `clause-checklist-en` 1.1.0: applicability gate before absence flagging -
  CUAD is an extraction taxonomy, not a mandatory-safeguard list; mutually
  exclusive pairs count as one decision; not-applicable never red-flags.
- `citation-extraction-en` 1.1.0: pointer-aware short-reference resolution
  (ibid./id./loc. cit. = immediately preceding; supra/op. cit. resolve by
  author/title/note pointer over proximity; ambiguous = unresolved, manual
  review).

## [2026.07.05-2] - 2026-07-05

Skill Constitution across the whole hub: all 18 skills pass the
`skill-audit --marketplace` gate (PASS 18/18, previously 0/18).

### Changed

- Every SKILL.md frontmatter now declares the 5 "Skill Constitution" governance
  fields: `license` (per the README tables), `allowed-tools` (explicit minimal
  set; Bash only where the skill ships scripts), `data-residency: local`,
  `requires-human-approval` (true for skills that end in a human gate: the whole
  data-protection bundle plus eu-ai-act-triage-en, nis2-compliance-triage-en,
  privilege-preflight-en; false for purely analytical, read-only skills),
  `pii-egress: none`.
- The `signature` field is intentionally omitted - the Ed25519 signature is
  added at publication time (skill-audit gate note).

### Fixed

- Marketplace-blocking rot flag: `<YYYY-MM-DD>` placeholder in the
  eu-ai-act-triage-en triage card (replaced with square brackets).

## [2026.07.05] - 2026-07-05

Six new curated skills from the lawve.ai hub review (139 skills, snapshot 2026-07-05),
plus a new `ai-governance` plugin. Apache-2.0 forks carry author attribution; the rest
is pattern-only, written from scratch.

### Added

- New plugin `ai-governance` (3 skills): `eu-ai-act-triage-en` 1.0.0 (Reg. 2024/1689 triage - definition, Art. 5, high-risk, GPAI, Art. 50, role mapping, FRIA signal), `nis2-compliance-triage-en` 1.0.0 (Dir. 2022/2555 - scope, ten Art. 21(2) measures, Art. 23 incident clock, national transposition check), `privilege-preflight-en` 1.0.0 (SAFE/CAUTION/STOP band before sending legal content to an external AI surface).
- `opposing-counsel-attack-en` 1.0.0 (verification-foundation 1.0.0 -> 1.1.0): single-pass opposing-counsel attack, the cheap tier below adversarial-legal-review-en. Fork: opposing-counsel-review (L. Meredith-Flister, Apache-2.0).
- `judicial-first-impression-en` 1.0.0 (verification-foundation): seven-part neutral cold-reader assessment. Fork: judicial-first-impression (L. Meredith-Flister, Apache-2.0).
- `authority-triage-en` 1.0.0 (eu-law-sources 1.0.0 -> 1.1.0): route the source layer (EU primary/secondary, national chain, courts, soft law) before answering.
- Curated list: lawvable/awesome-legal-skills hub + two MIT picks (Swiss authority triage, French judicial reasoning).

### Changed

- `.claude-plugin/marketplace.json` -> 2026.07.05 (new ai-governance plugin entry; verification-foundation and eu-law-sources descriptions/versions).
- README: 18 installable skills across five plugins.

## [2026.06.30-3] - 2026-06-30

The whole `data-protection` bundle is now tool-grade - each of the 4 skills ships a deterministic executable helper, not just instructions.

### Added

- `gdpr-dpia-en` 1.0.0 -> 1.1.0: `scripts/dpia_screening.py` - Art. 35 threshold screening (EDPB 9 criteria, ">=2" rule, Art. 35(3) cases) -> verdict required/recommended/not_required. Offline, zero deps.
- `gdpr-ropa-dpa-en` 1.0.0 -> 1.1.0: `scripts/dpa_clause_check.py` - mandatory processor-contract clause check, Art. 28(3)(a)-(h) -> list of missing clauses (the redline target). Offline, zero deps.

## [2026.06.30-2] - 2026-06-30

### Added

- `gdpr-breach-72h-en` 1.0.0 -> 1.1.0 and `gdpr-dsar-en` 1.0.0 -> 1.1.0: deterministic deadline calculator `scripts/gdpr_deadlines.py` (offline, zero dependencies, GDPR-safe). Computes the 72h limit from awareness (Art. 33) and the one-month limit with correct month arithmetic per Regulation (EEC) No 1182/71 (receipt 31 Jan -> ends 28/29 Feb, year rollover, +3mo clamping). Agent-native tool - the skill stops counting deadlines by hand.

## [2026.06.30] - 2026-06-30

New bundle `data-protection` - operational GDPR tooling for law firms and DPOs. Four skills grounded in the regulation's articles and EDPB guidelines, each ending in a draft for decision (governance boundary: the outward act stays human). Niche confirmed by discovery (legaltech-scout): existing DPIA/DSAR/breach skills are generic-English and lightly installed - this is the article-grounded version.

### Added

- Plugin `data-protection` (4 skills): gdpr-dpia-en 1.0.0 (DPIA, Art. 35-36), gdpr-breach-72h-en 1.0.0 (breach 72h, Art. 33-34), gdpr-dsar-en 1.0.0 (data subject rights, Art. 12, 15-22), gdpr-ropa-dpa-en 1.0.0 (RoPA + DPA, Art. 30, 28). `CLAUDE.md` + `.claude-plugin/plugin.json`. Apache-2.0.

### Changed

- Hub: 8 skills in three skill bundles -> 12 skills in four skill bundles. Parity with the Polish hub (`ochrona-danych`).

## [2026.06.29] - 2026-06-29

### Changed

- `content-quality` 1.0.0 -> 1.1.0. `humanizer-en` 2.5.1 -> 2.6.0: added a "Statistical signatures" section (patterns #30-#34) covering the quantitative features AI detectors measure - sentence-length variance (burstiness), verb/adverb vs noun/adjective morphology, lexical density and vocabulary diversity, emotional range, and mechanical transitions. Based on Wołoszyk & Domaszk, "Detecting AI-Generated Content" (MultiLingual, Sept. 2025).

## [2026.06.26] - 2026-06-26

Initial release - English hub as the method-neutral counterpart to the Polish hub, in the bundle model.

### Added

- Plugin `verification-foundation` - jurisdiction-neutral verification core (5 skills): adversarial-legal-review-en, legal-syllogism-en, citation-extraction-en, clause-checklist-en, output-scoring-en. No connectors.
- Plugin `content-quality` - English-writing tools (2 skills): humanizer-en, reviewer-en.
- Plugin `eu-law-sources` - eu-sparql-search + `.mcp.json` (eu-sparql connector, EUR-Lex / Cellar SPARQL).
- `references/` - three shared standards (citation-style, responsibility-and-data, firm-deployment).
- `CLAUDE.md` and `.claude-plugin/plugin.json` per bundle. CLAUDE.md is self-contained (core rules inline, since the repo-level references do not install with a plugin).
- Curated list in README - links to 7 strong open skills from other teams (not republished).

### Boundary

- Method ports to English; substance does not. Deep Polish-jurisdiction skills stay in [awesome-matematic-skills-pl](https://github.com/matematicsolutions/awesome-matematic-skills-pl).
