---
title: Resilience, Circuit Breaker & Retry
category: Architect/04_Design-Patterns-Building-Blocks
tags:
- circuit-breaker
- company/youtube
- difficulty/easy
- pattern/circuit-breaker
- pattern/cloud
- pattern/enterprise
- pattern/integration
- pattern/resilience
- patterns
- resilience
- resilience4j
- retry
- spring
created: 2026-09-03
completed: false
reviewed: '2026-09-03'
sr-due: '2026-09-06'
difficulty: Easy
excalidraw: ''
source: ''
type: concept
weeks: ''

---






## Why it Matters

In a distributed system a dependency failing is not an incident, but *failing badly* is: unbounded threads blocked, retries piled on retries, one slow service taking down everything that calls it. Bounding every wait and failing fast converts cascading failure into graceful degradation, which is the difference between an outage and a degraded SLO.

## Problems
### System Design Problem: Resilience, Circuit Breaker & Retry

**Requirements:**
- Functional: Core capabilities for resilience, circuit breaker & retry
- Non-functional (SLOs): Latency < 100ms p99, Availability 99.9%, Horizontal scalability

**Constraints:**
- Scale: Handle 10x growth without redesign
- Consistency: Appropriate model for domain (strong/eventual)
- Latency budget: p99 < 100ms for read paths

**API / Interfaces:**
- Primary: REST/gRPC endpoints for core operations
- Internal: Service-to-service contracts
- Events: Domain events for async integration

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


## Vs

- **Vs naive `@Retryable`:** Spring Retry alone retries forever into an outage; the breaker *stops calling* and lets the downstream recover.
- **Vs going async:** async + queue is the deeper fix for overload; resilience patterns are the sync-call seatbelt.






## Trade-offs
| Dimension | This Approach | Alternative | Trade-off Rationale | Decision Rule |
|-----------|---------------|-------------|---------------------|---------------|
| Complexity | Not specified | Not specified | Not specified | Not specified |
| Operational Burden | Not specified | Not specified | Not specified | Not specified |
| Latency | Not specified | Not specified | Not specified | Not specified |
| Consistency | Not specified | Not specified | Not specified | Not specified |
| Cost at Scale | Not specified | Not specified | Not specified | Not specified |

## Pitfalls

- Retry storms: no jitter/exponential backoff → thundering herd.
- Fallback that calls another failing service — fallbacks must be local/static.
- One shared breaker config for all deps — per-dependency tuning required.


## Pitfalls
1. Underestimating operational complexity (backups, monitoring, upgrades)
2. Ignoring failure modes (network partitions, disk failures, clock drift)
3. Not planning for 10x scale from day one
4. Skipping monitoring/alerting in MVP
5. Premature optimization before measuring
6. Dual-write without transactional outbox
7. Assuming global order in partitioned systems

## Interview Q&A

**Q: When must you NOT retry?**
A: Non-idempotent operations (POST payment), 4xx client errors, and breaker-open state. Retry only timeouts/5xx/429 with backoff + jitter.

**Q: How do you size bulkheads?**
A: From downstream p99 × expected concurrency; isolate critical pools (checkout) from batch pools.

**Q: How do you test breakers?**
A: Chaos/fault-injection tests (WireMock delays, Toxiproxy) asserting open-state behaviour + fallback correctness.


## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the core concept of Resilience, Circuit Breaker & Retry? :: **A:** Not specified #flashcard

#flashcard
**Q:** When do you apply Resilience, Circuit Breaker & Retry? :: **A:** Not specified #flashcard

#flashcard
**Q:** What is the primary trade-off in Resilience, Circuit Breaker & Retry? :: **A:** Not specified #flashcard

#flashcard
**Q:** What breaks first at scale in Resilience, Circuit Breaker & Retry? :: **A:** Not specified #flashcard

#flashcard
**Q:** How do you handle failures in Resilience, Circuit Breaker & Retry? :: **A:** Not specified #flashcard

#flashcard
**Q:** What are the key metrics to monitor for Resilience, Circuit Breaker & Retry? :: **A:** Not specified #flashcard

#flashcard
**Q:** How does Resilience, Circuit Breaker & Retry scale to 10x? :: **A:** Not specified #flashcard

#flashcard
**Q:** What is the consistency model for Resilience, Circuit Breaker & Retry? :: **A:** Not specified #flashcard

#flashcard
**Q:** How do you test Resilience, Circuit Breaker & Retry? :: **A:** Not specified #flashcard

#flashcard
**Q:** What is the operational cost of Resilience, Circuit Breaker & Retry? :: **A:** Not specified #flashcard

#flashcard
**Q:** When would you NOT use Resilience, Circuit Breaker & Retry? :: **A:** Not specified #flashcard

#flashcard
**Q:** What is the key design decision in Resilience, Circuit Breaker & Retry? :: **A:** Not specified #flashcard

#flashcard
**Q:** How do you migrate to Resilience, Circuit Breaker & Retry? :: **A:** Not specified #flashcard

#flashcard
**Q:** What security considerations for Resilience, Circuit Breaker & Retry? :: **A:** Not specified #flashcard

#flashcard
**Q:** How do you debug Resilience, Circuit Breaker & Retry in production? :: **A:** Not specified #flashcard


## Practice Tasks (Tasks Plugin)
- [ ] Explain the architecture from memory 📅 {{date:YYYY-MM-DD, +1}}
- [ ] Draw the system diagram without looking 📅 {{date:YYYY-MM-DD, +3}}
- [ ] Answer all Interview Q&A aloud 📅 {{date:YYYY-MM-DD, +7}}
- [ ] Review flashcards (Spaced Repetition) 📅 {{date:YYYY-MM-DD, +1}}

```tasks
not done
path includes Architect/04_Design-Patterns-Building-Blocks
sort by due
limit 10
```

## Related

- Microservices · 01_Enterprise-Patterns

# Resilience — Circuit Breaker, Retry, Bulkhead, Timeout

> **Intent:** Stop one failing dependency from cascading through the system: fail fast when a downstream is sick (breaker), retry only what's retryable, isolate resources (bulkhead), and bound every wait (timeout).
> Watch: [ByteMonk — Top 5 Resilience Patterns](https://www.youtube.com/watch?v=RfPNuaj5Ax0)

# application.yml

resilience4j.circuitbreaker.instances.inventory:
 sliding-window-size: 20
 failure-rate-threshold: 50
 wait-duration-in-open-state: 30s
```