# Existing 68 PM Skills as the Method Library

PM Superpowers does not replace the existing 68 PM skills. It treats them as the bottom-layer method library and adds four missing layers on top:

1. Scene routing: decide which workflow applies.
2. Workflow sequencing: combine multiple method skills into a complete PM workflow.
3. Gates: block premature output when core thinking is missing.
4. Handoff standards: prepare artifacts for UI and engineering agents.

When a step names one of these existing skills and the skill is available, use it. If the skill is unavailable in a future environment, follow the workflow and produce a compatible artifact from the templates.

## Handling Strategy for the 68 Skills

| Treatment | Meaning |
| --- | --- |
| Keep as-is | The skill remains an atomic PM method and can be invoked directly. |
| Orchestrate | PM Superpowers calls or references the skill as one step in a scenario workflow. |
| Govern | PM Superpowers checks the skill's output with evidence, gate, and handoff rules. |
| Extend only if missing | New PM Superpowers skills cover workflow gaps, not duplicate method logic. |

## Product Discovery

- `analyze-feature-requests`: turn requests into themes and opportunities.
- `brainstorm-experiments-existing`: experiments for an existing product.
- `brainstorm-experiments-new`: experiments for a new product.
- `brainstorm-ideas-existing`: solution ideas for an existing product.
- `brainstorm-ideas-new`: solution ideas for a new product.
- `identify-assumptions-existing`: assumptions in existing-product work.
- `identify-assumptions-new`: assumptions in new-product work.
- `interview-script`: user interview scripts.
- `job-stories`: job stories and situation-motivation-outcome framing.
- `opportunity-solution-tree`: opportunity and solution tree.
- `prioritize-assumptions`: rank assumptions by risk and uncertainty.
- `summarize-interview`: extract insights from interviews.
- `user-personas`: personas for target users.
- `user-segmentation`: user segmentation.
- `value-prop-statements`: value-proposition statements.
- `value-proposition`: value proposition development.

## Product Strategy

- `ansoff-matrix`: growth direction by market/product expansion.
- `business-model`: business model choices.
- `lean-canvas`: lean canvas for early ideas.
- `monetization-strategy`: monetization model.
- `north-star-metric`: north star metric definition.
- `pestle-analysis`: macro-environment scan.
- `porters-five-forces`: industry structure analysis.
- `pricing-strategy`: pricing strategy.
- `product-name`: product naming.
- `product-strategy`: product strategy synthesis.
- `product-vision`: product vision.
- `startup-canvas`: startup canvas.
- `swot-analysis`: strengths, weaknesses, opportunities, threats.

## Execution

- `brainstorm-okrs`: OKR generation.
- `create-prd`: product requirement document drafting.
- `dummy-dataset`: dummy data for examples or demos.
- `outcome-roadmap`: outcome-based roadmap.
- `pre-mortem`: risk pre-mortem.
- `prioritization-frameworks`: RICE, MoSCoW, Kano, and other prioritization approaches.
- `prioritize-features`: feature prioritization.
- `release-notes`: release notes.
- `retro`: retrospective.
- `sprint-plan`: sprint planning.
- `stakeholder-map`: stakeholder mapping.
- `strategy-red-team`: challenge strategy and assumptions.
- `summarize-meeting`: meeting summary.
- `test-scenarios`: test scenarios.
- `user-stories`: user stories.
- `wwas`: working backwards artifacts.

## Market Research

- `competitor-analysis`: competitor research.
- `customer-journey-map`: customer journey mapping.
- `market-segments`: market segment analysis.
- `market-sizing`: TAM/SAM/SOM and sizing.

## Data Analytics

- `ab-test-analysis`: A/B test analysis.
- `cohort-analysis`: cohort analysis.
- `metrics-dashboard`: metrics dashboard design.
- `sentiment-analysis`: sentiment analysis.
- `sql-queries`: SQL query drafting.

## Go To Market

- `beachhead-segment`: beachhead segment selection.
- `competitive-battlecard`: competitive battlecard.
- `growth-loops`: growth loop design.
- `gtm-motions`: GTM motion selection.
- `gtm-strategy`: go-to-market strategy.
- `ideal-customer-profile`: ideal customer profile.

## Marketing And Growth

- `marketing-ideas`: marketing ideas.
- `positioning-ideas`: positioning ideas.

## AI Shipping

- `intended-vs-implemented`: compare intended behavior and implementation.
- `shipping-artifacts`: shipping artifact generation.

## Toolkit And Operations

- `competitive-battlecard`: sales and competitive enablement.
- `draft-nda`: NDA drafting support.
- `grammar-check`: grammar checking.
- `privacy-policy`: privacy policy drafting support.
- `review-resume`: resume review.

## Workflow Mapping

| PM Superpowers workflow | Common supporting PM skills |
| --- | --- |
| `new-product-discovery` | `user-segmentation`, `user-personas`, `job-stories`, `opportunity-solution-tree`, `identify-assumptions-new`, `prioritize-assumptions`, `brainstorm-experiments-new`, `value-proposition` |
| `existing-product-optimization` | `customer-journey-map`, `north-star-metric`, `metrics-dashboard`, `cohort-analysis`, `brainstorm-ideas-existing`, `brainstorm-experiments-existing`, `pre-mortem` |
| `feedback-to-roadmap` | `analyze-feature-requests`, `sentiment-analysis`, `prioritize-features`, `outcome-roadmap`, `stakeholder-map` |
| `prd-standardization` | `create-prd`, `job-stories`, `user-stories`, `test-scenarios`, `pre-mortem` |
| `user-research` | `interview-script`, `summarize-interview`, `user-personas`, `customer-journey-map`, `identify-assumptions-new` |
| `prioritization-roadmap` | `prioritization-frameworks`, `prioritize-features`, `outcome-roadmap`, `brainstorm-okrs`, `stakeholder-map` |
| `metrics-experiments` | `north-star-metric`, `metrics-dashboard`, `sql-queries`, `ab-test-analysis`, `cohort-analysis`, `dummy-dataset` |
| `strategy-business-model` | `product-vision`, `product-strategy`, `market-segments`, `market-sizing`, `competitor-analysis`, `swot-analysis`, `business-model`, `pricing-strategy` |
| `launch-readiness` | `gtm-strategy`, `gtm-motions`, `beachhead-segment`, `ideal-customer-profile`, `competitive-battlecard`, `release-notes`, `shipping-artifacts` |
| `pm-operations` | `summarize-meeting`, `sprint-plan`, `retro`, `stakeholder-map`, `brainstorm-okrs`, `strategy-red-team` |
