---
title: System Design Decision Tree
type: guide
category: Architect
tags:
  - system-design
  - decision-tree
  - interviews
---

# System Design Decision Tree

## 1. Requirements first

- Who are the users?
- What are the critical use cases?
- Read/write ratio?
- Peak traffic?
- Data size and growth?
- Latency target?
- Availability target?
- Consistency requirement?
- Security/compliance constraints?
- Regional requirements?
- Recovery objectives?

## 2. Back-of-envelope

Estimate:

- requests/sec;
- peak multiplier;
- storage/day and storage/year;
- bandwidth;
- cache working set;
- queue throughput;
- replication overhead.

Record assumptions explicitly. Wrong assumptions are easier to fix than invisible assumptions.

## 3. Choose the dominant access pattern

| Dominant shape | Candidate |
|---|---|
| Read-heavy key lookup | Cache + KV/RDBMS |
| Ordered feed | Precompute/fan-out + cursor |
| Large media | Object store + CDN |
| Full-text search | Search index |
| Geo-nearby | Spatial index / geohash / S2 |
| Async workflow | Queue/stream + workers |
| Strict transactional workflow | Relational DB + transaction boundary |
| Analytics | Stream/batch pipeline + columnar store |
| High-cardinality metrics | Time-series/metrics system |

## 4. Choose consistency deliberately

Ask:

- What must be strongly consistent?
- What may be stale?
- What can be reconciled?
- Where is the transaction boundary?
- What happens during retry or duplicate delivery?

## 5. Choose communication

- Synchronous HTTP/gRPC when the caller needs the result now.
- Async messaging when work can be decoupled.
- Streaming when ordered event flow matters.
- WebSocket/SSE when clients need server-initiated updates.

## 6. Choose storage

Do not choose a database by popularity.

Choose based on:

- access pattern;
- consistency;
- transaction needs;
- scale;
- operational maturity;
- query flexibility;
- cost.

See 00 - NFR Decision Matrix and 00 - Architecture Trade-off Matrix.

## 7. Failure-first design

For every critical dependency:

**timeout → retry policy → idempotency → circuit breaker/bulkhead → fallback/degradation → observability**

Do not add retries without considering amplification.

## 8. Interview sequence

**Requirements → estimates → API/contracts → high-level architecture → data model → bottleneck → failure mode → scaling → security → observability → trade-offs**

## Anti-pattern

Do not start with:

> "Use Kafka + Kubernetes + Redis + microservices."

Start with constraints and derive the components.
