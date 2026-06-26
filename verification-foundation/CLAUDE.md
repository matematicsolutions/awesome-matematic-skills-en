# Verification foundation - shared rules

This file is the plugin's safety net. It applies even when a given skill is silent. The core is written out here so it works after installing the plugin alone. The fuller standard lives in `references/` in the marketplace repo.

## Five layers of protection (before any disclaimer)

1. **Source verification** - provisions and case law from databases, not the model's memory.
2. **Confidence class** - every legal claim marked: verified / check / do not use.
3. **Premise check** - facts from the user are tested before analysis.
4. **Explicit negative scope** - each skill states what it does NOT do.
5. **Human gate** - a qualified person reviews and approves the output.

If an error would pass without being stopped by layers 1-5, the fault is in the skill. Fix the tool, do not add a note. "This is not legal advice" stops no error and transfers no responsibility.

## Confidence tags

- **Verified** - source checked in this session, with a full identifier: `(GDPR Art. 6)`, `(Case C-311/18, CJEU)`.
- **Check** - plausible, unverified: `[check on EUR-Lex]`.
- **Do not use** - an invented case number or provision. Omit it, never fabricate.

The tag sits next to the line it concerns. A case number that exists is not enough - check the content.

## Human gate

Nothing is sent, filed, signed or published before a qualified person checks and approves it. A skill output is a draft, not a finished document.

## Plugin scope

The verification foundation is jurisdiction-neutral - the method, not the substance of any one legal system. It connects to no external source (no MCP connectors) and sends no data out. Substance comes from separate plugins (eu-law-sources). Deep national law (e.g. Polish case law) lives in the Polish marketplace, by design.
