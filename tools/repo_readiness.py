#!/usr/bin/env python3
"""Small, dependency-free readiness checker for a local GitHub repository checkout."""

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_FILES = ("README.md", "LICENSE")
RECOMMENDED_FILES = (
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "CHANGELOG.md",
    ".github",
)


def check(root: Path) -> tuple[list[str], list[str]]:
    missing_required = [name for name in REQUIRED_FILES if not (root / name).exists()]
    missing_recommended = [name for name in RECOMMENDED_FILES if not (root / name).exists()]
    return missing_required, missing_recommended


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", type=Path)
    args = parser.parse_args()

    required, recommended = check(args.root.resolve())

    if required:
        print("Missing required files:")
        for item in required:
            print(f"- {item}")
    else:
        print("Required repository files present.")

    if recommended:
        print("Recommended additions:")
        for item in recommended:
            print(f"- {item}")

    return 1 if required else 0


if __name__ == "__main__":
    raise SystemExit(main())
