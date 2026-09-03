---
title: "Spring Transaction"
category: Spring
tags: [spring, transaction, aop, jdbc, jpa, java25, virtual-threads]
created: 2026-01-18
updated: 2026-09-02
---

# Spring Transaction

> Part of [[README|Java MOC]] • `Spring` • Java 25 / Spring Framework 6.2 / Boot 3.5

## Intent
Make transaction management declarative (`@Transactional`) so that service code states *what* must be atomic/consistent/isolated/durable (ACID) without manually opening, committing, or rolling back JDBC/JPA transactions, with Spring handling commit/rollback via AOP proxies.


> Transactions look simple until they don't apply. I always check: are you calling through the proxy? Self-invocation silently skips @Transactional, catches everyone once.

## Definition
Spring's transaction abstraction (`PlatformTransactionManager` / `TransactionManager`) sits over `DataSourceTransactionManager` (JDBC), `JpaTransactionManager` (JPA/Hibernate), or `ReactiveTransactionManager` (R2DBC). `@Transactional` on a bean method causes a proxy to start a transaction before the method, commit on success, or roll back on (unchecked) exception.

## Architecture, diagram description

```
  Client → @Transactional Proxy (JDK/CGLIB)
                │
                ├── TransactionInterceptor
                │     │  1. TransactionAttributeSource reads @Transactional
                │     │  2. PlatformTransactionManager.getTransaction(def)
                │     ▼
                │   Transaction (PROPAGATION, ISOLATION, timeout, readOnly)
                │     │
                ▼     ▼
            Target Service Method (business logic + Repository/JPA calls)
                │
                ├── success → manager.commit(tx)
                └── RuntimeException / rollbackFor → manager.rollback(tx)

  Stack:
  @EnableTransactionManagement → TransactionInterceptor (AOP Advice)
        → AbstractPlatformTransactionManager → DataSource / JpaTransactionManager
        → JDBC Connection / EntityManager bound to thread (TransactionSynchronizationManager)

  Java 25: TransactionSynchronizationManager now supports ScopedValue propagation
           for virtual threads / StructuredTaskScope (Spring 6.2+).
```

Reference talk: https://www.youtube.com/watch?v=eWl8G7NDKqo&list=PLVz2XdJiJQxxj_zMhm6zCPO6zhtOcq-wl

## `@Transactional`, key attributes

| Attribute | Options | Default | Notes |
|---|---|---|---|
| `propagation` | `REQUIRED`, `REQUIRES_NEW`, `NESTED`, `SUPPORTS`, `NOT_SUPPORTED`, `MANDATORY`, `NEVER` | `REQUIRED` | Join existing or start new |
| `isolation` | `DEFAULT`, `READ_UNCOMMITTED`, `READ_COMMITTED`, `REPEATABLE_READ`, `SERIALIZABLE` | `DEFAULT` (DB) | Higher → more locking, less concurrency |
| `readOnly` | `true` / `false` | `false` | Hint for optimisation; some DBs enforce |
| `timeout` | seconds | `-1` (none) | Rollback on timeout |
| `rollbackFor` / `noRollbackFor` | exception classes | Rollback on unchecked (`RuntimeException`/`Error`) only | Add `rollbackFor = Exception.class` to include checked |
| `transactionManager` | bean name | primary `TransactionManager` | For multiple data sources |

### Propagation cheat-sheet

| Propagation | If TX exists | If no TX |
|---|---|---|
| `REQUIRED` | Join | Create new |
| `REQUIRES_NEW` | Suspend & create new | Create new |
| `NESTED` | Nested savepoint | Create new |
| `SUPPORTS` | Join | Non-transactional |
| `MANDATORY` | Join | Throw exception |
| `NEVER` | Throw exception | Non-transactional |

## Virtual threads & transactions (Java 25)

> Enable virtual threads: `spring.threads.virtual.enabled=true` (Boot 3.2+/3.5). Transactions remain thread-bound, each virtual thread gets its own transaction, just like platform threads. What changes is context propagation and blocking cost.

### TransactionSynchronizationManager with virtual threads

`TransactionSynchronizationManager` historically uses `ThreadLocal` to bind `Connection` / `EntityManager` / synchronizations to the current thread. On Java 25 with virtual threads:

| Concern | Platform threads | Virtual threads (Java 25 / Spring 6.2+) |
|---|---|---|
| TX binding | `ThreadLocal<ConnectionHolder>` per platform thread | Same per virtual thread, each virtual thread has its own `ThreadLocal`, so isolation is preserved |
| Propagating TX to child threads | Not supported (TX is thread-bound by design) | Still not supported, don't fork a `StructuredTaskScope` inside a `@Transactional` and expect the TX to propagate. Keep TX on the owning thread |
| `ScopedValue` | N/A | Spring 6.2+ can expose TX context via `ScopedValue` for read-only propagation to structured children (not for committing) |
| Blocking cost | Platform thread blocked for DB call duration | Virtual thread parks (JEP 491), cheap, no carrier pinning |

```java title="Java 25 - @Transactional on virtual threads (no code change)"

// Purpose: Spring Transaction: proxy-based @Transactional; REQUIRED joins, REQUIRES_NEW suspends; self-invocation bypasses proxy
// Framework: @Service @Transactional @Configuration @EnableTransactionManagement — Spring manages lifecycle and wiring; no manual new
// Roles: OrderService, TxConfig — stereotype defines layer (controller/service/repository)
// Invariant: proxy-based TX; self-invocation bypasses proxy; propagation controls commit boundary
```

```java title="Java 25 - DO NOT propagate TX into structured children"

// Purpose: Spring Transaction: proxy-based @Transactional; REQUIRED joins, REQUIRES_NEW suspends; self-invocation bypasses proxy
// Framework: @Service @Transactional — Spring manages lifecycle and wiring; no manual new
// Roles: BadPattern — stereotype defines layer (controller/service/repository)
// Invariant: proxy-based TX; self-invocation bypasses proxy; propagation controls commit boundary
```

Rules for Java 25:
- `@Transactional` is thread-bound, the TX lives on the thread that entered the proxy. Child virtual threads from `StructuredTaskScope` or `newVirtualThreadPerTaskExecutor()` do not inherit it.
- Keep the TX short and on one virtual thread; fan out outside the TX or fan out non-TX work only.
- `spring.threads.virtual.enabled=true` makes blocking TX calls cheap (virtual thread parks), but does not make long TXs desirable, they still hold DB locks.
- For async TX, use `TransactionTemplate` on the target thread or `@Transactional` on the async method itself (with `DelegatingSecurityContext` if needed).

### Programmatic alternative (when AOP cannot apply), Java 25

```java title="Java 25"

// Purpose: Spring Transaction: proxy-based @Transactional; REQUIRED joins, REQUIRES_NEW suspends; self-invocation bypasses proxy
// Framework: @Service — Spring manages lifecycle and wiring; no manual new
// Roles: ProgrammaticService — stereotype defines layer (controller/service/repository)
// Invariant: constructor injection — immutable, required deps; testable without container
```

## How `@Transactional` works internally
1. `@EnableTransactionManagement` registers `TransactionInterceptor` + auto-proxy creator.
2. At startup, beans with `@Transactional` are wrapped in a proxy.
3. On method call, `TransactionInterceptor` reads `TransactionAttribute`, asks `PlatformTransactionManager` for a `TransactionStatus`, binds `Connection`/`EntityManager` to thread via `TransactionSynchronizationManager` (now `ScopedValue`-aware on Java 25).
4. Invokes target method; on return commits, on exception evaluates rollback rules.

## AOT Hints for Transactions (Java 25 / GraalVM)

```java title="Java 25 - AOT hints for TX"

// Purpose: Spring Transaction: proxy-based @Transactional; REQUIRED joins, REQUIRES_NEW suspends; self-invocation bypasses proxy
// Framework: @ImportRuntimeHints @Configuration @Override — Spring manages lifecycle and wiring; no manual new
// Roles: TxHints — stereotype defines layer (controller/service/repository)
// Invariant: constructor injection — immutable, required deps; testable without container
```
- `@Transactional` proxies are auto-registered by Boot's AOT engine. Custom `PlatformTransactionManager` or `TransactionSynchronization` impls may need hints.

## Pros / cons

| Pros | Cons |
|---|---|
| Declarative, no boilerplate `try/commit/rollback` | Proxy-based, self-invocation bypasses TX |
| Unified abstraction over JDBC/JPA/JMS/R2DBC | Misunderstood defaults (checked exceptions don't roll back) |
| Propagation/isolation/timeout/readonly in one place | Long TXs hold DB locks → contention; keep TX short (even on virtual threads) |
| Testable with `@Transactional` on tests (auto-rollback) | Multiple `TransactionManager`s require qualification |
| Virtual threads make blocking TX calls cheap (no pool exhaustion) | TX still thread-bound, cannot span structured children |

## Interview Q&A

**Q: Why doesn't `@Transactional` work when method is called via `this`?** Self-invocation skips the proxy; call goes directly to target. Fix: inject `self` proxy, move method to another bean, or use `AspectJ` weaving.

Q: Which exceptions trigger rollback by default? Only unchecked (`RuntimeException`, `Error`). For checked exceptions add `rollbackFor = Exception.class`.

**Q: `REQUIRED` vs `REQUIRES_NEW`?** `REQUIRED` joins caller's TX (one commit); `REQUIRES_NEW` suspends caller TX and commits independently, inner failure doesn't roll back outer (unless outer chooses to).

**Q: What is `readOnly=true` really?** Hint to provider: may flush less, disable dirty checks, route to read replica; not a security guard.

Q: How to make two data sources transactional together? Need XA / JTA (`JtaTransactionManager`) or use the saga/outbox pattern; plain `DataSourceTransactionManager` is one resource only.

Q: Transactional tests auto-rollback, good or bad? Good for isolation; but the TX never truly commits, lazy-loading quirks differ from production. Use `@Commit` or `TestEntityManager` when commit semantics matter.

Q: How do transactions work with virtual threads (Java 25)? TX is still thread-bound via `TransactionSynchronizationManager`, each virtual thread has its own TX. `spring.threads.virtual.enabled=true` makes blocking DB calls cheap (virtual thread parks, JEP 491), but TX does not propagate to child virtual threads from `StructuredTaskScope` or `newVirtualThreadPerTaskExecutor()`. Keep TX on one thread; fan out non-TX work only.


<!-- SR -->
Why doesn't `@Transactional` work when method is called via `this`?:: Self-invocation skips the proxy; call goes directly to target. Fix: inject `self` proxy, move method to another bean, or use `AspectJ` weaving. #flashcard
Which exceptions trigger rollback by default?:: Only unchecked (`RuntimeException`, `Error`). For checked exceptions add `rollbackFor = Exception.class`. #flashcard
`REQUIRED` vs `REQUIRES_NEW`?:: `REQUIRED` joins caller's TX (one commit); `REQUIRES_NEW` suspends caller TX and commits independently, inner failure doesn't roll back outer (unless outer chooses to). #flashcard
What is `readOnly=true` really?:: Hint to provider: may flush less, disable dirty checks, route to read replica; not a security guard. #flashcard
How to make two data sources transactional together?:: Need XA / JTA (`JtaTransactionManager`) or use the saga/outbox pattern; plain `DataSourceTransactionManager` is one resource only. #flashcard
Transactional tests auto-rollback, good or bad?:: Good for isolation; but the TX never truly commits, lazy-loading quirks differ from production. Use `@Commit` or `TestEntityManager` when commit semantics matter. #flashcard
How do transactions work with virtual threads (Java 25)?:: TX is still thread-bound via `TransactionSynchronizationManager`, each virtual thread has its own TX. `spring.threads.virtual.enabled=true` makes blocking DB calls cheap (virtual thread parks, JEP 491), but TX does not propagate to child virtual threads from `StructuredTaskScope` or `newVirtualThreadPerTaskExecutor()`. Keep TX on one thread; fan out non-TX work only. #flashcard

## Pitfalls
- Annotating `private`/`final` methods or the class's internal calls, proxy cannot intercept.
- Catching and swallowing exceptions inside `@Transactional` method → no rollback (rethrow or `TransactionAspectSupport.currentTransactionStatus().setRollbackOnly()`).
- Long-running TXs doing HTTP/IO, extends lock duration; split work (virtual threads reduce thread starvation but not DB lock contention).
- `NESTED` requires savepoints, not supported by all drivers.
- Forgetting `@EnableTransactionManagement` outside Spring Boot (Boot enables it).
- Forking `StructuredTaskScope` inside `@Transactional` and expecting TX propagation, it won't propagate.
- Native image without hints for custom TX types, add `RuntimeHintsRegistrar`.

## Related
- [[Spring Framework]] • [[Spring Core]] • [[Dependency Injection]] • [[Spring Security]] • [[Threads]]
- [[README|Java MOC]]

---
*Category: Spring • Part of [[README|Java MOC]] • Java 25*
