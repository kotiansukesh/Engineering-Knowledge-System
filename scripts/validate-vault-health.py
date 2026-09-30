#!/usr/bin/env python3
"""Diagnostic health report for the Obsidian knowledge system.

This is intentionally non-blocking: it reports candidates for human review
instead of auto-deleting or auto-rewriting knowledge.
"""
from pathlib import Path
from collections import defaultdict
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
notes = sorted(ROOT.rglob("*.md"))
notes = [p for p in notes if ".obsidian" not in p.parts]
paths = {p.relative_to(ROOT).as_posix() for p in notes}
stems = defaultdict(list)
orphans, missing_meta, stale = [], [], []

for p in notes:
    rel = p.relative_to(ROOT).as_posix()
    text = p.read_text(encoding="utf-8", errors="replace")
    if p.name == "README.md" or p.parts[-2:] == ("00 - Knowledge System", "README.md"):
        continue
    stems[p.stem].append(rel)
    if not text.strip():
        orphans.append(f"empty: {rel}")
    # Durable notes should have at least title/type/category or domain.
    head = text[:2500]
    has_frontmatter = head.startswith("---\n")
    if not has_frontmatter:
        missing_meta.append(f"no frontmatter: {rel}")
    else:
        fm = head.split("---\n", 2)
        body = fm[1] if len(fm) > 1 else ""
        keys = {line.split(":",1)[0].strip() for line in body.splitlines() if ":" in line}
        if "title" not in keys or "type" not in keys:
            missing_meta.append(f"missing title/type: {rel}")
    # Flag version-sensitive areas without claiming they are wrong.
    if (p.parts and p.parts[0] in {"AI", "Java"}) and any(x in text.lower() for x in ("java 25", "spring boot", "model api", "openai", "anthropic", "gemini")):
        if "last-verified:" not in text.lower() and "reviewed:" not in text.lower():
            stale.append(f"version-sensitive without verification field: {rel}")

# A note is an orphan candidate when it has no wikilink to or from another
# note. This is heuristic; intentional standalone notes are valid.
incoming = defaultdict(int)
for p in notes:
    text = p.read_text(encoding="utf-8", errors="replace")
    import re
    for target in re.findall(r"\[\[([^\]|#]+)", text):
        target = target.strip()
        target_stem = Path(target).stem
        for candidate in stems.get(target_stem, []):
            incoming[candidate] += 1
for p in notes:
    rel = p.relative_to(ROOT).as_posix()
    if p.name != "README.md" and incoming[rel] == 0:
        orphans.append(f"link-orphan-candidate: {rel}")

duplicates = [f"{stem}: {', '.join(items)}" for stem, items in stems.items() if len(items) > 1]

print("Knowledge System Health")
print("======================")
print(f"Markdown notes: {len(notes)}")
print(f"Duplicate-stem candidates: {len(duplicates)}")
print(f"Orphan/empty candidates: {len(orphans)}")
print(f"Metadata candidates: {len(missing_meta)}")
print(f"Freshness candidates: {len(stale)}")

def section(title, items, limit=40):
    if not items:
        return
    print(f"\n{title}")
    for item in items[:limit]:
        print(f"- {item}")
    if len(items) > limit:
        print(f"- ... {len(items)-limit} more")

section("Duplicate-stem candidates", duplicates)
section("Orphan/empty candidates", orphans)
section("Metadata candidates", missing_meta)
section("Freshness candidates", stale)

print("\nHealth check is diagnostic. Review candidates before changing or deleting notes.")
