---
title: Sharding
category: Architect/10_System-Design-Interviews
tags:
- concept/interview-prep
- consistent-hashing
- difficulty/hard
- partitioning
- pattern/sharding
- pattern/system-design
- shard-key
- sharding
created: '2026-09-27'
completed: false
difficulty: Hard
reviewed: '2026-09-27'
sr-due: '2026-10-11'
source: https://github.com/donnemartin/system-design-primer
excalidraw: Sharding-Consistent-Hashing.excalidraw.json
weeks: '3'
type: concept

---











# Sharding

> Part of [[README|MOC]] • `Architect/10_System-Design-Interviews` • Weeks 3
> 🎨 **Visual diagram:** Open Excalidraw template: 

## Intent

[![](/donnemartin/system-design-primer/raw/master/images/wU8x5Id.png)](/donnemartin/system-design-primer/blob/master/images/wU8x5Id.png)

## Why it Matters

- **Interview signal**: Horizontal scaling differentiates junior/senior
- **Production impact**: Shard key choice locks you in for years
- **Core concept**: Consistent hashing, hot spots, rebalancing

[![](/donnemartin/system-design-primer/raw/master/images/wU8x5Id.png)](/donnemartin/system-design-primer/blob/master/images/wU8x5Id.png)
*[Source: Scalability, availability, stability, patterns](http://www.slideshare.net/jboner/scalability-availability-stability-patterns/)*

Sharding distributes data across different databases such that each database can only manage a subset of the data. Taking a users database as an example, as the number of users increases, more shards are added to the cluster.

Similar to the advantages of federation, sharding results in less read and write traffic, less replication, and more cache hits. Index size is also reduced, which generally improves performance with faster queries. If one shard goes down, the other shards are still operational, although you'll want to add some form of replication to avoid data loss. Like federation, there is no single central master serializing writes, allowing you to write in parallel with increased throughput.

Common ways to shard a table of users is either through the user's last name initial or the user's geographic location.

##### Disadvantage(s): sharding

- You'll need to update your application logic to work with shards, which could result in complex SQL queries.
- Data distribution can become lopsided in a shard. For example, a set of power users on a shard could result in increased load to that shard compared to others.
  - Rebalancing adds additional complexity. A sharding function based on [consistent hashing](http://www.paperplanes.de/2011/12/9/the-magic-of-consistent-hashing.html) can reduce the amount of transferred data.
- Joining data from multiple shards is more complex.
- Sharding adds more hardware and additional complexity.

##### Source(s) and further reading: sharding

- [The coming of the shard](http://highscalability.com/blog/2009/8/6/an-unorthodox-approach-to-database-design-the-coming-of-the.html)
- [Shard database architecture](https://en.wikipedia.org/wiki/Shard_(database_architecture))
- [Consistent hashing](http://www.paperplanes.de/2011/12/9/the-magic-of-consistent-hashing.html)

#### Denormalization

Denormalization attempts to improve read performance at the expense of some write performance. Redundant copies of the data are written in multiple tables to avoid expensive joins. Some RDBMS such as [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL) and Oracle support [materialized views](https://en.wikipedia.org/wiki/Materialized_view) which handle the work of storing redundant information and keeping redundant copies consistent.

Once data becomes distributed with techniques such as federation and sharding, managing joins across data centers further increases complexity. Denormalization might circumvent the need for such complex joins.

In most systems, reads can heavily outnumber writes 100:1 or even 1000:1. A read resulting in a complex database join can be very expensive, spending a significant amount of time on disk operations.

##### Disadvantage(s): denormalization

- Data is duplicated.
- Constraints can help redundant copies of information stay in sync, which increases complexity of the database design.
- A denormalized database under heavy write load might perform worse than its normalized counterpart.

###### Source(s) and further reading: denormalization

- [Denormalization

..._This content has been truncated to stay below 50000 characters_...

## Problems

### System Design Problem: Sharding

**Requirements:**
- See primer for detailed requirements

**Constraints:**
- High availability, scalability, fault tolerance

## Code / Example

```java
// Java 25 / Spring Boot 3.5: Sharding - Consistent Hashing Router with Vitess
// Production sharding router with virtual nodes and hotspot handling

package com.architect.sharding;

import com.google.common.hash.Hashing;
import org.springframework.stereotype.Component;

import java.nio.charset.StandardCharsets;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicInteger;

@Component
public class ConsistentHashShardRouter {

    private static final int VIRTUAL_NODES = 150;
    private final TreeMap<Long, String> ring = new TreeMap<>();
    private final Map<String, ShardInfo> shards = new ConcurrentHashMap<>();
    private final Map<String, AtomicInteger> hotKeyCounters = new ConcurrentHashMap<>();

    public void addShard(String shardId, String host, int port, int weight) {
        ShardInfo info = new ShardInfo(shardId, host, port, weight);
        shards.put(shardId, info);
        
        // Add virtual nodes proportional to weight
        int vnodes = VIRTUAL_NODES * weight;
        for (int i = 0; i < vnodes; i++) {
            String virtualKey = shardId + "-vn-" + i;
            long hash = Hashing.murmur3_128().hashString(virtualKey, StandardCharsets.UTF_8).asLong();
            ring.put(hash, shardId);
        }
    }

    public void removeShard(String shardId) {
        shards.remove(shardId);
        ring.values().removeIf(v -> v.equals(shardId));
    }

    public String getShard(String key) {
        if (ring.isEmpty()) throw new IllegalStateException("No shards available");
        
        long hash = Hashing.murmur3_128().hashString(key, StandardCharsets.UTF_8).asLong();
        Map.Entry<Long, String> entry = ring.ceilingEntry(hash);
        String shardId = (entry != null) ? entry.getValue() : ring.firstEntry().getValue();
        
        // Hotspot detection: if key accessed > threshold, route to dedicated cache
        AtomicInteger counter = hotKeyCounters.computeIfAbsent(key, k -> new AtomicInteger(0));
        if (counter.incrementAndGet() > 10000) { // Threshold
            return getShard(key + "-hot"); // Separate cache shard
        }
        
        return shardId;
    }

    public List<String> getShardsForRange(String startKey, String endKey) {
        long startHash = Hashing.murmur3_128().hashString(startKey, StandardCharsets.UTF_8).asLong();
        long endHash = Hashing.murmur3_128().hashString(endKey, StandardCharsets.UTF_8).asLong();
        
        return ring.subMap(startHash, true, endHash, true)
            .values()
            .stream()
            .distinct()
            .toList();
    }

    // Bounded load consistent hashing (Google-style)
    public String getShardWithBoundedLoad(String key, int maxLoadPerShard) {
        String primary = getShard(key);
        AtomicInteger load = shards.get(primary).currentLoad();
        
        if (load.get() < maxLoadPerShard) {
            load.incrementAndGet();
            return primary;
        }
        
        // Find next shard with capacity
        return ring.tailMap(Hashing.murmur3_128()
                .hashString(key, StandardCharsets.UTF_8).asLong())
            .values()
            .stream()
            .filter(s -> shards.get(s).currentLoad().get() < maxLoadPerShard)
            .findFirst()
            .orElse(primary); // Fallback
    }

    record ShardInfo(String id, String host, int port, int weight) {
        AtomicInteger currentLoad = new AtomicInteger(0);
    }
}

// Spring Data Sharding Configuration
@Configuration
@EnableJpaRepositories(basePackages = "com.architect.sharding.repository")
class ShardingConfig {

    @Bean
    public ShardingDataSource shardingDataSource(ConsistentHashShardRouter router) {
        Map<String, DataSource> shardDataSources = new HashMap<>();
        router.getShards().forEach((id, info) -> {
            HikariDataSource ds = new HikariDataSource();
            ds.setJdbcUrl("jdbc:postgresql://" + info.host() + ":" + info.port() + "/shard_" + id);
            ds.setUsername("shard_user");
            ds.setPassword("secret");
            shardDataSources.put(id, ds);
        });
        
        return new ShardingDataSource(shardDataSources, router);
    }
}
```
## When to Use / When NOT

| **Use When** | **Avoid When** |
|--------------|----------------|
| Building this system from scratch | Managed service covers need |
| Learning architecture patterns | Simple CRUD applications |
| Interview preparation | Requirements don't match |



## Trade-offs
| Dimension | This Approach | Alternative | Trade-off Rationale | Decision Rule |
|-----------|---------------|-------------|---------------------|---------------|
| Complexity | [TBD] | [TBD] | [TBD] | [TBD] |
| Operational Burden | [TBD] | [TBD] | [TBD] | [TBD] |
| Latency | [TBD] | [TBD] | [TBD] | [TBD] |
| Consistency | [TBD] | [TBD] | [TBD] | [TBD] |
| Cost at Scale | [TBD] | [TBD] | [TBD] | [TBD] |

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
**A:** ('Walk me through sharding strategy for a user table with 1B rows.', '1) Choose shard key: user_id (hash) for even distribution, or tenant_id for multi-tenant isolation. 2) Algorithm: consistent hashing (ketama) for minimal reshuffle, or range-based for ordered scans. 3) Virtual nodes (150-200 per physical) to prevent hotspots. 4) Routing layer: proxy (Vitess, ProxySQL) or client-side (driver-aware). 5) Resharding: split/merge shards, dual-write during migration, validate with shadow traffic.')

**Q2: Q2**
**A:** ('What are the hotspot problems and how do you solve them?', 'Power users (celebrity, bot) concentrate load on one shard. Solutions: 1) Separate hot keys to dedicated shards. 2) Local cache (Redis) for hot keys. 3) Consistent hashing with bounded loads (Google consistent hashing with bounded loads). 4) Request hedging for tail latency. 5) Rate limiting per shard key.')

**Q3: Q3**
**A:** ('How do you handle cross-shard transactions?', 'Avoid if possible. If needed: 1) Saga pattern (choreography/orchestration) with compensating transactions. 2) Two-phase commit (2PC) - rare, blocks. 3) Eventual consistency: dual-write to outbox table + CDC (Debezium) to event bus. 4) Denormalize to keep data co-located. 5) Use distributed transactions only for critical paths (payments).')

**Q4: Q4**
**A:** ('How do you reshard without downtime?', '1) Add new shards to ring. 2) Dual-write to old + new shards. 3) Backfill historical data (batch, low priority). 4) Verify consistency (checksum, row count). 5) Switch reads to new shards (canary). 6) Stop dual-write, remove old shards. Tools: Vitess, gh-ost, pt-online-schema-change.')

**Q5: Q5**
**A:** ('How do you monitor shard health?', 'Per-shard: QPS, latency (p50/p99), error rate, connection count, disk usage, replication lag. Cross-shard: shard size distribution (target +/-10%), hotspot detection (top 1% keys > 50% QPS), migration progress. Alerts: shard > 80% capacity, replication lag > 30s, QPS drop > 50%.')
## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is sharding? :: **A:** Horizontal partitioning: distribute data across multiple databases #flashcard

#flashcard
**Q:** What is a shard key? :: **A:** Column(s) used to determine which shard a row belongs to #flashcard

#flashcard
**Q:** Hash vs Range sharding? :: **A:** Hash: even distribution, no ordered scans. Range: ordered scans, hotspot risk #flashcard

#flashcard
**Q:** What is consistent hashing? :: **A:** Maps keys/nodes to ring. Adding/removing node only affects K/N keys #flashcard

#flashcard
**Q:** What are virtual nodes? :: **A:** Multiple ring positions per physical node (150-200) for even load distribution #flashcard

#flashcard
**Q:** What is the hotspot problem? :: **A:** Power users concentrate load on one shard #flashcard

#flashcard
**Q:** Hotspot solutions? :: **A:** Bounded loads, dedicated shards for hot keys, local cache, rate limiting per key #flashcard

#flashcard
**Q:** Cross-shard transactions? :: **A:** Avoid. If needed: Saga pattern, 2PC (rare), eventual consistency with outbox #flashcard

#flashcard
**Q:** How to reshard without downtime? :: **A:** Dual-write → backfill → verify → canary switch → remove old #flashcard

#flashcard
**Q:** What is Vitess? :: **A:** MySQL sharding proxy: query routing, resharding, connection pooling #flashcard

#flashcard
**Q:** Shard key selection criteria? :: **A:** High cardinality, even access pattern, co-location of related data #flashcard

#flashcard
**Q:** How to handle joins across shards? :: **A:** Avoid. Denormalize, duplicate data, or scatter-gather (expensive) #flashcard

#flashcard
**Q:** What is rebalancing? :: **A:** Moving data between shards to maintain even distribution #flashcard

#flashcard
**Q:** Consistent hashing vs range for time-series? :: **A:** Range better for time-series (ordered scans, easy retention) #flashcard

#flashcard
**Q:** Monitoring shard health? :: **A:** Per-shard QPS, latency, disk, replication lag. Cross-shard: size distribution, hotspots #flashcard
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