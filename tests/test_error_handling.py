"""Tests for per-paper error isolation and 3-strike escalation."""

from __future__ import annotations

import json
from pathlib import Path

from scripts.convert_papers import (
    log_conversion_error,
    record_failure_and_maybe_escalate,
)


def test_log_conversion_error_appends_jsonl(tmp_path: Path) -> None:
    log_path = tmp_path / "conversion_errors.jsonl"
    log_conversion_error(log_path, "2008.10010", "stage1", "boom")
    log_conversion_error(log_path, "2008.10010", "stage2", "kaboom")
    lines = log_path.read_text().splitlines()
    assert len(lines) == 2
    record = json.loads(lines[0])
    assert record["arxiv_id"] == "2008.10010"
    assert record["stage"] == "stage1"


def test_record_failure_escalates_after_three(tmp_path: Path) -> None:
    log_path = tmp_path / "conversion_errors.jsonl"
    fixme_path = tmp_path / "fixme.txt"
    for _ in range(3):
        record_failure_and_maybe_escalate(log_path, fixme_path, "2008.10010", "stage1", "boom")
    fixme = fixme_path.read_text().strip().splitlines()
    assert "2008.10010" in fixme


def test_record_failure_does_not_escalate_after_two(tmp_path: Path) -> None:
    log_path = tmp_path / "conversion_errors.jsonl"
    fixme_path = tmp_path / "fixme.txt"
    for _ in range(2):
        record_failure_and_maybe_escalate(log_path, fixme_path, "2008.10010", "stage1", "boom")
    assert not fixme_path.exists()
