#!/usr/bin/env bash

set -euo pipefail

BRANCH="${1:-cn}"
OUTPUT_DIR="${2:-../homebrew-cn-deploy}"
COMMIT_MESSAGE="${3:-Deploy snapshot from ${BRANCH}}"

REPO_ROOT="$(git rev-parse --show-toplevel)"
ABS_OUTPUT_DIR="$(cd "$(dirname "${OUTPUT_DIR}")" && pwd)/$(basename "${OUTPUT_DIR}")"

if ! git -C "${REPO_ROOT}" rev-parse --verify "${BRANCH}" >/dev/null 2>&1; then
	echo "Branch not found: ${BRANCH}" >&2
	exit 1
fi

if [ -e "${ABS_OUTPUT_DIR}" ] && [ -n "$(find "${ABS_OUTPUT_DIR}" -mindepth 1 -maxdepth 1 -print -quit 2>/dev/null)" ]; then
	echo "Output directory is not empty: ${ABS_OUTPUT_DIR}" >&2
	exit 1
fi

mkdir -p "${ABS_OUTPUT_DIR}"
git -C "${REPO_ROOT}" archive "${BRANCH}" | tar -x -C "${ABS_OUTPUT_DIR}"

git -C "${ABS_OUTPUT_DIR}" init >/dev/null
git -C "${ABS_OUTPUT_DIR}" checkout -b main >/dev/null 2>&1 || git -C "${ABS_OUTPUT_DIR}" checkout main >/dev/null 2>&1
git -C "${ABS_OUTPUT_DIR}" add -A
git -C "${ABS_OUTPUT_DIR}" commit -m "${COMMIT_MESSAGE}" >/dev/null

cat <<EOF
Deploy snapshot repository created:
  branch source: ${BRANCH}
  output path:   ${ABS_OUTPUT_DIR}

Next steps:
  1. cd ${ABS_OUTPUT_DIR}
  2. git remote add origin <your-deploy-repo-url>
  3. git push -u origin main
  4. Later updates can use: bash /data/homebrew/scripts/sync-deploy-repo.sh
EOF
