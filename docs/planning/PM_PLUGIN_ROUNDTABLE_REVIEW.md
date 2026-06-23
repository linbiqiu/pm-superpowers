# PM 插件圆桌评审：场景化产品工作流与查漏补缺

本文档以“圆桌论坛”的方式评审产品经理插件的设计思路。重点不是继续写提示词，而是审视：如果未来要做成类似 `superpowers` 的 Codex 插件，是否应该以十个高频产品场景为入口，背后封装技能流、模板、关卡和学习材料。

## 议题

如何把产品经理高频工作场景做成 Codex 插件，让新人和公司所有 PM 能自动选择正确工作流、按规范输出，并在没想清楚时被阻断？

## 参会者设定

以下人物用于代表不同思想传统。MBTI 为讨论用人格侧写，不作为事实断言。

| 人物 | 讨论用 MBTI | 代表视角 | 为什么邀请 |
| --- | --- | --- | --- |
| Marty Cagan | INTJ | 强调 empowered product teams、产品发现和结果导向 | 能检查插件是否把 PM 变成“写需求的人”，还是帮助团队做产品判断 |
| Teresa Torres | INFJ | Continuous Discovery、机会解决方案树、假设验证 | 能检查场景工作流是否真正从用户和机会出发 |
| Melissa Perri | ENTJ | Product strategy、避免 build trap、产品运营模型 | 能检查插件是否会导致“更快地写更多需求”，而不是避免错误建设 |
| Don Norman | INTP | 以人为本设计、用户心理模型、可用性 | 能检查插件是否忽略用户体验、任务流和认知负担 |
| Kent Beck | INTP | TDD、极限编程、流程纪律和反馈环 | 作为意外视角，检验 PM 插件是否像工程 superpowers 一样有硬关卡和可验证产物 |

## 开场：如何定义这个 PM 插件

【主持】【陈述】：在深入讨论前，我们先定义“产品经理场景化插件”。它不是提示词集合，也不是 PRD 生成器，而是一套嵌入 Codex 的产品工作操作系统。它通过场景路由判断用户要做什么，通过工作流技能组织步骤，通过关卡阻断不成熟输入，通过模板输出标准产物。

**简言之**：PM 插件的核心是“让产品工作按正确流程发生”，不是“帮用户更快写文档”。

【Marty Cagan】【陈述】：如果这个插件只是把 PRD 写得更漂亮，它会强化错误的产品组织。真正的产品工作要从结果、用户、约束和团队判断出发。插件必须让 PM 先说明 desired outcome，而不是直接进入 feature specification。

**简言之**：不要让插件成为 feature factory 的加速器。

【Teresa Torres】【补充】：我会用一个标准检查它：这个插件是否让团队持续识别机会、假设和实验？如果用户说“我要做功能 X”，插件应该问“这解决了哪个机会？哪个假设还没验证？”而不是马上帮他写需求。

**简言之**：场景流必须把“机会和假设”放在“方案和 PRD”之前。

【Melissa Perri】【质疑】：我担心十个场景如果只是按文档类型拆分，会让 PM 误以为产品工作就是产物堆叠。比如 PRD、路线图、指标、上线计划，这些是结果，不是工作本身。插件要帮助团队避免 build trap：别把产出当成果。

**简言之**：场景不是文档分类，而是决策情境分类。

【Don Norman】【补充】：产品场景必须包含用户任务和认知负担。比如“已有产品优化”不能只看指标，也要看用户如何理解系统、在哪里犯错、系统反馈是否清晰。否则插件会偏商业和流程，忽略可用性。

**简言之**：产品工作流必须覆盖用户任务流，不只是业务流程。

【Kent Beck】【修正】：我关心它是否有可执行纪律。研发 superpowers 有 TDD、verification、review。PM 插件也需要类似铁律：没有用户、问题、指标、验收标准，就不能进入下一阶段。否则插件只是建议，不是流程。

**简言之**：PM 插件必须有硬关卡，不只是温和提醒。

## 第一轮：插件方向是否正确

### 核心争议

“PM 插件应该是场景化工作流引擎，还是技能和模板库？”

【Marty Cagan】【陈述】：插件必须先是工作流引擎。技能和模板只是工具。如果用户直接选择 `create-prd`，很可能他在错误时间写 PRD。路由层应该优先于所有具体技能。

**简言之**：先判断场景，再调用技能。

【Teresa Torres】【补充】：路由层还要判断“探索 vs 交付”。很多用户输入看起来像需求，其实处在 discovery 阶段。比如“做一个 AI 客服助手”，这不应该进入 PRD，而应该进入新产品发现。

**简言之**：路由器要识别阶段，而不只识别关键词。

【Melissa Perri】【质疑】：我同意路由，但要小心过度自动化。插件不能假装所有 PM 场景都有唯一正确流程。它应该推荐工作流，并说明假设和置信度。低置信度时必须先澄清。

**简言之**：自动路由要有置信度和可纠错机制。

【Kent Beck】【补充】：这可以借鉴测试设计。路由输出应该像测试结果一样明确：`PASS`、`BLOCKED`、`NEEDS_CLARIFICATION`。不要输出含糊的“建议你可以”。流程状态要机器可读，才能被后续智能体消费。

**简言之**：路由和关卡结果要结构化。

【Don Norman】【质疑】：如果插件只根据用户说法路由，会误判。用户可能说“写 PRD”，但真正需要的是用户研究。系统应该识别用户表达背后的任务，而不是字面请求。

**简言之**：路由器要判断真实任务，而不是服从表面命令。

### 本轮结论

插件方向是正确的，但需要明确三点：

1. `pm-workflow-router` 是最高优先级入口，不是可选功能。
2. 路由器输出必须包含场景、置信度、依据、缺失信息、下一步。
3. 用户要求的动作不一定是正确动作，插件要能纠偏。

```text
用户输入
  |
  v
表面请求 ------------------+
  |                        |
  v                        v
真实产品场景判断 --> 置信度判断 --> 选择工作流 / 阻断澄清
```

## 第二轮：十个高频场景是否完整

当前十个场景：

1. 新产品/新想法探索
2. 已有产品问题优化
3. 客户反馈和功能请求整理
4. 写 PRD/需求文档
5. 用户研究和访谈
6. 功能优先级和路线图
7. 指标和增长实验
8. 产品战略和商业模式
9. 上线发布和风险检查
10. PM 日常运转

### Marty Cagan 的审视

【Marty Cagan】【陈述】：这十个场景覆盖了大部分 PM 工作，但我会重新强调“outcome”。目前 S4 写 PRD、S6 路线图、S9 发布，很容易变成 output-oriented。每个场景都必须要求明确 desired outcome。

**简言之**：每个场景都要从 outcome 开始，不然会变成产物工厂。

### Teresa Torres 的审视

【Teresa Torres】【补充】：S1、S2、S3、S5 都与 discovery 强相关，但它们的边界要清楚。S1 是新产品是否成立；S2 是已有产品机会诊断；S3 是反馈证据整理；S5 是研究方法。它们不应该互相替代。

**简言之**：发现类场景要按“新产品、已有问题、反馈池、研究动作”拆清楚。

### Melissa Perri 的审视

【Melissa Perri】【质疑】：我认为漏了一个高频但关键的场景：需求入口治理，也就是 intake/triage。很多组织的问题不是不会写 PRD，而是任何人都能把请求扔给 PM。插件应该先有“需求入口分流”。

**简言之**：在十个场景之前，需要一个 S0：需求入口治理。

### Don Norman 的审视

【Don Norman】【质疑】：我认为“用户任务流/体验走查”没有被明确表达。它可以放在 S2，也可以作为 S4 到 UI 前的必要检查。如果用户流程、状态、错误和反馈机制不清楚，不应该进入 UI。

**简言之**：必须补一个横切检查：用户任务流是否清楚。

### Kent Beck 的审视

【Kent Beck】【补充】：我看到另一个缺口：post-launch learning。上线不是结束。工程里完成后要验证，产品也要上线后看结果、复盘假设。S9 是 launch readiness，但还需要 release learning。

**简言之**：上线前检查不等于上线后学习。

## 查漏补缺：应补哪些能力

圆桌一致认为：十个场景作为“学习层”基本成立，但插件实现层需要补充几个能力。

### 1. S0：产品需求入口治理

这是最重要的缺口。

为什么重要：

- 公司里大量产品工作从模糊请求开始。
- 请求可能来自老板、销售、客户、运营、研发、数据、竞品。
- 如果不先 triage，后续所有工作流都会被污染。

建议插件新增：

```text
pm-intake-triage
```

触发场景：

- “帮我看看这个需求该怎么处理。”
- “老板提了个想法。”
- “客户要求做这个功能。”
- “这个需求该不该进产品池？”

背后技能流：

```text
pm-workflow-router
-> evidence-classifier
-> stakeholder-map
-> prioritization-frameworks
-> route-to-scene
```

标准输出：

- 请求来源
- 请求类型
- 事实/观点/假设分类
- 影响用户
- 业务目标
- 推荐进入哪个场景
- 是否阻断

结论：S0 不一定作为新人学习的第十一个场景，但必须作为插件入口能力。

### 2. 横切能力：Gate Review

当前每个场景都写了阻断点，但插件层面应该统一成一个技能：

```text
pm-gate-review
```

它不属于单一场景，而是每个场景进入下一阶段前都会调用。

统一关卡：

| Gate | 检查内容 | 不通过后果 |
| --- | --- | --- |
| Problem Gate | 用户、问题、场景、证据是否清楚 | 不能进入方案 |
| Discovery Gate | 假设、风险、验证计划是否清楚 | 不能进入 PRD |
| PRD Gate | 范围、指标、验收标准是否清楚 | 不能进入 UI/研发 |
| Design Handoff Gate | 用户流、状态、权限、文案是否清楚 | 不能进入研发 |
| Launch Gate | 测试、风险、监控、回滚是否清楚 | 不能上线 |
| Learning Gate | 上线后数据和复盘是否完成 | 不能关闭需求 |

输出统一为：

```text
PASS
PASS_WITH_RISKS
BLOCKED
```

### 3. 横切能力：证据分类

产品新人常犯的问题是混淆事实、观点、假设、承诺。

建议插件新增：

```text
evidence-classifier
```

它在 S0、S1、S2、S3、S4、S8 都很关键。

分类：

| 类型 | 说明 | 例子 |
| --- | --- | --- |
| Fact | 可验证事实 | “上周转化率 28%” |
| User Quote | 用户原话 | “这个步骤我不知道该点哪里” |
| Signal | 需要解释的信号 | “20 个客户问过这个功能” |
| Assumption | 未验证判断 | “用户会愿意付费” |
| Opinion | 主观看法 | “我觉得这个页面不好看” |
| Commitment | 已承诺事项 | “销售已承诺 Q3 提供” |

没有证据分类，插件很容易把二手观点当成真实需求。

### 4. 横切能力：Decision Log

PM 工作不只是产出文档，还要记录取舍。

建议插件新增：

```text
pm-decision-log
```

任何场景中出现以下内容都应写入：

- 为什么做
- 为什么不做
- 为什么先做 A 不做 B
- 谁决定
- 基于什么证据
- 有哪些风险
- 何时复查

这能解决路线图、PRD 和上线后争议。

### 5. 横切能力：Post-launch Learning

建议把上线后学习作为横切或独立场景。

如果公司重视产品闭环，建议新增 workflow：

```text
post-launch-learning
```

如果暂时控制范围，可先放入 S9 的第二阶段。

它要检查：

- 上线目标是否达成
- 指标是否变化
- 用户反馈如何
- 哪些假设被验证/证伪
- 哪些后续动作进入 backlog
- 是否关闭需求

没有这个能力，插件会强化“上线即完成”的错误习惯。

### 6. 横切能力：下游就绪检查

因为未来要串 UI 智能体和研发智能体，PM 插件必须有：

```text
downstream-readiness
```

它回答：

- 是否可以交给 UI？
- 是否可以交给研发？
- 还缺什么？
- 哪些信息会导致 UI 或研发返工？

检查项：

- 核心用户流
- 页面/功能范围
- 权限规则
- 状态和边界
- 文案和错误反馈
- 验收标准
- 指标和埋点

## 第三轮：插件结构是否需要调整

### 当前建议结构

```text
pm-superpowers/
  skills/
    pm-workflow-router/
    new-product-discovery/
    existing-product-optimization/
    feedback-to-roadmap/
    prd-standardization/
    user-research/
    prioritization-roadmap/
    metrics-experiments/
    strategy-business-model/
    launch-readiness/
    pm-operations/
```

### 圆桌修正建议

插件结构应调整为：

```text
pm-superpowers/
  skills/
    pm-workflow-router/
    pm-intake-triage/

    new-product-discovery/
    existing-product-optimization/
    feedback-to-roadmap/
    prd-standardization/
    user-research/
    prioritization-roadmap/
    metrics-experiments/
    strategy-business-model/
    launch-readiness/
    pm-operations/

    pm-gate-review/
    evidence-classifier/
    pm-decision-log/
    downstream-readiness/
    post-launch-learning/

  assets/
    templates/
      product-brief.md
      discovery-pack.md
      prd.md
      gate-review.md
      evidence-table.md
      decision-log.md
      roadmap.md
      metrics-plan.md
      launch-checklist.md
      post-launch-review.md
```

### 为什么这样更好

十个高频场景是用户学习和场景工作流入口。

但插件真正可靠，需要额外五类“流程控制技能”：

1. 入口治理：`pm-intake-triage`
2. 关卡判断：`pm-gate-review`
3. 证据判断：`evidence-classifier`
4. 决策记录：`pm-decision-log`
5. 下游交接：`downstream-readiness`

这些横切技能不一定直接暴露给新人，但必须在场景工作流内部被使用。

## 第四轮：十个高频场景的修正版

圆桌建议保留十个高频场景，但稍微调整命名和边界。

| 编号 | 插件场景 | 对用户的通俗解释 | 背后 workflow skill |
| --- | --- | --- | --- |
| S1 | 新想法/新产品探索 | 判断一个想法是否值得做，而不是直接写需求 | `new-product-discovery` |
| S2 | 已有产品问题优化 | 先诊断真实问题，再决定改什么 | `existing-product-optimization` |
| S3 | 反馈/需求池治理 | 把客户、销售、客服反馈变成证据和路线图 | `feedback-to-roadmap` |
| S4 | PRD 和需求标准化 | 把已明确的问题和方案变成可交付契约 | `prd-standardization` |
| S5 | 用户研究和访谈 | 通过用户事实理解任务、痛点和替代方案 | `user-research` |
| S6 | 优先级和路线图 | 在资源有限时做取舍，形成 outcome roadmap | `prioritization-roadmap` |
| S7 | 指标和实验 | 定义指标、看板、实验和结果判断 | `metrics-experiments` |
| S8 | 战略和商业模式 | 判断方向、市场、价值主张、商业模式和取舍 | `strategy-business-model` |
| S9 | 上线和 GTM 准备 | 确认发布、风险、沟通、监控、回滚和市场准备 | `launch-readiness` |
| S10 | PM 日常运营 | 会议、OKR、Sprint、复盘、决策和行动项沉淀 | `pm-operations` |

注意两点：

1. “产品需求入口治理”作为 S0，不放入十个业务场景，但作为插件必备入口。
2. “上线后复盘”可先作为 S9/S10 的后置阶段，后续成熟后独立成 `post-launch-learning`。

## 第五轮：哪些场景最该先做

### Marty Cagan

【Marty Cagan】【陈述】：优先做能改变团队行为的场景，而不是最容易生成文档的场景。我会先做 S1、S2、S4、S6、S9。它们能阻止错误投入、错误需求、错误路线图和错误上线。

**简言之**：先做能阻止错误建设的场景。

### Teresa Torres

【Teresa Torres】【补充】：我会把 S5 用户研究提前。没有用户研究，新产品发现和已有产品优化都会变成猜测。至少要把 `user-research` 作为 S1/S2 的内置能力。

**简言之**：用户研究可以不是 P0 独立入口，但必须内嵌到发现流。

### Melissa Perri

【Melissa Perri】【质疑】：如果不先做 intake triage，公司仍然会把垃圾输入送进漂亮流程。P0 应该有 `pm-intake-triage` 和 `pm-gate-review`。

**简言之**：先守住入口，再优化流程。

### Kent Beck

【Kent Beck】【补充】：我会先做关卡和验证，而不是先做 10 个 workflow。没有 gate 的 workflow 只是建议。P0 必须包括 `pm-gate-review`。

**简言之**：先做约束，再做丰富场景。

### Don Norman

【Don Norman】【补充】：每个 P0 场景都要检查用户任务流。即使不单独做 UX 场景，也要在 PRD Gate 中加入 core flow、states、errors、feedback。

**简言之**：用户任务流是下游 UI 和研发的基础。

## MVP 插件建议

第一版插件不要做完整 15 个技能。建议 MVP 做 8 个技能。

### P0 技能

| 技能 | 类型 | 为什么 P0 |
| --- | --- | --- |
| `pm-workflow-router` | 路由 | 所有任务入口，决定走什么流程 |
| `pm-intake-triage` | 入口治理 | 防止模糊请求直接进入 PRD |
| `pm-gate-review` | 横切关卡 | 防止没想清楚进入下一步 |
| `evidence-classifier` | 横切判断 | 防止观点、假设、事实混淆 |
| `new-product-discovery` | 场景工作流 | 覆盖新想法高频场景 |
| `feedback-to-roadmap` | 场景工作流 | 覆盖反馈和需求池高频痛点 |
| `prd-standardization` | 场景工作流 | 直接影响 UI/研发交接质量 |
| `launch-readiness` | 场景工作流 | 防止上线风险和交付失控 |

### P1 技能

| 技能 | 类型 |
| --- | --- |
| `existing-product-optimization` | 场景工作流 |
| `prioritization-roadmap` | 场景工作流 |
| `metrics-experiments` | 场景工作流 |
| `user-research` | 场景工作流 |
| `downstream-readiness` | 横切交接 |

### P2 技能

| 技能 | 类型 |
| --- | --- |
| `strategy-business-model` | 场景工作流 |
| `pm-operations` | 场景工作流 |
| `pm-decision-log` | 横切记录 |
| `post-launch-learning` | 闭环学习 |

## 关键设计原则

圆桌最终收敛出 9 条原则。

1. 场景优先，不是技能优先。
2. 路由优先，不是用户说什么就做什么。
3. 证据优先，不把观点当事实。
4. 结果优先，不把产物当成果。
5. 关卡优先，不让模糊输入进入下一步。
6. 学习层和执行层分离：十个场景用于学习，插件技能用于执行。
7. 横切能力必须存在：gate、evidence、decision、handoff、learning。
8. 第一版插件要小而硬，不要大而松。
9. PM 插件最终要为 UI/研发智能体提供稳定上游输入。

## 对现有文档的修正建议

### `PM_PLUGIN_SCENARIO_WORKFLOW_DESIGN.md`

建议补充：

- `pm-intake-triage`
- `pm-gate-review`
- `evidence-classifier`
- `pm-decision-log`
- `downstream-readiness`
- `post-launch-learning`
- MVP 技能优先级

### `PM_10_SCENARIOS_PLAYBOOK.md`

保留为学习材料，但开头应明确：

- 这不是插件最终结构。
- 十个场景是用户认知层。
- 插件执行层还包含 S0 和横切控制技能。

### `PM_SCENARIO_WORKFLOW_SYSTEM.md`

需要把“自动选择工作流”从交互描述改成插件架构描述：

- 路由 skill
- 场景 workflow skill
- 横切 gate skill
- 模板 assets
- references 机制

## 圆桌总结

【主持】【综合】：这次讨论最大的修正是：十个高频场景本身是正确方向，但不能把它们直接等同于插件结构。它们更适合作为用户学习层和场景入口。真正的插件需要额外的流程控制能力，尤其是 intake、gate、evidence、decision 和 downstream readiness。

最终建议是：

```text
用户学习层：十个高频 PM 场景
插件入口层：pm-workflow-router + pm-intake-triage
场景执行层：核心 workflow skills
流程控制层：gate / evidence / decision / readiness / learning
产物层：标准 templates 和 output specs
```

如果第一版就做 10 个完整场景，很容易做成“大而松”的提示词集合。更好的第一版，是做 4 个高频场景 + 4 个流程控制技能，让插件先形成纪律，再扩展覆盖面。

**最终判断**：方向应该从“十个场景说明文档”升级为“场景化 PM superpowers 插件”。十个场景保留，但插件 MVP 应优先做路由、入口治理、关卡和四个最高频场景。
