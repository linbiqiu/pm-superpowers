# 内置 68 个 PM 方法技能

PM Superpowers 内置 68 个 PM 方法技能作为底层方法库。终端用户只需要安装 PM Superpowers 插件，不需要额外安装 `pm-skills` 插件集。

PM Superpowers 不把 68 个方法技能重写成一个大技能，而是保留它们的原子能力，并在上层补齐四件事：

1. 场景路由：判断当前请求应该进入哪个产品工作流。
2. 工作流编排：把多个方法技能组合成完整 PM 工作流。
3. 门禁治理：当核心问题没想清楚时阻断，不强行输出完整文档。
4. 下游交接：把产物整理到 UI 和研发智能体可以继续工作的程度。

当场景步骤需要某个方法技能时，优先使用插件内置的同名技能。如果未来环境里某个方法技能不可用，仍要按照场景工作流和中文模板产出兼容结果，并说明能力缺口。

## PM method skills 直通契约

为了避免 PM Superpowers 的场景层限制底层方法技能，用户明确点名某个底层方法技能或明确要求使用某个产品方法时，允许直通执行该 PM method skill。

直通规则：

- 用户明确说“直接用 `market-sizing`”“用 `ab-test-analysis` 分析实验”“帮我跑 `interview-script`”时，优先执行被点名的方法技能。
- 直通输出只受 `chinese-output-standard.md` 约束，默认中文输出，不强制套完整场景工作流。
- 直通方法产物如果只是学习、分析或草稿，可以直接输出并标注关键假设。
- 直通方法产物如果要变成 PRD、路线图承诺、UI/研发交接或上线计划，再运行 `pm-gate-review` 或 `downstream-readiness`。
- 场景/治理技能不得把 68 个 PM method skills 改写成更浅的同名替代品。

简言之：方法可以直通，承诺仍需门禁。

## 68 个技能的处理策略

| Treatment | Meaning |
| --- | --- |
| 原样保留 | 方法技能仍然是一个独立的 PM 原子方法，可以被直接触发。 |
| 场景编排 | PM Superpowers 在具体场景中选择和组合这些方法技能。 |
| 门禁治理 | PM Superpowers 用证据、门禁、交接规则检查方法技能产物。 |
| 缺口扩展 | 只有缺少场景流、门禁、模板或交接标准时，才新增 PM Superpowers 技能。 |

## 更新策略

- 终端用户不需要关心 68 个方法技能的安装。
- 插件开发人员通过 `plugins/pm-superpowers/scripts/sync_pm_skills.py` 从认可来源同步 68 个方法技能；同步脚本会自动注入中文输出要求。
- 同步后必须运行插件校验和全部技能校验。
- 如果新增的是独立产品方法，先进入 PM 方法技能清单，再同步到插件。
- 如果新增的是公司场景、流程、门禁、模板或下游交接标准，直接更新 PM Superpowers 的场景/治理层。

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
