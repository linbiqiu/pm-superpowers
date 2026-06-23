---
name: evidence-classifier
description: "Use when PM work contains user feedback, research notes, analytics, stakeholder opinions, claims, assumptions, or mixed evidence that must be labeled before decisions, PRDs, roadmaps, or experiments."
---

# Evidence Classifier

Classify claims so product decisions do not treat assumptions as facts.

## Required References

Read `../../references/chinese-output-standard.md` first. Read `../../references/evidence-taxonomy.md`. Read `../../assets/templates/evidence-table.md` if the user needs a reusable artifact.

## Workflow

1. Extract each important claim from the source material.
2. Label every claim as Fact, User Quote, Signal, Assumption, Opinion, or Commitment.
3. Assign confidence: high, medium, or low.
4. State the product implication.
5. Mark whether validation is required before moving forward.

## Output

Use this table:

```markdown
| 主张 | 类型 | 来源 | 信心 | 产品含义 | 是否需要验证 |
| --- | --- | --- | --- | --- | --- |
```

Then summarize:

- 最强证据。
- 风险最高的假设。
- 可以继续推进的决策。
- 被阻断的决策。

## Rules

- Do not generalize from one quote unless you label it as a low-confidence signal.
- Treat stakeholder preference as Opinion unless backed by data, customer evidence, or a commitment.
- Commitments require owners and dates when possible.
