---
title: Event Sourcing & CQRS
category: Architect/06_Data-Architecture
tags:
- audit
- concept/cqrs
- concept/event-sourcing
- concept/polyglot-persistence
- concept/sql-vs-nosql
- cqrs
- data
- difficulty/hard
- event-sourcing
- kafka
- pattern/cqrs
- pattern/data-architecture
- pattern/event-sourcing
- spring
created: 2026-09-03
completed: false
reviewed: '2026-09-01'
sr-due: '2026-09-15'
difficulty: Hard
excalidraw: ''
source: ''
type: note
weeks: ''

---





## 🎯 Intent
Event Sourcing: persist state *changes* as an append-only event log (the log is truth; state is a fold). CQRS: split write models (commands, invariants) from read models (queries, shape-optimised). Combine them when auditability and divergent read/write needs justify the complexity.

## 💡 Why It Matters
- **Interview signal**: "How do you handle schema evolution?" and "Where do you start?" — sourcing everything is a common anti-pattern; CQRS-lite first covers 80% of cases
- **Right sizing**: Most systems don't need current state stored so much as *how it got there* — audit, replay, time travel, divergent read shapes
- **Cost**: Eventual consistency on reads, schema evolution over immutable log (upcasting), snapshotting, projections, replay tooling — steep learning curve

## Problems
### System Design Problem: Event Sourcing & CQRS

**Requirements:**
- Functional: Core capabilities for event sourcing & cqrs
- Non-functional (SLOs): Latency < 100ms p99, Availability 99.9%, Horizontal scalability

**Constraints:**
- Scale: Handle 10x growth without redesign
- Consistency: Appropriate model for domain (strong/eventual)
- Latency budget: p99 < 100ms for read paths

**API / Interfaces:**
- Primary: REST/gRPC endpoints for core operations
- Internal: Service-to-service contracts
- Events: Domain events for async integration

## 🧩 Diagram: Event Sourcing + CQRS Flow
```mermaid
graph LR
    CMD[Command: Place Order] --> DEC[Pure Decision Function<br/>Over Past Events]
    LOG[(Append-Only Event Log)] --> DEC
    DEC -->|append + expected-version| LOG
    LOG --> PROJ[Projectors] --> V1[Read Model: Order List]
    LOG --> V2[Read Model: Analytics]
    LOG --> SNAP[Snapshots every N Events]
    style LOG fill:#e8f5e9
    style DEC fill:#e3f2fd
```

## 💻 Code: Write Side + Projectors (Java 25 + Spring + Kafka)
```java
// Write side: append events, never UPDATE state rows
record Event(long seq, String orderId, String type, String payload) {}

@Transactional
public void handle(Command c) {
    var past = log.load(c.orderId());           // rehydrate by folding
    var next = OrderDecider.apply(past, c);     // pure decision function
    log.append(next);                           // single atomic append (optimistic concurrency on seq)
    publisher.publish(next);                    // feeds read models
}

// Read side: projector builds query tables (plain JPA/Mongo docs)
@Component
class OrderProjector {
    @KafkaListener(topics = "orders.events")
    public void on(Event e) {
        views.upsert(project(e));
    }
}

// Concurrency: expected-version check on append (`WHERE seq = ?`); conflict → reload, re-decide, retry
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
**Q:** What is the core concept of Event Sourcing & CQRS? :: **A:** [Key algorithm/architecture pattern] #flashcard

#flashcard
**Q:** When do you apply Event Sourcing & CQRS? :: **A:** [Trigger scenarios and context] #flashcard

#flashcard
**Q:** What is the primary trade-off in Event Sourcing & CQRS? :: **A:** [Main tension: e.g., consistency vs latency] #flashcard

#flashcard
**Q:** What breaks first at scale in Event Sourcing & CQRS? :: **A:** [Primary bottleneck: e.g., coordination, hot keys, replication lag] #flashcard

#flashcard
**Q:** How do you handle failures in Event Sourcing & CQRS? :: **A:** [Retry, circuit breaker, fallback, graceful degradation] #flashcard

#flashcard
**Q:** What are the key metrics to monitor for Event Sourcing & CQRS? :: **A:** [RED: rate, errors, duration; USE: utilization, saturation, errors] #flashcard

#flashcard
**Q:** How does Event Sourcing & CQRS scale to 10x? :: **A:** [Sharding, read replicas, async processing, caching layers] #flashcard

#flashcard
**Q:** What is the consistency model for Event Sourcing & CQRS? :: **A:** [Strong/eventual/causal - justify with use case] #flashcard

#flashcard
**Q:** How do you test Event Sourcing & CQRS? :: **A:** [Contract tests, chaos engineering, load tests, fault injection] #flashcard

#flashcard
**Q:** What is the operational cost of Event Sourcing & CQRS? :: **A:** [Team expertise, tooling, on-call burden, migration risk] #flashcard

#flashcard
**Q:** When would you NOT use Event Sourcing & CQRS? :: **A:** [Managed service covers need, simple CRUD, team lacks maturity] #flashcard

#flashcard
**Q:** What is the key design decision in Event Sourcing & CQRS? :: **A:** [The irreversible choice that defines the architecture] #flashcard

#flashcard
**Q:** How do you migrate to Event Sourcing & CQRS? :: **A:** [Strangler fig, dual-write, canary, feature flags] #flashcard

#flashcard
**Q:** What security considerations for Event Sourcing & CQRS? :: **A:** [AuthZ, encryption, audit, secrets management] #flashcard

#flashcard
**Q:** How do you debug Event Sourcing & CQRS in production? :: **A:** [Structured logging, correlation IDs, distributed tracing, SLO alerts] #flashcard


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
| Audit/regeneration needs (finance, ledger, replay to any point) | ✅ | Log is truth; full history |
| Reads/writes scale/shape differently (write: normalised; reads: 5 denormalised views) | ✅ | CQRS splits models |
| Temporal queries ("what did order look like Tuesday?") | ✅ | Replay to point in time |
| Standard CRUD | ❌ | Current-state rows simpler, faster, tooling-rich |
| CQRS without sourcing | ⚠️ | Separate read tables fed by outbox events covers most cases |


## 🆚 Vs. Alternatives
| Alternative | When to Choose | Decision Rule |
|---|---|---|
| **State-stored + Outbox** | Reliable publishing with simple current-state | 80% benefit at 20% cost. Choose full sourcing ONLY for audit/time-travel |
| **Plain EDA** | Notifications about changes | EDA notifies; sourcing *stores* changes as truth |
| **CQRS-lite (Outbox)** | Divergent reads without audit | Start here; add sourcing only to aggregates needing history |

## ⚠️ Pitfalls
1. **Sourcing everything ("event-sourced CRUD")** — log growth + replay pain with no payoff
2. **Fat events carrying volatile data** — snapshots rot; store decision facts, not derived data
3. **GDPR erasure vs immutable log** — plan crypto-shredding/pseudonymisation upfront
4. **No snapshot strategy** — rehydration O(N) events; snapshot every N (e.g., 100) events


## Pitfalls
1. Underestimating operational complexity (backups, monitoring, upgrades)
2. Ignoring failure modes (network partitions, disk failures, clock drift)
3. Not planning for 10x scale from day one
4. Skipping monitoring/alerting in MVP
5. Premature optimization before measuring
6. Dual-write without transactional outbox
7. Assuming global order in partitioned systems

## 🎤 Interview Q&A (Senior Depth)

**Q1: "How do you handle schema evolution?"**
> **Answer**: Additive events only; upcasters (v1→v2 on read); versioned event types (`OrderPlaced_v1`, `OrderPlaced_v2`); NEVER rewrite the log. Upcaster chain runs at projector load time. **Rejected**: "Migrate events in place" — violates immutability.

**Q2: "How do rebuilds work?"**
> **Answer**: Replay log into fresh projections; snapshot every N events to bound rehydration; blue/green projectors for zero-downtime rebuilds. **Metric**: Full replay < 30min for 1M events with snapshots. **Rejected**: "Rebuild on demand" — too slow for incidents.

**Q3: "Where do you start?"**
> **Answer**: CQRS-lite first (read models via outbox events); add sourcing only to aggregates that need history. **Decision rule**: If you don't need audit/replay/temporal queries, you don't need sourcing. **Rejected**: "Start with full ES" — over-engineering.

**Q4: "How do you handle concurrent commands on same aggregate?"**
> **Answer**: Optimistic concurrency via expected-version on append (`WHERE seq = ?`). Conflict → reload past events, re-run decision function, retry. **Metric**: Conflict rate < 1%; retry success > 99%. **Rejected**: "Pessimistic lock" — kills throughput.

**Q5: "CQRS without Event Sourcing — what's the difference?"**
> **Answer**: CQRS = split write/read models. Sourcing = log is truth. CQRS without sourcing = write to DB, publish events via outbox, projectors build read models. 80% of cases need only this. **Rejected**: "They're the same" — sourcing adds immutable log + replay; CQRS doesn't require it.

## 🔗 Related
- [[02_Consistency-CAP-PACELC]] · [[../05_DDD-Modeling/05_Domain-Events|Domain Events]] · [[01_SQL-vs-NoSQL-Selection]]