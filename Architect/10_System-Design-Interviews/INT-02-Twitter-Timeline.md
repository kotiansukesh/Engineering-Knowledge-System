---
title: Design Twitter Timeline
category: Architect/10_System-Design-Interviews
tags:
- company/twitter
- concept/interview-prep
- difficulty/hard
- fan-out
- news-feed
- pattern/system-design
- search
- timeline
- twitter
created: '2026-09-27'
completed: false
difficulty: Hard
reviewed: '2026-09-16'
sr-due: '2026-09-30'
source: https://github.com/donnemartin/system-design-primer
excalidraw: ''
weeks: '7'
type: note

---







# Design Twitter Timeline

> Part of [[README|MOC]] • `Architect/10_System-Design-Interviews` • Weeks 7
> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → System Design Interviews Diagram`

## Intent

[View exercise and solution](/donnemartin/system-design-primer/blob/master/solutions/system_design/twitter/README.md)

## Why it Matters

- **Interview signal**: Classic system design problem testing end-to-end design skills
- **Production impact**: Patterns used in real-world systems at scale
- **Core concepts**: Covers requirements gathering, API design, data modeling, scaling

[View exercise and solution](/donnemartin/system-design-primer/blob/master/solutions/system_design/twitter/README.md)

[![Imgur](/donnemartin/system-design-primer/raw/master/images/jrUBAF7.png)](/donnemartin/system-design-primer/blob/master/images/jrUBAF7.png)

## Problems

### System Design Problem: Design Twitter Timeline

**Requirements:**
- Post tweets (text, media)
- Follow/unfollow users
- Generate home timeline (fan-out)
- Generate user timeline
- Search tweets
- Handle 100M+ users, 500M tweets/day

**Constraints:**
- High availability (99.9%+)
- Horizontal scalability
- Fault tolerance
- Low latency (p99 < 100ms for reads)
- Data durability

## Code / Example

```java
// Java 25 / Spring Boot 3.5: Core concept for Design Twitter Timeline
// Architecture pattern - implementation varies by system

record DesignTwitterTimelineConfig(
    String component,
    int capacity,
    String strategy
) {
    static DesignTwitterTimelineConfig ofDefaults() {
        return new DesignTwitterTimelineConfig(
            "Design Twitter Timeline",
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
**A:** ('Design Twitter timeline. How do you generate home timeline for 300M users?', "Two approaches: 1) Fan-out on write (push): when user tweets, push to all followers' timeline caches (Redis). Write amplification: 300M * avg_followers. 2) Fan-out on read (pull): merge followee tweets at read time. Hybrid: push for active users (<10K followers), pull for celebrities. Use Redis sorted sets (score = timestamp). Pre-compute timelines for active users.")

**Q2: Q2**
**A:** ('How do you handle celebrity with 50M followers?', 'Do NOT fan-out on write. On read: merge celebrity tweets separately. Cache celebrity tweets in separate key. Use "pull" for high-follower accounts. Fan-out threshold: ~10K followers.')

**Q3: Q3**
**A:** ('How do you handle tweet deletion and edit?', 'Delete: remove from author timeline + fan-out delete to follower timelines (async, best-effort). Edit: not supported historically; if added, version tweets, update in place with edit timestamp.')

**Q4: Q4**
**A:** ('How do you rank tweets (algorithmic timeline)?', 'Features: recency, engagement (likes/retweets/replies), author affinity, media type, user preferences. Model: LightGBM/XGBoost, trained daily. Serve: candidate generation (followees + recommendations) -> ranking -> diversification -> cache. A/B test ranking changes.')

**Q5: Q5**
**A:** ('How do you scale search across 500M tweets/day?', 'Inverted index (Lucene/Elasticsearch). Shard by time (hourly/daily indices). Real-time indexing: Kafka -> Flink -> ES. Query: fan-out to shards, merge top-K. Cache frequent queries.')
## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the core pattern for Design Twitter Timeline? :: **A:** [Key algorithm/architecture from primer] #flashcard

#flashcard
**Q:** When do you use Design Twitter Timeline? :: **A:** [Trigger scenarios from primer] #flashcard

#flashcard
**Q:** Key trade-off in Design Twitter Timeline? :: **A:** [Main trade-off] #flashcard

#flashcard
**Q:** Scale bottleneck for Design Twitter Timeline? :: **A:** [Primary bottleneck] #flashcard


## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the core concept of Design Twitter Timeline? :: **A:** [Key algorithm/architecture pattern] #flashcard

#flashcard
**Q:** When do you apply Design Twitter Timeline? :: **A:** [Trigger scenarios and context] #flashcard

#flashcard
**Q:** What is the primary trade-off in Design Twitter Timeline? :: **A:** [Main tension: e.g., consistency vs latency] #flashcard

#flashcard
**Q:** What breaks first at scale in Design Twitter Timeline? :: **A:** [Primary bottleneck: e.g., coordination, hot keys, replication lag] #flashcard

#flashcard
**Q:** How do you handle failures in Design Twitter Timeline? :: **A:** [Retry, circuit breaker, fallback, graceful degradation] #flashcard

#flashcard
**Q:** What are the key metrics to monitor for Design Twitter Timeline? :: **A:** [RED: rate, errors, duration; USE: utilization, saturation, errors] #flashcard

#flashcard
**Q:** How does Design Twitter Timeline scale to 10x? :: **A:** [Sharding, read replicas, async processing, caching layers] #flashcard

#flashcard
**Q:** What is the consistency model for Design Twitter Timeline? :: **A:** [Strong/eventual/causal - justify with use case] #flashcard

#flashcard
**Q:** How do you test Design Twitter Timeline? :: **A:** [Contract tests, chaos engineering, load tests, fault injection] #flashcard

#flashcard
**Q:** What is the operational cost of Design Twitter Timeline? :: **A:** [Team expertise, tooling, on-call burden, migration risk] #flashcard

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