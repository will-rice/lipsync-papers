import subprocess
import sys
from pathlib import Path
import textwrap

import pytest

from papers_pipeline.config import TopicConfig
from papers_pipeline.errors import ConfigError
from papers_pipeline.models import Paper, SourceRecord
from papers_pipeline.normalize import deduplicate, normalize
from papers_pipeline.topics import TopicDecision, build_topic_gate


@pytest.mark.parametrize(
    ("title", "expected"),
    [
        ("  Neural   Speech\nRecognition ", "Neural Speech Recognition"),
        ("BirdCLEF: Audio Detection", "BirdCLEF: Audio Detection"),
    ],
)
def test_normalize_collapses_whitespace(
    source_record: SourceRecord, title: str, expected: str
) -> None:
    assert (
        normalize(source_record.model_copy(update={"title": title})).title == expected
    )


def test_normalize_sets_identifier_and_canonical_fields(
    source_record: SourceRecord,
) -> None:
    paper = normalize(
        source_record.model_copy(
            update={
                "doi": "10.1000/ABC.DEF",
                "authors": (" Ada  Lovelace ", " Grace\nHopper "),
                "categories": ("cs.CL", "cs.AI", "cs.CL"),
            }
        )
    )

    assert paper.identifier == "doi:10.1000/abc.def"
    assert paper.abstract == "A system for speech understanding."
    assert paper.authors == ("Ada Lovelace", "Grace Hopper")
    assert paper.categories == ("cs.AI", "cs.CL")


@pytest.mark.parametrize(
    ("raw_arxiv_id", "expected"),
    [
        ("2401.00001V2", "2401.00001v2"),
        (" arXiv:2401.00001V2 ", "2401.00001v2"),
        (" arXiv:CS.CL/0101010V1 ", "cs.cl/0101010v1"),
        ("math.GT/0309136", "math.gt/0309136"),
    ],
)
def test_normalize_canonicalizes_arxiv_ids(
    source_record: SourceRecord, raw_arxiv_id: str, expected: str
) -> None:
    paper = normalize(source_record.model_copy(update={"arxiv_id": raw_arxiv_id}))

    assert paper.arxiv_id == expected
    assert paper.identifier == f"arxiv:{expected}"


def test_dedupe_prefers_arxiv_then_doi_then_source(source_record: SourceRecord) -> None:
    arxiv = normalize(
        source_record.model_copy(update={"source": "arxiv", "arxiv_id": "2401.1"})
    )
    semantic = normalize(
        source_record.model_copy(
            update={"source": "semantic_scholar", "arxiv_id": "2401.1"}
        )
    )

    assert deduplicate([semantic, arxiv]) == [arxiv]


def test_deduplicate_merges_arxiv_versions_keeping_existing_identifier(
    source_record: SourceRecord,
) -> None:
    existing = normalize(
        source_record.model_copy(update={"source": "arxiv", "arxiv_id": "2401.12345"})
    )
    refetched = normalize(
        source_record.model_copy(update={"source": "arxiv", "arxiv_id": "2401.12345v2"})
    )

    assert deduplicate([refetched, existing]) == [existing]


def test_deduplicate_merges_bibliographic_fallback_without_strong_ids(
    source_record: SourceRecord,
) -> None:
    semantic = normalize(
        source_record.model_copy(
            update={"source": "semantic_scholar", "source_id": "semantic-1"}
        )
    )
    dblp = normalize(
        source_record.model_copy(
            update={
                "source": "dblp",
                "source_id": "dblp-1",
                "title": "Neural Speech Recognition",
            }
        )
    )

    assert deduplicate([dblp, semantic]) == [semantic]


def test_deduplicate_prefers_strong_id_match_over_bibliographic_fallback(
    source_record: SourceRecord,
) -> None:
    arxiv = normalize(
        source_record.model_copy(
            update={"source": "arxiv", "source_id": "2401.1", "arxiv_id": "2401.1"}
        )
    )
    weak_match = normalize(
        source_record.model_copy(
            update={
                "source": "dblp",
                "source_id": "dblp-1",
                "title": "Neural Speech Recognition",
            }
        )
    )

    assert deduplicate([weak_match, arxiv]) == [arxiv]


def test_deduplicate_backfills_doi_from_lower_ranked_duplicate(
    source_record: SourceRecord,
) -> None:
    arxiv = normalize(
        source_record.model_copy(
            update={"source": "arxiv", "source_id": "2401.1", "arxiv_id": "2401.1"}
        )
    )
    semantic = normalize(
        source_record.model_copy(
            update={
                "source": "semantic_scholar",
                "source_id": "semantic-1",
                "arxiv_id": "2401.1",
                "doi": "10.1000/ABC.DEF",
            }
        )
    )

    [paper] = deduplicate([semantic, arxiv])

    assert paper.source == "arxiv"
    assert paper.arxiv_id == "2401.1"
    assert paper.doi == "10.1000/abc.def"
    assert paper.identifier == "arxiv:2401.1"


def test_deduplicate_keeps_preferred_conflicting_ids_deterministically(
    source_record: SourceRecord,
) -> None:
    arxiv = normalize(
        source_record.model_copy(
            update={
                "source": "arxiv",
                "source_id": "2401.1",
                "arxiv_id": "2401.1",
                "doi": "10.1000/PREFERRED",
            }
        )
    )
    semantic = normalize(
        source_record.model_copy(
            update={
                "source": "semantic_scholar",
                "source_id": "semantic-1",
                "arxiv_id": "2401.1",
                "doi": "10.1000/OTHER",
            }
        )
    )

    first, second = deduplicate([semantic, arxiv]), deduplicate([arxiv, semantic])

    assert first == second == [arxiv.model_copy(update={"doi": "10.1000/preferred"})]


def test_deduplicate_source_precedence_is_order_independent(
    source_record: SourceRecord,
) -> None:
    semantic = normalize(
        source_record.model_copy(
            update={"source": "semantic_scholar", "source_id": "semantic-1"}
        )
    )
    dblp = normalize(
        source_record.model_copy(update={"source": "dblp", "source_id": "dblp-1"})
    )

    assert deduplicate([semantic, dblp]) == [semantic]
    assert deduplicate([dblp, semantic]) == [semantic]


def test_declarative_gate_reports_exclusion(
    topic_config: TopicConfig, paper: Paper
) -> None:
    gate = build_topic_gate(topic_config.model_copy(update={"exclude_any": ["survey"]}))

    decision = gate(paper.model_copy(update={"abstract": "A survey of speech"}))

    assert decision.accepted is False
    assert decision.reason == "matched excluded term: survey"


def test_declarative_gate_reports_missing_requirements(
    topic_config: TopicConfig, paper: Paper
) -> None:
    gate = build_topic_gate(
        topic_config.model_copy(update={"include_all": ["speech", "translation"]})
    )

    decision = gate(paper)

    assert decision == TopicDecision(
        accepted=False,
        reason="missing required terms: translation",
    )


def test_declarative_gate_reports_missing_categories(
    topic_config: TopicConfig, paper: Paper
) -> None:
    gate = build_topic_gate(topic_config.model_copy(update={"categories": ["cs.LG"]}))

    decision = gate(paper)

    assert decision == TopicDecision(
        accepted=False,
        reason="missing included category: cs.LG",
    )


def test_plugin_reference_must_use_module_function_format(
    topic_config: TopicConfig,
) -> None:
    with pytest.raises(
        ConfigError, match="topic.plugin must use module:function format"
    ):
        build_topic_gate(topic_config.model_copy(update={"plugin": "invalid-plugin"}))


def test_plugin_gate_rejects_incorrect_return_type(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    topic_config: TopicConfig,
    paper: Paper,
) -> None:
    plugin = _write_plugin(
        tmp_path,
        """
        from papers_pipeline.models import Paper


        def accept_topic(paper: Paper) -> bool:
            return True
        """,
    )
    monkeypatch.syspath_prepend(str(tmp_path))
    gate = build_topic_gate(topic_config.model_copy(update={"plugin": plugin}))

    with pytest.raises(ConfigError, match="topic plugin must return TopicDecision"):
        gate(paper)


def test_plugin_gate_accepts_normalized_paper(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    topic_config: TopicConfig,
    source_record: SourceRecord,
) -> None:
    plugin = _write_plugin(
        tmp_path,
        """
        from papers_pipeline.models import Paper
        from papers_pipeline.topics import TopicDecision


        def accept_topic(paper: Paper) -> TopicDecision:
            if not isinstance(paper, Paper):
                raise TypeError("expected Paper")
            return TopicDecision(
                accepted=paper.title == "Neural Speech Recognition",
                reason=f"normalized title: {paper.title}",
            )
        """,
    )
    monkeypatch.syspath_prepend(str(tmp_path))
    gate = build_topic_gate(topic_config.model_copy(update={"plugin": plugin}))

    decision = gate(normalize(source_record))

    assert decision == TopicDecision(
        accepted=True,
        reason="normalized title: Neural Speech Recognition",
    )


def test_repository_topic_plugin_loads_outside_the_repository(tmp_path: Path) -> None:
    # The papers-pipeline console script does not run from the repository
    # root, so the documented plugin must import from any working directory.
    script = (
        "from papers_pipeline.config import TopicConfig\n"
        "from papers_pipeline.topics import build_topic_gate\n"
        "build_topic_gate(TopicConfig(plugin='topic_plugin:accept_topic'))\n"
    )

    subprocess.run([sys.executable, "-c", script], cwd=tmp_path, check=True)


def _write_plugin(tmp_path: Path, body: str) -> str:
    module_name = f"topic_plugin_support_{abs(hash(body))}"
    path = tmp_path / f"{module_name}.py"
    path.write_text(textwrap.dedent(body))
    return f"{module_name}:accept_topic"
