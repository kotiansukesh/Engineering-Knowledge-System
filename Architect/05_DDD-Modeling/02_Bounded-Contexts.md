---
title: "Bounded Contexts"
category: "DDD & Modeling"
tags: [ddd, bounded-context, modules, microservices]
created: 2026-09-03
completed: false
---
## Why it Matters

One shared "Order" model is how a mid-size codebase becomes unmaintainable: sales, fulfilment and billing each need different fields and invariants of the same word, and every change negotiates between them. A bounded context makes the ambiguity explicit, inside the boundary one meaning holds, and integration with other meanings is a deliberate, versioned seam.

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
Physical mapping: package/module per context in a monolith; service per context in microservices (→ [[03_Context-Mapping]] for how they talk).

## When to use / not

- The moment a term has two definitions, or two teams change the same model for different reasons.
- Each context gets: own model, own language, own persistence, own team ownership.
- Size test: one context ≈ one module/service ownable by one team.

**When NOT:** single-team CRUD with one coherent vocabulary, a single context is fine; don't invent boundaries for ceremony.

## Trade-offs

| Pros | Cons |
|---|---|
| Independent evolution, no "shared model" merge hell | Duplicated concepts need sync (via events) |
| Teams autonomous within their boundary | More code than one shared model (worth it) |
| Clear ownership → clear accountability | Premature/wrong boundaries are costly, validate with change history |

## Vs

- **Vs namespaces/packages:** a package is a *code* grouping; a bounded context is a *language + ownership + persistence* boundary. Packages implement contexts; they aren't contexts by themselves.
- **Vs [[03_Architecture-Styles/03_Microservices|microservice]]:** 1 context : N services is fine (scale split); N contexts : 1 service is the distributed-monolith smell.

## Pitfalls

- Shared database across contexts, the boundary is fiction if SQL joins cross it.
- Context per entity (`OrderContext`, `CustomerContext`), contexts are capability-scoped, not entity-scoped.
- Big-bang boundary redraws, split incrementally behind anti-corruption layers.

## Interview q&a

**Q: How do you spot a missing boundary?**
A: Translation arguments in reviews, `OrderV2ForWarehouse`, booleans like `isForReturns`, two teams blocking each other on one PR.

**Q: Shared kernel or duplicate the model?**
A: Duplicate across contexts (sync via [[05_Domain-Events|events]]); share only tiny stable value objects (Money, IDs), and even those versioned.

## Related

- [[01_Strategic-DDD]] · [[03_Context-Mapping]] · [[05_Domain-Events]] · [[03_Architecture-Styles/06_Monolith-vs-Modular-Choice-Guide|Choice Guide]]

# Bounded Contexts

> **Intent:** Draw an explicit boundary inside which one model (one meaning per term) holds true, `Order` in Sales is not `Order` in Fulfilment, so each context evolves independently and integrations are deliberate, not accidental.
