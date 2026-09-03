---
title: "Hexagonal Architecture (Ports & Adapters)"
category: "Architecture Styles"
tags: [architecture, hexagonal, ports-adapters, clean-architecture, spring]
created: 2026-09-03
completed: false
---

# Hexagonal Architecture (Ports & Adapters)

> **Intent:** Put the domain model at the centre; all outside concerns (REST, JPA, messaging, clocks) talk to it only through **ports** (interfaces) with **adapters** (implementations) — so business logic is framework-independent and testable.

## 1. When to Use
- Domains with real business rules you must unit-test without Spring/DB.
- Codebases where framework churn (JPA → jOOQ, REST → gRPC) shouldn't touch the core.
- Long-lived services that will gain new inbound/outbound channels.

**When NOT:** trivial CRUD (overhead), prototypes, or teams unwilling to enforce the boundary.

## 2. Spring Boot Example

```java
// PORT (in) — driven by core, defined by core
public interface PlaceOrderUseCase { Order place(CreateOrderCmd cmd); }
// PORT (out)
public interface OrderStore { Order save(Order o); }

// CORE — pure Java, zero Spring imports
class PlaceOrderService implements PlaceOrderUseCase {
    private final OrderStore store;
    public Order place(CreateOrderCmd cmd) {
        return store.save(Order.place(cmd.items()));
    }
}
// ADAPTER (in) — web
@RestController class OrderController {
    private final PlaceOrderUseCase useCase; // depends on port only
    @PostMapping("/orders") OrderDto create(@RequestBody CreateOrderCmd c) {
        return OrderDto.from(useCase.place(c));
    }
}
// ADAPTER (out) — persistence
@Repository class JpaOrderStore implements OrderStore {
    private final SpringOrderRepo repo;
    public Order save(Order o) { return repo.save(OrderEntity.toJpa(o)).toDomain(); }
}

// Wiring — explicit @Configuration, not component-scan magic
@Configuration class OrderConfig {
    @Bean PlaceOrderUseCase useCase(OrderStore s) { return new PlaceOrderService(s); }
}
```

Package layout: `core/` (no Spring) · `adapter/in/web/` · `adapter/out/persistence/`.

## 3. Pros / Cons
| Pros | Cons |
|---|---|
| Domain unit-tests run in ms, no context | More interfaces + mapping code |
| Swap adapters freely (H2 for tests, Postgres prod) | Over-engineering for CRUD |
| Framework upgrades don't ripple inward | Needs discipline — one `@Autowired` JPA repo in core breaks it |
| Clearest expression of DIP | Newcomers find indirection confusing |

## 4. Vs
- **Vs [[01_Layered-Architecture|Layered]]:** layered points dependencies *down* to infra; hexagonal points them *inward* to the domain.
- **Vs Clean/Onion:** same idea, different vocabulary (use-cases/interactors vs ports). Pick one naming scheme per repo.

## 5. Interview Q&A
**Q: Where does `@Transactional` go?**
A: On the inbound adapter or an application-service orchestrator — transactions are infrastructure, not domain logic.

**Q: How do you verify the boundary?**
A: ArchUnit: `noClasses().that().resideIn("..core..").should().dependOn("org.springframework..")` (except maybe `spring-core` annotations you explicitly allow).

## 6. Pitfalls
- Anemic ports (`GenericRepository<T>` everywhere) — ports should be use-case-shaped.
- Mapping explosion: keep mappers dumb and co-located with adapters.
- Letting DTOs/entities cross the core — core owns its own model.

## 7. Links
- [[01_Layered-Architecture]] · [[06_Monolith-vs-Modular-Choice-Guide]] · [[05_DDD-Modeling/02_Bounded-Contexts|Bounded Contexts]]

<!-- Concept: hexagonal = dependency inversion applied to the whole app; the domain never imports the framework. -->
