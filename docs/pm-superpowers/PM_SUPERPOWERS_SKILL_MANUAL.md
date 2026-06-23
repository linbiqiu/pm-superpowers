# PM Superpowers 技能说明书

这份文档说明插件内 86 个技能的结构：18 个 PM Superpowers 场景/治理技能，68 个内置 PM 方法技能。使用者通常不需要自己挑 68 个方法技能，插件会按场景自动编排。

## 技能总览

PM Superpowers 的技能分两层：

- 场景/治理层：负责判断场景、组织步骤、设置门禁、统一中文产物和下游交接。
- 方法库层：负责具体产品方法，如 PRD、用户研究、竞品分析、指标、实验、GTM、路线图。

终端用户只需要安装 PM Superpowers 插件，不需要额外安装 `pm-skills` 插件集。

## 场景/治理技能总览

| 技能 | 类型 | 作用 |
| --- | --- | --- |
| `pm-workflow-router` | 入口 | 判断用户请求属于哪个产品场景 |
| `pm-intake-triage` | 入口 | 澄清模糊需求，形成 product brief |
| `evidence-classifier` | 控制 | 区分事实、用户原话、信号、假设、意见和承诺 |
| `pm-gate-review` | 控制 | 判断当前产物是否能进入下一步 |
| `pm-decision-log` | 控制 | 记录决策、选项、依据、owner 和开放问题 |
| `downstream-readiness` | 控制 | 检查是否能交给 UI 或研发 |
| `post-launch-learning` | 控制 | 上线后复盘和学习闭环 |
| `pm-project-initializer` | 项目管理 | 初始化产品项目工作区、AGENTS.md、决策记录和项目上下文 |
| `new-product-discovery` | 场景 | 新产品或新功能探索 |
| `existing-product-optimization` | 场景 | 已有产品优化 |
| `feedback-to-roadmap` | 场景 | 反馈转需求池和路线图 |
| `prd-standardization` | 场景 | PRD 起草、改写、评审和交接 |
| `user-research` | 场景 | 用户研究计划、访谈和洞察 |
| `prioritization-roadmap` | 场景 | 优先级和路线图 |
| `metrics-experiments` | 场景 | 指标、数据分析和实验 |
| `strategy-business-model` | 场景 | 战略、市场、竞品、商业模式 |
| `launch-readiness` | 场景 | 上线准备和 GTM |
| `pm-operations` | 场景 | 会议、sprint、复盘、OKR、协作运营 |

## 推荐调用顺序

大多数任务推荐这样走：

1. `pm-workflow-router`
2. 对应场景技能
3. `evidence-classifier`
4. `pm-gate-review`
5. 需要交接时运行 `downstream-readiness`
6. 上线后运行 `post-launch-learning`

如果用户希望把工作沉淀为一个可持续管理的产品项目，先运行 `pm-project-initializer`。

如果一开始信息不够，先走 `pm-intake-triage`。

## 入口技能

### pm-workflow-router

用于判断工作流。它不负责深度产出，而是回答：

- 这是哪个产品场景？
- 信心高不高？
- 输入是否足够？
- 下一步应该使用哪个技能？
- 是否需要先阻塞？

适合用户说：

```text
帮我判断这个产品问题该怎么推进。
```

### pm-intake-triage

用于模糊需求澄清。它会把一句话需求变成结构化 product brief，并判断是否能继续。

适合用户说：

```text
这个想法还比较粗，先帮我梳理清楚。
```

## 控制技能

### evidence-classifier

用于任何需要判断证据质量的场景。它强制区分：

- Fact：事实。
- User Quote：用户原话。
- Signal：多条证据形成的信号。
- Assumption：假设。
- Opinion：意见。
- Commitment：承诺。

它会防止团队把观点包装成事实。

### pm-gate-review

用于阶段门禁。它判断当前材料是否可以进入下一步。

典型检查：

- 探索是否可以进入 PRD？
- PRD 是否可以进入设计？
- PRD 是否可以进入研发？
- 上线是否准备好？
- 发布后是否形成学习？

### pm-decision-log

用于记录决策。它解决的是“过两周没人记得为什么这么定”的问题。

记录内容：

- 做了什么决定。
- 当时有哪些选项。
- 依据是什么。
- 谁负责。
- 还有什么没定。

### downstream-readiness

用于 PM 到 UI、研发的交接检查。

它不会替 UI 或研发做事，而是判断 PM 输入是否足够，让下游不用猜。

### post-launch-learning

用于上线后的复盘。它会检查：

- 结果是否达到预期。
- 用户反馈是什么。
- 数据是否可信。
- 应该继续、迭代、回滚还是重新探索。

### pm-project-initializer

用于初始化产品项目工作区。它会创建或更新：

- `AGENTS.md`
- `product-space/context/product-context.md`
- `product-space/context/stakeholders.md`
- `product-space/decisions/decision-log.md`
- `product-space/evidence/evidence-table.md`
- `product-space/workflows/workflow-state.md`
- `product-space/risks/risk-register.md`
- `product-space/handoffs/downstream-readiness.md`

适合用户说：

```text
请初始化当前项目的产品工作区，并创建 AGENTS.md、决策记录、证据表和下游交接检查。
```

这个技能不会在用户毫无请求时自动改项目。它会在用户明确要求初始化或项目化管理时触发，并尽量保留已有文件内容。

## 十个场景技能

### new-product-discovery

新产品或新功能探索。底层常用 skills：

- `user-segmentation`
- `user-personas`
- `job-stories`
- `opportunity-solution-tree`
- `identify-assumptions-new`
- `prioritize-assumptions`
- `brainstorm-experiments-new`
- `value-proposition`

输出：产品 brief、机会树、假设地图、验证实验计划。

### existing-product-optimization

已有产品优化。底层常用 skills：

- `customer-journey-map`
- `north-star-metric`
- `metrics-dashboard`
- `cohort-analysis`
- `brainstorm-ideas-existing`
- `brainstorm-experiments-existing`
- `pre-mortem`

输出：现状诊断、指标计划、优化实验、优化 backlog。

### feedback-to-roadmap

反馈转路线图。底层常用 skills：

- `analyze-feature-requests`
- `sentiment-analysis`
- `prioritize-features`
- `outcome-roadmap`
- `stakeholder-map`

输出：反馈主题、证据表、路线图候选、取舍说明。

### prd-standardization

PRD 标准化。底层常用 skills：

- `create-prd`
- `job-stories`
- `user-stories`
- `test-scenarios`
- `pre-mortem`
- `wwas`

输出：标准 PRD、验收标准、开放问题、下游交接检查。

### user-research

用户研究。底层常用 skills：

- `interview-script`
- `summarize-interview`
- `user-personas`
- `customer-journey-map`
- `identify-assumptions-new`
- `prioritize-assumptions`

输出：研究计划、访谈脚本、洞察总结、假设验证清单。

### prioritization-roadmap

优先级和路线图。底层常用 skills：

- `prioritization-frameworks`
- `prioritize-features`
- `outcome-roadmap`
- `brainstorm-okrs`
- `stakeholder-map`
- `strategy-red-team`

输出：优先级评分、outcome roadmap、取舍和决策记录。

### metrics-experiments

指标和实验。底层常用 skills：

- `north-star-metric`
- `metrics-dashboard`
- `sql-queries`
- `ab-test-analysis`
- `cohort-analysis`
- `dummy-dataset`

输出：指标方案、实验方案、SQL 请求、结果解读。

### strategy-business-model

战略和商业模式。底层常用 skills：

- `product-vision`
- `product-strategy`
- `market-segments`
- `market-sizing`
- `competitor-analysis`
- `swot-analysis`
- `business-model`
- `pricing-strategy`
- `ideal-customer-profile`

输出：战略备忘录、市场分析、ICP、定位和商业模式建议。

### launch-readiness

上线准备和 GTM。底层常用 skills：

- `gtm-strategy`
- `gtm-motions`
- `beachhead-segment`
- `ideal-customer-profile`
- `competitive-battlecard`
- `release-notes`
- `shipping-artifacts`

输出：上线清单、GTM 计划、release notes、风险和回滚计划。

### pm-operations

PM 日常运营。底层常用 skills：

- `summarize-meeting`
- `sprint-plan`
- `retro`
- `stakeholder-map`
- `brainstorm-okrs`
- `strategy-red-team`

输出：会议纪要、行动项、决策记录、sprint 或 OKR 计划。

## 场景/治理技能和方法技能的关系

内置 68 个 PM 方法技能可以单独使用，但新员工通常不知道什么时候用、怎么串起来、什么时候停止。PM Superpowers 补的是这三件事：

- 什么时候用。
- 用什么顺序。
- 什么条件下不能继续。

所以后续维护时建议：

- 原子方法新增到底层 PM method skills 清单，并同步到 PM Superpowers 插件。
- 场景流程新增到 PM Superpowers。
- 公司规范和门禁新增到 PM Superpowers references。
- 输出格式新增到 PM Superpowers templates。
