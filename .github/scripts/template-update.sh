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

# Copier names every file under a skip-if-exists directory on one `git apply`
# command line. With thousands of papers and figures that overflows the
# argument limit after Copier has rendered the new template but before it
# re-applies this repository's own changes, which resets papers.yml and
# topic_plugin.py to the template defaults. Update against a commit without
# the corpus, then restore the corpus and the original commit.
#
# The README section between the papers-index markers is regenerated from
# papers.csv, so it is not a change Copier should merge: its diff against the
# old template conflicts with any template edit near the markers. Update with
# the section the old release rendered, then put the generated one back.
base_commit="$(git rev-parse HEAD)"
git_dir="$(git rev-parse --absolute-git-dir)"
corpus_backup="$git_dir/template-update-corpus"
generated_readme="$git_dir/template-update-readme"
old_render="$git_dir/template-update-old-render"
git show "$base_commit:README.md" > "$generated_readme"

splice_index() {
  awk -v start='<!-- papers-index:start -->' -v end='<!-- papers-index:end -->' '
    NR == FNR {
      if ($0 == start) inside = 1
      else if ($0 == end) inside = 0
      else if (inside) section = section $0 "\n"
      next
    }
    $0 == start { print; printf "%s", section; skipping = 1; next }
    $0 == end { skipping = 0 }
    !skipping { print }
  ' "$1" README.md > README.md.spliced
  mv README.md.spliced README.md
}

restore_corpus() {
  if [[ -d "$corpus_backup" ]]; then
    mv "$corpus_backup" papers
  fi
  splice_index "$generated_readme"
  rm -rf "$old_render" "$generated_readme"
  git reset --quiet --mixed "$base_commit"
}
trap restore_corpus EXIT

src_path="$(
  awk '$1 == "_src_path:" { value=$2; gsub(/^["'\''"]|["'\''"]$/, "", value); print value; exit }' \
    "$answers_file"
)"
uv run copier copy --vcs-ref "$current_ref" --data-file "$answers_file" \
  --defaults --quiet "$src_path" "$old_render"
splice_index "$old_render/README.md"
git add README.md
if [[ -d papers ]]; then
  mv papers "$corpus_backup"
  git rm -r --quiet --cached papers
fi
git -c user.name=template-update -c user.email=template-update@localhost \
  commit --quiet --no-verify --allow-empty \
  -m "temp: update template without the corpus or generated index"

uv run copier update \
  --answers-file .copier-answers.yml \
  --vcs-ref "$template_ref" \
  --defaults \
  --trust \
  --conflict rej

restore_corpus
trap - EXIT

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
