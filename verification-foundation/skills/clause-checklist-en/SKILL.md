---
name: clause-checklist-en
description: >
  A clause checklist for a single contract - walks the contract against 41 clause categories
  (the CUAD taxonomy) and marks each one present / absent / risky, so the clause that should
  be there but is missing does not slip through. Extractive (quotes the contract, does not
  paraphrase). Common-law native, jurisdiction-neutral framing. Different from a bulk audit -
  this goes deep on one contract and asks "what is missing and what bites here". Pairs with
  adversarial-legal-review-en and reviewer-en. Use when: "check the clauses in this contract",
  "what is missing from this agreement", "clause spotting", "contract checklist", "review a
  single contract", "which clauses are risky" - before signing, in negotiation, or in DD of
  one contract.
metadata:
  author: Wiesław Mazur / MateMatic
  version: 1.0.0
  inspiration: >
    The 41-category clause taxonomy is based on CUAD (Contract Understanding Atticus Dataset),
    The Atticus Project, licensed CC BY 4.0 (https://www.atticusprojectai.org/cuad). Category
    descriptions and the risk framing are written from scratch. English counterpart of
    klauzule-kontraktowe-pl (which adds Polish-law anchors).
  companion_skills: adversarial-legal-review-en, reviewer-en, legal-syllogism-en
---

# Clause checklist - what a contract is missing, and what bites

## Philosophy

**The most expensive clauses are the ones that are not in the contract.** Reviewing a contract is not
only reading what is written - it is checking that no safeguard this deal needs is absent. This skill
walks the contract against a fixed list of 41 clause categories and, for each, says: present / absent
/ present-but-risky, quoting the clause when present.

It is **extractive** - what it shows comes from the contract, not from paraphrase. It flags presence
and risk; the assessment and the call stay with the lawyer.

## The 41 categories (CUAD taxonomy)

Groups follow CUAD (1-6) plus ungrouped categories. For each: present / absent / risky + a quote when present.

### Contract metadata
- **Document name**, **Parties** (verify authority to sign), **Governing law**.

### Group 1 - term and dates
- Agreement date · Effective date · Expiration date · Renewal term (auto-renew?) · Notice period to terminate renewal.

### Group 2 - competition restrictions
- Non-compete · Exclusivity · No-solicit of customers · Competitive restriction exception (carve-outs).

### Group 3 - control and assignment
- Change of control (consent/termination on M&A?) · Anti-assignment.

### Group 4 - licences
- License grant · Non-transferable license · Affiliate license (licensor) · Affiliate license (licensee) · Unlimited/all-you-can-eat license · Irrevocable or perpetual license.

### Group 5 - post-term and audit
- Post-termination services · Audit rights.

### Group 6 - liability
- Uncapped liability · Cap on liability.

### Ungrouped
- Most favored nation · No-solicit of employees · Non-disparagement · Termination for convenience · ROFR/ROFO/ROFN · Revenue/profit sharing · Price restrictions · Minimum commitment · Volume restriction · IP ownership assignment · Joint IP ownership · Source code escrow · Covenant not to sue · Liquidated damages · Warranty duration · Insurance · Third-party beneficiary.

## Output format

```
RED FLAGS (top):
- ABSENT: <category> - <why it is a risk in this deal>
- RISKY: <category> - <how it is one-sided>

41-CATEGORY TABLE:
| Category | Status | Note | Quote (if present) |
| Governing law | present | New York; courts of NY | "..." |
| Cap on liability | absent | no liability ceiling | - |
...
```

## Limits

- A presence-and-risk checklist, not an interpretation of clause wording. Whether a clause is
  effective, and the recommendation, are the lawyer's.
- The taxonomy is common-law-oriented at source (CUAD); for a specific jurisdiction add local-law
  anchors (for Poland, see klauzule-kontraktowe-pl).
- Descriptive references without a clause ("the parties intend to cooperate") have nothing to match -
  mark as "no clause, manual check".

## Attribution

The 41-category clause taxonomy is based on **CUAD (Contract Understanding Atticus Dataset)**, The
Atticus Project, **CC BY 4.0** (https://www.atticusprojectai.org/cuad). Category descriptions and the
risk framing are MateMatic's own. MateMatic interpretation, not the position of any bar or regulator.
