---
name: adversarial-legal-review-en
description: >
  A red team for a high-stakes deliverable - takes a finished, high-stakes document
  (a legal opinion, a DD/M&A memo, a court/board submission, a recommendation) and runs
  an adversarial debate: a builder constructs the strongest version of the thesis, an
  attacker tears it apart with counter-arguments and contrary authority, a synthesizer
  reconciles, a verifier does a final check. Goal: find the weakness BEFORE your opponent,
  the court, or the client does. Cost-gated - for high-stakes work only, not every query
  (token-expensive). Use when: "attack this opinion", "red team", "devil's advocate for
  this document", "find the weaknesses", "stress-test the argument", "what will the other
  side say", "pre-mortem", "defend this thesis", "adversarial review", verifying a
  high-stakes deliverable before it goes out. English counterpart of adversarial-legal-review-pl
  (this version drops the Polish case-law layer and is jurisdiction-agnostic).
metadata:
  author: Wiesław Mazur / MateMatic
  version: 1.0.0
  inspiration: >
    AnttiHero/lavern (Apache 2.0) - debate + 3-layer verification pattern; roles and prompts written from scratch.
    gregmos/memoforge (MIT) - bounded self-revision with regression-revert, reviewer access tiers, always-deliver invariant; concepts adapted clean-room.
---

# Adversarial Legal Review (English) - a red team for a high-stakes deliverable

## Philosophy

**Better your own agent finds the weakness in your thesis than your opponent finds it in the hearing.**

A single LLM pass produces an argument that sounds confident - because the model is trained to sound confident. That is an illusion of competence. The real value of an expert is to foresee the counter-argument, the contrary authority, and the gap in reasoning before the other side does. This skill institutionalises the adversarial move: one agent defends, one attacks, one reconciles, one verifies.

This is NOT writing a deliverable from scratch. It is a stress-test of a finished deliverable.

## Cost gate (read BEFORE running)

The full cycle is token-expensive. Run it **only for high-stakes** work:

| Run (high-stakes) | Do NOT run (routine) |
|---|---|
| A legal opinion going to a client | An internal note |
| Due diligence / an M&A memo | A summary of a judgment |
| A court submission before a deadline | A working draft |
| A recommendation to a board | FAQ, marketing content |
| A position carrying material financial or reputational risk | A routine query |

If the matter is not high-stakes, say so plainly and offer an ordinary single-pass review instead of the full debate. Do not burn tokens on routine work.

## Workflow (4 roles + verification)

Each role is a separate pass with a clean mandate. Pseudonymise the input (e.g. with a humaniser/anonymiser step) if the document contains privileged or personal data.

### Reviewer access tiers (anti-bias)

Reviewers split into two tiers with DIFFERENT access - this is deliberate, not an accident:

- **ISOLATED** (internal consistency): the logic/structure reviewer sees **only the current draft** - no sources, no authority. Mandate: does the thesis contradict the reasoning, do the conclusions follow from the premises, are there logical gaps. It does NOT judge whether a citation is real. *Warning: if this reviewer saw the sources, it would confuse "sounds-like-the-source" with "is-internally-consistent".*
- **AUGMENTED** (grounding): the attacker (role 2) and the citation check (verifier point 1) see the sources + intake, and pull contrary authority. Mandate: grounding of claims and contrary authority.

In single-agent mode (one LLM simulating the roles), isolation is **prompt discipline**, not a hard sandbox - explicitly instruct the ISOLATED role not to reach for sources. Hard isolation via separate passes is the premium option.

### 0. High-stakes gate
Assess whether the matter qualifies (table above). If not, stop and offer an ordinary review.

### 1. Builder - the strongest version of the thesis
Build the strongest possible argument for the deliverable's thesis. Gather the best rules, authority, and doctrine. Goal: give the attacker a hard target, not a straw man.
Output: thesis + 3-7 pillars (each with its legal/evidentiary basis).

### 2. Attacker - devil's advocate
Attack each pillar like an opposing counsel / a sceptical court:
- contrary authority (pull real sources for the relevant jurisdiction)
- a doctrinal counter-argument
- a factual / evidentiary gap
- over-reading of a rule, an omitted exception, an out-of-date line of authority
- procedural risk (deadlines, standing, jurisdiction/competence)
Output: per pillar - the charge + its strength (high/medium/low) + the source of the charge.

### 3. Synthesizer - the balance
For each pillar decide: **survived / weakened / defeated**. State what is left of the thesis after the attack, where the deliverable needs reframing, where a caveat is required ("contested risk, authority is split").
Output: a table of pillar -> verdict -> recommended change.

**Priority hierarchy (when charges collide):** Logic (consistency) ~ Citations (grounding) ~ Counter-arguments **>** Style **>** Clarity. The substantive layer (logic/citations/counter-arguments) NEVER trades against itself - on conflict, accumulate BOTH views and add a caveat, do not pick arbitrarily. Style and clarity NEVER override substance. The synthesizer writes only actionable change instructions; it ignores trivia (`nice_to_have`) and charges from reviewers who already accepted a pillar.

### 4. Verifier - final check (10 points)
A mechanical and substantive check of the synthesised deliverable:
1. Every citation grounded - the quote exists in the source word for word (BLOCK on a failure)
2. Every pillar has a basis
3. No defeated pillar left in the final thesis without a caveat
4. The attacker's contrary authority addressed (not swept under the rug)
5. No categorical claims where the line is contested
6. Currency of the rules (not repealed / amended)
7. Internal consistency (thesis does not contradict the reasoning)
8. Scope matches the client's question (no more, no less)
9. Procedural risks listed
10. Confidence level stated explicitly (no false certainty)

## Revision loop (bounded)

The debate is not single-pass. The synthesizer may order an edit and run the draft through the attack again - but within **hard limits**, with a guarantee that we never ship a worse version than the best one seen.

- **Versioning:** `draft_v1` (after the first synthesis), `draft_v2`... Each iteration = targeted edits from the synthesizer's recommendation, then a re-attack + verification.
- **`aggregate_score`** (0-100) = the mean of: verifier (X/10 -> x10) + consistency (ISOLATED, 0-100) + grounding (AUGMENTED, 0-100). Hard component: the citation grounding check (mechanical) - any failure is a blocker regardless of score (guards against a false revert on a subjective LLM score).
- **`v_best`:** after each iteration, remember the draft with the highest `aggregate_score`.
- **Iteration cap per stakes:** high-stakes = max 3 rounds; quick mode = max 1.

**The synthesizer owns the exit decision.** Tree (evaluate in order):

1. **Clean approval** - all reviewers accepted, 0 blockers -> exit `approved_on_vN`.
2. **REGRESSION-REVERT (N>=2)** - `aggregate_score(vN) < aggregate_score(v_best)` -> reject vN, restore `v_best`, exit `forced_exit_on_v<best>_with_remaining_issues` + a banner "round N made the deliverable worse - reverted to the best version".
3. **Plateau early-exit (N>=2)** - score >= threshold (default 85) but improvement < 1.0 pt vs the previous -> exit `accepted_early_on_vN` (do not burn tokens on marginal gains).
4. **Continue** - blockers remain, cap not reached, no regression/plateau -> increment, another round of targeted edits.
5. **Forced exit at max** - cap reached with blockers -> `forced_exit_at_max` + a banner listing the unresolved blockers.

## Terminal states and always-deliver

**Every ending MUST produce an artefact for the human** (a full review block or a markdown fallback). Never a silent / empty exit. Terminal states:

`approved_on_vN` | `accepted_early_on_vN` | `forced_exit_on_v<best>` (regression) | `forced_exit_at_max` | `failed_with_fallback` (e.g. no source data - deliver what you have + the reason).

The banner always shows: the terminal state, which draft version was delivered, what blockers remain.
**Governance:** the skill produces a recommendation + draft versions; it does NOT send the document. The decision to "send despite `forced_exit_at_max` with blockers" stays with the human (parity ends before the external act). A transcript of all versions v1..vN is an attachment for an audit bundle as evidence of bounded revision and any revert (AI Act art. 12/14).

## Output

```
## Adversarial review - <deliverable name>

Stakes: HIGH (qualifies)
Iterations: v2 (best=v2) | Terminal state: accepted_early_on_v2 | aggregate_score: 78 -> 86
Thesis pillars: 5 | Survived: 3 | Weakened: 1 | Defeated: 1

| Pillar                       | Attack (strength)   | Verdict   | Action                       |
|------------------------------|---------------------|-----------|------------------------------|
| Basis of the claim           | none (low)          | survived  | no change                    |
| Line of authority            | <case> (high)       | defeated  | remove or add a caveat       |
| ...                          | ...                 | ...       | ...                          |

Verifier check: 9/10 OK. Point 1 (grounding): 1 citation failed - BLOCK.
Confidence level after the debate: MEDIUM (authority is split on 1 pillar).

Recommendation: do NOT send before (a) fixing the failed citation, (b) adding a caveat to the defeated pillar.

[terminal-state banner - examples]
- forced_exit_on_v1: "Round 2 lowered aggregate_score (84 -> 79) - reverted to v1. Blockers remain: 1 citation failed."
- forced_exit_at_max: "3 rounds exhausted, blockers remain: pillar III still has no contrary authority addressed. Delivered v3 - the decision to send is yours."
```

Return the full debate transcript (builder/attacker/synthesizer) as an attachment to an audit bundle - it is the evidence of adversarial verification.

## Data protection

- Each role runs through the standard API - for privileged material, pseudonymise the input before running.
- Pulling contrary authority uses public sources.
- The skill does not store the deliverable outside the matter folder.

## AI Act integration

Adversarial verification + an explicit confidence level + a transcript = operationalising human oversight (art. 14) and documentation (art. 12). The human gets not a "finished answer" but a map of what survived the attack and with what confidence - and decides on that basis.

## Difference from a multi-perspective expert panel

An expert panel = a multi-perspective analysis of a business decision by 5-7 personas (a workshop product). This skill = an adversarial stress-test of ONE deliverable (thesis vs antithesis vs synthesis vs verification). The panel looks broad; the adversarial review looks deep.

## Attribution

The pattern (debate + 3-layer verification) is inspired by AnttiHero/lavern (Apache 2.0). Roles, prompts and the 10-point check are written from scratch. Bounded self-revision (the exit tree with regression-revert), reviewer access tiers (isolated/augmented), mediator conflict-priority and the always-deliver invariant are adapted clean-room from gregmos/memoforge (MIT) - concepts of loop control and roles, not prompts or code. Polish counterpart: adversarial-legal-review-pl.
