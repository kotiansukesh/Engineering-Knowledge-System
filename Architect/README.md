---
title: Architect Vault
type: moc
domain: architect
tags: [architecture, system-design, enterprise-architecture, ai-architecture]
created: 2026-09-30
---

# Architect

> **Design systems under constraints.**

This vault is for architecture reasoning: **Requirements → Constraints → Design → Failure → Trade-off → Defend**.

## Start here

1. [[01_Architecture-Foundations/README|Foundations]]
2. [[02_Requirements-Quality-Attributes/README|Requirements & Quality Attributes]]
3. [[03_Architecture-Styles/README|Architecture Styles]]
4. [[06_Data-Architecture/README|Data Architecture]]
5. [[07_Integration-APIs/README|Integration & APIs]]
6. [[08_NonFunctional-Ops/README|Reliability & Operations]]
7. [[10_System-Design-Interviews/README|System Design Practice]]
8. [[13_AI-Architecture/README|AI Architecture]]
9. [[99_Revision/Study Plan|Revision]]

## The architecture loop

```text
Requirements
    ↓
Constraints + Estimates
    ↓
Quality Attributes / SLOs
    ↓
Simplest viable design
    ↓
Failure analysis
    ↓
Alternatives + trade-offs
    ↓
Decision / ADR
    ↓
Evidence
    ↓
Review when constraints change
```

## Learn a concept

Every architecture note should answer:

1. **What problem does it solve?**
2. **What constraints make it useful?**
3. **How does it work?**
4. **What is the simplest alternative?**
5. **What fails?**
6. **What would I measure?**
7. **When would I redesign it?**

## Practice loop

**Learn → Understand → Build → Break → Explain → Review**

Reading a note is not evidence of mastery.

## Diagram rule

Use **one diagram for one question**.

- **Mermaid:** simple flow, sequence, state, component/class relationships.
- **Excalidraw:** spatial reasoning, distributed topology, concurrency, memory/layout exploration.
- Avoid static screenshots when the diagram can be regenerated from text.

## Active review

```tasks
not done
path includes Architect
sort by due
limit 15
```

## Dashboard

```dataview
TABLE WITHOUT ID
  file.link as "Topic",
  difficulty as "Difficulty",
  status as "Status",
  next_review as "Next review"
FROM "Architect"
WHERE type IN ("note", "architecture", "practice")
SORT date(next_review) ASC
LIMIT 20
```

## Vault boundaries

This is a **separate Obsidian vault**. Do not use ordinary `[[...]]` links to files in another vault.

For cross-vault references use the shared contract in `../_shared/`:

```yaml
related:
  - vault: java
    note: "Concurrency"
  - vault: ai
    note: "Agent Concurrency"
```

Use a GitHub/Markdown URL when a clickable cross-vault link is required.

## Plugin roles

- **Dataview:** derived views only.
- **Tasks:** actions and review work.
- **Templater:** note creation.
- **Excalidraw:** complex visual reasoning.

> **Do not add infrastructure unless a requirement, failure mode, organizational constraint, or measured bottleneck justifies it.**
