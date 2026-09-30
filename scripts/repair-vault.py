#!/usr/bin/env python3
"""Repair deterministic Obsidian vault hygiene issues without inventing content."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {"README.md", "AGENTS.md"}

def target_exists(target: str) -> bool:
    t = target.split("#", 1)[0].strip().replace("\\|", "|")
    if "|" in t:
        t = t.split("|", 1)[0]
    if not t:
        return False
    candidates = [t, t + ".md"] if not t.endswith(".md") else [t]
    return any((ROOT / c).is_file() for c in candidates)

def normalize_links(rel: str, text: str) -> str:
    source_dir = Path(rel).parent

    def repl(m):
        body = m.group(1).replace("\\|", "|")
        parts = body.split("|", 1)
        target, alias = parts[0].strip(), parts[1] if len(parts) == 2 else None
        if not target.startswith("../"):
            return m.group(0)
        candidate = (source_dir / target).as_posix()
        if target_exists(candidate):
            return f"[[{candidate}" + (f"|{alias}" if alias is not None else "") + "]]"
        return m.group(0)

    return re.sub(r"\[\[([^\]]+)\]\]", repl, text)

def clean_placeholders(text: str) -> str:
    replacements = {
        "[trigger keywords]": "Not specified",
        "[hyperparameter + typical range]": "Not specified",
        "[GPU hours / $ per 1M tokens]": "Not specified",
        "[TBD]": "Not specified",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

changed = 0
for path in sorted(ROOT.rglob("*.md")):
    rel = path.relative_to(ROOT).as_posix()
    if rel in EXCLUDED or ".obsidian" in path.parts or "_templates" in path.parts:
        continue
    text = path.read_text(encoding="utf-8")
    new = normalize_links(rel, text)
    new = clean_placeholders(new)
    if new != text:
        path.write_text(new, encoding="utf-8")
        changed += 1

print(f"changed={changed}")
