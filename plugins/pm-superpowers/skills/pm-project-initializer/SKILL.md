---
name: pm-project-initializer
description: "Use when the user wants to initialize, standardize, or manage a product project workspace with AGENTS.md, product context, decision log, evidence table, workflow state, risk register, handoff files, or persistent PM project documentation."
---

# PM Project Initializer

Initialize or update a product project workspace so PM Superpowers can manage product work as a project, not just one-off chat output.

## Required References

Read `../../references/chinese-output-standard.md` first. Read `../../references/project-workspace-standard.md`.

## Workflow

1. Confirm the target directory. If the user says "current project", use the current workspace root.
2. Inspect existing files before writing. Do not overwrite an existing `AGENTS.md` or decision log without preserving user content.
3. Create missing standard files from `../../assets/project-workspace/`.
4. If `AGENTS.md` already exists, add a PM Superpowers section instead of replacing the file.
5. Record the initial product context, known assumptions, open questions, and first workflow state.
6. Explain the initialized structure and the next recommended PM workflow.

## Standard Files

Create or update:

- `AGENTS.md`
- `product-space/README.md`
- `product-space/context/product-context.md`
- `product-space/context/stakeholders.md`
- `product-space/decisions/decision-log.md`
- `product-space/evidence/evidence-table.md`
- `product-space/workflows/workflow-state.md`
- `product-space/risks/risk-register.md`
- `product-space/handoffs/downstream-readiness.md`

## Rules

- Default all user-facing content to Chinese.
- Treat `AGENTS.md` as the project operating contract for future agents.
- Treat `decision-log.md` as the source of truth for product decisions.
- Treat `workflow-state.md` as the current PM workflow checkpoint.
- Mark missing context explicitly instead of inventing product facts.
- Ask for confirmation only when file conflicts would require replacing user-authored content.
