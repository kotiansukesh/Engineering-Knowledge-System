---
title: Design Web Crawler
category: Architect/10_System-Design-Interviews
tags:
- concept/interview-prep
- crawling
- deduplication
- difficulty/hard
- pattern/system-design
- politeness
- url-frontier
- web-crawler
created: '2026-09-27'
completed: false
difficulty: Hard
reviewed: '2026-09-27'
sr-due: '2026-10-11'
source: https://github.com/donnemartin/system-design-primer
excalidraw: ''
weeks: '7'
type: note
---






# Design Web Crawler

> Part of [[README|MOC]] • `Architect/10_System-Design-Interviews` • Weeks 7
> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → System Design Interviews Diagram`

## Intent

[View exercise and solution](/donnemartin/system-design-primer/blob/master/solutions/system_design/web_crawler/README.md)

## Why it Matters

- **Interview signal**: Classic system design problem testing end-to-end design skills
- **Production impact**: Patterns used in real-world systems at scale
- **Core concepts**: Covers requirements gathering, API design, data modeling, scaling

[View exercise and solution](/donnemartin/system-design-primer/blob/master/solutions/system_design/web_crawler/README.md)

[![Imgur](/donnemartin/system-design-primer/raw/master/images/bWxPtQA.png)](/donnemartin/system-design-primer/blob/master/images/bWxPtQA.png)

## Problems

### System Design Problem: Design Web Crawler

**Requirements:**
- Crawl web pages starting from seed URLs
- Extract links and content
- Respect robots.txt and crawl delays (politeness)
- Handle deduplication (URL frontier)
- Scale to billions of pages
- Support incremental / priority crawling

**Constraints:**
- High availability (99.9%+)
- Horizontal scalability
- Fault tolerance
- Low latency (p99 < 100ms for reads)
- Data durability

## Code / Example

```java
// Java 25 / Spring Boot 3.5: Core concept for Design Web Crawler
// Architecture pattern - implementation varies by system

record DesignWebCrawlerConfig(
    String component,
    int capacity,
    String strategy
) {
    static DesignWebCrawlerConfig ofDefaults() {
        return new DesignWebCrawlerConfig(
            "Design Web Crawler",
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
**A:** ('Design a web crawler for billions of pages.', '1) URL Frontier: priority queue (priority = PageRank, recency, domain). 2) Fetcher: polite (respect robots.txt, crawl-delay), deduplication (bloom filter + URL canonicalization). 3) Parser: extract links, content, metadata. 4) Storage: raw HTML (S3), parsed content (ES), metadata (DB). 4) Scheduler: politeness per domain (token bucket), priority updates. 5) Deduplication: simhash for near-dup, exact URL dedup.')

**Q2: Q2**
**A:** ('How do you handle politeness and avoid getting blocked?', 'Per-domain rate limit (token bucket, 1 req/sec default). Respect robots.txt (cache parsed rules). Rotate user agents, IPs. Exponential backoff on 429/5xx. Distributed crawlers: coordinate via ZooKeeper/etcd.')

**Q3: Q3**
**A:** ('How do you prioritize which pages to crawl?', 'Priority = f(PageRank, update frequency, domain authority, user demand). Refresh: high-priority pages daily, low-priority monthly. Incremental: only re-crawl changed pages (ETag, Last-Modified, content hash).')

**Q4: Q4**
**A:** ('How do you store and deduplicate billions of URLs?', 'URL canonicalization: remove fragments, sort query params, lowercase host. Bloom filter (10B entries, ~1.5GB) for fast negative check. Exact dedup: URL hash -> DB (LSM tree). Simhash for near-duplicate content detection (64-bit fingerprint).')

**Q5: Q5**
**A:** ('How do you scale the fetcher horizontally?', 'Partition URL frontier by domain hash. Each fetcher worker owns domain subset. Shared nothing except frontier (Redis/DB). Auto-scale workers based on queue depth. Circuit breaker per domain.')
## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the core pattern for Design Web Crawler? :: **A:** [Key algorithm/architecture from primer] #flashcard

#flashcard
**Q:** When do you use Design Web Crawler? :: **A:** [Trigger scenarios from primer] #flashcard

#flashcard
**Q:** Key trade-off in Design Web Crawler? :: **A:** [Main trade-off] #flashcard

#flashcard
**Q:** Scale bottleneck for Design Web Crawler? :: **A:** [Primary bottleneck] #flashcard

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
- [[BB-09-Web-Crawler|Complementary: BB-09-Web-Crawler]]

- [[Architect/10_System-Design-Interviews/README|System Design Interviews Folder]]
- [[Architect/03_Architecture-Styles/README|Architecture Styles]]
- [[Architect/08_NonFunctional-Ops/README|Non-Functional Requirements]]
- [[Architect/07_Integration-APIs/README|Integration Patterns]]

---

*Category: Architect/10_System-Design-Interviews • Part of [[README|MOC]]*