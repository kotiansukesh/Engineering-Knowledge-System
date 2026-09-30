---
title: Monolith vs Modular Monolith, Choice Guide
category: Architect/03_Architecture-Styles
tags:
- architecture
- company/youtube
- concept/clean-architecture
- concept/event-driven
- concept/hexagonal
- concept/microservices
- concept/monolith
- concept/serverless
- decision
- difficulty/hard
- modular-monolith
- monolith
- pattern/architecture-style
- spring
created: 2026-09-03
completed: false
reviewed: '2026-09-01'
sr-due: '2026-09-15'
difficulty: Hard
excalidraw: ''
source: ''
type: concept
weeks: ''

---





## Why it Matters

The choice is not monolith-vs-microservices, it is "are the boundaries real yet?" A modular monolith keeps boundaries *and* in-process calls, so you discover the seams cheaply and can extract them later with the same interface. Microservices bought before boundaries stabilise give you a distributed monolith: all the costs, none of the independence.

## Problems
### System Design Problem: Monolith vs Modular Monolith, Choice Guide

**Requirements:**
- Functional: Core capabilities for monolith vs modular monolith, choice guide
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
 M["Monolith (package-by-layer)"] --> MM["Modular monolith: api vs internal packages + ArchUnit"]
 MM -.|pain: deploy queue, 10x scale, 3+ teams|→ MS[Microservices: same API over the network]
 MM -.|boundaries not stable|→ M
 MS -->|chatty + lock-step?|→ MM
```

## Code

```java
// Package-by-module, NOT by layer:
// com.shop.order/{api,internal,domain}, com.shop.inventory/{...}
// Module API is the only cross-module entry point:
package com.shop.order.api; public interface OrderApi { OrderDto find(long id); }
// Other modules depend ONLY on api packages — enforced:
 // ArchUnit: noClasses().that().resideIn("..inventory..")
 // .should().dependOn("com.shop.order.internal..")
// Optional runtime enforcement: Spring Modulith
// @ApplicationModule, modulith verify, module events for decoupling
```
DB: one Postgres, separate schemas per module; module-private tables never joined across modules (use `OrderApi`, not SQL).

## When to use / not

- **Default to a modular monolith** when there are 1–4 teams, clear sub-domains, and one shared DB is acceptable, boundaries are enforced in code, and extraction stays a rename until real pain shows up.
- **Use this *guide*** when the microservices question comes up at all: it is a decision procedure, not a recommendation, work the trigger checklist, don't follow the hype.
- **Extract to microservices** only on a concrete signal: deploy queue longer than a day, one module needing 10× the scale of the rest, 3+ autonomous teams stepping on each other weekly, or a compliance isolation requirement.

**When NOT:** do not split a monolith whose boundaries are still fuzzy, you get a distributed monolith with all the network costs and none of the independence, and the seams you baked in become the wrong seams forever. Do not split for scale alone: a monolith scales uniformly behind a load balancer to very large traffic; what it cannot do is scale *one* capability independently.



## Trade-offs
| Dimension | This Approach | Alternative | Trade-off Rationale | Decision Rule |
|-----------|---------------|-------------|---------------------|---------------|
| Complexity | Not specified | Not specified | Not specified | Not specified |
| Operational Burden | Not specified | Not specified | Not specified | Not specified |
| Latency | Not specified | Not specified | Not specified | Not specified |
| Consistency | Not specified | Not specified | Not specified | Not specified |
| Cost at Scale | Not specified | Not specified | Not specified | Not specified |

## Vs

- **Vs Distributed:** extraction path, module → separate deployable with same API, switching in-process calls to HTTP/events behind the port (see Hexagonal).
- **Migration trigger checklist:** deploy queue >1 day, module needs 10× scale of rest, team stepping on each other weekly, compliance isolation.

## Pitfalls

- Pretend modules (package cycles, cross-module joins), run `modulith verify` in CI.
- Shared `common` bucket growing into a coupling magnet, version it or duplicate small DTOs.
- Premature extraction: splitting before boundaries stabilise bakes in the wrong seams.


## Pitfalls
1. Underestimating operational complexity (backups, monitoring, upgrades)
2. Ignoring failure modes (network partitions, disk failures, clock drift)
3. Not planning for 10x scale from day one
4. Skipping monitoring/alerting in MVP
5. Premature optimization before measuring
6. Dual-write without transactional outbox
7. Assuming global order in partitioned systems

## Interview q&a

**Q: "Monoliths don't scale", respond?**
A: They scale *uniformly* (more instances behind LB) fine to large traffic; what they don't give is *independent* scaling/deploy per capability. Quote numbers: extraction when one module drives >70% load.

**Q: How do you keep modules decoupled without network boundaries?**
A: `api` vs `internal` packages + ArchUnit/Spring Modulith verification in CI + module events instead of direct calls + per-module schemas.


## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the core concept of Monolith vs Modular Monolith, Choice Guide? :: **A:** Not specified #flashcard

#flashcard
**Q:** When do you apply Monolith vs Modular Monolith, Choice Guide? :: **A:** Not specified #flashcard

#flashcard
**Q:** What is the primary trade-off in Monolith vs Modular Monolith, Choice Guide? :: **A:** Not specified #flashcard

#flashcard
**Q:** What breaks first at scale in Monolith vs Modular Monolith, Choice Guide? :: **A:** Not specified #flashcard

#flashcard
**Q:** How do you handle failures in Monolith vs Modular Monolith, Choice Guide? :: **A:** Not specified #flashcard

#flashcard
**Q:** What are the key metrics to monitor for Monolith vs Modular Monolith, Choice Guide? :: **A:** Not specified #flashcard

#flashcard
**Q:** How does Monolith vs Modular Monolith, Choice Guide scale to 10x? :: **A:** Not specified #flashcard

#flashcard
**Q:** What is the consistency model for Monolith vs Modular Monolith, Choice Guide? :: **A:** Not specified #flashcard

#flashcard
**Q:** How do you test Monolith vs Modular Monolith, Choice Guide? :: **A:** Not specified #flashcard

#flashcard
**Q:** What is the operational cost of Monolith vs Modular Monolith, Choice Guide? :: **A:** Not specified #flashcard

#flashcard
**Q:** When would you NOT use Monolith vs Modular Monolith, Choice Guide? :: **A:** Not specified #flashcard

#flashcard
**Q:** What is the key design decision in Monolith vs Modular Monolith, Choice Guide? :: **A:** Not specified #flashcard

#flashcard
**Q:** How do you migrate to Monolith vs Modular Monolith, Choice Guide? :: **A:** Not specified #flashcard

#flashcard
**Q:** What security considerations for Monolith vs Modular Monolith, Choice Guide? :: **A:** Not specified #flashcard

#flashcard
**Q:** How do you debug Monolith vs Modular Monolith, Choice Guide in production? :: **A:** Not specified #flashcard


## Practice Tasks (Tasks Plugin)
- [ ] Explain the architecture from memory 📅 {{date:YYYY-MM-DD, +1}}
- [ ] Draw the system diagram without looking 📅 {{date:YYYY-MM-DD, +3}}
- [ ] Answer all Interview Q&A aloud 📅 {{date:YYYY-MM-DD, +7}}
- [ ] Review flashcards (Spaced Repetition) 📅 {{date:YYYY-MM-DD, +1}}

```tasks
not done
path includes Architect/03_Architecture-Styles
sort by due
limit 10
```

## Related

- 01_Layered-Architecture · 02_Hexagonal-Ports-Adapters · 03_Microservices · Bounded Contexts

# Monolith vs Modular Monolith, Choice Guide

> **Intent:** Give a repeatable decision path: default to a well-modularised monolith; split into microservices only when concrete pain (team, scale, deploy) forces it, with Spring patterns for keeping modules honest.
> Watch: [Monolithic vs Microservices: Which and When?](https://www.youtube.com/watch?v=NdeTGlZ__Do)

## 1. When to use What

| Signal | Choice |
|---|---|
| 1 team, 1 deploy cadence, fuzzy domain | Classic monolith (01_Layered-Architecture) |
| 1–4 teams, clear sub-domains, one DB acceptable | **Modular monolith** (this note) |
| Independent scaling/deploy per context, ≥3 autonomous teams | 03_Microservices |
| Spiky peripheral work (reports, webhooks) | 05_Serverless offshoots |
