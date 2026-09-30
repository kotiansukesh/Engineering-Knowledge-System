# Engineering Knowledge System

This repository is a **single Obsidian vault** for building senior-level engineering capability through knowledge, implementation, measurement, failure analysis, and architecture defense.

## Start here

**Do not browse this repository folder-by-folder.** It contains reference material, practice material, projects and evidence. The learning order is defined by [[00 - Start Here]].

### The learning system

**Orient → Diagnose → Learn → Build → Break → Explain → Review → Redesign**

The important output is capability, not note count.

## Knowledge architecture

```
Engineering Knowledge System
├── 00 - Start Here       → the learning path and what to do next
├── 00 - Knowledge System → how the vault works
├── Java                  → backend implementation and targeted foundations
├── Coding Patterns       → algorithmic reasoning practice
├── AI                    → LLM, RAG, agents and production AI engineering
├── Architect             → system and enterprise architecture reasoning
├── Build Lab             → progressively harder systems
└── Evidence              → implementations, benchmarks, failures and decisions
```

## Your primary path

**Backend Engineer → AI Engineer → AI Platform Engineer → AI Architect**

1. Follow [[00 - Start Here]].
2. Use [[Study Plan]] as the master calendar.
3. Enter a domain only through its README/MOC.
4. Build the corresponding project in [[Build Lab/README]].
5. Record proof in [[Evidence/README]].
6. Use domain study plans only for the material required by the current phase.

## Domain roles

| Domain | Purpose |
|---|---|
| [[Java/README]] | Strengthen implementation/runtime foundations when the current project needs them |
| [[Coding Patterns/README]] | Maintain algorithmic fluency through short, recurring practice |
| [[AI/README]] | Primary learning track for AI engineering |
| [[Architect/README]] | Learn to make and defend system-level decisions |
| [[Build Lab/README]] | Turn concepts into working systems |
| [[Evidence/README]] | Prove that learning produced capability |

## Plugin responsibilities

- **Dataview** — derived indexes, dashboards and analytics.
- **Tasks** — actionable review work.
- **Templater** — repeatable note creation.
- **Excalidraw** — spatial/state-heavy visual reasoning.
- **Mermaid** — small maintainable flow, sequence, state and structure diagrams.

Keep Markdown as the source of truth.

## Repository conventions

- YAML frontmatter stores stable, queryable metadata.
- Use normal vault wikilinks such as `[[Java/04_Concurrency/Threads]]`.
- Never use filesystem-style relative wikilinks such as `[[../Note]]`.
- Prefer path-only wikilinks in Markdown tables.
- Keep one canonical explanation for each concept.
- Use `prerequisites` and `related` metadata where relationships materially affect navigation.
- A diagram should answer one question.
- Keep version-sensitive claims dated or verified.
- Do not create a note merely because a topic appears in a course.

## Validation

```bash
python3 scripts/validate-vault.py
python3 scripts/validate-vault-health.py
python3 scripts/validate-coding-patterns.py
python3 scripts/validate-architect.py
```

## Design principle

> **This is one engineering knowledge system whose output is demonstrated capability—not a collection of disconnected notes.**
