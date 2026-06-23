# PM 门禁系统

用门禁防止产品工作在没想清楚时进入下一步。默认面向用户输出中文；状态值保留 `PASS`、`PASS_WITH_RISKS`、`BLOCKED`，方便插件和团队统一判断。

## Status Values

| 状态 | 含义 | 下一步 |
| --- | --- | --- |
| `PASS` | Inputs and reasoning are sufficient for the next workflow step. | Continue and produce the next artifact. |
| `PASS_WITH_RISKS` | Work can continue, but named risks or assumptions must remain visible. | Continue, but carry risks into the artifact. |
| `BLOCKED` | A core question, decision, or evidence requirement is missing. | Stop and ask for or derive the missing input. |

## Universal Gate Questions

1. What decision is this work supposed to support?
2. Who is the target user or customer segment?
3. What evidence is factual, and what is only an assumption?
4. What outcome or metric defines success?
5. What scope is explicitly in and out?
6. Who owns the decision and follow-up?
7. What downstream team will consume the output?

## Stage Gates

| Gate | Use before | Required proof |
| --- | --- | --- |
| Problem gate | solution brainstorming or PRD | clear user/problem statement, evidence or assumption labels |
| Opportunity gate | roadmap or strategy | target segment, opportunity size or severity, business relevance |
| Solution gate | PRD or design handoff | selected solution, alternatives considered, tradeoffs |
| Scope gate | sprint or dev handoff | in-scope, out-of-scope, dependencies, acceptance criteria |
| Metrics gate | launch or experiment | success metrics, guardrail metrics, measurement plan |
| Risk gate | launch or executive review | top risks, mitigation, owner, decision deadline |
| Handoff gate | UI or engineering agent | user flow, states, edge cases, constraints, open questions |
| Learning gate | post-launch iteration | result vs expectation, decision to keep/iterate/rollback |

## Blocking Rules

Return `BLOCKED` when any of these are missing:

- The work has no explicit decision or next consumer.
- The target user or customer segment is unknown.
- The request asks for a PRD, roadmap, or launch plan without a problem statement.
- Success metrics are needed but no metric or observable behavior is defined.
- The artifact would require facts that are not present and cannot be safely inferred.
- The handoff asks UI or engineering to build without scope, states, or acceptance criteria.

## Output Format

```markdown
## 门禁检查

- 状态：
- 当前工作流：
- 支持的决策：
- 已通过检查：
- 需要携带的风险：
- 阻断缺口：
- 需要补齐的信息：
- 推荐下一步技能：
```
