# PM Superpowers 内部发版指南

这份文档回答两个问题：

1. 现有 68 个 PM skills 怎么处理？
2. PM Superpowers 插件开发好后，如何发给内部团队使用？

## 现有 68 个 PM skills 怎么处理

结论：随 PM Superpowers 插件内置发布，作为底层方法库快照；逻辑上仍然保持“方法库”和“工作流插件”分层，不重写、不合并成一个大技能。

原因：

- 68 个 skills 已经覆盖很多产品方法，如 PRD、用户研究、市场分析、实验、GTM、路线图等。
- 它们适合做单点方法，但不负责判断场景和流程顺序。
- 如果让终端用户额外安装一组 `pm-skills` 插件，会增加试点和推广成本，也更容易出现“装了 PM Superpowers 但底层方法缺失”的问题。
- 内置快照可以让用户只安装一个插件，同时由插件开发人员集中同步和发版。
- PM Superpowers 要解决的是“怎么选、怎么串、怎么检查、怎么交接”。

推荐分工：

| 层级 | 负责内容 | 示例 |
| --- | --- | --- |
| PM method skills 方法库 | 原子产品方法，随插件内置 | `create-prd`、`market-sizing`、`ab-test-analysis` |
| PM Superpowers 场景层 | 场景工作流和门禁 | `new-product-discovery`、`prd-standardization`、`downstream-readiness` |
| 团队文档 | 学习材料和公司规范 | 场景手册、发版指南、模板说明 |

## 团队安装前置

团队成员只需要安装 PM Superpowers 插件。

不再要求团队成员单独安装 `pm-skills` 插件集。68 个底层 PM 方法技能已经位于：

```text
plugins/pm-superpowers/skills/
```

如果某位开发者本机同时安装了外部 `pm-skills` 插件集，可能在技能列表里看到重复的同名方法技能。团队正式推广时建议只启用 PM Superpowers，避免同名技能重复展示。

## 当前项目内插件位置

当前插件结构：

```text
plugins/pm-superpowers/
  .codex-plugin/plugin.json
  skills/                 # 18 个场景/治理技能 + 68 个内置 PM 方法技能
  references/
  assets/templates/
  scripts/sync_pm_skills.py

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

## 内部发版方式

推荐把当前仓库作为内部 Git 仓库或团队共享仓库。团队成员通过内部 marketplace 安装。

### 本地路径安装

适合试点或同一台机器验证：

```bash
codex plugin marketplace add "$(pwd)"
codex plugin add pm-superpowers@pm-superpowers-internal
```

### Git 仓库安装

适合团队发布。假设内部仓库地址是：

```text
git@your-company.example:product/product-workflows.git
```

团队成员执行：

```bash
codex plugin marketplace add git@your-company.example:product/product-workflows.git --ref main
codex plugin add pm-superpowers@pm-superpowers-internal
```

如果公司使用 HTTPS 仓库，把地址替换成 HTTPS 地址即可。

## 发版流程

每次更新插件时建议按这个流程：

1. 修改技能、references、templates 或文档。
2. 如果更新了底层 PM 方法技能，先运行 `plugins/pm-superpowers/scripts/sync_pm_skills.py`。
3. 运行插件校验。
4. 运行所有技能校验。
5. 更新 `plugins/pm-superpowers/.codex-plugin/plugin.json` 的版本号。
6. 提交到内部仓库。
7. 通知团队更新插件。
8. 团队成员重新安装或更新后，新开一个 Codex thread 使用。

## 更新底层 68 个 PM 方法技能

开发人员先把认可来源同步到本地源目录，默认源目录是：

```text
<repo-root>/.codex/skills
```

然后在仓库根目录运行：

```bash
python3 plugins/pm-superpowers/scripts/sync_pm_skills.py
```

如果源目录不在默认位置，可以指定：

```bash
python3 plugins/pm-superpowers/scripts/sync_pm_skills.py --source /path/to/approved-pm-skills
```

同步脚本只覆盖批准清单中的 68 个 PM 方法技能，不会覆盖 PM Superpowers 自身的场景/治理技能。同步时还会自动给每个方法技能注入中文输出要求，确保这些底层技能随 PM Superpowers 发布后默认遵循中文产物标准。

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

## 版本规则

建议使用语义化版本：

- `0.1.x`：试点期修复文案、模板、说明。
- `0.2.x`：新增或调整工作流。
- `1.0.0`：团队正式采用，流程稳定。
- `2.0.0`：产物结构或工作流有破坏性变化。

当前已进入 `0.4.3` 试点版本。`0.4.0` 重点把 68 个 PM 方法技能内置到插件包内，让团队成员只安装 PM Superpowers 即可使用完整产品工作流；`0.4.1` 补充了用户下载安装和首次使用指南，并整理了文档目录说明；`0.4.2` 修正了 GitHub 文档中的本机绝对路径；`0.4.3` 将 PRD 模板升级为自适应结构。

## 试点建议

第一阶段不要一上来全员强制。建议先选：

- 1-2 位资深 PM。
- 2-3 位刚接触产品工作的同事。
- 1 位设计代表。
- 1 位研发代表。

试点重点看：

- 场景识别是否准确。
- `BLOCKED` 是否真的挡住了没想清楚的需求。
- PRD 和交接材料是否减少设计、研发返工。
- 哪些公司专属规范需要加入 references。

## 什么时候更新 68 个 PM 方法技能

如果新增的是一个独立产品方法，更新底层 PM 方法技能清单，然后同步到 PM Superpowers：

- 新的定价方法。
- 新的竞品分析方法。
- 新的访谈总结方法。
- 新的实验分析方法。

如果新增的是一个流程、场景、门禁或模板，更新 PM Superpowers：

- 新增“数据产品需求评审”场景。
- 改 PRD 必填字段。
- 增加研发交接门禁。
- 调整上线清单。

## 内部推广话术

给团队说明时可以这样讲：

```text
PM Superpowers 是我们的产品工作流插件。
它不会替代大家的判断，而是把高频产品场景、标准产物、门禁和交接要求固化下来。
新同事可以按场景学习，老同事可以用它统一输出标准。
68 个 PM 方法技能已经内置在插件里，大家只需要安装 PM Superpowers 一个插件。
```
