---
title: Cache Strategies
category: Architect/10_System-Design-Interviews
tags:
- cache-aside
- concept/interview-prep
- difficulty/medium
- pattern/caching
- pattern/system-design
- refresh-ahead
- write-behind
- write-through
created: '2026-09-27'
completed: false
difficulty: Medium
reviewed: '2026-09-13'
sr-due: '2026-09-20'
source: https://github.com/donnemartin/system-design-primer
excalidraw: Cache-MultiLevel.excalidraw.json
weeks: '4'
type: note
---









# Cache Strategies

> Part of [[README|MOC]] • `Architect/10_System-Design-Interviews` • Weeks 4
> 🎨 **Visual diagram:** Open Excalidraw template: 

## Intent



## Why it Matters

- **Interview signal**: Frequently asked in system design interviews
- **Production impact**: Fundamental to scalable system design
- **Core concept**: Key building block for distributed systems

## Problems

### System Design Problem: Cache Strategies

**Requirements:**
- See primer for detailed requirements

**Constraints:**
- High availability, scalability, fault tolerance

## Code / Example

```java
// Java 25 / Spring Boot 3.5: Multi-Level Cache with Caffeine (L1) + Redis (L2)
// Production cache with write-through, cache-aside, and invalidation

package com.architect.cache;

import com.github.benmanes.caffeine.cache.Caffeine;
import org.springframework.cache.CacheManager;
import org.springframework.cache.annotation.EnableCaching;
import org.springframework.cache.caffeine.CaffeineCacheManager;
import org.springframework.data.redis.cache.RedisCacheConfiguration;
import org.springframework.data.redis.cache.RedisCacheManager;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.stereotype.Service;

import java.time.Duration;
import java.util.Map;

@Service
public class MultiLevelCacheService {

    private final CacheManager l1CacheManager; // Caffeine (in-process)
    private final CacheManager l2CacheManager; // Redis (distributed)
    private final RedisTemplate<String, Object> redisTemplate;

    public MultiLevelCacheService(CaffeineCacheManager l1, 
                                  RedisCacheManager l2,
                                  RedisTemplate<String, Object> redis) {
        this.l1CacheManager = l1;
        this.l2CacheManager = l2;
        this.redisTemplate = redis;
    }

    // Cache-Aside with L1/L2 fallback
    public <T> T get(String key, Class<T> type, java.util.function.Supplier<T> loader) {
        // L1: In-process (microsecond latency)
        var l1Cache = l1CacheManager.getCache("l1");
        T value = l1Cache.get(key, type);
        if (value != null) return value;

        // L2: Redis (millisecond latency)
        var l2Cache = l2CacheManager.getCache("l2");
        value = l2Cache.get(key, type);
        if (value != null) {
            l1Cache.put(key, value); // Populate L1
            return value;
        }

        // Miss: load from source
        value = loader.get();
        put(key, value);
        return value;
    }

    // Write-Through: write to both L1, L2, and DB
    public void put(String key, Object value) {
        var l1Cache = l1CacheManager.getCache("l1");
        var l2Cache = l2CacheManager.getCache("l2");
        
        l1Cache.put(key, value);
        l2Cache.put(key, value);
        
        // Async DB write (fire-and-forget with completion callback)
        CompletableFuture.runAsync(() -> persistToDb(key, value))
            .exceptionally(ex -> {
                // Invalidate on DB failure
                l1Cache.evict(key);
                l2Cache.evict(key);
                return null;
            });
    }

    // Event-driven invalidation via Redis pub/sub
    public void invalidate(String key) {
        l1CacheManager.getCache("l1").evict(key);
        l2CacheManager.getCache("l2").evict(key);
        
        // Publish invalidation event to other instances
        redisTemplate.convertAndSend("cache:invalidate", key);
    }

    // Cache tags for group invalidation
    public void invalidateByTag(String tag) {
        Set<String> keys = redisTemplate.opsForSet().members("cache:tag:" + tag);
        if (keys != null) {
            keys.forEach(this::invalidate);
            redisTemplate.delete("cache:tag:" + tag);
        }
    }

    private void persistToDb(String key, Object value) {
        // DB write logic
    }
}

// Configuration
@Configuration
@EnableCaching
class CacheConfig {

    @Bean
    public CaffeineCacheManager l1CacheManager() {
        CaffeineCacheManager manager = new CaffeineCacheManager("l1");
        manager.setCaffeine(Caffeine.newBuilder()
            .maximumSize(10_000)
            .expireAfterWrite(Duration.ofMinutes(5))
            .recordStats());
        return manager;
    }

    @Bean
    public RedisCacheManager l2CacheManager(RedisConnectionFactory factory) {
        RedisCacheConfiguration config = RedisCacheConfiguration.defaultCacheConfig()
            .entryTtl(Duration.ofHours(1))
            .disableCachingNullValues();
        return RedisCacheManager.builder(factory)
            .cacheDefaults(config)
            .build();
    }

    @Bean
    public RedisTemplate<String, Object> redisTemplate(RedisConnectionFactory factory) {
        RedisTemplate<String, Object> template = new RedisTemplate<>();
        template.setConnectionFactory(factory);
        template.setKeySerializer(new StringRedisSerializer());
        template.setValueSerializer(new GenericJackson2JsonRedisSerializer());
        return template;
    }
}
```
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
**A:** ('Compare cache-aside, write-through, write-behind, refresh-ahead.', 'Cache-Aside: app reads cache, misses -> DB, populates cache. Simple, eventual consistency. Write-Through: app writes cache + DB synchronously. Strong consistency, write latency = cache+DB. Write-Behind: app writes cache, async flush to DB. Low latency, risk of data loss on crash. Refresh-Ahead: async refresh before expiry. Low latency reads, complex. Choose: read-heavy -> cache-aside; write-heavy + strong consistency -> write-through; write-heavy + tolerable loss -> write-behind.')

**Q2: Q2**
**A:** ('How do you handle cache invalidation at scale?', '1) TTL + jitter (prevent thundering herd). 2) Event-driven invalidation: DB CDC (Debezium) -> Kafka -> cache workers. 3) Versioned keys: cache key includes version/hash, bump on write. 4) Write-through for critical data. 5) Cache tags: group related keys, invalidate by tag (Redis). 6) Probabilistic early expiration (random TTL +/-10%).')

**Q3: Q3**
**A:** ('What is the thundering herd problem and solutions?', 'Hot key expires -> 1000 requests hit DB simultaneously. Solutions: 1) Lock + single flight (Redis SETNX, only one fetches). 2) Stale-while-revalidate (serve stale, async refresh). 3) Jittered TTL (random +/-10-20%). 4) Pre-warm cache on deploy. 5) Request coalescing (group identical requests). 6) Circuit breaker on DB.')

**Q4: Q4**
**A:** ('How do you size cache capacity?', 'Working set analysis: 80/20 rule - 20% keys serve 80% requests. Measure: unique keys accessed in 24h, access frequency distribution. Formula: capacity = working_set * 1.5-2x headroom. Monitor: hit rate (>95% for L2, >99% for L1), eviction rate, memory pressure. Use LFU/LRU eviction.')

**Q5: Q5**
**A:** ('Multi-level caching (L1/L2) - design considerations.', 'L1: in-process (Caffeine, Guava) - microsecond latency, small (MBs). L2: distributed (Redis, Memcached) - millisecond latency, large (GBs). L1 caches L2 misses. Invalidation: L2 publishes invalidation events -> L1s subscribe. Consistency: L1 TTL short (10-60s), L2 authoritative. Sizing: L1 ~1-5% of L2.')
## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is cache-aside? :: **A:** App reads cache, on miss loads from DB, populates cache. Simple, eventual consistency #flashcard

#flashcard
**Q:** What is write-through? :: **A:** App writes to cache AND DB synchronously. Strong consistency, write latency = cache+DB #flashcard

#flashcard
**Q:** What is write-behind? :: **A:** App writes cache, async flush to DB. Low latency, risk of data loss on crash #flashcard

#flashcard
**Q:** What is refresh-ahead? :: **A:** Async refresh before expiry. Low latency reads, complex implementation #flashcard

#flashcard
**Q:** What is the thundering herd? :: **A:** Hot key expires → 1000 requests hit DB simultaneously #flashcard

#flashcard
**Q:** Thundering herd solutions? :: **A:** Single-flight (SETNX), stale-while-revalidate, jittered TTL, request coalescing #flashcard

#flashcard
**Q:** What is cache invalidation? :: **A:** Removing/updating stale cache entries. Hard problem in distributed systems #flashcard

#flashcard
**Q:** Invalidation strategies? :: **A:** TTL + jitter, event-driven (CDC), versioned keys, cache tags, probabilistic early expiry #flashcard

#flashcard
**Q:** What is multi-level caching? :: **A:** L1: in-process (Caffeine, μs). L2: distributed (Redis, ms). L1 caches L2 misses #flashcard

#flashcard
**Q:** L1 vs L2 sizing? :: **A:** L1 ~1-5% of L2. L1 TTL short (10-60s), L2 authoritative #flashcard

#flashcard
**Q:** How to size cache capacity? :: **A:** Working set analysis: 80/20 rule. Capacity = working_set * 1.5-2x headroom #flashcard

#flashcard
**Q:** What is LFU vs LRU? :: **A:** LFU: evict least frequently used. LRU: evict least recently used. LFU better for stable hot sets #flashcard

#flashcard
**Q:** Cache hit rate targets? :: **A:** L1: >99%. L2: >95%. Monitor eviction rate and memory pressure #flashcard

#flashcard
**Q:** What are cache tags? :: **A:** Group related keys, invalidate by tag (Redis SET operations) #flashcard

#flashcard
**Q:** When to use each strategy? :: **A:** Read-heavy → cache-aside. Write-heavy + strong consistency → write-through. Write-heavy + loss OK → write-behind #flashcard
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