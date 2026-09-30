#!/usr/bin/env python3
"""Repository-wide Obsidian vault consistency checks."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
files = {p.relative_to(ROOT).as_posix(): p for p in ROOT.rglob("*.md")}

errors = []
warnings = []

def resolves(target: str) -> bool:
    target = target.split("|", 1)[0].split("#", 1)[0].strip()
    if not target or target.startswith(("http://", "https://")):
        return True
    candidate = ROOT / target
    if candidate.suffix != ".md":
        candidate = candidate.with_suffix(".md")
    if candidate.exists():
        return True
    name = Path(target).name
    return any(Path(p).stem == name for p in files)

for rel, path in files.items():
    text = path.read_text(encoding="utf-8")

    if "[[../" in text:
        errors.append(f"{rel}: parent-relative wikilink")

    for n, line in enumerate(text.splitlines(), 1):
        for m in re.finditer(r"\[\[([^\]]+)\]\]", line):
            if not resolves(m.group(1)):
                errors.append(f"{rel}:{n}: unresolved wikilink [[{m.group(1)}]]")

        # Only Markdown table rows need the pipe-alias warning. A normal prose
        # line or fenced example may legitimately contain both pipes and links.
        stripped = line.strip()
        if stripped.startswith("|") and re.search(r"\\[\\[[^\\]]+\\|[^\\]]+\\]\\]", line):
            warnings.append(f"{rel}:{n}: wikilink alias inside table; use path-only wikilink")

    # Minimal metadata contract; warnings allow incremental migration.
    if text.startswith("---\n") and text.count("---\n") >= 2:
        frontmatter = text.split("---\n", 2)[1]
        keys = {line.split(":", 1)[0].strip() for line in frontmatter.splitlines() if ":" in line}
        if "title" not in keys or "type" not in keys:
            warnings.append(f"{rel}: missing title/type metadata")
    elif path.name != "README.md":
        warnings.append(f"{rel}: missing YAML frontmatter")

    for marker in (
        "[TBD]",
        "[trigger keywords]",
        "[hyperparameter + typical range]",
        "[GPU hours / $ per 1M tokens]",
        "What is the trigger keyword for {{title}}?",
    ):
        if marker in text:
            errors.append(f"{rel}: legacy placeholder {marker}")

required_roots = {
    "AI/README.md",
    "Architect/README.md",
    "Coding Patterns/README.md",
    "AGENTS.md",
}
for required in required_roots:
    if required not in files and not (ROOT / required).exists():
        errors.append(f"missing repository anchor: {required}")

print(f"Indexed {len(files)} Markdown files.")
if warnings:
    print(f"Warnings: {len(warnings)}")
    print("\n".join(warnings[:100]))

if errors:
    print(f"Errors: {len(errors)}")
    print("\n".join(errors))
    sys.exit(1)

print("Repository-wide vault validation passed.")
