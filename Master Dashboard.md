---
title: "Engineering Knowledge System Dashboard"
type: dashboard
domain: Cross-Domain
status: active
created: 2026-09-30
---

# Engineering Knowledge System Dashboard

> **Control plane, not a second curriculum.**
>
> [[Study Plan]] is the only schedule. This page answers: *What should I do now? What evidence exists? What needs attention?*

## Primary flow

**Study Plan → Current capability → Domain notes → Build Lab → Measure / Break → Evidence → Promotion gate**

## Current path

**Backend Expert → AI Engineer → AI Platform Engineer → AI Architect**

- [[00 - Start Here|Start Here]]
- [[Study Plan|Master Study Plan]]
- [[Build Lab/README|Build Lab]]
- [[Evidence/README|Evidence]]
- [[00 - Knowledge System/README|Knowledge System]]

## Domain navigation

| Domain | Use it for |
|---|---|
| [[Java/README|Java]] | Backend implementation and just-in-time Java/Spring/JVM depth |
| [[Coding Patterns/README|Coding Patterns]] | Algorithmic reasoning and interview maintenance |
| [[AI/README|AI]] | LLM, RAG, agents, evaluation and AI platform engineering |
| [[Architect/README|Architect]] | System design, trade-offs, enterprise and AI architecture |

## Active work queue

~~~tasks
not done
sort by due
limit 20
~~~

## Evidence health

~~~dataview
TABLE WITHOUT ID
  file.link AS "Evidence",
  type AS "Type",
  category AS "Category",
  reviewed AS "Reviewed"
FROM "Evidence"
WHERE file.name != "README" AND type
SORT reviewed ASC
LIMIT 20
~~~

## Project spine

~~~dataview
TABLE WITHOUT ID
  file.link AS "Project",
  completed AS "Done",
  reviewed AS "Reviewed"
FROM "Build Lab"
WHERE type = "project" OR file.name = "README"
SORT file.path ASC
~~~

## Review rules

- Do not interpret note counts as mastery.
- Do not create a new study calendar here.
- If a domain looks stale, inspect its MOC only after checking the current week in [[Study Plan]].
- Prefer one strong implementation/evaluation/failure experiment over many completed notes.

## Related

- [[00 - Knowledge System/Knowledge Model]]
- [[00 - Knowledge System/Learning Graph]]
- [[00 - Knowledge System/Maintenance Guide]]
