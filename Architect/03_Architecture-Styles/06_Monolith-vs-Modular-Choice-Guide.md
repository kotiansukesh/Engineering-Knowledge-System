---
title: "Monolith vs Modular Monolith, Choice Guide"
pattern: 6
category: "Architecture Styles"
tags: [architecture, monolith, modular-monolith, decision, spring]
created: 2026-09-03
completed: false
reviewed: ""
sr-due: ""
difficulty: Hard
problems-solved: []
problems-solved-dates: {}
excalidraw: ""
---
## Why it Matters

The choice is not monolith-vs-microservices, it is "are the boundaries real yet?" A modular monolith keeps boundaries *and* in-process calls, so you discover the seams cheaply and can extract them later with the same interface. Microservices bought before boundaries stabilise give you a distributed monolith: all the costs, none of the independence.

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

| Modular monolith pros | Cons vs microservices |
|---|---|
| One deploy, in-process calls (fast, typed) | Single scaling unit (scale all or nothing) |
| ACID transactions where truly needed | Single failure domain (mitigate with bulkheads) |
| Refactors/extractions are renames, not migrations | Requires discipline, no network forcing honesty |
| Full observability in one JVM | Tech-stack uniformity (usually a plus anyway) |

## Vs

- **Vs Distributed:** extraction path, module → separate deployable with same API, switching in-process calls to HTTP/events behind the port (see [[02_Hexagonal-Ports-Adapters|Hexagonal]]).
- **Migration trigger checklist:** deploy queue >1 day, module needs 10× scale of rest, team stepping on each other weekly, compliance isolation.

## Pitfalls

- Pretend modules (package cycles, cross-module joins), run `modulith verify` in CI.
- Shared `common` bucket growing into a coupling magnet, version it or duplicate small DTOs.
- Premature extraction: splitting before boundaries stabilise bakes in the wrong seams.

## Interview q&a

**Q: "Monoliths don't scale", respond?**
A: They scale *uniformly* (more instances behind LB) fine to large traffic; what they don't give is *independent* scaling/deploy per capability. Quote numbers: extraction when one module drives >70% load.

**Q: How do you keep modules decoupled without network boundaries?**
A: `api` vs `internal` packages + ArchUnit/Spring Modulith verification in CI + module events instead of direct calls + per-module schemas.

## Related

- [[01_Layered-Architecture]] · [[02_Hexagonal-Ports-Adapters]] · [[03_Microservices]] · [[05_DDD-Modeling/02_Bounded-Contexts|Bounded Contexts]]

# Monolith vs Modular Monolith, Choice Guide

> **Intent:** Give a repeatable decision path: default to a well-modularised monolith; split into microservices only when concrete pain (team, scale, deploy) forces it, with Spring patterns for keeping modules honest.
> Watch: [Monolithic vs Microservices: Which and When?](https://www.youtube.com/watch?v=NdeTGlZ__Do)

## 1. When to use What

| Signal | Choice |
|---|---|
| 1 team, 1 deploy cadence, fuzzy domain | Classic monolith ([[01_Layered-Architecture]]) |
| 1–4 teams, clear sub-domains, one DB acceptable | **Modular monolith** (this note) |
| Independent scaling/deploy per context, ≥3 autonomous teams | [[03_Microservices]] |
| Spiky peripheral work (reports, webhooks) | [[05_Serverless]] offshoots |
