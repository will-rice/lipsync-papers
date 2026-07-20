"""Tests for the semantic relevance gate in fetch_papers."""

from __future__ import annotations

import pytest

from scripts.fetch_papers import SemanticGate, load_existing_papers

pytestmark = pytest.mark.slow

# Relevant to the corpus but contains NO POSITIVE_RELEVANCE_KEYWORDS phrase —
# exactly the class of paper the keyword gate misses.
RELEVANT_NO_KEYWORD = {
    "arxiv_id": "test-relevant",
    "title": "Diffusion-Based Portrait Video Generation from Audio",
    "abstract": "We present a diffusion framework that animates a single portrait "
    "photograph from a driving speech signal. A transformer motion generator maps "
    "audio features to expressive head and mouth dynamics, producing photorealistic "
    "portrait videos that are temporally coherent and identity preserving.",
}

OFF_TOPIC = {
    "arxiv_id": "test-offtopic",
    "title": "Beamforming Codebook Design for Millimeter-Wave Channels",
    "abstract": "We propose a hierarchical codebook construction for hybrid "
    "beamforming in millimeter-wave communication systems, analyzing achievable "
    "rates under hardware constraints and channel estimation error.",
}


@pytest.fixture(scope="module")
def corpus() -> list[dict]:
    papers = list(load_existing_papers().values())
    assert len(papers) >= 100, "papers.csv should hold the curated corpus"
    return papers


@pytest.fixture(scope="module")
def gate(corpus: list[dict]) -> SemanticGate:
    return SemanticGate(corpus)


def test_relevant_scores_higher_than_off_topic(gate: SemanticGate) -> None:
    assert gate.score(RELEVANT_NO_KEYWORD) > gate.score(OFF_TOPIC)


def test_corpus_paper_excludes_itself(corpus: list[dict]) -> None:
    small = SemanticGate(corpus[:2])
    # With self excluded, each paper's only neighbor is the other one, so both
    # scores equal cos(a, b) — and neither is inflated by self-similarity 1.0.
    score_a = small.score(corpus[0])
    score_b = small.score(corpus[1])
    assert score_a == pytest.approx(score_b, abs=1e-5)
    assert score_a < 0.999
