# PM Superpowers 场景分类规范

用于路由产品管理工作。用户学习时看十个高频场景；插件执行时使用对应技能。默认面向用户输出中文。

## Routing Contract

Always identify:

- `scene_id`: `S0` to `S10`
- `confidence`: high, medium, or low
- `input_quality`: enough, partial, or insufficient
- `next_skill`: one PM Superpowers skill to run next
- `blocked_reason`: concrete missing decision or evidence when blocked
- `expected_artifacts`: documents or tables to produce

Do not move into artifact production when the problem, target user, decision owner, or evidence base is missing. Route to `pm-intake-triage` or `pm-gate-review` first.

## Scene Index

| ID | Scene | Typical user request | Primary PM Superpowers skill | Main artifacts |
| --- | --- | --- | --- | --- |
| S0 | Vague or mixed PM request | "帮我看看这个产品怎么做" | `pm-intake-triage` | clarified brief, routing decision |
| S1 | New product or new feature discovery | "我们想做一个新功能/新产品" | `new-product-discovery` | product brief, opportunity tree, assumptions, validation plan |
| S2 | Existing product optimization | "现有功能效果不好，怎么优化" | `existing-product-optimization` | diagnosis, metric tree, experiment plan, optimization backlog |
| S3 | Feedback or requests to roadmap | "一堆客户反馈怎么整理成需求" | `feedback-to-roadmap` | feedback themes, evidence table, roadmap candidates |
| S4 | PRD standardization | "帮我写/改 PRD" | `prd-standardization` | PRD, user stories, acceptance criteria, open issues |
| S5 | User research | "我要访谈用户/总结访谈" | `user-research` | research plan, interview script, insight summary |
| S6 | Prioritization and roadmap | "这么多需求怎么排优先级" | `prioritization-roadmap` | prioritization table, outcome roadmap, tradeoff memo |
| S7 | Metrics, analytics, and experiments | "怎么定义指标/分析实验" | `metrics-experiments` | metrics plan, SQL request, experiment readout |
| S8 | Strategy and business model | "产品方向/定位/商业模式怎么定" | `strategy-business-model` | strategy memo, market view, ICP, business model |
| S9 | Launch readiness and GTM | "上线前要准备什么" | `launch-readiness` | launch checklist, GTM plan, release notes |
| S10 | PM operations and collaboration | "会议纪要/复盘/迭代计划/跨部门对齐" | `pm-operations` | meeting summary, sprint plan, retro, decision log |

## Scene Selection Rules

- If the user asks "what workflow should I use", route to `pm-workflow-router`.
- If the request lacks product context, target user, intended outcome, or current stage, route to `pm-intake-triage`.
- If the request asks to check whether a document can proceed, route to `pm-gate-review`.
- If the request asks whether work can be handed to UI or engineering, route to `downstream-readiness`.
- If the request is after launch, route to `post-launch-learning` unless it is purely operational.
- If multiple scenes apply, choose the earliest unresolved product stage, then list secondary scenes as follow-up workflows.

## Minimum Inputs by Scene

| Scene | Minimum inputs before continuing |
| --- | --- |
| S1 | target user, problem, business intent, known evidence or assumption statement |
| S2 | existing flow or feature, current metric/symptom, affected segment, baseline if available |
| S3 | raw feedback/request source, customer/user identity or segment, frequency/severity signal |
| S4 | product goal, user flow, scope, non-goals, acceptance criteria owner |
| S5 | research question, target participants, decision that research will inform |
| S6 | candidate items, decision horizon, prioritization criteria, resource constraints |
| S7 | product question, metric definition, data source or tracking gap, decision threshold |
| S8 | market/customer scope, strategic question, constraints, business model hypothesis |
| S9 | release scope, target users, launch date or window, dependencies, risk owner |
| S10 | meeting/project context, stakeholders, decisions needed, timeline |

## Handoff Principles

- Produce learning artifacts before execution artifacts.
- Mark assumptions explicitly before writing confident recommendations.
- Gate each stage before moving to the next stage.
- Preserve decisions and unresolved questions for later agents.
