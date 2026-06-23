# PM Superpowers 内部发版指南

这份文档回答两个问题：

1. 现有 68 个 PM skills 怎么处理？
2. PM Superpowers 插件开发好后，如何发给内部团队使用？

## 现有 68 个 PM skills 怎么处理

结论：保留为底层方法库，不复制、不重写、不塞进一个大技能里。

原因：

- 68 个 skills 已经覆盖很多产品方法，如 PRD、用户研究、市场分析、实验、GTM、路线图等。
- 它们适合做单点方法，但不负责判断场景和流程顺序。
- 如果复制到新插件里，会产生两份维护源，后续版本容易冲突。
- PM Superpowers 要解决的是“怎么选、怎么串、怎么检查、怎么交接”。

推荐分工：

| 层级 | 负责内容 | 示例 |
| --- | --- | --- |
| PM skills 方法库 | 原子产品方法 | `create-prd`、`market-sizing`、`ab-test-analysis` |
| PM Superpowers | 场景工作流和门禁 | `new-product-discovery`、`prd-standardization`、`downstream-readiness` |
| 团队文档 | 学习材料和公司规范 | 场景手册、发版指南、模板说明 |

## 团队安装前置

团队成员需要两类能力：

- 已安装团队认可的 PM skills 插件集。
- 安装 PM Superpowers 插件。

如果团队未来把 PM skills 和 PM Superpowers 放在同一个内部 marketplace，也可以统一安装；但逻辑上仍然建议保持“方法库”和“工作流插件”分层。

## 当前项目内插件位置

当前插件结构：

```text
plugins/pm-superpowers/
  .codex-plugin/plugin.json
  skills/
  references/
  assets/templates/

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
codex plugin marketplace add /Users/linbiqiu/Documents/product
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
2. 运行插件校验。
3. 运行所有技能校验。
4. 更新 `plugins/pm-superpowers/.codex-plugin/plugin.json` 的版本号。
5. 提交到内部仓库。
6. 通知团队更新插件。
7. 团队成员重新安装或更新后，新开一个 Codex thread 使用。

## 校验命令

插件校验：

```bash
python3 /Users/linbiqiu/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py /Users/linbiqiu/Documents/product/plugins/pm-superpowers
```

技能校验：

```bash
for d in /Users/linbiqiu/Documents/product/plugins/pm-superpowers/skills/*; do
  python3 /Users/linbiqiu/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$d"
done
```

## 版本规则

建议使用语义化版本：

- `0.1.x`：试点期修复文案、模板、说明。
- `0.2.x`：新增或调整工作流。
- `1.0.0`：团队正式采用，流程稳定。
- `2.0.0`：产物结构或工作流有破坏性变化。

当前已进入 `0.3.0` 试点版本，重点补齐了中文输出规范、中文模板、面向用户的深度场景手册，以及产品项目工作区初始化能力。

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

## 什么时候更新 68 个 PM skills

如果新增的是一个独立产品方法，更新 PM skills：

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
现有 68 个 PM skills 仍然作为底层方法库，新插件负责编排这些方法。
```
