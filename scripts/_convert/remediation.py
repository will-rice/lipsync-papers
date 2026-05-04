"""LLM-driven remediation pass for low-quality conversions."""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path

# Heuristic thresholds
MIN_WORDS_PER_PAGE_RATIO = 0.5
MIN_WORDS_PER_PAGE = 200
LOW_CITATION_RESOLUTION_THRESHOLD = 0.30


@dataclass
class RemediationFlags:
    """Result of the heuristic flagger."""

    flagged: bool
    reasons: list[str] = field(default_factory=list)


def should_remediate(
    body: str,
    page_count: int,
    has_references: bool,
    citations_resolved_ratio: float,
    latex_exit_code: int,
) -> RemediationFlags:
    """Score a paper against the auto-flag heuristics from the spec."""
    reasons: list[str] = []
    word_count = len(body.split())
    expected_min_words = MIN_WORDS_PER_PAGE_RATIO * page_count * MIN_WORDS_PER_PAGE
    if word_count < expected_min_words:
        reasons.append("short_body")
    if not has_references:
        reasons.append("no_references")
    if citations_resolved_ratio < LOW_CITATION_RESOLUTION_THRESHOLD:
        reasons.append("low_citation_resolution")
    if latex_exit_code != 0:
        reasons.append("latex_build_failed")
    return RemediationFlags(flagged=bool(reasons), reasons=reasons)


def load_fixme_list(path: Path) -> set[str]:
    """Load the manual remediation list (one arxiv_id per line)."""
    if not path.exists():
        return set()
    return {
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    }


def append_to_fixme(path: Path, arxiv_id: str) -> None:
    """Append *arxiv_id* to the manual remediation list (no-op if already present)."""
    existing = load_fixme_list(path)
    if arxiv_id in existing:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(f"{arxiv_id}\n")
    logging.info("Auto-appended %s to %s", arxiv_id, path)
