"""Command-line entrypoint for the papers pipeline."""

import argparse
import asyncio
from datetime import datetime, timezone
import os
from pathlib import Path
import shutil
import sys
import time
from typing import Sequence

from papers_pipeline.adapters import build_adapters
from papers_pipeline.config import load_config
from papers_pipeline.convert import CommandRunner, DownloadingMaterializer
from papers_pipeline.errors import ConfigError, InfrastructureError
from papers_pipeline.formatting import format_changed, shard_paths
from papers_pipeline.front_matter import write_front_matter
from papers_pipeline.inventory import read_inventory
from papers_pipeline.git import GitRepository
from papers_pipeline.http import RequestClient
from papers_pipeline.pipeline import (
    Dependencies,
    PipelinePaths,
    has_more_work,
    run_nightly,
)
from papers_pipeline.state import load_state
from papers_pipeline.preflight import ToolLookup, validate_required_tools


def app(
    argv: Sequence[str] | None = None,
    *,
    tool_lookup: ToolLookup = shutil.which,
) -> int:
    """Run the pipeline CLI."""

    parser = argparse.ArgumentParser(prog="papers-pipeline")
    subparsers = parser.add_subparsers(dest="command", required=True)
    validate = subparsers.add_parser("validate")
    validate.add_argument("--config", type=Path, default=Path("papers.yml"))
    validate.add_argument("--config-only", action="store_true")
    nightly = subparsers.add_parser("nightly")
    nightly.add_argument("--config", type=Path, default=Path("papers.yml"))
    format_corpus = subparsers.add_parser("format-corpus")
    format_corpus.add_argument("--shard-index", type=int, required=True)
    format_corpus.add_argument("--shard-count", type=int, required=True)
    subparsers.add_parser("front-matter")

    args = parser.parse_args(list(argv) if argv is not None else None)
    if args.command == "validate":
        try:
            config = load_config(args.config, os.environ)
        except ConfigError as error:
            print(f"error: fix {args.config}: {error}", file=sys.stderr)
            return 2
        try:
            if not args.config_only:
                validate_required_tools(config, tool_lookup)
        except InfrastructureError as error:
            print(f"error: {error}", file=sys.stderr)
            return 2
        print(f"valid: {args.config}")
    elif args.command == "nightly":
        try:
            config = load_config(args.config, os.environ)
        except ConfigError as error:
            print(f"error: fix {args.config}: {error}", file=sys.stderr)
            return 2
        root = args.config.resolve().parent
        summary_path = (
            Path(os.environ["GITHUB_STEP_SUMMARY"])
            if "GITHUB_STEP_SUMMARY" in os.environ
            else None
        )
        dependencies = Dependencies(
            environ=os.environ,
            adapters=build_adapters(config, os.environ),
            client_factory=lambda deadline: RequestClient(config.fetch, deadline),
            materializer=DownloadingMaterializer(),
            runner=CommandRunner(),
            git=GitRepository(root),
            now=lambda: datetime.now(timezone.utc),
            monotonic=time.monotonic,
            tool_lookup=tool_lookup,
        )
        state_path = root / ".papers-state.yml"
        summary = asyncio.run(
            run_nightly(
                PipelinePaths(
                    root=root,
                    config=args.config,
                    state=state_path,
                    inventory=root / "papers.csv",
                    summary=summary_path,
                ),
                dependencies,
            )
        )
        # The nightly workflow dispatches the next run while this is true.
        if "GITHUB_OUTPUT" in os.environ:
            more_work = has_more_work(config, load_state(state_path), summary)
            with Path(os.environ["GITHUB_OUTPUT"]).open(
                "a", encoding="utf-8"
            ) as output:
                output.write(f"more_work={str(more_work).lower()}\n")
    elif args.command == "format-corpus":
        root = Path.cwd()
        selected = shard_paths(
            sorted((root / "papers").glob("*.md")),
            args.shard_index,
            args.shard_count,
        )
        asyncio.run(format_changed(selected, CommandRunner()))
    elif args.command == "front-matter":
        root = Path.cwd()
        changed = write_front_matter(root, read_inventory(root / "papers.csv"))
        asyncio.run(format_changed(changed, CommandRunner()))
        print(f"front matter updated: {len(changed)} papers")
    return 0


if __name__ == "__main__":
    raise SystemExit(app())
