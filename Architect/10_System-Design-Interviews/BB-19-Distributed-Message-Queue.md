---
title: Design a Distributed Message Queue (Kafka-like)
category: Architect/10_System-Design-Interviews
tags:
- concept/interview-prep
- consumer-groups
- difficulty/hard
- exactly-once
- kafka
- message-queue
- partitions
- pattern/system-design
created: '2026-09-27'
completed: false
difficulty: Hard
reviewed: '2026-09-20'
sr-due: '2026-10-04'
source: https://github.com/donnemartin/system-design-primer
excalidraw: ''
weeks: '6'
type: note
---






# Design a Distributed Message Queue (Kafka-like)

> Part of [[README|MOC]] • `Architect/10_System-Design-Interviews` • Weeks 6
> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → System Design Interviews Diagram`

## Intent



## Why it Matters

- **Interview signal**: Frequently asked in system design interviews
- **Production impact**: Fundamental to scalable system design
- **Core concept**: Key building block for distributed systems

## Problems

### System Design Problem: Design a Distributed Message Queue (Kafka-like)

**Requirements:**
- See primer for detailed requirements

**Constraints:**
- High availability, scalability, fault tolerance

## Code / Example

```java
// Java 25 / Spring Boot 3.5: Core concept for Design a Distributed Message Queue (Kafka-like)
// Architecture pattern - implementation varies by system

record DesignaDistributedMessageQueueKafkalikeConfig(
    String component,
    int capacity,
    String strategy
) {
    static DesignaDistributedMessageQueueKafkalikeConfig ofDefaults() {
        return new DesignaDistributedMessageQueueKafkalikeConfig(
            "Design a Distributed Message Queue (Kafka-like)",
            10000,
            "default"
        );
    }
}
```

### Concrete Example
- **Input:** Design requirements
- **Output:** Architecture diagram + component specs
- **Explanation:** See primer for step-by-step design

## When to Use / When NOT

| **Use When** | **Avoid When** |
|--------------|----------------|
| Building this system from scratch | Managed service covers need |
| Learning architecture patterns | Simple CRUD applications |
| Interview preparation | Requirements don't match |

## Trade-offs

| Dimension | This Approach | Alternative |
|-----------|---------------|-------------|
| Complexity | | |
| Operational Burden | | |
| Latency | | |
| Consistency | | |
| Cost at Scale | | |

## Vs Table

| Aspect | This Design | Managed Service | Decision Rule |
|--------|-------------|-----------------|---------------|
| Flexibility | Full | Limited | Need custom logic? → Self-host |
| Time to Market | Weeks | Hours | Prototype? → Managed |
| Cost at Scale | Optimizable | Fixed/marginal | High volume? → Self-host |

## Pitfalls

- Underestimating operational complexity
- Ignoring failure modes
- Not planning for 10x scale
- Skipping monitoring/alerting in MVP
- Premature optimization before measuring

## Interview Q&A (Senior Depth)

**Q1: Q1**
**A:** ('Design Kafka-like distributed message queue.', '1) Brokers: partition leaders + ISR (in-sync replicas). 2) Topics: partitioned, ordered per partition. 3) Producers: partitioner (key hash, round-robin), acks (all/1/0), idempotent. 4) Consumers: group protocol, offset management, rebalance (cooperative). 5) Storage: segments, index, time-index, compaction (log compaction for keys). 6) ZooKeeper/KRaft: controller, metadata. 7) Tiered storage: local SSD + S3.')

**Q2: Q2**
**A:** ('How does Kafka achieve high throughput?', 'Sequential disk I/O (append-only). Page cache (OS) for reads. Zero-copy (sendfile). Batching (linger.ms, batch.size). Compression (Snappy, ZSTD, LZ4). Partition parallelism.')

**Q3: Q3**
**A:** ('How do you handle consumer lag and rebalancing?', 'Lag: monitor per partition. Rebalance: cooperative (incremental) since 2.4. Static membership (group.instance.id) to avoid rebalance on restart. Max.poll.interval.ms for stuck consumers.')

**Q4: Q4**
**A:** ('How do you implement exactly-once semantics?', 'Idempotent producer: PID + sequence per partition. Transactional API: atomic write to multiple partitions + offset commit. Consumer: process + commit offset in same transaction. Requires idempotent consumer logic (dedup).')

**Q5: Q5**
**A:** ('How do you operate Kafka at scale (100+ brokers)?', 'Monitoring: under-replicated partitions, offline partitions, controller health, disk, network. Tiered storage for retention. Cruise Control for rebalance. MirrorMaker for cross-DC replication. KRaft mode (no ZooKeeper).')
## Flashcards (Spaced Repetition)

#flashcard
**Q:** Kafka architecture? :: **A:** Brokers: partition leaders + ISR. Topics: partitioned, ordered per partition. KRaft for metadata #flashcard

#flashcard
**Q:** High throughput? :: **A:** Sequential disk I/O (append-only). Page cache. Zero-copy (sendfile). Batching. Compression (ZSTD) #flashcard

#flashcard
**Q:** Consumer lag? :: **A:** Producer offset - consumer offset. Target < 1000. Monitor per partition #flashcard

#flashcard
**Q:** Rebalancing? :: **A:** Cooperative (incremental) since 2.4. Static membership (group.instance.id) avoids rebalance on restart #flashcard

#flashcard
**Q:** Exactly-once? :: **A:** Idempotent producer (PID+seq) + transactional API (atomic multi-partition + offset commit). Consumer dedup #flashcard

#flashcard
**Q:** Tiered storage? :: **A:** Hot on local SSD, cold on S3. Transparent to consumers. Retention by time/size #flashcard

#flashcard
**Q:** Log compaction? :: **A:** Key-based retention: latest value per key. Tombstones for delete. Background compaction #flashcard

#flashcard
**Q:** MirrorMaker? :: **A:** Cross-DC replication. Active-passive or active-active. Offset translation #flashcard

#flashcard
**Q:** Controller? :: **A:** KRaft: elected controller manages metadata. No ZooKeeper. ZK: controller in ZK ensemble #flashcard

#flashcard
**Q:** Partition leadership? :: **A:** Leader handles reads/writes. Followers replicate. ISR = in-sync replicas. min.insync.replicas #flashcard

#flashcard
**Q:** Producer acks? :: **A:** acks=0 (fire-forget), acks=1 (leader), acks=all (ISR). Default: all #flashcard

#flashcard
**Q:** Consumer groups? :: **A:** Each partition consumed by one consumer in group. Rebalance on join/leave. Max.poll.interval.ms #flashcard

#flashcard
**Q:** Monitoring? :: **A:** Under-replicated partitions, offline partitions, controller health, disk, network, lag, request latency #flashcard

#flashcard
**Q:** Cruise Control? :: **A:** Auto rebalance: partition movement for load balancing. Goal-based optimization #flashcard

#flashcard
**Q:** Kafka Streams? :: **A:** Stream processing library. Exactly-once. Stateful ops (joins, aggregations). Changelog topics #flashcard
## Practice Tasks (Tasks Plugin)

- [ ] Explain the architecture from memory 📅 {date:YYYY-MM-DD, +1}
- [ ] Draw the system diagram without looking 📅 {date:YYYY-MM-DD, +3}
- [ ] Answer all Interview Q&A aloud 📅 {date:YYYY-MM-DD, +7}
- [ ] Review flashcards (Spaced Repetition) 📅 {date:YYYY-MM-DD, +1}

```tasks
not done
path includes 10_System-Design-Interviews
sort by due
limit 10
```

## Related

- [[Architect/10_System-Design-Interviews/README|System Design Interviews Folder]]
- [[Architect/03_Architecture-Styles/README|Architecture Styles]]
- [[Architect/08_NonFunctional-Ops/README|Non-Functional Requirements]]
- [[Architect/07_Integration-APIs/README|Integration Patterns]]

---

*Category: Architect/10_System-Design-Interviews • Part of [[README|MOC]]*