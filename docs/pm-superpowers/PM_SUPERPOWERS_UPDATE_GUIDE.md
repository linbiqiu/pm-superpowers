# PM Superpowers 更新指南

这份文档说明团队用户如何知道插件有新版本、如何更新，以及为什么更新后需要新开 Codex thread。

## 先说结论

Codex 插件不会在后台静默自动更新。

当 PM Superpowers 在 GitHub 上发布新版本后，用户本地需要执行更新命令，或者运行仓库提供的一键更新脚本。更新完成后，还需要新开一个 Codex thread，旧 thread 通常不会自动加载新版本技能。

## 为什么不建议静默自动更新

PM Superpowers 不只是一个工具脚本，它会影响：

- 产品工作流。
- PRD、路线图、指标、上线等模板。
- 门禁规则。
- UI 和研发交接标准。

如果静默自动更新，用户可能不知道为什么模板变了、门禁变严了、输出结构不同了。因此更稳妥的方式是：

- 版本号明确。
- `CHANGELOG.md` 记录变化。
- 团队发布通知。
- 用户主动更新。
- 更新后新开 thread 生效。

## 如何知道有新版本

推荐三种方式一起使用：

1. 查看 GitHub Release 或仓库首页。
2. 查看 `CHANGELOG.md`。
3. 运行版本检查脚本。

版本检查脚本：

```bash
scripts/check_pm_superpowers_update.sh
```

它会显示：

- 本地安装版本。
- GitHub 远程版本。
- 是否需要更新。
- 推荐更新命令。

## 一键更新

在仓库根目录执行：

```bash
scripts/update_pm_superpowers.sh
```

脚本会执行：

1. 检查是否已添加 `pm-superpowers-internal` marketplace。
2. 如果没有，自动添加 GitHub marketplace。
3. 刷新 marketplace 快照。
4. 重新安装 `pm-superpowers` 插件。
5. 打印本地版本和远程版本。

更新完成后，请新开 Codex thread。

如果你的环境访问 GitHub HTTPS 不稳定，但 SSH 可以访问 GitHub，可以这样更新：

```bash
PM_SUPERPOWERS_REPO=git@github.com:linbiqiu/pm-superpowers.git scripts/update_pm_superpowers.sh
```

## 手动更新

如果你不想使用脚本，可以手动执行：

```bash
codex plugin marketplace upgrade pm-superpowers-internal
codex plugin add pm-superpowers@pm-superpowers-internal
```

如果还没有添加 marketplace，先执行：

```bash
codex plugin marketplace add linbiqiu/pm-superpowers --ref main
codex plugin add pm-superpowers@pm-superpowers-internal
```

## 本地 clone 安装的用户如何更新

如果你是通过本地 checkout 安装的：

```bash
cd /path/to/pm-superpowers
git pull
codex plugin add pm-superpowers@pm-superpowers-internal
```

然后新开 Codex thread。

## 团队发布建议

每次发布新版本时，维护者应同步三件事：

1. 更新 `plugins/pm-superpowers/.codex-plugin/plugin.json` 版本号。
2. 更新 `CHANGELOG.md`。
3. 发团队通知。

团队通知可以使用这个格式：

```text
PM Superpowers 已更新到 x.y.z。

主要变化：
- ...
- ...

更新方式：
scripts/update_pm_superpowers.sh

更新后请新开 Codex thread。
```

## 常见问题

### 更新后为什么旧 thread 还是旧行为？

插件技能是在 thread 启动时加载的。更新插件后，需要新开 Codex thread。

### 脚本显示本地版本带 `+codex.xxx` 是什么？

这是本地缓存刷新标记，不影响正式版本判断。例如：

```text
0.4.3+codex.20260623111011
```

它对应的正式版本是：

```text
0.4.3
```

### 能否完全自动更新？

不建议。产品工作流插件会影响团队规范，应该让用户知道版本变化，并主动选择更新。
