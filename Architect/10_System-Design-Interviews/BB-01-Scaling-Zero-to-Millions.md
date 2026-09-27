---
title: 'Scaling: From Zero to Millions of Users'
category: Architect/10_System-Design-Interviews
tags:
- architecture
- caching
- cdn
- concept/interview-prep
- difficulty/easy
- load-balancer
- pattern/system-design
- replication
- scaling
- sharding
created: '2026-09-27'
completed: false
difficulty: Easy
reviewed: '2026-09-22'
sr-due: '2026-09-25'
source: https://github.com/donnemartin/system-design-primer
excalidraw: ''
weeks: '1'
type: note
---






# Scaling: From Zero to Millions of Users

> Part of [[README|MOC]] • `Architect/10_System-Design-Interviews` • Weeks 1
> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → System Design Interviews Diagram`

## Intent



## Why it Matters

- **Interview signal**: Frequently asked in system design interviews
- **Production impact**: Fundamental to scalable system design
- **Core concept**: Key building block for distributed systems

## Problems

### System Design Problem: Scaling: From Zero to Millions of Users

**Requirements:**
- See primer for detailed requirements

**Constraints:**
- High availability, scalability, fault tolerance

## Code / Example

```java
// Java 25 / Spring Boot 3.5: Core concept for Scaling: From Zero to Millions of Users
// Architecture pattern - implementation varies by system

record Scaling:FromZerotoMillionsofUsersConfig(
    String component,
    int capacity,
    String strategy
) {
    static Scaling:FromZerotoMillionsofUsersConfig ofDefaults() {
        return new Scaling:FromZerotoMillionsofUsersConfig(
            "Scaling: From Zero to Millions of Users",
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
**A:** ('Walk me through scaling a service from zero to millions of users.', 'Phase 1 (0-10K): Monolith + single DB + vertical scaling. Phase 2 (10K-100K): Read replicas, caching (Redis), CDN for static assets. Phase 3 (100K-1M): Sharding, async processing (message queues), microservices split. Phase 4 (1M+): Multi-region, active-active, custom infrastructure. Key principle: scale bottleneck first, measure before optimizing.')

**Q2: Q2**
**A:** ('What are the first 3 bottlenecks you hit and how do you fix them?', '1) Database CPU: read replicas + caching. 2) Network bandwidth: CDN + compression. 3) Single-threaded app: stateless horizontal scaling + load balancer. Then: DB connections (pooling), locks (optimistic locking), GC pauses (tuning).')

**Q3: Q3**
**A:** ('How do you decide when to split microservices?', 'Team ownership boundaries (2-pizza team). Independent deployability. Different scaling needs. Different tech stacks. Data ownership. Start with modular monolith, extract when pain > cost. Strangler fig pattern.')

**Q4: Q4**
**A:** ('How do you handle distributed transactions across services?', 'Saga pattern (choreography via events or orchestration via central coordinator). Compensating transactions for rollback. Outbox pattern for reliability. Avoid 2PC. Eventual consistency with idempotency.')

**Q5: Q5**
**A:** ('What monitoring do you put in place at each phase?', 'Phase 1: APM (latency, errors), DB metrics. Phase 2: Cache hit rate, queue depth. Phase 3: Service mesh metrics (latency, error rate per service), distributed tracing. Phase 4: SLOs, error budgets, chaos engineering.')
## Flashcards (Spaced Repetition)

#flashcard
**Q:** Phase 1 (0-10K users)? :: **A:** Monolith + single DB + vertical scaling #flashcard

#flashcard
**Q:** Phase 2 (10K-100K)? :: **A:** Read replicas, caching (Redis), CDN for static assets #flashcard

#flashcard
**Q:** Phase 3 (100K-1M)? :: **A:** Sharding, async processing (message queues), microservices split #flashcard

#flashcard
**Q:** Phase 4 (1M+)? :: **A:** Multi-region, active-active, custom infrastructure #flashcard

#flashcard
**Q:** First 3 bottlenecks? :: **A:** 1) DB CPU: read replicas + caching. 2) Network: CDN + compression. 3) Single-threaded: stateless horizontal scaling #flashcard

#flashcard
**Q:** When to split microservices? :: **A:** Team boundaries (2-pizza), independent deploy, different scaling, different tech, data ownership #flashcard

#flashcard
**Q:** Strangler fig pattern? :: **A:** Gradually extract functionality from monolith, route traffic to new services #flashcard

#flashcard
**Q:** Distributed transactions? :: **A:** Saga pattern (choreography/orchestration), compensating transactions, outbox pattern, avoid 2PC #flashcard

#flashcard
**Q:** Monitoring per phase? :: **A:** P1: APM, DB. P2: cache hit rate, queue depth. P3: service mesh, tracing. P4: SLOs, error budgets, chaos #flashcard

#flashcard
**Q:** What is modular monolith? :: **A:** Monolith with clear module boundaries, separate packages, shared DB but logical separation #flashcard

#flashcard
**Q:** Database scaling order? :: **A:** Vertical → read replicas → caching → sharding #flashcard

#flashcard
**Q:** Stateless services? :: **A:** No local state. Session in Redis. Config in etcd/Consul. Enables horizontal scaling #flashcard

#flashcard
**Q:** Caching layers? :: **A:** CDN (static) → Redis (dynamic) → in-process (hot) → DB #flashcard

#flashcard
**Q:** Async processing? :: **A:** Message queues for: email, notifications, analytics, reporting, webhooks #flashcard

#flashcard
**Q:** Circuit breaker? :: **A:** Fail fast, prevent cascade. States: closed → open → half-open #flashcard
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