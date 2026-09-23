# CHANGELOG

All notable changes to this hub are recorded here.
Format follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/).
Versioning: CalVer for the hub (`YYYY.MM.DD`), SemVer per skill.

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
