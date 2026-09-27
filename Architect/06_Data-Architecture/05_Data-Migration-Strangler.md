---
title: Data Migration & Strangler Fig
category: Architect/06_Data-Architecture
tags:
- cdc
- concept/cqrs
- concept/event-sourcing
- concept/polyglot-persistence
- concept/sql-vs-nosql
- data
- difficulty/hard
- dual-write
- migration
- modernization
- pattern/data-architecture
- strangler-fig
created: 2026-09-03
completed: false
reviewed: '2026-09-19'
sr-due: '2026-10-03'
difficulty: Hard
excalidraw: ''
source: ''
type: note
weeks: ''
---



## 🎯 Intent
Modernise without big-bang rewrites: Strangler Fig incrementally routes traffic/data from legacy to new (facade → migrate → retire), with dual-write/read-reconciliation keeping both worlds consistent until cutover.

## 💡 Why It Matters
- **Interview signal**: "How do you prove the new store is correct before cutover?" and "Dual-write or CDC?" — big-bang bets the company on one release; strangler bets small amounts repeatedly
- **Transition design**: Migrations fail in the transition, not the destination — the design is about the transition
- **Reversibility**: Facade with a flag enables instant rollback (flag off) until retirement date

## 🧩 Diagram: Strangler Fig Migration Flow
```mermaid
graph TD
    CL[Client] --> FA[Facade / ACL: Route by Flag]
    FA -->|flag off| L[Legacy Store: SOT Until Cutover]
    FA -->|flag on| N[New Service + Own Schema]
    L -.dual-write or CDC backfill.→ N
    FA -.dark read: diff + reconcile.→ N
    N -->|shift reads → writes → retire| DONE[Legacy Deleted, Date Scheduled]
    style FA fill:#e3f2fd
    style L fill:#fff3e0
    style N fill:#e8f5e9
```

## 💻 Code: Strangler Facade with Dark Reads (Java 25 + Spring)
```java
// Strangler facade: route by capability flag, compare results (dark read)
@Service
class OrderFacade {
    public OrderDto get(long id) {
        if (flags.newRead("orders", id)) return newStore.find(id); // migrated path
        OrderDto legacy = legacyStore.find(id);
        asyncCompare(legacy, newStore.findQuietly(id)); // reconciliation log, not blocking
        return legacy;
    }

    // Dual-write during transition: legacy = SOT until cutover date
    @Transactional
    public void save(Order o) {
        legacyStore.save(o);
        outbox.publish(new OrderMigrated(o)); // new store consumes → eventually consistent copy
    }
}

// Migration mechanics: Flyway expand→migrate→contract
// 1) Add nullable col → 2) Backfill → 3) Switch code → 4) Drop old
// Cutover behind feature flag with instant rollback (flag off)
```

## ✅ When to Use / ❌ When NOT to Use
| Scenario | Use? | Reason |
|---|---|---|
| Legacy monolith/DB decomposed into bounded contexts/services | ✅ | See [[../05_DDD-Modeling/02_Bounded-Contexts]] |
| DB engine move (Oracle → Postgres) or schema reshape too big for one deploy | ✅ | Incremental, reversible |
| Any migration where rollback must stay possible until last mile | ✅ | Facade + flag = instant rollback |
| Greenfield system | ❌ | No legacy to strangle |

**Playbook**: 1) Facade (ACL) 2) Carve one seam 3) Dual-write + verify 4) Shift reads 5) Shift writes 6) Retire + delete.

## ⚖️ Trade-offs
| Dimension | Pros | Cons |
|---|---|---|
| **Zero-downtime** | Reversible per seam | **Dual-write period** doubles complexity + monitoring |
| **Incremental value** | One context at a time | **Reconciliation tooling** is throwaway code (budget it) |
| **Risk concentration** | Small, reviewable steps | **Lingering "temporary" facades** if retirement not scheduled |

## 🆚 Vs. Alternatives
| Alternative | When to Choose | Decision Rule |
|---|---|---|
| **Big-bang rewrite** | Never (almost) | Big-bang bets company on one release; strangler bets small amounts repeatedly |
| **Event-sourced rebuild** | Audit + replay needed | Sourcing replays history; strangler migrates live traffic. Combine: backfill from legacy dump, then catch up via events |

## ⚠️ Pitfalls
1. **No retirement date** — strangler becomes permanent scaffolding
2. **Migrating data without migrating ownership** — still one shared DB at the end
3. **Backfill without idempotency** → duplicates on retry; backfill in batches with checkpoints
4. **Dual-write in request path** — prefer CDC (Debezium): no app-code bugs, ordered, replayable

## 🎤 Interview Q&A (Senior Depth)

**Q1: "How do you prove the new store is correct before cutover?"**
> **Answer**: Dark reads + diff logging (sample % traffic, compare, alert on divergence) + reconciliation batch jobs (row counts, checksums) + canary % shift with rollback flag. **Metric**: Divergence rate < 0.01% over 1M dark reads. **Rejected**: "Trust the tests" — production data differs from test data.

**Q2: "Dual-write or change-data-capture?"**
> **Answer**: CDC (Debezium) preferred — no app-code dual-write bugs, ordered, replayable. Dual-write only when CDC can't reach legacy source. **Trade-off**: CDC adds infra; dual-write adds code complexity. **Rejected**: "Dual-write is simpler" — it's simpler until it isn't (race conditions, partial failures).

**Q3: "How do you handle the facade becoming permanent?"**
> **Answer**: Schedule retirement date in ADR; flag = temporary by design. If retirement slips, escalate as architectural debt. Budget throwaway reconciliation tooling explicitly. **Rejected**: "We'll clean it up later" — later never comes.

**Q4: "What's the Flyway expand→migrate→contract pattern?"**
> **Answer**: 1) Expand: add nullable column / new table. 2) Migrate: backfill data (idempotent batches with checkpoints). 3) Contract: switch code to new column, drop old. Each step deployable independently. **Metric**: Zero-downtime per step.

**Q5: "How do you migrate a high-traffic table with zero downtime?"**
> **Answer**: 1) Create new table + dual-write (CDC preferred). 2) Backfill in batches (10k rows, checkpoint every batch). 3) Dark read compare (1% → 10% → 100%). 4) Switch reads via flag. 5) Switch writes. 6) Drop old. **Rollback**: Flag off at any step before 5. **Rejected**: `ALTER TABLE` + hope — locks table, causes outage.

## 🔗 Related
- [[01_SQL-vs-NoSQL-Selection]] · [[../05_DDD-Modeling/03_Context-Mapping|Context Mapping (ACL)]] · [[../03_Architecture-Styles/06_Monolith-vs-Modular-Choice-Guide|Choice Guide]]