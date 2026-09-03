---
title: "Spring Data JPA"
category: Spring
tags: [spring, jpa, hibernate, interview]
created: 2026-01-18
updated: 2026-09-02
---

# Spring Data JPA

> Part of [[README|Java MOC]] • `Spring` • Java 25 / Spring Boot 3.5 / Hibernate 6.6 / JPA 3.2

## Intent
Eliminate boilerplate persistence: declare an interface (`extends JpaRepository`), get CRUD, paging, sorting, and query derivation for free; map entities with Hibernate so that transactions (`@Transactional`) and the persistence context handle flush/dirty-checking without manual JDBC.


> JPA is powerful until N+1 queries show up in production. I have been burned by lazy collections more than once, fetch joins or entity graphs are worth learning early.

## Definition
Spring Data JPA = Spring Data (repository abstraction) + JPA (Jakarta Persistence spec: `EntityManager`, `Entity` lifecycle, JPQL) + Hibernate (JPA provider: dirty checking, L1 cache, batching, lazy loading). Boot auto-configures `DataSource` (HikariCP), `EntityManagerFactory`, and `JpaTransactionManager`; repositories become transactional proxies at startup.

## Architecture, diagram description

```
 Controller (@RestController, virtual thread when spring.threads.virtual.enabled=true)
      │  OrderDto record ←→ Entity
      ▼
 Service (@Transactional)  ← TransactionInterceptor (AOP proxy)
      │  PlatformTransactionManager / JpaTransactionManager
      │  TransactionSynchronizationManager (ThreadLocal per virtual thread)
      ▼
 Spring Data Repository (interface → proxy at startup)
      │  JpaRepository<Order, Long> → SimpleJpaRepository
      ▼
 EntityManager / Persistence Context (L1 cache, per-transaction)
      │  persist / merge / remove / flush / dirty-check
      ▼
 Hibernate (Session, ActionQueue, JDBC batching, L2 cache optional)
      │
      ▼
 HikariCP → JDBC → PostgreSQL / MySQL
         (virtual thread parks on JDBC call - JEP 491 - carrier reused)

 Startup: @SpringBootApplication → @EnableJpaRepositories
          → scans interfaces → creates JDK proxies → registers as beans
 AOT (Java 25): entity reflection hints generated at build time
```

## JPA lifecycle, hibernate & identity

### Entity states

| State | In Persistence Context? | In DB? | How to enter |
|---|---|---|---|
| Transient | No | No | `new Order()` |
| Managed | Yes | May be flushed | `em.persist(o)`, `find()`, query result |
| Detached | No (was managed) | Yes | `em.detach()`, `em.clear()`, TX commit/close, serialize |
| Removed | Yes (scheduled) | Will be deleted on flush | `em.remove(managed)` |

```
 Transient ──persist()──▶ Managed ──flush/commit──▶ DB
                │              │  ▲
                │              ├──detach()/clear()/close──▶ Detached ──merge()──▶ Managed
                │              └──remove()──▶ Removed ──flush──▶ DB (DELETE) → Transient
```

### Hibernate dirty checking & flush

| Concept | Detail |
|---|---|
| Dirty checking | At flush, Hibernate compares managed entity snapshot vs current fields; changed entities → `UPDATE` automatically, no `save()` needed inside TX |
| Flush | `EntityManager.flush()` synchronises context → DB (still inside TX, not commit). Triggered before query, at `commit`, or manually |
| L1 cache | Per-`EntityManager` (per TX) map `id → entity`; `find(id)` hits L1 first |
| L2 cache | Optional `SessionFactory`-scoped (Ehcache/Caffeine), cross-TX, needs `@Cache` |

### Identity & equals/hashCode

| Concern | Rule |
|---|---|
| `@Id` generation | `IDENTITY` (DB auto-increment), `SEQUENCE` (preferred for batching), `UUID` |
| `equals/hashCode` | Don't use `@Id` before persist (null); use business key (e.g. `orderNumber`) or rely on identity until persisted |

```java title="Java 25 - JPA entity (Hibernate 6.6)"

// Purpose: Spring Data JPA: repository abstraction over JPA/Hibernate; derived queries; flush/commit semantics
// Framework: @Entity @Table @Id @GeneratedValue — Spring manages lifecycle and wiring; no manual new
// Roles: Order, Status, OrderDto — stereotype defines layer (controller/service/repository)
// Invariant: constructor injection — immutable, required deps; testable without container
```

### Fetching & N+1

| Fetch | Behaviour | Default |
|---|---|---|
| `LAZY` | Proxy loaded on first access, needs open `EntityManager` (within TX) | `@ManyToOne`, `@OneToMany` collections |
| `EAGER` | Loaded with parent | `@ManyToOne` (JPA default EAGER, override to LAZY) |

```java title="Fixing N+1 - Java 25"

// Purpose: Spring Data JPA: repository abstraction over JPA/Hibernate; derived queries; flush/commit semantics
// Framework: @Entity @ManyToOne @OneToMany @Query — Spring manages lifecycle and wiring; no manual new
// Roles: Order, OrderRepository — stereotype defines layer (controller/service/repository)
// Invariant: constructor injection — immutable, required deps; testable without container
```

> `spring.jpa.open-in-view=false` (Boot default since 2.x), closes `EntityManager` after TX, so lazy access outside TX fails fast instead of hiding N+1.

## Repositories, query derivation, JPQL, projections

```java title="Java 25 - Spring Data JPA repositories"

// Purpose: Spring Data JPA: repository abstraction over JPA/Hibernate; derived queries; flush/commit semantics
// Framework: @Query @Param @Transactional @Modifying — Spring manages lifecycle and wiring; no manual new
// Roles: OrderRepository, DTO — stereotype defines layer (controller/service/repository)
// Invariant: proxy-based TX; self-invocation bypasses proxy; propagation controls commit boundary
```

### Query keywords (derived)

| Keyword | JPQL | Example |
|---|---|---|
| `And`, `Or` | `and` / `or` | `findByStatusAndCustomerId` |
| `Between`, `LessThan`, `GreaterThan` | `between`, `<`, `>` | `findByTotalBetween` |
| `Like`, `Containing`, `StartingWith` | `like %?%` | `findByCustomerIdContaining` |
| `OrderBy` | `order by` | `findByStatusOrderByTotalDesc` |
| `Top3`, `First` | `limit` | `findTop3ByStatusOrderByCreatedAtDesc` |
| `IgnoreCase` | `upper()` | `findByCustomerIdIgnoreCase` |

### Projections vs entities

| Projection | What it returns | When to use |
|---|---|---|
| Entity `Order` | Full managed entity | Need to modify & flush |
| Interface projection | `interface OrderView { String getCustomerId(); }` | Read-only subset, no manual query |
| Record / DTO via JPQL `new` | Immutable `OrderDto` record | API response, no managed overhead |
| `Tuple` / `Object[]` | Raw columns | Ad-hoc reporting |

## Transactions, @Transactional

| Attribute | Options | Default | Notes |
|---|---|---|---|
| `propagation` | `REQUIRED`, `REQUIRES_NEW`, `NESTED`, `SUPPORTS`, `MANDATORY`, ... | `REQUIRED` | Join or new |
| `isolation` | `READ_COMMITTED` … `SERIALIZABLE` | `DEFAULT` (DB) | Higher → more locks |
| `readOnly` | `true/false` | `false` | Optimises flush/dirty check; route to replica |
| `rollbackFor` | exception classes | Unchecked only | Add `rollbackFor = Exception.class` for checked |
| `timeout` | seconds | `-1` | Rollback on timeout |

```java title="Java 25 - @Transactional service (virtual-thread aware)"

// Purpose: Spring Data JPA: repository abstraction over JPA/Hibernate; derived queries; flush/commit semantics
// Framework: @Service @Transactional — Spring manages lifecycle and wiring; no manual new
// Roles: OrderService, OrderFacade — stereotype defines layer (controller/service/repository)
// Invariant: proxy-based TX; self-invocation bypasses proxy; propagation controls commit boundary
```

### Virtual threads & JPA, rules (Java 25)

| Concern | Behaviour |
|---|---|
| TX binding | `TransactionSynchronizationManager` uses `ThreadLocal` per virtual thread, isolation preserved |
| Child threads | `StructuredTaskScope` / `newVirtualThreadPerTaskExecutor()` children do not inherit TX, keep DB work on owning thread |
| Blocking cost | JDBC call parks virtual thread (JEP 491), many concurrent TXs without pool exhaustion |
| Read-only TX | `readOnly=true` skips dirty checking, preferred for queries on virtual threads |

### Configuration (Boot 3.5)

```yaml title="application.yml - JPA / Hibernate"
spring:
  threads.virtual.enabled: true
  datasource:
    url: jdbc:postgresql://localhost:5432/demo
    hikari.maximum-pool-size: 20
  jpa:
    hibernate.ddl-auto: validate   # never update/create in prod
    open-in-view: false
    show-sql: false
    properties:
      hibernate.jdbc.batch_size: 25
      hibernate.order_inserts: true
      hibernate.order_updates: true
      hibernate.jdbc.batch_versioned_data: true
      hibernate.query.fail_on_pagination_over_collection_fetch: true
```

## Pros / cons

| Pros | Cons |
|---|---|
| Zero DAO boilerplate, interface is implementation | Magic proxy, method-name typos fail at startup, not compile time |
| Paging, sorting, `Specification`, `QueryDSL` built-in | Lazy loading outside TX → `LazyInitializationException` (fix: fetch join / EntityGraph, not `open-in-view`) |
| Hibernate dirty checking → no manual UPDATE | N+1 easy to introduce, always verify with `hibernate.stat` / `datasource-proxy` |
| `@Transactional` declarative, virtual-thread-friendly (parks on JDBC) | TX is thread-bound, cannot span `StructuredTaskScope` children |
| Records as DTOs + JPQL `new` keep API immutable | Entities still need no-arg constructor + mutable fields for Hibernate |

## Code Example, End-to-End (Java 25)

```java title="Java 25"

// Purpose: Spring Data JPA: repository abstraction over JPA/Hibernate; derived queries; flush/commit semantics
// Framework: @SpringBootApplication @NotBlank @NotNull @Positive — Spring manages lifecycle and wiring; no manual new
// Roles: JpaApplication, CreateOrderRequest, OrderDto — stereotype defines layer (controller/service/repository)
// Invariant: proxy-based TX; self-invocation bypasses proxy; propagation controls commit boundary
```

## Interview Q&A

Q: JPA vs Hibernate vs Spring Data JPA? JPA is the spec (`EntityManager`, annotations, JPQL); Hibernate is the JPA provider (implements the spec + extras like `@CreationTimestamp`, batching); Spring Data JPA is the repository abstraction over `EntityManager`/Hibernate, generates implementations from interfaces.

Q: Entity lifecycle states? Transient (`new`), Managed (in persistence context), Detached (context closed/cleared), Removed (scheduled delete). `persist` → managed, `detach/clear` → detached, `merge` re-attaches, `remove` schedules delete.

Q: What is dirty checking? Hibernate snapshots managed entities at load; at flush it diffs current state vs snapshot and issues `UPDATE` for changed fields automatically, no explicit `save()` needed inside a TX.

**Q: `save()` vs `saveAndFlush()`?** `save()` registers in context; flush may be deferred to commit/query. `saveAndFlush()` forces `flush()` immediately, needed when DB constraint must be validated before continuing.

Q: How to avoid N+1? Mark associations `LAZY`, use `join fetch` / `@EntityGraph` / DTO projections, set `hibernate.jdbc.batch_size`, and keep `open-in-view=false` so lazy outside TX fails fast.

**Q: `REQUIRED` vs `REQUIRES_NEW`?** `REQUIRED` joins caller's TX (single commit); `REQUIRES_NEW` suspends caller and commits independently, inner failure doesn't roll back outer.

Q: Which exceptions trigger rollback? Only unchecked (`RuntimeException`, `Error`) by default; add `rollbackFor = Exception.class` to include checked. Swallowing exceptions inside `@Transactional` prevents rollback, rethrow or `setRollbackOnly()`.

Q: How do transactions work with virtual threads (Java 25)? TX is per-thread via `TransactionSynchronizationManager`, each virtual thread has its own TX. `spring.threads.virtual.enabled=true` makes JDBC parks cheap (virtual thread parks, JEP 491), but TX does not propagate to `StructuredTaskScope` children. Keep TX on one virtual thread; fan out only non-TX work.

**Q: `GenerationType.SEQUENCE` vs `IDENTITY`?** `SEQUENCE` with `allocationSize=50` allows JDBC batching and pooled IDs, preferred. `IDENTITY` forces immediate INSERT (no batching) and is MySQL-idiomatic.

Q: AOT / native image for JPA? Boot's AOT generates entity reflection hints at build time; custom converters/listeners may need `RuntimeHintsRegistrar` or `@RegisterReflectionForBinding`.


<!-- SR -->
JPA vs Hibernate vs Spring Data JPA?:: JPA is the spec (`EntityManager`, annotations, JPQL); Hibernate is the JPA provider (implements the spec + extras like `@CreationTimestamp`, batching); Spring Data JPA is the repository abstraction over `EntityManager`/Hibernate, generates implementations from interfaces. #flashcard
Entity lifecycle states?:: Transient (`new`), Managed (in persistence context), Detached (context closed/cleared), Removed (scheduled delete). `persist` → managed, `detach/clear` → detached, `merge` re-attaches, `remove` schedules delete. #flashcard
What is dirty checking?:: Hibernate snapshots managed entities at load; at flush it diffs current state vs snapshot and issues `UPDATE` for changed fields automatically, no explicit `save()` needed inside a TX. #flashcard
`save()` vs `saveAndFlush()`?:: `save()` registers in context; flush may be deferred to commit/query. `saveAndFlush()` forces `flush()` immediately, needed when DB constraint must be validated before continuing. #flashcard
How to avoid N+1?:: Mark associations `LAZY`, use `join fetch` / `@EntityGraph` / DTO projections, set `hibernate.jdbc.batch_size`, and keep `open-in-view=false` so lazy outside TX fails fast. #flashcard
`REQUIRED` vs `REQUIRES_NEW`?:: `REQUIRED` joins caller's TX (single commit); `REQUIRES_NEW` suspends caller and commits independently, inner failure doesn't roll back outer. #flashcard
Which exceptions trigger rollback?:: Only unchecked (`RuntimeException`, `Error`) by default; add `rollbackFor = Exception.class` to include checked. Swallowing exceptions inside `@Transactional` prevents rollback, rethrow or `setRollbackOnly()`. #flashcard
How do transactions work with virtual threads (Java 25)?:: TX is per-thread via `TransactionSynchronizationManager`, each virtual thread has its own TX. `spring.threads.virtual.enabled=true` makes JDBC parks cheap (virtual thread parks, JEP 491), but TX does not propagate to `StructuredTaskScope` children. Keep TX on one virtual thread; fan out only non-TX work. #flashcard
`GenerationType.SEQUENCE` vs `IDENTITY`?:: `SEQUENCE` with `allocationSize=50` allows JDBC batching and pooled IDs, preferred. `IDENTITY` forces immediate INSERT (no batching) and is MySQL-idiomatic. #flashcard
AOT / native image for JPA?:: Boot's AOT generates entity reflection hints at build time; custom converters/listeners may need `RuntimeHintsRegistrar` or `@RegisterReflectionForBinding`. #flashcard

## Pitfalls

- Leaving `spring.jpa.hibernate.ddl-auto=update` in prod, use `validate` + Flyway/Liquibase.
- Keeping `open-in-view=true`, hides N+1 and holds `EntityManager` through view rendering; set `false`.
- Calling `@Transactional` method via `this` (self-invocation), bypasses proxy; move to another bean or inject self-proxy.
- Exposing entities as REST responses, leaks lazy proxies and couples API to persistence; always map to `record` DTOs.
- `EAGER` fetching on collections, loads entire graph; use `LAZY` + fetch joins.
- Forgetting `@Version`, lost updates silently overwrite; add optimistic locking.
- Forking `StructuredTaskScope` inside `@Transactional` expecting TX, child threads have no TX; fetch outside or use `TransactionTemplate` per child.
- `IDENTITY` + batching, incompatible; switch to `SEQUENCE` for batch inserts.
- Native image without entity hints, `NoSuchMethodException` at startup; let Boot AOT generate or add `RuntimeHintsRegistrar`.

## Related

- [[Spring Framework]] • [[Spring Core]] • [[Spring Transaction]] • [[Spring Boot]] • [[Spring MVC]] • [[Threads]]
- [[README|Java MOC]]

---
*Category: Spring • Part of [[README|Java MOC]] • Java 25*
