---
title: Architecture Decision Framework
type: guide
category: Architect
tags:
  - architecture
  - decision-making
  - trade-offs
  - system-design
---

# Architecture Decision Framework

> Architecture is the chain of constraints, decisions, trade-offs and evidence—not a collection of technologies.

## The 8-step loop

1. **Clarify the outcome** — what must the system enable?
2. **Quantify constraints** — traffic, latency, availability, data size, consistency, cost, team boundaries.
3. **State quality attributes** — turn vague NFRs into measurable scenarios.
4. **Choose the simplest viable shape** — do not distribute until a constraint requires it.
5. **Identify bottlenecks and failure modes** — what breaks first and how?
6. **Compare alternatives** — include at least one simpler option and one scale-oriented option.
7. **Record the decision** — use [[_templates/ADR-Template]].
8. **Define evidence** — metrics, load tests, architecture fitness functions, operational signals.

## Decision canvas

| Question | Evidence |
|---|---|
| What problem are we solving? | |
| What scale must we support? | |
| Which constraints are hard? | |
| Which quality attributes matter most? | |
| What is the simplest viable architecture? | |
| What alternative did we reject? | |
| What failure mode worries us most? | |
| What operational burden are we accepting? | |
| How will we validate the decision? | |
| What would cause us to revisit it? | |

## Trade-off rule

Never write:

> "Microservices are more scalable."

Write:

> "We choose service decomposition because team autonomy and independent scaling are hard requirements; we accept distributed tracing, deployment coordination and eventual consistency as costs."

Every architecture choice should answer:

**Why this? Why not the simpler alternative? What does it cost? What evidence would falsify it?**

## Architecture boundaries

Distinguish:

- **Business boundary** — bounded context / capability.
- **Runtime boundary** — process, service, function.
- **Data boundary** — ownership and consistency.
- **Deployment boundary** — independent release/scaling.
- **Team boundary** — ownership and cognitive load.

A boundary should exist because one or more constraints justify it.

## Related

[[00 - System Design Decision Tree]] · [[00 - NFR Decision Matrix]] · [[00 - Architecture Trade-off Matrix]] · [[00 - Interview Mode]]
