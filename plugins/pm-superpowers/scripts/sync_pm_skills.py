#!/usr/bin/env python3
"""Sync bundled PM method skills into the PM Superpowers plugin."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


PM_METHOD_SKILLS = [
    "ab-test-analysis",
    "analyze-feature-requests",
    "ansoff-matrix",
    "beachhead-segment",
    "brainstorm-experiments-existing",
    "brainstorm-experiments-new",
    "brainstorm-ideas-existing",
    "brainstorm-ideas-new",
    "brainstorm-okrs",
    "business-model",
    "cohort-analysis",
    "competitive-battlecard",
    "competitor-analysis",
    "create-prd",
    "customer-journey-map",
    "draft-nda",
    "dummy-dataset",
    "grammar-check",
    "growth-loops",
    "gtm-motions",
    "gtm-strategy",
    "ideal-customer-profile",
    "identify-assumptions-existing",
    "identify-assumptions-new",
    "intended-vs-implemented",
    "interview-script",
    "job-stories",
    "lean-canvas",
    "market-segments",
    "market-sizing",
    "marketing-ideas",
    "metrics-dashboard",
    "monetization-strategy",
    "north-star-metric",
    "opportunity-solution-tree",
    "outcome-roadmap",
    "pestle-analysis",
    "porters-five-forces",
    "positioning-ideas",
    "pre-mortem",
    "pricing-strategy",
    "prioritization-frameworks",
    "prioritize-assumptions",
    "prioritize-features",
    "privacy-policy",
    "product-name",
    "product-strategy",
    "product-vision",
    "release-notes",
    "retro",
    "review-resume",
    "sentiment-analysis",
    "shipping-artifacts",
    "sprint-plan",
    "sql-queries",
    "stakeholder-map",
    "startup-canvas",
    "strategy-red-team",
    "summarize-interview",
    "summarize-meeting",
    "swot-analysis",
    "test-scenarios",
    "user-personas",
    "user-segmentation",
    "user-stories",
    "value-prop-statements",
    "value-proposition",
    "wwas",
]

OVERLAY_START = "<!-- PM_SUPERPOWERS_LOCAL_OVERLAY_START -->"
OVERLAY_END = "<!-- PM_SUPERPOWERS_LOCAL_OVERLAY_END -->"
CHINESE_OUTPUT_OVERLAY = f"""{OVERLAY_START}

## PM Superpowers 中文输出要求

在 PM Superpowers 插件内使用本方法技能时，先读取 `../../references/chinese-output-standard.md`。除非用户明确要求英文或双语，所有用户可见输出必须以中文为核心语言；保留英文框架名、技能名或文件名时，需要补充中文解释。

{OVERLAY_END}

"""


def ignore_names(_: str, names: list[str]) -> set[str]:
    return {name for name in names if name in {".DS_Store", "__pycache__"}}


def apply_local_overlay(skill_md: Path) -> None:
    text = skill_md.read_text(encoding="utf-8")
    text = re.sub(
        rf"{re.escape(OVERLAY_START)}.*?{re.escape(OVERLAY_END)}\n\n?",
        "",
        text,
        flags=re.DOTALL,
    )

    if text.startswith("---\n"):
        frontmatter_end = text.find("\n---", 4)
        if frontmatter_end != -1:
            insert_at = frontmatter_end + len("\n---\n")
            text = text[:insert_at] + "\n" + CHINESE_OUTPUT_OVERLAY + text[insert_at:]
        else:
            text = CHINESE_OUTPUT_OVERLAY + text
    else:
        text = CHINESE_OUTPUT_OVERLAY + text

    skill_md.write_text(text, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    script_path = Path(__file__).resolve()
    default_plugin_root = script_path.parents[1]
    default_source = default_plugin_root.parents[1] / ".codex" / "skills"

    parser = argparse.ArgumentParser(
        description="Sync the approved 68 PM method skills into PM Superpowers."
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=default_source,
        help="Source directory containing the 68 PM skill folders.",
    )
    parser.add_argument(
        "--plugin-root",
        type=Path,
        default=default_plugin_root,
        help="PM Superpowers plugin root.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned changes without writing files.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_root = args.source.expanduser().resolve()
    plugin_root = args.plugin_root.expanduser().resolve()
    target_root = plugin_root / "skills"

    if not source_root.exists():
        raise SystemExit(f"Source directory not found: {source_root}")
    if not target_root.exists():
        raise SystemExit(f"Plugin skills directory not found: {target_root}")

    missing = [
        skill
        for skill in PM_METHOD_SKILLS
        if not (source_root / skill / "SKILL.md").exists()
    ]
    if missing:
        joined = ", ".join(missing)
        raise SystemExit(f"Missing source skills: {joined}")

    for skill in PM_METHOD_SKILLS:
        source = source_root / skill
        target = target_root / skill
        if args.dry_run:
            print(f"Would sync {source} -> {target}")
            continue
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(source, target, ignore=ignore_names)
        apply_local_overlay(target / "SKILL.md")
        print(f"Synced {skill}")

    print(f"Completed {len(PM_METHOD_SKILLS)} PM method skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
