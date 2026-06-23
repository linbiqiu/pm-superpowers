# PM Superpowers Test Scenarios

Use these prompts to forward-test routing and workflow behavior.

## Routing

| Prompt | Expected route |
| --- | --- |
| "我们想做一个面向销售团队的 AI 周报功能，帮我看看怎么推进" | `new-product-discovery`, with assumptions and discovery plan before PRD |
| "用户一直说导出不好用，帮我排个需求池" | `feedback-to-roadmap`, with evidence classification |
| "这份 PRD 能不能交给研发" | `pm-gate-review` then `downstream-readiness` |
| "上线前还有哪些事情没准备" | `launch-readiness` |
| "我们上周版本效果不明显，下一步怎么复盘" | `post-launch-learning` |

## Blocking Behavior

The plugin should block when:

- A PRD is requested but user/problem/scope are not known.
- A roadmap is requested without candidate items or decision horizon.
- A launch plan is requested without release scope.
- A metric analysis is requested with no metric definition or decision.

## Expected Output Qualities

- Every workflow states the selected scene.
- Assumptions and evidence are separated.
- The next step is explicit.
- Handoff readiness is not claimed unless the required fields are present.
- Existing PM skills are referenced as supporting methods, not duplicated.
