#!/usr/bin/env bash

set -euo pipefail

BRANCH="${1:-cn}"
TARGET_DIR="${2:-/data/homebrew-cn-deploy}"
COMMIT_MESSAGE="${3:-Sync deploy snapshot from ${BRANCH}}"

REPO_ROOT="$(git rev-parse --show-toplevel)"
ABS_TARGET_DIR="$(cd "$(dirname "${TARGET_DIR}")" && pwd)/$(basename "${TARGET_DIR}")"

if ! git -C "${REPO_ROOT}" rev-parse --verify "${BRANCH}" >/dev/null 2>&1; then
	echo "Branch not found: ${BRANCH}" >&2
	exit 1
fi

mkdir -p "${ABS_TARGET_DIR}"

if [ ! -d "${ABS_TARGET_DIR}/.git" ]; then
	git -C "${ABS_TARGET_DIR}" init >/dev/null
fi

git -C "${ABS_TARGET_DIR}" checkout -b main >/dev/null 2>&1 || git -C "${ABS_TARGET_DIR}" checkout main >/dev/null 2>&1

# Replace the working tree with the latest snapshot while preserving .git and any configured remotes.
find "${ABS_TARGET_DIR}" -mindepth 1 -maxdepth 1 ! -name '.git' -exec rm -rf {} +
git -C "${REPO_ROOT}" archive "${BRANCH}" | tar -x -C "${ABS_TARGET_DIR}"

git -C "${ABS_TARGET_DIR}" add -A

if git -C "${ABS_TARGET_DIR}" diff --cached --quiet; then
	echo "No changes to commit in ${ABS_TARGET_DIR}"
	exit 0
fi

git -C "${ABS_TARGET_DIR}" commit -m "${COMMIT_MESSAGE}" >/dev/null

cat <<EOF
Deploy repository synced:
  branch source: ${BRANCH}
  target path:   ${ABS_TARGET_DIR}
  commit:        ${COMMIT_MESSAGE}

Next step:
  cd ${ABS_TARGET_DIR} && git push origin main
EOF
