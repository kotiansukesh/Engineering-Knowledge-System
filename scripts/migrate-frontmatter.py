#!/usr/bin/env python3
"""Migrate durable-note frontmatter from generic type: note to semantic types.

Default mode is dry-run. Use --write to modify files.
The classifier is intentionally conservative: ambiguous notes remain type: note
and are reported for manual review rather than being assigned a misleading type.
"""
from __future__ import annotations
import argparse, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {"README.md", "AGENTS.md"}
EXCLUDED_PARTS = {".obsidian", "_templates"}

RULES = [
    (re.compile(r"(^|/)ADR Template\.md$", re.I), "evidence-template"),
    (re.compile(r"(^|/)ADR-Template\.md$", re.I), "template"),
    (re.compile(r"(^|/)Checklist\.md$", re.I), "checklist"),
    (re.compile(r"(^|/)Study[- ]Plan\.md$", re.I), "syllabus"),
    (re.compile(r"(^|/)Case-Studies\.md$", re.I), "case-study"),
    (re.compile(r"(^|/)Interview Questions\.md$", re.I), "interview"),
    (re.compile(r"(^|/)Interview Bank\.md$", re.I), "interview"),
    (re.compile(r"(^|/)Practice Dashboard\.md$", re.I), "dashboard"),
    (re.compile(r"(^|/)Dashboard\.md$", re.I), "dashboard"),
]

PREFIX_TYPES = [
    ("Coding Patterns/", "pattern"),
    ("Build Lab/", "project"),
    ("Evidence/", "evidence"),
    ("Architect/_templates/", "template"),
]

CATEGORY_TYPES = [
    ("/99_Revision/", "reference"),
]

def infer(path: Path, text: str) -> str | None:
    rel = path.relative_to(ROOT).as_posix()
    if rel in EXCLUDED or any(x in path.parts for x in EXCLUDED_PARTS):
        return None
    for rx, typ in RULES:
        if rx.search(rel):
            return typ
    for prefix, typ in PREFIX_TYPES:
        if rel.startswith(prefix):
            return typ
    for fragment, typ in CATEGORY_TYPES:
        if fragment in rel:
            return typ

    # Strong semantic signals inside existing frontmatter.
    if re.search(r"^type:\s*pattern\s*$", text, re.I | re.M):
        return "pattern"
    if re.search(r"^type:\s*(ADR|architecture-decision)\s*$", text, re.I | re.M):
        return "ADR"
    if re.search(r"^type:\s*(evaluation|benchmark)\s*$", text, re.I | re.M):
        return "evaluation"
    if re.search(r"^type:\s*(failure|failure-experiment)\s*$", text, re.I | re.M):
        return "failure"

    return None

def replace_type(text: str, typ: str) -> str:
    if re.search(r"^type:\s*.+$", text, re.I | re.M):
        return re.sub(r"^(type:\s*).+$", lambda m: m.group(1) + typ, text, count=1, flags=re.I | re.M)
    if text.startswith("---\n"):
        return text.replace("---\n", f"---\ntype: {typ}\n", 1)
    return f"---\ntype: {typ}\n---\n\n{text}"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    changed = ambiguous = 0
    for path in sorted(ROOT.rglob("*.md")):
        typ = infer(path, path.read_text(encoding="utf-8"))
        if not typ:
            continue
        text = path.read_text(encoding="utf-8")
        current = re.search(r"^type:\s*(.+)$", text, re.I | re.M)
        current_type = current.group(1).strip() if current else None
        if current_type == typ:
            continue
        print(f"{'[WRITE]' if args.write else '[PLAN]'} {path.relative_to(ROOT)}: {current_type or '<missing>'} -> {typ}")
        changed += 1
        if args.write:
            path.write_text(replace_type(text, typ), encoding="utf-8")
    print(f"changed={changed} mode={'write' if args.write else 'dry-run'}")
    if ambiguous:
        print(f"ambiguous={ambiguous}")

if __name__ == "__main__":
    main()
