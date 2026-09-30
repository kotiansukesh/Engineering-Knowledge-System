#!/usr/bin/env python3
"""Validate the Architect Obsidian vault without third-party dependencies."""

from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "Architect"
LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
FIELD_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?$")

errors: list[str] = []
warnings: list[str] = []

def md_files():
    return [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]

def targets():
    out = set()
    for p in md_files():
        rel = p.relative_to(ROOT).as_posix()[:-3]
        out.add(rel)
        out.add(p.stem)
    return out

def frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        errors.append(f"{path}: unterminated frontmatter")
        return {}
    data = {}
    for line in text[4:end].splitlines():
        m = FIELD_RE.match(line)
        if m:
            data[m.group(1)] = m.group(2) or ""
    return data

def main():
    if not VAULT.exists():
        print("ERROR: Architect folder not found")
        return 1

    files = [p for p in md_files() if VAULT in p.parents]
    known = targets()

    for path in files:
        text = path.read_text(encoding="utf-8")
        data = frontmatter(path)

        for raw in LINK_RE.findall(text):
            if raw.startswith("http://") or raw.startswith("https://"):
                continue
            if raw.startswith("../"):
                errors.append(f"{path}: forbidden relative wikilink [[{raw}]]")
                continue
            target = raw.split("#", 1)[0].split("|", 1)[0].strip()
            if target and target not in known:
                errors.append(f"{path}: missing wikilink target [[{raw}]]")

        for line_no, line in enumerate(text.splitlines(), 1):
            if line.lstrip().startswith("|") and "[[" in line:
                for raw in LINK_RE.findall(line):
                    if "|" in raw:
                        errors.append(f"{path}:{line_no}: pipe alias inside table wikilink [[{raw}]]")

        if data.get("type") == "note":
            for field in ("category", "completed", "difficulty"):
                if field not in data:
                    errors.append(f"{path}: note missing '{field}' frontmatter")

        if "[TBD]" in text:
            warnings.append(f"{path}: contains [TBD] placeholder")
        if "Key algorithm/architecture pattern" in text:
            warnings.append(f"{path}: contains generic flashcard placeholder")
        if "repeated sections" in text.lower():
            warnings.append(f"{path}: possible duplicated section marker")

    print(f"Validated {len(files)} Architect Markdown files.")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    for x in errors:
        print("ERROR:", x)
    for x in warnings:
        print("WARNING:", x)
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
