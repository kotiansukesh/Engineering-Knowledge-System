---
title: Architect Vault
type: MOC
category: Architect
tags: [architecture, system-design, enterprise-architecture, ai-architecture]
created: 2026-09-30
---

# Architect

> **Architecture is reasoning under constraints.** This vault trains the ability to design, defend, break, review and evolve systems.

## Start here

1. [[00 - Architecture Decision Framework]]
2. [[00 - Architecture Practice Engine]]
3. [[00 - System Design Decision Tree]]
4. [[00 - NFR Decision Matrix]]
5. [[00 - Architecture Trade-off Matrix]]
6. [[00 - Failure Injection Lab]]
7. [[00 - Trade-off Simulator]]
8. [[00 - Architecture Redesign Lab]]
9. [[00 - Architecture Review Mode]]
10. [[00 - Architecture Mastery Dashboard]]
11. [[00 - Architecture Portfolio]]
12. [[99_Revision/Study Plan]]

## Mastery progression

**Learn → Recognize → Guided → Constraint Injection → Blind → Failure Injection → Trade-off Defense → Review → Redesign → Interview → Mastered**

Reading a note is not evidence of mastery.

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
    ↓
Constraint Change / Redesign
~~~

## Vault map

| Layer | Location | Purpose |
|---|---|---|
| Foundations | [[01_Architecture-Foundations/README]] | principles |
| Requirements | [[02_Requirements-Quality-Attributes/README]] | measurable quality |
| Styles | [[03_Architecture-Styles/README]] | architectural shapes |
| Building blocks | [[04_Design-Patterns-Building-Blocks/README]] | mechanisms |
| DDD | [[05_DDD-Modeling/README]] | boundaries and ownership |
| Data | [[06_Data-Architecture/README]] | data decisions |
| Integration | [[07_Integration-APIs/README]] | APIs and messaging |
| Operations | [[08_NonFunctional-Ops/README]] | production behavior |
| Governance | [[09_Governance-Documentation/README]] | ADRs and governance |
| System design | [[10_System-Design-Interviews/README]] | design drills |
| Case studies | [[11_Real-World-Case-Studies/README]] | architecture autopsies |
| Enterprise | [[12_Enterprise-Architecture/README]] | business-to-technology architecture |
| AI | [[13_AI-Architecture/README]] | enterprise AI and agentic systems |
| Revision | [[99_Revision/Study Plan]] | adaptive practice |

## Capability dashboard

~~~dataview
TABLE WITHOUT ID
  file.link as "Area",
  difficulty as "Difficulty",
  mastery_stage as "Stage",
  reviewed as "Reviewed",
  "sr-due" as "Due"
FROM "Architect"
WHERE type IN ("note", "architecture-problem", "practice")
SORT date("sr-due") ASC
LIMIT 30
~~~

## Active practice

~~~tasks
not done
path includes Architect
sort by due
limit 25
~~~

## Plugin responsibilities

- **Dataview:** dashboards, indexes and derived analytics.
- **Tasks:** actionable practice and review work.
- **Templater:** repeatable ADR, architecture and interview creation.
- **Excalidraw:** C4, runtime, state and failure diagrams when visual reasoning adds value.

## Operating rule

> **Do not add infrastructure because it is familiar. Add it because a quantified requirement, failure mode, organizational constraint or measured bottleneck demands it.**


## Knowledge System Integration

- [[00 - Knowledge System/README|Knowledge System]] — shared learning model
- [[Evidence/Architecture Decisions/README|Architecture Decisions]] — durable ADR evidence
- [[Evidence/README|Evidence]] — failure and evaluation records
- [[Build Lab/README|Build Lab]] — systems to design, defend and evolve
