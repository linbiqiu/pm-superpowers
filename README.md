# PM Superpowers

PM Superpowers 是面向中国团队的 Codex 产品经理工作流插件。它内置 68 个 PM 方法技能，并把这些方法技能编排成场景化产品工作流，帮助产品经理完成需求澄清、产品探索、PRD、路线图、用户研究、指标实验、上线准备、日常运营和 UI/研发交接。

## 核心定位

- 默认以中文输出产品产物。
- 先判断场景，再进入工作流。
- 信息不足时阻断，不强行写完整文档。
- 把事实、用户原话、信号、假设、意见和承诺分开。
- 用门禁检查保护设计、研发、测试和上线质量。
- 可初始化产品项目工作区，生成 `AGENTS.md`、产品上下文、决策记录、证据表、风险清单和下游交接检查。
- 团队成员只需要安装 PM Superpowers 插件，不需要额外安装底层 `pm-skills` 插件集。

## 仓库结构

```text
.agents/plugins/marketplace.json        # 内部 marketplace 入口
plugins/pm-superpowers/                 # Codex 插件源码
  .codex-plugin/plugin.json
  skills/                               # 插件技能
  references/                           # 运行时规范
  assets/templates/                     # 中文产品产物模板
  assets/project-workspace/             # 用户项目初始化模板
scripts/                                # 用户检查和更新脚本
docs/pm-superpowers/                    # 用户、设计、发版和项目工作区文档
docs/planning/                          # 早期规划和圆桌讨论材料
docs/README.md                          # 文档目录说明
AGENTS.md                               # 本仓库的智能体协作规范
```

## 当前版本

插件版本：`0.4.8`

主要能力：

- 86 个插件技能：18 个 PM Superpowers 场景/治理技能，68 个内置 PM 方法技能。
- 10 份运行时规范和行为回归契约。
- 14 份中文交付模板。
- 1 套产品项目工作区初始化模板。
- 9 份正式使用和维护文档。

## 本地安装

在本仓库根目录执行：

```bash
codex plugin marketplace add "$(pwd)"
codex plugin add pm-superpowers@pm-superpowers-internal
```

安装或更新后，新开一个 Codex thread，插件技能才会完整加载。

检查和更新插件：

```bash
scripts/check_pm_superpowers_update.sh
scripts/update_pm_superpowers.sh
```

## 团队安装

把本仓库发布到内部 Git 平台后，团队成员执行：

```bash
codex plugin marketplace add <internal-repo-url> --ref main
codex plugin add pm-superpowers@pm-superpowers-internal
```

团队成员只需要安装 `pm-superpowers`。68 个 PM 方法技能已经随插件内置，作为底层方法库被场景工作流编排和治理。

如果插件开发人员需要更新底层 PM 方法技能，先把认可来源同步到本地源目录，再运行：

```bash
python3 plugins/pm-superpowers/scripts/sync_pm_skills.py
```

同步后必须运行插件校验和所有技能校验，再发版给团队。

## 重要文档

- [使用手册](docs/pm-superpowers/PM_SUPERPOWERS_USER_GUIDE.md)
- [下载安装和使用指南](docs/pm-superpowers/PM_SUPERPOWERS_INSTALL_AND_USAGE.md)
- [更新指南](docs/pm-superpowers/PM_SUPERPOWERS_UPDATE_GUIDE.md)
- [高频场景深度手册](docs/pm-superpowers/PM_SUPERPOWERS_SCENARIO_DEEP_DIVE.md)
- [插件设计说明](docs/pm-superpowers/PM_SUPERPOWERS_PLUGIN_DESIGN.md)
- [技能说明书](docs/pm-superpowers/PM_SUPERPOWERS_SKILL_MANUAL.md)
- [PM skills 内置策略](docs/pm-superpowers/PM_SKILLS_BUNDLING_STRATEGY.md)
- [产品项目工作区指南](docs/pm-superpowers/PM_PROJECT_WORKSPACE_GUIDE.md)
- [内部发版指南](docs/pm-superpowers/PM_SUPERPOWERS_RELEASE_GUIDE.md)

## 校验

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

行为回归契约校验：

```bash
python3 plugins/pm-superpowers/scripts/validate_behavior_regression.py
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
