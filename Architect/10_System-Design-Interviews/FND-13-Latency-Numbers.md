---
title: Latency Numbers Every Programmer Should Know
category: Architect/10_System-Design-Interviews
tags:
- back-of-envelope
- concept/interview-prep
- difficulty/easy
- latency
- pattern/system-design
- reference
created: '2026-09-27'
completed: false
difficulty: Easy
reviewed: '2026-09-19'
sr-due: '2026-09-22'
source: https://github.com/donnemartin/system-design-primer
excalidraw: ''
weeks: '1'
type: note
---




# Latency Numbers Every Programmer Should Know

> Part of [[README|MOC]] • `Architect/10_System-Design-Interviews` • Weeks 1
> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → System Design Interviews Diagram`

## Intent



## Why it Matters

- **Interview signal**: Frequently asked in system design interviews
- **Production impact**: Fundamental to scalable system design
- **Core concept**: Key building block for distributed systems

## Problems

### System Design Problem: Latency Numbers Every Programmer Should Know

**Requirements:**
- See primer for detailed requirements

**Constraints:**
- High availability, scalability, fault tolerance

## Code / Example

```java
// Java 25 / Spring Boot 3.5: Core concept for Latency Numbers Every Programmer Should Know
// Architecture pattern - implementation varies by system

record LatencyNumbersEveryProgrammerShouldKnowConfig(
    String component,
    int capacity,
    String strategy
) {
    static LatencyNumbersEveryProgrammerShouldKnowConfig ofDefaults() {
        return new LatencyNumbersEveryProgrammerShouldKnowConfig(
            "Latency Numbers Every Programmer Should Know",
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

**Q1: Walk me through the high-level architecture for Latency Numbers Every Programmer Should Know.**
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
**Q:** What is the core pattern for Latency Numbers Every Programmer Should Know? :: **A:** [Key algorithm/architecture from primer] #flashcard

#flashcard
**Q:** When do you use Latency Numbers Every Programmer Should Know? :: **A:** [Trigger scenarios from primer] #flashcard

#flashcard
**Q:** Key trade-off in Latency Numbers Every Programmer Should Know? :: **A:** [Main trade-off] #flashcard

#flashcard
**Q:** Scale bottleneck for Latency Numbers Every Programmer Should Know? :: **A:** [Primary bottleneck] #flashcard

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