import json
from collections.abc import Iterator
from pathlib import Path
from uuid import uuid4

import pytest
import yaml

from papers_pipeline.cli import app
from papers_pipeline.config import ConfigError, PipelineConfig, load_config

VALID_CONFIG = """\
repository:
  name: Example Papers
  slug: example-papers
  description: Example topic
adapters:
  - name: arxiv
    enabled: true
    secret_env: null
    lookback_days: 7
    page_size: 100
    max_pages: 5
    max_results: 500
    filters: {}
topic:
  include_any: ["Example topic"]
  include_all: []
  exclude_any: []
  categories: []
  plugin: null
fetch:
  request_timeout_seconds: 30
  retries: 3
  backoff_seconds: 1
  total_deadline_seconds: 900
conversion:
  max_batches_per_run: 4
  max_papers: 10
  max_cost: 100
  timeout_seconds: 1800
  html_cost: 2
  latex_cost: 4
  pdf_cost: 20
concurrency:
  html: 4
  latex: 2
  pdf: 1
"""


@pytest.fixture
def valid_config() -> Iterator[Path]:
    fixtures_dir = Path("tests/.task-2")
    fixtures_dir.mkdir(parents=True, exist_ok=True)
    config_path = fixtures_dir / f"{uuid4()}.yml"
    config_path.write_text(VALID_CONFIG)
    try:
        yield config_path
    finally:
        config_path.unlink(missing_ok=True)


def _load_yaml(path: Path) -> dict[str, object]:
    data = yaml.safe_load(path.read_text())
    assert isinstance(data, dict)
    return data


def _write_yaml(path: Path, data: dict[str, object]) -> None:
    path.write_text(yaml.safe_dump(data, sort_keys=False))


@pytest.mark.parametrize(
    ("section", "field", "value", "message"),
    [
        ("concurrency", "pdf", 2, "concurrency.pdf must equal 1"),
        (
            "conversion",
            "max_papers",
            0,
            "conversion.max_papers must be between 1 and 100",
        ),
        (
            "fetch",
            "total_deadline_seconds",
            30,
            "fetch.total_deadline_seconds must be between 60 and 7200",
        ),
        (
            "conversion",
            "timeout_seconds",
            3601,
            "conversion.timeout_seconds must be between 60 and 3600",
        ),
    ],
)
def test_unsafe_limits_are_rejected(
    valid_config: Path,
    section: str,
    field: str,
    value: int,
    message: str,
) -> None:
    data = _load_yaml(valid_config)
    config_section = data[section]
    assert isinstance(config_section, dict)
    config_section[field] = value
    _write_yaml(valid_config, data)

    with pytest.raises(ConfigError, match=message):
        load_config(valid_config, {})


@pytest.mark.parametrize("cost_field", ["html_cost", "latex_cost", "pdf_cost"])
def test_conversion_cost_cannot_exceed_batch_budget(
    valid_config: Path,
    cost_field: str,
) -> None:
    data = _load_yaml(valid_config)
    conversion = data["conversion"]
    assert isinstance(conversion, dict)
    conversion["max_cost"] = 10
    conversion[cost_field] = 11
    _write_yaml(valid_config, data)

    with pytest.raises(
        ConfigError,
        match=(
            rf"conversion\.{cost_field} must not exceed "
            r"conversion\.max_cost"
        ),
    ):
        load_config(valid_config, {})


def test_enabled_adapter_requires_declared_secret(valid_config: Path) -> None:
    data = _load_yaml(valid_config)
    adapters = data["adapters"]
    assert isinstance(adapters, list)
    assert isinstance(adapters[0], dict)
    adapters[0]["secret_env"] = "S2_KEY"
    _write_yaml(valid_config, data)

    with pytest.raises(ConfigError, match="missing secret S2_KEY"):
        load_config(valid_config, {})


@pytest.mark.parametrize(
    "plugin", ["accept_topic", "topic_plugin", "topic-plugin:accept_topic"]
)
def test_plugin_reference_must_use_module_function_format(
    valid_config: Path, plugin: str
) -> None:
    data = _load_yaml(valid_config)
    topic = data["topic"]
    assert isinstance(topic, dict)
    topic["plugin"] = plugin
    _write_yaml(valid_config, data)

    with pytest.raises(
        ConfigError, match="topic.plugin must use module:function format"
    ):
        load_config(valid_config, {})


@pytest.mark.parametrize(
    ("adapter_name", "filters", "message"),
    [
        ("arxiv", {"query": "*"}, "arxiv.filters only supports: search_query"),
        (
            "huggingface",
            {"query": "*"},
            "huggingface.filters does not support any keys",
        ),
        (
            "semantic_scholar",
            {"search_query": "*"},
            "semantic_scholar.filters only supports: query",
        ),
        ("dblp", {"search_query": "*"}, "dblp.filters only supports: query"),
        (
            "biorxiv_crossref",
            {"query": "*"},
            "biorxiv_crossref.filters only supports: provider",
        ),
        (
            "biorxiv_crossref",
            {"provider": "medrxiv"},
            "biorxiv_crossref.filters.provider must be biorxiv or crossref",
        ),
        (
            "papers_with_code",
            {"query": "*"},
            "papers_with_code.filters does not support any keys",
        ),
    ],
)
def test_adapter_filters_must_match_supported_keys(
    valid_config: Path, adapter_name: str, filters: dict[str, str], message: str
) -> None:
    data = _load_yaml(valid_config)
    adapters = data["adapters"]
    assert isinstance(adapters, list)
    assert isinstance(adapters[0], dict)
    adapters[0]["name"] = adapter_name
    adapters[0]["filters"] = filters
    _write_yaml(valid_config, data)

    with pytest.raises(ConfigError, match=message):
        load_config(valid_config, {})


def test_semantic_scholar_page_size_matches_its_api_limit(valid_config: Path) -> None:
    data = yaml.safe_load(valid_config.read_text(encoding="utf-8"))
    data["adapters"] = [
        {
            "name": "semantic_scholar",
            "secret_env": "SEMANTIC_SCHOLAR_API_KEY",
            "lookback_days": 7,
            "page_size": 101,
            "max_pages": 1,
            "max_results": 101,
        }
    ]
    valid_config.write_text(yaml.safe_dump(data), encoding="utf-8")

    with pytest.raises(ConfigError, match="page_size must be at most 100"):
        load_config(valid_config, {"SEMANTIC_SCHOLAR_API_KEY": "secret"})


def test_checked_in_schema_matches_model() -> None:
    expected = (
        json.dumps(
            PipelineConfig.model_json_schema(),
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )

    assert Path("papers.schema.json").read_text() == expected


def test_validate_command_accepts_valid_config(
    valid_config: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    exit_code = app(
        ["validate", "--config", str(valid_config)],
        tool_lookup=lambda name: f"/tools/{name}",
    )

    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out == f"valid: {valid_config}\n"


def test_validate_command_reports_missing_runtime_tool(
    valid_config: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    exit_code = app(
        ["validate", "--config", str(valid_config)],
        tool_lookup=lambda name: None if name == "marker_single" else f"/tools/{name}",
    )

    captured = capsys.readouterr()
    assert exit_code == 2
    assert captured.err == "error: missing required tools: marker_single\n"


def test_validate_command_reports_invalid_config_without_traceback(
    valid_config: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    data = _load_yaml(valid_config)
    concurrency = data["concurrency"]
    assert isinstance(concurrency, dict)
    concurrency["pdf"] = 2
    _write_yaml(valid_config, data)

    exit_code = app(["validate", "--config", str(valid_config)])

    captured = capsys.readouterr()
    assert exit_code != 0
    assert captured.out == ""
    assert captured.err == f"error: fix {valid_config}: concurrency.pdf must equal 1\n"
    assert "Traceback" not in captured.err
