# awesome-matematic-skills-en

[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-8-blue.svg)](#installable-skills-8)
[![Plugin](https://img.shields.io/badge/Claude%20Code-plugin%20marketplace-orange.svg)](.claude-plugin/marketplace.json)
[![EU law](https://img.shields.io/badge/jurisdiction-EU%20%2B%20neutral-blue.svg)](#why-an-english-hub)
[![GDPR-safe](https://img.shields.io/badge/GDPR--safe-by%20default-green.svg)](#why-an-english-hub)

English hub of method-neutral legal AI skills for Claude Code / Cowork. The verification core, content-quality tools and EU-level law sources port across jurisdictions; deep national law stays where it belongs.

Maintainer: [Wieslaw Mazur](https://www.linkedin.com/in/wieslawmazur/) / [MateMatic Solutions](https://matematicsolutions.com).
Curatorial licence: **MIT** (skills keep their own licences declared in SKILL.md).

> **The method/substance line.** What ports to English is the method - grounding, red-team review, scoring, citation discipline, EU law search. What does not port is the substance of a specific legal system. Deep Polish-jurisdiction skills (case law, KRS, redlining, PL grounding) live in the Polish hub: [awesome-matematic-skills-pl](https://github.com/matematicsolutions/awesome-matematic-skills-pl).

## What's here

1. **Domain bundles installed with one command** - 8 skills grouped by function into three plugins. The verification foundation installs without any connector; EU law sources ship their MCP connector with the bundle.
2. **Curated list** - links to strong open skills from other teams (below). We point to them, we do not republish them.
3. **Companion Polish hub** for Polish-jurisdiction skills and live PL sources.

## Installation

```bash
# 1. Add the marketplace (once)
/plugin marketplace add matematicsolutions/awesome-matematic-skills-en

# 2. Install the bundles you need
/plugin install verification-foundation@matematic-skills-en   # core, no connectors
/plugin install content-quality@matematic-skills-en           # English-writing tools
/plugin install eu-law-sources@matematic-skills-en            # EU law + eu-sparql connector
```

The verification foundation and content-quality bundles use no connectors and send nothing out. `eu-law-sources` runs its MCP connector via `npx`, so it needs `node` in the environment.

---

## Installable skills (8)

### Plugin `verification-foundation` (jurisdiction-neutral verification core)

Install-always. No connectors, sends no data out. `/plugin install verification-foundation@matematic-skills-en`.

| Skill | What it does | Licence |
|---|---|---|
| adversarial-legal-review-en | Red team for a high-stakes deliverable - builder/attacker/synthesizer/verifier finds the weakness before opposing counsel does. | Apache-2.0 |
| legal-syllogism-en | Structure legal reasoning as major premise / minor premise / conclusion; surface hidden premises. | Apache-2.0 |
| citation-extraction-en | Extract and structure legal citations from text so they can be verified, not trusted on sight. | Apache-2.0 |
| clause-checklist-en | Check a contract against a clause checklist; flag missing or risky clauses. | Apache-2.0 |
| output-scoring-en | Score an AI legal output against a rubric before it ships. | Apache-2.0 |

### Plugin `content-quality` (English-writing tools)

`/plugin install content-quality@matematic-skills-en`.

| Skill | What it does | Licence |
|---|---|---|
| humanizer-en | Strip AI-writing patterns (inflated symbolism, rule of three, em-dash overuse, AI vocabulary); make text read naturally. | MIT |
| reviewer-en | Grumpy senior editor: a verdict (disaster/weak/mediocre/ok) and charges anchored to `file:line`. Points out what is wrong, does not rewrite. | MIT |

### Plugin `eu-law-sources` (EU law + connector)

Ships the `eu-sparql` MCP connector (read-only, public EUR-Lex / Cellar). Requires node/npx. `/plugin install eu-law-sources@matematic-skills-en`.

| Skill | What it does | Licence |
|---|---|---|
| eu-sparql-search | Search EU legislation and CJEU case law via the Publications Office SPARQL endpoint (CELEX, ELI URI, multi-language acts). | Apache-2.0 |

---

## Curated - strong skills from other teams

We point to these, we do not republish them - check each repo's own licence before use.

| Skill | Source |
|---|---|
| AI Act for engineers | [morellid/ai-act-skill](https://github.com/morellid/ai-act-skill) |
| Anthropic legal suite | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) |
| AI Act resources | [GenAI-Gurus/awesome-eu-ai-act](https://github.com/GenAI-Gurus/awesome-eu-ai-act) |
| Presidio - PII anonymisation | [microsoft/presidio](https://github.com/microsoft/presidio) |
| GRC compliance | [Sushegaad/Claude-Skills-Governance-Risk-and-Compliance](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance) |
| Privacy procedures | [mukul975/Privacy-Data-Protection-Skills](https://github.com/mukul975/Privacy-Data-Protection-Skills) |
| Contract review (CUAD) | [evolsb/claude-legal-skill](https://github.com/evolsb/claude-legal-skill) |

## Need live sources of law too?

EU law ships with `eu-law-sources` above. For national law, see the [eu-legal-mcp connector line](https://github.com/matematicsolutions) - one MCP connector per jurisdiction (DE/AT/ES/FI/IE/NL/SE/FR/LU), each grounding acts and case law against the official source.

## Why an English hub

1. **You install only what applies.** Grounding, red-team review and scoring travel to any jurisdiction; country-specific case law does not, so this hub never ships you Polish or German rules you cannot use.
2. **GDPR-safe by default.** The verification and content skills run locally and send no data out. Connectors are read-only over public APIs.
3. **AI Act Art. 12 + Art. 50.** Record-keeping and the transparency duty are built into how these skills present output - every output is a draft, marked as AI-generated.
4. **Vendor-agnostic.** The skills follow the open [Agent Skills](https://github.com/anthropics/skills) format and run wherever it is implemented.

## Shared standards

All skills inherit three shared standards in [`references/`](./references): citation style and confidence tags, responsibility and data protection, firm deployment. Each plugin's `CLAUDE.md` carries the core inline so it works after installing the plugin alone.

## Licence

- Curatorial (README, taxonomy, marketplace.json): **MIT**
- Per-skill: declared in `SKILL.md` frontmatter (Apache-2.0 for MateMatic-authored, MIT for adaptations)
- Curated entries above: each keeps its own upstream licence

## Contact

[matematicsolutions.com](https://matematicsolutions.com) | [LinkedIn Wieslaw Mazur](https://www.linkedin.com/in/wieslawmazur/) | [github.com/matematicsolutions](https://github.com/matematicsolutions)
