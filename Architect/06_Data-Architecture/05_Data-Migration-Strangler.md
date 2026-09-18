---
title: "Data Migration & Strangler Fig"
category: "Data Architecture"
tags: [data, migration, strangler-fig, modernization, dual-write]
created: 2026-09-03
completed: false
---
## Why it Matters

Big-bang migrations bet the company on one release day; strangler bets small amounts repeatedly. The technique that matters most is the *facade with a flag*: route by capability, dark-read the new store, compare, then shift traffic in percentages with instant rollback. Migrations fail in the transition, not the destination, so the design is about the transition.

## Diagram

```mermaid
graph TD
 CL[Client] --> FA[Facade / ACL: route by flag]
 FA -->|flag off| L[Legacy store: SOT until cutover]
 FA -->|flag on| N[New service + own schema]
 L -.|dual-write or CDC backfill|→ N
 FA -.dark read: diff + reconcile.-> N
 N -->|shift reads → writes → retire| DONE[legacy deleted, date scheduled]
```

## Code

```java
// Strangler facade: route by capability flag, compare results (dark read)
@Service class OrderFacade {
 public OrderDto get(long id) {
 if (flags.newRead("orders", id)) return newStore.find(id); // migrated path
 OrderDto legacy = legacyStore.find(id);
 asyncCompare(legacy, newStore.findQuietly(id)); // reconciliation log, not blocking
 return legacy;
 }
 // Dual-write during transition: legacy = SOT until cutover date
 @Transactional public void save(Order o) {
 legacyStore.save(o);
 outbox.publish(new OrderMigrated(o)); // new store consumes → eventually consistent copy
 }
}
```
Migration mechanics: Flyway expand→migrate→contract (add nullable col → backfill → switch code → drop old); cutover behind feature flag with instant rollback (flag off).

## When to use / not

- Legacy monolith/DB being decomposed into [[05_DDD-Modeling/02_Bounded-Contexts|bounded contexts]] or [[03_Architecture-Styles/03_Microservices|services]].
- DB engine moves (Oracle → Postgres) or schema reshapes too big for one deploy.
- Any migration where rollback must stay possible until the last mile.

Playbook: 1) facade (anti-corruption layer) 2) carve one seam 3) dual-write + verify 4) shift reads 5) shift writes 6) retire + delete.

## Trade-offs

| Pros | Cons |
|---|---|
| Zero-downtime, reversible per seam | Dual-write period doubles complexity + monitoring |
| Value ships incrementally (one context at a time) | Reconciliation tooling is throwaway code (budget it) |
| Risk concentrated in small, reviewable steps | Lingering "temporary" facades if retirement isn't scheduled |

## Vs

- **Vs big-bang rewrite:** big-bang bets the company on one release; strangler bets small amounts repeatedly, with a facade tax.
- **Vs [[03_Event-Sourcing-CQRS|event-sourced rebuild]]:** sourcing replays history; strangler migrates live traffic, combine: backfill from legacy dump, then catch up via events.

## Pitfalls

- No retirement date, strangler becomes permanent scaffolding.
- Migrating data without migrating *ownership* (still one shared DB at the end).
- Backfill without idempotency → duplicates on retry; backfill in batches with checkpoints.

## Interview q&a

**Q: How do you prove the new store is correct before cutover?**
A: Dark reads + diff logging (sample % traffic, compare, alert on divergence), reconciliation batch jobs (row counts, checksums), then canary % shift with rollback flag.

**Q: Dual-write or change-data-capture?**
A: CDC (Debezium) preferred, no app-code dual-write bugs, ordered, replayable. Dual-write only when CDC can't reach the legacy source.

## Related

- [[01_SQL-vs-NoSQL-Selection]] · [[05_DDD-Modeling/03_Context-Mapping|Context Mapping (ACL)]] · [[03_Architecture-Styles/06_Monolith-vs-Modular-Choice-Guide|Choice Guide]]

# Data Migration & Strangler fig

> **Intent:** Modernise without big-bang rewrites: strangler incrementally routes traffic/data from legacy to new (facade → migrate → retire), with dual-write/read-reconciliation keeping both worlds consistent until cutover.
> Watch: [Concept && Coding, SAGA, Strangler, CQRS](https://www.youtube.com/watch?v=qGlUKtjqaEQ)
