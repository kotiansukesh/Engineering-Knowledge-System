---
title: Resilience, Circuit Breaker & Retry
category: Design Patterns & Building Blocks
tags:
- patterns
- resilience
- circuit-breaker
- retry
- resilience4j
- spring
created: 2026-09-03
completed: false
reviewed: ''
sr-due: ''
difficulty: Easy
excalidraw: ''
source: ''
type: note
weeks: ''
---

## Why it Matters

In a distributed system a dependency failing is not an incident, but *failing badly* is: unbounded threads blocked, retries piled on retries, one slow service taking down everything that calls it. Bounding every wait and failing fast converts cascading failure into graceful degradation, which is the difference between an outage and a degraded SLO.

## Diagram

```mermaid
graph TD
 C[Caller] --> TO[Timeout: bound the wait]
 TO --> RT[Retry: idempotent only, backoff + jitter]
 RT --> CB{Circuit breaker}
 CB -->|closed| D[Downstream]
 CB -->|open| FB[Fallback: local/static, label staleness]
 D -->|50% failures in window|→ CB
 BH[Bulkhead: capped pool] -.limits concurrency.-> C
```

## Code

```java
@Service class Pricing {
 private final InventoryClient client;
 // Order matters: Retry OUTSIDE breaker is the common setup
 @Retry(name = "inventory") // 3 attempts, backoff, retry-on-timeout only
 @CircuitBreaker(name = "inventory", fallbackMethod = "cached") // opens after 50% failures / 10 calls
 @Bulkhead(name = "inventory", type = Type.SEMAPHORE) // cap concurrent calls
 @TimeLimiter(name = "inventory") // bound the wait (CompletableFuture)
 public CompletableFuture<Price> quote(String sku) { return client.quoteAsync(sku); }

 CompletableFuture<Price> cached(String sku, Throwable t) {
 return CompletableFuture.completedFuture(Price.lastKnown(sku)); // graceful fallback
 }
}

## When to use / NOT

- Any sync call crossing the network (REST, gRPC, DB failover, broker produce).
- Always pair: **timeout → retry (idempotent only) → circuit breaker → fallback → bulkhead**.

**When NOT:** non-idempotent writes retried blindly (double-charge), or masking a root cause that needs fixing, not absorbing.

## Trade-offs

| Pros | Cons |
|---|---|
| Cascades contained; degrades gracefully | Tuning thresholds per dependency is real work |
| Declarative, metrics-exported (Micrometer) | Retries amplify load on a struggling downstream |
| Fallbacks keep UX alive | Fallback staleness can mislead (label it: "last known") |

## Vs

- **Vs naive `@Retryable`:** Spring Retry alone retries forever into an outage; the breaker *stops calling* and lets the downstream recover.
- **Vs [[04_Event-Driven-Architecture|going async]]:** async + queue is the deeper fix for overload; resilience patterns are the sync-call seatbelt.

## Pitfalls

- Retry storms: no jitter/exponential backoff → thundering herd.
- Fallback that calls another failing service — fallbacks must be local/static.
- One shared breaker config for all deps — per-dependency tuning required.

## Interview Q&A

**Q: When must you NOT retry?**
A: Non-idempotent operations (POST payment), 4xx client errors, and breaker-open state. Retry only timeouts/5xx/429 with backoff + jitter.

**Q: How do you size bulkheads?**
A: From downstream p99 × expected concurrency; isolate critical pools (checkout) from batch pools.

**Q: How do you test breakers?**
A: Chaos/fault-injection tests (WireMock delays, Toxiproxy) asserting open-state behaviour + fallback correctness.

## Related

- [[03_Architecture-Styles/03_Microservices|Microservices]] · [[01_Enterprise-Patterns]]

# Resilience — Circuit Breaker, Retry, Bulkhead, Timeout

> **Intent:** Stop one failing dependency from cascading through the system: fail fast when a downstream is sick (breaker), retry only what's retryable, isolate resources (bulkhead), and bound every wait (timeout).
> Watch: [ByteMonk — Top 5 Resilience Patterns](https://www.youtube.com/watch?v=RfPNuaj5Ax0)

# application.yml

resilience4j.circuitbreaker.instances.inventory:
 sliding-window-size: 20
 failure-rate-threshold: 50
 wait-duration-in-open-state: 30s
```