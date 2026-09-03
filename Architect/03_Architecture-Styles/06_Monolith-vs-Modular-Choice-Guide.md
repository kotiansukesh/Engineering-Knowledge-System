---
title: "Monolith vs Modular Monolith — Choice Guide"
category: "Architecture Styles"
tags: [architecture, monolith, modular-monolith, decision, spring]
created: 2026-09-03
completed: false
---

# Monolith vs Modular Monolith — Choice Guide

> **Intent:** Give a repeatable decision path: default to a well-modularised monolith; split into microservices only when concrete pain (team, scale, deploy) forces it — with Spring patterns for keeping modules honest.

## 1. When to Use What
| Signal | Choice |
|---|---|
| 1 team, 1 deploy cadence, fuzzy domain | Classic monolith ([[01_Layered-Architecture]]) |
| 1–4 teams, clear sub-domains, one DB acceptable | **Modular monolith** (this note) |
| Independent scaling/deploy per context, ≥3 autonomous teams | [[03_Microservices]] |
| Spiky peripheral work (reports, webhooks) | [[05_Serverless]] offshoots |

## 2. Spring Boot Example (Modular Monolith)

```java
// Package-by-module, NOT by layer:
// com.shop.order/{api,internal,domain}, com.shop.inventory/{...}
// Module API is the only cross-module entry point:
package com.shop.order.api; public interface OrderApi { OrderDto find(long id); }
// Other modules depend ONLY on api packages — enforced:
 // ArchUnit: noClasses().that().resideIn("..inventory..")
 //   .should().dependOn("com.shop.order.internal..")
// Optional runtime enforcement: Spring Modulith
// @ApplicationModule, modulith verify, module events for decoupling
```

DB: one Postgres, separate schemas per module; module-private tables never joined across modules (use `OrderApi`, not SQL).

## 3. Pros / Cons
| Modular monolith pros | Cons vs microservices |
|---|---|
| One deploy, in-process calls (fast, typed) | Single scaling unit (scale all or nothing) |
| ACID transactions where truly needed | Single failure domain (mitigate with bulkheads) |
| Refactors/extractions are renames, not migrations | Requires discipline — no network forcing honesty |
| Full observability in one JVM | Tech-stack uniformity (usually a plus anyway) |

## 4. Vs
- **Vs Distributed:** extraction path — module → separate deployable with same API, switching in-process calls to HTTP/events behind the port (see [[02_Hexagonal-Ports-Adapters|Hexagonal]]).
- **Migration trigger checklist:** deploy queue >1 day, module needs 10× scale of rest, team stepping on each other weekly, compliance isolation.

## 5. Interview Q&A
**Q: "Monoliths don't scale" — respond?**
A: They scale *uniformly* (more instances behind LB) fine to large traffic; what they don't give is *independent* scaling/deploy per capability. Quote numbers: extraction when one module drives >70% load.

**Q: How do you keep modules decoupled without network boundaries?**
A: `api` vs `internal` packages + ArchUnit/Spring Modulith verification in CI + module events instead of direct calls + per-module schemas.

## 6. Pitfalls
- Pretend modules (package cycles, cross-module joins) — run `modulith verify` in CI.
- Shared `common` bucket growing into a coupling magnet — version it or duplicate small DTOs.
- Premature extraction: splitting before boundaries stabilise bakes in the wrong seams.

## 7. Links
- [[01_Layered-Architecture]] · [[02_Hexagonal-Ports-Adapters]] · [[03_Microservices]] · [[05_DDD-Modeling/02_Bounded-Contexts|Bounded Contexts]]

<!-- Concept: modular monolith = microservice boundaries with monolith ops; extract along proven seams, not predicted ones. -->
