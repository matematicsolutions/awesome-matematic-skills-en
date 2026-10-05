# verification-foundation

Ten jurisdiction-neutral skills for checking legal AI output before it goes out. Each one
either makes a single step checkable (citations, the syllogism, the clauses, whether the
final document still carries what the analysis found) or attacks the result the way
opposing counsel or a judge would.

| Skill | What it does |
|---|---|
| `citation-extraction-en` | Pulls every citation out of a text (ECLI, CELEX, OJ, case names, provisions) and resolves short forms |
| `legal-syllogism-en` | Lays out major premise, minor premise, application and conclusion, and names the weak links |
| `clause-checklist-en` | Checks one contract against the 41 CUAD clause categories: present, absent or risky |
| `adversarial-legal-review-en` | Four-role debate on a high-stakes document: builder, attacker, synthesizer, verifier |
| `opposing-counsel-attack-en` | One pass by the other side's lawyer, procedural attacks included |
| `judicial-first-impression-en` | A judge's cold first reading: what confused it, what was assumed, what persuaded |
| `output-scoring-en` | Mechanical citation check, then a 1-5 rubric; returns send, revise or full verification |
| `legal-request-router-en` | Decides at the start how much checking a request deserves |
| `intake-sufficiency-en` | Scores whether an instruction is complete enough to start, and drafts the questions |
| `deliverable-fidelity-en` | Checks that no finding fell out of the executive summary |

## Install

In Claude Code:

```
/plugin marketplace add matematicsolutions/awesome-matematic-skills-en
/plugin install verification-foundation@matematic-skills-en
```

## Data

The skills have no connectors and open no network connections of their own. They work on
the text in your conversation, which goes to whatever model you have configured, the same
way as any other message you send. Nothing is stored by MateMatic.

## Licence

Apache-2.0, see `LICENSE`. Clause categories in `clause-checklist-en` come from CUAD
(The Atticus Project, CC BY 4.0).
