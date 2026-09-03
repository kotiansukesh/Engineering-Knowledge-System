---
title: "Data Migration & Strangler Fig"
category: "Data Architecture"
tags: [data, migration, strangler-fig, modernization, dual-write]
created: 2026-09-03
completed: false
---

# Data Migration & Strangler Fig

> **Intent:** Modernise without big-bang rewrites: strangler incrementally routes traffic/data from legacy to new (facade → migrate → retire), with dual-write/read-reconciliation keeping both worlds consistent until cutover.

## 1. When to Use
- Legacy monolith/DB being decomposed into [[05_DDD-Modeling/02_Bounded-Contexts|bounded contexts]] or [[03_Architecture-Styles/03_Microservices|services]].
- DB engine moves (Oracle → Postgres) or schema reshapes too big for one deploy.
- Any migration where rollback must stay possible until the last mile.

Playbook: 1) facade (anti-corruption layer) 2) carve one seam 3) dual-write + verify 4) shift reads 5) shift writes 6) retire + delete.

## 2. Spring Boot Example

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

## 3. Pros / Cons
| Pros | Cons |
|---|---|
| Zero-downtime, reversible per seam | Dual-write period doubles complexity + monitoring |
| Value ships incrementally (one context at a time) | Reconciliation tooling is throwaway code (budget it) |
| Risk concentrated in small, reviewable steps | Lingering "temporary" facades if retirement isn't scheduled |

## 4. Vs
- **Vs big-bang rewrite:** big-bang bets the company on one release; strangler bets small amounts repeatedly — with a facade tax.
- **Vs [[03_Event-Sourcing-CQRS|event-sourced rebuild]]:** sourcing replays history; strangler migrates live traffic — combine: backfill from legacy dump, then catch up via events.

## 5. Interview Q&A
**Q: How do you prove the new store is correct before cutover?**
A: Dark reads + diff logging (sample % traffic, compare, alert on divergence), reconciliation batch jobs (row counts, checksums), then canary % shift with rollback flag.

**Q: Dual-write or change-data-capture?**
A: CDC (Debezium) preferred — no app-code dual-write bugs, ordered, replayable. Dual-write only when CDC can't reach the legacy source.

## 6. Pitfalls
- No retirement date — strangler becomes permanent scaffolding.
- Migrating data without migrating *ownership* (still one shared DB at the end).
- Backfill without idempotency → duplicates on retry; backfill in batches with checkpoints.

## 7. Links
- [[01_SQL-vs-NoSQL-Selection]] · [[05_DDD-Modeling/03_Context-Mapping|Context Mapping (ACL)]] · [[03_Architecture-Styles/06_Monolith-vs-Modular-Choice-Guide|Choice Guide]]

<!-- Concept: strangler = never stop the world; each seam migrates behind a flag, proves itself in the dark, then takes traffic. -->
