---
name: downstream-readiness
description: "Use when product work must be checked or prepared for UI generation, design handoff, engineering planning, implementation, QA, or an agent-to-agent workflow from PM to UI to development."
---

# Downstream Readiness

Check whether PM output is ready for UI and engineering agents.

## Required References

Read `../../references/chinese-output-standard.md` first. Read `../../references/downstream-handoff.md` and `../../references/gate-system.md`.

## Workflow

1. Identify the target handoff: UI, engineering, or both.
2. Check the required PM inputs for that handoff.
3. Identify missing decisions that would force downstream agents to guess.
4. Classify readiness.
5. Produce a handoff checklist or block with required PM clarification.

## Output

Use `../../assets/templates/downstream-readiness.md` when creating an artifact.

Always include:

- Target handoff.
- Readiness status.
- Present inputs.
- Blocking gaps.
- Required next PM artifact.
- Recommended next agent: PM, UI, or engineering.

## Rules

- Do not mark engineering ready without acceptance criteria and scope.
- Do not mark UI ready without users, flow, states, and constraints.
- Carry open questions forward instead of hiding them.
