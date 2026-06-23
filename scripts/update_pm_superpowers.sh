#!/usr/bin/env bash
set -euo pipefail

REPO="${PM_SUPERPOWERS_REPO:-linbiqiu/pm-superpowers}"
REF="${PM_SUPERPOWERS_REF:-main}"
PLUGIN="${PM_SUPERPOWERS_PLUGIN:-pm-superpowers}"
MARKETPLACE="${PM_SUPERPOWERS_MARKETPLACE:-pm-superpowers-internal}"

echo "准备更新 ${PLUGIN}@${MARKETPLACE}"
echo "来源：${REPO}@${REF}"
echo

if codex plugin marketplace list >/tmp/pm-superpowers-marketplaces.txt 2>/tmp/pm-superpowers-marketplaces.err; then
  if ! awk '{print $1}' /tmp/pm-superpowers-marketplaces.txt | grep -qx "${MARKETPLACE}"; then
    echo "未发现 marketplace：${MARKETPLACE}"
    echo "正在添加 marketplace..."
    codex plugin marketplace add "${REPO}" --ref "${REF}"
  else
    echo "已发现 marketplace：${MARKETPLACE}"
  fi
else
  echo "无法读取 marketplace 列表，尝试添加 marketplace。"
  cat /tmp/pm-superpowers-marketplaces.err >&2 || true
  codex plugin marketplace add "${REPO}" --ref "${REF}"
fi

echo
echo "刷新 marketplace 快照..."
upgrade_output="$(codex plugin marketplace upgrade "${MARKETPLACE}" 2>&1 || true)"
if [[ -n "${upgrade_output}" ]]; then
  if grep -q "not configured as a Git marketplace" <<<"${upgrade_output}"; then
    echo "当前 marketplace 不是 Git marketplace，跳过快照刷新。"
  else
    echo "${upgrade_output}"
  fi
fi

echo
echo "重新安装插件..."
codex plugin add "${PLUGIN}@${MARKETPLACE}"

echo
"$(dirname "$0")/check_pm_superpowers_update.sh" || true

echo
echo "更新完成。请新开一个 Codex thread 使用新版插件。"
