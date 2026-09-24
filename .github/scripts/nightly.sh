#!/usr/bin/env bash
set -euo pipefail

git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

pipeline_status=0
uv run papers-pipeline nightly --config papers.yml || pipeline_status=$?

# The pipeline commits everything it writes, so any leftover change means a
# batch stopped midway; never publish that state.
dirty_status="$(git status --porcelain=v1 --untracked-files=all)"
if [[ -n "$dirty_status" ]]; then
  printf '%s\n' \
    "Refusing to push because the worktree has uncommitted changes:" \
    "$dirty_status" >&2
  if ((pipeline_status == 0)); then
    pipeline_status=1
  fi
  exit "$pipeline_status"
fi

push_status=0
# main can advance (e.g. PR merges) during a long run; replay batches on top.
{
  git fetch --quiet origin main &&
    git rebase --quiet FETCH_HEAD &&
    git push origin HEAD:main
} || push_status=$?
if ((pipeline_status != 0)); then
  exit "$pipeline_status"
fi
exit "$push_status"
