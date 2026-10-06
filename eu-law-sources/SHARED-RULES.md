## Shared rules of the eu-law-sources plugin (EU law sources)

These rules apply to every skill in this plugin, including where the skill itself is silent. They are copied into each skill, so they hold whether you install the whole plugin or a single skill.

### Sources, not memory

This plugin searches and fetches EU law (legislation and CJEU case law) through an MCP connector (read-only, public EUR-Lex / Cellar SPARQL). Every legal claim belongs to a class:

- **Verified** - confirmed in the database, with an identifier: `(Case C-311/18, CJEU)`, `(CELEX 32016R0679)`.
- **Check** - plausible, not yet confirmed: `[verify on EUR-Lex]`.
- **Do not use** - a CELEX or case number with no match. Omit it, never fabricate.

A case number that exists is not enough - check that the judgment decides what you cite. Whether case law is still good law is a human assessment.

### Connector in this plugin

`.mcp.json` declares the EU SPARQL connector (EUR-Lex / Cellar, read-only, public data). It needs `node`/`npx` in the environment. This is EU-level, language-neutral law - national law of a specific member state is out of scope here.

### Human gate

Output is a draft for review. Nothing is sent or filed before a qualified person checks it and takes professional responsibility.
