"""Tests for scripts/_convert/remediation.py."""
from __future__ import annotations

from scripts._convert.remediation import RemediationFlags, should_remediate


def test_short_body_flags_remediation() -> None:
    flags = should_remediate(
        body="Short.",
        page_count=10,
        has_references=True,
        citations_resolved_ratio=1.0,
        latex_exit_code=0,
    )
    assert flags.flagged is True
    assert "short_body" in flags.reasons


def test_no_references_flags_remediation() -> None:
    flags = should_remediate(
        body="word " * 1000,
        page_count=10,
        has_references=False,
        citations_resolved_ratio=1.0,
        latex_exit_code=0,
    )
    assert flags.flagged is True
    assert "no_references" in flags.reasons


def test_low_citation_resolution_flags() -> None:
    flags = should_remediate(
        body="word " * 1000,
        page_count=10,
        has_references=True,
        citations_resolved_ratio=0.1,
        latex_exit_code=0,
    )
    assert flags.flagged is True
    assert "low_citation_resolution" in flags.reasons


def test_clean_paper_not_flagged() -> None:
    flags = should_remediate(
        body="word " * 2000,
        page_count=10,
        has_references=True,
        citations_resolved_ratio=0.7,
        latex_exit_code=0,
    )
    assert flags.flagged is False


def test_latex_failure_flags() -> None:
    flags = should_remediate(
        body="anything",
        page_count=10,
        has_references=True,
        citations_resolved_ratio=1.0,
        latex_exit_code=1,
    )
    assert flags.flagged is True
    assert "latex_build_failed" in flags.reasons


def test_remediate_with_pdf_returns_corrected_markdown(fixtures_dir, tmp_path):
    import json
    from scripts._convert.remediation import remediate_with_pdf

    class StubClient:
        def __init__(self, response_path):
            self._response = json.loads(response_path.read_text())
            self.calls = []

        @property
        def messages(self):
            return self

        def create(self, **kwargs):
            self.calls.append(kwargs)
            class _Resp:
                content = [type("Block", (), {"type": "text", "text": txt["text"]})()
                           for txt in self._response["content"]]
            return _Resp()

    pdf = tmp_path / "fake.pdf"
    pdf.write_bytes(b"%PDF-1.7\n%fake")
    client = StubClient(fixtures_dir / "remediation_response.json")
    body = remediate_with_pdf(pdf, mangled_body="bad output", client=client)
    assert "Cleaned Paper" in body
    assert client.calls, "expected client.messages.create to be called"
