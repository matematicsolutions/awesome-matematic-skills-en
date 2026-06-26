# EU multi-jurisdiction - shared rules

This file is the plugin's safety net. It applies even when a connector is silent.

This plugin installs nine national-law MCP connectors in one step (DE, AT, ES, FI, IE, NL, SE, FR, LU). Each is read-only over the country's official open-data API and returns sources with stable identifiers (ELI / ECLI).

## Sources, not memory

Every legal claim belongs to a class:

- **Verified** - confirmed in the official source, with an identifier: `(BGB § 433, de-eli)`, `(Case C-311/18, CJEU)`.
- **Check** - plausible, not yet confirmed: `[verify in the national gazette]`.
- **Do not use** - an identifier with no match. Omit it, never fabricate.

A reference that exists is not enough - confirm it says what you attribute to it. Each jurisdiction has its own structure and language; keep the jurisdiction visible in every citation so nothing is silently applied to the wrong country.

## Requirements

These connectors run via `uvx` (Python), so the environment needs `uv` installed. France (`fr-eli`, Legifrance/PISTE) needs free PISTE OAuth credentials; the other eight need no key. Installing all nine starts nine MCP servers - install the plugin when you actually work across borders, not by default.

## Human gate

Output is a draft for review. National law of a country you do not practise in is a starting point for a local lawyer, not advice. Nothing is filed or signed before a qualified person checks it.

## Scope

EU member-state legislation and case law, one connector per country. EU-level law (EUR-Lex / CJEU) is in the `eu-law-sources` plugin. Verification method (grounding, red-team, scoring) is in `verification-foundation`.
