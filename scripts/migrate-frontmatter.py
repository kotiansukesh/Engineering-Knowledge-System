#!/usr/bin/env python3
"""Migrate durable-note frontmatter to semantic types.

Default mode is dry-run. Use --write to modify files.
The classifier is conservative where semantics are genuinely ambiguous, but
all known durable areas have explicit classifications.
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
    (re.compile(r"^00 - Start Here\.md$", re.I), "MOC"),
    (re.compile(r"^Study Plan\.md$", re.I), "syllabus"),
    (re.compile(r"^00 - Knowledge System/Learning Graph\.md$", re.I), "MOC"),
    (re.compile(r"^00 - Knowledge System/Cross Domain Map\.md$", re.I), "MOC"),
    (re.compile(r"^00 - Knowledge System/10x Exercises\.md$", re.I), "exercise"),
    (re.compile(r"^00 - Knowledge System/.*\.md$", re.I), "reference"),
]

PREFIX_TYPES = [
    ("Coding Patterns/", "pattern"),
    ("Build Lab/", "project"),
    ("Evidence/", "evidence"),
    ("Architect/_templates/", "template"),
]

CATEGORY_TYPES = [("/99_Revision/", "reference")]

DOMAIN_TYPES = [
    ("AI/", "concept"),
    ("Architect/", "concept"),
    ("Java/", "concept"),
]

def infer(path: Path, text: str) -> str | None:
    rel = path.relative_to(ROOT).as_posix()
    if rel in EXCLUDED or any(x in path.parts for x in EXCLUDED_PARTS):
        return None
    existing = re.search(r"^type:\s*(.+)$", text, re.I | re.M)
    if existing:
        current = existing.group(1).strip()
        legacy_aliases = {"plan": "syllabus", "architecture-decision": "ADR", "failure-experiment": "failure"}
        if current.lower() in legacy_aliases:
            return legacy_aliases[current.lower()]
        if current.lower() not in {"note"}:
            return current
    for rx, typ in RULES:
        if rx.search(rel):
            return typ
    for prefix, typ in PREFIX_TYPES:
        if rel.startswith(prefix):
            return typ
    for fragment, typ in CATEGORY_TYPES:
        if fragment in rel:
            return typ
    for prefix, typ in DOMAIN_TYPES:
        if rel.startswith(prefix):
            return typ
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
    changed = 0
    unresolved = []
    for path in sorted(ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        typ = infer(path, text)
        if not typ:
            if path.name not in EXCLUDED and not any(x in path.parts for x in EXCLUDED_PARTS):
                unresolved.append(path.relative_to(ROOT).as_posix())
            continue
        current = re.search(r"^type:\s*(.+)$", text, re.I | re.M)
        current_type = current.group(1).strip() if current else None
        if current_type == typ:
            continue
        print(f"{'[WRITE]' if args.write else '[PLAN]'} {path.relative_to(ROOT)}: {current_type or '<missing>'} -> {typ}")
        changed += 1
        if args.write:
            path.write_text(replace_type(text, typ), encoding="utf-8")
    print(f"changed={changed} mode={'write' if args.write else 'dry-run'}")
    print(f"unresolved={len(unresolved)}")
    for rel in unresolved[:100]:
        print(f"[REVIEW] {rel}")

if __name__ == "__main__":
    main()
