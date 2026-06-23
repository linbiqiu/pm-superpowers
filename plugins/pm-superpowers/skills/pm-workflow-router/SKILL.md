---
name: pm-workflow-router
description: "Use when a product-management request needs to be classified into the right PM Superpowers workflow, especially vague, multi-step, or cross-functional PM work involving discovery, PRD, roadmap, metrics, launch, operations, UI handoff, or engineering handoff."
---

# PM Workflow Router

Route the user's request before doing PM work.

## Required References

Read `../../references/chinese-output-standard.md` first. Read `../../references/scene-taxonomy.md`. Read `../../references/supporting-pm-skills.md` when selecting supporting method skills.

## Workflow

1. Restate the user's request as a PM job.
2. Classify the request into one primary scene from `S0` to `S10`.
3. Identify secondary scenes only if they are likely follow-up workflows.
4. Check the minimum inputs for the selected scene.
5. Decide whether to continue, ask clarifying questions, or run a gate review.
6. Name the next PM Superpowers skill and the expected artifact.

## Routing Output

Use this format:

```markdown
## 工作流路由

- 场景：
- 判断信心：
- 输入质量：
- 用户任务：
- 推荐工作流：
- 可配合使用的 PM skills：
- 预期产物：
- 门禁状态：
- 缺失信息：
- 下一步：
```

## Rules

- If the request is too vague, route to `pm-intake-triage`.
- If the user asks whether work is ready, route to `pm-gate-review`.
- If the user asks whether it can go to UI or engineering, route to `downstream-readiness`.
- Do not produce a PRD, roadmap, or launch plan during routing unless the user explicitly asked for both routing and output.
- Prefer the earliest unresolved product stage when multiple workflows apply.
