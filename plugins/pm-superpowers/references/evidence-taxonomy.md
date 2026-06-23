# 证据分类规范

当产品工作混合了数据、用户反馈、假设、观点和承诺时，使用这份规范。默认面向用户输出中文，英文类型名可保留但必须解释中文含义。

## Evidence Types

| Type | Definition | Example | How to use |
| --- | --- | --- | --- |
| Fact | Verified objective information. | "Conversion is 12.4% for the last 30 days." | Can support decisions directly if source is reliable. |
| User Quote | Direct statement from a user or customer. | "I cannot find where to export." | Use as qualitative evidence, not population truth. |
| Signal | Pattern across multiple facts or quotes. | "Export complaints appear in 18 tickets this month." | Use to prioritize investigation. |
| Assumption | Unverified belief that affects the plan. | "Power users will pay for bulk export." | Validate or carry as risk. |
| Opinion | Preference or judgment without evidence. | "This page feels confusing." | Use as hypothesis, not proof. |
| Commitment | Stated promise, dependency, deadline, or owner. | "Sales needs this by July 15." | Track in decision log and plan. |

## Confidence Levels

| Level | Criteria |
| --- | --- |
| High | Recent, directly relevant, source is known, and corroborated by data or multiple users. |
| Medium | Relevant but partial, dated, small sample, or single source. |
| Low | Anecdotal, inferred, unsourced, or based on stakeholder opinion. |

## 证据表模板

```markdown
| 主张 | 类型 | 来源 | 信心 | 产品含义 | 是否需要验证 |
| --- | --- | --- | --- | --- | --- |
```

## Working Rules

- Label every important claim.
- Do not convert user quotes into broad user needs unless a pattern is shown.
- Treat stakeholder preference as Opinion unless backed by data, customer evidence, or a tracked Commitment.
- Do not hide assumptions inside polished PRD language.
- If evidence is weak but action is still reasonable, mark the output `PASS_WITH_RISKS`.
- If the plan depends on an unverified high-risk assumption, ask for validation before execution.
