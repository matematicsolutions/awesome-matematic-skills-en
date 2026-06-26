# CHANGELOG

All notable changes to this hub are recorded here.
Format follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/).
Versioning: CalVer for the hub (`YYYY.MM.DD`), SemVer per skill.

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
