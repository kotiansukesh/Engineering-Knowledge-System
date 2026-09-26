---
title: Rate Limiter
category: System Design
tags:
- system-design
- interview
- rate-limiting
- redis
- gateway
created: 2026-09-04
completed: false
reviewed: ''
sr-due: ''
difficulty: Medium
excalidraw: ''
source: ''
type: note
weeks: ''
---

## Why it Matters

Rate limiting protects every other drill, which is why interviewers reach for it: it is the one cross-cutting concern where a wrong answer (per-instance counters, IP-only keys, silently dropping) visibly breaks the system. The real design tension is between exact fairness and per-request latency, a good answer states the approximation deliberately.

## Diagram

```mermaid
graph LR
 REQ[request] → AU[auth: who]
 AU --> PRE[local Caffeine pre-check]
 PRE -.miss.-> RL[Redis Lua: token bucket / sliding window]
 RL -->|allowed| SVC[service]
 RL -->|over| R4[429 + Retry-After + X-RateLimit-*]
 CFG[route rules in config] --> RL
```

## Code

```java
// Gateway filter: token-bucket via Redis Lua (atomic); headers: X-RateLimit-Remaining + Retry-After
@Component public class RateLimitFilter implements GlobalFilter {
 public Mono<Void> filter(ServerWebExchange ex, GatewayFilterChain chain) {
 String key = "rl:" + ex.getRequest().getPath() + ":" + userId(ex);
 // Lua: refill(bucket, rate) → take 1 → return remaining; sliding-window-counter variant for strict windows
 long remaining = redis.eval(TOKEN_BUCKET_LUA, key, capacity, refillPerSec);
 ex.getResponse().getHeaders().add("X-RateLimit-Remaining", String.valueOf(remaining));
 return remaining < 0 ? reject429(ex) : chain.filter(ex);
 }
}
```
Design: enforce at **gateway** (Spring Cloud Gateway), counters in **Redis Cluster** (Lua atomicity), rules in config (per-route limits). Algorithms: token-bucket (burst-friendly) vs sliding-window-counter (strict, 2-key). Local Caffeine pre-check sheds load before Redis.

## When to use / not

- Per-user / per-IP / per-API-key fairness; gateway enforcement, p99 overhead < 5ms.
- Scale anchor: 1M rps checks; counters in Redis, local pre-check optional.
- **When NOT:** business quota (monthly seats), that's billing state, not hot-path limiting.

## Trade-offs

| Pros | Cons |
|---|---|
| Gateway-central: one policy, all services | Redis per-request: extra RTT (pipeline / local cache) |
| Token bucket: allows legit bursts | Fixed window: boundary stampede (use sliding) |
| 429 + Retry-After: clients self-throttle | Clock skew across nodes, keep windows ≥ 1s |

## Vs

- **Vs backpressure (KEDA/queue):** rate-limit rejects fast at edge; backpressure absorbs with queues, use both (limit → queue → shed).
- **Vs auth:** auth says *who*; rate-limit says *how much*, separate filters, auth first.

## Pitfalls

- Per-instance in-memory counters, N instances = N× limit; must centralise or coordinate.
- Limiting by IP only, NAT/shared office = innocent users blocked; key by user+route.
- No rule for internal callers, one retry storm bypasses everything; limit service-to-service too.

## Interview q&a

**Q: Token bucket vs sliding window?**
A: Bucket = burst-friendly (chat send), sliding-window-counter = strict fairness (paid API). Default to sliding for interviews unless bursts are the point.

**Q: Distributed consistency?**
A: Redis Lua = atomic per key; sticky routing optional. Approximate (local + async sync) is fine at 1M rps, exactness costs latency.

**Q: What do clients see?**
A: `429 + Retry-After`, `X-RateLimit-Limit/Remaining/Reset`; SDKs honour it. Never silently drop.

## Related

- [[../04_Design-Patterns-Building-Blocks/04_API-Gateway-BFF|Gateway-BFF]] · [[../04_Design-Patterns-Building-Blocks/02_Resilience-Circuit-Breaker-Retry|Resilience]] · [[01_URL-Shortener-TinyURL|URL Shortener]] · [[04_WhatsApp-Chat|WhatsApp Chat]]

# Rate Limiter (Distributed)

> **Intent:** protect every hot path above (shorten-create, tweet-post, ride-request, chat-send) with fair, low-latency throttling, the cross-cutting drill interviewers love.
