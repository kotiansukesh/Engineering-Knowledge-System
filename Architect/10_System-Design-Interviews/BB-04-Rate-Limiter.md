---
title: Design a Rate Limiter
category: Architect/10_System-Design-Interviews
tags:
- concept/interview-prep
- difficulty/medium
- distributed
- pattern/rate-limiting
- pattern/system-design
- rate-limiter
- sliding-window
- token-bucket
created: '2026-09-27'
completed: false
difficulty: Medium
reviewed: '2026-09-27'
sr-due: '2026-10-04'
source: https://github.com/donnemartin/system-design-primer
excalidraw: Rate-Limiter-Algorithms.excalidraw.json
weeks: '2'
type: note
---







# Design a Rate Limiter

> Part of [[README|MOC]] • `Architect/10_System-Design-Interviews` • Weeks 2
> 🎨 **Visual diagram:** Open Excalidraw template: 

## Intent



## Why it Matters

- **Interview signal**: Frequently asked in system design interviews
- **Production impact**: Fundamental to scalable system design
- **Core concept**: Key building block for distributed systems

## Problems

### System Design Problem: Design a Rate Limiter

**Requirements:**
- See primer for detailed requirements

**Constraints:**
- High availability, scalability, fault tolerance

## Code / Example

```java
// Java 25 / Spring Boot 3.5: Core concept for Design a Rate Limiter
// Architecture pattern - implementation varies by system

record DesignaRateLimiterConfig(
    String component,
    int capacity,
    String strategy
) {
    static DesignaRateLimiterConfig ofDefaults() {
        return new DesignaRateLimiterConfig(
            "Design a Rate Limiter",
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
**A:** ('Design a distributed rate limiter. Compare algorithms.', 'Token Bucket: burst allowance, smooth rate. Leaky Bucket: fixed rate, no burst. Sliding Window Log: precise, memory heavy. Sliding Window Counter: approximate, low memory. Fixed Window: simple, burst at boundaries. Distributed: Redis (Lua script for atomicity) or local + sync. Choose: API gateway -> token bucket; login -> sliding window; streaming -> leaky bucket.')

**Q2: Q2**
**A:** ('How do you implement token bucket in Redis atomically?', 'Lua script: check tokens, decrement, refill based on elapsed time. Return allowed/remaining. Keys: rate_limit:{user_id}:{window}. TTL = window + buffer. Pipeline for batch checks.')

**Q3: Q3**
**A:** ('How do you handle rate limiting at edge vs application layer?', 'Edge (Cloudflare, AWS WAF, Envoy): DDoS protection, IP-based, low latency. Application: user-level, API-key level, business logic aware (e.g., premium tier). Both needed: edge for volumetric, app for semantic.')

**Q4: Q4**
**A:** ('How do you handle rate limit exceeded responses?', 'HTTP 429 with Retry-After header. JSON body: {limit, remaining, reset}. Client: exponential backoff + jitter. Distinguish: per-IP vs per-user vs per-endpoint.')

**Q5: Q5**
**A:** ('How do you test rate limiter correctness under load?', 'Chaos: burst traffic, clock skew, Redis failover. Verify: no over-limiting (false positive), no under-limiting (false negative). Jepsen-style: concurrent requests, verify count. Metrics: allowed/denied ratio, latency overhead.')
## Flashcards (Spaced Repetition)

#flashcard
**Q:** Token Bucket? :: **A:** Burst allowance, smooth rate. Refill tokens/sec. Redis Lua for atomicity. Best: API Gateway #flashcard

#flashcard
**Q:** Leaky Bucket? :: **A:** Fixed rate, no burst. Queue + constant drain. Best: streaming, smooth traffic #flashcard

#flashcard
**Q:** Sliding Window Log? :: **A:** Precise, stores all timestamps. Memory heavy. Best: login, exact counting #flashcard

#flashcard
**Q:** Sliding Window Counter? :: **A:** Approximate, low memory. Weighted prev+curr window. Best: high QPS #flashcard

#flashcard
**Q:** Fixed Window? :: **A:** Simple, burst at boundaries. Best: coarse limiting #flashcard

#flashcard
**Q:** Edge vs App rate limiting? :: **A:** Edge: DDoS, IP-based, volumetric. App: user-level, business logic, premium tiers. Both needed #flashcard

#flashcard
**Q:** Rate limit response? :: **A:** HTTP 429 + Retry-After + JSON {limit, remaining, reset}. Client: exponential backoff + jitter #flashcard

#flashcard
**Q:** Distributed rate limiting? :: **A:** Redis sorted sets (sliding log) or counters (sliding window). Lua for atomicity #flashcard

#flashcard
**Q:** Token bucket in Redis? :: **A:** Lua: check tokens, decrement, refill by elapsed time. Keys: rate_limit:{user}:{window} #flashcard

#flashcard
**Q:** Per-endpoint vs per-user? :: **A:** Per-endpoint: protect expensive ops. Per-user: fair usage. Per-IP: DDoS. Layer all three #flashcard

#flashcard
**Q:** Rate limit headers? :: **A:** X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, Retry-After #flashcard

#flashcard
**Q:** Testing rate limiter? :: **A:** Chaos: burst traffic, clock skew, Redis failover. Verify no over/under-limiting. Jepsen-style #flashcard

#flashcard
**Q:** Sliding window formula? :: **A:** count = prev_window_count * (1 - overlap_ratio) + current_window_count #flashcard

#flashcard
**Q:** How to handle premium tiers? :: **A:** Different limits per tier. Store tier in user profile. Check tier before applying limit #flashcard

#flashcard
**Q:** Rate limiting GraphQL? :: **A:** Query complexity cost (fields, depth). Limit by cost, not just request count #flashcard
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