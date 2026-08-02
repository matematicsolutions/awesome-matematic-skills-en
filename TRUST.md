# Trust and limits

What these skills guarantee, what they do not control, and where our claims end. Gaps first.

## What we do not control

A skill is a set of instructions executed by whatever AI agent you run it in
(Claude Code, Cowork, any SKILL.md-compatible runtime). The text you put in
front of the agent goes to the model you have configured. If that model is a
cloud API, your text reaches that provider under your agreement with them,
regardless of anything a skill does. The agent itself is also outside our
control: its telemetry and connections are between you and its vendor.

No file in this repository can change that, and none of our claims should be
read as saying otherwise. "GDPR-safe" anywhere in this hub describes the
skill layer, never your model pipeline.

## What a skill in this hub does guarantee

Each claim below is checkable by reading the skill's own files.

- **Method bundles add no connectors.** `verification-foundation`,
  `data-protection`, `ai-governance` and `content-quality` declare no MCP
  servers and no endpoints of their own.
- **Source bundles do reach out, and say so.** `eu-law-sources` declares the
  EU SPARQL connector in its `.mcp.json`, and `eu-sparql-search` sends your
  query to the EU Publications Office endpoint. `eu-multi-jurisdiction`
  installs nine national-law connectors, each querying the public API of
  that country's legal database. These query public law, so phrase queries
  in terms of the law, not of your matter.
- **No outbound calls in shipped scripts.** Bundled scripts (deadline
  calculators, gap checkers) are Python standard library, offline, and
  receive dates or clause lists, not case files.
- **Drafts, not acts.** Notifying a supervisory authority, sending a DSAR
  response, filing, signing: the skill prepares the document, a person
  performs the act. This boundary is stated per bundle in its `CLAUDE.md`.

## What the frontmatter fields mean

Some skills carry `data-residency: local` and `pii-egress: none`. Scope:
**the skill's own behaviour**. `pii-egress: none` means the skill adds no
channel that moves personal data out. It does not mean your session sends
nothing out; that is decided by your model configuration, above.

## If you need full locality

Point your agent at a local model (for example via Ollama). Then the skill
layer and the model layer are both on your machine. Whether the agent
itself is local too depends on its vendor, not on us. With a cloud model,
keep identifying details out of prompts or
anonymise first; the Polish hub ships `let-it-be` for exactly that.

## Human gate

Nothing produced here is legal advice. Treat every output as a draft that
must not leave the firm without review and approval by a qualified person.
If an error would pass without being caught by the checks a skill runs,
that is a defect in the skill; report it rather than relying on a
disclaimer to absorb it.
