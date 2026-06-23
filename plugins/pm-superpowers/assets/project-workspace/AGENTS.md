# AGENTS.md

本文件是当前产品项目的智能体协作规则。所有后续 agent 在处理本项目时，应先阅读本文件和 `product-space/` 下的项目资料。

## 默认语言

- 面向用户的输出默认使用中文。
- 保留必要英文专有名词、文件名、字段名和技能名。
- 重要结论要写清楚依据、假设、风险和下一步。

## 项目工作方式

- 先判断产品场景，再产出文档。
- 信息不足时使用 `BLOCKED`，不要强行补全。
- 把事实、用户原话、信号、假设、意见和承诺分开记录。
- 重要产品决策必须写入 `product-space/decisions/decision-log.md`。
- 当前工作流状态必须写入 `product-space/workflows/workflow-state.md`。
- 准备交给 UI 或研发前，必须更新 `product-space/handoffs/downstream-readiness.md`。

## PM Superpowers 标准场景

- S0 模糊需求澄清
- S1 新产品或新功能探索
- S2 已有产品优化
- S3 反馈转路线图
- S4 PRD 标准化
- S5 用户研究
- S6 优先级和路线图
- S7 指标和实验
- S8 战略和商业模式
- S9 上线准备和 GTM
- S10 PM 日常运营协作

## 项目记忆文件

- `product-space/context/product-context.md`：产品背景和上下文
- `product-space/context/stakeholders.md`：相关方
- `product-space/decisions/decision-log.md`：决策记录
- `product-space/evidence/evidence-table.md`：证据表
- `product-space/workflows/workflow-state.md`：工作流状态
- `product-space/risks/risk-register.md`：风险清单
- `product-space/handoffs/downstream-readiness.md`：下游交接检查

## 交付质量要求

- PRD 必须包含用户、问题、范围、非目标、验收标准、指标和风险。
- 路线图必须包含目标、候选项、评分口径、取舍理由和决策记录。
- 上线计划必须包含发布范围、测试覆盖、监控、回滚和相关方同步。
- 会议纪要必须包含决策、行动项、负责人、截止时间和待确认问题。
