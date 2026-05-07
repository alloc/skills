#!/usr/bin/env python3
"""Render an asciinema cast to an embeddable SVG with svg-term."""

from __future__ import annotations

import argparse
import os
import re
import shlex
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

CAST_ID_RE = re.compile(r"^[A-Za-z0-9_-]+$")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Render a local asciinema .cast file, cast ID, or asciinema.org URL to SVG via svg-term.",
    )
    parser.add_argument(
        "source",
        help="Local .cast file, asciinema cast ID, or asciinema.org URL.",
    )
    parser.add_argument("output", help="Output SVG path, for example demo.svg.")
    parser.add_argument(
        "--source-type",
        choices=("auto", "file", "cast-id", "url"),
        default="auto",
        help="How to interpret source. Default: auto.",
    )
    parser.add_argument(
        "--no-window",
        action="store_true",
        help="Omit svg-term's terminal window frame. Default keeps the window frame.",
    )
    parser.add_argument(
        "--svg-term",
        default="svg-term",
        help="svg-term command/path. Use quotes for commands with arguments, e.g. 'npx svg-term-cli'.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the command that would run without invoking svg-term.",
    )
    return parser


def die(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    sys.exit(2)


def extract_cast_id_from_url(source: str) -> str:
    parsed = urlparse(source)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        die(f"not a URL: {source}")

    parts = [part for part in parsed.path.split("/") if part]
    if not parts:
        die(f"could not find a cast ID in URL: {source}")

    if parts[0] == "a" and len(parts) >= 2:
        return parts[1]
    return parts[-1]


def resolve_source(source: str, source_type: str) -> tuple[str, Path | str]:
    path = Path(source)

    if source_type == "file":
        if not path.exists():
            die(f"cast file does not exist: {source}")
        return "file", path

    if source_type == "url":
        return "cast-id", extract_cast_id_from_url(source)

    if source_type == "cast-id":
        if not CAST_ID_RE.match(source):
            die("cast ID must contain only letters, digits, underscores, or hyphens")
        return "cast-id", source

    if path.exists():
        return "file", path

    if source.startswith(("http://", "https://")):
        return "cast-id", extract_cast_id_from_url(source)

    if CAST_ID_RE.match(source):
        return "cast-id", source

    if os.sep in source or source.endswith(".cast"):
        die(f"cast file does not exist: {source}")

    die(f"could not determine source type for: {source}")


def svg_term_base_command(raw_command: str, dry_run: bool) -> list[str]:
    command = shlex.split(raw_command)
    if not command:
        die("--svg-term cannot be empty")

    executable = command[0]
    if not dry_run and not (Path(executable).exists() or shutil.which(executable)):
        die(f"svg-term executable not found: {executable}")

    return command


def command_for_cast_id(base: list[str], cast_id: str, output: Path, include_window: bool) -> list[str]:
    command = [*base, f"--cast={cast_id}", "--out", str(output)]
    if include_window:
        command.append("--window")
    return command


def command_for_file(base: list[str], output: Path, include_window: bool) -> list[str]:
    command = [*base, "--out", str(output)]
    if include_window:
        command.append("--window")
    return command


def print_command(command: list[str], stdin_path: Path | None) -> None:
    rendered = " ".join(shlex.quote(part) for part in command)
    if stdin_path is not None:
        rendered = f"cat {shlex.quote(str(stdin_path))} | {rendered}"
    print(rendered)


def main() -> int:
    args = build_parser().parse_args()
    output = Path(args.output)
    if output.suffix.lower() != ".svg":
        die("output path should end with .svg")

    kind, value = resolve_source(args.source, args.source_type)
    include_window = not args.no_window
    base = svg_term_base_command(args.svg_term, args.dry_run)

    if kind == "file":
        cast_path = Path(value)
        command = command_for_file(base, output, include_window)
        if args.dry_run:
            print_command(command, cast_path)
            return 0
        output.parent.mkdir(parents=True, exist_ok=True)
        with cast_path.open("rb") as cast:
            subprocess.run(command, stdin=cast, check=True)
        return 0

    cast_id = str(value)
    command = command_for_cast_id(base, cast_id, output, include_window)
    if args.dry_run:
        print_command(command, None)
        return 0
    output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(command, check=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
