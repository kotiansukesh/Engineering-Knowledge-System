---
title: Availability vs Consistency (CAP Theorem)
category: Architect/10_System-Design-Interviews
tags:
- availability
- cap-theorem
- company/youtube
- concept/interview-prep
- consistency
- difficulty/medium
- partition-tolerance
- pattern/system-design
created: '2026-09-27'
completed: false
difficulty: Medium
reviewed: '2026-09-12'
sr-due: '2026-09-19'
source: https://github.com/donnemartin/system-design-primer
excalidraw: CAP-Theorem-Decision.excalidraw.json
weeks: '2'
type: note

---











# Availability vs Consistency (CAP Theorem)

> Part of [[README|MOC]] • `Architect/10_System-Design-Interviews` • Weeks 2
> 🎨 **Visual diagram:** Open Excalidraw template: 

## Intent

[![](/donnemartin/system-design-primer/raw/master/images/bgLMI2u.png)](/donnemartin/system-design-primer/blob/master/images/bgLMI2u.png)

## Why it Matters

- **Interview signal**: CAP theorem is the #1 distributed systems question
- **Production impact**: Every distributed database decision is a CP vs AP choice
- **Core concept**: You cannot have all three - networks WILL partition

[![](/donnemartin/system-design-primer/raw/master/images/bgLMI2u.png)](/donnemartin/system-design-primer/blob/master/images/bgLMI2u.png)
*[Source: CAP theorem revisited](https://robertgreiner.com/cap-theorem-revisited)*

In a distributed computer system, you can only support two of the following guarantees:

- **Consistency** - Every read receives the most recent write or an error
- **Availability** - Every request receives a response, without guarantee that it contains the most recent version of the information
- **Partition Tolerance** - The system continues to operate despite arbitrary partitioning due to network failures
*Networks aren't reliable, so you'll need to support partition tolerance. You'll need to make a software tradeoff between consistency and availability.*

#### CP - consistency and partition tolerance

Waiting for a response from the partitioned node might result in a timeout error. CP is a good choice if your business needs require atomic reads and writes.

#### AP - availability and partition tolerance

Responses return the most readily available version of the data available on any node, which might not be the latest. Writes might take some time to propagate when the partition is resolved.

AP is a good choice if the business needs to allow for eventual consistency or when the system needs to continue working despite external errors.

### Source(s) and further reading

- [CAP theorem revisited](https://robertgreiner.com/cap-theorem-revisited/)
- [A plain english introduction to CAP theorem](http://ksat.me/a-plain-english-introduction-to-cap-theorem)
- [CAP FAQ](https://github.com/henryr/cap-faq)
- [The CAP theorem](https://www.youtube.com/watch?v=k-Yaq8AHlFA)

## Problems

### System Design Problem: Availability vs Consistency (CAP Theorem)

**Requirements:**
- See primer for detailed requirements

**Constraints:**
- High availability, scalability, fault tolerance

## Code / Example

```java
// Java 25 / Spring Boot 3.5: CAP Theorem - Tunable Consistency Client
// Demonstrates how to configure consistency level per operation

package com.architect.cap;

import org.springframework.data.cassandra.core.CassandraTemplate;
import org.springframework.data.cassandra.core.query.Query;
import org.springframework.data.cassandra.core.query.ConsistencyLevel;
import org.springframework.stereotype.Service;
import reactor.core.publisher.Mono;

@Service
public class TunableConsistencyService {

    private final CassandraTemplate cassandraTemplate;

    public TunableConsistencyService(CassandraTemplate cassandraTemplate) {
        this.cassandraTemplate = cassandraTemplate;
    }

    // Strong consistency (CP) - for financial transactions
    public Mono<User> getUserStrongConsistency(String userId) {
        Query query = Query.query(where("id").is(userId))
            .consistencyLevel(ConsistencyLevel.QUORUM); // R + W > N
        return cassandraTemplate.selectOne(query, User.class);
    }

    // Eventual consistency (AP) - for user profile reads
    public Mono<User> getUserEventualConsistency(String userId) {
        Query query = Query.query(where("id").is(userId))
            .consistencyLevel(ConsistencyLevel.ONE); // Low latency, may be stale
        return cassandraTemplate.selectOne(query, User.class);
    }

    // Per-operation consistency based on business context
    public Mono<Account> transferFunds(TransferRequest req) {
        return cassandraTemplate.getSession()
            .executeReactive(
                "BEGIN BATCH " +
                "UPDATE accounts SET balance = balance - ? WHERE id = ? IF balance >= ?; " +
                "UPDATE accounts SET balance = balance + ? WHERE id = ?; " +
                "APPLY BATCH;",
                req.amount(), req.fromAccount(), req.amount(),
                req.amount(), req.toAccount()
            )
            .map(result -> result.one().getBool("[applied]"))
            .filter(applied -> applied)
            .switchIfEmpty(Mono.error(new InsufficientFundsException()));
    }
}

// Configuration for different consistency profiles
@Configuration
class CassandraConsistencyConfig {

    @Bean
    public CassandraClusterFactoryBean cluster() {
        CassandraClusterFactoryBean cluster = new CassandraClusterFactoryBean();
        cluster.setContactPoints("cassandra-1,cassandra-2,cassandra-3");
        cluster.setPort(9042);
        cluster.setConsistencyLevel(ConsistencyLevel.LOCAL_QUORUM); // Default
        return cluster;
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
**A:** ('Walk me through the CAP theorem and why it matters in practice.', 'CAP states you can only guarantee 2 of 3: Consistency (linearizability), Availability (every request succeeds), Partition Tolerance (system works despite network failures). Since networks WILL partition, the real choice is CP vs AP. CP (e.g., HBase, ZooKeeper) blocks writes during partition to ensure consistency. AP (e.g., Cassandra, DynamoDB) accepts writes on both sides, reconciling later. Most systems are AP for user-facing features, CP for coordination/metadata.')

**Q2: Q2**
**A:** ('How do you handle the consistency-availability trade-off in a real system?', 'Use hybrid approach: CP for metadata/coordination (ZooKeeper, etcd, Consul), AP for user data. Implement tunable consistency per operation (Cassandra QUORUM, DynamoDB strong/read-after-write). Use read-repair, hinted handoff, anti-entropy for eventual consistency. For financial data, use synchronous replication + consensus (Raft/Paxos).')

**Q3: Q3**
**A:** ('What happens during a network partition in a CP system vs AP system?', 'CP: Minority partition becomes unavailable (rejects writes, may serve stale reads if configured). Majority continues. AP: Both partitions accept writes. Conflict resolution on merge (last-write-wins, CRDTs, application-level). Risk: split-brain, data loss, divergence.')

**Q4: Q4**
**A:** ('How do you test partition tolerance in CI/CD?', 'Chaos engineering: inject network partitions (tc/netem, Chaos Mesh, Litmus). Test: minority partition unavailability (CP), write acceptance on both sides (AP), merge behavior, data integrity. Tools: Jepsen tests for linearizability verification.')

**Q5: Q5**
**A:** ('What monitoring tells you if CAP trade-off is working?', 'CP: replication lag, leader election frequency, quorum availability. AP: conflict rate, read-repair rate, hinted handoff queue, divergence metrics (vector clocks). Both: p99 latency, error rate, availability SLO.')
## Flashcards (Spaced Repetition)

#flashcard
**Q:** What does CAP stand for? :: **A:** Consistency, Availability, Partition Tolerance #flashcard

#flashcard
**Q:** What is the CAP theorem? :: **A:** In a distributed system, you can only guarantee 2 of 3: Consistency, Availability, Partition Tolerance #flashcard

#flashcard
**Q:** Why must you choose Partition Tolerance? :: **A:** Networks are unreliable - partitions WILL happen, so PT is mandatory #flashcard

#flashcard
**Q:** What is a CP system? :: **A:** Consistency + Partition Tolerance. Blocks writes during partition (e.g., HBase, ZooKeeper, etcd) #flashcard

#flashcard
**Q:** What is an AP system? :: **A:** Availability + Partition Tolerance. Accepts writes on both sides, reconciles later (e.g., Cassandra, DynamoDB) #flashcard

#flashcard
**Q:** What is linearizability? :: **A:** Strong consistency model: operations appear to execute atomically at some point between invocation and response #flashcard

#flashcard
**Q:** What is eventual consistency? :: **A:** If no new updates, all reads eventually return the last written value #flashcard

#flashcard
**Q:** What is read-repair? :: **A:** Background process that fixes stale replicas during read operations #flashcard

#flashcard
**Q:** What is hinted handoff? :: **A:** When a replica is down, writes are stored on another node and forwarded when it recovers #flashcard

#flashcard
**Q:** What is anti-entropy? :: **A:** Background process (Merkle trees) that reconciles differences between replicas #flashcard

#flashcard
**Q:** What is QUORUM in Cassandra? :: **A:** R + W > N. Typical: N=3, W=2, R=2 for strong consistency #flashcard

#flashcard
**Q:** What is the trade-off of strong consistency? :: **A:** Higher latency (wait for acks), unavailability during minority partition #flashcard

#flashcard
**Q:** How do you test partition tolerance? :: **A:** Chaos engineering: inject network partitions (tc/netem, Chaos Mesh, Jepsen tests) #flashcard

#flashcard
**Q:** What monitoring for CP systems? :: **A:** Replication lag, leader election frequency, quorum availability #flashcard

#flashcard
**Q:** What monitoring for AP systems? :: **A:** Conflict rate, read-repair rate, hinted handoff queue, vector clock divergence #flashcard
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