---
title: Design Pastebin/URL Shortener
category: Architect/10_System-Design-Interviews
tags:
- base62
- concept/interview-prep
- difficulty/medium
- hashing
- pastebin
- pattern/system-design
- url-shortener
created: '2026-09-27'
completed: false
difficulty: Medium
reviewed: '2026-09-04'
sr-due: '2026-09-11'
source: https://github.com/donnemartin/system-design-primer
excalidraw: ''
weeks: '7'
type: note
---






# Design Pastebin/URL Shortener

> Part of [[README|MOC]] • `Architect/10_System-Design-Interviews` • Weeks 7
> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → System Design Interviews Diagram`

## Intent

[View exercise and solution](/donnemartin/system-design-primer/blob/master/solutions/system_design/pastebin/README.md)

## Why it Matters

- **Interview signal**: Classic system design problem testing end-to-end design skills
- **Production impact**: Patterns used in real-world systems at scale
- **Core concepts**: Covers requirements gathering, API design, data modeling, scaling

[View exercise and solution](/donnemartin/system-design-primer/blob/master/solutions/system_design/pastebin/README.md)

[![Imgur](/donnemartin/system-design-primer/raw/master/images/4edXG0T.png)](/donnemartin/system-design-primer/blob/master/images/4edXG0T.png)

## Problems

### System Design Problem: Design Pastebin/URL Shortener

**Requirements:**
- Shorten long URLs to short aliases (e.g., bit.ly/abc123)
- Redirect short URL to original URL
- Custom aliases support
- Expiration / TTL for links
- Analytics: click count, referrers, geography

**Constraints:**
- High availability (99.9%+)
- Horizontal scalability
- Fault tolerance
- Low latency (p99 < 100ms for reads)
- Data durability

## Code / Example

```java
// Java 25 / Spring Boot 3.5: Core concept for Design Pastebin/URL Shortener
// Architecture pattern - implementation varies by system

record DesignPastebinURLShortenerConfig(
    String component,
    int capacity,
    String strategy
) {
    static DesignPastebinURLShortenerConfig ofDefaults() {
        return new DesignPastebinURLShortenerConfig(
            "Design Pastebin/URL Shortener",
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
**A:** ('Design a URL shortener like bit.ly. Walk me through the architecture.', '1) API Gateway -> Shorten Service (stateless). 2) Key Generation: Base62 encoding of auto-increment ID (Snowflake) or hash (MD5/SHA256 + Base62, handle collisions). 3) Storage: Redis for hot URLs (LRU), MySQL/PostgreSQL for persistence. 4) Redirect Service: lookup Redis -> DB -> 301/302 redirect. 5) Analytics: async write to Kafka -> Flink/Spark -> ClickHouse. 6) Custom aliases: reserved namespace, validation. 7) TTL/expiration: TTL index or scheduled cleanup.')

**Q2: Q2**
**A:** ('How do you handle collision in hash-based key generation?', 'Retry with different salt/counter. Base62 of (hash + counter) % 62^7. Check DB unique constraint. Or use sequential IDs (Snowflake) + Base62 - no collision, but predictable. Trade-off: sequential = enumerable, hash = opaque but collision risk.')

**Q3: Q3**
**A:** ('How do you scale to 100M URLs/day?', 'Shard by hash(key) or user_id. Read replicas for redirects (99% reads). Redis Cluster for hot set. CDN for redirect responses (cache 301). Async analytics pipeline. Rate limiting per API key.')

**Q4: Q4**
**A:** ('What happens when the redirect service goes down?', 'Multi-AZ deployment. Health checks + DNS failover. Circuit breaker on upstream. Serve stale from CDN (cache 301 for 24h). Graceful degradation: return 503 with retry-after.')

**Q5: Q5**
**A:** ('How do you prevent abuse (spam, phishing)?', 'Rate limiting per IP/user. Domain reputation check. ML-based URL classification. User reporting + manual review. CAPTCHA on create. Allowlist/denylist.')
## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the core pattern for Design Pastebin/URL Shortener? :: **A:** [Key algorithm/architecture from primer] #flashcard

#flashcard
**Q:** When do you use Design Pastebin/URL Shortener? :: **A:** [Trigger scenarios from primer] #flashcard

#flashcard
**Q:** Key trade-off in Design Pastebin/URL Shortener? :: **A:** [Main trade-off] #flashcard

#flashcard
**Q:** Scale bottleneck for Design Pastebin/URL Shortener? :: **A:** [Primary bottleneck] #flashcard

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
- [[BB-08-URL-Shortener|Complementary: BB-08-URL-Shortener]]

- [[Architect/10_System-Design-Interviews/README|System Design Interviews Folder]]
- [[Architect/03_Architecture-Styles/README|Architecture Styles]]
- [[Architect/08_NonFunctional-Ops/README|Non-Functional Requirements]]
- [[Architect/07_Integration-APIs/README|Integration Patterns]]

---

*Category: Architect/10_System-Design-Interviews • Part of [[README|MOC]]*