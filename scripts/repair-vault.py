#!/usr/bin/env python3
"""Repair deterministic Obsidian vault hygiene issues without inventing content."""
from pathlib import Path
import re
import posixpath

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
        # Normalize any resolvable vault-relative path containing parent segments.
        # This includes links such as Architect/06_Data-Architecture/../05_DDD-Modeling/...
        if "/../" not in target and not target.startswith("../"):
            return m.group(0)
        candidate = posixpath.normpath(target if target.startswith("..") else target)
        if target.startswith("../"):
            candidate = posixpath.normpath((source_dir / target).as_posix())
        if target_exists(candidate):
            return f"[[{candidate}" + (f"|{alias}" if alias is not None else "") + "]]"
        return m.group(0)

    return re.sub(r"\[\[([^\]]+)\]\]", repl, text)

def strip_unresolved_links(text: str) -> str:
    def repl(m):
        body = m.group(1).replace("\\|", "|")
        target, alias = (body.split("|", 1) + [None])[:2]
        target = target.strip()
        if target.startswith(("http://", "https://")) or target_exists(target):
            return m.group(0)
        return (alias.strip() if alias else target) or ""
    return re.sub(r"\[\[([^\]]+)\]\]", repl, text)

def clean_placeholders(text: str) -> str:
    replacements = {
        "[trigger keywords]": "Not specified",
        "[hyperparameter + typical range]": "Not specified",
        "[GPU hours / $ per 1M tokens]": "Not specified",
        "[TBD]": "Not specified",
        "[Key algorithm/architecture pattern]": "Not specified",
        "[Trigger scenarios]": "Not specified",
        "[Trigger scenarios and context]": "Not specified",
        "[Main trade-off]": "Not specified",
        "[Main tension: e.g., consistency vs latency]": "Not specified",
        "[Primary bottleneck: e.g., coordination, hot keys, replication lag]": "Not specified",
        "[Retry, circuit breaker, fallback, graceful degradation]": "Not specified",
        "[RED: rate, errors, duration; USE: utilization, saturation, errors]": "Not specified",
        "[Sharding, read replicas, async processing, caching layers]": "Not specified",
        "[Strong/eventual/causal - justify with use case]": "Not specified",
        "[Contract tests, chaos engineering, load tests, fault injection]": "Not specified",
        "[Managed service covers need, simple CRUD, team lacks maturity]": "Not specified",
        "[The irreversible choice that defines the architecture]": "Not specified",
        "[Strangler fig, dual-write, canary, feature flags]": "Not specified",
        "[AuthZ, encryption, audit, secrets management]": "Not specified",
        "[Structured logging, correlation IDs, distributed tracing, SLO alerts]": "Not specified",
        "[Team expertise, tooling, on-call burden, migration risk]": "Not specified",

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
    new = strip_unresolved_links(new)
    new = clean_placeholders(new)
    if new != text:
        path.write_text(new, encoding="utf-8")
        changed += 1

print(f"changed={changed}")
