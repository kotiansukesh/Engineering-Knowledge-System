#!/usr/bin/env python3
"""Validate the AI Obsidian vault for structural and cross-vault hygiene."""

from pathlib import Path
import re
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
AI_ROOT = REPO_ROOT / "AI"
errors = []
warnings = []

markdown_files = {p.relative_to(REPO_ROOT).as_posix(): p for p in REPO_ROOT.rglob("*.md")}

def resolve_wikilink(source: Path, raw_target: str) -> bool:
    target = raw_target.split("|", 1)[0].split("#", 1)[0].strip()
    if not target or target.startswith(("http://", "https://")):
        return True

    # Obsidian links are vault-relative in this repository.
    candidate = REPO_ROOT / target
    if candidate.suffix != ".md":
        candidate_md = candidate.with_suffix(".md")
    else:
        candidate_md = candidate

    if candidate_md.exists():
        return True

    # A link may omit the .md suffix or point to a note by basename.
    basename = Path(target).name
    matches = [
        p for p in markdown_files
        if Path(p).stem == basename or p == target
    ]
    return bool(matches)

for path in AI_ROOT.rglob("*.md"):
    text = path.read_text(encoding="utf-8")

    if "[[../" in text:
        errors.append(f"{path.relative_to(REPO_ROOT)}: parent-relative Obsidian link")

    for line_no, line in enumerate(text.splitlines(), 1):
        for match in re.finditer(r"\[\[([^\]]+)\]\]", line):
            if not resolve_wikilink(path, match.group(1)):
                errors.append(
                    f"{path.relative_to(REPO_ROOT)}:{line_no}: unresolved wikilink "
                    f"[[{match.group(1)}]]"
                )

        # Pipe aliases inside Markdown tables are parsed as table separators.
        if "|" in line and "[[" in line and "]]" in line:
            warnings.append(
                f"{path.relative_to(REPO_ROOT)}:{line_no}: "
                "review wikilink aliases inside tables"
            )

    for marker in (
        "[trigger keywords]",
        "[hyperparameter + typical range]",
        "[GPU hours / $ per 1M tokens]",
        "What is the trigger keyword for {{title}}?",
        "[TBD]",
    ):
        if marker in text:
            errors.append(
                f"{path.relative_to(REPO_ROOT)}: legacy placeholder: {marker}"
            )

template = AI_ROOT / "_templates" / "Unified-Note-Template.md"
if template.exists():
    errors.append(f"{template.relative_to(REPO_ROOT)}: duplicate template should not exist")

if warnings:
    print("AI vault warnings:")
    print("\n".join(warnings))

if errors:
    print("\nAI vault errors:")
    print("\n".join(errors))
    sys.exit(1)

print(
    f"AI vault validation passed: {len(markdown_files)} repository Markdown files "
    f"indexed; {len(warnings)} warning(s)."
)
