---
title: Design a News Feed System
category: Architect/10_System-Design-Interviews
tags:
- concept/interview-prep
- difficulty/hard
- fan-out
- news-feed
- pattern/system-design
- pull-vs-push
- ranking
created: '2026-09-27'
completed: false
difficulty: Hard
reviewed: '2026-09-07'
sr-due: '2026-09-21'
source: https://github.com/donnemartin/system-design-primer
excalidraw: ''
weeks: '4'
type: note
---






# Design a News Feed System

> Part of [[README|MOC]] • `Architect/10_System-Design-Interviews` • Weeks 4
> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → System Design Interviews Diagram`

## Intent



## Why it Matters

- **Interview signal**: Frequently asked in system design interviews
- **Production impact**: Fundamental to scalable system design
- **Core concept**: Key building block for distributed systems

## Problems

### System Design Problem: Design a News Feed System

**Requirements:**
- See primer for detailed requirements

**Constraints:**
- High availability, scalability, fault tolerance

## Code / Example

```java
// Java 25 / Spring Boot 3.5: Core concept for Design a News Feed System
// Architecture pattern - implementation varies by system

record DesignaNewsFeedSystemConfig(
    String component,
    int capacity,
    String strategy
) {
    static DesignaNewsFeedSystemConfig ofDefaults() {
        return new DesignaNewsFeedSystemConfig(
            "Design a News Feed System",
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
**A:** ('Design Facebook/Instagram news feed. Fan-out on write vs read?', 'Hybrid: push for active users (<5K followers), pull for celebrities. Write path: post -> fan-out to follower timelines (Redis sorted sets, score = timestamp * weight). Read path: merge followee timelines + ranked candidates. Ranking: LightGBM model (engagement, affinity, recency). Cache: pre-computed feeds for active users.')

**Q2: Q2**
**A:** ('How do you handle ranking at scale?', 'Two-stage: 1) Candidate generation: followees + recommendations (collaborative filtering, content-based) -> 1000 candidates. 2) Ranking: pointwise/pairwise/listwise model (XGBoost/LightGBM). Features: user-user affinity, content type, recency, engagement history. Serving: TensorFlow Serving / Triton. A/B test models.')

**Q3: Q3**
**A:** ('How do you handle real-time updates (new post, like, comment)?', 'Write path: on new post, fan-out to active followers (async, Kafka). On like/comment: update counters (Redis), invalidate feed cache for affected users. WebSocket/push for real-time feel. Eventual consistency acceptable (seconds).')

**Q4: Q4**
**A:** ('How do you handle "following" 5000 users with high post volume?', "Do not fan-out all. Pull model: on read, fetch from followees' post shards. Merge top-K with heap. Cache merged result. Rank only top candidates.")

**Q5: Q5**
**A:** ('How do you measure feed quality?', 'Metrics: session time, posts viewed, interactions/impression (CTR), long-clicks, hides/reports. A/B test ranking changes. Long-term: retention, DAU/MAU. Counter-metrics: spam reports, misinformation flags.')
## Flashcards (Spaced Repetition)

#flashcard
**Q:** Fan-out on write vs read? :: **A:** Hybrid: push for active (<5K followers), pull for celebrities. Redis sorted sets (score = timestamp*weight) #flashcard

#flashcard
**Q:** Celebrity handling? :: **A:** Do NOT fan-out 50M followers. Pull model: merge on read. Cache celebrity tweets separately #flashcard

#flashcard
**Q:** Ranking pipeline? :: **A:** 1) Candidate gen: followees + recs (CF, content-based) → 1000. 2) Ranking: LightGBM/XGBoost → top 50 #flashcard

#flashcard
**Q:** Real-time updates? :: **A:** New post: async fan-out to active (Kafka). Like/comment: update counters (Redis), invalidate cache #flashcard

#flashcard
**Q:** High-volume followees? :: **A:** Don't fan-out all. Pull: fetch from followee shards, merge top-K with heap, rank top candidates #flashcard

#flashcard
**Q:** Feed quality metrics? :: **A:** Session time, posts viewed, CTR, long-clicks, hides/reports. A/B test ranking. Counter: spam flags #flashcard

#flashcard
**Q:** Tweet deletion? :: **A:** Remove from author timeline + async fan-out delete to followers. Best-effort #flashcard

#flashcard
**Q:** Tweet editing? :: **A:** Version tweets. Update in place with edit_timestamp. Not supported historically #flashcard

#flashcard
**Q:** Candidate generation? :: **A:** Followees (primary) + recommendations (collaborative filtering, content-based, graph-based) #flashcard

#flashcard
**Q:** Model serving? :: **A:** TensorFlow Serving / Triton. Feature store (Feast). Online features: Redis. Offline: BigQuery #flashcard

#flashcard
**Q:** Diversification? :: **A:** Avoid same author/type cluster. MMR (Maximal Marginal Relevance). Category balancing #flashcard

#flashcard
**Q:** A/B testing? :: **A:** Ramp: 1% → 5% → 50%. Metrics: engagement, retention. Guardrail: spam reports, latency #flashcard

#flashcard
**Q:** Storage? :: **A:** Posts: Cassandra/Scylla (partition by user_id, cluster by timestamp). Timelines: Redis sorted sets #flashcard

#flashcard
**Q:** Fan-out threshold? :: **A:** ~10K followers. Above: pull. Below: push. Configurable per system #flashcard

#flashcard
**Q:** Feed caching? :: **A:** Pre-compute for active users. TTL: 5-15 min. Invalidate on new post/interaction #flashcard
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