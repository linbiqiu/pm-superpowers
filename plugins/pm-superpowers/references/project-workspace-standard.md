# 产品项目工作区标准

PM Superpowers 可以帮助用户把一次性产品讨论沉淀为可持续管理的产品项目工作区。这个能力由 `pm-project-initializer` 触发。

## 是否会自动初始化

不会在用户毫无请求时自动写入项目文件。标准行为是：

- 当用户明确说“初始化产品项目”“建立产品空间”“创建 AGENTS.md”“记录决策”“按项目管理这个需求”时，触发项目初始化。
- 如果当前项目已经有 `AGENTS.md`，只追加或更新 PM Superpowers 相关段落，不覆盖原内容。
- 如果当前项目已有决策记录，合并新决策，不删除历史记录。
- 后续 PM 工作如果发现项目工作区存在，应优先读取其中的上下文、决策、证据和工作流状态。

## 标准目录

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

## 文件职责

| 文件 | 职责 |
| --- | --- |
| `AGENTS.md` | 项目级智能体协作规则，告诉后续 agent 如何处理产品工作 |
| `product-context.md` | 产品背景、用户、目标、范围和当前阶段 |
| `stakeholders.md` | 相关方、角色、职责和沟通节奏 |
| `decision-log.md` | 产品决策、依据、负责人、后续动作 |
| `evidence-table.md` | 事实、用户原话、信号、假设、意见和承诺 |
| `workflow-state.md` | 当前处在哪个 PM 场景、门禁状态和下一步 |
| `risk-register.md` | 产品、交付、数据、上线和组织风险 |
| `downstream-readiness.md` | 是否可以交给 UI、研发、测试、运营等下游 |

## 后续使用规则

- 每次进入新 PM 场景时，更新 `workflow-state.md`。
- 每次做出产品决策时，更新 `decision-log.md`。
- 每次新增用户反馈、数据结论或重要假设时，更新 `evidence-table.md`。
- 每次准备交给 UI 或研发时，更新 `handoffs/downstream-readiness.md`。
- 每次发现风险时，更新 `risk-register.md`。

## 初始化输出

初始化完成后，向用户说明：

- 创建或更新了哪些文件。
- 当前缺少哪些产品上下文。
- 推荐下一步 PM Superpowers 工作流。
- 哪些文件未来会作为项目记忆使用。
