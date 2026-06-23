# 下游交接标准

当产品产物要交给 UI 智能体、设计、研发或测试时，使用这份标准。默认面向用户输出中文。

## 产品到 UI 智能体交接

Required before UI generation:

- Target users and top jobs.
- Primary user flow.
- Page or screen inventory.
- Key states: empty, loading, success, error, partial, permission-limited.
- Content requirements and terminology.
- UX constraints and non-goals.
- Accessibility or platform constraints.
- Open questions that affect design.

Recommended artifacts:

- Product brief.
- PRD or feature brief.
- Customer journey map.
- Acceptance criteria.
- Evidence table.

## UI 到研发交接

Required before engineering:

- Final or current UI artifact location.
- Functional requirements.
- Data requirements and API assumptions.
- State and edge-case behavior.
- Analytics events.
- Acceptance criteria.
- Release and rollout constraints.
- Known technical risks or dependencies.

## PM 到研发交接

Required before direct engineering:

- Problem and outcome.
- Scope and non-goals.
- User stories or job stories.
- Acceptance criteria.
- Metrics and instrumentation.
- Dependencies.
- Rollout, rollback, and support plan.
- Decision log and open questions.

## 就绪状态

| 状态 | 含义 |
| --- | --- |
| 可交给 UI | UI 智能体可以在不猜核心产品意图的情况下产出有效页面。 |
| 可交给研发 | 研发可以在不代替产品做决策的情况下评估和实现。 |
| 需要 PM 补充 | 缺少产品决策，下游继续会被迫猜。 |
| 需要证据 | 当前方案依赖未验证假设或缺少证据支撑。 |
