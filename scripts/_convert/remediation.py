"""LLM-driven remediation pass for low-quality conversions."""
from __future__ import annotations

import base64
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Protocol

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


CLAUDE_MODEL = "claude-sonnet-4-6"
MAX_OUTPUT_TOKENS = 16000

REMEDIATION_SYSTEM_PROMPT = """You are given (1) a PDF of an academic paper and (2) a markdown rendering produced by automated tools that may have errors. Output a corrected markdown that preserves the section/equation/citation structure of the PDF, keeps citation markers like [1] or \\cite{Smith2020} intact, and uses LaTeX $...$ for math. Do not add references that aren't in the PDF. Output only the corrected markdown — no preamble, no explanation."""


class _AnthropicLike(Protocol):
    """Duck-typed Anthropic client interface, narrow enough for our use."""

    @property
    def messages(self): ...


def remediate_with_pdf(
    pdf_path: Path,
    mangled_body: str,
    client: _AnthropicLike,
) -> str:
    """Call Claude with the PDF + mangled markdown, return the corrected markdown."""
    pdf_b64 = base64.standard_b64encode(pdf_path.read_bytes()).decode("ascii")
    response = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=MAX_OUTPUT_TOKENS,
        system=[
            {
                "type": "text",
                "text": REMEDIATION_SYSTEM_PROMPT,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "document",
                        "source": {
                            "type": "base64",
                            "media_type": "application/pdf",
                            "data": pdf_b64,
                        },
                    },
                    {
                        "type": "text",
                        "text": f"Existing (potentially mangled) rendering:\n\n```markdown\n{mangled_body}\n```",
                    },
                ],
            }
        ],
    )
    parts = [b.text for b in response.content if getattr(b, "type", "") == "text"]
    return "\n".join(parts).strip()


def build_anthropic_client():
    """Construct a real anthropic.Anthropic client. Imported lazily so tests don't need the SDK env."""
    import anthropic

    return anthropic.Anthropic()
