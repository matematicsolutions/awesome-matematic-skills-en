# data-protection

Four skills for the GDPR work that has a clock or a checklist behind it: a personal data breach,
a DPIA, a data subject request, and the records of processing with the processor contract. Each
skill maps the task to the GDPR articles, asks for the facts it needs instead of guessing them, and
ends in a draft for the controller or DPO to approve.

| Skill | What it does |
|---|---|
| `gdpr-breach-72h-en` | Breach response under Art. 33-34: classification, risk factors (EDPB Guidelines 9/2022), notification without undue delay with the 72-hour outer limit, communication to individuals and its exemptions, breach register |
| `gdpr-dpia-en` | Whether a DPIA is required (Art. 35(3), national lists, the nine WP248 criteria), the Art. 35(7) minimum content, the Art. 36 prior-consultation decision |
| `gdpr-dsar-en` | Data subject requests under Art. 12 and 15-22: identity, the one-month limit and extension, exemptions such as Art. 17(3), draft response and request register |
| `gdpr-ropa-dpa-en` | Records of processing (Art. 30) and a processor-contract check against each Art. 28(3) stipulation, with a redline of what is missing |

Every statutory reference in these skills was checked against the GDPR text on EUR-Lex and logged,
unit by unit, in [`reviews/legal-accuracy.md`](https://github.com/matematicsolutions/awesome-matematic-skills-en/blob/main/reviews/legal-accuracy.md).
The skills organise the obligations; they are not legal advice on a specific matter.

## Install

In Claude Code:

```
/plugin marketplace add matematicsolutions/awesome-matematic-skills-en
/plugin install data-protection@matematic-skills-en
```

The deadline and checklist calculators are small Python scripts with no dependencies. They need
Python 3 on your machine, and Claude Code asks you before it runs each one.

## Data

The skills have no connectors and open no network connections of their own. The calculators run
offline on your machine and only read the dates or clause letters you give them. The incident
details, system descriptions or requests you paste go to whatever model you have configured, the
same way as any other message, so keep real personal data of data subjects out of the prompt
unless your setup is cleared for it. Nothing is stored by MateMatic.

Filing with a supervisory authority, sending a notification or a response, erasing or exporting
data and signing a contract are never done by the skills: they prepare the draft, a person acts.

## Licence

Apache-2.0, see `LICENSE`.
