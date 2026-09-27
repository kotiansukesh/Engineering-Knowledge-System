---
title: Design Consistent Hashing
category: Architect/10_System-Design-Interviews
tags:
- concept/interview-prep
- consistent-hashing
- difficulty/medium
- ketama
- pattern/consistent-hashing
- pattern/system-design
- virtual-nodes
created: '2026-09-27'
completed: false
difficulty: Medium
reviewed: '2026-09-10'
sr-due: '2026-09-17'
source: https://github.com/donnemartin/system-design-primer
excalidraw: ''
weeks: '2'
type: note
---






# Design Consistent Hashing

> Part of [[README|MOC]] • `Architect/10_System-Design-Interviews` • Weeks 2
> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → System Design Interviews Diagram`

## Intent



## Why it Matters

- **Interview signal**: Frequently asked in system design interviews
- **Production impact**: Fundamental to scalable system design
- **Core concept**: Key building block for distributed systems

## Problems

### System Design Problem: Design Consistent Hashing

**Requirements:**
- See primer for detailed requirements

**Constraints:**
- High availability, scalability, fault tolerance

## Code / Example

```java
// Java 25 / Spring Boot 3.5: Core concept for Design Consistent Hashing
// Architecture pattern - implementation varies by system

record DesignConsistentHashingConfig(
    String component,
    int capacity,
    String strategy
) {
    static DesignConsistentHashingConfig ofDefaults() {
        return new DesignConsistentHashingConfig(
            "Design Consistent Hashing",
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
**A:** ('Explain consistent hashing and why it is used for sharding.', 'Maps keys and nodes to a ring (0 to 2^32-1). Key goes to next clockwise node. Adding/removing node only affects adjacent keys (K/N keys moved vs all). Virtual nodes (vnodes) distribute load evenly. Ketama algorithm: 160 vnodes per physical node.')

**Q2: Q2**
**A:** ('How do you handle hotspots with consistent hashing?', 'Bounded loads (Google): each node has capacity, route to next node if overloaded. Virtual node weight adjustment. Separate hot keys to dedicated nodes. Local cache (Redis) for top keys.')

**Q3: Q3**
**A:** ('How does consistent hashing compare to range-based sharding?', 'Consistent: minimal reshuffle on add/remove, good for dynamic clusters. Range: ordered scans, easier debugging, but hotspots on sequential keys, reshuffle on split/merge. Choose consistent for caching, range for time-series/analytics.')

**Q4: Q4**
**A:** ('How do you implement consistent hashing in production?', 'Library: hashicorp/memberlist, Spotify DNS, or custom. Ring: sorted array of (hash, node). Binary search for key. Vnodes: 100-200 per node. Health checks: remove unhealthy nodes from ring.')

**Q5: Q5**
**A:** ('What happens during network partition in consistent hashing ring?', 'Nodes may have different ring views. Use gossip (SWIM) for membership. Split-brain: two rings. Resolve: quorum, last-write-wins, or pause writes. Prefer CP for metadata, AP for data.')
## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is consistent hashing? :: **A:** Maps keys and nodes to ring (0 to 2^32-1). Key → next clockwise node #flashcard

#flashcard
**Q:** Why virtual nodes? :: **A:** Even load distribution. 150-200 vnodes per physical node. Ketama algorithm #flashcard

#flashcard
**Q:** Adding/removing node? :: **A:** Only K/N keys affected (vs all keys in modulo hashing) #flashcard

#flashcard
**Q:** Hotspot handling? :: **A:** Bounded loads (Google): route to next node if overloaded. Weight adjustment. Dedicated nodes #flashcard

#flashcard
**Q:** Consistent vs range sharding? :: **A:** Consistent: minimal reshuffle, dynamic. Range: ordered scans, but hotspots on sequential keys #flashcard

#flashcard
**Q:** Implementation? :: **A:** Sorted array of (hash, node). Binary search for key. Health checks remove unhealthy nodes #flashcard

#flashcard
**Q:** Network partition in ring? :: **A:** Different ring views. Gossip (SWIM) for membership. Split-brain: quorum, LWW, or pause writes #flashcard

#flashcard
**Q:** Ketama algorithm? :: **A:** 160 vnodes per node. MD5 hash of node:vn. Sorted ring. Used in memcached, Redis Cluster #flashcard

#flashcard
**Q:** Consistent hashing in Redis Cluster? :: **A:** 16384 hash slots. Slots assigned to nodes. Resharding moves slots #flashcard

#flashcard
**Q:** Rendezvous hashing? :: **A:** HRW (Highest Random Weight): score = hash(key, node). No ring, simpler, same properties #flashcard

#flashcard
**Q:** Jump consistent hash? :: **A:** O(1) memory, no ring. Good for uniform loads, not for weighted #flashcard

#flashcard
**Q:** Maglev hashing? :: **A:** Google's consistent hashing for network load balancing. Minimal disruption #flashcard

#flashcard
**Q:** When NOT to use? :: **A:** Need ordered scans (range queries). Simple static cluster (modulo fine). Very few nodes #flashcard

#flashcard
**Q:** Rebalancing trigger? :: **A:** Node add/remove, load imbalance > threshold, node failure #flashcard

#flashcard
**Q:** Monitoring? :: **A:** Key distribution per node, vnode distribution, rebalance frequency, lookup latency #flashcard
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