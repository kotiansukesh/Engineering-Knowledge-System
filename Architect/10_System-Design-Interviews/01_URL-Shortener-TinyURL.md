---
title: "URL Shortener (TinyURL)"
category: "System Design"
tags: [system-design, interview, hashing, caching, cap]
created: 2026-09-04
completed: false
---

# URL Shortener (TinyURL)

> **Intent:** turn long URLs into short, redirectable keys at high read volume — the canonical key-generation + cache interview drill.

## 1. When to Use

- Read-heavy (Grokking assumes **100:1**), latency-sensitive redirect path; writes need global uniqueness.
- Scale anchor (Grokking): **500M** new URLs/mo → ~**200/s** writes, ~**19K/s** reads; 5yr × 500B/row ≈ **15TB**; 80/20 hot set ≈ **170GB** cache.
- **When NOT:** need mutable/edits-heavy links or strong analytics consistency — that's a different system (event pipeline, not redirect path).

## 2. Example (Spring Boot 3.5 + K8s)

```java
// POST /api/v1/urls {longUrl} → {key}; GET /{key} → 302 + Cache-Control: private, max-age=90
@RestController public class ShortenController {
    @PostMapping("/api/v1/urls") public ShortUrl create(@RequestBody CreateUrl req) {
        String key = keyGen.next(); // base62(counter) OR hash+collision-check
        store.save(new UrlMapping(key, req.longUrl())); // Postgres + Redis write-through
        return new ShortUrl(key);
    }
    @GetMapping("/{key}") public ResponseEntity<Void> redirect(@PathVariable String key) {
        String longUrl = cache.get(key, () -> store.find(key)); // 80/20 hot keys in Redis/CDN
        return ResponseEntity.status(302).location(URI.create(longUrl)).build();
    }
}
```

Design: `Gateway → Shorten-Svc (HPA) → Postgres (hash-sharded by key) + Redis (hot keys, 24h TTL) + Kafka(url-created → analytics)`. Key gen: **range-based counter + base62** (short, no collisions) vs **hash + retry** (stateless, needs collision check). Grokking's dedicated option: offline **KGS** (pre-generated 6-char keys, ~412GB key space, in-memory buffer per app server). CDN caches 302s for hot keys.

Grokking schema: `URL(hash varchar(16), original_url varchar(512), creation_date, expiration_date, user_id)` + `User(...)`; hash-based partitioning via consistent hashing; LRU cache; periodic expired-link sweeper; `api_dev_key` quota for throttling.

## 3. Pros / Cons

| Pros | Cons |
|---|---|
| Counter+base62: collision-free, short keys | Counter: single coordination point (mitigate with ZK ranges) |
| Cache + CDN absorbs 100:1 reads | Hash: collision handling + longer keys |
| Async analytics keeps redirect p99 low | Deletes/expiry need tombstones + purge |

## 4. Vs

- **Vs Twitter feed:** shortener is a KV lookup; feed is a fan-out/merge problem — different hard part.
- **Vs pastebin:** same shape, larger values — chunk + object store (S3) instead of row-per-doc.

## 5. Interview Q&A

**Q: How do you generate keys?**
A: Pre-allocated counter ranges per app node → base62 encode. No coordination per request, no collisions, ~7 chars for billions. Hash (MD5+truncate) works but needs DB collision check + retry. Grokking's KGS variant pre-generates keys offline into used/unused tables with an in-memory buffer.

**Q: How do you handle 10× reads?**
A: Redis for hot keys + CDN on 302s, read replicas for Postgres, consistent-hash sharding by key. Redirect never touches Kafka synchronously.

**Q: Custom aliases / expiry?**
A: Unique index on key; custom alias = `INSERT … ON CONFLICT` → 409. Expiry = lazy (TTL + nightly sweep, Grokking's cleanup service) + CDN purge on delete.

## 6. Pitfalls

- Synchronous analytics/click-count on redirect path — kills p99.
- Auto-increment DB id exposed directly — leaks growth rate; encode/offset it.
- No rate-limit on create — spam fills the DB; gateway token-bucket per user/IP.

## 7. Links

- [[../06_Data-Architecture/04_Caching-CDN|Caching-CDN]] · [[../04_Design-Patterns-Building-Blocks/03_Caching-Strategies|Caching Strategies]] · [[../06_Data-Architecture/02_Consistency-CAP-PACELC|CAP/PACELC]] · [[05_Rate-Limiter|Rate Limiter]]
- Source: [[https://github.com/Jeevan-kumar-Raj/Grokking-System-Design/blob/master/designs/short-url.md|Grokking: Short URL (full text — numbers, KGS, schema)]]

<!-- Concept: reads win — generate keys without coordination, serve redirects without touching the DB. -->
