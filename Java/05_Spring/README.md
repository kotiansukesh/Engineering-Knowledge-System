---
title: "05 Spring"
category: "Java/05_Spring"
type: "folder-MOC"
tags: [MOC, spring, java]
created: "2026-09-30"
completed: false
reviewed: "2026-09-30"
sr-due: "2026-10-07"
---

# 05 Spring

> Learn Spring as a runtime and architecture model, not as a list of annotations.

## Canonical Reading Order

1. [[Spring Framework]] — IoC, bean lifecycle, AOP and proxy model.
2. [[Dependency Injection]] — composition and dependency boundaries.
3. [[Spring Boot]] — auto-configuration, configuration and production defaults.
4. [[Spring MVC]] — HTTP request processing and web boundaries.
5. [[Spring Data JPA]] — repositories, persistence context and query behavior.
6. [[Spring Transaction]] — transaction boundaries, propagation and isolation.
7. [[Spring Security]] — filter chain, authentication, authorization and method security.
8. [[Spring AI]] — Java/Spring integration with models, RAG and tool calling.

## Version Strategy

As of September 2026, the current Spring generation is Spring Framework 7 and Spring Boot 4.x, with Java 25 as a first-class baseline for the new generation. Keep older Spring 6 / Boot 3 notes as migration knowledge when you work on existing systems; do not mix APIs from different generations without checking the project's dependency management.

## What Senior Engineers Must Explain

- What the container actually does during startup.
- How dependency injection differs from service location.
- Where proxies intercept calls and where self-invocation bypasses advice.
- How transaction boundaries interact with persistence context and thread ownership.
- How the security filter chain establishes request security.
- What Boot auto-configuration adds and how to override it deliberately.
- How to test framework behavior without turning every test into a full application-context test.

## Practice

- [ ] Build one controller → service → repository slice.
- [ ] Add validation and consistent error responses.
- [ ] Add one transaction boundary and explain its propagation/isolation choice.
- [ ] Add authentication and authorization and explain the filter chain.
- [ ] Add an integration test against a real database container.

## Related

- [[../04_Concurrency/README|Concurrency]]
- [[../11_JVM-Performance/README|JVM & Performance]]
- [[../12_Testing-Tooling/README|Testing & Tooling]]
- [[../AI/README|AI Engineering]]
- [[../README|Java MOC]]
