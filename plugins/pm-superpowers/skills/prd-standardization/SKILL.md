---
name: prd-standardization
description: "Use when drafting, rewriting, reviewing, or standardizing a PRD, feature spec, requirements document, user stories, acceptance criteria, or development-ready product requirement."
---

# PRD Standardization

Create or review PRDs with adaptive structure and gates. Do not force every request into one full PRD shape.

## Required References

Read `../../references/chinese-output-standard.md` first. Read `../../references/gate-system.md`, `../../references/evidence-taxonomy.md`, `../../references/downstream-handoff.md`, and `../../references/supporting-pm-skills.md`.

## Supporting PM Skills

Use available method skills when useful: `create-prd`, `job-stories`, `user-stories`, `test-scenarios`, `pre-mortem`, `stakeholder-map`, and `wwas`.

## Workflow

1. Confirm the PRD consumer and decision stage.
2. Select the PRD type before drafting: lightweight requirement, standard feature PRD, UI/experience PRD, backend/API/data PRD, optimization/experiment PRD, or launch/operations PRD.
3. Check problem, user or affected role, evidence, scope, metrics, dependencies, risks, and intended downstream consumer.
4. Draft or rewrite the PRD using only the applicable modules in `../../assets/templates/prd.md`.
5. Mark non-applicable modules as "本次不适用" with a short reason instead of inventing content.
6. Create user stories, job stories, or system scenarios only when they fit the PRD type.
7. Define acceptance criteria and edge cases appropriate to the PRD type.
8. Run `pm-gate-review`.
9. Run `downstream-readiness` only if the PRD is intended for UI or engineering handoff.

## Artifacts

Use:

- `../../assets/templates/prd.md`
- `../../assets/templates/acceptance-criteria.md`
- `../../assets/templates/gate-review.md`
- `../../assets/templates/downstream-readiness.md`

## Block Conditions

Block when the request asks for an engineering-ready PRD but scope, acceptance criteria, or target user / affected role is missing.

Do not block merely because a module is not applicable. For example, backend-only, configuration, data, or operations PRDs may not need UI states; lightweight copy changes may not need experiment design. Record the non-applicability and continue if the core decision, scope, and acceptance criteria are clear.
