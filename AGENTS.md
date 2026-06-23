# AGENTS.md

本文件是 PM Superpowers 仓库的智能体协作规范。所有 agent 在修改本仓库时必须先阅读本文件。

## 仓库目标

本仓库维护一个面向中国团队的 Codex 产品经理工作流插件。插件需要帮助用户按产品场景推进工作，并默认输出中文产品产物。

## 默认语言

- 面向用户的文档、模板、说明和交付产物默认使用中文。
- 技能名、插件名、文件名、英文框架名可保留英文，但需要在用户文档中解释中文含义。
- 不要新增默认英文模板。

## 目录约定

- 插件源码放在 `plugins/pm-superpowers/`。
- 用户文档和维护文档放在 `docs/pm-superpowers/`。
- 规划过程材料放在 `docs/planning/`。
- 项目级 marketplace 放在 `.agents/plugins/marketplace.json`。
- 不提交 `.codex/`，它是本地技能安装目录。

## 插件修改规则

- 修改插件 manifest 后运行插件校验。
- 新增或修改技能后运行所有技能校验。
- 新增用户可见输出模板时必须使用中文字段。
- 新增工作流时要说明场景、输入、门禁、产物和下游交接。
- PM Superpowers 内置 68 个 PM method skills 作为随插件发布的方法库快照；不要把这些方法技能重写成一个大技能。
- 更新底层 PM method skills 时，优先使用 `plugins/pm-superpowers/scripts/sync_pm_skills.py` 从认可来源同步，再运行所有技能校验。

## 校验命令

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/plugin-creator/scripts/validate_plugin.py" plugins/pm-superpowers
```

```bash
for d in plugins/pm-superpowers/skills/*; do
  python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" "$d"
done
```

## 发版规则

- Patch：模板、文档、小修复。
- Minor：新增技能、新增项目工作区模板、新增场景工作流。
- Major：破坏性修改输出结构或团队工作规范。

当前版本：`0.4.2`

## Git 规则

- 不提交 `.DS_Store`。
- 不提交 `.codex/` 本地安装目录。
- 提交前检查 `git status --short`。
- 提交信息使用清晰中文或英文均可，但要说明变更范围。
