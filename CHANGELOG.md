# CHANGELOG

All notable changes to this hub are recorded here.
Format follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/).
Versioning: CalVer for the hub (`YYYY.MM.DD`), SemVer per skill.

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
