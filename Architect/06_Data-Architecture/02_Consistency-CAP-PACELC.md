---
title: Consistency, CAP & PACELC
category: Architect/06_Data-Architecture
tags:
- data
- cap
- pacelc
- consistency
- distributed-systems
created: 2026-09-03
completed: false
reviewed: ''
sr-due: ''
difficulty: Medium
excalidraw: ''
source: ''
type: note
weeks: ''
---

## 🎯 Intent
Make consistency-vs-availability trade-offs explicit per operation — not per database. CAP (partition → choose C or A) + PACELC (else → choose Latency or Consistency) turns trivia into a design tool.

## 💡 Why It Matters
- **Interview signal**: "Is CAP 'pick two of three'?" and "How do you handle conflicts in AP mode?" — outdated framing vs per-operation design
- **Real cost**: One global consistency setting overpays latency on reads, risks availability on writes
- **Operation-level design**: Checkout fails rather than oversell; stale catalogue page costs nothing — choose per operation

## 🧩 Diagram: CAP + PACELC Decision Tree
```mermaid
graph TD
    W[Write Arrives] --> P{Partition?}
    P -->|yes, payment ledger| C1[Choose Consistency: Fail Fast]
    P -->|yes, catalogue view| A1[Choose Availability: Serve Stale]
    P -->|no partition| E{Else (PACELC)}
    E -->|checkout commit| LC[Latency Yield to C: Sync Quorum]
    E -->|product read| LL[C Yield to Latency: Edge Cache]
    style C1 fill:#ffebee
    style A1 fill:#e8f5e9
    style LC fill:#fff3e0
    style LL fill:#e3f2fd
```

## 💻 Code: Consistency Stance as Code (Java 25 + Resilience4j)
```java
// Strong-consistency operation: optimistic lock on the aggregate
@Entity
class Inventory {
    @Version private long version; // conflict → OptimisticLockException → retry with backoff
    private int stock;
}

// Availability-leaning operation: explicit, documented staleness window
@Cacheable(value = "catalogue", key = "#id")
public ProductDto view(String id) {
    return repo.find(id); // TTL = accepted staleness, not an accident
}

// Partition stance is code, not config: fail-fast vs serve-last-known
// Resilience4j fallback choice made per use case
@Bean
public Fallback<ProductDto> catalogueFallback() {
    return (id, ex) -> {
        // AP stance: serve stale from cache
        return cache.get(id);
    };
}

@Bean
public Fallback<PaymentResult> paymentFallback() {
    return (cmd, ex) -> {
        // CP stance: fail fast, don't oversell
        throw new PaymentUnavailableException("Partition: failing fast");
    };
}
```

## ✅ When to Use / ❌ When NOT to Use
| Scenario | Use? | Reason |
|---|---|---|
| Every distributed decision | ✅ | Checkout (C) vs catalogue (A) vs cart (between) |
| PACELC in normal operation | ✅ | Sync cross-region write (C, slow) vs local + async replicate (L, stale) |
| Interview framing | ✅ | "Depends on operation" beats "our DB is CP/AP" |
| One global setting for all ops | ❌ | Overpays latency on reads, risks availability on writes |

## ⚖️ Trade-offs
| Dimension | Strong Consistency (CP) | Eventual Consistency (AP) |
|---|---|---|
| **Reasoning** | Simple, no reconciliation | Requires conflict resolution |
| **Availability** | Lower (fails on partition) | Higher (serves stale) |
| **Latency** | Higher (sync quorum) | Lower (local/edge) |
| **Conflict Resolution** | None needed | Idempotency keys, versioning, CRDTs, business queues |
| **UX Copy** | "Failed — try again" | "Usually up to date" (honest) |

**Decision rule**: Checkout = CP (fail rather than oversell). Catalogue = AP (serve stale). Cart = AP (merge later via CRDT/last-write).

## 🆚 Vs. Alternatives
| Alternative | When to Choose | Decision Rule |
|---|---|---|
| **Store Bias** | Stores bias toward C or A, but operations decide | You can do eventual on Postgres (read replicas) and strong-ish on NoSQL (conditional writes) |
| **CQRS + Event Sourcing** | Mixed consistency implementation | CQRS = consistent writes + eventually-consistent reads. See [[03_Event-Sourcing-CQRS]] |

## ⚠️ Pitfalls
1. **One global consistency setting** — overpays latency on reads, risks availability on writes
2. **"Eventual" without a bound** — define staleness SLAs (p99 lag < 5s) and alert on them
3. **Assuming network won't partition** — VPC AZ failure says hi
4. **CAP as "pick two of three"** — outdated framing; partitions happen, real choice is C-vs-A *during* partition, L-vs-C *otherwise*

## 🎤 Interview Q&A (Senior Depth)

**Q1: "Is CAP 'pick two of three'?"**
> **Answer**: Outdated framing. Partitions happen — the real choice is C-vs-A *during* a partition, and L-vs-C *otherwise* (PACELC). Design per operation, not per database. **Rejected**: "We chose CP" — which operation? All of them?

**Q2: "How do you handle conflicts in AP mode?"**
> **Answer**: Idempotency keys + versioning; merge rules declared upfront (last-writer-wins with vector clocks, CRDTs, or business reconciliation queues). **Metric**: Conflict rate < 0.1%; reconciliation queue drain < 5min. **Rejected**: "Last write wins" — loses data silently.

**Q3: "How do you implement per-operation consistency in Spring?"**
> **Answer**: `@Transactional` + `@Version` for CP (optimistic lock → retry). `@Cacheable` with explicit TTL for AP (staleness = documented contract). Resilience4j fallback per use case: fail-fast (CP) vs serve-stale (AP). **Rejected**: Global `spring.jpa.properties.hibernate.lock.timeout` — one size fits none.

**Q4: "What's the latency cost of CP vs AP in normal operation (PACELC)?"**
> **Answer**: CP = sync quorum (cross-region ~50-100ms). AP = local write + async replicate (~5-10ms). Difference = 5-10× latency. Choose CP only where inconsistency cost > latency cost (payments, inventory). **Metric**: p99 latency budget per operation.

**Q5: "How do you test partition behaviour?"**
> **Answer**: Chaos Mesh / Litmus: inject partition between service and DB; assert CP operations fail fast, AP operations serve stale with documented TTL. Run in staging nightly. **Rejected**: "We don't test partitions" — hope is not a strategy.

## 🔗 Related
- [[01_SQL-vs-NoSQL-Selection]] · [[03_Event-Sourcing-CQRS]] · [[../05_DDD-Modeling/05_Domain-Events|Domain Events]]