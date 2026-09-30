#!/usr/bin/env python3
"""Validate the Coding Patterns Obsidian vault.

No third-party dependencies are required.
The validator checks:
- Obsidian wikilink targets
- forbidden filesystem-style links
- pipe aliases inside Markdown-table wikilinks
- required pattern frontmatter fields
- duplicate LeetCode IDs in the Problem Bank
- referenced Coding Patterns paths in Dataview/Tasks blocks
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "Coding Patterns"

REQUIRED_PATTERN_FIELDS = {
    "type", "pattern", "domain", "category", "advanced", "mastery",
    "recognition_score", "difficulty", "leetcode", "created",
    "reviewed", "next_review", "tags",
}

LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
FIELD_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?$")
PROBLEM_ID_RE = re.compile(r"^\|\s*(\d+)\s*\|")
DATAVIEW_PATH_RE = re.compile(r'^(?:FROM|path includes)\s+"([^"]+)"', re.MULTILINE)

errors: list[str] = []
warnings: list[str] = []

def md_files() -> list[Path]:
    return [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]

def note_targets() -> set[str]:
    result = set()
    for p in md_files():
        rel_root = p.relative_to(ROOT).as_posix()[:-3]
        rel_vault = p.relative_to(VAULT).as_posix()[:-3] if VAULT in p.parents else rel_root
        result.update({rel_root, rel_vault, p.stem})
    return result

def resolves(target: str, source: Path, targets: set[str]) -> bool:
    target = target.split("#", 1)[0].split("|", 1)[0].strip()
    if not target or target.startswith(("http://", "https://")):
        return True
    if target.startswith("../"):
        return False
    candidates = {target.removesuffix(".md")}
    if target.startswith("Coding Patterns/"):
        candidates.add(target[len("Coding Patterns/"):].removesuffix(".md"))
    else:
        candidates.add((source.parent / target).as_posix().removesuffix(".md"))
    return any(x in targets for x in candidates)

def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        errors.append(f"{path}: unterminated YAML frontmatter")
        return {}
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        m = FIELD_RE.match(line)
        if m:
            data[m.group(1)] = m.group(2) or ""
    return data

def validate_links(path: Path, text: str, targets: set[str]) -> None:
    if VAULT not in path.parents and path != VAULT:
        return
    for raw in LINK_RE.findall(text):
        if raw.startswith("http://") or raw.startswith("https://"):
            continue
        if raw.startswith("../"):
            errors.append(f"{path}: forbidden relative wikilink [[{raw}]]")
            continue

        target = raw.split("#", 1)[0]
        target = target.split("|", 1)[0].strip()
        if "|" in raw and "|" in target:
            errors.append(f"{path}: malformed wikilink [[{raw}]]")

        if target and not resolves(target, path, targets):
            errors.append(f"{path}: missing wikilink target [[{raw}]]")

def validate_pattern_metadata(path: Path, data: dict[str, str]) -> None:
    if data.get("type") != "pattern":
        return
    missing = REQUIRED_PATTERN_FIELDS - data.keys()
    for field in sorted(missing):
        errors.append(f"{path}: missing pattern frontmatter field '{field}'")
    score = data.get("recognition_score")
    if score and not re.fullmatch(r"\d+", score.strip()):
        warnings.append(f"{path}: recognition_score is not numeric: {score}")

def validate_problem_bank(path: Path, text: str) -> None:
    if path.name != "Problem Bank.md":
        return
    ids: dict[str, int] = {}
    for line_no, line in enumerate(text.splitlines(), 1):
        m = PROBLEM_ID_RE.match(line)
        if not m:
            continue
        problem_id = m.group(1)
        ids[problem_id] = ids.get(problem_id, 0) + 1
    for problem_id, count in ids.items():
        if count > 1:
            errors.append(f"{path}:{problem_id}: duplicate problem ID appears {count} times")

def validate_queries(path: Path, text: str) -> None:
    for folder in DATAVIEW_PATH_RE.findall(text):
        if not (ROOT / folder).exists():
            errors.append(f"{path}: query references missing path '{folder}'")
    if "path includes Coding Patterns" in text and not VAULT.exists():
        errors.append(f"{path}: Tasks path references missing Coding Patterns folder")

def main() -> int:
    if not VAULT.exists():
        print("ERROR: Coding Patterns folder not found")
        return 1

    targets = note_targets()
    files = md_files()

    for path in files:
        text = path.read_text(encoding="utf-8")
        data = frontmatter(path)
        validate_links(path, text, targets)
        validate_pattern_metadata(path, data)
        validate_problem_bank(path, text)
        validate_queries(path, text)

    # The most important table-link failure mode in this vault.
    for path in files:
        if VAULT not in path.parents:
            continue
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith("|") and "[[" in line and "]]" in line:
                for link in LINK_RE.findall(line):
                    if "|" in link:
                        errors.append(f"{path}:{line_no}: pipe alias inside table-capable wikilink [[{link}]]")

    print(f"Validated {len(files)} Markdown files.")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    for item in errors:
        print(f"ERROR: {item}")
    for item in warnings:
        print(f"WARNING: {item}")

    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
