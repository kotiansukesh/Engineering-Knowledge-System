#!/usr/bin/env python3
"""
Expand flashcards from 4 to 15 per note for top 20 patterns.
"""

import yaml
import re
from pathlib import Path

TARGET = Path('/Users/sukesh/Documents/GitHub/Obsidian/Architect/10_System-Design-Interviews')

FLASHCARDS = {
    'FND-04-CAP-Theorem.md': [
        ("What does CAP stand for?", "Consistency, Availability, Partition Tolerance"),
        ("What is the CAP theorem?", "In a distributed system, you can only guarantee 2 of 3: Consistency, Availability, Partition Tolerance"),
        ("Why must you choose Partition Tolerance?", "Networks are unreliable - partitions WILL happen, so PT is mandatory"),
        ("What is a CP system?", "Consistency + Partition Tolerance. Blocks writes during partition (e.g., HBase, ZooKeeper, etcd)"),
        ("What is an AP system?", "Availability + Partition Tolerance. Accepts writes on both sides, reconciles later (e.g., Cassandra, DynamoDB)"),
        ("What is linearizability?", "Strong consistency model: operations appear to execute atomically at some point between invocation and response"),
        ("What is eventual consistency?", "If no new updates, all reads eventually return the last written value"),
        ("What is read-repair?", "Background process that fixes stale replicas during read operations"),
        ("What is hinted handoff?", "When a replica is down, writes are stored on another node and forwarded when it recovers"),
        ("What is anti-entropy?", "Background process (Merkle trees) that reconciles differences between replicas"),
        ("What is QUORUM in Cassandra?", "R + W > N. Typical: N=3, W=2, R=2 for strong consistency"),
        ("What is the trade-off of strong consistency?", "Higher latency (wait for acks), unavailability during minority partition"),
        ("How do you test partition tolerance?", "Chaos engineering: inject network partitions (tc/netem, Chaos Mesh, Jepsen tests)"),
        ("What monitoring for CP systems?", "Replication lag, leader election frequency, quorum availability"),
        ("What monitoring for AP systems?", "Conflict rate, read-repair rate, hinted handoff queue, vector clock divergence"),
    ],
    'NET-01-Load-Balancer.md': [
        ("What is a load balancer?", "Distributes incoming requests across multiple backend servers"),
        ("L4 vs L7 load balancing?", "L4: TCP/UDP, no HTTP parsing. L7: HTTP-aware, path routing, SSL termination, WAF"),
        ("Common LB algorithms?", "Round-robin, Least Connections, Least Time, Consistent Hash, Weighted, IP Hash"),
        ("What is SSL termination?", "Decrypt at LB, encrypt to backend. Removes cert management from backends"),
        ("What is session persistence?", "Route same client to same backend (cookie, IP hash). Prefer stateless with Redis"),
        ("Active vs Passive health checks?", "Active: LB sends probes. Passive: monitors real traffic (5xx, timeouts)"),
        ("What is graceful drain?", "Stop new connections, wait for in-flight requests to complete before removing backend"),
        ("What is circuit breaker?", "Fast-fail when error rate exceeds threshold, prevent cascade failures"),
        ("How to scale the LB itself?", "DNS round-robin, anycast IP, ECMP, cloud managed (ALB/NLB/GCLB)"),
        ("What is slow start?", "Gradually add recovered backend back to pool to avoid overwhelming it"),
        ("What is connection pooling?", "Reuse backend connections to reduce handshake overhead"),
        ("What is RED metrics?", "Rate, Errors, Duration - key metrics per backend"),
        ("What is USE metrics?", "Utilization, Saturation, Errors - for resource monitoring"),
        ("L4 vs L7 latency?", "L4: ~1ms. L7: ~2-5ms (HTTP parsing overhead)"),
        ("When to use L4 vs L7?", "L4: raw throughput, non-HTTP, TLS passthrough. L7: microservices, canary, API gateway"),
    ],
    'DB-05-Sharding.md': [
        ("What is sharding?", "Horizontal partitioning: distribute data across multiple databases"),
        ("What is a shard key?", "Column(s) used to determine which shard a row belongs to"),
        ("Hash vs Range sharding?", "Hash: even distribution, no ordered scans. Range: ordered scans, hotspot risk"),
        ("What is consistent hashing?", "Maps keys/nodes to ring. Adding/removing node only affects K/N keys"),
        ("What are virtual nodes?", "Multiple ring positions per physical node (150-200) for even load distribution"),
        ("What is the hotspot problem?", "Power users concentrate load on one shard"),
        ("Hotspot solutions?", "Bounded loads, dedicated shards for hot keys, local cache, rate limiting per key"),
        ("Cross-shard transactions?", "Avoid. If needed: Saga pattern, 2PC (rare), eventual consistency with outbox"),
        ("How to reshard without downtime?", "Dual-write → backfill → verify → canary switch → remove old"),
        ("What is Vitess?", "MySQL sharding proxy: query routing, resharding, connection pooling"),
        ("Shard key selection criteria?", "High cardinality, even access pattern, co-location of related data"),
        ("How to handle joins across shards?", "Avoid. Denormalize, duplicate data, or scatter-gather (expensive)"),
        ("What is rebalancing?", "Moving data between shards to maintain even distribution"),
        ("Consistent hashing vs range for time-series?", "Range better for time-series (ordered scans, easy retention)"),
        ("Monitoring shard health?", "Per-shard QPS, latency, disk, replication lag. Cross-shard: size distribution, hotspots"),
    ],
    'CACHE-02-Cache-Strategies.md': [
        ("What is cache-aside?", "App reads cache, on miss loads from DB, populates cache. Simple, eventual consistency"),
        ("What is write-through?", "App writes to cache AND DB synchronously. Strong consistency, write latency = cache+DB"),
        ("What is write-behind?", "App writes cache, async flush to DB. Low latency, risk of data loss on crash"),
        ("What is refresh-ahead?", "Async refresh before expiry. Low latency reads, complex implementation"),
        ("What is the thundering herd?", "Hot key expires → 1000 requests hit DB simultaneously"),
        ("Thundering herd solutions?", "Single-flight (SETNX), stale-while-revalidate, jittered TTL, request coalescing"),
        ("What is cache invalidation?", "Removing/updating stale cache entries. Hard problem in distributed systems"),
        ("Invalidation strategies?", "TTL + jitter, event-driven (CDC), versioned keys, cache tags, probabilistic early expiry"),
        ("What is multi-level caching?", "L1: in-process (Caffeine, μs). L2: distributed (Redis, ms). L1 caches L2 misses"),
        ("L1 vs L2 sizing?", "L1 ~1-5% of L2. L1 TTL short (10-60s), L2 authoritative"),
        ("How to size cache capacity?", "Working set analysis: 80/20 rule. Capacity = working_set * 1.5-2x headroom"),
        ("What is LFU vs LRU?", "LFU: evict least frequently used. LRU: evict least recently used. LFU better for stable hot sets"),
        ("Cache hit rate targets?", "L1: >99%. L2: >95%. Monitor eviction rate and memory pressure"),
        ("What are cache tags?", "Group related keys, invalidate by tag (Redis SET operations)"),
        ("When to use each strategy?", "Read-heavy → cache-aside. Write-heavy + strong consistency → write-through. Write-heavy + loss OK → write-behind"),
    ],
    'ASYNC-02-Message-Queues.md': [
        ("Kafka vs RabbitMQ vs Pulsar?", "Kafka: log-based, high throughput, replay. RabbitMQ: broker-based, flexible routing. Pulsar: tiered storage, geo-replication"),
        ("What is exactly-once semantics?", "Message processed exactly one time. Hard to achieve. Requires idempotent producer + transactional consumer"),
        ("Kafka idempotent producer?", "PID + sequence per partition. enable.idempotence=true. Retries + acks=all"),
        ("Kafka transactional API?", "Atomic write to multiple partitions + offset commit in same transaction"),
        ("How to handle ordering?", "Per-partition ordering. Partition by correlation key (user_id, order_id)"),
        ("What is consumer lag?", "Producer offset - consumer offset. Target: < 1000 messages"),
        ("What is rebalancing?", "Consumer group membership change. Cooperative (incremental) since Kafka 2.4"),
        ("Static membership?", "group.instance.id to avoid rebalance on restart"),
        ("Dead letter queue?", "Messages that fail after max retries. Separate topic per retry count. Alert on DLQ growth"),
        ("Exponential backoff?", "1s, 2s, 4s, 8s... max 5 retries. Poison pill detection after N attempts"),
        ("What is log compaction?", "Key-based retention: keep latest value per key. Tombstones for deletes"),
        ("Tiered storage?", "Hot data on local SSD, cold data on S3. Transparent to consumers"),
        ("MirrorMaker?", "Cross-DC replication for disaster recovery"),
        ("KRaft mode?", "Kafka without ZooKeeper. Metadata in internal __cluster_metadata topic"),
        ("Monitoring Kafka?", "Under-replicated partitions, offline partitions, controller health, disk, network, lag"),
    ],
    'BB-01-Scaling-Zero-to-Millions.md': [
        ("Phase 1 (0-10K users)?", "Monolith + single DB + vertical scaling"),
        ("Phase 2 (10K-100K)?", "Read replicas, caching (Redis), CDN for static assets"),
        ("Phase 3 (100K-1M)?", "Sharding, async processing (message queues), microservices split"),
        ("Phase 4 (1M+)?", "Multi-region, active-active, custom infrastructure"),
        ("First 3 bottlenecks?", "1) DB CPU: read replicas + caching. 2) Network: CDN + compression. 3) Single-threaded: stateless horizontal scaling"),
        ("When to split microservices?", "Team boundaries (2-pizza), independent deploy, different scaling, different tech, data ownership"),
        ("Strangler fig pattern?", "Gradually extract functionality from monolith, route traffic to new services"),
        ("Distributed transactions?", "Saga pattern (choreography/orchestration), compensating transactions, outbox pattern, avoid 2PC"),
        ("Monitoring per phase?", "P1: APM, DB. P2: cache hit rate, queue depth. P3: service mesh, tracing. P4: SLOs, error budgets, chaos"),
        ("What is modular monolith?", "Monolith with clear module boundaries, separate packages, shared DB but logical separation"),
        ("Database scaling order?", "Vertical → read replicas → caching → sharding"),
        ("Stateless services?", "No local state. Session in Redis. Config in etcd/Consul. Enables horizontal scaling"),
        ("Caching layers?", "CDN (static) → Redis (dynamic) → in-process (hot) → DB"),
        ("Async processing?", "Message queues for: email, notifications, analytics, reporting, webhooks"),
        ("Circuit breaker?", "Fail fast, prevent cascade. States: closed → open → half-open"),
    ],
    'BB-04-Rate-Limiter.md': [
        ("Token Bucket?", "Burst allowance, smooth rate. Refill tokens/sec. Redis Lua for atomicity. Best: API Gateway"),
        ("Leaky Bucket?", "Fixed rate, no burst. Queue + constant drain. Best: streaming, smooth traffic"),
        ("Sliding Window Log?", "Precise, stores all timestamps. Memory heavy. Best: login, exact counting"),
        ("Sliding Window Counter?", "Approximate, low memory. Weighted prev+curr window. Best: high QPS"),
        ("Fixed Window?", "Simple, burst at boundaries. Best: coarse limiting"),
        ("Edge vs App rate limiting?", "Edge: DDoS, IP-based, volumetric. App: user-level, business logic, premium tiers. Both needed"),
        ("Rate limit response?", "HTTP 429 + Retry-After + JSON {limit, remaining, reset}. Client: exponential backoff + jitter"),
        ("Distributed rate limiting?", "Redis sorted sets (sliding log) or counters (sliding window). Lua for atomicity"),
        ("Token bucket in Redis?", "Lua: check tokens, decrement, refill by elapsed time. Keys: rate_limit:{user}:{window}"),
        ("Per-endpoint vs per-user?", "Per-endpoint: protect expensive ops. Per-user: fair usage. Per-IP: DDoS. Layer all three"),
        ("Rate limit headers?", "X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, Retry-After"),
        ("Testing rate limiter?", "Chaos: burst traffic, clock skew, Redis failover. Verify no over/under-limiting. Jepsen-style"),
        ("Sliding window formula?", "count = prev_window_count * (1 - overlap_ratio) + current_window_count"),
        ("How to handle premium tiers?", "Different limits per tier. Store tier in user profile. Check tier before applying limit"),
        ("Rate limiting GraphQL?", "Query complexity cost (fields, depth). Limit by cost, not just request count"),
    ],
    'BB-05-Consistent-Hashing.md': [
        ("What is consistent hashing?", "Maps keys and nodes to ring (0 to 2^32-1). Key → next clockwise node"),
        ("Why virtual nodes?", "Even load distribution. 150-200 vnodes per physical node. Ketama algorithm"),
        ("Adding/removing node?", "Only K/N keys affected (vs all keys in modulo hashing)"),
        ("Hotspot handling?", "Bounded loads (Google): route to next node if overloaded. Weight adjustment. Dedicated nodes"),
        ("Consistent vs range sharding?", "Consistent: minimal reshuffle, dynamic. Range: ordered scans, but hotspots on sequential keys"),
        ("Implementation?", "Sorted array of (hash, node). Binary search for key. Health checks remove unhealthy nodes"),
        ("Network partition in ring?", "Different ring views. Gossip (SWIM) for membership. Split-brain: quorum, LWW, or pause writes"),
        ("Ketama algorithm?", "160 vnodes per node. MD5 hash of node:vn. Sorted ring. Used in memcached, Redis Cluster"),
        ("Consistent hashing in Redis Cluster?", "16384 hash slots. Slots assigned to nodes. Resharding moves slots"),
        ("Rendezvous hashing?", "HRW (Highest Random Weight): score = hash(key, node). No ring, simpler, same properties"),
        ("Jump consistent hash?", "O(1) memory, no ring. Good for uniform loads, not for weighted"),
        ("Maglev hashing?", "Google's consistent hashing for network load balancing. Minimal disruption"),
        ("When NOT to use?", "Need ordered scans (range queries). Simple static cluster (modulo fine). Very few nodes"),
        ("Rebalancing trigger?", "Node add/remove, load imbalance > threshold, node failure"),
        ("Monitoring?", "Key distribution per node, vnode distribution, rebalance frequency, lookup latency"),
    ],
    'BB-06-Key-Value-Store.md': [
        ("What is LSM Tree?", "Log-Structured Merge Tree: MemTable (RAM) → SSTables (disk, immutable, sorted)"),
        ("MemTable?", "In-memory sorted structure (skip list/B-tree). Flushed to SSTable when full"),
        ("SSTable?", "Sorted String Table: immutable, sorted key-value files on disk. Bloom filter for fast negative"),
        ("Compaction strategies?", "Size-tiered (write-opt), Leveled (read-opt), Universal (hybrid). Choose by workload"),
        ("WAL?", "Write-Ahead Log: durability for MemTable. Replay on restart"),
        ("Bloom filter?", "Probabilistic data structure: fast negative lookups (definitely not in SSTable)"),
        ("Quorum consistency?", "R + W > N. N=3, W=2, R=2 = strong. DynamoDB consistent read = quorum"),
        ("Range queries on hash?", "Hash kills range. Solutions: secondary index (scatter-gather), composite key, dual-write to column store"),
        ("Tombstone GC?", "Tombstones removed after gc_grace_seconds. Risk: resurrection if node down > gc_grace"),
        ("Cassandra vs DynamoDB?", "Cassandra: tunable consistency, LSM, wide rows. DynamoDB: managed, single-digit ms, on-demand"),
        ("Partitioning?", "Consistent hashing + vnodes. Token range per node. Virtual nodes for even distribution"),
        ("Replication?", "N replicas. Hinted handoff for down nodes. Read repair. Anti-entropy (Merkle trees)"),
        ("Gossip protocol?", "Membership, failure detection. Seed nodes for bootstrapping. SWIM for failure detection"),
        ("Time-to-live (TTL)?", "Per-cell expiration. Automatic cleanup. Monitor TTL expiration rate"),
        ("Monitoring?", "Read/write latency (p50/p99), compaction backlog, tombstone ratio, disk usage, heap"),
    ],
    'BB-07-Unique-ID-Generator-Snowflake.md': [
        ("Snowflake ID structure?", "64-bit: 1 sign(0) + 41 timestamp(ms) + 10 machine(1024) + 12 sequence(4096/ms)"),
        ("Timestamp bits?", "41 bits ms since epoch = ~69 years. Epoch custom (e.g., 2020-01-01)"),
        ("Machine ID bits?", "10 bits = 1024 nodes. Static config or dynamic (etcd/Consul lease)"),
        ("Sequence bits?", "12 bits = 4096 IDs/ms per node. Overflow: wait next ms"),
        ("Clock backward?", "Block/wait for catch-up, or reject, or logical clock. Max drift threshold (100ms). NTP required"),
        ("K8s machine ID?", "Pod UID hash modulo 1024. Or 5 bits DC + 5 bits pod. Etcd lease for dynamic"),
        ("Snowflake vs UUIDv4?", "Snowflake: 64-bit, time-ordered, needs coordination. UUIDv4: 128-bit, random, no coordination"),
        ("Snowflake vs UUIDv7?", "UUIDv7: 128-bit, time-ordered, no coordination. Snowflake: 64-bit, index-friendly"),
        ("Snowflake vs ULID?", "ULID: 128-bit, time-ordered, case-insensitive, Crockford base32. Snowflake: 64-bit"),
        ("Snowflake vs NanoID?", "NanoID: URL-safe, customizable alphabet/length. Not time-ordered"),
        ("Why 64-bit?", "Fits in DB BIGINT. Index-friendly (sequential-ish). Smaller than UUID"),
        ("ID exhaustion?", "4M IDs/sec per node. 1024 nodes = 4B IDs/sec. Monitor sequence usage %"),
        ("Twitter Snowflake?", "Original implementation. 41-bit timestamp (2010 epoch), 10-bit worker, 12-bit sequence"),
        ("Sonyflake?", "Sony's variant: 39-bit timestamp (10ms units), 8-bit machine, 16-bit sequence"),
        ("Baidu UID?", "Baidu's: time + machine + sequence + version. Used in FENGCHAO"),
    ],
    'BB-08-URL-Shortener.md': [
        ("TinyURL vs bit.ly?", "TinyURL: simpler, no analytics, 6 chars. bit.ly: analytics, custom domains, enterprise"),
        ("Key generation?", "Sequential ID (counter) + Base62 = no collision, predictable. Hash + Base62 = opaque, collision risk"),
        ("Collision handling?", "Retry with salt/counter. Check DB unique constraint. Or use sequential (Snowflake)"),
        ("Scale redirects to 1B/day?", "CDN cache 301. Redis Cluster for hot URLs (LFU). Read replicas. Async analytics"),
        ("Custom aliases?", "Reserved namespace (api, admin). Validate: alphanumeric, length, no profanity. Unique index"),
        ("Link expiration?", "TTL column. Background job delete/mark inactive. Check TTL on redirect"),
        ("Prevent enumeration?", "Use hash (MD5/SHA256) + Base62. Random suffix. Rate limit. robots.txt disallow"),
        ("Analytics pipeline?", "Async: click → Kafka → Flink/Spark → ClickHouse. Dimensions: geo, referrer, device"),
        ("Redirect: 301 vs 302?", "301: permanent, cacheable (CDN). 302: temporary, not cacheable. TinyURL uses 301"),
        ("Multi-region?", "Active-active: write to local, async replicate. Conflict: last-write-wins or CRDT"),
        ("URL canonicalization?", "Remove fragments, sort query params, lowercase host. Prevents duplicate entries"),
        ("Short code length?", "6 chars (62^6 = 56B). 7 chars = 3.5T. Base62: [a-z][A-Z][0-9]"),
        ("Database schema?", "id (BIGINT), long_url (TEXT), short_code (VARCHAR), user_id, created_at, expires_at, clicks"),
        ("Cache invalidation?", "On delete: invalidate Redis. On update: update Redis. TTL as safety net"),
        ("Abuse prevention?", "Rate limit create. Domain reputation. ML classification. CAPTCHA. Allow/deny lists"),
    ],
    'BB-09-Web-Crawler.md': [
        ("Crawler components?", "URL Frontier (priority queue), Fetcher (HTTP pool), Parser (extract links), Dedup (bloom+simhash), Storage (S3+ES+DB)"),
        ("URL Frontier?", "Min-heap priority queue. Priority = PageRank + freshness. Per-domain queues for politeness"),
        ("Politeness?", "Per-domain token bucket (1 req/sec default). Respect robots.txt. Exponential backoff on 429/5xx"),
        ("Deduplication?", "URL canonicalization + bloom filter (visited) + simhash (near-dup content, 64-bit fingerprint)"),
        ("JavaScript-heavy sites?", "Headless browser (Puppeteer/Playwright) for rendering. Use selectively. Cache rendered HTML"),
        ("Prioritization?", "Priority = f(PageRank, update_freq, domain_authority, user_demand). High: daily, Low: monthly"),
        ("Incremental crawling?", "Only re-fetch changed: ETag, Last-Modified, content hash. Conditional GET"),
        ("Storage?", "Raw HTML → S3. Parsed content → Elasticsearch. Metadata → Cassandra/DB"),
        ("Distributed coordination?", "Partition frontier by domain hash. etcd/ZooKeeper for domain locks. Shared nothing"),
        ("Crawl budget?", "Max pages per domain per time window. Respect robots.txt crawl-delay"),
        ("Simhash?", "64-bit fingerprint. Hamming distance < 3 = near-duplicate. LSH for scaling"),
        ("Bloom filter sizing?", "10B entries, 1% false positive = ~1.5GB. Scalable bloom filter for growth"),
        ("Monitoring?", "Pages crawled/sec, queue depth, dedup rate, error rate, politeness violations"),
        ("ByteByteGo vs Google?", "ByteByteGo: single-region, simpler priority. Google: multi-region, Caffeine, Bigtable, Colossus"),
        ("robots.txt handling?", "Cache parsed rules per domain. Respect Disallow, crawl-delay, Sitemap"),
    ],
    'BB-10-Notification-System.md': [
        ("Notification channels?", "Push (FCM/APNs), Email (SendGrid), SMS (Twilio), In-app (WebSocket)"),
        ("Template engine?", "Per-channel rendering. Variables, localization, preview. Jinja2/Handlebars"),
        ("10M WebSocket connections?", "Connection server cluster (stateless). Redis pub/sub routing. Shard by user_id. Heartbeat"),
        ("Critical notification delivery?", "Multi-channel fallback: push → SMS → email. Idempotent send. Sync wait for provider ack"),
        ("User preferences?", "Per-user, per-type, per-channel. Quiet hours (TZ-aware). Frequency capping. Unsubscribe link"),
        ("Deduplication?", "Dedup key per notification. Prevent duplicate sends. TTL on dedup keys"),
        ("Retry strategy?", "Exponential backoff + DLQ. Alert on DLQ growth. Max retries per channel"),
        ("Scaling pipeline?", "Partition Kafka by user_id. Consumer groups per channel. Backpressure: pause consumption"),
        ("Delivery tracking?", "Message ID → provider ID. Webhooks for delivery/read/click. Analytics pipeline"),
        ("GDPR compliance?", "Right to delete. Consent management. Data retention policies. Unsubscribe in every email"),
        ("In-app notifications?", "WebSocket for real-time. Fallback to poll. Badge counts. Mark read sync"),
        ("Rate limiting providers?", "Respect provider limits (FCM: 1000/req, SendGrid: 600/sec). Queue locally, throttle"),
        ("Template versioning?", "Version templates. A/B test. Rollback capability. Preview before send"),
        ("Monitoring?", "Delivery rate, open rate, click rate, bounce rate, latency, DLQ size, provider errors"),
        ("Idempotent sends?", "Client generates idempotency key. Server dedups on key. Safe retry"),
    ],
    'BB-11-News-Feed-System.md': [
        ("Fan-out on write vs read?", "Hybrid: push for active (<5K followers), pull for celebrities. Redis sorted sets (score = timestamp*weight)"),
        ("Celebrity handling?", "Do NOT fan-out 50M followers. Pull model: merge on read. Cache celebrity tweets separately"),
        ("Ranking pipeline?", "1) Candidate gen: followees + recs (CF, content-based) → 1000. 2) Ranking: LightGBM/XGBoost → top 50"),
        ("Real-time updates?", "New post: async fan-out to active (Kafka). Like/comment: update counters (Redis), invalidate cache"),
        ("High-volume followees?", "Don't fan-out all. Pull: fetch from followee shards, merge top-K with heap, rank top candidates"),
        ("Feed quality metrics?", "Session time, posts viewed, CTR, long-clicks, hides/reports. A/B test ranking. Counter: spam flags"),
        ("Tweet deletion?", "Remove from author timeline + async fan-out delete to followers. Best-effort"),
        ("Tweet editing?", "Version tweets. Update in place with edit_timestamp. Not supported historically"),
        ("Candidate generation?", "Followees (primary) + recommendations (collaborative filtering, content-based, graph-based)"),
        ("Model serving?", "TensorFlow Serving / Triton. Feature store (Feast). Online features: Redis. Offline: BigQuery"),
        ("Diversification?", "Avoid same author/type cluster. MMR (Maximal Marginal Relevance). Category balancing"),
        ("A/B testing?", "Ramp: 1% → 5% → 50%. Metrics: engagement, retention. Guardrail: spam reports, latency"),
        ("Storage?", "Posts: Cassandra/Scylla (partition by user_id, cluster by timestamp). Timelines: Redis sorted sets"),
        ("Fan-out threshold?", "~10K followers. Above: pull. Below: push. Configurable per system"),
        ("Feed caching?", "Pre-compute for active users. TTL: 5-15 min. Invalidate on new post/interaction"),
    ],
    'BB-12-Chat-System.md': [
        ("Chat architecture?", "Gateway (WS) → Message Service (Cassandra/Scylla, partition by conversation_id) → Delivery (WS + Push)"),
        ("Message ordering?", "Per-conversation sequencing (single Kafka partition/Scylla partition). Client dedup"),
        ("Exactly-once?", "Client local ID + server ID. Idempotent writes (upsert by message_id). Ack: client→server"),
        ("Group chat 1000 members?", "Fan-out: write once, notify all (async). Message ID per recipient for ack tracking. Mute settings"),
        ("Scale to 1B msg/day?", "Partition by conversation_id. Read replicas for recent. Archive old to S3. Media separate (CDN)"),
        ("Presence?", "Heartbeat (ping/pong). Last-seen in Redis. Online/offline/away. Broadcast presence changes"),
        ("E2E encryption?", "Signal Protocol (Double Ratchet). Client keys. Server never sees plaintext. Group: Sender Keys"),
        ("Media handling?", "Upload → S3. Send thumbnail + CDN URL. Compress images. Video: transcoding pipeline"),
        ("Message search?", "Inverted index per conversation. Elasticsearch. Paginate by timestamp"),
        ("Offline delivery?", "Push notification (FCM/APNs) for offline. Store until online. Sync on reconnect"),
        ("Connection scaling?", "Stateless gateway. Horizontal scale. Redis for presence/counters. TLS offload at LB"),
        ("Message acknowledgment?", "Client ack → server confirms. Unacked → retry with same ID. Read receipts: per-recipient"),
        ("Group admin?", "Add/remove members. Promote/demote. Delete messages. Mute. Admin-only announcements"),
        ("Message edit/delete?", "Edit: version + edit_ts. Delete: soft delete (tombstone). Sync across devices"),
        ("Monitoring?", "Message latency (p50/p99), delivery rate, connection count, presence accuracy, WS errors"),
    ],
    'BB-14-YouTube-Video-Streaming.md': [
        ("Video streaming components?", "Upload (chunked) → Transcoding (FFmpeg, multi-res) → CDN (HLS/DASH segments) → Player (ABR)"),
        ("Adaptive Bitrate (ABR)?", "Client measures throughput + buffer. Algorithm: BOLA, throughput-based, hybrid. Hysteresis"),
        ("Transcoding at scale?", "Async: S3 event → SQS → spot workers. Priority queue. Segment-level parallelism. Pre-transcode popular"),
        ("HLS vs DASH?", "HLS: Apple, .m3u8, TS segments. DASH: standard, .mpd, fMP4. Both adaptive. DASH more flexible"),
        ("CDN optimization?", "Tiered: origin → regional → edge. Prefetch next segments. Segment 2-6s. Manifest at edge (Lambda@Edge)"),
        ("Live vs VOD?", "Live: LL-HLS/WebRTC, 1-2s segments, RTMP/SRT ingest, DVR window. VOD: pre-transcoded, full manifest"),
        ("Transcode pipeline?", "Upload → S3 → Event → MediaConvert/FFmpeg → Outputs (240p-8K, H.264/VP9/AV1) → S3 → CDN"),
        ("QoE metrics?", "Startup time, rebuffer rate, bitrate, join time, error rate. Per-session tracking"),
        ("Segment duration?", "2-6s trade-off: shorter = lower latency, more overhead. Live: 1-2s for low latency"),
        ("DRM?", "Widevine/PlayReady/FairPlay. Key rotation. License server. Offline playback support"),
        ("Thumbnail/sprite?", "Generate at intervals. Sprite sheet for hover preview. WebVTT for chapters"),
        ("Cost optimization?", "Tiered storage (hot/warm/cold). Spot instances for transcoding. Cache hit > 95%"),
        ("Multi-CDN?", "DNS-based or client-side switching. Cedexis/Conviva. Failover on error/latency"),
        ("Live-to-VOD?", "Clip and store after stream ends. Trim slate. Generate VOD manifest"),
        ("Monitoring?", "Concurrent viewers, bitrate distribution, rebuffer ratio, CDN hit rate, origin bandwidth"),
    ],
    'BB-19-Distributed-Message-Queue.md': [
        ("Kafka architecture?", "Brokers: partition leaders + ISR. Topics: partitioned, ordered per partition. KRaft for metadata"),
        ("High throughput?", "Sequential disk I/O (append-only). Page cache. Zero-copy (sendfile). Batching. Compression (ZSTD)"),
        ("Consumer lag?", "Producer offset - consumer offset. Target < 1000. Monitor per partition"),
        ("Rebalancing?", "Cooperative (incremental) since 2.4. Static membership (group.instance.id) avoids rebalance on restart"),
        ("Exactly-once?", "Idempotent producer (PID+seq) + transactional API (atomic multi-partition + offset commit). Consumer dedup"),
        ("Tiered storage?", "Hot on local SSD, cold on S3. Transparent to consumers. Retention by time/size"),
        ("Log compaction?", "Key-based retention: latest value per key. Tombstones for delete. Background compaction"),
        ("MirrorMaker?", "Cross-DC replication. Active-passive or active-active. Offset translation"),
        ("Controller?", "KRaft: elected controller manages metadata. No ZooKeeper. ZK: controller in ZK ensemble"),
        ("Partition leadership?", "Leader handles reads/writes. Followers replicate. ISR = in-sync replicas. min.insync.replicas"),
        ("Producer acks?", "acks=0 (fire-forget), acks=1 (leader), acks=all (ISR). Default: all"),
        ("Consumer groups?", "Each partition consumed by one consumer in group. Rebalance on join/leave. Max.poll.interval.ms"),
        ("Monitoring?", "Under-replicated partitions, offline partitions, controller health, disk, network, lag, request latency"),
        ("Cruise Control?", "Auto rebalance: partition movement for load balancing. Goal-based optimization"),
        ("Kafka Streams?", "Stream processing library. Exactly-once. Stateful ops (joins, aggregations). Changelog topics"),
    ],
}

def update_flashcards(file_path: Path, cards: list):
    """Update a note's Flashcards section with 15 cards."""
    content = file_path.read_text(encoding='utf-8')
    if not content.startswith('---'):
        return False
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    fm = yaml.safe_load(parts[1]) or {}
    body = parts[2]
    
    # Build new flashcards section
    new_fc = "## Flashcards (Spaced Repetition)\n\n"
    for q, a in cards:
        new_fc += f"#flashcard\n**Q:** {q} :: **A:** {a} #flashcard\n\n"
    
    # Replace existing flashcards section
    if "## Flashcards (Spaced Repetition)" in body:
        pattern = r'## Flashcards \(Spaced Repetition\).*?(?=\n## |\Z)'
        body = re.sub(pattern, new_fc.rstrip(), body, flags=re.DOTALL)
    else:
        # Add before Practice Tasks
        if "## Practice Tasks" in body:
            body = body.replace("## Practice Tasks", new_fc + "## Practice Tasks")
        else:
            body += "\n\n" + new_fc
    
    new_fm = "---\n" + yaml.dump(fm, sort_keys=False, allow_unicode=True, default_flow_style=False) + "---\n"
    file_path.write_text(new_fm + body, encoding='utf-8')
    return True

def main():
    updated = 0
    for filename, cards in FLASHCARDS.items():
        file_path = TARGET / filename
        if not file_path.exists():
            print(f"  MISSING: {filename}")
            continue
        
        if update_flashcards(file_path, cards):
            print(f"  UPDATED: {filename} ({len(cards)} cards)")
            updated += 1
    
    print(f"\nTotal updated: {updated}")

if __name__ == "__main__":
    main()