---
title: Design LRU Cache
category: Architect/10_System-Design-Interviews
tags:
- cache
- concept/interview-prep
- data-structure
- difficulty/medium
- lru-cache
- ood
- pattern/caching
- pattern/system-design
created: '2026-09-27'
completed: false
difficulty: Medium
reviewed: '2026-09-25'
sr-due: '2026-10-02'
source: https://github.com/donnemartin/system-design-primer
excalidraw: ''
weeks: '8'
type: concept

---






# Design LRU Cache

> Part of [[README|MOC]] • `Architect/10_System-Design-Interviews` • Weeks 8
> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → System Design Interviews Diagram`

## Intent

System design interview problem from system-design-primer with solution approach.

## Why it Matters

- **Interview signal**: Classic system design problem testing end-to-end design skills
- **Production impact**: Patterns used in real-world systems at scale
- **Core concepts**: Covers requirements gathering, API design, data modeling, scaling

## Problems

### System Design Problem: Design LRU Cache

**Requirements:**
- get(key) - return value or -1
- put(key, value) - insert/update, evict LRU if at capacity
- O(1) time for both operations
- Fixed capacity

**Constraints:**
- High availability (99.9%+)
- Horizontal scalability
- Fault tolerance
- Low latency (p99 < 100ms for reads)
- Data durability

## Code / Example

```java
// Java 25 / Spring Boot 3.5: Core concept for Design LRU Cache
// Architecture pattern - implementation varies by system

record DesignLRUCacheConfig(
    String component,
    int capacity,
    String strategy
) {
    static DesignLRUCacheConfig ofDefaults() {
        return new DesignLRUCacheConfig(
            "Design LRU Cache",
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
| Dimension | This Approach | Alternative | Trade-off Rationale | Decision Rule |
|-----------|---------------|-------------|---------------------|---------------|
| Complexity | Not specified | Not specified | Not specified | Not specified |
| Operational Burden | Not specified | Not specified | Not specified | Not specified |
| Latency | Not specified | Not specified | Not specified | Not specified |
| Consistency | Not specified | Not specified | Not specified | Not specified |
| Cost at Scale | Not specified | Not specified | Not specified | Not specified |

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

**Q1: Walk me through the high-level architecture for Design LRU Cache.**
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
**Q:** What is the core pattern for Design LRU Cache? :: **A:** [Key algorithm/architecture from primer] #flashcard

#flashcard
**Q:** When do you use Design LRU Cache? :: **A:** [Trigger scenarios from primer] #flashcard

#flashcard
**Q:** Key trade-off in Design LRU Cache? :: **A:** [Main trade-off] #flashcard

#flashcard
**Q:** Scale bottleneck for Design LRU Cache? :: **A:** [Primary bottleneck] #flashcard


## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the core concept of Design LRU Cache? :: **A:** [Key algorithm/architecture pattern] #flashcard

#flashcard
**Q:** When do you apply Design LRU Cache? :: **A:** [Trigger scenarios and context] #flashcard

#flashcard
**Q:** What is the primary trade-off in Design LRU Cache? :: **A:** [Main tension: e.g., consistency vs latency] #flashcard

#flashcard
**Q:** What breaks first at scale in Design LRU Cache? :: **A:** [Primary bottleneck: e.g., coordination, hot keys, replication lag] #flashcard

#flashcard
**Q:** How do you handle failures in Design LRU Cache? :: **A:** [Retry, circuit breaker, fallback, graceful degradation] #flashcard

#flashcard
**Q:** What are the key metrics to monitor for Design LRU Cache? :: **A:** [RED: rate, errors, duration; USE: utilization, saturation, errors] #flashcard

#flashcard
**Q:** How does Design LRU Cache scale to 10x? :: **A:** [Sharding, read replicas, async processing, caching layers] #flashcard

#flashcard
**Q:** What is the consistency model for Design LRU Cache? :: **A:** [Strong/eventual/causal - justify with use case] #flashcard

#flashcard
**Q:** How do you test Design LRU Cache? :: **A:** [Contract tests, chaos engineering, load tests, fault injection] #flashcard

#flashcard
**Q:** What is the operational cost of Design LRU Cache? :: **A:** [Team expertise, tooling, on-call burden, migration risk] #flashcard

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