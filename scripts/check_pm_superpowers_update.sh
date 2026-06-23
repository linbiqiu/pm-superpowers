#!/usr/bin/env bash
set -euo pipefail

REPO="${PM_SUPERPOWERS_REPO:-linbiqiu/pm-superpowers}"
REF="${PM_SUPERPOWERS_REF:-main}"
PLUGIN="${PM_SUPERPOWERS_PLUGIN:-pm-superpowers}"
MARKETPLACE="${PM_SUPERPOWERS_MARKETPLACE:-pm-superpowers-internal}"

remote_version="$(
  python3 - "$REPO" "$REF" <<'PY'
import base64
import json
import sys
import urllib.request

repo = sys.argv[1]
ref = sys.argv[2]

repo = repo.removeprefix("https://github.com/")
repo = repo.removesuffix(".git")
path = "plugins/pm-superpowers/.codex-plugin/plugin.json"
url = f"https://api.github.com/repos/{repo}/contents/{path}?ref={ref}"

with urllib.request.urlopen(url, timeout=20) as response:
    payload = json.load(response)
content = base64.b64decode(payload["content"])
data = json.loads(content)
print(data["version"])
PY
)"

local_line="$(codex plugin list 2>/dev/null | awk -v selector="${PLUGIN}@${MARKETPLACE}" '$1 == selector {print; exit}')"

if [[ -z "${local_line}" ]]; then
  echo "本地未安装 ${PLUGIN}@${MARKETPLACE}"
  echo "远程最新版本：${remote_version}"
  echo
  echo "安装命令："
  echo "  codex plugin marketplace add ${REPO} --ref ${REF}"
  echo "  codex plugin add ${PLUGIN}@${MARKETPLACE}"
  exit 0
fi

local_version="$(awk '{print $4}' <<<"${local_line}")"
local_base_version="${local_version%%+*}"

echo "本地版本：${local_version}"
echo "远程版本：${remote_version}"

if [[ "${local_base_version}" == "${remote_version}" ]]; then
  echo "状态：已是最新正式版本。"
else
  echo "状态：发现新版本，需要更新。"
  echo
  echo "更新命令："
  echo "  scripts/update_pm_superpowers.sh"
fi
