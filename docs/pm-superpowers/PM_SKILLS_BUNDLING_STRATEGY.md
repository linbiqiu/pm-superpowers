# PM skills 内置策略说明

## 结论

PM Superpowers 应该默认内置底层 68 个 PM method skills。

这样对使用者最简单：团队成员只需要安装 PM Superpowers 一个插件，就能获得场景工作流、门禁、中文模板、项目工作区初始化能力，以及底层产品方法库。

同时，插件开发人员仍然可以随时更新底层方法技能：先从认可来源同步 68 个 PM method skills，再随 PM Superpowers 一起发版。

## 为什么内置更适合内部团队

如果不内置，团队成员需要先安装 `pm-skills`，再安装 PM Superpowers。这个方式对开发者清晰，但对普通使用者不够友好，容易出现几个问题：

- 新同事不知道还要额外安装底层技能。
- 有人只装了 PM Superpowers，实际使用时缺少 `create-prd`、`market-sizing`、`ab-test-analysis` 等方法技能。
- 不同同事安装的底层技能版本不一致，输出标准容易漂移。
- 内部培训时还要解释两套插件、两套更新方式，推广成本更高。

内置后，使用者只需要理解一个入口：PM Superpowers。

## 内置不等于重写

内置 68 个 PM method skills，不代表把它们重写进 PM Superpowers 的场景技能里。

正确做法是：

- 68 个方法技能仍然保留独立目录和独立技能名。
- 18 个 PM Superpowers 场景/治理技能负责选择、组合、检查和交接。
- 方法技能负责“怎么做某个方法”，例如写 PRD、做市场规模测算、设计 A/B 实验。
- 场景技能负责“现在该不该做、按什么顺序做、做到什么程度才能进入下一步”。

这样既保证用户安装简单，又保证架构上不混乱。

## PM method skills 直通契约

为了避免 PM Superpowers 的场景工作流限制底层方法技能，插件保留 PM method skills 的直通使用方式。

当用户明确点名某个底层方法技能，或明确要求使用某个产品方法时，优先允许直接执行该方法技能。例如：

```text
直接用 market-sizing 帮我估算这个市场规模。
用 ab-test-analysis 分析这组实验结果。
帮我生成 interview-script。
```

直通时的规则：

- 方法技能仍然使用自己的原子方法结构。
- 输出默认遵循中文输出规范。
- 不强制套完整场景工作流，不要求先经过 S0-S10。
- 只在输出要变成 PRD、路线图承诺、UI/研发交接或上线计划时，再补 `pm-gate-review` 或 `downstream-readiness`。
- 场景/治理技能不能把底层方法技能重写成更浅的同名替代品。

这条契约保证高级 PM 可以直接调用方法工具，新人也可以通过 PM Superpowers 场景层获得流程保护。

## 当前插件结构

```text
plugins/pm-superpowers/
  .codex-plugin/plugin.json
  skills/
    pm-workflow-router/
    prd-standardization/
    downstream-readiness/
    create-prd/
    market-sizing/
    ab-test-analysis/
    ...
  references/
  assets/
  scripts/
    sync_pm_skills.py
```

`skills/` 目录里共有 86 个技能：

- 18 个 PM Superpowers 场景/治理技能。
- 68 个内置 PM method skills。

## 开发者如何更新底层 PM method skills

默认同步来源是仓库内的：

```text
<repo-root>/.codex/skills
```

更新步骤：

1. 先把上游或团队认可的 PM method skills 更新到本地源目录。
2. 在仓库根目录运行同步脚本。
3. 运行插件校验。
4. 运行所有技能校验。
5. 更新插件版本号。
6. 提交并推送到内部仓库。
7. 通知团队更新插件并新开 Codex thread。

同步命令：

```bash
python3 plugins/pm-superpowers/scripts/sync_pm_skills.py
```

如果源目录不在默认位置：

```bash
python3 plugins/pm-superpowers/scripts/sync_pm_skills.py --source /path/to/approved-pm-skills
```

同步脚本只覆盖批准清单中的 68 个 PM method skills，不会覆盖 PM Superpowers 自己的场景/治理技能。

同步脚本还会给每个内置方法技能自动注入 PM Superpowers 本地 overlay，要求技能先读取中文输出规范，并默认以中文输出用户可见内容。这样即使原始方法技能正文是英文，团队使用时仍然遵循中文产物标准。

## 版本策略

建议按影响范围决定版本号：

- Patch：修正文案、模板、小错误，底层方法技能没有结构性变化。
- Minor：同步底层 PM method skills、新增方法技能、新增场景工作流、新增项目工作区模板。
- Major：破坏性修改输出结构、门禁规则或团队协作规范。

本次把 68 个 PM method skills 内置进插件，属于 Minor 版本，因此从 `0.3.0` 升级到 `0.4.0`。

## 重复安装怎么办

如果用户本机同时启用了外部 `pm-skills` 插件集和 PM Superpowers，可能会看到重复的同名方法技能。

团队正式推广时建议：

- 普通使用者只安装 PM Superpowers。
- 插件开发者可以保留外部 `pm-skills` 作为对比和同步来源。
- 发现技能列表重复时，优先保留 PM Superpowers，停用外部 `pm-skills` 插件集。

## 给团队的简单说明

可以这样对团队解释：

```text
PM Superpowers 是我们的产品工作流插件。
它已经内置常用的 68 个产品方法技能，所以大家只需要安装一个插件。
使用时不用记住所有技能名，直接描述场景，插件会判断该走探索、PRD、用户研究、路线图、指标实验、上线准备还是日常运营流程。
如果信息没想清楚，插件会先阻断并提示需要补齐什么，避免没准备好就进入 UI 或研发。
```
