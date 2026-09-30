---
title: Saga, Outbox & Inbox
category: Architect/04_Design-Patterns-Building-Blocks
tags:
- company/youtube
- difficulty/hard
- idempotency
- inbox
- kafka
- microservices
- outbox
- pattern/cloud
- pattern/enterprise
- pattern/integration
- pattern/resilience
- pattern/saga
- patterns
- saga
- spring
created: 2026-09-03
completed: false
reviewed: '2026-09-20'
sr-due: '2026-10-04'
difficulty: Hard
excalidraw: ''
source: ''
type: note
weeks: ''

---






## Why it Matters

2PC across services blocks and fails; pretending you don't need distributed transactions silently loses events. Saga + outbox + inbox is the honest answer: each step commits locally, the outbox guarantees the event escapes the crash, and consumer-side dedupe makes redelivery harmless. It is the substrate that makes eventual consistency safe enough for money.

## Problems
### System Design Problem: Saga, Outbox & Inbox

**Requirements:**
- Functional: Core capabilities for saga, outbox & inbox
- Non-functional (SLOs): Latency < 100ms p99, Availability 99.9%, Horizontal scalability

**Constraints:**
- Scale: Handle 10x growth without redesign
- Consistency: Appropriate model for domain (strong/eventual)
- Latency budget: p99 < 100ms for read paths

**API / Interfaces:**
- Primary: REST/gRPC endpoints for core operations
- Internal: Service-to-service contracts
- Events: Domain events for async integration

## Diagram

```mermaid
graph LR
 O[Order-Svc: order row + outbox row, one TX] --> OB[(outbox)]
 OB --> R[Relay] --> K[(Kafka)]
 K --> P[Payment-Svc]
 P -->|payment.confirmed| K2[(Kafka)]
 K2 --> S[Shipment-Svc]
 P -.|payment.failed|→ C[compensation: cancel order]
 S --> IN[inbox: dedupe by eventId]
```

## Code

```java
// Outbox: same local TX writes order row + outbox row
@Transactional
public Order place(Cart c) {
 Order o = orders.save(new Order(c)); // business write
 outbox.save(new Outbox("order.placed", o.getId(), toJson(o))); // same TX — atomic
 return o;
}
// Relay: polls outbox → Kafka, marks sent (or Debezium CDC tails the table)

// Consumer: inbox check first, then work
@Transactional
public void onPayment(PaymentEvent e) {
 if (inbox.exists(e.eventId())) return; // redelivery guard
 ledger.apply(e); // local TX
 inbox.save(new Inbox(e.eventId())); // same TX
}
// Compensation on failure: PaymentFailed → cancelOrder (reverse TX)
```
Orchestration (Temporal/Camunda) when the flow has branches, timeouts, human steps; choreography (events) when the flow is linear.

## When to use / not

- Multi-service business flow (order → pay → ship) needing eventual consistency.
- Any producer that must not lose events on crash (DB commit and publish must be atomic).

**When NOT:** single-service transaction covers it, don't pay saga cost; or strict immediate consistency required (redesign the boundary first).





## Trade-offs
| Dimension | This Approach | Alternative | Trade-off Rationale | Decision Rule |
|-----------|---------------|-------------|---------------------|---------------|
| Complexity | [TBD] | [TBD] | [TBD] | [TBD] |
| Operational Burden | [TBD] | [TBD] | [TBD] | [TBD] |
| Latency | [TBD] | [TBD] | [TBD] | [TBD] |
| Consistency | [TBD] | [TBD] | [TBD] | [TBD] |
| Cost at Scale | [TBD] | [TBD] | [TBD] | [TBD] |

## Vs

- **Vs 2PC/XA:** 2PC blocks all participants on coordinator failure; saga never blocks, compensates instead.
- **Vs dual-write (DB then Kafka):** dual-write loses events on crash between the two; outbox makes it one atomic commit.

## Pitfalls

- Publishing before commit, or after commit without outbox, both lose events.
- Non-idempotent consumer (double-charge on redelivery).
- Saga without observability: no sagaId in every log/span → undebuggable.


## Pitfalls
1. Underestimating operational complexity (backups, monitoring, upgrades)
2. Ignoring failure modes (network partitions, disk failures, clock drift)
3. Not planning for 10x scale from day one
4. Skipping monitoring/alerting in MVP
5. Premature optimization before measuring
6. Dual-write without transactional outbox
7. Assuming global order in partitioned systems

## Interview q&a

**Q: Choreography vs orchestration?**
A: Choreography (events, no center) for simple linear flows; orchestration (coordinator owns the state machine) for branches, timeouts, retries with deadlines.

**Q: How do you guarantee at-least-once without duplicates hurting?**
A: Outbox for publish guarantee + consumer-side inbox/eventId dedupe + idempotency key on the business op (e.g. orderId unique).

**Q: What breaks most often?**
A: Missing compensation paths and out-of-order events, version events, keep handlers backward-compatible, test the rollback flow.


## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the core concept of Saga, Outbox & Inbox? :: **A:** [Key algorithm/architecture pattern] #flashcard

#flashcard
**Q:** When do you apply Saga, Outbox & Inbox? :: **A:** [Trigger scenarios and context] #flashcard

#flashcard
**Q:** What is the primary trade-off in Saga, Outbox & Inbox? :: **A:** [Main tension: e.g., consistency vs latency] #flashcard

#flashcard
**Q:** What breaks first at scale in Saga, Outbox & Inbox? :: **A:** [Primary bottleneck: e.g., coordination, hot keys, replication lag] #flashcard

#flashcard
**Q:** How do you handle failures in Saga, Outbox & Inbox? :: **A:** [Retry, circuit breaker, fallback, graceful degradation] #flashcard

#flashcard
**Q:** What are the key metrics to monitor for Saga, Outbox & Inbox? :: **A:** [RED: rate, errors, duration; USE: utilization, saturation, errors] #flashcard

#flashcard
**Q:** How does Saga, Outbox & Inbox scale to 10x? :: **A:** [Sharding, read replicas, async processing, caching layers] #flashcard

#flashcard
**Q:** What is the consistency model for Saga, Outbox & Inbox? :: **A:** [Strong/eventual/causal - justify with use case] #flashcard

#flashcard
**Q:** How do you test Saga, Outbox & Inbox? :: **A:** [Contract tests, chaos engineering, load tests, fault injection] #flashcard

#flashcard
**Q:** What is the operational cost of Saga, Outbox & Inbox? :: **A:** [Team expertise, tooling, on-call burden, migration risk] #flashcard

#flashcard
**Q:** When would you NOT use Saga, Outbox & Inbox? :: **A:** [Managed service covers need, simple CRUD, team lacks maturity] #flashcard

#flashcard
**Q:** What is the key design decision in Saga, Outbox & Inbox? :: **A:** [The irreversible choice that defines the architecture] #flashcard

#flashcard
**Q:** How do you migrate to Saga, Outbox & Inbox? :: **A:** [Strangler fig, dual-write, canary, feature flags] #flashcard

#flashcard
**Q:** What security considerations for Saga, Outbox & Inbox? :: **A:** [AuthZ, encryption, audit, secrets management] #flashcard

#flashcard
**Q:** How do you debug Saga, Outbox & Inbox in production? :: **A:** [Structured logging, correlation IDs, distributed tracing, SLO alerts] #flashcard


## Practice Tasks (Tasks Plugin)
- [ ] Explain the architecture from memory 📅 {{date:YYYY-MM-DD, +1}}
- [ ] Draw the system diagram without looking 📅 {{date:YYYY-MM-DD, +3}}
- [ ] Answer all Interview Q&A aloud 📅 {{date:YYYY-MM-DD, +7}}
- [ ] Review flashcards (Spaced Repetition) 📅 {{date:YYYY-MM-DD, +1}}

```tasks
not done
path includes Architect/04_Design-Patterns-Building-Blocks
sort by due
limit 10
```

## Related

- [[05_Decomposition-Bounded-Context|Decomposition]] · [[Architect/07_Integration-APIs/Kafka Messaging and Idempotency.md|Kafka-Idempotency]] · [[../../06_Data-Architecture/03_Event-Sourcing-CQRS|ES-CQRS]] · [[02_Resilience-Circuit-Breaker-Retry|Resilience]]

# Saga, Outbox & Inbox

> **Intent:** Keep cross-service writes consistent without 2PC, saga sequences local transactions with compensations; outbox guarantees the event actually leaves; inbox + idempotency keys make redelivery safe.
> Watch: [ByteMonk, Saga Pattern, Distributed Transactions](https://www.youtube.com/watch?v=d2z78guUR4g)
