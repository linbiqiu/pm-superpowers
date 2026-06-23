# PM Superpowers 下载安装和使用指南

这份文档给团队成员使用，目标是让不熟悉插件机制的同事也能完成安装、更新和第一次使用。

## 你需要先知道的事

PM Superpowers 是一个 Codex 插件，不是普通网页应用，也不是需要双击打开的软件。

安装后，你在 Codex 里描述产品工作场景，例如“帮我梳理这个需求应该怎么推进”，插件会自动选择合适的产品经理工作流，并默认输出中文产品产物。

当前插件已经内置 68 个 PM 方法技能。普通用户只需要安装 PM Superpowers 一个插件，不需要单独安装 `pm-skills`。

## 安装前准备

请确认你已经具备：

- 已安装 Codex。
- 能访问团队 GitHub 或内部 Git 仓库。
- 如果仓库是私有仓库，你的 GitHub 账号已经有访问权限。
- 终端里可以运行 `codex` 命令。

如果运行下面命令能看到帮助信息，说明 Codex CLI 可用：

```bash
codex plugin --help
```

## 推荐安装方式：从 GitHub 仓库安装

适合团队成员使用。

当前仓库地址：

```text
https://github.com/linbiqiu/pm-superpowers
```

如果仓库是私有仓库，先确保本机已经登录 GitHub，或者至少能通过 `git clone` 访问这个仓库。可以使用：

```bash
gh auth login
```

然后添加插件 marketplace：

```bash
codex plugin marketplace add linbiqiu/pm-superpowers --ref main
```

安装插件：

```bash
codex plugin add pm-superpowers@pm-superpowers-internal
```

确认安装结果：

```bash
codex plugin list
```

看到类似下面的信息，就说明插件已经安装并启用：

```text
pm-superpowers@pm-superpowers-internal  installed, enabled
```

安装完成后，请新开一个 Codex thread。已经打开的旧 thread 不一定会加载新安装的插件技能。

## 本地 checkout 安装方式

适合插件开发者、试点同事或需要从本地仓库验证的人。

先下载仓库：

```bash
git clone https://github.com/linbiqiu/pm-superpowers.git
cd pm-superpowers
```

添加本地 marketplace：

```bash
codex plugin marketplace add "$(pwd)"
```

安装插件：

```bash
codex plugin add pm-superpowers@pm-superpowers-internal
```

安装完成后，同样需要新开一个 Codex thread。

## 更新插件

推荐使用一键更新脚本：

```bash
scripts/check_pm_superpowers_update.sh
scripts/update_pm_superpowers.sh
```

更新完成后请新开一个 Codex thread。

如果 GitHub HTTPS 连接不稳定，但 SSH 可以访问 GitHub：

```bash
PM_SUPERPOWERS_REPO=git@github.com:linbiqiu/pm-superpowers.git scripts/update_pm_superpowers.sh
```

如果你是从 GitHub marketplace 安装的：

```bash
codex plugin marketplace upgrade pm-superpowers-internal
codex plugin add pm-superpowers@pm-superpowers-internal
```

如果你是从本地 checkout 安装的：

```bash
cd /path/to/pm-superpowers
git pull
codex plugin add pm-superpowers@pm-superpowers-internal
```

更新后请新开一个 Codex thread。

更详细的版本检查和更新说明见：

- [PM_SUPERPOWERS_UPDATE_GUIDE.md](PM_SUPERPOWERS_UPDATE_GUIDE.md)

## 第一次怎么用

不要一开始就要求插件直接写完整 PRD。更推荐先让它判断你当前属于哪个产品工作场景。

可以这样问：

```text
我现在有一个比较粗的产品想法，请先帮我判断应该走哪个 PM 工作流，并告诉我还缺哪些关键信息。
```

也可以直接描述真实业务：

```text
我们想做一个给销售主管看的 AI 周报功能，目标是减少人工整理时间。请帮我按 PM Superpowers 的方式梳理产品思路。
```

如果你已经有 PRD：

```text
请按 PM Superpowers 检查这份 PRD 是否可以交给 UI 和研发，如果不能，请指出阻断项。
```

如果你要把一个项目纳入产品空间管理：

```text
请初始化当前项目的产品工作区，创建 AGENTS.md、产品上下文、决策记录、证据表、风险清单和下游交接检查。
```

## 常见使用场景

| 你要做的事 | 推荐说法 |
| --- | --- |
| 想法很粗，不知道怎么推进 | “请先判断这个产品问题应该走哪个 PM 工作流。” |
| 做新产品或新功能探索 | “请帮我做新产品探索，先不要直接写 PRD。” |
| 优化已有功能 | “请帮我分析这个功能表现不好应该怎么优化。” |
| 把用户反馈变成需求池 | “请把这些反馈分类、聚合，并转成路线图候选。” |
| 写或评审 PRD | “请按 PM Superpowers 标准整理成可评审 PRD。” |
| 做用户研究 | “请帮我设计研究计划和访谈脚本。” |
| 排优先级和路线图 | “请帮我做优先级判断和 outcome roadmap。” |
| 做指标和实验 | “请帮我定义指标、实验方案和判断方式。” |
| 上线前检查 | “请检查这个版本是否具备上线条件。” |
| 会议或复盘 | “请整理会议纪要、行动项、决策记录和风险。” |

## 使用时要遵守的原则

- 信息不足时，插件可能输出 `BLOCKED`。这不是失败，而是在提醒你不要没想清楚就进入下一步。
- 插件默认用中文输出；英文框架名会保留，但应补充中文解释。
- 产品产物要交给 UI 或研发前，建议运行下游交接检查。
- 如果你看到很多底层技能名，不需要自己逐个挑选。直接描述场景，插件会自动选择。

## 常见问题

### 安装后为什么当前 thread 里看不到插件？

新安装或更新插件后，需要新开一个 Codex thread。旧 thread 通常不会自动加载新插件技能。

### 还需要单独安装 pm-skills 吗？

不需要。PM Superpowers 已经内置 68 个 PM 方法技能。

如果你本机之前安装过外部 `pm-skills` 插件集，可能会在技能列表里看到重复的技能名。普通用户建议只保留 PM Superpowers，避免重复展示。

### 插件目录里为什么有很多 skills？

这是正常的。PM Superpowers 由 18 个场景/治理技能和 68 个方法技能组成。Codex 需要这些技能以独立目录形式存在，才能按场景自动触发。

### 怎么确认安装的是最新版本？

运行：

```bash
codex plugin list
```

查看 `pm-superpowers@pm-superpowers-internal` 的版本号。当前正式版本见仓库根目录的 `CHANGELOG.md`。

### 使用时应该先读哪份文档？

建议顺序：

1. 本文档：完成安装和第一次使用。
2. `PM_SUPERPOWERS_USER_GUIDE.md`：学习日常怎么按场景使用。
3. `PM_SUPERPOWERS_SCENARIO_DEEP_DIVE.md`：深入理解十个高频产品场景。
4. `PM_PROJECT_WORKSPACE_GUIDE.md`：学习如何把产品项目沉淀成长期工作区。
