#!/usr/bin/env python3
"""
Deepen Interview Q&A for top 20 patterns in Architect/10_System-Design-Interviews
"""

import yaml
import re
from pathlib import Path

TARGET = Path('/Users/sukesh/Documents/GitHub/Obsidian/Architect/10_System-Design-Interviews')

# Top 20 patterns for deep Q&A
TOP_20 = [
    'FND-04-CAP-Theorem.md',
    'NET-01-Load-Balancer.md',
    'DB-05-Sharding.md',
    'CACHE-02-Cache-Strategies.md',
    'ASYNC-02-Message-Queues.md',
    'INT-01-URL-Shortener-Pastebin.md',
    'INT-02-Twitter-Timeline.md',
    'INT-03-Web-Crawler.md',
    'BB-01-Scaling-Zero-to-Millions.md',
    'BB-04-Rate-Limiter.md',
    'BB-05-Consistent-Hashing.md',
    'BB-06-Key-Value-Store.md',
    'BB-07-Unique-ID-Generator-Snowflake.md',
    'BB-08-URL-Shortener.md',
    'BB-09-Web-Crawler.md',
    'BB-10-Notification-System.md',
    'BB-11-News-Feed-System.md',
    'BB-12-Chat-System.md',
    'BB-14-YouTube-Video-Streaming.md',
    'BB-19-Distributed-Message-Queue.md',
]

DEEP_QA = {
    'FND-04-CAP-Theorem.md': {
        'Q1': ('Walk me through the CAP theorem and why it matters in practice.',
               'CAP states you can only guarantee 2 of 3: Consistency (linearizability), Availability (every request succeeds), Partition Tolerance (system works despite network failures). Since networks WILL partition, the real choice is CP vs AP. CP (e.g., HBase, ZooKeeper) blocks writes during partition to ensure consistency. AP (e.g., Cassandra, DynamoDB) accepts writes on both sides, reconciling later. Most systems are AP for user-facing features, CP for coordination/metadata.'),
        'Q2': ('How do you handle the consistency-availability trade-off in a real system?',
               'Use hybrid approach: CP for metadata/coordination (ZooKeeper, etcd, Consul), AP for user data. Implement tunable consistency per operation (Cassandra QUORUM, DynamoDB strong/read-after-write). Use read-repair, hinted handoff, anti-entropy for eventual consistency. For financial data, use synchronous replication + consensus (Raft/Paxos).'),
        'Q3': ('What happens during a network partition in a CP system vs AP system?',
               'CP: Minority partition becomes unavailable (rejects writes, may serve stale reads if configured). Majority continues. AP: Both partitions accept writes. Conflict resolution on merge (last-write-wins, CRDTs, application-level). Risk: split-brain, data loss, divergence.'),
        'Q4': ('How do you test partition tolerance in CI/CD?',
               'Chaos engineering: inject network partitions (tc/netem, Chaos Mesh, Litmus). Test: minority partition unavailability (CP), write acceptance on both sides (AP), merge behavior, data integrity. Tools: Jepsen tests for linearizability verification.'),
        'Q5': ('What monitoring tells you if CAP trade-off is working?',
               'CP: replication lag, leader election frequency, quorum availability. AP: conflict rate, read-repair rate, hinted handoff queue, divergence metrics (vector clocks). Both: p99 latency, error rate, availability SLO.'),
    },
    'NET-01-Load-Balancer.md': {
        'Q1': ('Design a load balancer from scratch. What are the key components?',
               '1) Health checker (active/passive, HTTP/TCP/gRPC). 2) Algorithm (round-robin, least-connections, least-time, consistent-hash, weighted). 3) Connection pool/state table. 4) SSL termination (hardware offload or software). 5) Layer 4 (TCP/UDP) vs Layer 7 (HTTP) routing. 6) HA setup: active-passive (VRRP) or active-active (anycast/ECMP). 7) Metrics: RED (rate, errors, duration) per backend.'),
        'Q2': ('L4 vs L7 load balancing - when to use each?',
               'L4: TCP/UDP, lower latency (~1ms), no HTTP parsing, no cookie affinity, no content routing. Use for: raw throughput, non-HTTP protocols, TLS passthrough. L7: HTTP-aware, path/host routing, cookie affinity, SSL termination, WAF, compression. Use for: microservices, API gateways, canary deployments. Most modern systems use both: L4 at edge, L7 per service.'),
        'Q3': ('How do you handle session persistence without sticky sessions?',
               'Stateless design: external session store (Redis, DB). JWT with short expiry + refresh tokens. Client-side affinity via consistent hashing (IP + user-agent). If sticky required: cookie-based (insert cookie), source IP hash (problematic behind NAT). Prefer stateless.'),
        'Q4': ('What happens when a backend becomes unhealthy?',
               'Active checks: remove from pool after N consecutive failures. Passive checks: track 5xx/timeout rate, eject if > threshold. Graceful drain: stop new connections, wait for in-flight (drain timeout). Circuit breaker: fast-fail before health check catches up. Slow-start: gradually add back after recovery.'),
        'Q5': ('How do you scale the load balancer itself?',
               'Horizontal: DNS round-robin, anycast IP, ECMP. Cloud: ALB/NLB/GCLB auto-scale. On-prem: HAProxy/Envoy cluster with keepalived/VRRP or BGP anycast. State sync: connection table replication (expensive) or stateless (prefer). Metrics: connections/sec, active connections, CPU, memory.'),
    },
    'DB-05-Sharding.md': {
        'Q1': ('Walk me through sharding strategy for a user table with 1B rows.',
               '1) Choose shard key: user_id (hash) for even distribution, or tenant_id for multi-tenant isolation. 2) Algorithm: consistent hashing (ketama) for minimal reshuffle, or range-based for ordered scans. 3) Virtual nodes (150-200 per physical) to prevent hotspots. 4) Routing layer: proxy (Vitess, ProxySQL) or client-side (driver-aware). 5) Resharding: split/merge shards, dual-write during migration, validate with shadow traffic.'),
        'Q2': ('What are the hotspot problems and how do you solve them?',
               'Power users (celebrity, bot) concentrate load on one shard. Solutions: 1) Separate hot keys to dedicated shards. 2) Local cache (Redis) for hot keys. 3) Consistent hashing with bounded loads (Google consistent hashing with bounded loads). 4) Request hedging for tail latency. 5) Rate limiting per shard key.'),
        'Q3': ('How do you handle cross-shard transactions?',
               'Avoid if possible. If needed: 1) Saga pattern (choreography/orchestration) with compensating transactions. 2) Two-phase commit (2PC) - rare, blocks. 3) Eventual consistency: dual-write to outbox table + CDC (Debezium) to event bus. 4) Denormalize to keep data co-located. 5) Use distributed transactions only for critical paths (payments).'),
        'Q4': ('How do you reshard without downtime?',
               '1) Add new shards to ring. 2) Dual-write to old + new shards. 3) Backfill historical data (batch, low priority). 4) Verify consistency (checksum, row count). 5) Switch reads to new shards (canary). 6) Stop dual-write, remove old shards. Tools: Vitess, gh-ost, pt-online-schema-change.'),
        'Q5': ('How do you monitor shard health?',
               'Per-shard: QPS, latency (p50/p99), error rate, connection count, disk usage, replication lag. Cross-shard: shard size distribution (target +/-10%), hotspot detection (top 1% keys > 50% QPS), migration progress. Alerts: shard > 80% capacity, replication lag > 30s, QPS drop > 50%.'),
    },
    'CACHE-02-Cache-Strategies.md': {
        'Q1': ('Compare cache-aside, write-through, write-behind, refresh-ahead.',
               'Cache-Aside: app reads cache, misses -> DB, populates cache. Simple, eventual consistency. Write-Through: app writes cache + DB synchronously. Strong consistency, write latency = cache+DB. Write-Behind: app writes cache, async flush to DB. Low latency, risk of data loss on crash. Refresh-Ahead: async refresh before expiry. Low latency reads, complex. Choose: read-heavy -> cache-aside; write-heavy + strong consistency -> write-through; write-heavy + tolerable loss -> write-behind.'),
        'Q2': ('How do you handle cache invalidation at scale?',
               '1) TTL + jitter (prevent thundering herd). 2) Event-driven invalidation: DB CDC (Debezium) -> Kafka -> cache workers. 3) Versioned keys: cache key includes version/hash, bump on write. 4) Write-through for critical data. 5) Cache tags: group related keys, invalidate by tag (Redis). 6) Probabilistic early expiration (random TTL +/-10%).'),
        'Q3': ('What is the thundering herd problem and solutions?',
               'Hot key expires -> 1000 requests hit DB simultaneously. Solutions: 1) Lock + single flight (Redis SETNX, only one fetches). 2) Stale-while-revalidate (serve stale, async refresh). 3) Jittered TTL (random +/-10-20%). 4) Pre-warm cache on deploy. 5) Request coalescing (group identical requests). 6) Circuit breaker on DB.'),
        'Q4': ('How do you size cache capacity?',
               'Working set analysis: 80/20 rule - 20% keys serve 80% requests. Measure: unique keys accessed in 24h, access frequency distribution. Formula: capacity = working_set * 1.5-2x headroom. Monitor: hit rate (>95% for L2, >99% for L1), eviction rate, memory pressure. Use LFU/LRU eviction.'),
        'Q5': ('Multi-level caching (L1/L2) - design considerations.',
               'L1: in-process (Caffeine, Guava) - microsecond latency, small (MBs). L2: distributed (Redis, Memcached) - millisecond latency, large (GBs). L1 caches L2 misses. Invalidation: L2 publishes invalidation events -> L1s subscribe. Consistency: L1 TTL short (10-60s), L2 authoritative. Sizing: L1 ~1-5% of L2.'),
    },
    'ASYNC-02-Message-Queues.md': {
        'Q1': ('Design a message queue system. Compare Kafka, RabbitMQ, Pulsar.',
               'Kafka: log-based, high throughput, replay, ordered per partition, retention by time/size. RabbitMQ: broker-based, flexible routing (exchange/queue), lower latency, message acknowledgment, TTL. Pulsar: tiered storage, geo-replication, multi-tenancy, separation of compute/storage. Choose Kafka for event streaming/log aggregation; RabbitMQ for task queues/RPC; Pulsar for multi-tenant/cloud-native.'),
        'Q2': ('How do you guarantee exactly-once semantics?',
               'True exactly-once is hard. Kafka: idempotent producer (PID + sequence) + transactional API (atomic write to multiple partitions). Consumer: process + commit offset in same transaction. RabbitMQ: publisher confirms + consumer acks + deduplication (message ID). Application-level: idempotent consumers (dedup keys, upserts).'),
        'Q3': ('How do you handle message ordering at scale?',
               'Per-partition ordering (Kafka) or per-queue (RabbitMQ). Key: partition by correlation key (user_id, order_id). For global ordering: single partition (throughput limit). Trade-off: parallelism vs ordering. Use sequencing tokens for cross-partition ordering.'),
        'Q4': ('What about dead letter queues and retry strategies?',
               'Exponential backoff: 1s, 2s, 4s, 8s, max 5 retries. DLQ after max retries. Separate retry topic/queue per attempt count. Alert on DLQ growth. Poison pill detection: message processed > N times -> DLQ. Replay: fix bug, replay from DLQ or original topic with offset reset.'),
        'Q5': ('How do you monitor queue health?',
               'Lag: consumer offset vs producer offset (target < 1000). Throughput: msg/s in/out. Latency: produce-to-consume (p50/p99). Error rate. DLQ size. Under-replicated partitions (Kafka). Queue depth, memory, disk (RabbitMQ).'),
    },
    'INT-01-URL-Shortener-Pastebin.md': {
        'Q1': ('Design a URL shortener like bit.ly. Walk me through the architecture.',
               '1) API Gateway -> Shorten Service (stateless). 2) Key Generation: Base62 encoding of auto-increment ID (Snowflake) or hash (MD5/SHA256 + Base62, handle collisions). 3) Storage: Redis for hot URLs (LRU), MySQL/PostgreSQL for persistence. 4) Redirect Service: lookup Redis -> DB -> 301/302 redirect. 5) Analytics: async write to Kafka -> Flink/Spark -> ClickHouse. 6) Custom aliases: reserved namespace, validation. 7) TTL/expiration: TTL index or scheduled cleanup.'),
        'Q2': ('How do you handle collision in hash-based key generation?',
               'Retry with different salt/counter. Base62 of (hash + counter) % 62^7. Check DB unique constraint. Or use sequential IDs (Snowflake) + Base62 - no collision, but predictable. Trade-off: sequential = enumerable, hash = opaque but collision risk.'),
        'Q3': ('How do you scale to 100M URLs/day?',
               'Shard by hash(key) or user_id. Read replicas for redirects (99% reads). Redis Cluster for hot set. CDN for redirect responses (cache 301). Async analytics pipeline. Rate limiting per API key.'),
        'Q4': ('What happens when the redirect service goes down?',
               'Multi-AZ deployment. Health checks + DNS failover. Circuit breaker on upstream. Serve stale from CDN (cache 301 for 24h). Graceful degradation: return 503 with retry-after.'),
        'Q5': ('How do you prevent abuse (spam, phishing)?',
               'Rate limiting per IP/user. Domain reputation check. ML-based URL classification. User reporting + manual review. CAPTCHA on create. Allowlist/denylist.'),
    },
    'INT-02-Twitter-Timeline.md': {
        'Q1': ('Design Twitter timeline. How do you generate home timeline for 300M users?',
               'Two approaches: 1) Fan-out on write (push): when user tweets, push to all followers\' timeline caches (Redis). Write amplification: 300M * avg_followers. 2) Fan-out on read (pull): merge followee tweets at read time. Hybrid: push for active users (<10K followers), pull for celebrities. Use Redis sorted sets (score = timestamp). Pre-compute timelines for active users.'),
        'Q2': ('How do you handle celebrity with 50M followers?',
               'Do NOT fan-out on write. On read: merge celebrity tweets separately. Cache celebrity tweets in separate key. Use "pull" for high-follower accounts. Fan-out threshold: ~10K followers.'),
        'Q3': ('How do you handle tweet deletion and edit?',
               'Delete: remove from author timeline + fan-out delete to follower timelines (async, best-effort). Edit: not supported historically; if added, version tweets, update in place with edit timestamp.'),
        'Q4': ('How do you rank tweets (algorithmic timeline)?',
               'Features: recency, engagement (likes/retweets/replies), author affinity, media type, user preferences. Model: LightGBM/XGBoost, trained daily. Serve: candidate generation (followees + recommendations) -> ranking -> diversification -> cache. A/B test ranking changes.'),
        'Q5': ('How do you scale search across 500M tweets/day?',
               'Inverted index (Lucene/Elasticsearch). Shard by time (hourly/daily indices). Real-time indexing: Kafka -> Flink -> ES. Query: fan-out to shards, merge top-K. Cache frequent queries.'),
    },
    'INT-03-Web-Crawler.md': {
        'Q1': ('Design a web crawler for billions of pages.',
               '1) URL Frontier: priority queue (priority = PageRank, recency, domain). 2) Fetcher: polite (respect robots.txt, crawl-delay), deduplication (bloom filter + URL canonicalization). 3) Parser: extract links, content, metadata. 4) Storage: raw HTML (S3), parsed content (ES), metadata (DB). 4) Scheduler: politeness per domain (token bucket), priority updates. 5) Deduplication: simhash for near-dup, exact URL dedup.'),
        'Q2': ('How do you handle politeness and avoid getting blocked?',
               'Per-domain rate limit (token bucket, 1 req/sec default). Respect robots.txt (cache parsed rules). Rotate user agents, IPs. Exponential backoff on 429/5xx. Distributed crawlers: coordinate via ZooKeeper/etcd.'),
        'Q3': ('How do you prioritize which pages to crawl?',
               'Priority = f(PageRank, update frequency, domain authority, user demand). Refresh: high-priority pages daily, low-priority monthly. Incremental: only re-crawl changed pages (ETag, Last-Modified, content hash).'),
        'Q4': ('How do you store and deduplicate billions of URLs?',
               'URL canonicalization: remove fragments, sort query params, lowercase host. Bloom filter (10B entries, ~1.5GB) for fast negative check. Exact dedup: URL hash -> DB (LSM tree). Simhash for near-duplicate content detection (64-bit fingerprint).'),
        'Q5': ('How do you scale the fetcher horizontally?',
               'Partition URL frontier by domain hash. Each fetcher worker owns domain subset. Shared nothing except frontier (Redis/DB). Auto-scale workers based on queue depth. Circuit breaker per domain.'),
    },
    'BB-01-Scaling-Zero-to-Millions.md': {
        'Q1': ('Walk me through scaling a service from zero to millions of users.',
               'Phase 1 (0-10K): Monolith + single DB + vertical scaling. Phase 2 (10K-100K): Read replicas, caching (Redis), CDN for static assets. Phase 3 (100K-1M): Sharding, async processing (message queues), microservices split. Phase 4 (1M+): Multi-region, active-active, custom infrastructure. Key principle: scale bottleneck first, measure before optimizing.'),
        'Q2': ('What are the first 3 bottlenecks you hit and how do you fix them?',
               '1) Database CPU: read replicas + caching. 2) Network bandwidth: CDN + compression. 3) Single-threaded app: stateless horizontal scaling + load balancer. Then: DB connections (pooling), locks (optimistic locking), GC pauses (tuning).'),
        'Q3': ('How do you decide when to split microservices?',
               'Team ownership boundaries (2-pizza team). Independent deployability. Different scaling needs. Different tech stacks. Data ownership. Start with modular monolith, extract when pain > cost. Strangler fig pattern.'),
        'Q4': ('How do you handle distributed transactions across services?',
               'Saga pattern (choreography via events or orchestration via central coordinator). Compensating transactions for rollback. Outbox pattern for reliability. Avoid 2PC. Eventual consistency with idempotency.'),
        'Q5': ('What monitoring do you put in place at each phase?',
               'Phase 1: APM (latency, errors), DB metrics. Phase 2: Cache hit rate, queue depth. Phase 3: Service mesh metrics (latency, error rate per service), distributed tracing. Phase 4: SLOs, error budgets, chaos engineering.'),
    },
    'BB-04-Rate-Limiter.md': {
        'Q1': ('Design a distributed rate limiter. Compare algorithms.',
               'Token Bucket: burst allowance, smooth rate. Leaky Bucket: fixed rate, no burst. Sliding Window Log: precise, memory heavy. Sliding Window Counter: approximate, low memory. Fixed Window: simple, burst at boundaries. Distributed: Redis (Lua script for atomicity) or local + sync. Choose: API gateway -> token bucket; login -> sliding window; streaming -> leaky bucket.'),
        'Q2': ('How do you implement token bucket in Redis atomically?',
               'Lua script: check tokens, decrement, refill based on elapsed time. Return allowed/remaining. Keys: rate_limit:{user_id}:{window}. TTL = window + buffer. Pipeline for batch checks.'),
        'Q3': ('How do you handle rate limiting at edge vs application layer?',
               'Edge (Cloudflare, AWS WAF, Envoy): DDoS protection, IP-based, low latency. Application: user-level, API-key level, business logic aware (e.g., premium tier). Both needed: edge for volumetric, app for semantic.'),
        'Q4': ('How do you handle rate limit exceeded responses?',
               'HTTP 429 with Retry-After header. JSON body: {limit, remaining, reset}. Client: exponential backoff + jitter. Distinguish: per-IP vs per-user vs per-endpoint.'),
        'Q5': ('How do you test rate limiter correctness under load?',
               'Chaos: burst traffic, clock skew, Redis failover. Verify: no over-limiting (false positive), no under-limiting (false negative). Jepsen-style: concurrent requests, verify count. Metrics: allowed/denied ratio, latency overhead.'),
    },
    'BB-05-Consistent-Hashing.md': {
        'Q1': ('Explain consistent hashing and why it is used for sharding.',
               'Maps keys and nodes to a ring (0 to 2^32-1). Key goes to next clockwise node. Adding/removing node only affects adjacent keys (K/N keys moved vs all). Virtual nodes (vnodes) distribute load evenly. Ketama algorithm: 160 vnodes per physical node.'),
        'Q2': ('How do you handle hotspots with consistent hashing?',
               'Bounded loads (Google): each node has capacity, route to next node if overloaded. Virtual node weight adjustment. Separate hot keys to dedicated nodes. Local cache (Redis) for top keys.'),
        'Q3': ('How does consistent hashing compare to range-based sharding?',
               'Consistent: minimal reshuffle on add/remove, good for dynamic clusters. Range: ordered scans, easier debugging, but hotspots on sequential keys, reshuffle on split/merge. Choose consistent for caching, range for time-series/analytics.'),
        'Q4': ('How do you implement consistent hashing in production?',
               'Library: hashicorp/memberlist, Spotify DNS, or custom. Ring: sorted array of (hash, node). Binary search for key. Vnodes: 100-200 per node. Health checks: remove unhealthy nodes from ring.'),
        'Q5': ('What happens during network partition in consistent hashing ring?',
               'Nodes may have different ring views. Use gossip (SWIM) for membership. Split-brain: two rings. Resolve: quorum, last-write-wins, or pause writes. Prefer CP for metadata, AP for data.'),
    },
    'BB-06-Key-Value-Store.md': {
        'Q1': ('Design a key-value store like Cassandra/DynamoDB. Core components?',
               '1) LSM Tree: MemTable (in-memory, sorted) -> SSTables (immutable, disk). 2) Compaction: merge SSTables, remove tombstones. 3) WAL: durability for MemTable. 4) Bloom filter: fast negative lookups. 5) Partitioning: consistent hashing + vnodes. 6) Replication: quorum (R+W>N). 7) Gossip: membership, failure detection.'),
        'Q2': ('Explain LSM tree compaction strategies.',
               'Size-tiered: merge same-size SSTables (write-optimized). Leveled: merge into levels (read-optimized, space-amplification lower). Universal: mix of both. Choose: write-heavy -> size-tiered; read-heavy -> leveled.'),
        'Q3': ('How do you handle range queries on hash-partitioned data?',
               'Hash partitioning kills range queries. Solutions: 1) Secondary index (local per shard, scatter-gather). 2) Composite key: (tenant_id, timestamp) -> range within tenant. 3) Dual-write to column store (ClickHouse) for analytics. 4) Scan all shards (expensive).'),
        'Q4': ('How do you achieve strong consistency with quorum?',
               'R + W > N. Typical: N=3, W=2, R=2 (strong). DynamoDB: consistent read = quorum. Cassandra: QUORUM. Trade-off: latency (wait for acks), availability (minority partition unavailable).'),
        'Q5': ('How do you handle TTL and tombstone garbage collection?',
               'TTL per cell. Tombstones written on delete. Compaction removes tombstones (after gc_grace_seconds). Risk: tombstone resurrection if node down > gc_grace. Monitor: tombstone ratio, compaction backlog.'),
    },
    'BB-07-Unique-ID-Generator-Snowflake.md': {
        'Q1': ('Design a distributed unique ID generator (Snowflake).',
               '64-bit: 1 bit sign (0), 41 bits timestamp (ms since epoch, ~69 years), 10 bits machine ID (1024 nodes), 12 bits sequence (4096/ms per node). Total: ~4M IDs/sec per node. Monotonic increasing, roughly time-ordered.'),
        'Q2': ('What happens if clock goes backwards?',
               'Wait for clock catch-up (block). Or reject request. Or use logical clock (increment sequence). Guard: max drift threshold (e.g., 100ms). Log alert. NTP sync required.'),
        'Q3': ('How do you assign machine IDs in dynamic environments (K8s)?',
               'Static: config file. Dynamic: etcd/Consul/ZooKeeper lease. Kubernetes: pod UID hash modulo 1024. Or use 5 bits for DC, 5 for pod.'),
        'Q4': ('How do you handle ID exhaustion (sequence overflow)?',
               'Sequence: 12 bits = 4096/ms. If exceeded: wait next ms. At 4M IDs/sec, need 1000 nodes. Monitor: sequence usage %, alert > 80%.'),
        'Q5': ('Snowflake vs UUID vs ULID vs NanoID.',
               'Snowflake: time-ordered, 64-bit, needs coordination. UUIDv4: random, 128-bit, no coordination, not ordered. UUIDv7: time-ordered, 128-bit. ULID: 128-bit, time-ordered, case-insensitive. NanoID: URL-safe, customizable. Choose Snowflake for DB primary keys (index-friendly).'),
    },
    'BB-08-URL-Shortener.md': {
        'Q1': ('Design TinyURL. How is it different from bit.ly?',
               'Core: same as bit.ly. Differences: TinyURL - simpler, no analytics, no custom aliases (or limited), shorter codes (6 chars). bit.ly - analytics, custom domains, enterprise features. Architecture: Base62 of sequential ID (counter in Redis/MySQL) or hash. Redirect: 301 (cacheable) vs 302 (not cacheable).'),
        'Q2': ('How do you handle custom aliases and collisions?',
               'Reserved namespace (api, admin, www). Validate: alphanumeric, length, no profanity. Check DB unique index. On collision: return error, suggest alternatives.'),
        'Q3': ('How do you scale redirects to 1B/day?',
               'Redirect is read-heavy. CDN cache 301 (immutable). Redis Cluster for hot URLs (LFU eviction). Read replicas for DB. Async analytics (separate pipeline). Rate limit per IP.'),
        'Q4': ('How do you handle link rot and expiration?',
               'TTL column in DB. Background job: delete expired, or mark inactive. Redirect service: check TTL before redirect. User dashboard: show expired links.'),
        'Q5': ('How do you prevent enumeration of all short URLs?',
               'Use hash (MD5/SHA256) + Base62 instead of sequential ID. Or add random suffix. Rate limit redirect endpoint. robots.txt disallow.'),
    },
    'BB-09-Web-Crawler.md': {
        'Q1': ('Design a web crawler for billions of pages (ByteByteGo approach).',
               '1) URL Frontier: min-heap priority queue (priority = PageRank, freshness). 2) Fetcher: HTTP client pool, respect robots.txt, per-domain rate limiting (token bucket). 3) Parser: extract links, compute checksum for dedup. 4) Deduplication: URL canonicalization + bloom filter (visited) + simhash (near-dup content). 5) Storage: raw HTML (S3), parsed content (ES/DB), metadata (Cassandra). 6) Scheduler: politeness (delay per domain), priority updates. 7) Horizontal scaling: partition frontier by domain hash.'),
        'Q2': ('How does ByteByteGo crawler differ from Google-scale?',
               'ByteByteGo: single-region, simpler priority (PageRank + freshness), bloom filter for visited. Google: multi-region, complex ranking, Caffeine (incremental indexing), per-document indexing pipeline, massive distributed storage (Bigtable/Colossus).'),
        'Q3': ('How do you handle JavaScript-heavy sites?',
               'Headless browser (Puppeteer/Playwright) for rendering. Resource heavy: use selectively (high-value sites). Alternative: prerendering service. Cache rendered HTML.'),
        'Q4': ('How do you handle crawl politeness and avoid bans?',
               'Per-domain token bucket (configurable rate). Respect robots.txt (cached, parsed). Randomized user-agent rotation. Exponential backoff on 429/5xx. Distributed coordination via etcd/ZooKeeper for domain locks.'),
        'Q5': ('How do you prioritize URLs in the frontier?',
               'Priority = f(PageRank, update_frequency, domain_authority, user_demand_score). Refresh policy: high-priority daily, low-priority monthly. Incremental: only re-fetch changed (ETag, Last-Modified, content hash).'),
    },
    'BB-10-Notification-System.md': {
        'Q1': ('Design a notification system (push, email, SMS, in-app).',
               '1) API Gateway -> Notification Service (stateless). 2) Template Engine: render per channel. 3) Channel Adapters: FCM/APNs (push), SendGrid/Twilio (email/SMS), WebSocket (in-app). 4) Queue: Kafka (high throughput) or RabbitMQ (lower). 5) Preferences: user opt-in/out per channel/type. 6) Deduplication: prevent duplicate sends. 7) Retry: exponential backoff + DLQ. 8) Analytics: delivery, open, click rates.'),
        'Q2': ('How do you handle 10M concurrent WebSocket connections?',
               'Connection server cluster (stateless). Redis pub/sub for message routing. Connection sharding by user_id. Heartbeat (ping/pong) for liveness. Offload TLS to load balancer. Horizontal scale: add connection servers.'),
        'Q3': ('How do you guarantee delivery for critical notifications (OTP, alerts)?',
               'Multi-channel fallback: push -> SMS -> email. Idempotent send (dedup key). Synchronous send for critical (wait for provider ack). Retry with exponential backoff. Alert on DLQ.'),
        'Q4': ('How do you handle user preferences and timezone?',
               'Preference service: per-user, per-type, per-channel. Quiet hours (timezone-aware). Frequency capping (max N/day). Unsubscribe link in every email. GDPR compliance (right to delete).'),
        'Q5': ('How do you scale the notification pipeline?',
               'Partition Kafka by user_id. Consumer groups per channel. Horizontal scale workers. Backpressure: pause consumption if downstream slow. Metrics: queue lag, delivery latency, success rate per channel.'),
    },
    'BB-11-News-Feed-System.md': {
        'Q1': ('Design Facebook/Instagram news feed. Fan-out on write vs read?',
               'Hybrid: push for active users (<5K followers), pull for celebrities. Write path: post -> fan-out to follower timelines (Redis sorted sets, score = timestamp * weight). Read path: merge followee timelines + ranked candidates. Ranking: LightGBM model (engagement, affinity, recency). Cache: pre-computed feeds for active users.'),
        'Q2': ('How do you handle ranking at scale?',
               'Two-stage: 1) Candidate generation: followees + recommendations (collaborative filtering, content-based) -> 1000 candidates. 2) Ranking: pointwise/pairwise/listwise model (XGBoost/LightGBM). Features: user-user affinity, content type, recency, engagement history. Serving: TensorFlow Serving / Triton. A/B test models.'),
        'Q3': ('How do you handle real-time updates (new post, like, comment)?',
               'Write path: on new post, fan-out to active followers (async, Kafka). On like/comment: update counters (Redis), invalidate feed cache for affected users. WebSocket/push for real-time feel. Eventual consistency acceptable (seconds).'),
        'Q4': ('How do you handle "following" 5000 users with high post volume?',
               'Do not fan-out all. Pull model: on read, fetch from followees\' post shards. Merge top-K with heap. Cache merged result. Rank only top candidates.'),
        'Q5': ('How do you measure feed quality?',
               'Metrics: session time, posts viewed, interactions/impression (CTR), long-clicks, hides/reports. A/B test ranking changes. Long-term: retention, DAU/MAU. Counter-metrics: spam reports, misinformation flags.'),
    },
    'BB-12-Chat-System.md': {
        'Q1': ('Design WhatsApp/Slack. 1-on-1 and group chat.',
               '1) Gateway: WebSocket/long-polling, connection management. 2) Message Service: persist (Cassandra/ScyllaDB, partition by conversation_id), assign sequence ID. 3) Delivery: push to online (WebSocket), offline -> push notification (FCM/APNs). 4) Group: fan-out to members, message ordering per conversation. 5) Presence: heartbeat, last-seen. 6) Media: upload to S3, send thumbnail + CDN URL.'),
        'Q2': ('How do you guarantee message ordering and exactly-once?',
               'Per-conversation sequencing (single partition in Kafka/Scylla). Client: local ID + server ID, dedup on receive. Idempotent writes (upsert by message_id). Ack: client ack -> server confirms. Unacked -> retry with same ID.'),
        'Q3': ('How do you scale to 1B messages/day?',
               'Partition by conversation_id (hash). Read replicas for recent messages. Archive old messages to cold storage (S3). Media separate (S3 + CDN). Connection servers stateless, scale horizontally. Redis for presence/counters.'),
        'Q4': ('How do you handle group chat with 1000 members?',
               'Fan-out: write once, notify all (async). Message ID per recipient for ack tracking. Mute/notification settings per user. Admin controls. Search: inverted index per conversation.'),
        'Q5': ('How do you handle end-to-end encryption?',
               'Signal Protocol (Double Ratchet). Client generates keys. Server never sees plaintext. Group: Sender Keys (per-member ratchet). Key rotation on member join/leave. Backup: encrypted key backup to cloud (optional).'),
    },
    'BB-14-YouTube-Video-Streaming.md': {
        'Q1': ('Design YouTube video streaming. Key components?',
               '1) Upload: chunked/resumable upload to S3. 2) Transcoding: async pipeline (FFmpeg) -> multiple resolutions (240p-8K), codecs (H.264, VP9, AV1), HLS/DASH segments. 3) CDN: segment caching, edge compute for manifest manipulation. 4) Manifest: MPD (DASH) / m3u8 (HLS) with adaptive bitrate. 5) Player: ABR algorithm (bandwidth estimation, buffer health). 6) Analytics: QoE metrics (startup time, rebuffer rate, bitrate).'),
        'Q2': ('How does adaptive bitrate streaming (ABR) work?',
               'Client measures: throughput (segment download time), buffer occupancy. Algorithm: BOLA (buffer occupancy), throughput-based, or hybrid. Switch up/down based on predicted bandwidth. Avoid oscillation (hysteresis).'),
        'Q3': ('How do you handle transcoding at scale (500h uploaded/min)?',
               'Async: upload -> S3 event -> SQS -> transcoding workers (spot instances). Priority queue: premium/short first. Parallel: segment-level parallelism. Output: per-resolution segments + manifest. Cache: popular videos pre-transcoded.'),
        'Q4': ('How do you optimize CDN costs and latency?',
               'Tiered caching: origin -> regional -> edge. Prefetch next segments. Segment duration: 2-6s (trade-off: latency vs overhead). Manifest at edge (Lambda@Edge/Cloudflare Workers). Peering with ISPs. Cache hit rate > 95%.'),
        'Q5': ('How do you handle live streaming vs VOD?',
               'Live: low-latency HLS (LL-HLS) or WebRTC. Segment duration 1-2s. Ingest: RTMP/SRT -> transcoder -> packager -> CDN. DVR: sliding window. VOD: pre-transcoded, full manifest. Live-to-VOD: clip and store after stream ends.'),
    },
    'BB-19-Distributed-Message-Queue.md': {
        'Q1': ('Design Kafka-like distributed message queue.',
               '1) Brokers: partition leaders + ISR (in-sync replicas). 2) Topics: partitioned, ordered per partition. 3) Producers: partitioner (key hash, round-robin), acks (all/1/0), idempotent. 4) Consumers: group protocol, offset management, rebalance (cooperative). 5) Storage: segments, index, time-index, compaction (log compaction for keys). 6) ZooKeeper/KRaft: controller, metadata. 7) Tiered storage: local SSD + S3.'),
        'Q2': ('How does Kafka achieve high throughput?',
               'Sequential disk I/O (append-only). Page cache (OS) for reads. Zero-copy (sendfile). Batching (linger.ms, batch.size). Compression (Snappy, ZSTD, LZ4). Partition parallelism.'),
        'Q3': ('How do you handle consumer lag and rebalancing?',
               'Lag: monitor per partition. Rebalance: cooperative (incremental) since 2.4. Static membership (group.instance.id) to avoid rebalance on restart. Max.poll.interval.ms for stuck consumers.'),
        'Q4': ('How do you implement exactly-once semantics?',
               'Idempotent producer: PID + sequence per partition. Transactional API: atomic write to multiple partitions + offset commit. Consumer: process + commit offset in same transaction. Requires idempotent consumer logic (dedup).'),
        'Q5': ('How do you operate Kafka at scale (100+ brokers)?',
               'Monitoring: under-replicated partitions, offline partitions, controller health, disk, network. Tiered storage for retention. Cruise Control for rebalance. MirrorMaker for cross-DC replication. KRaft mode (no ZooKeeper).'),
    },
}

def update_note_qa(file_path: Path, qa_dict: dict):
    """Update a note's Interview Q&A section with deep answers."""
    content = file_path.read_text(encoding='utf-8')
    if not content.startswith('---'):
        return False
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    fm = yaml.safe_load(parts[1]) or {}
    body = parts[2]
    
    # Build new Q&A section
    new_qa = "## Interview Q&A (Senior Depth)\n\n"
    for i, (q, a) in enumerate(qa_dict.items(), 1):
        new_qa += f"**Q{i}: {q}**\n**A:** {a}\n\n"
    
    # Replace existing Q&A section
    if "## Interview Q&A (Senior Depth)" in body:
        # Find the section and replace until next ## heading
        pattern = r'## Interview Q&A \(Senior Depth\).*?(?=\n## |\Z)'
        body = re.sub(pattern, new_qa.rstrip(), body, flags=re.DOTALL)
    else:
        # Add before Flashcards section
        if "## Flashcards" in body:
            body = body.replace("## Flashcards", new_qa + "## Flashcards")
        else:
            body += "\n\n" + new_qa
    
    # Write back
    new_fm = "---\n" + yaml.dump(fm, sort_keys=False, allow_unicode=True, default_flow_style=False) + "---\n"
    file_path.write_text(new_fm + body, encoding='utf-8')
    return True

def main():
    updated = 0
    for filename in TOP_20:
        file_path = TARGET / filename
        if not file_path.exists():
            print(f"  MISSING: {filename}")
            continue
        
        if filename in DEEP_QA:
            if update_note_qa(file_path, DEEP_QA[filename]):
                print(f"  UPDATED: {filename}")
                updated += 1
        else:
            print(f"  NO DEEP QA: {filename}")
    
    print(f"\nTotal updated: {updated}")

if __name__ == "__main__":
    main()