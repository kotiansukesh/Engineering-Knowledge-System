---
title: Relational Database (RDBMS)
category: Architect/10_System-Design-Interviews
tags:
- acid
- company/youtube
- concept/interview-prep
- difficulty/medium
- pattern/system-design
- rdbms
- sql
- transactions
created: '2026-09-27'
completed: false
difficulty: Medium
reviewed: '2026-08-30'
sr-due: '2026-09-06'
source: https://github.com/donnemartin/system-design-primer
excalidraw: ''
weeks: '3'
type: note
---




# Relational Database (RDBMS)

> Part of [[README|MOC]] • `Architect/10_System-Design-Interviews` • Weeks 3
> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → System Design Interviews Diagram`

## Intent

A relational database like SQL is a collection of data items organized in tables.

## Why it Matters

- **Interview signal**: Frequently asked in system design interviews
- **Production impact**: Fundamental to scalable system design
- **Core concept**: Key building block for distributed systems

A relational database like SQL is a collection of data items organized in tables.

**ACID** is a set of properties of relational database [transactions](https://en.wikipedia.org/wiki/Database_transaction).

- **Atomicity** - Each transaction is all or nothing
- **Consistency** - Any transaction will bring the database from one valid state to another
- **Isolation** - Executing transactions concurrently has the same results as if the transactions were executed serially
- **Durability** - Once a transaction has been committed, it will remain so
There are many techniques to scale a relational database: **master-slave replication**, **master-master replication**, **federation**, **sharding**, **denormalization**, and **SQL tuning**.

#### Master-slave replication

The master serves reads and writes, replicating writes to one or more slaves, which serve only reads. Slaves can also replicate to additional slaves in a tree-like fashion. If the master goes offline, the system can continue to operate in read-only mode until a slave is promoted to a master or a new master is provisioned.

[![](/donnemartin/system-design-primer/raw/master/images/C9ioGtn.png)](/donnemartin/system-design-primer/blob/master/images/C9ioGtn.png)
*[Source: Scalability, availability, stability, patterns](http://www.slideshare.net/jboner/scalability-availability-stability-patterns/)*

##### Disadvantage(s): master-slave replication

- Additional logic is needed to promote a slave to a master.
- See Disadvantage(s): replication for points related to **both** master-slave and master-master.

#### Master-master replication

Both masters serve reads and writes and coordinate with each other on writes. If either master goes down, the system can continue to operate with both reads and writes.

[![](/donnemartin/system-design-primer/raw/master/images/krAHLGg.png)](/donnemartin/system-design-primer/blob/master/images/krAHLGg.png)
*[Source: Scalability, availability, stability, patterns](http://www.slideshare.net/jboner/scalability-availability-stability-patterns/)*

##### Disadvantage(s): master-master replication

- You'll need a load balancer or you'll need to make changes to your application logic to determine where to write.
- Most master-master systems are either loosely consistent (violating ACID) or have increased write latency due to synchronization.
- Conflict resolution comes more into play as more write nodes are added and as latency increases.
- See Disadvantage(s): replication for points related to **both** master-slave and master-master.

##### Disadvantage(s): replication

- There is a potential for loss of data if the master fails before any newly written data can be replicated to other nodes.
- Writes are replayed to the read replicas. If there are a lot of writes, the read replicas can get bogged down with replaying writes and can't do as many reads.
- The more read slaves, the more you have to replicate, which leads to greater replication lag.
- On some systems, writing to the master can spawn multiple threads to write in parallel, whereas read replicas only support writing sequentially with a single thread.
- Replication adds more hardware and additional complexity.

##### Source(s) and further reading: replication

- [Scalability, availability, stability, patterns](http://www.slideshare.net/jboner/scalability-availability-stability-patterns/)
- [Multi-master replication](https://en.wikipedia.org/wiki/Multi-master_replication)

#### Federation

[![](/donnemartin/system-design-primer/raw/master/images/U3qV33e.png)](/donnemartin/system-design-primer/blob/master/images/U3qV33e.png)
*[Source: Scaling up to your first 10 million users](https://www.youtube.com/watch?v=kKjm4ehYiMs)*

Federation (or functional partitioning) splits up databases by function. For example, instead of a single, monolithic database, you could have three databases: **forums**, **users**, and **products**, resulting in less read and write traffic to each database and therefore less replication lag. Smaller databases result in more data that can fit in memory, which in turn results in more cache hits due to improved cache locality. With no single central master serializing writes you can write in parallel, increasing throughput.

##### Disadvantage(s): federation

- Federation is not effective if your schema requires huge functions or tables.
- You'll need to update your application logic to determine which database to read and write.
- Joining data from two databases is more complex with a [server link](http://stackoverflow.com/questions/5145637/querying-data-by-joining-two-tables-in-two-database-on-different-servers).
- Federation adds more hardware and additional complexity.

##### Source(s) and further reading: federation

- [Scaling up to your first 10 million users](https://www.youtube.com/watch?v=kKjm4ehYiMs)

#### Sharding

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
- Constraints can help redundant copie

## Problems

### System Design Problem: Relational Database (RDBMS)

**Requirements:**
- See primer for detailed requirements

**Constraints:**
- High availability, scalability, fault tolerance

## Code / Example

```java
// Java 25 / Spring Boot 3.5: Core concept for Relational Database (RDBMS)
// Architecture pattern - implementation varies by system

record RelationalDatabaseRDBMSConfig(
    String component,
    int capacity,
    String strategy
) {
    static RelationalDatabaseRDBMSConfig ofDefaults() {
        return new RelationalDatabaseRDBMSConfig(
            "Relational Database (RDBMS)",
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

- slave replication
- *both** master-slave and master-master.

## Interview Q&A (Senior Depth)

**Q1: Walk me through the high-level architecture for Relational Database (RDBMS).**
**A:** [Key components, data flow, boundaries. Use back-of-envelope to justify scale.]

**Q2: What are the key trade-offs in this design?**
**A:** [CAP, Latency vs Throughput, Build vs Buy, SQL vs NoSQL, Sync vs Async. Cite specific choices.]

**Q3: How does this scale to 10x traffic?**
**A:** [Stateless services, sharding, read replicas, caching layers, async processing via message queues. Identify bottlenecks.]

**Q4: What happens when [critical component] fails?**
**A:** [Retries, circuit breakers, fallback, graceful degradation, data recovery, replay.]

**Q5: How do you monitor and debug this in production?**
**A:** [RED metrics: rate, errors, duration. USE metrics: utilization, saturation, errors. Structured logging, correlation IDs. SLO-based alerting.]

## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the core pattern for Relational Database (RDBMS)? :: **A:** [Key algorithm/architecture from primer] #flashcard

#flashcard
**Q:** When do you use Relational Database (RDBMS)? :: **A:** [Trigger scenarios from primer] #flashcard

#flashcard
**Q:** Key trade-off in Relational Database (RDBMS)? :: **A:** [Main trade-off] #flashcard

#flashcard
**Q:** Scale bottleneck for Relational Database (RDBMS)? :: **A:** [Primary bottleneck] #flashcard

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