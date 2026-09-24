import os
from pathlib import Path

import pytest

from papers_pipeline.config import load_config
from papers_pipeline.models import Paper
from papers_pipeline.topics import TopicDecision, build_topic_gate

CONFIG_PATH = Path(__file__).resolve().parents[1] / "papers.yml"


@pytest.mark.parametrize(
    ("title", "abstract", "expected"),
    [
        (
            "Audio-Driven Talking Face Generation",
            "We propose a diffusion model for lip sync.",
            TopicDecision(True, "accepted"),
        ),
        (
            "Neural Dubbing for Film",
            "Visual dubbing with a transformer.",
            TopicDecision(True, "accepted"),
        ),
        (
            "Lip Sync in Live Theatre",
            "A study of actors and audiences.",
            TopicDecision(False, "missing ML keyword"),
        ),
        (
            "Neural Speech Enhancement",
            "A deep learning model for denoising.",
            TopicDecision(False, "missing lipsync relevance keyword"),
        ),
        (
            "Talking Head Generation for Speech Recognition",
            "A neural talking face model.",
            TopicDecision(False, "matched excluded term: speech recognition"),
        ),
    ],
)
def test_configured_topic_plugin_applies_legacy_rules(
    paper: Paper, title: str, abstract: str, expected: TopicDecision
) -> None:
    config = load_config(CONFIG_PATH, os.environ)
    gate = build_topic_gate(config.topic)

    decision = gate(paper.model_copy(update={"title": title, "abstract": abstract}))

    assert config.topic.plugin == "topic_plugin:accept_topic"
    assert decision == expected
