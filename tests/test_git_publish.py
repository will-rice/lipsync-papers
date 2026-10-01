import subprocess
from pathlib import Path

import pytest

from papers_pipeline.git import GitRepository


def git(cwd: Path, *args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=cwd, check=True, capture_output=True, text=True
    ).stdout.strip()


def clone(origin: Path, target: Path) -> Path:
    git(origin.parent, "clone", "-q", "-b", "main", str(origin), str(target))
    git(target, "config", "user.name", "Test")
    git(target, "config", "user.email", "test@example.test")
    return target


def commit(repository: Path, name: str, content: str) -> str:
    (repository / name).write_text(content, encoding="utf-8")
    git(repository, "add", name)
    git(repository, "commit", "-q", "-m", f"change {name}")
    return git(repository, "rev-parse", "HEAD")


@pytest.fixture
def origin(tmp_path: Path) -> Path:
    origin = tmp_path / "origin.git"
    origin.mkdir()
    git(origin, "init", "--bare", "-q", "-b", "main")
    seed = tmp_path / "seed"
    seed.mkdir()
    git(seed, "init", "-q", "-b", "main")
    git(seed, "config", "user.name", "Test")
    git(seed, "config", "user.email", "test@example.test")
    commit(seed, "papers.csv", "initial\n")
    git(seed, "push", "-q", str(origin), "main")
    return origin


def test_publish_pushes_commits_on_top_of_remote_changes(
    origin: Path, tmp_path: Path
) -> None:
    work = clone(origin, tmp_path / "work")
    other = clone(origin, tmp_path / "other")
    merged = commit(other, "code.txt", "merged\n")
    git(other, "push", "-q", "origin", "main")
    commit(work, "papers.csv", "initial\nbatch\n")

    assert GitRepository(work).publish()

    published = git(origin, "rev-list", "refs/heads/main").splitlines()
    assert published[0] == git(work, "rev-parse", "HEAD")
    assert merged in published


def test_publish_reports_an_unavailable_remote_and_keeps_commits(
    origin: Path, tmp_path: Path
) -> None:
    work = clone(origin, tmp_path / "work")
    batch = commit(work, "papers.csv", "initial\nbatch\n")
    git(work, "remote", "set-url", "origin", str(tmp_path / "missing.git"))

    assert not GitRepository(work).publish()

    assert git(work, "rev-parse", "HEAD") == batch


def test_publish_aborts_a_conflicting_rebase(origin: Path, tmp_path: Path) -> None:
    work = clone(origin, tmp_path / "work")
    other = clone(origin, tmp_path / "other")
    commit(other, "papers.csv", "initial\ntheirs\n")
    git(other, "push", "-q", "origin", "main")
    batch = commit(work, "papers.csv", "initial\nours\n")

    assert not GitRepository(work).publish()

    # Later batches can still be committed: no rebase is left in progress.
    assert git(work, "rev-parse", "HEAD") == batch
    assert git(work, "status", "--porcelain=v1") == ""
    assert not (work / ".git" / "rebase-merge").exists()
