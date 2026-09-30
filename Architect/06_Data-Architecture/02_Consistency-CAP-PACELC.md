---
title: Consistency, CAP & PACELC
category: Architect/06_Data-Architecture
tags:
- cap
- concept/cqrs
- concept/event-sourcing
- concept/polyglot-persistence
- concept/sql-vs-nosql
- consistency
- data
- difficulty/medium
- distributed-systems
- pacelc
- pattern/data-architecture
created: 2026-09-03
completed: false
reviewed: '2026-08-30'
sr-due: '2026-09-06'
difficulty: Medium
excalidraw: ''
source: ''
type: concept
weeks: ''

---





## 🎯 Intent
Make consistency-vs-availability trade-offs explicit per operation — not per database. CAP (partition → choose C or A) + PACELC (else → choose Latency or Consistency) turns trivia into a design tool.

## 💡 Why It Matters
- **Interview signal**: "Is CAP 'pick two of three'?" and "How do you handle conflicts in AP mode?" — outdated framing vs per-operation design
- **Real cost**: One global consistency setting overpays latency on reads, risks availability on writes
- **Operation-level design**: Checkout fails rather than oversell; stale catalogue page costs nothing — choose per operation

## Problems
### System Design Problem: Consistency, CAP & PACELC

**Requirements:**
- Functional: Core capabilities for consistency, cap & pacelc
- Non-functional (SLOs): Latency < 100ms p99, Availability 99.9%, Horizontal scalability

**Constraints:**
- Scale: Handle 10x growth without redesign
- Consistency: Appropriate model for domain (strong/eventual)
- Latency budget: p99 < 100ms for read paths

**API / Interfaces:**
- Primary: REST/gRPC endpoints for core operations
- Internal: Service-to-service contracts
- Events: Domain events for async integration

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
|

## Trade-offs
| Dimension | This Approach | Alternative | Trade-off Rationale | Decision Rule |
|-----------|---------------|-------------|---------------------|---------------|
| Complexity | [TBD] | [TBD] | [TBD] | [TBD] |
| Operational Burden | [TBD] | [TBD] | [TBD] | [TBD] |
| Latency | [TBD] | [TBD] | [TBD] | [TBD] |
| Consistency | [TBD] | [TBD] | [TBD] | [TBD] |
| Cost at Scale | [TBD] | [TBD] | [TBD] | [TBD] |

## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the core concept of Consistency, CAP & PACELC? :: **A:** [Key algorithm/architecture pattern] #flashcard

#flashcard
**Q:** When do you apply Consistency, CAP & PACELC? :: **A:** [Trigger scenarios and context] #flashcard

#flashcard
**Q:** What is the primary trade-off in Consistency, CAP & PACELC? :: **A:** [Main tension: e.g., consistency vs latency] #flashcard

#flashcard
**Q:** What breaks first at scale in Consistency, CAP & PACELC? :: **A:** [Primary bottleneck: e.g., coordination, hot keys, replication lag] #flashcard

#flashcard
**Q:** How do you handle failures in Consistency, CAP & PACELC? :: **A:** [Retry, circuit breaker, fallback, graceful degradation] #flashcard

#flashcard
**Q:** What are the key metrics to monitor for Consistency, CAP & PACELC? :: **A:** [RED: rate, errors, duration; USE: utilization, saturation, errors] #flashcard

#flashcard
**Q:** How does Consistency, CAP & PACELC scale to 10x? :: **A:** [Sharding, read replicas, async processing, caching layers] #flashcard

#flashcard
**Q:** What is the consistency model for Consistency, CAP & PACELC? :: **A:** [Strong/eventual/causal - justify with use case] #flashcard

#flashcard
**Q:** How do you test Consistency, CAP & PACELC? :: **A:** [Contract tests, chaos engineering, load tests, fault injection] #flashcard

#flashcard
**Q:** What is the operational cost of Consistency, CAP & PACELC? :: **A:** [Team expertise, tooling, on-call burden, migration risk] #flashcard

#flashcard
**Q:** When would you NOT use Consistency, CAP & PACELC? :: **A:** [Managed service covers need, simple CRUD, team lacks maturity] #flashcard

#flashcard
**Q:** What is the key design decision in Consistency, CAP & PACELC? :: **A:** [The irreversible choice that defines the architecture] #flashcard

#flashcard
**Q:** How do you migrate to Consistency, CAP & PACELC? :: **A:** [Strangler fig, dual-write, canary, feature flags] #flashcard

#flashcard
**Q:** What security considerations for Consistency, CAP & PACELC? :: **A:** [AuthZ, encryption, audit, secrets management] #flashcard

#flashcard
**Q:** How do you debug Consistency, CAP & PACELC in production? :: **A:** [Structured logging, correlation IDs, distributed tracing, SLO alerts] #flashcard


## Practice Tasks (Tasks Plugin)
- [ ] Explain the architecture from memory 📅 {{date:YYYY-MM-DD, +1}}
- [ ] Draw the system diagram without looking 📅 {{date:YYYY-MM-DD, +3}}
- [ ] Answer all Interview Q&A aloud 📅 {{date:YYYY-MM-DD, +7}}
- [ ] Review flashcards (Spaced Repetition) 📅 {{date:YYYY-MM-DD, +1}}

```tasks
not done
path includes Architect/06_Data-Architecture
sort by due
limit 10
```

---|---|---|
| Every distributed decision | ✅ | Checkout (C) vs catalogue (A) vs cart (between) |
| PACELC in normal operation | ✅ | Sync cross-region write (C, slow) vs local + async replicate (L, stale) |
| Interview framing | ✅ | "Depends on operation" beats "our DB is CP/AP" |
| One global setting for all ops | ❌ | Overpays latency on reads, risks availability on writes |


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


## Pitfalls
1. Underestimating operational complexity (backups, monitoring, upgrades)
2. Ignoring failure modes (network partitions, disk failures, clock drift)
3. Not planning for 10x scale from day one
4. Skipping monitoring/alerting in MVP
5. Premature optimization before measuring
6. Dual-write without transactional outbox
7. Assuming global order in partitioned systems

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