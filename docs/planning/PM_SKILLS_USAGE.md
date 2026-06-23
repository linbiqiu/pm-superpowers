# PM Skills 使用说明

本文档说明当前项目已安装的产品经理技能包如何使用、每类技能适合什么场景，以及常见工作流该怎么提问。

安装位置：

- 项目内技能副本：`.codex/skills/`
- Codex 插件来源：`pm-skills`
- 已安装插件数量：9 个
- 已安装技能数量：68 个
- 已安装工作流命令文件：42 个

## 使用方式

### 推荐用法

在 Codex 里直接用自然语言描述任务，并明确点名技能或工作流名称。技能会根据上下文自动匹配；如果你想强制使用某个技能，可以直接写技能名。

示例：

```text
用 create-prd 帮我基于下面的功能想法写一份 PRD：...
```

```text
用 opportunity-solution-tree 帮我把“提升新用户激活率”拆成机会、方案和实验。
```

```text
帮我跑一个完整的产品发现流程：先 brainstorm-ideas-new，再 identify-assumptions-new，再 prioritize-assumptions，最后 brainstorm-experiments-new。
```

### 关于 slash 命令

仓库里包含 `/discover`、`/write-prd`、`/strategy` 这类 Claude 风格命令文件。Codex 已安装这些文件，但在 Codex 里最稳妥的调用方式是自然语言描述工作流，而不是依赖 slash 命令一定能被运行。

例如，把：

```text
/discover AI 会议纪要产品
```

改成：

```text
请按 discover 工作流帮我做 AI 会议纪要产品的产品发现：先发散方案，再识别假设，再排序风险最高的假设，最后设计验证实验。
```

### 输入越具体，输出越好

使用这些技能时，最好提供：

- 产品或业务背景
- 目标用户或客户细分
- 当前阶段：想法、MVP、增长期、成熟期
- 当前目标：验证需求、写 PRD、做战略、规划发布、分析数据
- 可用材料：用户反馈、访谈记录、PRD、路线图、埋点数据、竞品信息、会议纪要
- 输出格式：表格、PRD、路线图、实验计划、汇报稿、SQL、测试用例等

## 选择指南

| 你现在要做什么 | 优先使用 |
| --- | --- |
| 从 0 到 1 探索产品想法 | `brainstorm-ideas-new`、`identify-assumptions-new`、`prioritize-assumptions`、`brainstorm-experiments-new` |
| 优化已有产品或功能 | `brainstorm-ideas-existing`、`identify-assumptions-existing`、`prioritize-features`、`opportunity-solution-tree` |
| 准备用户访谈 | `interview-script` |
| 总结访谈或反馈 | `summarize-interview`、`sentiment-analysis`、`user-segmentation` |
| 写战略或商业模式 | `product-strategy`、`startup-canvas`、`lean-canvas`、`business-model` |
| 做市场或竞品研究 | `market-sizing`、`competitor-analysis`、`market-segments`、`porters-five-forces` |
| 写 PRD 或拆需求 | `create-prd`、`user-stories`、`job-stories`、`wwas` |
| 做优先级排序 | `prioritize-features`、`prioritization-frameworks`、`prioritize-assumptions` |
| 做发版前风险检查 | `pre-mortem`、`strategy-red-team`、`test-scenarios` |
| 定义指标体系 | `north-star-metric`、`metrics-dashboard`、`cohort-analysis` |
| 做上线和增长 | `gtm-strategy`、`ideal-customer-profile`、`beachhead-segment`、`growth-loops` |
| 做产品营销 | `positioning-ideas`、`value-prop-statements`、`marketing-ideas`、`product-name` |
| 分析实验或写 SQL | `ab-test-analysis`、`sql-queries`、`cohort-analysis` |
| 审核 AI 生成代码是否可发布 | `shipping-artifacts`、`intended-vs-implemented` |

## 插件说明

### pm-product-discovery：产品发现

用于从问题空间进入方案空间，适合早期探索、持续发现、假设验证、访谈准备、功能请求整理和指标设计。

典型场景：

- 你有一个新产品想法，但不确定用户是否需要
- 你有一堆功能请求，需要聚类和排序
- 你要设计用户访谈提纲
- 你要把业务目标拆成机会、解决方案和实验
- 你要设计某个产品或功能的指标看板

常用提示词：

```text
用 discover 工作流帮我探索这个产品想法：面向小团队的 AI 项目复盘助手。请先判断这是新产品还是已有产品场景，再逐步输出想法、假设、优先级和实验。
```

```text
用 triage-requests 的方式分析下面这些客户功能请求，按主题聚类，并基于影响、成本、风险和战略匹配度给出优先级。
```

| 技能 | 作用 | 适用场景 |
| --- | --- | --- |
| `brainstorm-ideas-new` | 为新产品做多视角功能和方案发散 | 新产品立项、创业想法、早期探索 |
| `brainstorm-ideas-existing` | 为已有产品做多视角方案发散 | 现有产品优化、发现机会后的方案探索 |
| `brainstorm-experiments-new` | 为新产品设计低成本验证实验 | 验证市场需求、pretotype、落地页、预购测试 |
| `brainstorm-experiments-existing` | 为已有产品假设设计验证实验 | A/B 测试、原型测试、技术 spike、低成本验证 |
| `identify-assumptions-new` | 识别新产品的高风险假设 | 创业概念、0 到 1 产品、风险地图 |
| `identify-assumptions-existing` | 识别已有产品或功能的风险假设 | 功能上线前、需求评审、可行性分析 |
| `prioritize-assumptions` | 用影响和风险矩阵排序假设 | 决定先验证什么、安排实验顺序 |
| `prioritize-features` | 基于影响、成本、风险和战略匹配排序功能 | backlog 评审、季度规划、范围裁剪 |
| `analyze-feature-requests` | 聚类并分析客户功能请求 | 客服工单、销售反馈、用户调研汇总 |
| `opportunity-solution-tree` | 构建机会解决方案树 | 从目标拆机会、方案和实验 |
| `interview-script` | 生成用户访谈提纲 | 访谈准备、JTBD 探索、需求发现 |
| `summarize-interview` | 总结访谈记录 | 访谈复盘、洞察提炼、行动项整理 |
| `metrics-dashboard` | 设计产品指标看板 | 定义 KPI、北极星指标、健康指标、告警阈值 |

### pm-product-strategy：产品战略

用于定义产品方向、目标用户、商业模式、定价、外部环境和增长路径，适合年度规划、融资材料、战略评审、产品线重构。

典型场景：

- 你要写一份完整产品战略
- 你要比较不同商业模式
- 你要做定价策略
- 你要分析市场环境和竞争压力
- 你要定义清晰的价值主张

常用提示词：

```text
用 product-strategy 帮我为“企业知识库 AI 助手”写一份 9 部分产品战略画布，包含目标用户、价值主张、取舍、指标、增长和护城河。
```

```text
用 pricing-strategy 和 monetization-strategy 分析这个 SaaS 产品是否应该从按席位收费改成按使用量收费。
```

| 技能 | 作用 | 适用场景 |
| --- | --- | --- |
| `product-strategy` | 创建 9 部分产品战略画布 | 产品方向、战略文档、年度规划 |
| `product-vision` | 生成产品愿景 | 团队对齐、愿景陈述、战略开头 |
| `value-proposition` | 用 JTBD 模板设计价值主张 | 明确用户、场景、结果和替代方案 |
| `startup-canvas` | 结合战略和商业模式的新产品画布 | 创业项目、新产品线、MVP 前评估 |
| `lean-canvas` | 生成 Lean Canvas | 早期商业假设、问题和解决方案建模 |
| `business-model` | 生成商业模式画布 | 价值创造、交付和变现路径分析 |
| `monetization-strategy` | 发散 3 到 5 个变现策略 | 收入模式探索、定价前分析 |
| `pricing-strategy` | 分析和设计定价策略 | 新定价、调价、包装、竞品价格对比 |
| `swot-analysis` | SWOT 分析 | 战略评估、竞品态势、内部外部因素 |
| `pestle-analysis` | PESTLE 宏观环境分析 | 政策、经济、社会、技术、法律、环境因素 |
| `porters-five-forces` | 波特五力分析 | 行业吸引力、竞争压力、进入壁垒 |
| `ansoff-matrix` | Ansoff 增长矩阵 | 市场渗透、市场开发、产品开发、多元化 |

### pm-execution：产品执行

用于把战略和发现结果落成文档、计划、需求、测试、发布和复盘，适合产品经理日常执行。

典型场景：

- 你要写 PRD
- 你要拆用户故事或验收标准
- 你要做 Sprint 计划或复盘
- 你要写 OKR、路线图、发布说明
- 你要做发版前风险分析

常用提示词：

```text
用 create-prd 根据下面的问题陈述写一份 8 部分 PRD，最后补充成功指标、范围外事项和发布计划。
```

```text
用 strategy-red-team 压测这份 PRD，找出最关键的假设、失败模式、最低成本验证方式和停止标准。
```

| 技能 | 作用 | 适用场景 |
| --- | --- | --- |
| `create-prd` | 创建 8 部分 PRD | 需求文档、功能规格、评审材料 |
| `brainstorm-okrs` | 生成团队级 OKR | 季度规划、目标对齐、战略落地 |
| `outcome-roadmap` | 把功能路线图改成结果导向路线图 | 路线图升级、向高层表达战略意图 |
| `sprint-plan` | 规划 Sprint | 容量估算、故事选择、依赖和风险识别 |
| `retro` | 组织 Sprint 复盘 | 复盘会议、行动项、持续改进 |
| `release-notes` | 生成用户可读发布说明 | changelog、产品更新公告 |
| `pre-mortem` | 做上线前风险预演 | 发布前检查、项目风险识别 |
| `stakeholder-map` | 建立利益相关方地图和沟通计划 | 跨团队协作、上线沟通、组织对齐 |
| `summarize-meeting` | 总结会议纪要 | 决策、行动项、责任人、后续事项 |
| `user-stories` | 写用户故事和验收标准 | backlog 拆分、敏捷开发、验收条件 |
| `job-stories` | 写 JTBD 风格 job stories | 表达场景、动机和期望结果 |
| `wwas` | 写 Why-What-Acceptance 格式 backlog | 强调业务上下文和验收标准 |
| `test-scenarios` | 生成测试场景 | QA 测试、验收测试、边界和异常路径 |
| `dummy-dataset` | 生成测试假数据 | demo、开发测试、样例数据 |
| `prioritization-frameworks` | 提供 9 种优先级框架参考 | RICE、ICE、Kano、MoSCoW 等选择 |
| `strategy-red-team` | 对 PRD、路线图或战略做反方压力测试 | 高风险决策、上会前评审、关键假设验证 |

### pm-market-research：市场研究

用于从用户、市场、竞品和反馈中提炼洞察，适合做调研、定位、竞品分析和市场进入判断。

常用提示词：

```text
用 market-sizing 估算中国中小企业 AI 客服工具的 TAM、SAM、SOM。请同时给出 top-down 和 bottom-up 两种算法。
```

```text
用 competitor-analysis 分析下面三个竞品，输出差异化机会和我们应该避开的竞争点。
```

| 技能 | 作用 | 适用场景 |
| --- | --- | --- |
| `competitor-analysis` | 分析竞品优劣势和差异化机会 | 竞品 brief、定位、战略评估 |
| `customer-journey-map` | 绘制端到端客户旅程 | 找摩擦点、优化 onboarding、体验地图 |
| `market-segments` | 识别 3 到 5 个潜在客户细分 | 目标市场选择、用户分群 |
| `market-sizing` | 估算 TAM、SAM、SOM | 投资人材料、市场进入、机会评估 |
| `sentiment-analysis` | 分析用户反馈情绪和主题 | 评论、问卷、客服记录、满意度洞察 |
| `user-personas` | 从研究资料生成用户画像 | Persona、用户理解、产品决策 |
| `user-segmentation` | 基于行为、JTBD 和需求做用户分群 | 分群模型、差异化策略 |

### pm-data-analytics：数据分析

用于产品数据问题、SQL 生成、留存分析和实验结果判断。

常用提示词：

```text
用 sql-queries 写一条 PostgreSQL 查询：统计过去 30 天每天完成 onboarding 的新用户数，并按渠道分组。
```

```text
用 ab-test-analysis 分析这个实验：Control 转化率 4.2%，样本 5000；Variant 转化率 4.8%，样本 5100。告诉我是否应该发布。
```

| 技能 | 作用 | 适用场景 |
| --- | --- | --- |
| `sql-queries` | 将自然语言转成 SQL | 报表、数据探索、业务问题查询 |
| `cohort-analysis` | 做 cohort 留存和采用分析 | 留存曲线、功能采用、流失分析 |
| `ab-test-analysis` | 分析 A/B 测试结果 | 显著性、样本量、置信区间、发布决策 |

### pm-marketing-growth：产品营销和增长

用于产品定位、命名、价值主张文案、北极星指标和低成本营销创意。

常用提示词：

```text
用 north-star-metric 帮我为 B2B 项目协作 SaaS 设计北极星指标和 3 到 5 个输入指标。
```

```text
用 positioning-ideas 为我们的 AI 写作工具生成 5 个差异化定位方向，并指出各自适合的目标客群。
```

| 技能 | 作用 | 适用场景 |
| --- | --- | --- |
| `marketing-ideas` | 生成低成本营销创意 | 活动策划、增长实验、产品推广 |
| `north-star-metric` | 定义北极星指标和输入指标 | 指标体系、团队对齐、增长管理 |
| `positioning-ideas` | 生成差异化定位 | 市场定位、竞品区隔、品牌策略 |
| `product-name` | 生成产品名称 | 新产品命名、品牌重命名 |
| `value-prop-statements` | 把价值主张转成营销、销售和 onboarding 文案 | 官网文案、销售话术、引导文案 |

### pm-go-to-market：上市和增长战略

用于发布计划、ICP、beachhead 市场、GTM motion、增长飞轮和销售 battlecard。

常用提示词：

```text
用 gtm-strategy 帮我为“AI 客服质检工具”设计上市计划，包含 beachhead segment、ICP、渠道、信息、指标和时间线。
```

```text
用 competitive-battlecard 为我们和 Intercom 的竞争准备销售 battlecard。
```

| 技能 | 作用 | 适用场景 |
| --- | --- | --- |
| `beachhead-segment` | 选择第一个切入市场 | 市场进入、首批客户选择 |
| `ideal-customer-profile` | 定义 ICP | 销售和营销对齐、PMF 分析 |
| `gtm-strategy` | 创建上市策略 | 新产品发布、新市场进入 |
| `gtm-motions` | 选择 GTM motion 和渠道 | inbound、outbound、PLG、ABM、伙伴等 |
| `growth-loops` | 识别增长飞轮 | 可持续增长、产品驱动传播 |
| `competitive-battlecard` | 生成竞品销售 battlecard | 销售赋能、竞品异议处理 |

### pm-ai-shipping：AI 代码发版检查

用于让 AI 生成或快速搭建的应用在上线前变得可审查、可测试、可交付。它更偏 PM 负责发版质量、风险和交接的场景。

常用提示词：

```text
用 shipping-artifacts 帮我为当前代码库整理上线前需要的文档：架构、用户流程、权限、环境变量、测试覆盖。
```

```text
用 intended-vs-implemented 检查当前代码是否符合 permissions.md 和 flows.md 中记录的权限意图。
```

| 技能 | 作用 | 适用场景 |
| --- | --- | --- |
| `shipping-artifacts` | 定义 AI 应用发版前所需文档集 | 代码交接、安全审查、测试规划、上线准备 |
| `intended-vs-implemented` | 比较“文档意图”和“代码实现”的差距 | 权限审计、代码 review、安全风险识别 |

### pm-toolkit：PM 工具箱

用于 PM 日常通用文档和个人职业材料。

常用提示词：

```text
用 grammar-check 检查下面这段产品公告的语法、逻辑和表达流畅度，只给出具体修改建议，不要整篇重写。
```

```text
用 privacy-policy 为一个面向美国和欧盟用户的 SaaS 分析产品起草隐私政策草案，并标出需要法律审查的条款。
```

| 技能 | 作用 | 适用场景 |
| --- | --- | --- |
| `grammar-check` | 检查语法、逻辑和行文流畅度 | 邮件、公告、文档、PRD 文案 |
| `review-resume` | PM 简历评审 | 求职、简历优化、关键词和成果表达 |
| `draft-nda` | 起草 NDA | 合作、外包、客户交流前保密协议 |
| `privacy-policy` | 起草隐私政策 | 产品上线、合规准备、数据处理说明 |

## 常用工作流

下面的工作流来自已安装的 command 文件。Codex 中建议用自然语言调用这些工作流。

| 工作流 | 插件 | 输入 | 输出 |
| --- | --- | --- | --- |
| `discover` | pm-product-discovery | 产品或功能想法 | 想法发散、假设地图、优先级、实验计划 |
| `brainstorm` | pm-product-discovery | `ideas` 或 `experiments`，`existing` 或 `new`，加产品描述 | 多视角想法或实验方案 |
| `triage-requests` | pm-product-discovery | 功能请求文本、CSV 或表格 | 主题聚类、优先级、建议行动 |
| `interview` | pm-product-discovery | `prep` 加研究主题，或 `summarize` 加访谈记录 | 访谈脚本或访谈洞察总结 |
| `setup-metrics` | pm-product-discovery | 产品或功能范围 | 北极星指标、输入指标、健康指标、告警阈值 |
| `strategy` | pm-product-strategy | 产品或公司描述 | 完整产品战略画布 |
| `business-model` | pm-product-strategy | `lean`、`full`、`startup`、`value-prop` 或 `all` | 商业模式或价值主张分析 |
| `market-scan` | pm-product-strategy | 产品、市场或行业 | SWOT、PESTLE、五力、Ansoff 综合分析 |
| `pricing` | pm-product-strategy | 产品或定价问题 | 定价模型、竞品分析、支付意愿、实验建议 |
| `value-proposition` | pm-product-strategy | 产品或功能 | 6 部分 JTBD 价值主张 |
| `write-prd` | pm-execution | 功能或问题陈述 | 完整 PRD |
| `plan-okrs` | pm-execution | 团队、产品域或公司目标 | 团队级 OKR |
| `transform-roadmap` | pm-execution | 功能列表或路线图 | 结果导向路线图 |
| `sprint` | pm-execution | `plan`、`retro` 或 `release-notes` 加上下文 | Sprint 计划、复盘或发布说明 |
| `pre-mortem` | pm-execution | PRD、发布计划或功能描述 | 风险清单、分类和缓解方案 |
| `red-team-prd` | pm-execution | PRD、路线图或战略 | 关键假设、失败模式、最低成本验证、停止标准 |
| `meeting-notes` | pm-execution | 会议记录或转写 | 决策、摘要、行动项 |
| `stakeholder-map` | pm-execution | 项目、计划或发布 | 权力兴趣矩阵和沟通计划 |
| `write-stories` | pm-execution | `user`、`job` 或 `wwa` 加功能描述 | backlog 条目和验收标准 |
| `test-scenarios` | pm-execution | 用户故事、功能规格或描述 | 测试场景、边界条件、异常路径 |
| `generate-data` | pm-execution | 数据集需求 | CSV、JSON、SQL 或 Python 假数据 |
| `research-users` | pm-market-research | 研究数据、问卷或产品描述 | 用户画像、分群、客户旅程 |
| `analyze-feedback` | pm-market-research | 用户反馈文本或表格 | 情绪、主题、分群洞察 |
| `competitive-analysis` | pm-market-research | 产品或市场 | 竞品地图、优劣势、差异化机会 |
| `write-query` | pm-data-analytics | 自然语言数据问题 | SQL 查询 |
| `analyze-cohorts` | pm-data-analytics | 数据文件或分析描述 | cohort 留存、采用趋势、洞察 |
| `analyze-test` | pm-data-analytics | A/B 测试结果 | 显著性判断和 ship/extend/stop 建议 |
| `market-product` | pm-marketing-growth | 产品或营销挑战 | 营销创意、定位、价值主张文案、命名 |
| `north-star` | pm-marketing-growth | 产品或业务 | 北极星指标和输入指标 |
| `plan-launch` | pm-go-to-market | 产品或功能发布 | GTM 策略、ICP、渠道、信息、时间线 |
| `growth-strategy` | pm-go-to-market | 产品或增长问题 | 增长飞轮和 GTM motion |
| `battlecard` | pm-go-to-market | 我方产品和竞品 | 销售 battlecard |
| `ship-check` | pm-ai-shipping | 代码库路径或范围 | 发版包：文档、安全、性能、测试覆盖 |
| `document-app` | pm-ai-shipping | 代码库路径或模块 | 架构、流程、权限、变量等系统文档 |
| `derive-tests` | pm-ai-shipping | 代码库路径或模块 | 测试覆盖地图和建议测试 |
| `security-audit-static` | pm-ai-shipping | 代码库路径或模块 | 静态安全审查发现 |
| `performance-audit-static` | pm-ai-shipping | 代码库路径或模块 | 性能风险和优化建议 |
| `proofread` | pm-toolkit | 需要检查的文本 | 语法、逻辑、流畅度修改建议 |
| `review-resume` | pm-toolkit | 简历文本或文件 | PM 简历评审 |
| `tailor-resume` | pm-toolkit | 简历加 JD | 针对岗位的简历优化建议 |
| `draft-nda` | pm-toolkit | 双方和合作背景 | NDA 草案 |
| `privacy-policy` | pm-toolkit | 产品和数据处理背景 | 隐私政策草案 |

## 组合使用示例

### 从想法到 PRD

```text
我有一个新产品想法：面向自由职业者的 AI 报价助手。请按以下步骤推进：
1. 用 brainstorm-ideas-new 发散可行功能。
2. 用 identify-assumptions-new 识别关键风险假设。
3. 用 prioritize-assumptions 排序最该验证的假设。
4. 用 brainstorm-experiments-new 设计低成本验证实验。
5. 基于最有把握的方向，用 create-prd 写第一版 PRD。
```

### 从客户反馈到路线图

```text
下面是 50 条客户反馈。请先用 analyze-feature-requests 聚类，再用 prioritize-features 排优先级，最后用 outcome-roadmap 改写成结果导向路线图。
```

### 从战略到上市

```text
请为这个产品做完整规划：
1. 用 product-strategy 写产品战略画布。
2. 用 value-proposition 明确核心价值主张。
3. 用 ideal-customer-profile 定义 ICP。
4. 用 beachhead-segment 选择首个切入市场。
5. 用 gtm-strategy 输出上市计划。
```

### 从发布前检查到测试计划

```text
请检查当前仓库是否适合发布：
1. 用 shipping-artifacts 生成或检查必要文档。
2. 用 intended-vs-implemented 对比文档意图和代码实现。
3. 用 test-scenarios 为关键用户故事生成测试场景。
4. 用 pre-mortem 输出发布风险和缓解计划。
```

### 从指标到数据查询

```text
请为我们的 onboarding 流程设计指标体系：
1. 用 north-star-metric 判断是否有合适的北极星指标。
2. 用 metrics-dashboard 设计看板。
3. 用 sql-queries 生成 PostgreSQL 查询来计算关键指标。
4. 如果有历史数据，再用 cohort-analysis 分析不同注册 cohort 的激活和留存。
```

## 最佳实践

- 先说明业务阶段：新产品、已有产品、增长期、成熟期。
- 先说明目标：探索、决策、对齐、执行、发版、复盘。
- 对复杂任务要求分阶段输出，阶段之间让 Codex 停下来等待确认。
- 对战略类任务提供约束：目标市场、竞品、商业模式、当前资源。
- 对数据类任务提供 schema、口径、时间范围和数据库类型。
- 对 PRD 和执行类任务明确输出模板和读者：工程、设计、销售、高层或客户。
- 对法律类草案只当作初稿，最终交给专业律师审查。

## 本地维护

项目内技能文件位于：

```text
<repo-root>/.codex/skills
```

查看已安装插件：

```bash
codex plugin list
```

查看 PM marketplace：

```bash
codex plugin marketplace list
```

更新 PM marketplace：

```bash
codex plugin marketplace upgrade pm-skills
```

更新后如果需要同步项目内 `.codex/skills` 副本，可以重新从 `phuryn/pm-skills` 安装技能目录。
