#!/usr/bin/env python3
"""Static checks for Mermaid flowcharts used in Obsidian."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

UNQUOTED_SPECIAL = re.compile(
    r"(?P<id>[A-Za-z][A-Za-z0-9_]*)\[(?![\(\{\"])(?P<label>[^\]\n]*[(){}][^\]\n]*)\]"
)

for path in ROOT.rglob("*.md"):
    rel = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding="utf-8")
    in_mermaid = False

    for line_no, line in enumerate(text.splitlines(), 1):
        if line.strip().lower() == "```mermaid":
            in_mermaid = True
            continue
        if in_mermaid and line.strip() == "```":
            in_mermaid = False
            continue
        if not in_mermaid:
            continue

        for match in UNQUOTED_SPECIAL.finditer(line):
            errors.append(
                f"{rel}:{line_no}: Mermaid node label contains special characters without quotes: {match.group(0)}"
            )

if errors:
    print(f"Mermaid validation failed: {len(errors)} issue(s)")
    print("\n".join(errors))
    sys.exit(1)

print("Mermaid static validation passed.")
