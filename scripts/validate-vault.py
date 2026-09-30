#!/usr/bin/env python3
"""Repository-wide Obsidian vault consistency checks."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
files = {p.relative_to(ROOT).as_posix(): p for p in ROOT.rglob("*.md")}

errors = []
warnings = []

# Durable knowledge notes have a semantic role. Navigation, tooling, and
# workflow-support Markdown files do not need to pretend they are knowledge
# artifacts merely to satisfy frontmatter validation.
def is_knowledge_artifact(rel: str, path: Path) -> bool:
    parts = Path(rel).parts
    name = path.name

    if name in {"README.md", "AGENTS.md"}:
        return False

    if "scripts" in parts or ".obsidian" in parts:
        return False

    # Templates are source material for creating notes, not notes themselves.
    if any(part.lower() in {"_templates", "templates"} for part in parts):
        return False

    # Dashboards/control-plane pages are workflow support artifacts. They may
    # still carry a specialized type such as dashboard, but are not required
    # to participate in the durable-note contract.
    if "dashboard" in name.lower():
        return False

    return True


def resolves(source_rel: str, target: str) -> tuple[bool, list[str]]:
    target = target.split("|", 1)[0].split("#", 1)[0].strip()
    if not target or target.startswith(("http://", "https://")):
        return True, []

    source_dir = Path(source_rel).parent

    # Prefer an explicit vault-relative path.
    if "/" in target:
        candidate = target if target.endswith(".md") else target + ".md"
        return candidate in files, [candidate]

    # Bare links commonly refer to a sibling note such as [[README]].
    sibling = (source_dir / f"{target}.md").as_posix()
    if sibling in files:
        return True, [sibling]

    # A unique basename is safe; duplicates are ambiguous and should be reviewed.
    candidates = [p for p in files if Path(p).stem == Path(target).stem]
    if len(candidates) == 1:
        return True, candidates
    if len(candidates) > 1:
        return True, candidates
    return False, []


for rel, path in files.items():
    text = path.read_text(encoding="utf-8")

    if "[[../" in text:
        errors.append(f"{rel}: parent-relative wikilink")

    for n, line in enumerate(text.splitlines(), 1):
        for m in re.finditer(r"\[\[([^\]]+)\]\]", line):
            ok, candidates = resolves(rel, m.group(1))
            if not ok:
                errors.append(f"{rel}:{n}: unresolved wikilink [[{m.group(1)}]]")
            elif len(candidates) > 1:
                warnings.append(
                    f"{rel}:{n}: ambiguous wikilink [[{m.group(1)}]]; "
                    + ", ".join(candidates[:8])
                )

        # Only Markdown table rows need the pipe-alias warning. A normal prose
        # line or fenced example may legitimately contain both pipes and links.
        stripped = line.strip()
        if stripped.startswith("|") and re.search(r"\[\[[^\]]+\|[^\]]+\]\]", line):
            warnings.append(f"{rel}:{n}: wikilink alias inside table; use path-only wikilink")

    # Metadata contract applies only to durable knowledge artifacts. This keeps
    # README/navigation/support files lightweight while making note roles
    # machine-checkable.
    if is_knowledge_artifact(rel, path):
        if text.startswith("---\n") and text.count("---\n") >= 2:
            frontmatter = text.split("---\n", 2)[1]
            metadata = {}
            for line in frontmatter.splitlines():
                if ":" in line:
                    key, value = line.split(":", 1)
                    metadata[key.strip()] = value.strip().strip('"').strip("'")

            if "title" not in metadata or not metadata["title"]:
                warnings.append(f"{rel}: missing title metadata")
            if "type" not in metadata or not metadata["type"]:
                warnings.append(f"{rel}: missing type metadata")
            elif metadata["type"].lower() == "note":
                warnings.append(
                    f"{rel}: legacy generic type: note; migrate to a semantic type "
                    "(concept, pattern, reference, exercise, project, ADR, failure, evaluation, MOC)"
                )
        else:
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
