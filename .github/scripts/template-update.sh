#!/usr/bin/env bash
set -euo pipefail

template_ref="${TEMPLATE_REF-}"
release_pattern='^v?[0-9]+\.[0-9]+\.[0-9]+$'
if [[ ! "$template_ref" =~ $release_pattern ]]; then
  echo "TEMPLATE_REF must be an immutable release tag (for example, v1.2.3)" >&2
  exit 2
fi

answers_file=".copier-answers.yml"
if [[ ! -f "$answers_file" ]]; then
  echo "Required Copier answers file is missing: $answers_file" >&2
  exit 2
fi

current_ref="$(
  awk '$1 == "_commit:" { value=$2; gsub(/^["'\''"]|["'\''"]$/, "", value); print value; exit }' \
    "$answers_file"
)"
if [[ -z "$current_ref" || ! "$current_ref" =~ $release_pattern ]]; then
  echo "$answers_file must contain an immutable release tag in _commit" >&2
  exit 2
fi

current_version="${current_ref#v}"
target_version="${template_ref#v}"
if [[ "$current_version" == "$target_version" ]]; then
  echo "Repository already uses template release $template_ref; nothing to update."
  if [[ -n "${GITHUB_OUTPUT-}" ]]; then
    echo "updated=false" >> "$GITHUB_OUTPUT"
  fi
  exit 0
fi

newest_version="$(printf '%s\n%s\n' "$current_version" "$target_version" | sort -V | tail -n 1)"
if [[ "$newest_version" != "$target_version" ]]; then
  echo "TEMPLATE_REF $template_ref must be newer than current release $current_ref" >&2
  exit 2
fi

uv run copier update \
  --answers-file .copier-answers.yml \
  --vcs-ref "$template_ref" \
  --defaults \
  --trust \
  --conflict rej

if find . -type f -name '*.rej' -print -quit | grep -q .; then
  echo "Copier update left conflicts (.rej files); refusing to continue" >&2
  exit 1
fi
git diff --check

uv lock
# Provision dev tools online; validation below must not touch the network.
uv sync --locked --extra dev
export UV_OFFLINE=1
uv run papers-pipeline validate --config papers.yml --config-only
uv run pre-commit run --all-files
uv run pytest
if [[ -n "${GITHUB_OUTPUT-}" ]]; then
  echo "updated=true" >> "$GITHUB_OUTPUT"
fi
