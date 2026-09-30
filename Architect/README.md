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

1. Foundations
2. Requirements & Quality Attributes
3. Architecture Styles
4. Data Architecture
5. Integration & APIs
6. Reliability & Operations
7. System Design Practice
8. AI Architecture
9. Revision

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
