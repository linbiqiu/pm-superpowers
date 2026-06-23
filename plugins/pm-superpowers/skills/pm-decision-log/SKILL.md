---
name: pm-decision-log
description: "Use when PM work needs decisions, owners, options, tradeoffs, commitments, or open questions tracked across discovery, PRD, roadmap, launch, or cross-functional collaboration."
---

# PM Decision Log

Capture product decisions so future agents and teammates know why work moved forward.

## Required References

Read `../../references/chinese-output-standard.md` first. Read `../../references/evidence-taxonomy.md`. Use `../../assets/templates/decision-log.md` for reusable logs.

## Workflow

1. Extract decisions already made.
2. Extract open decisions and dependencies.
3. Record options considered and evidence used.
4. Assign owner and follow-up date when available.
5. Highlight decisions blocking UI, engineering, launch, or leadership review.

## Output

Use this structure:

```markdown
## 已做决策

| 决策 | 背景 | 已考虑选项 | 依据 | 负责人 | 后续动作 |
| --- | --- | --- | --- | --- | --- |

## 待决事项

| 待决事项 | 负责人 | 截止时间 | 阻断什么 |
| --- | --- | --- | --- |
```

## Rules

- Separate a decision from a recommendation.
- Do not invent owner names.
- Mark unresolved product choices before any downstream handoff.
