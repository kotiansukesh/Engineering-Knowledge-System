---
title: Content Delivery Network (CDN)
category: Architect/10_System-Design-Interviews
tags:
- cdn
- company/amazon
- concept/interview-prep
- difficulty/easy
- pattern/system-design
- pull-cdn
- push-cdn
- static-content
created: '2026-09-27'
completed: false
difficulty: Easy
reviewed: '2026-09-10'
sr-due: '2026-09-13'
source: https://github.com/donnemartin/system-design-primer
excalidraw: ''
weeks: '2'
type: note
---




# Content Delivery Network (CDN)

> Part of [[README|MOC]] • `Architect/10_System-Design-Interviews` • Weeks 2
> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → System Design Interviews Diagram`

## Intent

[![](/donnemartin/system-design-primer/raw/master/images/h9TAuGI.jpg)](/donnemartin/system-design-primer/blob/master/images/h9TAuGI.jpg)

## Why it Matters

- **Interview signal**: Frequently asked in system design interviews
- **Production impact**: Fundamental to scalable system design
- **Core concept**: Key building block for distributed systems

[![](/donnemartin/system-design-primer/raw/master/images/h9TAuGI.jpg)](/donnemartin/system-design-primer/blob/master/images/h9TAuGI.jpg)
*[Source: Why use a CDN](https://www.creative-artworks.eu/why-use-a-content-delivery-network-cdn/)*

A content delivery network (CDN) is a globally distributed network of proxy servers, serving content from locations closer to the user. Generally, static files such as HTML/CSS/JS, photos, and videos are served from CDN, although some CDNs such as Amazon's CloudFront support dynamic content. The site's DNS resolution will tell clients which server to contact.

Serving content from CDNs can significantly improve performance in two ways:

- Users receive content from data centers close to them
- Your servers do not have to serve requests that the CDN fulfills



Push CDNs receive new content whenever changes occur on your server. You take full responsibility for providing content, uploading directly to the CDN and rewriting URLs to point to the CDN. You can configure when content expires and when it is updated. Content is uploaded only when it is new or changed, minimizing traffic, but maximizing storage.

Sites with a small amount of traffic or sites with content that isn't often updated work well with push CDNs. Content is placed on the CDNs once, instead of being re-pulled at regular intervals.

### Pull CDNs

Pull CDNs grab new content from your server when the first user requests the content. You leave the content on your server and rewrite URLs to point to the CDN. This results in a slower request until the content is cached on the CDN.

A [time-to-live (TTL)](https://en.wikipedia.org/wiki/Time_to_live) determines how long content is cached. Pull CDNs minimize storage space on the CDN, but can create redundant traffic if files expire and are pulled before they have actually changed.

Sites with heavy traffic work well with pull CDNs, as traffic is spread out more evenly with only recently-requested content remaining on the CDN.

### Disadvantage(s): CDN

- CDN costs could be significant depending on traffic, although this should be weighed with additional costs you would incur not using a CDN.
- Content might be stale if it is updated before the TTL expires it.
- CDNs require changing URLs for static content to point to the CDN.

### Source(s) and further reading

- [Globally distributed content delivery](https://figshare.com/articles/Globally_distributed_content_delivery/6605972)
- [The differences between push and pull CDNs](https://www.geeksforgeeks.org/system-design/pull-cdn-vs-push-cdn/)
- [Wikipedia](https://en.wikipedia.org/wiki/Content_delivery_network)

## Problems

### System Design Problem: Content Delivery Network (CDN)

**Requirements:**
- See primer for detailed requirements

**Constraints:**
- High availability, scalability, fault tolerance

## Code / Example

```java
// Java 25 / Spring Boot 3.5: Core concept for Content Delivery Network (CDN)
// Architecture pattern - implementation varies by system

record ContentDeliveryNetworkCDNConfig(
    String component,
    int capacity,
    String strategy
) {
    static ContentDeliveryNetworkCDNConfig ofDefaults() {
        return new ContentDeliveryNetworkCDNConfig(
            "Content Delivery Network (CDN)",
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

**Q1: Walk me through the high-level architecture for Content Delivery Network (CDN).**
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
**Q:** What is the core pattern for Content Delivery Network (CDN)? :: **A:** [Key algorithm/architecture from primer] #flashcard

#flashcard
**Q:** When do you use Content Delivery Network (CDN)? :: **A:** [Trigger scenarios from primer] #flashcard

#flashcard
**Q:** Key trade-off in Content Delivery Network (CDN)? :: **A:** [Main trade-off] #flashcard

#flashcard
**Q:** Scale bottleneck for Content Delivery Network (CDN)? :: **A:** [Primary bottleneck] #flashcard

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