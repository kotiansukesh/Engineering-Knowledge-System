---
title: "Saga, Outbox & Inbox"
category: "Design Patterns & Building Blocks"
tags: [patterns, microservices, saga, outbox, inbox, idempotency, kafka, spring]
created: 2026-09-03
completed: false
---

# Saga, Outbox & Inbox

> **Intent:** Keep cross-service writes consistent without 2PC — saga sequences local transactions with compensations; outbox guarantees the event actually leaves; inbox + idempotency keys make redelivery safe.

## 1. When to Use
- Multi-service business flow (order → pay → ship) needing eventual consistency.
- Any producer that must not lose events on crash (DB commit and publish must be atomic).

**When NOT:** single-service transaction covers it — don't pay saga cost; or strict immediate consistency required (redesign the boundary first).

## 2. Spring Boot Example (outbox + choreography)

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
    ledger.apply(e);                         // local TX
    inbox.save(new Inbox(e.eventId()));      // same TX
}
// Compensation on failure: PaymentFailed → cancelOrder (reverse TX)
```

Orchestration (Temporal/Camunda) when the flow has branches, timeouts, human steps; choreography (events) when the flow is linear.

## 3. Pros / Cons
| Pros | Cons |
|---|---|
| No distributed locks; services stay autonomous | Eventual consistency — UI must handle pending states |
| Outbox = no lost events on crash | Saga debugging needs correlation IDs + tracing |
| Redelivery-safe via inbox | Compensation logic is real code to maintain |

## 4. Vs
- **Vs 2PC/XA:** 2PC blocks all participants on coordinator failure; saga never blocks, compensates instead.
- **Vs dual-write (DB then Kafka):** dual-write loses events on crash between the two; outbox makes it one atomic commit.

## 5. Interview Q&A
**Q: Choreography vs orchestration?**
A: Choreography (events, no center) for simple linear flows; orchestration (coordinator owns the state machine) for branches, timeouts, retries with deadlines.

**Q: How do you guarantee at-least-once without duplicates hurting?**
A: Outbox for publish guarantee + consumer-side inbox/eventId dedupe + idempotency key on the business op (e.g. orderId unique).

**Q: What breaks most often?**
A: Missing compensation paths and out-of-order events — version events, keep handlers backward-compatible, test the rollback flow.

## 6. Pitfalls
- Publishing before commit, or after commit without outbox — both lose events.
- Non-idempotent consumer (double-charge on redelivery).
- Saga without observability: no sagaId in every log/span → undebuggable.

## 7. Links
- [[05_Decomposition-Bounded-Context|Decomposition]] · [[../../07_Integration-APIs/03_Kafka-Messaging-Idempotency|Kafka-Idempotency]] · [[../../06_Data-Architecture/03_Event-Sourcing-CQRS|ES-CQRS]] · [[02_Resilience-Circuit-Breaker-Retry|Resilience]]

<!-- Concept: atomic publish via outbox, safe retry via inbox, rollback via compensation — never 2PC. -->
