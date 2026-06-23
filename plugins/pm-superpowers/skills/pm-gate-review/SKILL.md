---
name: pm-gate-review
description: "Use when checking whether PM work is ready to move forward, including discovery to PRD, PRD to UI, PRD to engineering, roadmap approval, launch readiness, or post-launch learning."
---

# PM Gate Review

Review whether the current PM artifact can safely move to the next stage.

## Required References

Read `../../references/chinese-output-standard.md` first. Read `../../references/gate-system.md`. Read `../../references/downstream-handoff.md` when the next consumer is UI or engineering.

## Workflow

1. Identify the current workflow and the next stage.
2. Determine the decision being supported.
3. Check universal gates and the relevant stage gate.
4. Classify status as `PASS`, `PASS_WITH_RISKS`, or `BLOCKED`.
5. Provide the smallest useful next action.

## Output

Use `../../assets/templates/gate-review.md` when the user needs a document.

Always include:

- Status.
- Passed checks.
- Risks carried forward.
- Blocking gaps.
- Required next input.
- Recommended next PM Superpowers skill.

## Rules

- `PASS_WITH_RISKS` is acceptable only when the risk is named and owned.
- `BLOCKED` must include the exact missing input or decision.
- Do not polish a weak artifact into looking approved.
