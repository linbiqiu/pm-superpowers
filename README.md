# PM Superpowers

PM Superpowers 是面向中国团队的 Codex 产品经理工作流插件。它把现有 PM skills 方法库编排成场景化产品工作流，帮助产品经理完成需求澄清、产品探索、PRD、路线图、用户研究、指标实验、上线准备、日常运营和 UI/研发交接。

## 核心定位

- 默认以中文输出产品产物。
- 先判断场景，再进入工作流。
- 信息不足时阻断，不强行写完整文档。
- 把事实、用户原话、信号、假设、意见和承诺分开。
- 用门禁检查保护设计、研发、测试和上线质量。
- 可初始化产品项目工作区，生成 `AGENTS.md`、产品上下文、决策记录、证据表、风险清单和下游交接检查。

## 仓库结构

```text
.agents/plugins/marketplace.json        # 内部 marketplace 入口
plugins/pm-superpowers/                 # Codex 插件源码
  .codex-plugin/plugin.json
  skills/                               # 插件技能
  references/                           # 运行时规范
  assets/templates/                     # 中文产品产物模板
  assets/project-workspace/             # 用户项目初始化模板
docs/pm-superpowers/                    # 用户、设计、发版和项目工作区文档
docs/planning/                          # 早期规划和圆桌讨论材料
AGENTS.md                               # 本仓库的智能体协作规范
```

## 当前版本

插件版本：`0.3.0`

主要能力：

- 18 个插件技能。
- 9 份运行时规范。
- 14 份中文交付模板。
- 1 套产品项目工作区初始化模板。
- 6 份正式使用和维护文档。

## 本地安装

在本仓库根目录执行：

```bash
codex plugin marketplace add /Users/linbiqiu/Documents/product
codex plugin add pm-superpowers@pm-superpowers-internal
```

安装或更新后，新开一个 Codex thread，插件技能才会完整加载。

## 团队安装

把本仓库发布到内部 Git 平台后，团队成员执行：

```bash
codex plugin marketplace add <internal-repo-url> --ref main
codex plugin add pm-superpowers@pm-superpowers-internal
```

团队仍需安装现有 `pm-skills` 插件集。PM Superpowers 不复制 68 个 PM skills，而是把它们作为底层方法库进行编排和治理。

## 重要文档

- [使用手册](/Users/linbiqiu/Documents/product/docs/pm-superpowers/PM_SUPERPOWERS_USER_GUIDE.md)
- [高频场景深度手册](/Users/linbiqiu/Documents/product/docs/pm-superpowers/PM_SUPERPOWERS_SCENARIO_DEEP_DIVE.md)
- [插件设计说明](/Users/linbiqiu/Documents/product/docs/pm-superpowers/PM_SUPERPOWERS_PLUGIN_DESIGN.md)
- [技能说明书](/Users/linbiqiu/Documents/product/docs/pm-superpowers/PM_SUPERPOWERS_SKILL_MANUAL.md)
- [产品项目工作区指南](/Users/linbiqiu/Documents/product/docs/pm-superpowers/PM_PROJECT_WORKSPACE_GUIDE.md)
- [内部发版指南](/Users/linbiqiu/Documents/product/docs/pm-superpowers/PM_SUPERPOWERS_RELEASE_GUIDE.md)

## 校验

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

## 远程仓库发布

如果使用 GitHub，需要先登录：

```bash
gh auth login
```

然后创建远程仓库并推送：

```bash
gh repo create pm-superpowers --private --source=. --remote=origin --push
```

如果公司使用内部 Git 平台，先创建空仓库，再执行：

```bash
git remote add origin <internal-repo-url>
git push -u origin main
```

