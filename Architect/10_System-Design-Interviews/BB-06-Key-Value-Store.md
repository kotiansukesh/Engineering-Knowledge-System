---
title: Design a Key-Value Store
category: Architect/10_System-Design-Interviews
tags:
- compaction
- concept/interview-prep
- difficulty/medium
- key-value-store
- lsm-tree
- pattern/system-design
- sstable
created: '2026-09-27'
completed: false
difficulty: Medium
reviewed: '2026-09-08'
sr-due: '2026-09-15'
source: https://github.com/donnemartin/system-design-primer
excalidraw: ''
weeks: '3'
type: note
---







# Design a Key-Value Store

> Part of [[README|MOC]] • `Architect/10_System-Design-Interviews` • Weeks 3
> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → System Design Interviews Diagram`

## Intent

[View exercise and solution](/donnemartin/system-design-primer/blob/master/solutions/system_design/query_cache/README.md)

## Why it Matters

- **Interview signal**: Frequently asked in system design interviews
- **Production impact**: Fundamental to scalable system design
- **Core concept**: Key building block for distributed systems

[View exercise and solution](/donnemartin/system-design-primer/blob/master/solutions/system_design/query_cache/README.md)

[![Imgur](/donnemartin/system-design-primer/raw/master/images/4j99mhe.png)](/donnemartin/system-design-primer/blob/master/images/4j99mhe.png)



[View exercise and solution](/donnemartin/system-design-primer/blob/master/solutions/system_design/sales_rank/README.md)

[![Imgur](/donnemartin/system-design-primer/raw/master/images/MzExP06.png)](/donnemartin/system-design-primer/blob/master/images/MzExP06.png)

### Design a system that scales to millions of users on AWS

[View exercise and solution](/donnemartin/system-design-primer/blob/master/solutions/system_design/scaling_aws/README.md)

[![Imgur](/donnemartin/system-design-primer/raw/master/images/jj3A5N8.png)](/donnemartin/system-design-primer/blob/master/images/jj3A5N8.png)

## Problems

### System Design Problem: Design a Key-Value Store

**Requirements:**
- See primer for detailed requirements

**Constraints:**
- High availability, scalability, fault tolerance

## Code / Example

```java
// Java 25 / Spring Boot 3.5: Core concept for Design a Key-Value Store
// Architecture pattern - implementation varies by system

record DesignaKeyValueStoreConfig(
    String component,
    int capacity,
    String strategy
) {
    static DesignaKeyValueStoreConfig ofDefaults() {
        return new DesignaKeyValueStoreConfig(
            "Design a Key-Value Store",
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
**A:** ('Design a key-value store like Cassandra/DynamoDB. Core components?', '1) LSM Tree: MemTable (in-memory, sorted) -> SSTables (immutable, disk). 2) Compaction: merge SSTables, remove tombstones. 3) WAL: durability for MemTable. 4) Bloom filter: fast negative lookups. 5) Partitioning: consistent hashing + vnodes. 6) Replication: quorum (R+W>N). 7) Gossip: membership, failure detection.')

**Q2: Q2**
**A:** ('Explain LSM tree compaction strategies.', 'Size-tiered: merge same-size SSTables (write-optimized). Leveled: merge into levels (read-optimized, space-amplification lower). Universal: mix of both. Choose: write-heavy -> size-tiered; read-heavy -> leveled.')

**Q3: Q3**
**A:** ('How do you handle range queries on hash-partitioned data?', 'Hash partitioning kills range queries. Solutions: 1) Secondary index (local per shard, scatter-gather). 2) Composite key: (tenant_id, timestamp) -> range within tenant. 3) Dual-write to column store (ClickHouse) for analytics. 4) Scan all shards (expensive).')

**Q4: Q4**
**A:** ('How do you achieve strong consistency with quorum?', 'R + W > N. Typical: N=3, W=2, R=2 (strong). DynamoDB: consistent read = quorum. Cassandra: QUORUM. Trade-off: latency (wait for acks), availability (minority partition unavailable).')

**Q5: Q5**
**A:** ('How do you handle TTL and tombstone garbage collection?', 'TTL per cell. Tombstones written on delete. Compaction removes tombstones (after gc_grace_seconds). Risk: tombstone resurrection if node down > gc_grace. Monitor: tombstone ratio, compaction backlog.')
## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is LSM Tree? :: **A:** Log-Structured Merge Tree: MemTable (RAM) → SSTables (disk, immutable, sorted) #flashcard

#flashcard
**Q:** MemTable? :: **A:** In-memory sorted structure (skip list/B-tree). Flushed to SSTable when full #flashcard

#flashcard
**Q:** SSTable? :: **A:** Sorted String Table: immutable, sorted key-value files on disk. Bloom filter for fast negative #flashcard

#flashcard
**Q:** Compaction strategies? :: **A:** Size-tiered (write-opt), Leveled (read-opt), Universal (hybrid). Choose by workload #flashcard

#flashcard
**Q:** WAL? :: **A:** Write-Ahead Log: durability for MemTable. Replay on restart #flashcard

#flashcard
**Q:** Bloom filter? :: **A:** Probabilistic data structure: fast negative lookups (definitely not in SSTable) #flashcard

#flashcard
**Q:** Quorum consistency? :: **A:** R + W > N. N=3, W=2, R=2 = strong. DynamoDB consistent read = quorum #flashcard

#flashcard
**Q:** Range queries on hash? :: **A:** Hash kills range. Solutions: secondary index (scatter-gather), composite key, dual-write to column store #flashcard

#flashcard
**Q:** Tombstone GC? :: **A:** Tombstones removed after gc_grace_seconds. Risk: resurrection if node down > gc_grace #flashcard

#flashcard
**Q:** Cassandra vs DynamoDB? :: **A:** Cassandra: tunable consistency, LSM, wide rows. DynamoDB: managed, single-digit ms, on-demand #flashcard

#flashcard
**Q:** Partitioning? :: **A:** Consistent hashing + vnodes. Token range per node. Virtual nodes for even distribution #flashcard

#flashcard
**Q:** Replication? :: **A:** N replicas. Hinted handoff for down nodes. Read repair. Anti-entropy (Merkle trees) #flashcard

#flashcard
**Q:** Gossip protocol? :: **A:** Membership, failure detection. Seed nodes for bootstrapping. SWIM for failure detection #flashcard

#flashcard
**Q:** Time-to-live (TTL)? :: **A:** Per-cell expiration. Automatic cleanup. Monitor TTL expiration rate #flashcard

#flashcard
**Q:** Monitoring? :: **A:** Read/write latency (p50/p99), compaction backlog, tombstone ratio, disk usage, heap #flashcard
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
- [[INT-06-Key-Value-Store-for-Search|Complementary: INT-06-Key-Value-Store-for-Search]]

- [[Architect/10_System-Design-Interviews/README|System Design Interviews Folder]]
- [[Architect/03_Architecture-Styles/README|Architecture Styles]]
- [[Architect/08_NonFunctional-Ops/README|Non-Functional Requirements]]
- [[Architect/07_Integration-APIs/README|Integration Patterns]]

---

*Category: Architect/10_System-Design-Interviews • Part of [[README|MOC]]*