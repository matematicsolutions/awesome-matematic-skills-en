---
name: output-scoring-en
description: >
  Scores the quality of an AI legal output before it goes out, in two layers: objective
  (mechanically checkable - do the citations exist, are the provisions and dockets real)
  and subjective (LLM-as-judge on a 1-5 rubric: legal correctness, completeness, clarity,
  jurisdiction fit, grounding/anti-hallucination). Returns a scorecard and a decision:
  send / revise / full verification. A layer above the deliverable - it does not write,
  it scores. Jurisdiction-neutral. Pairs with reviewer-en, adversarial-legal-review-en and
  legal-syllogism-en. Use when: "score this output", "is this ready to send", "quality of
  this legal answer", "scorecard for the deliverable", "rubric check" - before sending an
  opinion, memo, or brief.
metadata:
  author: Wiesław Mazur / MateMatic
  version: 1.0.0
  inspiration: >
    Two-layer method (objective matching + a subjective LLM-as-judge rubric, 1-5 scale)
    based on DISC-Law-Eval from DISC-LawLLM (Fudan DISC Lab), Apache-2.0
    (https://github.com/FudanDISC/DISC-LawLLM). Exam data and judge model dropped; rubric,
    dimensions and thresholds written from scratch. English counterpart of ocena-outputu-pl.
  companion_skills: reviewer-en, adversarial-legal-review-en, legal-syllogism-en
---

# Output scoring - a scorecard before you send

## Philosophy

**Before you send it, score it - and keep what is checkable apart from what must be judged.** An AI
output can read smoothly and still be wrong. This skill scores it in two layers: objective (facts you
can verify mechanically) and subjective (quality you have to judge against an explicit rubric).
Mixing the two is where false confidence comes from - "sounds right" is not "the citations check out".

It **scores**; it does not write or send. The decision is the lawyer's; the scorecard is the basis.

## Layer 1 - objective (mechanically checkable)

Delegate, do not guess:
- **Citations and provisions** - do they exist in the source verbatim; were they all caught.
- **Dockets / identifiers** - real and correctly written.
- **Completeness** - did any RED finding drop out of the summary.

The objective result is binary per item: matches / does not. Even one mismatched citation means the
output is not ready, whatever the subjective score.

## Layer 2 - subjective (1-5 rubric, LLM-as-judge)

Score each dimension 1-5 with a one-sentence reason:

| Dimension | 1 | 5 |
|---|---|---|
| Legal correctness | thesis wrong or unsupported | thesis sound and grounded in the rule |
| Completeness | omits material issues | covers everything material to the question |
| Clarity | muddled, inconsistent | precise, readable for the reader |
| Jurisdiction fit | confuses systems/rules | correct for the governing law |
| Grounding (anti-hallucination) | claims with no basis | every claim has a basis |

## Decision

- **Send** - Layer 1 clean and subjective average >= 4, no dimension < 3.
- **Revise** - Layer 1 clean but a dimension scores 2-3 (name it).
- **Full verification** - Layer 1 has a mismatch or a dimension = 1 -> route to grounding / adversarial review.

## Output format

```
LAYER 1 (objective): citations OK/X | provisions OK/X | dockets OK/X | completeness OK/X
LAYER 2 (1-5 rubric):
  Legal correctness: 4 - <reason>
  Completeness: 3 - <...>
  Clarity: 5 - <...>
  Jurisdiction fit: 4 - <...>
  Grounding: 4 - <...>
  Average: 4.0
DECISION: Revise (Completeness 3 - limitation period not addressed)
```

## Limits

- The subjective score is the model's judgement against a rubric, not an oracle - at high stakes the
  final call is the lawyer's, and the scorecard is evidence of due diligence.
- Layer 1 does not replace the tools it calls - it aggregates them into one decision.
- It scores the output; it does not create or fix it.

## Attribution

Two-layer method (objective matching + a subjective LLM-as-judge rubric on a 1-5 scale) based on
**DISC-Law-Eval** from DISC-LawLLM (Fudan DISC Lab), Apache-2.0. Exam data and judge model dropped;
rubric dimensions, thresholds and framing are MateMatic's own. MateMatic interpretation, not the
position of any bar or regulator.
