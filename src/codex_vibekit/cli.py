from __future__ import annotations

import argparse
import sys

from .codex_setup import build_codex_setup_prompt
from .scaffold import init_scaffold
from .system_check import run_check


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="codex-vibekit")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser(
        "init", help="Inject the vibekit scaffold into a target directory."
    )
    init_parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Target directory path (default: current directory).",
    )

    subparsers.add_parser("check", help="Check local prerequisites (uv, git, Python).")
    subparsers.add_parser(
        "codex-setup",
        help="Print a one-time setup prompt for registering Codex-native skills.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)

    if args.command == "check":
        return run_check()

    if args.command == "init":
        try:
            result = init_scaffold(args.path)
        except Exception as exc:  # pragma: no cover
            print(f"error: {exc}", file=sys.stderr)
            return 1

        print(result.summary())
        return 0

    if args.command == "codex-setup":
        print(build_codex_setup_prompt())
        return 0

    print(f"error: unknown command {args.command!r}", file=sys.stderr)
    return 2


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
