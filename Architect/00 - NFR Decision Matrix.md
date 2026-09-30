---
title: NFR Decision Matrix
type: guide
category: Architect
tags:
  - architecture
  - nfr
  - scalability
  - reliability
---

# NFR Decision Matrix

> NFRs become useful when expressed as measurable scenarios.

## Quality attribute → architecture lever

| NFR | First questions | Typical levers | Main cost |
|---|---|---|---|
| Latency | p50/p95/p99? payload? region? | caching, locality, async, indexing | staleness/complexity |
| Availability | target? dependency budget? | replication, failover, isolation | cost/operational complexity |
| Scalability | what scales: reads, writes, storage? | partitioning, stateless compute, queues | coordination |
| Consistency | what must never disagree? | transactions, quorum, ownership | latency/availability |
| Durability | RPO/RTO? | replication, WAL, backups | storage/cost |
| Security | threat model? trust boundaries? | authN/Z, encryption, isolation | latency/complexity |
| Operability | who owns it at 2am? | automation, observability, runbooks | engineering effort |
| Cost | fixed vs variable? | tiering, caching, autoscaling | performance/complexity |

## Scenario format

**Source → stimulus → environment → measurable response → threshold**

Example:

> During a 10× traffic spike in one region, the checkout API must maintain p99 < 500 ms for 99.9% of requests while preserving payment correctness.

This is more useful than "the system must be scalable."

## Constraint tension map

| Tension | Question |
|---|---|
| Consistency ↔ availability | Can stale data be tolerated? |
| Latency ↔ durability | Can acknowledgement precede durable persistence? |
| Cost ↔ redundancy | What failure probability justifies another replica? |
| Throughput ↔ ordering | Is global order really required? |
| Freshness ↔ cache hit rate | How stale can data become? |
| Isolation ↔ simplicity | Does failure containment justify another boundary? |

## Review questions

- What is the measured target?
- Which component owns the SLO?
- What happens at 2×, 10× and 100× load?
- Which dependency fails first?
- What is the degraded mode?
- How is correctness recovered after failure?
