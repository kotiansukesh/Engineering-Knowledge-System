---
title: Design a Web Crawler
category: Architect/10_System-Design-Interviews
tags:
- company/amazon
- concept/interview-prep
- deduplication
- difficulty/hard
- pattern/system-design
- politeness
- url-frontier
- web-crawler
created: '2026-09-27'
completed: false
difficulty: Hard
reviewed: '2026-09-14'
sr-due: '2026-09-28'
source: https://github.com/donnemartin/system-design-primer
excalidraw: ''
weeks: '3'
type: note
---







# Design a Web Crawler

> Part of [[README|MOC]] • `Architect/10_System-Design-Interviews` • Weeks 3
> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → System Design Interviews Diagram`

## Intent

[View exercise and solution](/donnemartin/system-design-primer/blob/master/solutions/system_design/web_crawler/README.md)

## Why it Matters

- **Interview signal**: Frequently asked in system design interviews
- **Production impact**: Fundamental to scalable system design
- **Core concept**: Key building block for distributed systems

[View exercise and solution](/donnemartin/system-design-primer/blob/master/solutions/system_design/web_crawler/README.md)

[![Imgur](/donnemartin/system-design-primer/raw/master/images/bWxPtQA.png)](/donnemartin/system-design-primer/blob/master/images/bWxPtQA.png)



[View exercise and solution](/donnemartin/system-design-primer/blob/master/solutions/system_design/mint/README.md)

[![Imgur](/donnemartin/system-design-primer/raw/master/images/V5q57vU.png)](/donnemartin/system-design-primer/blob/master/images/V5q57vU.png)

### Design the data structures for a social network

[View exercise and solution](/donnemartin/system-design-primer/blob/master/solutions/system_design/social_graph/README.md)

[![Imgur](/donnemartin/system-design-primer/raw/master/images/cdCv5g7.png)](/donnemartin/system-design-primer/blob/master/images/cdCv5g7.png)

### Design a key-value store for a search engine

[View exercise and solution](/donnemartin/system-design-primer/blob/master/solutions/system_design/query_cache/README.md)

[![Imgur](/donnemartin/system-design-primer/raw/master/images/4j99mhe.png)](/donnemartin/system-design-primer/blob/master/images/4j99mhe.png)

### Design Amazon's sales ranking by category feature

[View exercise and solution](/donnemartin/system-design-primer/blob/master/solutions/system_design/sales_rank/README.md)

[![Imgur](/donnemartin/system-design-primer/raw/master/images/MzExP06.png)](/donnemartin/system-design-primer/blob/master/images/MzExP06.png)

### Design a system that scales to millions of users on AWS

[View exercise and solution](/donnemartin/system-design-primer/blob/master/solutions/system_design/scaling_aws/README.md)

[![Imgur](/donnemartin/system-design-primer/raw/master/images/jj3A5N8.png)](/donnemartin/system-design-primer/blob/master/images/jj3A5N8.png)

## Problems

### System Design Problem: Design a Web Crawler

**Requirements:**
- See primer for detailed requirements

**Constraints:**
- High availability, scalability, fault tolerance

## Code / Example

```java
// Java 25 / Spring Boot 3.5: Core concept for Design a Web Crawler
// Architecture pattern - implementation varies by system

record DesignaWebCrawlerConfig(
    String component,
    int capacity,
    String strategy
) {
    static DesignaWebCrawlerConfig ofDefaults() {
        return new DesignaWebCrawlerConfig(
            "Design a Web Crawler",
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
**A:** ('Design a web crawler for billions of pages (ByteByteGo approach).', '1) URL Frontier: min-heap priority queue (priority = PageRank, freshness). 2) Fetcher: HTTP client pool, respect robots.txt, per-domain rate limiting (token bucket). 3) Parser: extract links, compute checksum for dedup. 4) Deduplication: URL canonicalization + bloom filter (visited) + simhash (near-dup content). 5) Storage: raw HTML (S3), parsed content (ES/DB), metadata (Cassandra). 6) Scheduler: politeness (delay per domain), priority updates. 7) Horizontal scaling: partition frontier by domain hash.')

**Q2: Q2**
**A:** ('How does ByteByteGo crawler differ from Google-scale?', 'ByteByteGo: single-region, simpler priority (PageRank + freshness), bloom filter for visited. Google: multi-region, complex ranking, Caffeine (incremental indexing), per-document indexing pipeline, massive distributed storage (Bigtable/Colossus).')

**Q3: Q3**
**A:** ('How do you handle JavaScript-heavy sites?', 'Headless browser (Puppeteer/Playwright) for rendering. Resource heavy: use selectively (high-value sites). Alternative: prerendering service. Cache rendered HTML.')

**Q4: Q4**
**A:** ('How do you handle crawl politeness and avoid bans?', 'Per-domain token bucket (configurable rate). Respect robots.txt (cached, parsed). Randomized user-agent rotation. Exponential backoff on 429/5xx. Distributed coordination via etcd/ZooKeeper for domain locks.')

**Q5: Q5**
**A:** ('How do you prioritize URLs in the frontier?', 'Priority = f(PageRank, update_frequency, domain_authority, user_demand_score). Refresh policy: high-priority daily, low-priority monthly. Incremental: only re-fetch changed (ETag, Last-Modified, content hash).')
## Flashcards (Spaced Repetition)

#flashcard
**Q:** Crawler components? :: **A:** URL Frontier (priority queue), Fetcher (HTTP pool), Parser (extract links), Dedup (bloom+simhash), Storage (S3+ES+DB) #flashcard

#flashcard
**Q:** URL Frontier? :: **A:** Min-heap priority queue. Priority = PageRank + freshness. Per-domain queues for politeness #flashcard

#flashcard
**Q:** Politeness? :: **A:** Per-domain token bucket (1 req/sec default). Respect robots.txt. Exponential backoff on 429/5xx #flashcard

#flashcard
**Q:** Deduplication? :: **A:** URL canonicalization + bloom filter (visited) + simhash (near-dup content, 64-bit fingerprint) #flashcard

#flashcard
**Q:** JavaScript-heavy sites? :: **A:** Headless browser (Puppeteer/Playwright) for rendering. Use selectively. Cache rendered HTML #flashcard

#flashcard
**Q:** Prioritization? :: **A:** Priority = f(PageRank, update_freq, domain_authority, user_demand). High: daily, Low: monthly #flashcard

#flashcard
**Q:** Incremental crawling? :: **A:** Only re-fetch changed: ETag, Last-Modified, content hash. Conditional GET #flashcard

#flashcard
**Q:** Storage? :: **A:** Raw HTML → S3. Parsed content → Elasticsearch. Metadata → Cassandra/DB #flashcard

#flashcard
**Q:** Distributed coordination? :: **A:** Partition frontier by domain hash. etcd/ZooKeeper for domain locks. Shared nothing #flashcard

#flashcard
**Q:** Crawl budget? :: **A:** Max pages per domain per time window. Respect robots.txt crawl-delay #flashcard

#flashcard
**Q:** Simhash? :: **A:** 64-bit fingerprint. Hamming distance < 3 = near-duplicate. LSH for scaling #flashcard

#flashcard
**Q:** Bloom filter sizing? :: **A:** 10B entries, 1% false positive = ~1.5GB. Scalable bloom filter for growth #flashcard

#flashcard
**Q:** Monitoring? :: **A:** Pages crawled/sec, queue depth, dedup rate, error rate, politeness violations #flashcard

#flashcard
**Q:** ByteByteGo vs Google? :: **A:** ByteByteGo: single-region, simpler priority. Google: multi-region, Caffeine, Bigtable, Colossus #flashcard

#flashcard
**Q:** robots.txt handling? :: **A:** Cache parsed rules per domain. Respect Disallow, crawl-delay, Sitemap #flashcard
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
- [[INT-03-Web-Crawler|Complementary: INT-03-Web-Crawler]]

- [[Architect/10_System-Design-Interviews/README|System Design Interviews Folder]]
- [[Architect/03_Architecture-Styles/README|Architecture Styles]]
- [[Architect/08_NonFunctional-Ops/README|Non-Functional Requirements]]
- [[Architect/07_Integration-APIs/README|Integration Patterns]]

---

*Category: Architect/10_System-Design-Interviews • Part of [[README|MOC]]*