---
title: Architect Vault
type: MOC
category: Architect
tags:
  - architecture
  - system-design
  - interview-prep
  - decision-making
created: 2026-09-30
completed: false
reviewed:
sr-due:
---

# Architect

> **Architecture is reasoning under constraints.** This vault trains requirements, trade-offs, failure modes, system design and decision traceability—not component memorization.

## Start here

1. [[00 - Architecture Decision Framework]] — the core architecture reasoning loop.
2. [[00 - System Design Decision Tree]] — derive components from requirements.
3. [[00 - NFR Decision Matrix]] — turn NFRs into measurable scenarios.
4. [[00 - Architecture Trade-off Matrix]] — compare simple vs scale-oriented choices.
5. [[00 - Interview Mode]] — 45-minute system-design simulation.
6. [[00 - Architecture Failure Log]] — capture recurring reasoning failures.
7. [[10_System-Design-Interviews/README]] — curated system-design drills.
8. [[99_Revision/Study Plan]] — progression and review.

## Learning architecture

**Learn → Guided → Blind → Mixed → Interview → Mastered**

A note being read or a diagram being memorized is not evidence of architecture mastery.

### Mastery evidence

You should be able to:

- clarify ambiguous requirements;
- quantify scale before selecting infrastructure;
- translate NFRs into measurable scenarios;
- choose the simplest architecture satisfying constraints;
- explain consistency and failure semantics;
- identify the first bottleneck;
- design degraded modes and recovery;
- compare alternatives explicitly;
- state operational ownership and cost;
- explain what evidence would cause the design to change.

## 18-week progression

| Phase | Weeks | Focus | Evidence |
|---|---:|---|---|
| Foundations | 1–2 | Principles, quality attributes, trade-offs | explain decisions from constraints |
| Requirements | 3 | NFRs and quality scenarios | measurable SLO scenarios |
| Architecture styles | 4–5 | Monolith, microservices, event-driven, serverless | choose based on constraints |
| Building blocks | 6–7 | Resilience, caching, gateways, integration | failure-first design |
| DDD | 8–9 | boundaries, aggregates, events, sagas | ownership + consistency |
| Data | 10–11 | SQL/NoSQL, CQRS, event sourcing | access-pattern selection |
| Integration | 12–13 | REST, gRPC, async, Kafka, idempotency | delivery semantics |
| Operations | 14–15 | observability, security, deployment, chaos | production readiness |
| System design | 16–18 | end-to-end interview drills | timed independent design |

## Vault map

| Layer | Location | Purpose |
|---|---|---|
| Foundations | [[01_Architecture-Foundations/README]] | principles and architecture basics |
| Requirements | [[02_Requirements-Quality-Attributes/README]] | NFRs and quality scenarios |
| Styles | [[03_Architecture-Styles/README]] | architectural styles |
| Building blocks | [[04_Design-Patterns-Building-Blocks/README]] | reusable architecture mechanisms |
| DDD | [[05_Domain-Driven-Design/README]] | domain boundaries and consistency |
| Data | [[06_Data-Architecture/README]] | storage and data systems |
| Integration | [[07_Integration-APIs/README]] | communication and messaging |
| Operations | [[08_NonFunctional-Ops/README]] | reliability, security, observability |
| System design | [[10_System-Design-Interviews/README]] | interview drills |
| Revision | [[99_Revision/Study Plan]] | practice and review |

## Architecture decision loop

~~~text
Requirements
    ↓
Constraints + Estimates
    ↓
Quality Attributes / SLOs
    ↓
Simplest Viable Architecture
    ↓
Bottleneck + Failure Analysis
    ↓
Alternatives + Trade-offs
    ↓
Decision / ADR
    ↓
Evidence / Fitness Function
    ↓
Review Trigger
~~~

## Current review queue

~~~dataview
TABLE WITHOUT ID
  file.link as "Note",
  category as "Area",
  difficulty as "Difficulty",
  reviewed as "Reviewed",
  "sr-due" as "Due"
FROM "Architect"
WHERE type = "note" AND (("sr-due" != "" AND date("sr-due") <= date(today)) OR reviewed = null)
SORT date("sr-due") ASC
LIMIT 25
~~~

## Interview queue

~~~dataview
TABLE WITHOUT ID
  file.link as "Interview",
  problem as "Problem",
  requirements_score as "Req",
  estimation_score as "Est",
  design_score as "Design",
  reliability_score as "Reliability",
  tradeoff_score as "Trade-offs",
  review_date as "Review"
FROM "Architect"
WHERE type = "interview"
SORT date(review_date) ASC
LIMIT 20
~~~

## Active practice

~~~tasks
not done
path includes Architect
sort by due
limit 25
~~~

## Plugin responsibilities

- **Dataview:** indexes, review queues and analytics.
- **Tasks:** actionable practice.
- **Templater:** ADRs and interview sessions.
- **Excalidraw:** C4/state-heavy diagrams only when they add information.

## Important rule

> **Do not add infrastructure because it is familiar. Add it because a quantified requirement or failure mode demands it.**
