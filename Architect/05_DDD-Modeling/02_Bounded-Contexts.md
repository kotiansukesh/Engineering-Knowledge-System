---
title: Bounded Contexts
category: Architect/05_DDD-Modeling
tags:
- bounded-context
- concept/aggregate
- concept/bounded-context
- concept/domain-event
- concept/saga
- ddd
- difficulty/easy
- microservices
- modules
- pattern/ddd
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

One shared "Order" model is how a mid-size codebase becomes unmaintainable: sales, fulfilment and billing each need different fields and invariants of the same word, and every change negotiates between them. A bounded context makes the ambiguity explicit, inside the boundary one meaning holds, and integration with other meanings is a deliberate, versioned seam.

## Problems
### System Design Problem: Bounded Contexts

**Requirements:**
- Functional: Core capabilities for bounded contexts
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
graph LR
 subgraph Sales context
 SO["Order: total, buyer"]
 end
 subgraph Fulfilment context
 FO["Order: shipTo, parcels"]
 end
 SO -.|events: order.placed.v1|→ FO
 FO -.|events: order.shipped.v1|→ SO
 SO --> DB1[(own schema)]
 FO --> DB2[(own schema)]
```

## Code

```java
// SAME word, DIFFERENT models per context — this is the point:
package sales; record Order(long id, Money total, CustomerRef buyer) {} // cares: price, buyer
package fulfilment; record Order(long id, Address shipTo, List<Parcel> parcels) {} // cares: packing, address
// Modules depend on each other's API, never internals:
// com.shop.sales.api.SalesOrderApi ↔ com.shop.fulfilment.internal.* (forbidden — ArchUnit/Spring Modulith)
```
Physical mapping: package/module per context in a monolith; service per context in microservices (→ 03_Context-Mapping for how they talk).

## When to use / not

- The moment a term has two definitions, or two teams change the same model for different reasons.
- Each context gets: own model, own language, own persistence, own team ownership.
- Size test: one context ≈ one module/service ownable by one team.

**When NOT:** single-team CRUD with one coherent vocabulary, a single context is fine; don't invent boundaries for ceremony.





## Trade-offs
| Dimension | This Approach | Alternative | Trade-off Rationale | Decision Rule |
|-----------|---------------|-------------|---------------------|---------------|
| Complexity | Not specified | Not specified | Not specified | Not specified |
| Operational Burden | Not specified | Not specified | Not specified | Not specified |
| Latency | Not specified | Not specified | Not specified | Not specified |
| Consistency | Not specified | Not specified | Not specified | Not specified |
| Cost at Scale | Not specified | Not specified | Not specified | Not specified |

## Vs

- **Vs namespaces/packages:** a package is a *code* grouping; a bounded context is a *language + ownership + persistence* boundary. Packages implement contexts; they aren't contexts by themselves.
- **Vs microservice:** 1 context : N services is fine (scale split); N contexts : 1 service is the distributed-monolith smell.

## Pitfalls

- Shared database across contexts, the boundary is fiction if SQL joins cross it.
- Context per entity (`OrderContext`, `CustomerContext`), contexts are capability-scoped, not entity-scoped.
- Big-bang boundary redraws, split incrementally behind anti-corruption layers.


## Pitfalls
1. Underestimating operational complexity (backups, monitoring, upgrades)
2. Ignoring failure modes (network partitions, disk failures, clock drift)
3. Not planning for 10x scale from day one
4. Skipping monitoring/alerting in MVP
5. Premature optimization before measuring
6. Dual-write without transactional outbox
7. Assuming global order in partitioned systems

## Interview q&a

**Q: How do you spot a missing boundary?**
A: Translation arguments in reviews, `OrderV2ForWarehouse`, booleans like `isForReturns`, two teams blocking each other on one PR.

**Q: Shared kernel or duplicate the model?**
A: Duplicate across contexts (sync via events); share only tiny stable value objects (Money, IDs), and even those versioned.


## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the core concept of Bounded Contexts? :: **A:** [Key algorithm/architecture pattern] #flashcard

#flashcard
**Q:** When do you apply Bounded Contexts? :: **A:** [Trigger scenarios and context] #flashcard

#flashcard
**Q:** What is the primary trade-off in Bounded Contexts? :: **A:** [Main tension: e.g., consistency vs latency] #flashcard

#flashcard
**Q:** What breaks first at scale in Bounded Contexts? :: **A:** [Primary bottleneck: e.g., coordination, hot keys, replication lag] #flashcard

#flashcard
**Q:** How do you handle failures in Bounded Contexts? :: **A:** [Retry, circuit breaker, fallback, graceful degradation] #flashcard

#flashcard
**Q:** What are the key metrics to monitor for Bounded Contexts? :: **A:** [RED: rate, errors, duration; USE: utilization, saturation, errors] #flashcard

#flashcard
**Q:** How does Bounded Contexts scale to 10x? :: **A:** [Sharding, read replicas, async processing, caching layers] #flashcard

#flashcard
**Q:** What is the consistency model for Bounded Contexts? :: **A:** [Strong/eventual/causal - justify with use case] #flashcard

#flashcard
**Q:** How do you test Bounded Contexts? :: **A:** [Contract tests, chaos engineering, load tests, fault injection] #flashcard

#flashcard
**Q:** What is the operational cost of Bounded Contexts? :: **A:** [Team expertise, tooling, on-call burden, migration risk] #flashcard

#flashcard
**Q:** When would you NOT use Bounded Contexts? :: **A:** [Managed service covers need, simple CRUD, team lacks maturity] #flashcard

#flashcard
**Q:** What is the key design decision in Bounded Contexts? :: **A:** [The irreversible choice that defines the architecture] #flashcard

#flashcard
**Q:** How do you migrate to Bounded Contexts? :: **A:** [Strangler fig, dual-write, canary, feature flags] #flashcard

#flashcard
**Q:** What security considerations for Bounded Contexts? :: **A:** [AuthZ, encryption, audit, secrets management] #flashcard

#flashcard
**Q:** How do you debug Bounded Contexts in production? :: **A:** [Structured logging, correlation IDs, distributed tracing, SLO alerts] #flashcard


## Practice Tasks (Tasks Plugin)
- [ ] Explain the architecture from memory 📅 {{date:YYYY-MM-DD, +1}}
- [ ] Draw the system diagram without looking 📅 {{date:YYYY-MM-DD, +3}}
- [ ] Answer all Interview Q&A aloud 📅 {{date:YYYY-MM-DD, +7}}
- [ ] Review flashcards (Spaced Repetition) 📅 {{date:YYYY-MM-DD, +1}}

```tasks
not done
path includes Architect/05_DDD-Modeling
sort by due
limit 10
```

## Related

- 01_Strategic-DDD · 03_Context-Mapping · 05_Domain-Events · Choice Guide

# Bounded Contexts

> **Intent:** Draw an explicit boundary inside which one model (one meaning per term) holds true, `Order` in Sales is not `Order` in Fulfilment, so each context evolves independently and integrations are deliberate, not accidental.
