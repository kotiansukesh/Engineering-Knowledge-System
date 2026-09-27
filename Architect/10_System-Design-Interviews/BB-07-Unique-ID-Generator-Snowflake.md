---
title: Design a Unique ID Generator (Snowflake)
category: Architect/10_System-Design-Interviews
tags:
- concept/interview-prep
- difficulty/medium
- distributed-id
- pattern/system-design
- snowflake
- unique-id
created: '2026-09-27'
completed: false
difficulty: Medium
reviewed: '2026-09-14'
sr-due: '2026-09-21'
source: https://github.com/donnemartin/system-design-primer
excalidraw: ''
weeks: '3'
type: note
---






# Design a Unique ID Generator (Snowflake)

> Part of [[README|MOC]] • `Architect/10_System-Design-Interviews` • Weeks 3
> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → System Design Interviews Diagram`

## Intent



## Why it Matters

- **Interview signal**: Frequently asked in system design interviews
- **Production impact**: Fundamental to scalable system design
- **Core concept**: Key building block for distributed systems

## Problems

### System Design Problem: Design a Unique ID Generator (Snowflake)

**Requirements:**
- See primer for detailed requirements

**Constraints:**
- High availability, scalability, fault tolerance

## Code / Example

```java
// Java 25 / Spring Boot 3.5: Core concept for Design a Unique ID Generator (Snowflake)
// Architecture pattern - implementation varies by system

record DesignaUniqueIDGeneratorSnowflakeConfig(
    String component,
    int capacity,
    String strategy
) {
    static DesignaUniqueIDGeneratorSnowflakeConfig ofDefaults() {
        return new DesignaUniqueIDGeneratorSnowflakeConfig(
            "Design a Unique ID Generator (Snowflake)",
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
**A:** ('Design a distributed unique ID generator (Snowflake).', '64-bit: 1 bit sign (0), 41 bits timestamp (ms since epoch, ~69 years), 10 bits machine ID (1024 nodes), 12 bits sequence (4096/ms per node). Total: ~4M IDs/sec per node. Monotonic increasing, roughly time-ordered.')

**Q2: Q2**
**A:** ('What happens if clock goes backwards?', 'Wait for clock catch-up (block). Or reject request. Or use logical clock (increment sequence). Guard: max drift threshold (e.g., 100ms). Log alert. NTP sync required.')

**Q3: Q3**
**A:** ('How do you assign machine IDs in dynamic environments (K8s)?', 'Static: config file. Dynamic: etcd/Consul/ZooKeeper lease. Kubernetes: pod UID hash modulo 1024. Or use 5 bits for DC, 5 for pod.')

**Q4: Q4**
**A:** ('How do you handle ID exhaustion (sequence overflow)?', 'Sequence: 12 bits = 4096/ms. If exceeded: wait next ms. At 4M IDs/sec, need 1000 nodes. Monitor: sequence usage %, alert > 80%.')

**Q5: Q5**
**A:** ('Snowflake vs UUID vs ULID vs NanoID.', 'Snowflake: time-ordered, 64-bit, needs coordination. UUIDv4: random, 128-bit, no coordination, not ordered. UUIDv7: time-ordered, 128-bit. ULID: 128-bit, time-ordered, case-insensitive. NanoID: URL-safe, customizable. Choose Snowflake for DB primary keys (index-friendly).')
## Flashcards (Spaced Repetition)

#flashcard
**Q:** Snowflake ID structure? :: **A:** 64-bit: 1 sign(0) + 41 timestamp(ms) + 10 machine(1024) + 12 sequence(4096/ms) #flashcard

#flashcard
**Q:** Timestamp bits? :: **A:** 41 bits ms since epoch = ~69 years. Epoch custom (e.g., 2020-01-01) #flashcard

#flashcard
**Q:** Machine ID bits? :: **A:** 10 bits = 1024 nodes. Static config or dynamic (etcd/Consul lease) #flashcard

#flashcard
**Q:** Sequence bits? :: **A:** 12 bits = 4096 IDs/ms per node. Overflow: wait next ms #flashcard

#flashcard
**Q:** Clock backward? :: **A:** Block/wait for catch-up, or reject, or logical clock. Max drift threshold (100ms). NTP required #flashcard

#flashcard
**Q:** K8s machine ID? :: **A:** Pod UID hash modulo 1024. Or 5 bits DC + 5 bits pod. Etcd lease for dynamic #flashcard

#flashcard
**Q:** Snowflake vs UUIDv4? :: **A:** Snowflake: 64-bit, time-ordered, needs coordination. UUIDv4: 128-bit, random, no coordination #flashcard

#flashcard
**Q:** Snowflake vs UUIDv7? :: **A:** UUIDv7: 128-bit, time-ordered, no coordination. Snowflake: 64-bit, index-friendly #flashcard

#flashcard
**Q:** Snowflake vs ULID? :: **A:** ULID: 128-bit, time-ordered, case-insensitive, Crockford base32. Snowflake: 64-bit #flashcard

#flashcard
**Q:** Snowflake vs NanoID? :: **A:** NanoID: URL-safe, customizable alphabet/length. Not time-ordered #flashcard

#flashcard
**Q:** Why 64-bit? :: **A:** Fits in DB BIGINT. Index-friendly (sequential-ish). Smaller than UUID #flashcard

#flashcard
**Q:** ID exhaustion? :: **A:** 4M IDs/sec per node. 1024 nodes = 4B IDs/sec. Monitor sequence usage % #flashcard

#flashcard
**Q:** Twitter Snowflake? :: **A:** Original implementation. 41-bit timestamp (2010 epoch), 10-bit worker, 12-bit sequence #flashcard

#flashcard
**Q:** Sonyflake? :: **A:** Sony's variant: 39-bit timestamp (10ms units), 8-bit machine, 16-bit sequence #flashcard

#flashcard
**Q:** Baidu UID? :: **A:** Baidu's: time + machine + sequence + version. Used in FENGCHAO #flashcard
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