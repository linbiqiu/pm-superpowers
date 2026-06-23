# PM Superpowers 产品项目工作区指南

这份文档回答一个关键问题：用户使用 PM Superpowers 时，插件会不会按项目方式管理产品工作，记录关键决策和关键事项？

## 结论

插件不会在用户毫无请求时自动写入项目文件。标准方式是：

- 用户明确说“初始化产品项目工作区”“创建 AGENTS.md”“按项目管理这个需求”“记录关键决策”时，触发 `pm-project-initializer`。
- 插件会在当前项目中创建或更新标准文件。
- 后续产品工作可以读取这些文件，把上下文、决策、证据、风险和交接状态持续沉淀下来。

这种方式比完全自动写文件更稳，因为它不会在用户不知情的情况下修改项目。

## 初始化后会生成什么

标准结构：

```text
AGENTS.md
product-space/
  README.md
  context/
    product-context.md
    stakeholders.md
  decisions/
    decision-log.md
  evidence/
    evidence-table.md
  workflows/
    workflow-state.md
  risks/
    risk-register.md
  handoffs/
    downstream-readiness.md
```

## 每个文件解决什么问题

| 文件 | 作用 |
| --- | --- |
| `AGENTS.md` | 告诉后续 agent 如何处理这个产品项目 |
| `product-context.md` | 记录产品背景、用户、目标、范围和当前状态 |
| `stakeholders.md` | 记录相关方、职责和沟通节奏 |
| `decision-log.md` | 记录关键产品决策、依据、负责人和后续动作 |
| `evidence-table.md` | 记录事实、用户原话、信号、假设、意见和承诺 |
| `workflow-state.md` | 记录当前处在哪个 PM 场景、门禁状态和下一步 |
| `risk-register.md` | 记录产品、技术、数据、上线和协作风险 |
| `downstream-readiness.md` | 检查是否可以交给 UI、研发、测试或运营 |

## 用户应该怎么说

初始化一个新产品项目：

```text
请用 PM Superpowers 初始化当前项目的产品工作区，创建 AGENTS.md、产品上下文、决策记录、证据表、风险清单和下游交接检查。
```

把当前需求纳入项目管理：

```text
请把这个需求按产品项目方式管理，更新工作流状态、决策记录和待确认问题。
```

记录关键决策：

```text
请把刚才这个产品决策写入 decision-log，并记录依据、负责人和后续动作。
```

检查是否可以交给 UI 或研发：

```text
请读取当前 product-space，检查这份需求是否可以交给 UI 和研发，并更新 downstream-readiness。
```

## 插件如何维护项目记忆

建议规则：

- 每次进入新场景，更新 `product-space/workflows/workflow-state.md`。
- 每次做出关键决策，更新 `product-space/decisions/decision-log.md`。
- 每次新增用户反馈、数据结论或重要假设，更新 `product-space/evidence/evidence-table.md`。
- 每次识别风险，更新 `product-space/risks/risk-register.md`。
- 每次准备交接，更新 `product-space/handoffs/downstream-readiness.md`。

## 和普通聊天有什么区别

普通聊天的问题是上下文容易散。项目工作区的价值是：

- 后续 agent 可以读到之前的关键决策。
- 新同事可以快速理解项目状态。
- PRD、路线图、上线检查不会脱离上下文。
- UI 和研发交接时有固定检查标准。
- 产品负责人可以追踪决策依据。

## 注意事项

- 如果项目已有 `AGENTS.md`，插件应追加 PM Superpowers 段落，不应覆盖。
- 如果已有决策记录，插件应追加新决策，不应删除旧记录。
- 不确定的信息写“待确认”，不要编造。
- 项目工作区不是替代 PRD，而是产品项目的长期上下文。
