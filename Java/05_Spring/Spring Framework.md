---
title: "Spring Framework"
category: Spring
tags: [spring, framework, ioc, di, aop, java25, virtual-threads]
created: 2026-01-18
updated: 2026-09-02
---

# Spring Framework

> Part of [[README|Java MOC]] • `Spring` • Java 25 / Spring Boot 3.5 / Spring Framework 6.2

## Intent
Spring Framework is a comprehensive, open-source application framework for the Java platform that simplifies enterprise Java development by providing Inversion of Control (IoC), Dependency Injection (DI), Aspect-Oriented Programming (AOP), and declarative services (transactions, security, data access) so that business code stays POJO-centric and testable.


> You can use Spring without Boot, but honestly I rarely do. The framework is the plumbing, Boot is the opinionated defaults on top, know which one you're debugging.

## Definition
Spring is a lightweight container + ecosystem. The container instantiates, wires, and manages the lifecycle of beans (objects declared in configuration / annotations) and applies cross-cutting concerns (transactions, security, caching) via proxies/AOP without coupling business code to infrastructure.

## Architecture, diagram description

```
┌─────────────────────────────────────────────────┐
│              Spring Framework 6.2               │
├──────────┬──────────┬─────────┬─────────────────┤
│   Core Container  │  AOP / Aspects │  Data Access/Integration │ Web (MVC/WebFlux) │
│  • spring-core    │  • spring-aop │  • spring-jdbc           │  • spring-web     │
│  • spring-beans   │  • spring-aspects │ • spring-tx         │  • spring-webmvc  │
│  • spring-context │  • spring-instrument │ • spring-orm (Hibernate/JPA) │ • spring-websocket│
│  • spring-expression (SpEL) │              │ • spring-jms / OXM    │  • spring-webflux │
├──────────┴──────────┴─────────┴─────────────────┤
│  Test: spring-test (JUnit 5, Mockito, TestContext) │
└─────────────────────────────────────────────────┘
         ▲
         │  Underlying: Jakarta EE, Reactive Streams, Micrometer, Virtual Threads (Loom)
```

Layered reading (bottom→top): `Core` (IoC/DI, SpEL) → `AOP` → `Data Access` (JDBC, ORM, TX) → `Web` (Servlet MVC or Reactive). Modern apps typically pull `spring-boot-starter-*` which auto-configures these. On Java 25 + Boot 3.5, the web layer can run on virtual threads with a single flag.

Original modular view: ![[Pasted image 20210916101820.png]]

### Core container (4 modules)
| Module | Role |
|---|---|
| `spring-core` | IoC/DI fundamentals, resource abstraction, type conversion |
| `spring-beans` | `BeanFactory`, bean definitions, lifecycle |
| `spring-context` | `ApplicationContext` (events, i18n, resources), annotation processing |
| `spring-expression (SpEL)` | Runtime expression language for bean wiring (`#{...}`) |

### Other Layers
- AOP / Aspects / Instrument, proxy-based advice, AspectJ integration, load-time weaving.
- Data Access / Integration, `spring-jdbc` (template, exception hierarchy), `spring-tx` (declarative transactions), `spring-orm` (Hibernate/JPA), `spring-jms`, `spring-oxm`.
- Web, `spring-web` (common), `spring-webmvc` (Servlet), `spring-webflux` (reactive), `spring-websocket`, `spring-webmvc-portlet` (legacy).

## Virtual Threads, Spring Boot 3.2+ / 3.5 on Java 25

> One flag to enable virtual threads everywhere: `spring.threads.virtual.enabled=true` (Boot 3.2+, stabilised in 3.5). On Java 25 this is the recommended default for IO-bound services.

```yaml title="Java 25 - application.yml (Boot 3.5)"
spring:
  threads:
    virtual:
      enabled: true   # Tomcat, Jetty, Undertow + @Async + scheduling → virtual threads
```
```properties title="or application.properties"
spring.threads.virtual.enabled=true
```

What the flag does:

| Component | Without flag (platform threads) | With `virtual.enabled=true` (Java 25) |
|---|---|---|
| Embedded Tomcat | `ThreadPoolExecutor` (default 200 threads) | `Executors.newVirtualThreadPerTaskExecutor()`, one virtual thread per request, no pool tuning |
| Jetty / Undertow | Platform thread pool | Virtual-thread executor |
| `@Async` | `SimpleAsyncTaskExecutor` on platform threads | Virtual-thread `AsyncTaskExecutor` |
| `@Scheduled` | Platform scheduler | Virtual-thread scheduler |
| Spring Data / JDBC | Blocks platform thread (scales to ~200 concurrent) | Blocks virtual thread (scales to 10k+ concurrent), no code change |

```java title="Java 25 - Spring Boot 3.5 minimal app on virtual threads"

// Purpose: Spring Framework: IoC container manages lifecycle; DI via constructor; AOP proxies cross-cutting concerns
// Framework: @SpringBootApplication @RestController @GetMapping @Configuration — Spring manages lifecycle and wiring; no manual new
// Roles: App, HelloController, AsyncConfig — stereotype defines layer (controller/service/repository)
// Invariant: stateless singleton controller; delegates to service; HTTP semantics via ResponseEntity
```

Custom thread factory (naming):
```java title="Java 25 - custom virtual-thread factory for Spring"

// Purpose: Spring Framework: IoC container manages lifecycle; DI via constructor; AOP proxies cross-cutting concerns
// Framework: @Configuration @Bean — Spring manages lifecycle and wiring; no manual new
// Roles: VirtualThreadConfig — stereotype defines layer (controller/service/repository)
// Invariant: constructor injection — immutable, required deps; testable without container
```

> When NOT to use virtual threads: CPU-bound batch, heavy computation, or JNI/native code, keep platform threads (`spring.threads.virtual.enabled=false` + custom `TaskExecutor` for those workloads). JEP 491 makes `synchronized` safe, but native frames still pin.

## AOT & graalvm native image, hints (Spring 6.2 / boot 3.5)

Spring Framework 6.2 + Boot 3.5 on Java 25 compile to GraalVM native image via AOT processing. Hints tell the ahead-of-time compiler what to keep.

```java title="Java 25 - RuntimeHintsRegistrar (AOT hints)"

// Purpose: Spring Framework: IoC container manages lifecycle; DI via constructor; AOP proxies cross-cutting concerns
// Framework: @Configuration @ImportRuntimeHints @Override @Transactional — Spring manages lifecycle and wiring; no manual new
// Roles: App, Hints — stereotype defines layer (controller/service/repository)
// Invariant: proxy-based TX; self-invocation bypasses proxy; propagation controls commit boundary
```
```java title="Java 25 - @RegisterReflectionForBinding (Boot 3.5 shortcut)"

// Purpose: Spring Framework: IoC container manages lifecycle; DI via constructor; AOP proxies cross-cutting concerns
// Framework: @RegisterReflectionForBinding @RestController — Spring manages lifecycle and wiring; no manual new
// Roles: OrderController — stereotype defines layer (controller/service/repository)
// Invariant: stateless singleton controller; delegates to service; HTTP semantics via ResponseEntity
```

Key points:
- `spring-boot:build-image` or `mvn -Pnative native:compile` triggers AOT → generates `reflect-config.json`, `resource-config.json` automatically for most Spring beans. Manual `RuntimeHintsRegistrar` only for dynamic reflection / custom serializers.
- Virtual threads work in native image (GraalVM 23.1+ / Java 25), no extra hint needed; `spring.threads.virtual.enabled=true` is honoured in native.
- Test with `mvn spring-boot:process-aot` then `java -Dspring.aot.enabled=true -jar app.jar`.

## Core Concepts
- IoC / DI, objects declare dependencies via constructors/setters/fields; the container injects them. See [[Spring Core]] and [[Dependency Injection]].
- AOP, cross-cutting logic (logging, TX, security) as `Aspect`s with pointcuts/advice; applied via JDK or CGLIB proxies.
- Bean lifecycle, `instantiate → populate → BeanNameAware → BeanFactoryAware → BeanPostProcessor → @PostConstruct → InitializingBean → ready → @PreDestroy → DisposableBean`.

## Pros / cons

| Pros | Cons |
|---|---|
| POJO programming, highly testable (mock-friendly) | Learning curve; magic of auto-configuration can obscure behaviour |
| Huge ecosystem (Boot, Security, Data, Cloud) | Startup time / memory footprint vs. bare Java or Quarkus/Micronaut (mitigated by Boot 3 + GraalVM native + AOT) |
| Declarative TX, security, caching via annotations | Reflection/proxy overhead; debugging AOP proxies |
| Strong community & backwards compatibility | Over-configuration possible, prefer Boot + starters |
| Production-ready observability (Actuator, Micrometer) | Classpath/bean overriding conflicts if dependency management is lax |
| Virtual threads (Java 25) eliminate thread-pool tuning for IO | Virtual threads require Java 21+ and driver compatibility checks |

## Code example, minimal DI without boot (Java 25)
```java title="Java 25"

// Purpose: Spring Framework: IoC container manages lifecycle; DI via constructor; AOP proxies cross-cutting concerns
// Framework: @Configuration @ComponentScan @Component @Autowired — Spring manages lifecycle and wiring; no manual new
// Roles: AppConfig, EmailService, MyApplication — stereotype defines layer (controller/service/repository)
// Invariant: constructor injection — immutable, required deps; testable without container
```

## Interview Q&A

Q: Spring Framework vs Spring Boot vs Spring Cloud? Framework is the core container; Boot adds auto-configuration, embedded server, starters, and Actuator for rapid apps; Cloud adds distributed-system patterns (config, discovery, gateway).

Q: Why does Spring prefer constructor injection? Immutability, guaranteed required deps, easier unit testing, avoids circular field-injection pitfalls.

Q: JDK dynamic proxy vs CGLIB? JDK proxy requires interfaces; CGLIB subclasses the class. Spring picks automatically; use `proxyTargetClass=true` to force CGLIB. On Java 25 with AOT, prefer interfaces for native-image friendliness (needs proxy hint otherwise).

Q: How to exclude an auto-configuration in Boot? `@SpringBootApplication(exclude = DataSourceAutoConfiguration.class)` or `spring.autoconfigure.exclude` in properties.

Q: Where does AOP sit architecturally? Between caller and bean, proxy intercepts calls matching pointcuts; order with `@Order`.

**Q: How does `spring.threads.virtual.enabled=true` work?** Boot 3.2+ auto-configures Tomcat/Jetty/Undertow and `AsyncTaskExecutor` to use `Executors.newVirtualThreadPerTaskExecutor()` / `Thread.ofVirtual().factory()`. On Java 25 this is the recommended default for IO-bound MVC apps, no code change, just the flag. Requires Java 21+.

Q: What are AOT hints? Hints (`RuntimeHintsRegistrar`, `@RegisterReflectionForBinding`) tell GraalVM native-image which reflective accesses, resources, proxies, and serialization to include. Boot's AOT engine generates most automatically; custom hints only for dynamic cases.


<!-- SR -->
Spring Framework vs Spring Boot vs Spring Cloud?:: Framework is the core container; Boot adds auto-configuration, embedded server, starters, and Actuator for rapid apps; Cloud adds distributed-system patterns (config, discovery, gateway). #flashcard
Why does Spring prefer constructor injection?:: Immutability, guaranteed required deps, easier unit testing, avoids circular field-injection pitfalls. #flashcard
JDK dynamic proxy vs CGLIB?:: JDK proxy requires interfaces; CGLIB subclasses the class. Spring picks automatically; use `proxyTargetClass=true` to force CGLIB. On Java 25 with AOT, prefer interfaces for native-image friendliness (needs proxy hint otherwise). #flashcard
How to exclude an auto-configuration in Boot?:: `@SpringBootApplication(exclude = DataSourceAutoConfiguration.class)` or `spring.autoconfigure.exclude` in properties. #flashcard
Where does AOP sit architecturally?:: Between caller and bean, proxy intercepts calls matching pointcuts; order with `@Order`. #flashcard
How does `spring.threads.virtual.enabled=true` work?:: Boot 3.2+ auto-configures Tomcat/Jetty/Undertow and `AsyncTaskExecutor` to use `Executors.newVirtualThreadPerTaskExecutor()` / `Thread.ofVirtual().factory()`. On Java 25 this is the recommended default for IO-bound MVC apps, no code change, just the flag. Requires Java 21+. #flashcard
What are AOT hints?:: Hints (`RuntimeHintsRegistrar`, `@RegisterReflectionForBinding`) tell GraalVM native-image which reflective accesses, resources, proxies, and serialization to include. Boot's AOT engine generates most automatically; custom hints only for dynamic cases. #flashcard

## Pitfalls
- Field injection hides wiring and complicates tests, prefer constructor injection.
- Circular dependencies, constructor cycles fail fast; setter cycles are hidden (break cycles with refactoring or `@Lazy`).
- Self-invocation bypasses AOP proxy, `this.method()` inside same bean skips advice; inject `self` or refactor.
- Forgetting `spring.threads.virtual.enabled=true` on Java 25 IO-bound services → under-utilised platform pool (200 threads) instead of unbounded virtual threads.
- Native image without hints, `ClassNotFound` / `NoSuchMethod` at runtime; run `process-aot` and add `RuntimeHintsRegistrar`.

## Related
- [[Spring Core]] • [[Dependency Injection]] • [[Spring Security]] • [[Spring Transaction]] • [[Threads]]
- [[README|Java MOC]]

---
*Category: Spring • Part of [[README|Java MOC]] • Java 25*
