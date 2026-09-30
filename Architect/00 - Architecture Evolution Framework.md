---
title: Architecture Evolution Framework
type: framework
category: Architect
tags: [architecture, evolution, migration]
---

# Architecture Evolution Framework

Real systems evolve through measured constraints.

~~~text
Current State
    ↓
Observed Requirement / Constraint
    ↓
Measured Bottleneck
    ↓
Smallest Viable Change
    ↓
Migration Strategy
    ↓
Validation
    ↓
New State
~~~

## Evolution questions

- What evidence says the current architecture is insufficient?
- Which component is actually the bottleneck?
- Can a local change solve it?
- What migration risk is introduced?
- Can old and new paths coexist?
- How do we roll back?
- What data consistency risk exists?
- What operational burden increases?

## Common transitions

- Monolith → modular monolith
- Modular monolith → selected service extraction
- Primary DB → replicas
- Single database → partitioned data
- synchronous workflow → asynchronous workers
- single region → multi-region
- legacy platform → strangler migration

## Migration checklist

- [ ] baseline metrics
- [ ] target architecture
- [ ] compatibility boundary
- [ ] data migration plan
- [ ] dual-write/reconciliation analysis
- [ ] rollback plan
- [ ] observability
- [ ] canary/cutover plan
- [ ] success criteria
- [ ] decommission plan
