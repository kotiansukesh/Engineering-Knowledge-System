#!/usr/bin/env python3
"""Validate the AI Obsidian vault for structural and template hygiene."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

for path in ROOT.rglob("*.md"):
    text = path.read_text(encoding="utf-8")

    if "[[../" in text:
        errors.append(f"{path}: parent-relative Obsidian link")

    if "|[[" in text or re.search(r"\[\[[^\]]+\|[^\]]+\]\]", text):
        # Wikilink aliases are allowed outside tables; table aliases are checked below.
        for line_no, line in enumerate(text.splitlines(), 1):
            if "|" in line and "[[" in line and "]]" in line:
                errors.append(f"{path}:{line_no}: wikilink alias inside table")

    forbidden = (
        "[trigger keywords]",
        "[hyperparameter + typical range]",
        "[GPU hours / $ per 1M tokens]",
        "What is the trigger keyword for {{title}}?",
    )
    for marker in forbidden:
        if marker in text:
            errors.append(f"{path}: generic placeholder: {marker}")

    if "[TBD]" in text:
        errors.append(f"{path}: [TBD] placeholder")

template = ROOT / "_templates" / "Unified-Note-Template.md"
if template.exists():
    errors.append(f"{template}: duplicate template should not exist")

if errors:
    print("\n".join(errors))
    sys.exit(1)

print("AI vault validation passed.")
