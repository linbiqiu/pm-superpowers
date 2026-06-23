# Changelog

## 0.4.2

- 修正 GitHub 文档中的本机绝对路径，统一改为相对链接、`<repo-root>`、`$(pwd)` 或 `${CODEX_HOME:-$HOME/.codex}`。
- 修复 planning 文档中指向本机路径的 Markdown 链接。
- 更新 README、AGENTS、发版指南、审计文档和用户手册中的路径示例。

## 0.4.1

- 新增用户下载安装和使用指南，覆盖 GitHub 安装、本地安装、更新和首次使用。
- 新增 `docs/README.md` 和 `docs/planning/README.md`，区分正式文档和规划过程材料。
- 清理本地 `.DS_Store` 文件，减少目录干扰。

## 0.4.0

- 将 68 个 PM method skills 内置到 PM Superpowers 插件包内。
- 新增 `scripts/sync_pm_skills.py`，支持开发者从认可来源同步底层方法技能。
- 更新 README、插件设计说明、技能说明书、内部发版指南和运行时 reference，明确用户只需安装 PM Superpowers。
- 新增 `PM_SKILLS_BUNDLING_STRATEGY.md`，说明内置策略、更新流程、版本规则和重复安装处理。

## 0.3.0

- 新增 `pm-project-initializer` 技能。
- 新增产品项目工作区标准和初始化模板。
- 新增仓库级 `README.md`、`AGENTS.md` 和 `.gitignore`。
- 补充产品项目工作区使用指南。

## 0.2.0

- 增加中文输出规范。
- 17 个插件技能接入中文输出规范。
- 14 份核心模板中文化。
- 深度场景手册升级为面向用户和学习者的版本。

## 0.1.0

- 初始化 PM Superpowers 插件。
- 创建 17 个产品经理场景和控制技能。
- 创建运行时 references、标准模板和用户文档。
- 创建内部 marketplace。
