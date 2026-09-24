import os
from pathlib import Path

import yaml
from pydantic import ValidationError

from papers_pipeline.errors import PipelineError
from papers_pipeline.models import PipelineState


def load_state(path: Path) -> PipelineState:
    if not path.exists():
        return PipelineState()

    try:
        raw_state = yaml.safe_load(path.read_text())
    except OSError as error:
        raise PipelineError(str(error)) from error
    except yaml.YAMLError as error:
        raise PipelineError(str(error)) from error

    if raw_state is None:
        return PipelineState()
    if not isinstance(raw_state, dict):
        raise PipelineError("state: expected a mapping at the top level")

    try:
        return PipelineState.model_validate(raw_state)
    except ValidationError as error:
        raise PipelineError(str(error)) from error


def save_state(path: Path, state: PipelineState) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f"{path.name}.tmp")
    temporary.write_text(
        yaml.safe_dump(state.model_dump(mode="json"), sort_keys=True),
        encoding="utf-8",
    )
    os.replace(temporary, path)
