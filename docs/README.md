# 文档目录说明

本目录分两类材料：

## 正式用户文档

位置：`docs/pm-superpowers/`

这里是给团队用户、产品经理、插件维护者直接阅读的正式文档。优先从下面几份开始：

- `PM_SUPERPOWERS_INSTALL_AND_USAGE.md`：下载、安装、更新和第一次使用。
- `PM_SUPERPOWERS_FEISHU_INTERNAL_GUIDE.md`：适合复制/导入飞书云文档的内部传播介绍，覆盖安装、使用和高频场景。
- `PM_SUPERPOWERS_UPDATE_GUIDE.md`：检查版本、更新插件和团队通知方式。
- `PM_SUPERPOWERS_USER_GUIDE.md`：按场景使用 PM Superpowers。
- `PM_SUPERPOWERS_SCENARIO_DEEP_DIVE.md`：十个高频产品场景的深入说明。
- `PM_SUPERPOWERS_PLUGIN_DESIGN.md`：插件设计理念和架构。
- `PM_SUPERPOWERS_RELEASE_GUIDE.md`：内部发版和维护方式。

## 规划过程材料

位置：`docs/planning/`

这里保留的是插件设计早期的讨论、方案推演和场景规划材料。它们用于追溯设计思路，不作为最终用户安装或操作说明。正式使用时以 `docs/pm-superpowers/` 为准。

## 为什么插件目录里有很多 skill 文件

PM Superpowers 当前内置 86 个技能：

- 18 个 PM Superpowers 场景/治理技能。
- 68 个 PM method skills。

这些技能必须放在 `plugins/pm-superpowers/skills/` 的直接子目录下，Codex 才能发现并加载。看起来文件较多是正常现象，不是重复生成的临时文件。
