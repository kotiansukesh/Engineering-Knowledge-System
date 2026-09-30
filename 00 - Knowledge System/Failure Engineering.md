---
title: "Failure Engineering"
type: reference
category: "Knowledge System"
status: active
---

# Failure Engineering

Failure analysis is a cross-domain engineering primitive.

## Failure record

1. Trigger
2. Preconditions
3. Blast radius
4. Detection signal
5. Degraded behavior
6. Recovery
7. Preventive control
8. Test/experiment
9. Evidence
10. Revisit condition

## Failure families

- Java/JVM: memory pressure, contention, GC pauses, thread starvation.
- Backend: dependency outage, data inconsistency, queue backlog, retry storm.
- AI: retrieval miss, hallucination, tool failure, prompt injection, runaway cost.
- Architecture: wrong boundary, bottleneck, cascading failure, operational blind spot.

See [[../Evidence/Failure Experiments/README]] for the evidence store.
