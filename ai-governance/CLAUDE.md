# AI governance - shared rules

This file is the plugin's safety net. It applies even when a given skill is silent.

These skills run regulatory triage for organisations deploying or building AI: EU AI Act classification and role mapping, NIS2 scope and obligations triage, and a privilege pre-flight check before legal content is sent to an external AI surface. Each ends in a draft for decision, not a finished act.

## Rules

- **Output is a draft for decision.** A classification card, a scope assessment or a redacted prompt is a starting point for counsel / the compliance owner. A person approves and acts on it.
- **Governance boundary - the outward act stays human.** Registering an AI system, notifying a CSIRT or supervisory authority, filing a FRIA, sending anything to an external AI service - the skill prepares the draft, it does not perform the act.
- **Regulation from the source, not from memory.** Article references carry confidence tags; anything uncertain is marked for verification against EUR-Lex (eu-sparql-search / mcp-eu-compliance connectors) or the national transposition before it is relied on. National transposition status changes - always check it at time of use.
- **Triage is not a conformity assessment.** These skills classify, map and flag. A high-risk or GPAI finding routes to a human and a full assessment; it is never the end of the analysis.
- **Not legal advice.** The skills organise obligations and map them to provisions; they do not replace legal analysis of a specific matter.
- **Confidentiality.** System descriptions, incident details and prompt content are confidential - do not move them outside the agreed flow. Processing is local (GDPR-safe).

## Plugin scope

Regulatory triage for AI and cyber (AI Act, NIS2) plus prompt-level privilege hygiene. It does not verify citations or fetch sources of law - use `verification-foundation` and `eu-law-sources` for that. GDPR operations (DPIA, breach, DSAR) live in `data-protection`; the AI Act triage pairs with `gdpr-dpia-en` when a system processes personal data.
