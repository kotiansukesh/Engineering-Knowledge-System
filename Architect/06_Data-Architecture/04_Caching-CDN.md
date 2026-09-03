---
title: "Caching & CDN"
category: "Data Architecture"
tags: [data, caching, cdn, http-caching, redis, performance]
created: 2026-09-03
completed: false
---

# Caching & CDN (Multi-Layer Strategy)

> **Intent:** Layer caches from browser → CDN edge → gateway → app → DB so each request is served by the cheapest layer that may hold a valid answer — with invalidation and TTLs designed per layer, not improvised.

## 1. When to Use
Layers and their jobs:
| Layer | Serves | Invalidate via |
|---|---|---|
| Browser (`Cache-Control: max-age`, ETag) | Private, per-user GETs | Versioned URLs, short max-age |
| CDN edge (CloudFront/Cloudflare) | Public static + cacheable API GETs | Path purge / versioned keys, `s-maxage` |
| Gateway (Spring Cloud Gateway) | Brief shared GETs, rate-limit counters | Short TTL (seconds–minutes) |
| App (Caffeine local / Redis) | DTOs, computed views | Write-through evict + TTL (see [[04_Design-Patterns-Building-Blocks/03_Caching-Strategies|Caching Strategies]]) |
| DB (buffer pool, materialised views) | Hot pages, pre-joined reads | Refresh concurrently on schedule |

## 2. Spring Boot Example

```java
// HTTP caching headers — let browsers + CDN do the work
@GetMapping("/products/{id}")
public ResponseEntity<ProductDto> get(@PathVariable String id,
        @RequestHeader(value = "If-None-Match", required = false) String inm) {
    var p = catalogue.get(id);
    String etag = "\"" + p.version() + "\"";
    if (etag.equals(inm)) return ResponseEntity.status(304).build();
    return ResponseEntity.ok().eTag(etag)
        .cacheControl(CacheControl.maxAge(60, SECONDS).cachePublic()).body(p);
}
// Static assets: content-hashed filenames (app.9f2c.js) → immutable, Cache-Control: max-age=1y
```

## 3. Pros / Cons
| Pros | Cons |
|---|---|
| Each layer multiplies origin offload (CDN often 90%+) | Stale-serving risk compounds across layers |
| Edge latency (ms) for global users | Purge is eventually consistent — plan for it |
| Survives origin outages briefly (stale-while-revalidate) | Debugging "which layer served this?" needs headers (`Age`, `X-Cache`) |

## 4. Vs
- **Vs [[04_Design-Patterns-Building-Blocks/03_Caching-Strategies|app-only caching]]:** app cache saves compute; CDN saves *bytes on the wire* + global latency. Different bills, both worth paying.
- **Vs precomputation (materialised views):** durable vs ephemeral — combine: nightly view + edge TTL.

## 5. Interview Q&A
**Q: How do you invalidate across layers?**
A: Versioned keys/URLs (deploy-safe), event-driven purge (product-updated → CDN purge + Redis evict), TTLs as backstop. Prefer versioning over purging — purges are slow and partial.

**Q: Private vs public caching?**
A: `private` for user-scoped (browser only), `s-maxage`/`public` for shared edge; never edge-cache personalised payloads under shared keys.

## 6. Pitfalls
- Caching authenticated responses at edge under one key — personal data leak.
- No `Vary` discipline (`Vary: Accept-Encoding, Authorization` where needed).
- Thundering herd on CDN miss — origin shield + stale-while-revalidate.

## 7. Links
- [[04_Design-Patterns-Building-Blocks/03_Caching-Strategies|Caching Strategies]] · [[04_Design-Patterns-Building-Blocks/04_API-Gateway-BFF|Gateway/BFF]]

<!-- Concept: cache in layers, invalidate by version — the only purge you trust is the one you never need. -->
