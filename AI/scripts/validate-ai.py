#!/usr/bin/env python3
"""Validate the AI Obsidian vault for structural hygiene.

Warnings are reported for legacy content so the validator can be introduced
without blocking the repository. Structural link/template violations fail.
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
warnings = []

for path in ROOT.rglob("*.md"):
    text = path.read_text(encoding="utf-8")

    if "[[../" in text:
        errors.append(f"{path}: parent-relative Obsidian link")

    for line_no, line in enumerate(text.splitlines(), 1):
        if "|" in line and "[[" in line and "]]" in line:
            warnings.append(f"{path}:{line_no}: review wikilink aliases inside tables")

    for marker in (
        "[trigger keywords]",
        "[hyperparameter + typical range]",
        "[GPU hours / $ per 1M tokens]",
        "What is the trigger keyword for {{title}}?",
        "[TBD]",
    ):
        if marker in text:
            warnings.append(f"{path}: legacy placeholder: {marker}")

template = ROOT / "_templates" / "Unified-Note-Template.md"
if template.exists():
    errors.append(f"{template}: duplicate template should not exist")

if warnings:
    print("AI vault warnings:")
    print("\n".join(warnings))

if errors:
    print("\nAI vault errors:")
    print("\n".join(errors))
    sys.exit(1)

print(f"AI vault validation passed with {len(warnings)} warning(s).")
