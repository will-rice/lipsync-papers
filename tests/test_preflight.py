import pytest

from papers_pipeline.config import PipelineConfig
from papers_pipeline.errors import InfrastructureError
from papers_pipeline.preflight import required_tools, validate_required_tools


def _config() -> PipelineConfig:
    return PipelineConfig.model_validate(
        {
            "repository": {
                "name": "Test",
                "slug": "test-papers",
                "description": "Test",
            },
            "adapters": [
                {
                    "name": name,
                    "lookback_days": 7,
                    "page_size": 10,
                    "max_pages": 2,
                    "max_results": 20,
                }
                for name in ("arxiv", "dblp")
            ],
            "topic": {},
            "fetch": {
                "request_timeout_seconds": 5,
                "retries": 0,
                "backoff_seconds": 0,
                "total_deadline_seconds": 60,
            },
            "conversion": {
                "max_batches_per_run": 1,
                "max_papers": 5,
                "max_cost": 10,
                "html_cost": 1,
                "latex_cost": 1,
                "pdf_cost": 1,
            },
            "concurrency": {"html": 1, "latex": 1, "pdf": 1},
        }
    )


def test_required_tools_follow_enabled_adapter_formats() -> None:
    config = _config()

    assert required_tools(config) == ("marker_single", "pandoc", "prettier")


def test_preflight_reports_missing_tools_concisely() -> None:
    config = _config()

    with pytest.raises(
        InfrastructureError,
        match=r"^missing required tools: marker_single, prettier$",
    ):
        validate_required_tools(
            config,
            lookup=lambda name: "/tools/pandoc" if name == "pandoc" else None,
        )
