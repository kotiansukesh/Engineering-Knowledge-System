---
title: Design a URL Shortener (TinyURL)
category: Architect/10_System-Design-Interviews
tags:
- analytics
- base62
- concept/interview-prep
- difficulty/medium
- pattern/system-design
- url-shortener
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







# Design a URL Shortener (TinyURL)

> Part of [[README|MOC]] • `Architect/10_System-Design-Interviews` • Weeks 3
> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → System Design Interviews Diagram`

## Intent



## Why it Matters

- **Interview signal**: Frequently asked in system design interviews
- **Production impact**: Fundamental to scalable system design
- **Core concept**: Key building block for distributed systems

## Problems

### System Design Problem: Design a URL Shortener (TinyURL)

**Requirements:**
- See primer for detailed requirements

**Constraints:**
- High availability, scalability, fault tolerance

## Code / Example

```java
// Java 25 / Spring Boot 3.5: Core concept for Design a URL Shortener (TinyURL)
// Architecture pattern - implementation varies by system

record DesignaURLShortenerTinyURLConfig(
    String component,
    int capacity,
    String strategy
) {
    static DesignaURLShortenerTinyURLConfig ofDefaults() {
        return new DesignaURLShortenerTinyURLConfig(
            "Design a URL Shortener (TinyURL)",
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
**A:** ('Design TinyURL. How is it different from bit.ly?', 'Core: same as bit.ly. Differences: TinyURL - simpler, no analytics, no custom aliases (or limited), shorter codes (6 chars). bit.ly - analytics, custom domains, enterprise features. Architecture: Base62 of sequential ID (counter in Redis/MySQL) or hash. Redirect: 301 (cacheable) vs 302 (not cacheable).')

**Q2: Q2**
**A:** ('How do you handle custom aliases and collisions?', 'Reserved namespace (api, admin, www). Validate: alphanumeric, length, no profanity. Check DB unique index. On collision: return error, suggest alternatives.')

**Q3: Q3**
**A:** ('How do you scale redirects to 1B/day?', 'Redirect is read-heavy. CDN cache 301 (immutable). Redis Cluster for hot URLs (LFU eviction). Read replicas for DB. Async analytics (separate pipeline). Rate limit per IP.')

**Q4: Q4**
**A:** ('How do you handle link rot and expiration?', 'TTL column in DB. Background job: delete expired, or mark inactive. Redirect service: check TTL before redirect. User dashboard: show expired links.')

**Q5: Q5**
**A:** ('How do you prevent enumeration of all short URLs?', 'Use hash (MD5/SHA256) + Base62 instead of sequential ID. Or add random suffix. Rate limit redirect endpoint. robots.txt disallow.')
## Flashcards (Spaced Repetition)

#flashcard
**Q:** TinyURL vs bit.ly? :: **A:** TinyURL: simpler, no analytics, 6 chars. bit.ly: analytics, custom domains, enterprise #flashcard

#flashcard
**Q:** Key generation? :: **A:** Sequential ID (counter) + Base62 = no collision, predictable. Hash + Base62 = opaque, collision risk #flashcard

#flashcard
**Q:** Collision handling? :: **A:** Retry with salt/counter. Check DB unique constraint. Or use sequential (Snowflake) #flashcard

#flashcard
**Q:** Scale redirects to 1B/day? :: **A:** CDN cache 301. Redis Cluster for hot URLs (LFU). Read replicas. Async analytics #flashcard

#flashcard
**Q:** Custom aliases? :: **A:** Reserved namespace (api, admin). Validate: alphanumeric, length, no profanity. Unique index #flashcard

#flashcard
**Q:** Link expiration? :: **A:** TTL column. Background job delete/mark inactive. Check TTL on redirect #flashcard

#flashcard
**Q:** Prevent enumeration? :: **A:** Use hash (MD5/SHA256) + Base62. Random suffix. Rate limit. robots.txt disallow #flashcard

#flashcard
**Q:** Analytics pipeline? :: **A:** Async: click → Kafka → Flink/Spark → ClickHouse. Dimensions: geo, referrer, device #flashcard

#flashcard
**Q:** Redirect: 301 vs 302? :: **A:** 301: permanent, cacheable (CDN). 302: temporary, not cacheable. TinyURL uses 301 #flashcard

#flashcard
**Q:** Multi-region? :: **A:** Active-active: write to local, async replicate. Conflict: last-write-wins or CRDT #flashcard

#flashcard
**Q:** URL canonicalization? :: **A:** Remove fragments, sort query params, lowercase host. Prevents duplicate entries #flashcard

#flashcard
**Q:** Short code length? :: **A:** 6 chars (62^6 = 56B). 7 chars = 3.5T. Base62: [a-z][A-Z][0-9] #flashcard

#flashcard
**Q:** Database schema? :: **A:** id (BIGINT), long_url (TEXT), short_code (VARCHAR), user_id, created_at, expires_at, clicks #flashcard

#flashcard
**Q:** Cache invalidation? :: **A:** On delete: invalidate Redis. On update: update Redis. TTL as safety net #flashcard

#flashcard
**Q:** Abuse prevention? :: **A:** Rate limit create. Domain reputation. ML classification. CAPTCHA. Allow/deny lists #flashcard
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
- [[INT-01-URL-Shortener-Pastebin|Complementary: INT-01-URL-Shortener-Pastebin]]

- [[Architect/10_System-Design-Interviews/README|System Design Interviews Folder]]
- [[Architect/03_Architecture-Styles/README|Architecture Styles]]
- [[Architect/08_NonFunctional-Ops/README|Non-Functional Requirements]]
- [[Architect/07_Integration-APIs/README|Integration Patterns]]

---

*Category: Architect/10_System-Design-Interviews • Part of [[README|MOC]]*