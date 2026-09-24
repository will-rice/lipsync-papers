import re
import shutil
import stat
import subprocess
from pathlib import Path
from typing import Any

import pytest
import yaml


class WorkflowLoader(yaml.SafeLoader):
    """Load workflow YAML without treating the key `on` as a boolean."""


WorkflowLoader.yaml_implicit_resolvers = {
    key: list(resolvers)
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}
for first_character in "OoYyNn":
    WorkflowLoader.yaml_implicit_resolvers[first_character] = [
        resolver
        for resolver in WorkflowLoader.yaml_implicit_resolvers.get(first_character, [])
        if resolver[0] != "tag:yaml.org,2002:bool"
    ]

WORKFLOWS = Path(".github/workflows")
SCRIPTS = Path(".github/scripts")
PINNED_ACTION = re.compile(r"^[^@\s]+@[0-9a-f]{40}$")
DIRTY_PATHS = (
    "papers",
    "papers.csv",
    ".papers-state.yml",
    "README.md",
    "src/unrelated.py",
)


def workflow(name: str) -> dict[str, Any]:
    loaded = yaml.load(
        (WORKFLOWS / name).read_text(encoding="utf-8"),
        Loader=WorkflowLoader,
    )
    assert isinstance(loaded, dict)
    return loaded


def test_actions_are_sha_pinned_and_jobs_and_steps_have_timeouts() -> None:
    paths = sorted(WORKFLOWS.glob("*.yml"))
    assert {path.name for path in paths} == {
        "alphaxiv.yml",
        "ci.yml",
        "format-corpus.yml",
        "nightly.yml",
        "template-update.yml",
    }
    for path in paths:
        data = workflow(path.name)
        for job in data["jobs"].values():
            assert isinstance(job.get("timeout-minutes"), int)
            for step in job["steps"]:
                assert isinstance(step.get("timeout-minutes"), int)
                if "uses" in step:
                    assert PINNED_ACTION.fullmatch(step["uses"])


def test_ci_triggers_and_permissions_are_read_only() -> None:
    data = workflow("ci.yml")
    assert data["on"] == {
        "pull_request": None,
        "push": {"branches": ["main"]},
    }
    assert data["permissions"] == {"contents": "read"}


def test_all_python_workflows_use_locked_dependencies() -> None:
    for name in ("ci.yml", "nightly.yml", "format-corpus.yml"):
        text = (WORKFLOWS / name).read_text(encoding="utf-8")
        assert "uv==" in text
        assert "uv sync --locked" in text


def test_nightly_provisions_pinned_conversion_and_formatting_tools() -> None:
    text = (WORKFLOWS / "nightly.yml").read_text(encoding="utf-8")
    assert "marker-pdf==1.10.1" in text
    assert "pypandoc-binary==1.15" in text
    assert "prettier@3.6.2" in text
    assert "pypandoc.get_pandoc_path()" in text
    assert '"$HOME/.local/bin" >> "$GITHUB_PATH"' in text
    assert text.index("marker-pdf==1.10.1") < text.index("nightly.sh")


def test_nightly_has_non_overlapping_mutation_concurrency() -> None:
    data = workflow("nightly.yml")
    assert set(data["on"]) == {"schedule", "workflow_dispatch"}
    assert data["concurrency"] == {
        "group": "nightly-papers",
        "cancel-in-progress": False,
    }
    assert data["permissions"] == {"actions": "write", "contents": "write"}
    run_step, continue_step = data["jobs"]["update"]["steps"][-2:]
    assert run_step["id"] == "run"
    assert run_step["env"] == {
        "SEMANTIC_SCHOLAR_API_KEY": "${{ secrets.SEMANTIC_SCHOLAR_API_KEY }}"
    }
    assert continue_step["if"] == "steps.run.outputs.more_work == 'true'"
    assert (
        continue_step["run"] == 'gh workflow run nightly.yml --ref "$GITHUB_REF_NAME"'
    )
    assert continue_step["env"] == {"GH_TOKEN": "${{ github.token }}"}


def test_nightly_never_runs_a_complete_corpus_glob() -> None:
    text = (WORKFLOWS / "nightly.yml").read_text(encoding="utf-8")
    assert "format-corpus" not in text
    assert "papers/*.md" not in text
    assert "papers/**/*.md" not in text


def test_alphaxiv_sync_is_read_only_and_configured() -> None:
    data = workflow("alphaxiv.yml")
    assert data["on"] == {
        "workflow_run": {
            "workflows": ["Nightly papers"],
            "types": ["completed"],
            "branches": ["main"],
        },
        "workflow_dispatch": None,
    }
    assert data["permissions"] == {"contents": "read"}
    assert data["jobs"]["sync"]["if"] == "vars.ALPHAXIV_COLLECTION != ''"

    sync_step = data["jobs"]["sync"]["steps"][-1]
    assert sync_step["run"] == "uv run python -m papers_pipeline.alphaxiv_sync"
    assert sync_step["env"] == {
        "ALPHAXIV_API_KEY": "${{ secrets.ALPHAXIV_API_KEY }}",
        "ALPHAXIV_COLLECTION": "${{ vars.ALPHAXIV_COLLECTION }}",
    }


def test_format_corpus_is_manual_only_and_opens_a_pr() -> None:
    data = workflow("format-corpus.yml")
    assert set(data["on"]) == {"workflow_dispatch"}
    assert data["permissions"] == {"contents": "read"}
    assert "permissions" not in data["jobs"]["plan"]
    assert "permissions" not in data["jobs"]["format"]
    assert data["jobs"]["combine"]["permissions"] == {
        "contents": "write",
        "pull-requests": "write",
    }
    assert data["concurrency"]["cancel-in-progress"] is False
    text = (WORKFLOWS / "format-corpus.yml").read_text(encoding="utf-8")
    assert "git push" not in text
    assert "peter-evans/create-pull-request@" in text
    assert "base: ${{ needs.plan.outputs.base_branch }}" in text


def test_feature_branch_dispatch_cannot_contaminate_formatting_pr() -> None:
    data = workflow("format-corpus.yml")
    text = (WORKFLOWS / "format-corpus.yml").read_text(encoding="utf-8")
    assert "github.sha" not in text
    assert "github.ref" not in text
    jobs = data["jobs"]
    plan = jobs["plan"]
    plan_checkout = plan["steps"][0]
    assert plan_checkout["with"]["ref"] == (
        "${{ github.event.repository.default_branch }}"
    )
    assert plan["outputs"] == {
        "base_branch": "${{ github.event.repository.default_branch }}",
        "base_sha": "${{ steps.base.outputs.sha }}",
        "matrix": "${{ steps.matrix.outputs.matrix }}",
    }
    assert jobs["format"]["needs"] == "plan"
    assert set(jobs["combine"]["needs"]) == {"plan", "format"}
    for job_name in ("format", "combine"):
        checkout = jobs[job_name]["steps"][0]
        assert checkout["with"]["ref"] == "${{ needs.plan.outputs.base_sha }}"


def test_format_corpus_limits_and_builds_deterministic_shards() -> None:
    data = workflow("format-corpus.yml")
    plan = data["jobs"]["plan"]
    matrix_script = next(
        step["run"] for step in plan["steps"] if step.get("id") == "matrix"
    )
    assert data["on"]["workflow_dispatch"]["inputs"]["shard_count"]["options"] == [
        "1",
        "2",
        "4",
        "8",
        "16",
        "32",
    ]
    assert "range($count)" in matrix_script
    assert data["jobs"]["format"]["strategy"]["fail-fast"] is False


def test_format_corpus_combines_binary_patches_in_numeric_order() -> None:
    text = (WORKFLOWS / "format-corpus.yml").read_text(encoding="utf-8")
    assert "git diff --binary" in text
    assert "sort -zV" in text
    assert '[[ -s "$patch" ]]' in text
    assert "git apply --index" in text


def _git(cwd: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=cwd,
        check=True,
        capture_output=True,
        text=True,
    )


def _nightly_scenario(
    tmp_path: Path,
    *,
    dirty_path: str | None,
    concurrent_push: bool = False,
) -> tuple[int, int]:
    origin = tmp_path / "origin.git"
    work = tmp_path / "work"
    fake_bin = tmp_path / "bin"
    origin.mkdir()
    _git(origin, "init", "--bare", "-q")
    work.mkdir()
    _git(work, "init", "-q", "-b", "main")
    _git(work, "config", "user.name", "Test")
    _git(work, "config", "user.email", "test@example.test")
    (work / "papers.csv").write_text("initial\n", encoding="utf-8")
    (work / ".gitignore").write_text(".cache/\n", encoding="utf-8")
    _git(work, "add", "papers.csv", ".gitignore")
    _git(work, "commit", "-q", "-m", "initial")
    _git(work, "remote", "add", "origin", str(origin))
    _git(work, "push", "-q", "-u", "origin", "main")

    concurrent_command = ""
    if concurrent_push:
        other = tmp_path / "other"
        _git(tmp_path, "clone", "-q", "-b", "main", str(origin), str(other))
        _git(other, "config", "user.name", "Other")
        _git(other, "config", "user.email", "other@example.test")
        concurrent_command = (
            f'printf "merged\\n" > "{other}/code.txt"\n'
            f'git -C "{other}" add code.txt\n'
            f'git -C "{other}" commit -q -m "concurrent merge"\n'
            f'git -C "{other}" push -q origin main\n'
        )

    fake_bin.mkdir()
    uv = fake_bin / "uv"
    dirty_command = ""
    if dirty_path is not None:
        target = (
            f"{dirty_path}/leftover"
            if dirty_path in {"papers", ".cache"}
            else dirty_path
        )
        (work / target).parent.mkdir(parents=True, exist_ok=True)
        dirty_command = f'printf "inconsistent\\n" >> "{target}"\n'
    uv.write_text(
        "#!/usr/bin/env bash\n"
        "set -eu\n"
        'printf "committed\\n" >> papers.csv\n'
        "git add papers.csv\n"
        'git commit -q -m "pipeline batch"\n'
        f"{concurrent_command}"
        f"{dirty_command}"
        "exit 23\n",
        encoding="utf-8",
    )
    uv.chmod(uv.stat().st_mode | stat.S_IXUSR)
    script = SCRIPTS / "nightly.sh"
    git_executable = shutil.which("git")
    bash_executable = shutil.which("bash")
    assert git_executable is not None and bash_executable is not None
    completed = subprocess.run(
        [str(script.resolve())],
        cwd=work,
        env={
            "PATH": (
                f"{fake_bin}:{Path(git_executable).parent}:"
                f"{Path(bash_executable).parent}"
            )
        },
        check=False,
    )
    remote_count = int(
        _git(
            tmp_path,
            f"--git-dir={origin}",
            "rev-list",
            "--count",
            "refs/heads/main",
        ).stdout.strip()
    )
    return completed.returncode, remote_count


@pytest.mark.parametrize("dirty_path", DIRTY_PATHS)
def test_nightly_rejects_any_dirty_path_after_failure(
    tmp_path: Path,
    dirty_path: str,
) -> None:
    status, remote_count = _nightly_scenario(tmp_path, dirty_path=dirty_path)
    assert status != 0
    assert remote_count == 1


@pytest.mark.parametrize("dirty_path", [None, ".cache/http/response"])
def test_nightly_pushes_consistent_commits_with_clean_or_ignored_cache(
    tmp_path: Path,
    dirty_path: str | None,
) -> None:
    status, remote_count = _nightly_scenario(tmp_path, dirty_path=dirty_path)
    assert status != 0
    assert remote_count == 2


def test_nightly_script_is_executable() -> None:
    script = SCRIPTS / "nightly.sh"
    assert script.stat().st_mode & stat.S_IXUSR


def test_template_update_opens_pr_and_never_pushes_main() -> None:
    data = workflow("template-update.yml")
    assert data["permissions"] == {"contents": "read"}
    assert set(data["on"]) == {"schedule", "workflow_dispatch"}
    assert data["concurrency"] == {
        "group": "template-update",
        "cancel-in-progress": False,
    }
    assert set(data["jobs"]) == {"validate", "publish"}
    commands = "\n".join(
        step.get("run", "") for job in data["jobs"].values() for step in job["steps"]
    )
    assert 'gh api "repos/$TEMPLATE_REPOSITORY/releases/latest"' in commands
    assert ".github/scripts/template-update.sh" in commands
    assert "git push" not in commands
    assert any(
        "peter-evans/create-pull-request@" in step.get("uses", "")
        for step in data["jobs"]["publish"]["steps"]
    )
    update_step = next(
        step for step in data["jobs"]["validate"]["steps"] if step.get("id") == "update"
    )
    assert update_step["run"] == ".github/scripts/template-update.sh"
    publish = data["jobs"]["publish"]
    assert publish["needs"] == "validate"
    assert publish["if"] == "needs.validate.outputs.updated == 'true'"


def test_pr_workflows_remove_downloaded_patches_and_constrain_staging() -> None:
    template_update = workflow("template-update.yml")["jobs"]["publish"]["steps"]
    update_pr = template_update[-1]
    assert "rm -f template-update.patch" in template_update[-2]["run"]
    assert "template-update.patch" not in update_pr["with"]["add-paths"]
    assert "src/**" in update_pr["with"]["add-paths"]
    assert "tests/**" in update_pr["with"]["add-paths"]

    formatting = workflow("format-corpus.yml")["jobs"]["combine"]["steps"]
    format_pr = formatting[-1]
    assert "rm -rf patches" in formatting[-2]["run"]
    assert format_pr["with"]["add-paths"] == "papers/**"


def test_template_update_withholds_write_credentials_until_pr_step() -> None:
    data = workflow("template-update.yml")
    assert data["permissions"] == {"contents": "read"}
    assert set(data["jobs"]) == {"validate", "publish"}

    validate = data["jobs"]["validate"]
    assert "permissions" not in validate
    release_step = next(
        step for step in validate["steps"] if step.get("id") == "release"
    )
    assert release_step["env"]["GH_TOKEN"] == "${{ github.token }}"
    assert all(
        "GH_TOKEN" not in step.get("env", {})
        for step in validate["steps"]
        if step is not release_step
    )

    publish = data["jobs"]["publish"]
    assert publish["permissions"] == {
        "contents": "write",
        "pull-requests": "write",
    }
    pull_request_step = publish["steps"][-1]
    assert pull_request_step["with"]["token"] == "${{ github.token }}"
    assert all(
        "GH_TOKEN" not in step.get("env", {}) and "token" not in step.get("with", {})
        for step in publish["steps"][:-1]
    )

    checkout_steps = [
        step
        for job in data["jobs"].values()
        for step in job["steps"]
        if step.get("uses", "").startswith("actions/checkout@")
    ]
    assert checkout_steps
    assert all(step["with"]["persist-credentials"] is False for step in checkout_steps)
    assert validate["steps"][0]["with"]["fetch-depth"] == 0
    assert validate["steps"][0]["with"]["ref"] == (
        "${{ github.event.repository.default_branch }}"
    )


def test_template_update_validates_release_and_handles_noop_and_conflicts() -> None:
    script = SCRIPTS / "template-update.sh"
    text = script.read_text(encoding="utf-8")
    assert script.stat().st_mode & stat.S_IXUSR
    assert "immutable release tag" in text
    assert ".copier-answers.yml" in text
    assert "_commit:" in text
    assert "already uses template release" in text
    assert "updated=false" in text
    assert "updated=true" in text
    assert "newer than current release" in text
    assert "Copier update left conflicts" in text
    assert "uv run copier update" in text
    assert '--vcs-ref "$template_ref"' in text
    assert "--answers-file .copier-answers.yml" in text
    assert "uv lock" in text
    # Dev tools must be provisioned online before validation goes offline.
    assert (
        text.index("uv lock")
        < text.index("uv sync --locked --extra dev")
        < text.index("export UV_OFFLINE=1")
        < text.index("pre-commit run --all-files")
    )
    assert "papers-pipeline validate --config papers.yml" in text
    assert "pre-commit run --all-files" in text
    assert "pytest" in text
    assert "git diff --check" in text


@pytest.mark.parametrize(
    "template_ref",
    ["", "main", "HEAD", "v1", "v1.2", "refs/heads/main", "v1.2.3;echo bad"],
)
def test_template_update_rejects_non_release_refs(
    tmp_path: Path,
    template_ref: str,
) -> None:
    script = (SCRIPTS / "template-update.sh").resolve()
    answers = tmp_path / ".copier-answers.yml"
    answers.write_text("_commit: v1.2.3\n", encoding="utf-8")
    completed = subprocess.run(
        [str(script)],
        cwd=tmp_path,
        env={"PATH": "/usr/bin:/bin", "TEMPLATE_REF": template_ref},
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode != 0
    assert "TEMPLATE_REF must be an immutable release tag" in completed.stderr


@pytest.mark.parametrize("template_ref", ["v1.2.3", "1.2.3"])
def test_template_update_is_noop_when_release_is_current(
    tmp_path: Path,
    template_ref: str,
) -> None:
    script = (SCRIPTS / "template-update.sh").resolve()
    (tmp_path / ".copier-answers.yml").write_text(
        "_commit: v1.2.3\n",
        encoding="utf-8",
    )
    completed = subprocess.run(
        [str(script)],
        cwd=tmp_path,
        env={"PATH": "/usr/bin:/bin", "TEMPLATE_REF": template_ref},
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 0
    assert "already uses template release" in completed.stdout


def test_nightly_rebases_onto_concurrent_main_updates(tmp_path: Path) -> None:
    status, remote_count = _nightly_scenario(
        tmp_path, dirty_path=None, concurrent_push=True
    )
    assert status == 23
    assert remote_count == 3
