#!/usr/bin/env python3
"""Validate PM Superpowers behavior regression contracts.

This is a static guardrail. It does not replace end-to-end model evaluation, but
it prevents the plugin from silently losing the routing, blocking, handoff,
launch, and PM method skill passthrough contracts documented in references.
"""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
from typing import Any


DIRECT_CONTRACT_NEEDLES = [
    "PM method skills 直通契约",
    "用户明确点名",
    "不强制套完整场景工作流",
    "pm-gate-review",
    "downstream-readiness",
]


DIRECT_CONTRACT_FILES = [
    "references/supporting-pm-skills.md",
    "docs/pm-superpowers/PM_SKILLS_BUNDLING_STRATEGY.md",
    "docs/pm-superpowers/PM_SUPERPOWERS_SKILL_MANUAL.md",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(read_text(path))


def load_method_skills(sync_script: Path) -> list[str]:
    tree = ast.parse(read_text(sync_script), filename=str(sync_script))
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(isinstance(target, ast.Name) and target.id == "PM_METHOD_SKILLS" for target in node.targets):
                value = ast.literal_eval(node.value)
                if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
                    raise ValueError("PM_METHOD_SKILLS must be a list of strings")
                return value
    raise ValueError("PM_METHOD_SKILLS not found in sync script")


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def validate_cases(plugin_root: Path, repo_root: Path, failures: list[str]) -> int:
    cases_path = plugin_root / "references" / "behavior-regression-cases.json"
    payload = load_json(cases_path)
    cases = payload.get("cases", [])
    require(isinstance(cases, list) and cases, "behavior-regression-cases.json must contain non-empty cases", failures)

    seen_ids: set[str] = set()
    checked = 0

    for case in cases:
        checked += 1
        case_id = case.get("id")
        require(isinstance(case_id, str) and case_id, f"case #{checked} is missing id", failures)
        require(case_id not in seen_ids, f"duplicate case id: {case_id}", failures)
        seen_ids.add(case_id)

        for field in ("user_prompt", "expected_behavior"):
            require(isinstance(case.get(field), str) and case[field], f"{case_id}: missing {field}", failures)

        for skill in case.get("acceptable_skills", []):
            require((plugin_root / "skills" / skill / "SKILL.md").exists(), f"{case_id}: acceptable skill missing: {skill}", failures)

        for skill in case.get("forbidden_primary_skills", []):
            require((plugin_root / "skills" / skill / "SKILL.md").exists(), f"{case_id}: forbidden skill missing: {skill}", failures)

        for source in case.get("guardrail_sources", []):
            rel_path = source.get("path")
            require(isinstance(rel_path, str), f"{case_id}: guardrail source missing path", failures)
            if not isinstance(rel_path, str):
                continue
            base = repo_root if rel_path.startswith("docs/") else plugin_root
            path = base / rel_path
            require(path.exists(), f"{case_id}: guardrail source not found: {rel_path}", failures)
            if not path.exists():
                continue
            text = read_text(path)
            for needle in source.get("contains", []):
                require(needle in text, f"{case_id}: {rel_path} missing required text: {needle}", failures)

    return checked


def validate_direct_contract(plugin_root: Path, repo_root: Path, failures: list[str]) -> None:
    for rel_path in DIRECT_CONTRACT_FILES:
        base = repo_root if rel_path.startswith("docs/") else plugin_root
        path = base / rel_path
        require(path.exists(), f"direct contract file missing: {rel_path}", failures)
        if not path.exists():
            continue
        text = read_text(path)
        for needle in DIRECT_CONTRACT_NEEDLES:
            require(needle in text, f"{rel_path} missing direct contract text: {needle}", failures)


def validate_method_skill_overlays(plugin_root: Path, failures: list[str]) -> int:
    method_skills = load_method_skills(plugin_root / "scripts" / "sync_pm_skills.py")
    require(len(method_skills) == 68, f"expected 68 PM method skills, found {len(method_skills)}", failures)

    for skill in method_skills:
        skill_md = plugin_root / "skills" / skill / "SKILL.md"
        require(skill_md.exists(), f"method skill missing: {skill}", failures)
        if not skill_md.exists():
            continue
        text = read_text(skill_md)
        require("PM_SUPERPOWERS_LOCAL_OVERLAY_START" in text, f"{skill}: missing local overlay start", failures)
        require("PM_SUPERPOWERS_LOCAL_OVERLAY_END" in text, f"{skill}: missing local overlay end", failures)
        require("../../references/chinese-output-standard.md" in text, f"{skill}: missing Chinese output reference", failures)
        require("pm-gate-review" not in text, f"{skill}: method skill should not embed pm-gate-review", failures)
        require("downstream-readiness" not in text, f"{skill}: method skill should not embed downstream-readiness", failures)

    return len(method_skills)


def parse_args() -> argparse.Namespace:
    script_path = Path(__file__).resolve()
    default_plugin_root = script_path.parents[1]
    default_repo_root = default_plugin_root.parents[1]

    parser = argparse.ArgumentParser(description="Validate PM Superpowers behavior regression contracts.")
    parser.add_argument("--plugin-root", type=Path, default=default_plugin_root)
    parser.add_argument("--repo-root", type=Path, default=default_repo_root)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    plugin_root = args.plugin_root.expanduser().resolve()
    repo_root = args.repo_root.expanduser().resolve()
    failures: list[str] = []

    checked_cases = validate_cases(plugin_root, repo_root, failures)
    validate_direct_contract(plugin_root, repo_root, failures)
    checked_method_skills = validate_method_skill_overlays(plugin_root, failures)

    if failures:
        print("Behavior regression validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"Behavior regression validation passed: {checked_cases} cases, {checked_method_skills} method skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
