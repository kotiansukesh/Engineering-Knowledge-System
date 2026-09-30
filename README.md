# Engineering Knowledge System

This repository is a **single Obsidian vault** for building senior-level engineering capability through knowledge, implementation, measurement, failure analysis, and architectural defense.

## Knowledge architecture

```
Engineering Knowledge System
├── 00 - Knowledge System → how the vault works
├── Java                 → implementation, JVM, Spring and backend engineering
├── Coding Patterns      → algorithmic reasoning and pattern recognition
├── AI                   → LLM, RAG, agents and production AI engineering
├── Architect            → constraints, system design and enterprise architecture
├── Build Lab            → progressively harder systems and portfolio projects
└── Evidence             → implementations, benchmarks, failures, evaluations and decisions
```

These are **domains inside one vault**, not separate vaults. Use normal Obsidian wikilinks to connect concepts across them.

## Learning loop

**Understand → Build → Measure → Break → Decide → Explain → Review → Redesign**

A completed note is not mastery. Mastery requires independent evidence.

## Start here

1. [[Study Plan]]
2. [[Master Dashboard]]
3. [[00 - Knowledge System/README]]
4. [[Build Lab/README]]
5. [[Evidence/README]]

Then explore the domain MOCs:

- [[Java/README]]
- [[Coding Patterns/README]]
- [[AI/README]]
- [[Architect/README]]

## Plugin responsibilities

- **Dataview** — derived indexes, dashboards and analytics.
- **Tasks** — actionable review work.
- **Templater** — repeatable note creation.
- **Excalidraw** — spatial/state-heavy visual reasoning.
- **Mermaid** — small maintainable flow, sequence, state and structure diagrams.

Keep the source of truth in Markdown. Do not turn plugins into the knowledge model.

## Repository conventions

- YAML frontmatter stores stable, queryable metadata.
- Use normal local wikilinks such as `[[Java/04_Concurrency/Threads]]`.
- Avoid filesystem-style relative wikilinks such as `[[../Note]]`.
- Avoid pipe aliases inside Markdown table cells when a plain wikilink is sufficient.
- Keep one canonical explanation for each concept; link to it from other domains.
- A diagram should answer one question.
- Prefer maintainable diagram sources over static screenshots.
- Do not create a note merely because a topic appears in a course.

## Validation

Run:

```bash
python3 scripts/validate-vault.py
python3 scripts/validate-vault-health.py
```

GitHub Actions runs the same repository-level checks on pushes and pull requests.

## Design principle

> **This is one engineering knowledge system whose output is demonstrated capability—not a collection of disconnected notes.**
