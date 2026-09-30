# Engineering Knowledge System

An Obsidian vault for building senior-level engineering capability through **knowledge, implementation, measurement, failure analysis, and architectural defense**.

## Knowledge architecture

```
Knowledge System
├── Java              → implementation language, JVM, Spring and backend engineering
├── Coding Patterns   → algorithmic reasoning and pattern recognition
├── AI                → LLM, RAG, agents and production AI engineering
├── Architect         → constraints, system design, decisions and enterprise architecture
├── Evidence          → implementations, benchmarks, failures, evaluations and decisions
└── Build Lab         → progressively harder systems that turn knowledge into portfolio evidence
```

The domains are deliberately connected. A concept should be learnable in isolation, but its engineering value is demonstrated through relationships and evidence.

## Learning loop

**Understand → Build → Measure → Break → Decide → Explain → Review → Redesign**

Completion of a note is not mastery. Mastery requires independent evidence.

## Repository conventions

- Markdown is the source of truth.
- YAML frontmatter stores stable metadata and learning state.
- Dataview derives dashboards and indexes.
- Tasks represent actionable work.
- Templater creates repeatable note structures.
- Excalidraw is used when spatial reasoning adds information.
- Mermaid is preferred for small inline diagrams.
- Obsidian wikilinks are used for internal navigation.
- Table wikilinks should be path-only; avoid pipe aliases inside tables.
- Never use parent-relative wikilinks such as `[[../Note]]`.

## Validation

Run:

```bash
python3 scripts/validate-vault.py
python3 scripts/validate-vault-health.py
```

The first command is the integrity gate. The second produces a diagnostic health report for metadata, orphans, duplicates, freshness and structural quality.

## Agent operating contract

See [[AGENTS]] for repository rules and [[00 - Knowledge System/Agent Workflow]] for the operating loop used by coding/knowledge agents.

## Start here

- [[Master Dashboard]]
- [[00 - Knowledge System/README]]
- [[00 - Knowledge System/Knowledge Model]]
- [[00 - Knowledge System/Learning Graph]]
- [[Evidence/README]]
- [[Build Lab/README]]
- [[Java/README]]
- [[Coding Patterns/README]]
- [[AI/README]]
- [[Architect/README]]

## Design principle

> **Stop treating this repository as collections of notes. Treat it as one engineering knowledge system whose output is demonstrated capability.**
