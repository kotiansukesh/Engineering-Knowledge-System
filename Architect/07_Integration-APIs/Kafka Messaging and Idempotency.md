---
title: "Kafka Messaging and Idempotency"
category: integration
tags: [kafka, messaging, idempotency, outbox, interview]
created: 2026-09-03
completed: false
---

# Kafka Messaging and Idempotency

> Part of [[README|07 Integration MOC]] • `integration` • **Events at scale + exactly-once effect.** Interviews test **outbox, idempotent consumers, and ordering**.

## TL;DR for interviews

> **Kafka = durable log, not a queue.** Producer: **transactional outbox** (DB write + event atomically). Consumer: **idempotency key + dedupe table** → at-least-once delivery, exactly-once effect.

## Core Design

| Concern | Pattern |
|---------|---------|
| Publish atomically | Transactional outbox table → relay publishes |
| Ordering | Same key → same partition (per-key order only) |
| No lost events | `acks=all`, `enable.idempotence=true`, min ISR |
| No double-apply | Consumer dedupe on `event_id` (unique constraint) |
| Replay | Reset offset / new consumer group, idempotent handlers |

## Spring Kafka — Idempotent Consumer

```java
// Concept: the UNIQUE(event_id) insert is the lock — duplicates die here, not in business logic
@Transactional
@KafkaListener(topics = "payments", groupId = "ledger")
public void onPayment(PaymentEvent e) {
    int inserted = jdbc.update(
        "INSERT INTO processed_events(event_id) VALUES (?) ON CONFLICT DO NOTHING", e.id());
    if (inserted == 0) return; // Concept: redelivery — already applied, ack and skip
    ledger.apply(e);           // Concept: runs at most once per event_id
}
```

## Outbox (Producer Side)

```java
// Concept: business row + outbox row commit together; a relay polls outbox → Kafka
@Transactional
public void placeOrder(Order o) {
    orders.save(o);
    outbox.save(new OutboxEvent("order.placed", o.getId(), toJson(o))); // same TX
}
```

## Quick Check

- [ ] Why outbox instead of publish-then-commit?
- [ ] Partition key vs consumer group — what controls order vs parallelism?
- [ ] How do you get exactly-once *effect*?

## Pitfalls

- Dual-write (DB + Kafka in code, no outbox) → ghost events or lost events on crash.
- Assuming global order — only per-key within a partition.

## Interview Q&A

- **Q: Poison message kills the consumer loop?** A: Retry with backoff → dead-letter topic after N attempts, alert on DLQ depth.
- **Q: Rebasing offsets / retention?** A: Size retention by replay need (e.g. 7d); long-term audit lives in object storage, not Kafka.

## Related

- [[gRPC and Protobuf]] • [[Gateway and Service Mesh]] • [[../08_NonFunctional-Ops/Resilience and Chaos|Resilience and Chaos]]
