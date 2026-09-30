---
title: Architecture Trade-off Matrix
type: guide
category: Architect
tags:
  - architecture
  - trade-offs
  - system-design
---

# Architecture Trade-off Matrix

## Common decisions

| Decision | Simpler option | Scale-oriented option | What changes |
|---|---|---|---|
| Application | Modular monolith | Microservices | deployment + failure boundaries |
| Database | Single relational DB | Partitioned/sharded/polyglot | ownership + operational burden |
| Communication | REST | gRPC / async events | coupling + delivery semantics |
| Processing | Synchronous | Queue + workers | latency vs durability/throughput |
| Cache | No cache | Redis/CDN | freshness + invalidation |
| Search | DB queries | Search index | indexing pipeline + eventual consistency |
| IDs | DB-generated | Snowflake/ULID/range allocation | coordination + ordering |
| Files | DB blob | Object store + CDN | lifecycle + consistency |
| Multi-region | Single region | Active/passive or active/active | failover + data semantics |

## Decision rule

Choose the **simplest option that satisfies the measured constraints**.

Move right only when a concrete constraint pays for the additional operational complexity.

## Architecture review

For every proposed component ask:

1. Which requirement forces it?
2. What problem exists without it?
3. What new failure mode does it create?
4. Who operates it?
5. What metric proves it is helping?
6. Can it be removed later?
