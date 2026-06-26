# Citation and confidence standard

Shared standard for every skill in this repo. Each plugin points to it from its `CLAUDE.md`. Goal: the reader sees source confidence at a glance, and the model does not invent citations.

## Three confidence classes

Every legally meaningful claim (a provision, a case number, a quote, a contract clause) belongs to one of three classes. The class is visible at once, next to the line it concerns, not grouped at the end of a paragraph.

- **Verified** - source checked in this session. Written with a full identifier and source: `(Regulation (EU) 2016/679, Art. 6, EUR-Lex)` or `(Case C-311/18, CJEU)`.
- **Check** - plausible but unverified. Inline next to the sentence: `[check on EUR-Lex]`, `[verify the case number]`.
- **Do not use** - an invented case number, a non-existent provision, a quote with no source. Omit it. Never fabricate an identifier to fill a gap.

A case number that exists is not enough. Check the content: that the provision says what you attribute to it, and that the judgment decides what you quote.

## Citation format

- **Case law:** court or court abbreviation + number: `Case C-311/18`, `T-640/16`. Keep the original notation.
- **Legislation:** instrument + article: `GDPR Art. 6(1)(f)`, `Directive 2019/790 Art. 17`. Ranges with a hyphen: `Art. 2-4`.
- **Identifiers:** add a stable identifier where one exists - CELEX, ELI URI, ECLI.
- **Source database:** note where the confirmation came from - `EUR-Lex`, `Cellar`, `national gazette`.

## Source hierarchy

1. Primary: official journals, EUR-Lex / Cellar, court registries.
2. Secondary: literature and commentary, only when supplied by the user or the licence allows.
3. Never: the model's memory as the sole basis.

## What this standard does NOT do

- It does not replace substantive review by a qualified lawyer.
- It does not judge whether case law is still good law - that is a human assessment.
- It does not settle questions of interpretation - it only marks whether a source was confirmed.
