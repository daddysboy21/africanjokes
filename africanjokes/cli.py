"""Command-line interface for the africanjokes package."""

from __future__ import annotations

import argparse
import sys
from typing import List, Optional, Sequence

import africanjokes


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="africanjokes",
        description=(
            "Random African jokes and proverbs from the comfort of your terminal. "
            "Run with no arguments to print a random joke."
        ),
    )

    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "-j", "--joke",
        action="store_true",
        help="Print a random joke (default behavior).",
    )
    mode.add_argument(
        "-p", "--proverb",
        action="store_true",
        help="Print a random African proverb.",
    )
    mode.add_argument(
        "--list-countries",
        action="store_true",
        help="List all countries available for jokes.",
    )
    mode.add_argument(
        "--list-proverb-countries",
        action="store_true",
        help="List all countries available for proverbs.",
    )
    mode.add_argument(
        "--list-themes",
        action="store_true",
        help="List all available joke themes.",
    )
    mode.add_argument(
        "-v", "--version",
        action="store_true",
        help="Show the installed africanjokes version and exit.",
    )

    parser.add_argument(
        "-c", "--country",
        metavar="NAME",
        help="Filter to jokes/proverbs from a given country (case-insensitive).",
    )
    parser.add_argument(
        "-t", "--theme",
        metavar="NAME",
        help="Filter jokes by theme (case-insensitive). Ignored for proverbs.",
    )
    parser.add_argument(
        "-n", "--count",
        type=int,
        default=1,
        metavar="N",
        help="Number of items to print (default: 1).",
    )
    parser.add_argument(
        "--metadata",
        action="store_true",
        help="Show country (and theme/origin) alongside each item.",
    )

    return parser


def _format_joke(joke: africanjokes.Joke, with_metadata: bool) -> str:
    if not with_metadata:
        return str(joke)
    themes = ", ".join(joke.themes) if joke.themes else "—"
    return f"{joke}  [{joke.country} · {themes}]"


def _format_proverb(proverb: africanjokes.Proverb, with_metadata: bool) -> str:
    if not with_metadata:
        return str(proverb)
    return f"{proverb}  [{proverb.country} · {proverb.attribution}]"


def _print_lines(lines: Sequence[str]) -> None:
    for line in lines:
        print(line)


def _run_jokes(args: argparse.Namespace) -> int:
    try:
        jokes = africanjokes.get_jokes(
            n=args.count,
            country=args.country,
            theme=args.theme,
        )
    except (LookupError, ValueError) as exc:
        print(f"africanjokes: {exc}", file=sys.stderr)
        return 1
    _print_lines([_format_joke(j, args.metadata) for j in jokes])
    return 0


def _run_proverbs(args: argparse.Namespace) -> int:
    if args.theme:
        print("africanjokes: --theme has no effect on proverbs.", file=sys.stderr)
    try:
        proverbs = africanjokes.get_proverbs(n=args.count, country=args.country)
    except (LookupError, ValueError) as exc:
        print(f"africanjokes: {exc}", file=sys.stderr)
        return 1
    _print_lines([_format_proverb(p, args.metadata) for p in proverbs])
    return 0


def _ensure_utf8_stdio() -> None:
    # Many Windows consoles default to a legacy code page (cp1252) that can't
    # render the curly quotes and em dashes used in the joke text. Reconfigure
    # stdout/stderr to UTF-8 so output renders correctly there too.
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except (ValueError, OSError):
                pass


def main(argv: Optional[List[str]] = None) -> int:
    _ensure_utf8_stdio()
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.version:
        print(f"africanjokes {africanjokes.__version__}")
        return 0

    if args.list_countries:
        _print_lines(africanjokes.list_countries("jokes"))
        return 0

    if args.list_proverb_countries:
        _print_lines(africanjokes.list_countries("proverbs"))
        return 0

    if args.list_themes:
        _print_lines(africanjokes.list_themes())
        return 0

    if args.count < 1:
        print("africanjokes: --count must be >= 1.", file=sys.stderr)
        return 2

    if args.proverb:
        return _run_proverbs(args)

    return _run_jokes(args)


if __name__ == "__main__":
    raise SystemExit(main())
