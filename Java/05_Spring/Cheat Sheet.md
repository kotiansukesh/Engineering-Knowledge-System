---
category: CheatSheet
tags: [java, spring, cheatsheet]
title: Spring / Spring Boot — Cheat Sheet
---

# Spring / Spring Boot — Cheat Sheet

## Spring MVC Request Flow

```mermaid
flowchart LR
    C[Client] --> DS[DispatcherServlet]
    DS --> HM[HandlerMapping]
    HM --> CT[Controller @GetMapping]
    CT --> SV[Service]
    SV --> RP[Repository/JPA]
    CT --> VN[View/JSON via HttpMessageConverter]
    VN --> DS --> C
    DS --- IR[Interceptor pre/post]
    DS --- EH[@ControllerAdvice ExceptionHandler]
    DS --- FL[Filter - before DS]
```

## Vs Tables

| Comparison | A | B | Pick |
|---|---|---|---|
| **@Component vs @Service vs @Repository vs @Controller** | All are `@Component` stereotypes | `@Repository` adds persistence exception translation; `@Service` semantics | Use specific stereotype for clarity + AOP pointcuts |
| **@Autowired vs Constructor injection** | Field injection (hidden dep, hard test) | Constructor injection (immutable, required) | **Constructor injection** — mandated since Spring 4.3 |
| **@Scope singleton vs prototype** | Singleton: 1 per container (default) | Prototype: new per injection/request | Singleton + stateless beans; prototype for stateful |
| **@Transactional REQUIRED vs REQUIRES_NEW** | REQUIRED joins existing TX | REQUIRES_NEW suspends & creates new | REQUIRES_NEW for audit/log that must commit independently |
| **Filter vs Interceptor vs AOP** | Filter: Servlet, before DS | Interceptor: Spring MVC, pre/post Handle | AOP: any Spring bean method |
| **JPA save vs saveAndFlush** | `save` may defer to flush/commit | `saveAndFlush` immediate DB write | Flush only when you need ID or constraint check now |
| **RestTemplate vs WebClient** | Blocking, deprecated | Non-blocking reactive | WebClient (or RestClient in Spring 6.1+) |

## Annotations — Must Know

| Annotation | Purpose |
|---|---|
| `@SpringBootApplication` | `@Configuration + @EnableAutoConfiguration + @ComponentScan` |
| `@RestController` | `@Controller + @ResponseBody` — JSON |
| `@RequestBody / @ResponseBody` | JSON ↔ object via Jackson |
| `@PathVariable / @RequestParam / @RequestHeader` | URL / query / header binding |
| `@Valid + @Validated` | Bean validation (`@NotNull`, `@Size`) |
| `@Transactional` | Proxy-based TX; self-invocation bypasses proxy! |
| `@Async / @EnableAsync` | Async execution (needs executor) |
| `@Cacheable / @CacheEvict` | Declarative caching |
| `@Value("${prop:default}")` | Property injection; prefer `@ConfigurationProperties` for groups |
| `@Profile("prod")` / `@ConditionalOnProperty` | Conditional beans |
| `@ControllerAdvice + @ExceptionHandler` | Global exception handling |

## Boot Internals — Interview Hot

| Topic | One-Liner |
|---|---|
| **Auto-configuration** | `spring.factories` / `AutoConfiguration.imports` + `@ConditionalOnClass/OnMissingBean` |
| **Starter** | Opinionated dependency set (`spring-boot-starter-web` → Tomcat+Spring MVC+Jackson) |
| **Actuator** | `/actuator/health, metrics, env, beans, mappings` |
| **Externalized config order** | CLI args > env vars > `application-{profile}.yml` > `application.yml` > defaults |
| **Transaction proxy trap** | `@Transactional` on private/self-called method = **no TX** (proxy not invoked) — extract to another bean |
| **N+1** | `FetchType.LAZY` + `@EntityGraph` / `JOIN FETCH` / `BatchSize` |

## Java 25 One-Liners

```java

// Purpose: Spring Cheat Sheet: annotations, scopes, and request flow at a glance
// Framework: @NotBlank @Email @RestController @RequiredArgsConstructor — Spring manages lifecycle and wiring; no manual new
// Roles: as, CreateUserRequest, UserController — stereotype defines layer (controller/service/repository)
// Invariant: proxy-based TX; self-invocation bypasses proxy; propagation controls commit boundary
```

*Category: CheatSheet*
