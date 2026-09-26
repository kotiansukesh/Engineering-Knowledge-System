---
title: Decomposition, Bounded Context to Service
category: Design Patterns & Building Blocks
tags:
- patterns
- microservices
- decomposition
- ddd
- strangler
- spring
created: 2026-09-03
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

Services split along the wrong axis cost forever: layer-shaped splits couple everything to everything, and team-shaped splits re-architect on every re-org. Decomposing by bounded context with a strangler path means each extraction ships value, is reversible, and lands on a boundary that survives an org change.

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

## Trade-offs

| Pros | Cons |
|---|---|
| Team autonomy, independent deploy/scale | Cross-service queries need composition or views |
| Forces clean domain seams | Premature split = distributed monolith |

## Vs

- **Vs layer-split (UI/Biz/DB services):** layers couple everything to everything; capability-split isolates change.
- **Vs big-bang rewrite:** strangler ships value each cutover; rewrite stalls for months.

## Pitfalls

- Shared DB between "services" — that's a distributed monolith.
- Splitting by team size instead of domain — re-org creates re-architecture.
- No contract tests (Spring Cloud Contract) → silent breakage on extract.

## Interview Q&A

**Q: How do you find service boundaries?**
A: Bounded contexts via event storming — one context, one service, one DB; shared kernel is a smell.

**Q: How do you split without downtime?**
A: Strangler + gateway routing + CDC backfill (Debezium), then cut reads, then writes.

**Q: When do you merge services back?**
A: Chatty sync + lock-step releases + one team owning both — the seam was wrong.

## Related

- [[../../03_Architecture-Styles/03_Microservices|Microservices]] · [[../../05_DDD-Modeling/02_Bounded-Contexts|Bounded Contexts]] · [[06_Saga-Outbox-Inbox|Saga-Outbox]] · [[../../06_Data-Architecture/05_Data-Migration-Strangler|Strangler]]

# Decomposition — Bounded Context to Service

> **Intent:** Carve services along bounded contexts so each owns its data and team — decompose by business capability, not by layer, and extract incrementally via strangler.

# application.yml (per service)

spring.datasource.url: jdbc:postgresql://order-db:5432/orders
```
Strangler order: facade → new service behind gateway route → dual-write or CDC backfill → cut traffic → delete old module.
