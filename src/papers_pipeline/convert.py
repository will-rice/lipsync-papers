import asyncio
import hashlib
import locale
import re
import shutil
import subprocess
from collections.abc import Awaitable, Callable, Sequence
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Protocol
from uuid import uuid4

from papers_pipeline.batching import Batch, expected_markdown
from papers_pipeline.config import ConcurrencyConfig
from papers_pipeline.errors import InfrastructureError, PaperError
from papers_pipeline.front_matter import with_front_matter
from papers_pipeline.models import FailureAttempt, Paper, PipelineState
from papers_pipeline.remote import RemoteDownloader

_DEFAULT_CONVERSION_TIMEOUT = 900.0
_PROCESS_SHUTDOWN_TIMEOUT = 2.0
_MARKER_TOOL = "marker_single"
_PANDOC_TOOL = "pandoc"
# arXiv renders most papers to HTML with LaTeXML. Converting that article with
# pandoc takes under a second, versus minutes of CPU OCR per PDF with marker.
_ARXIV_HTML_URL = "https://arxiv.org/html/{arxiv_id}"
_LATEXML_ARTICLE = re.compile(r'<article class="ltx_document.*?</article>', re.DOTALL)
_DOCUMENT_FAILURE_PATTERNS = (
    re.compile(
        r"\b(?:corrupt(?:ed)?|damaged|malformed)\s+"
        r"(?:input\s+)?(?:document|pdf|file)\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:failed|unable)\s+to\s+parse\s+"
        r"(?:input\s+|source\s+)?(?:document|pdf|file)\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\bunsupported\s+(?:input\s+|document\s+|file\s+)?"
        r"(?:format|type)\b",
        re.IGNORECASE,
    ),
    re.compile(r"\bnot\s+a\s+(?:valid\s+)?pdf\b", re.IGNORECASE),
)


class CommandRunner:
    async def run(
        self, argv: Sequence[str], timeout: float
    ) -> subprocess.CompletedProcess[str]:
        try:
            process = await asyncio.create_subprocess_exec(
                *argv,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
        except FileNotFoundError as error:
            raise InfrastructureError(f"missing conversion tool: {argv[0]}") from error

        stdout_task = asyncio.create_task(_read_stream(process.stdout))
        stderr_task = asyncio.create_task(_read_stream(process.stderr))

        try:
            await asyncio.wait_for(process.wait(), timeout=timeout)
        except asyncio.TimeoutError:
            stdout, stderr = await _terminate_process(
                process,
                stdout_task=stdout_task,
                stderr_task=stderr_task,
            )
            # A document the converter cannot finish in time fails that paper;
            # failures count per paper, so the batch and the run continue.
            raise PaperError(
                f"conversion timed out after {timeout:.0f}s: {argv[0]}"
            ) from subprocess.TimeoutExpired(
                cmd=list(argv),
                timeout=timeout,
                output=stdout,
                stderr=stderr,
            )
        except asyncio.CancelledError:
            await asyncio.shield(
                _terminate_process(
                    process,
                    stdout_task=stdout_task,
                    stderr_task=stderr_task,
                )
            )
            raise

        stdout = _decode_output(await stdout_task)
        stderr = _decode_output(await stderr_task)
        assert process.returncode is not None
        completed = subprocess.CompletedProcess(
            args=list(argv),
            returncode=process.returncode,
            stdout=stdout,
            stderr=stderr,
        )

        if completed.returncode != 0:
            output = "\n".join(
                part.strip()
                for part in (completed.stderr, completed.stdout)
                if part.strip()
            )
            message = output or f"{argv[0]} failed with exit {completed.returncode}"
            process_error = subprocess.CalledProcessError(
                returncode=completed.returncode,
                cmd=completed.args,
                output=completed.stdout,
                stderr=completed.stderr,
            )
            if _is_document_failure(completed.returncode, output):
                raise PaperError(message) from process_error
            raise InfrastructureError(
                f"conversion infrastructure failure: {message}"
            ) from process_error
        return completed


async def _read_stream(stream: asyncio.StreamReader | None) -> bytes:
    if stream is None:
        return b""
    return await stream.read()


async def _terminate_process(
    process: asyncio.subprocess.Process,
    *,
    stdout_task: asyncio.Task[bytes],
    stderr_task: asyncio.Task[bytes],
) -> tuple[str, str]:
    if process.returncode is None:
        try:
            process.terminate()
        except ProcessLookupError:
            pass

        try:
            await asyncio.wait_for(process.wait(), timeout=_PROCESS_SHUTDOWN_TIMEOUT)
        except asyncio.TimeoutError:
            if process.returncode is None:
                try:
                    process.kill()
                except ProcessLookupError:
                    pass
            await process.wait()

    stdout, stderr = await asyncio.gather(stdout_task, stderr_task)
    return _decode_output(stdout), _decode_output(stderr)


def _decode_output(data: bytes) -> str:
    return data.decode(locale.getpreferredencoding(False), errors="replace")


def _is_document_failure(returncode: int, output: str) -> bool:
    if returncode < 0 or returncode in {137, 143}:
        return False
    return any(pattern.search(output) for pattern in _DOCUMENT_FAILURE_PATTERNS)


class DownloadingMaterializer:
    def __init__(
        self,
        downloader: Callable[[str, float], Awaitable[bytes]] | None = None,
    ) -> None:
        self._downloader = downloader or _download_bytes

    async def materialize(self, paper: Paper, root: Path) -> Path:
        # The downloader validates the URL scheme, host and resolved addresses.
        # Name by format, not URL: an arXiv ID such as 1511.06841 would
        # otherwise yield the suffix ".06841" and hide the format from tools.
        suffix = _default_suffix(paper)
        target = (
            root / "inputs" / f"{_materialized_name(paper, paper.input_url)}{suffix}"
        )
        payload = await self._downloader(paper.input_url, _DEFAULT_CONVERSION_TIMEOUT)
        # root is the per-batch workspace, which is removed after the batch.
        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(payload)
        except OSError as error:
            raise InfrastructureError(
                f"conversion input cache write failed: {paper.input_url}"
            ) from error
        return target


class InputMaterializer(Protocol):
    async def materialize(self, paper: Paper, root: Path) -> Path: ...


@dataclass(frozen=True)
class PaperConversion:
    paper: Paper
    output: Path | None
    error: str | None


@dataclass(frozen=True)
class ConversionResult:
    succeeded: tuple[PaperConversion, ...]
    failed: tuple[PaperConversion, ...]
    promoted: tuple[Path, ...]
    state: PipelineState


@dataclass(frozen=True)
class _PreparedConversion:
    paper: Paper
    staged_output: Path | None
    error: str | None


def command_for(paper: Paper, input_path: Path, output: Path) -> list[str]:
    if paper.input_format in {"html", "latex"}:
        return [
            _PANDOC_TOOL,
            str(input_path),
            f"--from={paper.input_format}",
            "--to=gfm-raw_html",
            f"--output={output}",
        ]
    return [_MARKER_TOOL, str(input_path), "--output_dir", str(output)]


async def convert_batch(
    batch: Batch,
    root: Path,
    state: PipelineState,
    concurrency: ConcurrencyConfig,
    runner: CommandRunner,
    materializer: InputMaterializer | None,
    now: datetime,
    timeout_seconds: float = _DEFAULT_CONVERSION_TIMEOUT,
) -> ConversionResult:
    if concurrency.pdf != 1:
        raise InfrastructureError("PDF concurrency must equal 1")

    materializer = materializer or DownloadingMaterializer()
    workspace = _batch_workspace(root)
    semaphores = {
        "html": asyncio.Semaphore(concurrency.html),
        "latex": asyncio.Semaphore(concurrency.latex),
        "pdf": asyncio.Semaphore(1),
    }

    async def convert_arxiv_html(paper: Paper, staged_output: Path) -> bool:
        """Convert from arXiv's HTML rendering; False when arXiv has none."""
        html_paper = paper.model_copy(
            update={
                "input_format": "html",
                "input_url": _ARXIV_HTML_URL.format(arxiv_id=paper.arxiv_id),
            }
        )
        try:
            input_path = await materializer.materialize(html_paper, workspace)
        except PaperError:
            return False
        article = _LATEXML_ARTICLE.search(
            input_path.read_text(encoding="utf-8", errors="replace")
        )
        if article is None:
            return False
        # Drop arXiv's page chrome so only the paper reaches the markdown.
        input_path.write_text(article.group(0), encoding="utf-8")
        async with semaphores["html"]:
            await runner.run(
                command_for(html_paper, input_path, staged_output),
                timeout=timeout_seconds,
            )
        return True

    async def convert_one(paper: Paper) -> _PreparedConversion:
        try:
            staged_output = _staged_output_path(workspace, paper)
            if paper.arxiv_id is not None and await convert_arxiv_html(
                paper, staged_output
            ):
                return _PreparedConversion(
                    paper=paper, staged_output=staged_output, error=None
                )
            input_path = await materializer.materialize(paper, workspace)
            async with semaphores[paper.input_format]:
                if paper.input_format in {"html", "latex"}:
                    await runner.run(
                        command_for(paper, input_path, staged_output),
                        timeout=timeout_seconds,
                    )
                else:
                    marker_output_dir = _marker_output_dir(workspace, paper)
                    await runner.run(
                        command_for(paper, input_path, marker_output_dir),
                        timeout=timeout_seconds,
                    )
                    produced_markdown = _marker_markdown_path(
                        marker_output_dir, input_path
                    )
                    if not produced_markdown.exists():
                        raise InfrastructureError(
                            f"converter reported success without output: {paper.identifier}"
                        )
                    _atomic_move(produced_markdown, staged_output)

            if not staged_output.exists():
                raise InfrastructureError(
                    f"converter reported success without output: {paper.identifier}"
                )
            return _PreparedConversion(
                paper=paper, staged_output=staged_output, error=None
            )
        except PaperError as error:
            return _PreparedConversion(
                paper=paper, staged_output=None, error=str(error)
            )

    tasks = [asyncio.create_task(convert_one(paper)) for paper in batch.papers]
    results: list[_PreparedConversion] = []

    try:
        pending = set(tasks)
        while pending:
            done, pending = await asyncio.wait(
                pending,
                return_when=asyncio.FIRST_COMPLETED,
            )
            for task in done:
                try:
                    results.append(task.result())
                except InfrastructureError:
                    await _cancel_pending(pending)
                    raise
                except BaseException as error:
                    await _cancel_pending(pending)
                    raise InfrastructureError(
                        "unexpected converter task failure"
                    ) from error

        succeeded = _promote_successes(results, root)
        failures = {
            identifier: list(attempts)
            for identifier, attempts in state.failures.items()
        }
        failed: list[PaperConversion] = []
        promoted: list[Path] = []

        for result in results:
            if result.error is None:
                failures.pop(result.paper.identifier, None)
                continue

            failed.append(
                PaperConversion(paper=result.paper, output=None, error=result.error)
            )
            attempts = [
                *failures.get(result.paper.identifier, []),
                FailureAttempt(occurred_at=now, error=result.error),
            ][-3:]
            if len(attempts) < 3:
                failures[result.paper.identifier] = attempts
                continue

            marker = expected_markdown(root, result.paper).with_suffix(".fixme.txt")
            write_fixme(
                marker,
                identifier=result.paper.identifier,
                latest_error=result.error,
                attempts=attempts,
            )
            promoted.append(marker)
            failures.pop(result.paper.identifier, None)

        return ConversionResult(
            succeeded=succeeded,
            failed=tuple(failed),
            promoted=tuple(promoted),
            state=state.model_copy(update={"failures": failures}),
        )
    finally:
        _cleanup_workspace(workspace)


async def _download_bytes(url: str, timeout: float) -> bytes:
    return await RemoteDownloader().download(url, timeout)


def _materialized_name(paper: Paper, input_url: str) -> str:
    digest = hashlib.sha256(input_url.encode("utf-8")).hexdigest()[:12]
    slug = "".join(
        character if character.isalnum() else "-"
        for character in paper.identifier.casefold()
    ).strip("-")
    trimmed = "-".join(part for part in slug.split("-") if part)[:48] or "paper"
    return f"{trimmed}--{digest}"


def _default_suffix(paper: Paper) -> str:
    return {"html": ".html", "latex": ".tex", "pdf": ".pdf"}[paper.input_format]


def _batch_workspace(root: Path) -> Path:
    workspace = root / ".convert-batch" / uuid4().hex[:12]
    workspace.mkdir(parents=True, exist_ok=False)
    return workspace


def _staged_output_path(workspace: Path, paper: Paper) -> Path:
    path = workspace / "outputs" / expected_markdown(workspace, paper).name
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def _marker_output_dir(workspace: Path, paper: Paper) -> Path:
    path = workspace / "marker" / expected_markdown(workspace, paper).stem
    path.mkdir(parents=True, exist_ok=True)
    return path


def _marker_markdown_path(output_dir: Path, input_path: Path) -> Path:
    return output_dir / input_path.stem / f"{input_path.stem}.md"


def _promote_successes(
    results: Sequence[_PreparedConversion], root: Path
) -> tuple[PaperConversion, ...]:
    succeeded: list[PaperConversion] = []
    for result in results:
        if result.error is not None or result.staged_output is None:
            continue
        output = expected_markdown(root, result.paper)
        result.staged_output.write_text(
            with_front_matter(
                result.paper, result.staged_output.read_text(encoding="utf-8")
            ),
            encoding="utf-8",
        )
        _atomic_move(result.staged_output, output)
        succeeded.append(PaperConversion(paper=result.paper, output=output, error=None))
    return tuple(succeeded)


def write_fixme(
    path: Path,
    *,
    identifier: str,
    latest_error: str,
    attempts: list[FailureAttempt],
) -> None:
    """Write the marker that blocks a paper from conversion until removed."""
    _atomic_write_text(
        path,
        "\n".join(
            [
                f"paper: {identifier}",
                f"latest_error: {latest_error}",
                *(
                    f"attempt: {attempt.occurred_at.isoformat()} {attempt.error}"
                    for attempt in attempts
                ),
            ]
        )
        + "\n",
    )


def _atomic_write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f"{path.name}.tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)


def _atomic_move(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    source.replace(destination)


async def _cancel_pending(tasks: set[asyncio.Task[_PreparedConversion]]) -> None:
    for task in tasks:
        task.cancel()
    if tasks:
        await asyncio.gather(*tasks, return_exceptions=True)


def _cleanup_workspace(workspace: Path) -> None:
    shutil.rmtree(workspace, ignore_errors=True)
    try:
        workspace.parent.rmdir()
    except OSError:
        pass
