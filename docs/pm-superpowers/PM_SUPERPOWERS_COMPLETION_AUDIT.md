# PM Superpowers 完成审计

审计日期：2026-06-22

更新日期：2026-06-23

2026-06-23 更新：PM Superpowers 从 `0.3.0` 升级到 `0.4.0`，68 个 PM method skills 已改为随插件内置发布。团队成员只需要安装 PM Superpowers 一个插件；插件开发人员通过同步脚本维护底层方法技能快照。

2026-06-23 二次更新：PM Superpowers 从 `0.4.0` 升级到 `0.4.1`，补充用户下载安装和使用指南，并为 `docs/`、`docs/planning/` 增加目录说明。

2026-06-23 三次更新：PM Superpowers 从 `0.4.1` 升级到 `0.4.2`，修正文档中写死的本机绝对路径，改为仓库相对路径、`<repo-root>` 或 `${CODEX_HOME:-$HOME/.codex}`。

2026-06-23 四次更新：PM Superpowers 从 `0.4.2` 升级到 `0.4.3`，将 PRD 模板从单一固定结构升级为自适应模块结构。

2026-06-23 五次更新：PM Superpowers 从 `0.4.3` 升级到 `0.4.4`，新增版本检查脚本、更新脚本和更新指南。

## 目标拆解

本轮目标来自完整产品工作流插件建设要求，包含：

1. 安装并保留现有 PM skills，使其在本地产品目录可用。
2. 学习并整理现有 PM skills 的作用和应用场景。
3. 面向新产品经理和公司 PM，设计高频场景化最佳工作流。
4. 不只是写提示词，而是做成 Codex 插件化形态。
5. 插件内融合场景工作流、技能流、门禁、规范和模板。
6. 补齐缺失的控制技能，如路由、澄清、证据分类、门禁、下游交接等。
7. 输出面向用户的场景化使用文档。
8. 输出插件设计理念、核心工作流和技能说明书。
9. 明确现有 68 个 PM skills 如何处理。
10. 明确插件如何发版给内部团队使用。
11. 完成校验和本地安装验证。

## 当前产物

### 底层 PM Skills

位置：

```text
<repo-root>/.codex/skills
```

数量：68 个。

处理策略：

- 随 PM Superpowers 插件内置发布。
- 不重写。
- 不合并成一个大技能。
- 作为底层产品方法库快照保留。
- 由 PM Superpowers 进行场景化编排和治理。

### PM Superpowers 插件

位置：

```text
plugins/pm-superpowers
```

Manifest：

```text
plugins/pm-superpowers/.codex-plugin/plugin.json
```

Marketplace：

```text
.agents/plugins/marketplace.json
```

Marketplace 名称：

```text
pm-superpowers-internal
```

插件名称：

```text
pm-superpowers
```

### 插件技能

共 86 个：

18 个 PM Superpowers 场景/治理技能：

- `pm-workflow-router`
- `pm-intake-triage`
- `evidence-classifier`
- `pm-gate-review`
- `pm-decision-log`
- `downstream-readiness`
- `post-launch-learning`
- `pm-project-initializer`
- `new-product-discovery`
- `existing-product-optimization`
- `feedback-to-roadmap`
- `prd-standardization`
- `user-research`
- `prioritization-roadmap`
- `metrics-experiments`
- `strategy-business-model`
- `launch-readiness`
- `pm-operations`

68 个内置 PM method skills 位于同一 `skills/` 目录中，例如 `create-prd`、`market-sizing`、`ab-test-analysis`、`user-stories`、`gtm-strategy`。

### 运行时 References

共 9 份：

- `chinese-output-standard.md`
- `scene-taxonomy.md`
- `supporting-pm-skills.md`
- `gate-system.md`
- `evidence-taxonomy.md`
- `downstream-handoff.md`
- `project-workspace-standard.md`
- `skill-test-scenarios.md`
- `internal-release-model.md`

### 标准模板

共 14 份：

- `product-brief.md`
- `discovery-pack.md`
- `assumption-map.md`
- `experiment-plan.md`
- `prd.md`
- `acceptance-criteria.md`
- `gate-review.md`
- `evidence-table.md`
- `decision-log.md`
- `outcome-roadmap.md`
- `metrics-plan.md`
- `launch-checklist.md`
- `post-launch-review.md`
- `downstream-readiness.md`

### 产品项目工作区模板

共 9 份：

- `AGENTS.md`
- `product-space/README.md`
- `product-space/context/product-context.md`
- `product-space/context/stakeholders.md`
- `product-space/decisions/decision-log.md`
- `product-space/evidence/evidence-table.md`
- `product-space/workflows/workflow-state.md`
- `product-space/risks/risk-register.md`
- `product-space/handoffs/downstream-readiness.md`

### 用户和维护文档

位置：

```text
docs/pm-superpowers
```

文档：

- `PM_SUPERPOWERS_USER_GUIDE.md`：面向 PM 的十个场景化使用手册。
- `PM_SUPERPOWERS_INSTALL_AND_USAGE.md`：面向用户的下载、安装、更新和首次使用指南。
- `PM_SUPERPOWERS_UPDATE_GUIDE.md`：版本检查、插件更新和团队通知指南。
- `PM_SUPERPOWERS_SCENARIO_DEEP_DIVE.md`：十个高频场景的深度讲解、门禁、工作流和落地训练说明。
- `PM_SUPERPOWERS_PLUGIN_DESIGN.md`：插件设计理念、架构、门禁和下游串联说明。
- `PM_SUPERPOWERS_SKILL_MANUAL.md`：18 个场景/治理技能和 68 个内置 PM method skills 的关系说明。
- `PM_SKILLS_BUNDLING_STRATEGY.md`：68 个 PM method skills 的内置策略、同步方式和重复安装处理。
- `PM_PROJECT_WORKSPACE_GUIDE.md`：产品项目工作区、AGENTS.md、决策记录和项目记忆使用说明。
- `PM_SUPERPOWERS_RELEASE_GUIDE.md`：内部团队发版、安装、升级和维护方式。
- `PM_SUPERPOWERS_COMPLETION_AUDIT.md`：本完成审计。

## 十个高频场景覆盖

| 场景 | 插件技能 | 状态 |
| --- | --- | --- |
| 模糊需求澄清 | `pm-intake-triage` | 已覆盖 |
| 新产品或新功能探索 | `new-product-discovery` | 已覆盖 |
| 已有产品优化 | `existing-product-optimization` | 已覆盖 |
| 反馈转路线图 | `feedback-to-roadmap` | 已覆盖 |
| PRD 标准化 | `prd-standardization` | 已覆盖 |
| 用户研究 | `user-research` | 已覆盖 |
| 优先级和路线图 | `prioritization-roadmap` | 已覆盖 |
| 指标、分析和实验 | `metrics-experiments` | 已覆盖 |
| 战略和商业模式 | `strategy-business-model` | 已覆盖 |
| 上线准备和 GTM | `launch-readiness` | 已覆盖 |
| PM 日常运营协作 | `pm-operations` | 已覆盖 |

说明：其中“模糊需求澄清”作为 S0 入口场景，十个高频业务场景作为 S1-S10，其中 PM 日常运营协作覆盖会议、复盘、sprint、OKR 和跨部门行动项。

## 校验命令

插件校验：

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/plugin-creator/scripts/validate_plugin.py" plugins/pm-superpowers
```

技能校验：

```bash
for d in plugins/pm-superpowers/skills/*; do
  python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" "$d"
done
```

安装状态检查：

```bash
codex plugin list
```

## 已验证结果

- 插件校验通过。
- 86 个技能全部通过 `quick_validate`。
- 68 个 PM method skills 已随 PM Superpowers 插件内置；团队用户不再需要单独安装外部 `pm-skills` 插件集。
- `pm-superpowers@pm-superpowers-internal` 处于 installed/enabled。
- 插件版本为 `0.4.4`。

## 内部发版方式

本地试点：

```bash
codex plugin marketplace add <repo-root>
codex plugin add pm-superpowers@pm-superpowers-internal
```

内部 Git 发版：

```bash
codex plugin marketplace add <internal-repo-url> --ref main
codex plugin add pm-superpowers@pm-superpowers-internal
```

团队成员安装或更新后，需要新开 Codex thread，以加载新插件技能。

## 结论

当前版本已经完成可用的 PM Superpowers 插件 MVP：

- 能作为 Codex 插件安装。
- 能通过插件和技能校验。
- 有场景化工作流。
- 有门禁和证据治理。
- 默认面向中国团队输出中文产物。
- 支持初始化产品项目工作区和标准 `AGENTS.md`。
- 有下游 UI/研发交接标准。
- 有用户学习文档和内部发版文档。
- 已明确 68 个 PM method skills 的内置、同步和编排策略。

后续迭代重点应放在团队试点反馈、公司专属模板、真实案例库和与 UI/研发插件的联调上。
