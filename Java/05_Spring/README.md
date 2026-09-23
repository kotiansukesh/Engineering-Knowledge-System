---
title: "Spring"
category: "Spring"
tags: [spring, framework, boot, java25]
created: 2026-09-03
pattern: 0
difficulty: Hard
completed: false
reviewed:
sr-due:
---# Spring Framework

> IoC container, DI, Boot auto-config, MVC, Data JPA, Security, Transactions , all notes now carry **native mermaid architecture diagrams** and **real runnable Java 25 snippets** (no stub blocks). One flag runs everything on virtual threads: `spring.threads.virtual.enabled=true`. | Part of [[README|Java MOC]]
```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category"
FROM "Java/05_Spring"
WHERE file.name != "README"
SORT file.name ASC
```

## Progress

```dataview
TABLE WITHOUT ID file.link as "Note", choice(completed, "✅", "⬜") as "Done"
FROM "Java/05_Spring"
WHERE category
SORT file.name ASC
```

## The 9 Notes , What Lives Here

| # | Note | Mermaid diagram | Interview 60-sec |
|---|------|-----------------|------------------|
| 1 | [[Spring Framework]] | IoC container flowchart (scan → definitions → DI → AOP proxy) | Framework vs Boot vs Cloud; constructor injection; JDK vs CGLIB proxies |
| 2 | [[Spring Core]] | Container flowchart (registry → context → env/events/resources/AOP) | `BeanFactory` vs `ApplicationContext`; scopes; AOT hints |
| 3 | [[Dependency Injection]] | Tight-coupling vs IoC-container diagram | Constructor > setter > field; `@Qualifier` vs `@Primary`; `@Lazy` |
| 4 | [[Spring Boot]] | Auto-configuration flowchart (`@Conditional` → conditional beans → server) | Starters vs auto-config; config order; Actuator security |
| 5 | [[Spring MVC]] | Request flow (`Tomcat → Filter → DispatcherServlet → Controller → JSON`) | Dispatch flow; `@ControllerAdvice` + `ProblemDetail`; MVC vs WebFlux |
| 6 | [[Spring Data JPA]] | Layer flowchart + entity-state `stateDiagram-v2` (transient→managed→detached→removed) | N+1 fixes; dirty checking; `REQUIRED` vs `REQUIRES_NEW` |
| 7 | [[Spring Transaction]] | Proxy flow (`client → proxy → interceptor → commit/rollback`) | Self-invocation trap; rollback rules; TX stays on one virtual thread |
| 8 | [[Spring Security]] | Filter-chain flowchart (request → authN → context → authZ → controller) | AuthN vs authZ; JWT validation; `DelegatingSecurityContext*` on virtual threads |
| 9 | [[Cheat Sheet]] | MVC request-flow diagram + vs tables | Last-night revision |

> **Virtual threads everywhere:** `spring.threads.virtual.enabled=true` (Boot 3.2+/3.5, Java 25) moves Tomcat + `@Async` + scheduling to virtual threads. TX stays thread-bound; propagate security context with `DelegatingSecurityContext*`; prefer `ScopedValue` over `ThreadLocal` (see [[Threads]]).

## How to use

- **New to Spring?** Read [[Spring Framework]] → [[Spring Core]] → [[Dependency Injection]] → [[Spring Boot]] → [[Spring MVC]] → [[Spring Data JPA]] → [[Spring Transaction]] → [[Spring Security]].
- **Interview?** Every `## Interview Q&A` doubles as `` flashcards.
- **Native image?** Each note has an AOT hints snippet (`RuntimeHintsRegistrar` / `@RegisterReflectionForBinding`).

[[README|← Back to Java MOC]]
