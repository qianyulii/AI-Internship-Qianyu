#!/usr/bin/env bash
set -euo pipefail
PROJECT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_DIR"
if [[ ! -x .venv/bin/jupyter ]]; then
  echo "Project environment is missing. Run: uv sync --locked" >&2
  exit 1
fi
exec .venv/bin/jupyter lab --ip=127.0.0.1 --ServerApp.root_dir="$PROJECT_DIR" "$@"
