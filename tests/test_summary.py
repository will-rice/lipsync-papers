from pathlib import Path

from papers_pipeline.summary import RunSummary, SourceCounts, write_actions_summary


def test_summary_contains_required_counts_timings_and_events() -> None:
    summary = RunSummary(
        sources=(
            SourceCounts(
                source="arxiv",
                fetched=4,
                accepted=2,
                deduplicated=1,
                rejected=2,
                capped=True,
                complete=False,
            ),
        ),
        inventory=3,
        generated=1,
        pending=2,
        attempted=2,
        succeeded=1,
        failed=1,
        promoted_to_fixme=1,
        timings={"fetch": 0.125},
        events=["arxiv: cap reached; continuation persisted", "deadline exhausted"],
        fixme_paths=["papers/broken.fixme.txt"],
    )

    markdown = summary.to_markdown()

    for heading in (
        "Sources",
        "Inventory and conversion",
        "Timings",
        "Continuation and failures",
    ):
        assert f"## {heading}" in markdown
    assert "| arxiv | 4 | 2 | 1 | 2 | True | False |" in markdown
    assert "- promoted_to_fixme: 1" in markdown
    assert "deadline exhausted" in markdown
    assert "papers/broken.fixme.txt" in markdown


def test_actions_summary_appends_without_replacing_previous_steps(
    tmp_path: Path,
) -> None:
    path = tmp_path / "summary.md"
    path.write_text("previous step\n", encoding="utf-8")

    write_actions_summary(path, RunSummary(events=["continued"]))
    write_actions_summary(None, RunSummary())

    assert path.read_text(encoding="utf-8").startswith("previous step\n")
    assert path.read_text(encoding="utf-8").count("# Papers pipeline summary") == 1
