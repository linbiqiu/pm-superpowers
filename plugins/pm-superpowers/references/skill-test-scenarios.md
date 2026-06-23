# PM Superpowers Test Scenarios

Use these prompts to forward-test routing and workflow behavior. The machine-readable regression version is `behavior-regression-cases.json`; run `plugins/pm-superpowers/scripts/validate_behavior_regression.py` before release.

## Routing

| Prompt | Expected route |
| --- | --- |
| "我们想做一个面向销售团队的 AI 周报功能，帮我看看怎么推进" | `new-product-discovery`, with assumptions and discovery plan before PRD |
| "用户一直说导出不好用，帮我排个需求池" | `feedback-to-roadmap`, with evidence classification |
| "这份 PRD 能不能交给研发" | `pm-gate-review` then `downstream-readiness` |
| "上线前还有哪些事情没准备" | `launch-readiness` |
| "我们上周版本效果不明显，下一步怎么复盘" | `post-launch-learning` |

## Behavior Regression Cases

| Case | Prompt | Expected behavior | Must not happen |
| --- | --- | --- | --- |
| 模糊想法不直接进 PRD | "老板说我们也要做一个 AI 助手，帮我写 PRD。" | 先进入 `pm-intake-triage`、`pm-workflow-router` 或 `new-product-discovery`，补用户、问题、证据和决策。 | 不要直接调用 `create-prd` 产出工程可交付 PRD。 |
| 客户请求不照单进路线图 | "客户说一定要 Excel 导出，销售也说很重要，帮我排进路线图。" | 先用 `feedback-to-roadmap` 和 `evidence-classifier` 区分用户原话、信号、意见、承诺和频率/严重度。 | 不要把客户提出的方案直接承诺为 roadmap item。 |
| 缺验收标准不能交研发 | "这份 PRD 没写验收标准，但能不能先交给研发开做？" | 运行 `pm-gate-review` 或 `downstream-readiness`，缺 scope 或验收标准时标记 `BLOCKED`。 | 不要标记工程交接已就绪。 |
| 缺监控回滚不能上线 | "功能明天上线，但还没有监控和回滚方案，帮我做上线计划。" | 运行 `launch-readiness`，缺监控或回滚时标记 `BLOCKED` 或显式列为负责人明确的风险。 | 不要宣称上线准备完成。 |
| 方法技能允许直通 | "直接用 market-sizing 帮我估算这个市场规模，不要先套完整 PM Superpowers 场景流程。" | 允许直接使用 `market-sizing`，默认中文输出；只有进入 PRD、路线图承诺、UI/研发交接或上线计划时再加门禁。 | 不要强制先套 S0-S10 完整流程。 |

## Blocking Behavior

The plugin should block when:

- A PRD is requested but user/problem/scope are not known.
- A roadmap is requested without candidate items or decision horizon.
- A launch plan is requested without release scope.
- A launch plan lacks monitoring, rollback, or a release owner.
- A metric analysis is requested with no metric definition or decision.
- Engineering handoff is requested without scope or acceptance criteria.

## Expected Output Qualities

- Every workflow states the selected scene.
- Assumptions and evidence are separated.
- The next step is explicit.
- Handoff readiness is not claimed unless the required fields are present.
- Bundled PM method skills are used as supporting methods, while PM Superpowers remains responsible for routing, gates, templates, and handoff quality.
- Explicitly named PM method skills can be used directly without forcing a full scenario workflow.
