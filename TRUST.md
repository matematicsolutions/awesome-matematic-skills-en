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

## The licence will not be taken back

The skills in this hub are open and stay open. Apache-2.0 for the ones we wrote,
MIT for adaptations, each declared in its own `SKILL.md` frontmatter. That is a
settled decision, not a trial period, and it is worth stating plainly because the
alternative is common: a source-available licence that reserves the right to
revoke permission later. A firm cannot build a process on a permission that can
be withdrawn.

Two things follow, and both are checkable rather than promised. What you have
already installed stays yours under the licence you received it under; no later
change here reaches back. And you can fork the hub and run it yourself, which is
the only guarantee that actually survives us losing interest.

We do not claim this is charity. Our work that is genuinely hard to copy is not
in these files: it is in the corpora, the source connectors and the measurements
behind them. Closing the licence here would buy us little in practice, because
most of what a skill carries is method: a rubric, a threshold, an order of steps.
Anyone can read that and rewrite it in their own words, and no licence term stops
them from doing so.

If a skill here ever stops being a method and starts carrying a corpus, data, or
a measurement that cannot be reproduced without our work, that specific component
gets its own licence and we say so in the open. Nothing currently in this hub is
in that position.

## Human gate

Nothing produced here is legal advice. Treat every output as a draft that
must not leave the firm without review and approval by a qualified person.
If an error would pass without being caught by the checks a skill runs,
that is a defect in the skill; report it rather than relying on a
disclaimer to absorb it.
