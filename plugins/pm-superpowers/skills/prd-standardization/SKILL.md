---
name: prd-standardization
description: "Use when drafting, rewriting, reviewing, or standardizing a PRD, feature spec, requirements document, user stories, acceptance criteria, or development-ready product requirement."
---

# PRD Standardization

Create or review PRDs with consistent structure and gates.

## Required References

Read `../../references/chinese-output-standard.md` first. Read `../../references/gate-system.md`, `../../references/evidence-taxonomy.md`, `../../references/downstream-handoff.md`, and `../../references/supporting-pm-skills.md`.

## Supporting PM Skills

Use available method skills when useful: `create-prd`, `job-stories`, `user-stories`, `test-scenarios`, `pre-mortem`, `stakeholder-map`, and `wwas`.

## Workflow

1. Confirm the PRD consumer and decision stage.
2. Check problem, user, evidence, scope, metrics, dependencies, and risks.
3. Draft or rewrite the PRD using the standard template.
4. Create user stories or job stories.
5. Define acceptance criteria and edge cases.
6. Run `pm-gate-review`.
7. Run `downstream-readiness` if the PRD is intended for UI or engineering.

## Artifacts

Use:

- `../../assets/templates/prd.md`
- `../../assets/templates/acceptance-criteria.md`
- `../../assets/templates/gate-review.md`
- `../../assets/templates/downstream-readiness.md`

## Block Conditions

Block when the request asks for an engineering-ready PRD but scope, acceptance criteria, or target user is missing.
