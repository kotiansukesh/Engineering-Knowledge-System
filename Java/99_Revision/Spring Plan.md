---
title: "Spring Boot Plan — 14 Days"
category: Revision
tags: [plan, spring, revision]
created: 2026-09-02
updated: 2026-09-02
---

# Spring Boot Plan — 14 Days

> Focus: Spring Boot 3.5 + MVC + JPA + Security + Transaction + Patterns for Spring. **Prereq:** finish [[Java Plan]] Weeks 1-2 (Core/OOP/Collections) or skim [[01_Core-Java/Cheat Sheet]]. Java 25 + virtual threads throughout.

```dataview
TABLE WITHOUT ID choice(completed, "✅", "⬜") as "Done", file.link as "Note", category as "Category", reviewed as "Reviewed"
FROM "Java/05_Spring" OR "Java/06_Design-Patterns" OR "Java/04_Concurrency"
WHERE category
SORT file.path ASC
LIMIT 5
```

## Week 1 — Spring Core + Boot

### Day 1 — Spring Framework & Core ⏱ 60 min
- [ ] [[Spring Framework]] • [[Spring Core]] • [[Dependency Injection]] — IoC, BeanFactory vs ApplicationContext, scopes, lifecycle
- [ ] [[Dependency Injection Pattern]] (Design Patterns Extra) • [[Singleton]] (enum)
- Goal: DI styles, which to use when

### Day 2 — Spring Boot ⏱ 75 min
- [ ] [[Spring Boot]] — starters, auto-config `@Conditional*`, `application.yml` + `@ConfigurationProperties` record, Actuator
- [ ] `spring.threads.virtual.enabled=true` — Tomcat/Jetty with virtual threads
- Goal: Boot magic + AOT hints

### Day 3 — Spring MVC ⏱ 75 min
- [ ] [[Spring MVC]] — `@RestController`, `ResponseEntity`, validation on records, `@ControllerAdvice` + `ProblemDetail`
- [ ] Filter vs Interceptor vs AOP — where to log/auth
- Goal: one happy-path CRUD + error handler

### Day 4 — Spring Data JPA ⏱ 75 min
- [ ] [[Spring Data JPA]] — JPA states (transient/managed/detached), Hibernate dirty-checking, L1/L2, N+1 fix `join fetch` / `@EntityGraph`
- [ ] Repositories (derived/JPQL/paging/projections) + `@Modifying`
- Goal: draw JPA lifecycle diagram

### Day 5 — Transaction & Concurrency for Spring ⏱ 75 min
- [ ] [[Spring Transaction]] — `@Transactional` propagation/isolation, proxy pitfall (self-invocation), `TransactionTemplate`
- [ ] [[Executor Framework]] • [[CompletableFuture]] — `newVirtualThreadPerTaskExecutor()` **inside** service (not inside TX)
- Goal: why not fork inside `@Transactional`

### Day 6 — Review + Flashcards ⏱ 45 min
- [ ] SR queue from [[Spring Framework]] → [[Spring Data JPA]]
- [ ] [[05_Spring/Cheat Sheet|Spring Cheat Sheet]]

## Week 2 — Security + Patterns + Mocks

### Day 7 — Spring Security ⏱ 75 min
- [ ] [[Spring Security]] — filter chain `DelegatingFilterProxy → FilterChainProxy`, JWT/OAuth2/OIDC, Security 6 DSL
- [ ] [[Locks and Synchronizers]] • [[Concurrent Collections]] — when Spring needs them
- Goal: secure one endpoint end-to-end

### Day 8 — Design Patterns for Spring ⏱ 75 min
- [ ] [[Factory Method]] • [[Abstract Factory]] • [[Builder]] • [[Prototype]] • [[Adapter]] • [[Decorator]] • [[Proxy]] — how Spring uses them
- Goal: map each pattern to a Spring class (`BeanFactory`, `RestTemplate`, `AOP Proxy`)

### Day 9 — Behavioral Patterns in Services ⏱ 60 min
- [ ] [[Strategy]] • [[Observer]] (with virtual threads + `StructuredTaskScope`) • [[Command]] • [[Template Method]] • [[Chain of Responsibility]]
- Goal: Strategy/Observer are Spring service staples

### Day 10 — Structural Cleanup ⏱ 45 min
- [ ] [[Facade]] • [[Composite]] • [[Flyweight]] (record) • [[Memento]] (record) • [[Bridge]]
- [ ] [[DAO Pattern]] • [[Dependency Injection Pattern]]

### Day 11 — Iterator/Mediator/State/Visitor ⏱ 45 min
- [ ] [[Iterator]] • [[Mediator]] • [[State]] • [[Visitor]] (sealed switch replaces double dispatch)

### Day 12 — Mock 1 — Spring ⏱ 90 min
- [ ] Random 10 from `99_Revision/Interview Questions.md` Spring section
- [ ] Whiteboard one pattern + one transaction propagation

### Day 13 — Mock 2 — Full Stack ⏱ 90 min
- [ ] Build: `Controller (MVC)` → `Service (@Transactional + virtual threads)` → `Repository (JPA)` — explain each layer

### Day 14 — Final Review ⏱ 60 min
- [ ] [[06_Design-Patterns/Cheat Sheet|Patterns Cheat Sheet]] • [[04_Concurrency/Cheat Sheet|Concurrency Cheat Sheet]] • SR overdue
- [ ] Mark all Spring notes `completed: true` + `reviewed: 2026-09-03`

---
*Part of [[README|Java MOC]] • [[Java Plan|← Java Plan]] • [[30-Day Plan|Legacy Combined Plan]]*
