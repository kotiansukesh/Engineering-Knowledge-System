---
title: "Saga, Outbox & Inbox"
pattern: 6
category: "Design Patterns & Building Blocks"
tags: [patterns, microservices, saga, outbox, inbox, idempotency, kafka, spring]
created: 2026-09-03
completed: false
reviewed: ""
sr-due: ""
difficulty: Hard
problems-solved: []
problems-solved-dates: {}
excalidraw: ""
---
## Why it Matters

2PC across services blocks and fails; pretending you don't need distributed transactions silently loses events. Saga + outbox + inbox is the honest answer: each step commits locally, the outbox guarantees the event escapes the crash, and consumer-side dedupe makes redelivery harmless. It is the substrate that makes eventual consistency safe enough for money.

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

| Pros | Cons |
|---|---|
| No distributed locks; services stay autonomous | Eventual consistency, UI must handle pending states |
| Outbox = no lost events on crash | Saga debugging needs correlation IDs + tracing |
| Redelivery-safe via inbox | Compensation logic is real code to maintain |

## Vs

- **Vs 2PC/XA:** 2PC blocks all participants on coordinator failure; saga never blocks, compensates instead.
- **Vs dual-write (DB then Kafka):** dual-write loses events on crash between the two; outbox makes it one atomic commit.

## Pitfalls

- Publishing before commit, or after commit without outbox, both lose events.
- Non-idempotent consumer (double-charge on redelivery).
- Saga without observability: no sagaId in every log/span → undebuggable.

## Interview q&a

**Q: Choreography vs orchestration?**
A: Choreography (events, no center) for simple linear flows; orchestration (coordinator owns the state machine) for branches, timeouts, retries with deadlines.

**Q: How do you guarantee at-least-once without duplicates hurting?**
A: Outbox for publish guarantee + consumer-side inbox/eventId dedupe + idempotency key on the business op (e.g. orderId unique).

**Q: What breaks most often?**
A: Missing compensation paths and out-of-order events, version events, keep handlers backward-compatible, test the rollback flow.

## Related

- [[05_Decomposition-Bounded-Context|Decomposition]] · [[Architect/07_Integration-APIs/Kafka Messaging and Idempotency.md|Kafka-Idempotency]] · [[../../06_Data-Architecture/03_Event-Sourcing-CQRS|ES-CQRS]] · [[02_Resilience-Circuit-Breaker-Retry|Resilience]]

# Saga, Outbox & Inbox

> **Intent:** Keep cross-service writes consistent without 2PC, saga sequences local transactions with compensations; outbox guarantees the event actually leaves; inbox + idempotency keys make redelivery safe.
> Watch: [ByteMonk, Saga Pattern, Distributed Transactions](https://www.youtube.com/watch?v=d2z78guUR4g)
