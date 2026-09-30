---
title: Architect
type: MOC
domain: Architect
tags: [architecture, system-design, enterprise-architecture, ai-architecture]
created: 2026-09-30
---

# Architect

> **Design systems under constraints.**

This is a domain inside the **single repository-wide Obsidian vault**. The master learning order is [[00 - Start Here]]; this MOC tells you how to navigate architecture material once the master plan points here.

## Start here when architecture becomes the current phase

1. [[01_Architecture-Foundations/README|Foundations]]
2. [[02_Requirements-Quality-Attributes/README|Requirements & Quality Attributes]]
3. [[03_Architecture-Styles/README|Architecture Styles]]
4. [[06_Data-Architecture/README|Data Architecture]]
5. [[07_Integration-APIs/README|Integration & APIs]]
6. [[08_NonFunctional-Ops/README|Reliability & Operations]]
7. [[10_System-Design-Interviews/README|System Design Practice]]
8. [[13_AI-Architecture/README|AI Architecture]]
9. [[99_Revision/Study Plan|Revision]]

## Architecture loop

**Requirements → Constraints → Quality Attributes → Simplest Design → Failure → Trade-off → Decision → Evidence → Review**

## Practice

**Learn → Guided → Blind → Failure Injection → Defend → Redesign**

Reading a note is not evidence of mastery.

## Diagram rule

Use one diagram for one question.

- **Mermaid:** simple flow, sequence, state and structure.
- **Excalidraw:** spatial reasoning, distributed topology and exploratory diagrams.

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

## Plugin roles

- **Dataview:** derived views only.
- **Tasks:** actions and review work.
- **Templater:** note creation.
- **Excalidraw:** complex visual reasoning.

> **Do not add infrastructure unless a requirement, failure mode, organizational constraint, or measured bottleneck justifies it.**
