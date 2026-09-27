# Practice Problems - System Design Interview Exercises

> **Purpose:** Hands-on design exercises with solution skeletons for interview preparation.
> **Format:** Each problem includes requirements, constraints, solution skeleton, and trade-off analysis.

---

## Problem Set 1: Distributed Systems Fundamentals

### 1. Design a Distributed ID Generator (Snowflake Alternative)
**Difficulty:** Medium | **Time:** 35 min

**Requirements:**
- Generate 64-bit globally unique IDs
- Roughly time-ordered (for DB index efficiency)
- 10,000 IDs/second per node
- 1,000 nodes max
- No central coordinator

**Constraints:**
- Clock drift up to 100ms
- Nodes may join/leave dynamically
- IDs must be sortable

**Solution Skeleton:**
```java
// 64-bit layout: 1|41|10|12 = sign|timestamp|node|sequence
public class DistributedIdGenerator {
    private final long nodeId;
    private long lastTimestamp = -1;
    private long sequence = 0;
    private static final long SEQUENCE_MASK = 0xFFF; // 12 bits
    
    public synchronized long nextId() {
        long timestamp = timeGen();
        if (timestamp < lastTimestamp) {
            // Handle clock drift
        }
        if (timestamp == lastTimestamp) {
            sequence = (sequence + 1) & SEQUENCE_MASK;
            if (sequence == 0) timestamp = tilNextMillis(lastTimestamp);
        } else {
            sequence = 0;
        }
        lastTimestamp = timestamp;
        return ((timestamp - EPOCH) << 22) | (nodeId << 12) | sequence;
    }
}
```

**Trade-offs:**
- Time-ordered vs UUIDv4 random
- Clock sync dependency vs coordination-free
- 64-bit fits BIGINT vs 128-bit UUID

---

### 2. Design a Rate Limiter for API Gateway
**Difficulty:** Medium | **Time:** 35 min

**Requirements:**
- Limit requests per user per endpoint
- Support multiple tiers (Free: 100/min, Pro: 1000/min, Enterprise: 10000/min)
- Sub-millisecond latency
- Distributed across 50 gateway instances

**Constraints:**
- Redis cluster with 3 shards
- Must handle burst traffic
- Graceful degradation if Redis down

**Solution Skeleton:**
```java
@Service
public class DistributedRateLimiter {
    private final RedisTemplate<String, String> redis;
    
    // Sliding Window Counter (memory efficient)
    public boolean allowRequest(String userId, String endpoint, int limit, int windowSec) {
        String key = "ratelimit:" + userId + ":" + endpoint;
        long now = System.currentTimeMillis() / 1000;
        long windowStart = now - windowSec;
        
        String lua = """
            local current = redis.call('ZRANGEBYSCORE', KEYS[1], ARGV[1], '+inf')
            if #current < tonumber(ARGV[3]) then
                redis.call('ZADD', KEYS[1], ARGV[2], ARGV[2])
                redis.call('EXPIRE', KEYS[1], ARGV[4])
                return 1
            end
            return 0
        """;
        
        return redis.execute(new DefaultRedisScript<>(lua, Boolean.class),
            key, windowStart, now, limit, windowSec + 1);
    }
}
```

**Trade-offs:**
- Sliding window log (accurate, memory heavy) vs counter (approximate, efficient)
- Per-endpoint vs per-user vs per-IP
- Local cache + async sync vs pure Redis

---

### 3. Design a Distributed Cache with Write-Through
**Difficulty:** Medium | **Time:** 40 min

**Requirements:**
- L1 (in-process, Caffeine) + L2 (Redis Cluster)
- Write-through to PostgreSQL
- TTL with jitter
- Cache tags for group invalidation

**Solution Skeleton:**
```java
@Service
public class MultiLevelCacheService {
    private final Cache<String, Object> l1Cache;  // Caffeine
    private final RedisTemplate<String, Object> l2Cache;
    private final JdbcTemplate db;
    
    public <T> T get(String key, Class<T> type, Supplier<T> loader) {
        // L1
        T val = l1Cache.getIfPresent(key);
        if (val != null) return val;
        
        // L2
        val = (T) l2Cache.opsForValue().get(key);
        if (val != null) {
            l1Cache.put(key, val);
            return val;
        }
        
        // DB
        val = loader.get();
        put(key, val);
        return val;
    }
    
    @Transactional
    public void put(String key, Object value) {
        l1Cache.put(key, value);
        l2Cache.opsForValue().set(key, value, Duration.ofMinutes(5 + random.nextInt(60)));
        db.update("UPDATE cache_data SET value=? WHERE key=?", value, key);
    }
    
    public void invalidateByTag(String tag) {
        Set<String> keys = l2Cache.opsForSet().members("cache:tag:" + tag);
        keys.forEach(k -> { l1Cache.invalidate(k); l2Cache.delete(k); });
    }
}
```

---

## Problem Set 2: Data-Intensive Applications

### 4. Design a Sharded Key-Value Store
**Difficulty:** Hard | **Time:** 45 min

**Requirements:**
- 100TB data, 1M writes/sec, 10M reads/sec
- Strong consistency per key
- Horizontal scaling (add nodes)
- Range queries on secondary index

**Solution Skeleton:**
```java
// Consistent hashing + virtual nodes
public class ShardedKVStore {
    private final ConsistentHashRouter router;  // 150 vnodes/node
    private final Map<String, ShardClient> shards;
    
    public void put(String key, byte[] value) {
        String shardId = router.getShard(key);
        shards.get(shardId).put(key, value);
    }
    
    // For range queries: maintain secondary index in separate column store
    public List<Entry> rangeQuery(String startKey, String endKey) {
        List<String> shards = router.getShardsForRange(startKey, endKey);
        return shards.parallelStream()
            .flatMap(s -> shards.get(s).scan(startKey, endKey).stream())
            .sorted(Comparator.comparing(Entry::getKey))
            .collect(Collectors.toList());
    }
}
```

---

### 5. Design a Message Queue with Exactly-Once
**Difficulty:** Hard | **Time:** 45 min

**Requirements:**
- 1M messages/sec
- Exactly-once delivery
- Message ordering per key
- 7-day retention
- Dead letter queue

**Solution Skeleton:**
```java
// Producer: idempotent + transactional
@Transactional
public void sendOrder(Order order) {
    orderRepo.save(order);  // DB
    kafkaTemplate.send("orders", order.getId(), new OrderEvent(order));  // Kafka
    kafkaTemplate.send("inventory", order.getId(), new InventoryEvent(order.getItems()));
}

// Consumer: idempotent with dedup
@KafkaListener(topics = "orders")
@Transactional
public void consume(ConsumerRecord<String, OrderEvent> record) {
    if (dedupRepo.existsByEventId(record.headers().lastHeader("event-id").value())) {
        return;
    }
    processOrder(record.value());
    dedupRepo.save(new DedupEvent(record.headers().lastHeader("event-id").value()));
}
```

---

## Problem Set 3: Real-World Systems

### 6. Design TinyURL (URL Shortener)
**Difficulty:** Medium | **Time:** 35 min

**Requirements:**
- Shorten long URLs to 6-char codes
- 100M URLs, 1B redirects/day
- Custom aliases
- Analytics (clicks, geo, referrer)
- Link expiration

**Solution Skeleton:**
```java
// Key generation: sequential ID + Base62 (no collision, predictable length)
@Service
public class UrlShortener {
    private final SnowflakeIdGenerator idGen;
    private final RedisTemplate<String, String> redis;
    private final JdbcTemplate db;
    
    public String shorten(String longUrl, String customAlias) {
        String code = customAlias != null ? customAlias : toBase62(idGen.nextId());
        
        // Atomic check-and-set
        Boolean success = redis.opsForValue()
            .setIfAbsent("url:" + code, longUrl, Duration.ofDays(365));
        if (!success) throw new DuplicateAliasException();
        
        db.update("INSERT INTO urls(code, long_url, created_at) VALUES (?,?,?)", 
            code, longUrl, Instant.now());
        return "https://tiny.url/" + code;
    }
    
    public String redirect(String code) {
        String url = redis.opsForValue().get("url:" + code);
        if (url == null) {
            url = db.queryForObject("SELECT long_url FROM urls WHERE code=?", String.class, code);
            if (url != null) redis.opsForValue().set("url:" + code, url, Duration.ofHours(1));
        }
        // Async analytics
        kafkaTemplate.send("clicks", code, new ClickEvent(code, requestInfo));
        return url;
    }
}
```

---

### 7. Design a Web Crawler
**Difficulty:** Hard | **Time:** 45 min

**Requirements:**
- Crawl 1B pages
- Respect robots.txt
- Handle JS-rendered pages
- Deduplicate near-duplicate content
- Incremental updates

**Solution Skeleton:**
```java
public class WebCrawler {
    private final PriorityBlockingQueue<UrlTask> frontier;  // Priority = PageRank
    private final BloomFilter<String> visited;  // 10B entries
    private final SimHashIndex nearDupIndex;  // 64-bit fingerprints
    
    public void crawl() {
        while (!frontier.isEmpty()) {
            UrlTask task = frontier.poll();
            if (visited.mightContain(task.url)) continue;
            
            // Politeness: per-domain rate limiter
            domainLimiter.acquire(task.domain);
            
            HttpResponse resp = fetcher.fetch(task.url);
            if (resp.isHtml()) {
                List<String> links = parser.extractLinks(resp.body());
                for (String link : links) {
                    String canonical = canonicalize(link);
                    if (!visited.mightContain(canonical)) {
                        double priority = calculatePriority(canonical, resp.pageRank());
                        frontier.offer(new UrlTask(canonical, priority));
                    }
                }
            }
            
            // Near-duplicate detection
            long fingerprint = simhash.fingerprint(resp.textContent());
            if (nearDupIndex.isNearDuplicate(fingerprint)) continue;
            nearDupIndex.add(fingerprint, task.url);
            
            visited.add(task.url);
            storage.save(task.url, resp);
        }
    }
}
```

---

### 8. Design a News Feed (Twitter/Instagram)
**Difficulty:** Hard | **Time:** 45 min

**Requirements:**
- 500M users, 100M DAU
- 1000 posts/sec per user (celebrity)
- Fan-out on write for active, pull for celebrities
- Ranking with ML model
- Real-time updates

**Solution Skeleton:**
```java
// Hybrid fan-out
@Service
public class NewsFeedService {
    private final RedisTemplate<String, String> redis;  // Sorted sets: ZSET user:feed score=timestamp
    private final KafkaTemplate<String, PostEvent> kafka;
    
    public void onPost(Post post) {
        // Push to active followers (< 10K)
        List<Long> activeFollowers = followerRepo.findActiveFollowers(post.authorId(), 10000);
        activeFollowers.parallelStream().forEach(followerId -> {
            redis.opsForZSet().add("feed:" + followerId, post.id(), post.timestamp() * post.weight());
        });
        
        // For celebrities: publish to fanout topic, pull on read
        if (followerRepo.count(post.authorId()) > 10000) {
            kafka.send("celebrity-posts", post.authorId(), post);
        }
    }
    
    public List<Post> getFeed(Long userId, int limit) {
        // Get pre-computed feed (active followees)
        Set<ZSetOperations.TypedTuple<String>> feed = redis.opsForZSet()
            .reverseRangeWithScores("feed:" + userId, 0, limit - 1);
        
        // Merge with celebrity posts (pull)
        List<Post> celebPosts = fetchCelebrityPosts(userId, limit);
        return mergeAndRank(feed, celebPosts, limit);
    }
}
```

---

### 9. Design a Chat System (WhatsApp/Slack)
**Difficulty:** Hard | **Time:** 45 min

**Requirements:**
- 1B messages/day
- 1-to-1 + group (up to 1000)
- E2E encryption (Signal Protocol)
- Message delivery receipts
- Media sharing

**Solution Skeleton:**
```java
// WebSocket gateway (stateless)
@Component
@ServerEndpoint("/ws/chat")
public class ChatGateway {
    private final SessionRegistry sessions;  // Redis: userId -> Set<sessionId>
    private final MessageService messageService;
    
    @OnMessage
    public void onMessage(Session session, String message) {
        ChatMessage msg = parse(message);
        // E2E: server never decrypts
        messageService.persist(msg);  // Partition by conversation_id
        
        // Deliver to online recipients
        Set<String> recipients = getRecipients(msg.conversationId());
        for (String recipient : recipients) {
            sessions.getSessions(recipient).forEach(s -> sendAsync(s, msg));
        }
        
        // Push for offline
        pushService.notifyOffline(recipients, msg);
    }
}

// Signal Protocol (Double Ratchet) - client side only
// Server stores: ciphertext, sender_key_id, message_number
```

---

### 10. Design Video Streaming (YouTube/Netflix)
**Difficulty:** Hard | **Time:** 45 min

**Requirements:**
- 1B hours watched/day
- Adaptive bitrate (HLS/DASH)
- Live + VOD
- DRM
- Global CDN

**Solution Skeleton:**
```java
// Upload & Transcode
@Service
public class VideoService {
    private final S3Client s3;
    private final MediaConvertClient transcoder;
    
    public String initiateUpload(String videoId, long size) {
        // Multipart upload to S3
        CreateMultipartUploadRequest req = CreateMultipartUploadRequest.builder()
            .bucket("uploads").key("raw/" + videoId).build();
        return s3.createMultipartUpload(req).uploadId();
    }
    
    @EventListener
    public void onUploadComplete(S3Event event) {
        // Transcode to ladder: 240p, 360p, 480p, 720p, 1080p, 4K
        // H.264 + VP9 + AV1
        // HLS segments (6s) + DASH (fMP4)
        JobTemplate template = JobTemplate.builder()
            .outputGroups(hlsGroup, dashGroup)
            .build();
        transcoder.createJob(CreateJobRequest.builder()
            .jobTemplate(template.name())
            .input(event.objectKey())
            .outputBucket("transcoded")
            .build());
    }
}

// Player: ABR algorithm (BOLA)
// Client measures throughput + buffer → selects quality
```

---

## Problem Set 4: Architecture Patterns

### 11. Saga Pattern for Distributed Transactions
**Difficulty:** Medium | **Time:** 30 min

**Scenario:** Order → Payment → Inventory → Shipping

**Solution:**
```java
// Choreography-based Saga
@Component
public class OrderSaga {
    @EventListener
    public void handleOrderCreated(OrderCreatedEvent e) {
        paymentService.charge(e.orderId(), e.amount())
            .onSuccess(v -> eventBus.publish(new PaymentCompletedEvent(e.orderId())))
            .onFailure(err -> eventBus.publish(new OrderFailedEvent(e.orderId(), err)));
    }
    
    @EventListener
    public void handlePaymentCompleted(PaymentCompletedEvent e) {
        inventoryService.reserve(e.orderId())
            .onSuccess(v -> eventBus.publish(new InventoryReservedEvent(e.orderId())))
            .onFailure(err -> compensatePayment(e.orderId()));
    }
    
    // Compensation actions for each step
}
```

---

### 12. CQRS + Event Sourcing
**Difficulty:** Hard | **Time:** 40 min

**Scenario:** E-commerce order management with audit trail

**Solution:**
```java
// Write model (Commands)
@Aggregate
public class OrderAggregate {
    @EventSourcingHandler
    public void on(OrderCreatedEvent e) { this.id = e.orderId(); }
    
    @CommandHandler
    public void handle(CreateOrderCommand cmd) {
        if (cmd.items().isEmpty()) throw new IllegalArgumentException();
        apply(new OrderCreatedEvent(cmd.orderId(), cmd.items(), cmd.customerId()));
    }
}

// Read model (Projections)
@Projection
public class OrderSummaryProjection {
    @EventHandler
    public void on(OrderCreatedEvent e) {
        jdbc.update("INSERT INTO order_summary(id, customer_id, total, status) VALUES (?,?,?,?)",
            e.orderId(), e.customerId(), e.total(), "CREATED");
    }
}
```

---

### 13. Leader Election with etcd/Consul
**Difficulty:** Medium | **Time:** 30 min

**Solution:**
```java
@Service
public class LeaderElection {
    private final EtcdClient etcd;
    private final String electionName;
    private final String nodeId;
    
    public boolean becomeLeader() {
        // Compare-and-swap
        TxnResponse resp = etcd.txn()
            .If(new Compare(CompareOp.VERSION, CompareTarget.KEY, electionKey, 0))
            .Then(new Put(electionKey, nodeId).withLease(leaseId))
            .Else()
            .commit();
        return resp.isSucceeded();
    }
    
    @Scheduled(fixedDelay = 5000)
    public void keepAlive() {
        if (isLeader) etcd.leaseKeepAlive(leaseId);
    }
}
```

---

## Problem Set 5: Scaling Challenges

### 14. Scale a Monolith to Microservices
**Difficulty:** Hard | **Time:** 45 min

**Steps:**
1. Identify bounded contexts (DDD)
2. Strangler Fig: route new traffic to services
3. Shared DB → separate DBs (dual-write → cutover)
4. Sync → async (event-driven)
5. Deploy independently

**Migration Checklist:**
- [ ] Service boundaries defined
- [ ] API contracts versioned
- [ ] Data ownership clear
- [ ] Observability (traces, metrics, logs)
- [ ] CI/CD per service
- [ ] Chaos engineering ready

---

### 15. Design Multi-Region Active-Active
**Difficulty:** Hard | **Time:** 45 min

**Requirements:**
- 3 regions (US, EU, APAC)
- < 100ms cross-region latency
- RPO = 0, RTO < 30s
- Conflict resolution

**Solution Skeleton:**
```java
// CRDT for conflict-free replication
public class CRDTCounter {
    private final Map<String, Long> positive = new HashMap<>();
    private final Map<String, Long> negative = new HashMap<>();
    
    public void increment(String nodeId) {
        positive.merge(nodeId, 1L, Long::sum);
    }
    
    public long value() {
        return positive.values().stream().mapToLong(Long::longValue).sum()
             - negative.values().stream().mapToLong(Long::longValue).sum();
    }
    
    public void merge(CRDTCounter other) {
        positive.keySet().forEach(k -> 
            positive.merge(k, other.positive.getOrDefault(k, 0L), Math::max));
        negative.keySet().forEach(k -> 
            negative.merge(k, other.negative.getOrDefault(k, 0L), Math::max));
    }
}
```

---

## Study Schedule

| Week | Problems | Focus |
|------|----------|-------|
| 1 | 1, 2, 3 | Fundamentals |
| 2 | 4, 5 | Data-intensive |
| 3 | 6, 7, 8 | Real-world |
| 4 | 9, 10 | Complex systems |
| 5 | 11, 12, 13 | Patterns |
| 6 | 14, 15 | Scaling |

---

## Evaluation Rubric

For each problem, self-assess:

| Criterion | Excellent (5) | Good (3) | Needs Work (1) |
|-----------|---------------|----------|----------------|
| **Requirements Clarification** | Asks clarifying Qs, defines scope | Covers main requirements | Misses key requirements |
| **High-Level Design** | Clear components, data flow | Basic architecture | Unclear or missing |
| **Data Model** | Schema, partitioning, indexes | Basic tables | No data model |
| **API Design** | REST/gRPC, versioning, errors | Basic endpoints | No API design |
| **Scaling Strategy** | Specific bottlenecks, solutions | General scaling | No scaling plan |
| **Trade-offs** | Explicit CAP, latency, cost | Some trade-offs | No trade-offs |
| **Failure Handling** | Retries, circuit breaker, DLQ | Basic retries | No failure handling |
| **Monitoring** | RED/USE metrics, alerts, dashboards | Basic logging | No monitoring |

---

*Last updated: 2025-09-27 | Add new problems to this folder as `.md` files*