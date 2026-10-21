---
name: nis2-compliance-triage-en
description: >-
  NIS2 scope and obligations triage (Directive (EU) 2022/2555) in English - a scope navigator:
  is the entity in scope at all (Annex I and II sectors, size-cap rule, size-independent
  exceptions), essential vs important entity, map of the 10 risk-management measures under
  Art. 21(2), incident reporting clock under Art. 23 (24h -> 72h -> 1 month), management body
  duties under Art. 20, penalty ceilings. NIS2 is a directive: obligations bite through NATIONAL
  transposition, and transpositions differ per member state - so the skill puts the transposition
  question first and marks it for checking against the national source before anything is relied
  on. It has no connector of its own and does not confirm transposition status. Output: a
  NIS2 card for human decision. Use when: "does NIS2 apply to us", "essential or important
  entity", "the 10 measures of Art. 21", "NIS2 incident reporting", "management board
  cybersecurity duties", "NIS2 fines", "national transposition of NIS2".
license: Apache-2.0
allowed-tools: [Read]
data-residency: local
requires-human-approval: true
pii-egress: none
attribution:
  relationship: original
  note: >
    No third-party source. The "scope navigator" pattern is common in the compliance
    ecosystem; content written from scratch on the text of Directive (EU) 2022/2555.
metadata:
  author: Wiesław Mazur / MateMatic
  version: 1.1.0
  companion_skills: gdpr-breach-72h-en, matematic-konstytucja-ai, sejm-eli-mcp, mcp-eu-compliance
  parity: nis2-ksc-pl
---

# NIS2 Compliance Triage EN - scope and obligations navigator (Directive (EU) 2022/2555)

## Philosophy

NIS2 is first a scope question, only then a measures question. Most bad advice skips triage: a
company "feels" in scope (or out of scope) and jumps straight to an audit. This skill runs the
navigator in a fixed order: **in scope? -> which category -> which measures -> which reporting ->
what does the national transposition say**. Every claim carries a certainty tag; an article
number that cannot be confirmed in the session gets [TO VERIFY], never a guessed number.

Second principle: **a directive does not bind a company directly**. Obligations come from the
national implementing act, and member states transposed NIS2 differently and at different times.
Until the transposition status of the relevant country is established as of the day of use,
everything below is a map of the directive, not a list of enforceable duties.

## When to use / What it does NOT do

**Use for:** initial "does NIS2 apply to us" triage, the "essential or important" dispute, an
inventory of the 10 measures under Art. 21(2) before an audit, laying out the incident reporting
clock in advance, briefing the management body on Art. 20 liability, turning gaps into an
implementation plan.

**Does NOT:**
- replace a security audit or penetration test - the measures map is built from user
  declarations; the skill verifies nothing technically,
- assess the quality of a measure (whether backups actually restore) - only whether it exists
  and is documented according to the user,
- run a live incident - during an ongoing incident it points to the internal response procedure
  and the responsible human (CISO / board / counsel),
- send any notification to a CSIRT or competent authority - it drafts and sets the clock,
- settle entity classification definitively - that is a legal call on the national implementing
  act, behind the human gate.

**Regime boundary:** if the incident involves personal data, TWO clocks run IN PARALLEL - NIS2
(24h early warning / 72h incident notification to the CSIRT or authority) and GDPR (72h
notification to the data protection authority, Art. 33 GDPR). The GDPR clock is run by
`gdpr-breach-72h-en`. One notification never substitutes for the other.

## Workflow

### Step 0 - national transposition status (MANDATORY, before any advice)

The transposition deadline expired on 17 October 2024 (Art. 41 of the directive). Member states
missed it to varying degrees, and national acts diverge on registration, deadlines, authority
structure and penalties. Therefore:

1. Identify the member state(s) whose law applies to the entity, using Art. 26:

   | Entity | Member state with jurisdiction |
   |---|---|
   | Default - any entity not listed below (Art. 26(1)) | where it is established |
   | Providers of public electronic communications networks or publicly available electronic communications services (Art. 26(1)(a)) | where it provides its services |
   | DNS service providers, TLD name registries, entities providing domain name registration services, cloud computing service providers, data centre service providers, CDN providers, managed service providers, managed security service providers, providers of online marketplaces, online search engines and social networking services platforms (Art. 26(1)(b)) | where it has its main establishment in the Union (Art. 26(2)): where cybersecurity risk-management decisions are predominantly taken; failing that, where cybersecurity operations are carried out; failing that, the establishment with the most employees in the Union |
   | Public administration entities (Art. 26(1)(c)) | the member state that established them |

   The main-establishment rule covers ONLY the closed list in Art. 26(1)(b) - not "digital
   infrastructure" as a whole (IXPs, trust service providers and electronic communications
   providers are not on it). An Art. 26(1)(b) entity not established in the Union but offering
   services in it must designate a representative in the Union (Art. 26(3)).
2. Verify the transposition status of that state as of the day of use. Examples of national
   acts: Germany - NIS2UmsuCG (NIS-2-Umsetzungs- und Cybersicherheitsstärkungsgesetz), status [TO VERIFY]; Poland -
   Act of 23 January 2026 amending the Act on the National Cybersecurity System (KSC) and
   certain other acts, Journal of Laws (Dz.U.) 2026 item 252; it entered into force one month
   after publication (its art. 49), on 3 April 2026 per ISAP, and ISAP lists it as in force (checked 2026-10-19 - re-check
   the current KSC text and any later amendment in ISAP via the sejm-eli-mcp connector). For
   other states, check the national gazette or the mcp-eu-compliance connector; do not assume
   any act is in force without checking.
   EU level: no act amending Directive (EU) 2022/2555 had been adopted as of 2026-10-19 (Cellar);
   the Commission proposal COM(2026) 13 of 20 January 2026 to amend it ("simplification
   measures") was still a proposal - check its status before relying on the current text.
3. Record the result on the card (field "Transposition status") with the date checked.
4. Pick the analysis regime: (a) national act in force -> analyse on the act; (b) not in
   force -> analyse on the directive as a map of INCOMING obligations, and flag that the old
   NIS1-based national regime may still apply in the meantime.
5. **Never state that a national transposition is in force without verifying it in the
   session.**

### Step 1 - sector triage (Annex I and II)

**Annex I - sectors of high criticality:** energy (electricity, district heating and cooling,
oil, gas, hydrogen), transport (air, rail, water, road), banking, financial market
infrastructures, health, drinking water, waste water, digital infrastructure (incl. IXPs, DNS
service providers, TLD name registries, cloud computing providers, data centre providers, CDNs,
trust service providers, public electronic communications networks and services), ICT service
management B2B (managed service providers and managed security service providers), public
administration, space.

**Annex II - other critical sectors:** postal and courier services, waste management,
manufacture, production and distribution of chemicals, food (production, processing,
distribution), manufacturing (incl. medical devices, computer/electronic/optical products,
electrical equipment, machinery, motor vehicles and other transport equipment), digital
providers (online marketplaces, online search engines, social networking platforms), research
organisations.

Entity outside both annexes -> as a rule out of scope; still check whether the national
transposition extends the catalogue ([TO VERIFY] field on the card).

### Step 2 - size-cap rule and size-independent exceptions (Art. 2)

**Size-cap rule (Art. 2(1)):** the directive covers Annex I or II entities that qualify as
**medium-sized enterprises** under Article 2 of the Annex to Recommendation 2003/361/EC, or
exceed the ceilings for medium-sized enterprises. The test, from the Annex to the
Recommendation:
- **Headcount and financial ceilings** (Annex, Article 2): small - fewer than 50 persons AND
  annual turnover and/or annual balance sheet total not exceeding EUR 10 million; medium-sized -
  fewer than 250 persons AND annual turnover not exceeding EUR 50 million and/or annual balance
  sheet total not exceeding EUR 43 million. So an entity is at least medium-sized if it has 50 or
  more persons, or if BOTH its turnover AND its balance sheet total exceed EUR 10 million; it
  exceeds the medium-sized ceilings if it has 250 or more persons, or if its turnover exceeds
  EUR 50 million AND its balance sheet total exceeds EUR 43 million.
- **Aggregation** (Annex, Articles 3 and 6(2)): add the data of partner enterprises in proportion
  to the shareholding or voting rights (whichever is greater; for cross-holdings, the greater
  percentage), and 100% of the data of linked
  enterprises. Member states may take into account the entity's degree of independence from its
  partner or linked enterprises (recital 16 of the directive) - [TO VERIFY in the transposition].
- **Public ownership:** the rule in Article 3(4) of the Annex (25% or more public control
  excludes SME status) does not apply for NIS2 purposes (Art. 2(1), second subparagraph).
- **Two accounting periods** (Annex, Article 4(2)): a change in category takes effect only if the
  ceilings are crossed over two consecutive accounting periods.

Micro and small enterprises are, as a rule, out - subject to the size-independent paths below.

**Size-independent paths** - check these BEFORE concluding "out of scope", because some reach
entities outside Annex I and II:
- **Domain name registration services:** entities providing them are in scope regardless of
  size (Art. 2(4)) - an independent path.
- **Critical entities** identified under the CER Directive (EU) 2022/2557, regardless of size
  (Art. 2(3)).
- **Entities of a type in Annex I or II, regardless of size, where** (Art. 2(2)): (a) the
  services are provided by providers of public electronic communications networks or publicly
  available electronic communications services, trust service providers, or TLD name registries
  and DNS service providers; (b) the entity is the sole provider in a member state of a service
  essential for critical societal or economic activities; (c) disruption of its service could
  significantly impact public safety, public security or public health; (d) disruption could
  induce a significant systemic risk, in particular cross-border; (e) it is critical because of
  its specific importance at national or regional level; (f) it is a public administration
  entity of central government, or at regional level following a risk-based assessment.
- Member states may extend the directive to local public administration and education
  institutions (Art. 2(5)) - [TO VERIFY in the transposition].

### Step 3 - essential vs important entity (Art. 3)

Run the Art. 3(1) paths in order; the first one that fits makes the entity **essential**:
1. Annex I entities that exceed the ceilings for medium-sized enterprises (Art. 3(1)(a)).
2. Qualified trust service providers, TLD name registries and DNS service providers, regardless
   of size (Art. 3(1)(b)).
3. Providers of public electronic communications networks or publicly available electronic
   communications services that qualify as medium-sized enterprises (Art. 3(1)(c)).
4. Public administration entities of central government (Art. 2(2)(f)(i); Art. 3(1)(d)).
5. Annex I or II entities that a member state has identified as essential under Art. 2(2)(b)
   to (e) (Art. 3(1)(e)).
6. Critical entities under the CER Directive (Art. 2(3); Art. 3(1)(f)).
7. If the member state so provides, entities it identified before 16 January 2023 as operators
   of essential services under the NIS1 Directive or national law (Art. 3(1)(g)).

**Important** (Art. 3(2)): every in-scope Annex I or II entity that does not qualify as
essential - including medium-sized Annex I entities, medium and large Annex II entities,
non-qualified trust service providers, and entities identified under Art. 2(2)(b) to (e) as
important rather than essential. Record on the card which path decided the category. The final national split is set by the implementing act - tag the national
classification [TO VERIFY] until Step 0 confirms it. Why it matters: different supervision (ex
ante vs ex post) and different penalty ceilings (Step 7).

### Step 4 - sector-specific Union acts (Art. 4), then the 10 risk-management measures (Art. 21(2))

**Pre-check (Art. 4):** where a sector-specific Union legal act requires the entity to adopt
cybersecurity risk-management measures or to notify significant incidents, and those
requirements are at least equivalent in effect to the directive's obligations, the corresponding
NIS2 provisions - including supervision and enforcement under Chapter VII - do not apply to that
entity. Name the sectoral act, state which NIS2 provisions it displaces (measures, reporting, or
both), and tag the equivalence assessment [TO VERIFY] until a human confirms it. Only what
remains under NIS2 goes into the map below and the clock in Step 5.

Entities that remain under Art. 21 after this pre-check (essential and important alike)
implement measures proportionate to the risk, covering AT LEAST:

1. policies on risk analysis and information system security,
2. incident handling,
3. business continuity (backup management, disaster recovery) and crisis management,
4. supply chain security, including relationships with direct suppliers and service providers,
5. security in network and information systems acquisition, development and maintenance,
   including vulnerability handling and disclosure,
6. policies and procedures to assess the effectiveness of cybersecurity risk-management
   measures,
7. basic cyber hygiene practices and cybersecurity training,
8. policies and procedures on the use of cryptography and, where appropriate, encryption,
9. human resources security, access control policies and asset management,
10. multi-factor or continuous authentication, secured voice, video and text communications and
    secured emergency communication systems, where appropriate.

For each measure ask the user for status (implemented / partial / missing / unknown) and record
it. "Unknown" is a gap, not a zero - do not guess on the user's behalf.

### Step 5 - significant incident reporting (Art. 23)

**Significant incident** (Art. 23(3)): it has caused or is capable of causing severe operational
disruption of the services or financial loss for the entity, OR it has affected or is capable of
affecting other natural or legal persons by causing considerable material or non-material
damage.

The clock (Art. 23(4)). The first two deadlines run from becoming aware of the significant
incident. Each is the latest permitted time; the submission itself is due without undue delay:
- without undue delay, at the latest within **24h** - early warning to the CSIRT or competent
  authority (incl. whether unlawful or malicious action is suspected and whether cross-border
  impact is possible),
- without undue delay, at the latest within **72h** - incident notification (updating the early
  warning; initial assessment of severity, impact and indicators of compromise). Exception: a
  trust service provider must submit the incident notification for a significant incident
  affecting the provision of its trust services within **24h**, not 72h,
- on CSIRT/authority request - **intermediate report** on status updates,
- **1 month** after the incident notification - **final report** (detailed description, threat
  type, root cause, mitigation applied, cross-border impact); if the incident is still ongoing -
  a progress report, with the final report one month after the incident is handled.
- Where appropriate - notify the recipients of the services likely to be affected.

The addressee (which CSIRT / authority) and the exact submission channel are national - [TO
VERIFY in the transposition from Step 0]. During a LIVE incident: the skill sets the clock and
drafts, then hands over to the response procedure and the human. Personal data involved ->
`gdpr-breach-72h-en` in parallel.

### Step 6 - management body (Art. 20)

The management body of an essential or important entity: **approves** the Art. 21
risk-management measures, **oversees** their implementation, and **can be held liable** for the
entity's infringements of that article. Members of the management body must **follow training**
in cybersecurity and should offer similar training to employees. The precise shape of personal
liability (fines on managers, other sanctions) is national - [TO VERIFY in the transposition].

### Step 7 - penalties (Art. 34)

Ceilings from the directive for infringements of Art. 21 or Art. 23 (maxima each member state
must at least provide for; turnover means the total worldwide annual turnover in the preceding
financial year of the undertaking to which the entity belongs):
- **essential** entities: at least up to **EUR 10 000 000 or 2%** of total worldwide annual
  turnover - whichever is higher,
- **important** entities: at least up to **EUR 7 000 000 or 1.4%** of turnover - whichever is
  higher.

National acts set the concrete brackets, manager-level fines and supervisory measures (including
a possible temporary ban on managerial functions in essential entities - [TO VERIFY article
number and national shape]) - all [TO VERIFY in the transposition from Step 0].

## Output format - NIS2 card (literal template)

```
NIS2 CARD - [entity] - [analysis date]

TRANSPOSITION STATUS (Step 0): [member state + result + date checked / TO VERIFY]
Analysis regime: [national implementing act / directive 2022/2555 as map + legacy NIS1 regime]

IN SCOPE: [YES / NO / TO VERIFY]
Entity category: [essential / important / out of scope / TO VERIFY]
Sector: [Annex I or II - sector - subsector]
Basis for inclusion: [size-cap: medium/large / size-independent path: which one]
Category path: [Art. 3(1) point that made it essential / Art. 3(2) important]
Sector-specific act (Art. 4): [none / act + displaced NIS2 provisions - TO VERIFY equivalence]

MAP OF 10 MEASURES (Art. 21(2)) - status per user declaration:
| #  | Measure                                      | Status                          | Gap |
| 1  | risk analysis and IS security policies       | [implemented/partial/missing/unknown] | ... |
| 2  | incident handling                            | ...                             | ... |
| ... (all 10)                                                                            |

REPORTING CLOCK (Art. 23) - [mode: simulation / live incident]:
- awareness:                  [date+time or "n/a"]
- early warning (24h):        [outer limit from awareness - without undue delay]
- incident notification (72h):[outer limit from awareness - 24h for a trust service provider]
- final report (1 month):     [deadline counted from submission of the incident notification]
- addressee: [CSIRT/authority per transposition - TO VERIFY if not established]
- personal data involved: [YES -> gdpr-breach-72h-en in parallel / NO]

MANAGEMENT BODY (Art. 20): [approval: status | oversight: status | training: status]

PENALTY EXPOSURE: [ceiling per category: EUR 10m / 2% or EUR 7m / 1.4%]

GAPS: [numbered list - including every "unknown" from the measures map]
NEXT STEPS: [1-5 items, most urgent first]
CERTAINTY TAGS: [what was verified in session, what remains TO VERIFY]
```

## Human gate

The NIS2 card is a draft for decision, not a ruling. Entity classification, the decision to
notify an incident and any submission to a CSIRT or competent authority are approved and
executed by an authorised human (board / CISO / counsel). During a live incident the skill does
not take over response - it sets the clock and drafts; the procedure and the human run the rest.
Submission is never automatic.

## Companion skills

- `gdpr-breach-72h-en` - the parallel GDPR clock when the incident involves personal data,
- `matematic-konstytucja-ai` - AI governance rules for organisations in NIS2 scope,
- **sejm-eli-mcp** connector - status of the Polish KSC act and its amendment in ISAP,
- **mcp-eu-compliance** connector - text of Directive (EU) 2022/2555 from EUR-Lex for verifying
  provisions.

## Source verification

Article numbers in this skill come from the text of Directive (EU) 2022/2555; before they enter
a deliverable, verify each citation against EUR-Lex (CELEX 32022L2555, via mcp-eu-compliance)
and the national law against the national gazette (for Poland: ISAP via sejm-eli-mcp). The
verification foundation tags apply: verified / [TO VERIFY] / do not use. Any number or threshold
you cannot confirm in the session keeps its [TO VERIFY] tag - never invent an article number or
a penalty bracket.

<!-- shared-rules:begin (generated from ../../SHARED-RULES.md by scripts/shared-rules-sync.py - do not edit here) -->
## Shared rules of the ai-governance plugin (AI governance)

These rules apply to every skill in this plugin, including where the skill itself is silent. They are copied into each skill, so they hold whether you install the whole plugin or a single skill.

These skills run regulatory triage for organisations deploying or building AI: EU AI Act classification and role mapping, NIS2 scope and obligations triage, and a privilege pre-flight check before legal content is sent to an external AI surface. Each ends in a draft for decision, not a finished act.

### Rules

- **Output is a draft for decision.** A classification card, a scope assessment or a redacted prompt is a starting point for counsel / the compliance owner. A person approves and acts on it.
- **Governance boundary - the outward act stays human.** Registering an AI system, notifying a CSIRT or supervisory authority, filing a FRIA, sending anything to an external AI service - the skill prepares the draft, it does not perform the act.
- **Regulation from the source, not from memory.** Article references carry confidence tags; anything uncertain is marked for verification against EUR-Lex (eu-sparql-search / mcp-eu-compliance connectors) or the national transposition before it is relied on. National transposition status changes - always check it at time of use.
- **Triage is not a conformity assessment.** These skills classify, map and flag. A high-risk or GPAI finding routes to a human and a full assessment; it is never the end of the analysis.
- **Not legal advice.** The skills organise obligations and map them to provisions; they do not replace legal analysis of a specific matter.
- **Confidentiality.** System descriptions, incident details and prompt content are confidential - do not move them outside the agreed flow. These skills add no outbound channel of their own; what reaches your model is decided by your configuration (see https://github.com/matematicsolutions/awesome-matematic-skills-en/blob/main/TRUST.md).

### Plugin scope

Regulatory triage for AI and cyber (AI Act, NIS2) plus prompt-level privilege hygiene. It does not verify citations or fetch sources of law - use `verification-foundation` and `eu-law-sources` for that. GDPR operations (DPIA, breach, DSAR) live in `data-protection`; the AI Act triage pairs with `gdpr-dpia-en` when a system processes personal data.
<!-- shared-rules:end -->
