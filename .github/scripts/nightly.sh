#!/usr/bin/env bash
set -euo pipefail

git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

pipeline_status=0
# --publish pushes every batch as it is committed, so a run that fails or is
# cut off keeps all but its newest batch.
uv run papers-pipeline nightly --config papers.yml --publish || pipeline_status=$?

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

PUSH_ATTEMPTS=5
PUSH_RETRY_SECONDS=60

push_status=0
# main can advance (e.g. PR merges) during a long run; replay batches on top.
# A push can also fail because GitHub is briefly unavailable, and giving up
# would discard hours of converted batches, so retry before failing.
for ((attempt = 1; attempt <= PUSH_ATTEMPTS; attempt++)); do
  push_status=0
  {
    git fetch --quiet origin main &&
      git rebase --quiet FETCH_HEAD &&
      git push origin HEAD:main
  } || push_status=$?
  if ((push_status == 0 || attempt == PUSH_ATTEMPTS)); then
    break
  fi
  echo "Push attempt $attempt failed; retrying in ${PUSH_RETRY_SECONDS}s" >&2
  sleep "$PUSH_RETRY_SECONDS"
done
if ((pipeline_status != 0)); then
  exit "$pipeline_status"
fi
exit "$push_status"
