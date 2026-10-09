#!/usr/bin/env bash
# Build the environment papers are converted in. The nightly and CI both run
# this script, so CI proves the exact environment, from the same lock, before
# a nightly run depends on it. Extra arguments go to `uv sync`.
set -euo pipefail

# torch is a large download; a slow mirror must not time it out.
export UV_HTTP_TIMEOUT=300
# The convert extra holds docling and pandoc, pinned by uv.lock.
uv sync --locked --extra convert "$@"

# Fetch docling's models now, so a failed download stops the job here instead
# of failing a paper in the middle of a run.
uv run docling-tools models download layout tableformer rapidocr
echo "DOCLING_ARTIFACTS_PATH=$HOME/.cache/docling/models" >> "$GITHUB_ENV"

npm install --global prettier@3.6.2

mkdir -p "$HOME/.local/bin"
ln -sf "$(uv run python -c 'import pypandoc; print(pypandoc.get_pandoc_path())')" \
  "$HOME/.local/bin/pandoc"
echo "$HOME/.local/bin" >> "$GITHUB_PATH"
