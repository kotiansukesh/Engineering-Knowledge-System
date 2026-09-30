---
title: Decomposition, Bounded Context to Service
category: Architect/04_Design-Patterns-Building-Blocks
tags:
- ddd
- decomposition
- difficulty/medium
- microservices
- pattern/cloud
- pattern/enterprise
- pattern/integration
- pattern/resilience
- patterns
- spring
- strangler
created: 2026-09-03
completed: false
reviewed: '2026-08-29'
sr-due: '2026-09-05'
difficulty: Medium
excalidraw: ''
source: ''
type: concept
weeks: ''

---






## Why it Matters

Services split along the wrong axis cost forever: layer-shaped splits couple everything to everything, and team-shaped splits re-architect on every re-org. Decomposing by bounded context with a strangler path means each extraction ships value, is reversible, and lands on a boundary that survives an org change.

## Problems
### System Design Problem: Decomposition, Bounded Context to Service

**Requirements:**
- Functional: Core capabilities for decomposition, bounded context to service
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
 subgraph Monolith
 FA[OrderFacade seam] --> OM[order module]
 end
 FA -->|new service behind gateway route| NS[Order-Svc + own schema]
 OM -.|dual-write / CDC backfill|→ NS
 NS -->|cut reads, then writes| DONE[old module deleted]
```

## Code

```java
// Target: own Boot app + own schema + own Flyway history
@SpringBootApplication
public class OrderServiceApp { public static void main(String[] a) { SpringApplication.run(OrderServiceApp.class, a); } }

// Seam first: anti-corruption layer inside the monolith
@Component class OrderFacade {
 private final OrderModule orders; // in-process today, HTTP client tomorrow — same interface
 public Order place(Cart c) { return orders.place(c); }
}

## When to use / NOT

- Greenfield with clear sub-domains, or a modular monolith hitting team/release contention.
- Different scaling, consistency, or compliance needs per capability.

**When NOT:** boundaries still fuzzy, < 3 teams, or no observability/DevOps maturity — stay modular until the seam is obvious.


## Vs

- **Vs layer-split (UI/Biz/DB services):** layers couple everything to everything; capability-split isolates change.
- **Vs big-bang rewrite:** strangler ships value each cutover; rewrite stalls for months.






## Trade-offs
| Dimension | This Approach | Alternative | Trade-off Rationale | Decision Rule |
|-----------|---------------|-------------|---------------------|---------------|
| Complexity | [TBD] | [TBD] | [TBD] | [TBD] |
| Operational Burden | [TBD] | [TBD] | [TBD] | [TBD] |
| Latency | [TBD] | [TBD] | [TBD] | [TBD] |
| Consistency | [TBD] | [TBD] | [TBD] | [TBD] |
| Cost at Scale | [TBD] | [TBD] | [TBD] | [TBD] |

## Pitfalls

- Shared DB between "services" — that's a distributed monolith.
- Splitting by team size instead of domain — re-org creates re-architecture.
- No contract tests (Spring Cloud Contract) → silent breakage on extract.


## Pitfalls
1. Underestimating operational complexity (backups, monitoring, upgrades)
2. Ignoring failure modes (network partitions, disk failures, clock drift)
3. Not planning for 10x scale from day one
4. Skipping monitoring/alerting in MVP
5. Premature optimization before measuring
6. Dual-write without transactional outbox
7. Assuming global order in partitioned systems

## Interview Q&A

**Q: How do you find service boundaries?**
A: Bounded contexts via event storming — one context, one service, one DB; shared kernel is a smell.

**Q: How do you split without downtime?**
A: Strangler + gateway routing + CDC backfill (Debezium), then cut reads, then writes.

**Q: When do you merge services back?**
A: Chatty sync + lock-step releases + one team owning both — the seam was wrong.


## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the core concept of Decomposition, Bounded Context to Service? :: **A:** [Key algorithm/architecture pattern] #flashcard

#flashcard
**Q:** When do you apply Decomposition, Bounded Context to Service? :: **A:** [Trigger scenarios and context] #flashcard

#flashcard
**Q:** What is the primary trade-off in Decomposition, Bounded Context to Service? :: **A:** [Main tension: e.g., consistency vs latency] #flashcard

#flashcard
**Q:** What breaks first at scale in Decomposition, Bounded Context to Service? :: **A:** [Primary bottleneck: e.g., coordination, hot keys, replication lag] #flashcard

#flashcard
**Q:** How do you handle failures in Decomposition, Bounded Context to Service? :: **A:** [Retry, circuit breaker, fallback, graceful degradation] #flashcard

#flashcard
**Q:** What are the key metrics to monitor for Decomposition, Bounded Context to Service? :: **A:** [RED: rate, errors, duration; USE: utilization, saturation, errors] #flashcard

#flashcard
**Q:** How does Decomposition, Bounded Context to Service scale to 10x? :: **A:** [Sharding, read replicas, async processing, caching layers] #flashcard

#flashcard
**Q:** What is the consistency model for Decomposition, Bounded Context to Service? :: **A:** [Strong/eventual/causal - justify with use case] #flashcard

#flashcard
**Q:** How do you test Decomposition, Bounded Context to Service? :: **A:** [Contract tests, chaos engineering, load tests, fault injection] #flashcard

#flashcard
**Q:** What is the operational cost of Decomposition, Bounded Context to Service? :: **A:** [Team expertise, tooling, on-call burden, migration risk] #flashcard

#flashcard
**Q:** When would you NOT use Decomposition, Bounded Context to Service? :: **A:** [Managed service covers need, simple CRUD, team lacks maturity] #flashcard

#flashcard
**Q:** What is the key design decision in Decomposition, Bounded Context to Service? :: **A:** [The irreversible choice that defines the architecture] #flashcard

#flashcard
**Q:** How do you migrate to Decomposition, Bounded Context to Service? :: **A:** [Strangler fig, dual-write, canary, feature flags] #flashcard

#flashcard
**Q:** What security considerations for Decomposition, Bounded Context to Service? :: **A:** [AuthZ, encryption, audit, secrets management] #flashcard

#flashcard
**Q:** How do you debug Decomposition, Bounded Context to Service in production? :: **A:** [Structured logging, correlation IDs, distributed tracing, SLO alerts] #flashcard


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

- [[../../03_Architecture-Styles/03_Microservices|Microservices]] · [[../../05_DDD-Modeling/02_Bounded-Contexts|Bounded Contexts]] · [[06_Saga-Outbox-Inbox|Saga-Outbox]] · [[../../06_Data-Architecture/05_Data-Migration-Strangler|Strangler]]

# Decomposition — Bounded Context to Service

> **Intent:** Carve services along bounded contexts so each owns its data and team — decompose by business capability, not by layer, and extract incrementally via strangler.

# application.yml (per service)

spring.datasource.url: jdbc:postgresql://order-db:5432/orders
```
Strangler order: facade → new service behind gateway route → dual-write or CDC backfill → cut traffic → delete old module.
