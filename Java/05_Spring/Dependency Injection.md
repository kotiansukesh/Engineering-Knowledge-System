---
title: "Dependency Injection"
category: Spring
tags: [spring, di, ioc, java25, virtual-threads]
created: 2026-01-18
updated: 2026-09-02
---

# Dependency Injection

> Part of [[README|Java MOC]] • `Spring` • Java 25 / Spring Framework 6.2

## Intent
Dependency Injection (DI) is the Spring implementation of Inversion of Control (IoC): instead of an object constructing its own dependencies (`new X()`), an external entity (the container / an assembler) provides them, so the object depends only on abstractions and remains testable and replaceable.


> I used to think field injection was convenient, then I tried to write a test without Spring. Never again. Constructor injection is the only one that makes your dependencies obvious, use it.

## Definition
DI = "don't call us, we'll call you." A client declares what it needs (via constructor, setter, or field), and a provider (Spring container, factory, test harness) supplies it at creation time. Spring supports constructor, setter, and field injection; constructor injection is the recommended form.

## Architecture, diagram description

```
  Without DI:                    With DI (IoC Container):
  ┌──────────┐  new  ┌────────┐  ┌──────────┐    injects    ┌────────┐
  │ MyApp    │──────▶│EmailSvc│  │ MyApp    │◀──────────────│ Container│
  └──────────┘       └────────┘  └──────────┘   MessageService└────────┘
       tight coupling - hard to test              ▲           ▲
                                              interface   Email/Twitter impl
  Container flow:
  @Configuration / @ComponentScan → BeanDefinitions → BeanFactory
        → resolves @Autowired constructor → instantiates EmailService
        → injects into MyApplication → returns fully wired graph

  Java 25: container can wire virtual-thread executors as beans (see below).
```

Key principle: depend on `MessageService` interface, not `EmailService` concrete class.

## Injection styles, comparison

| Style | Syntax | Required? | Testability | Spring recommendation |
|---|---|---|---|---|
| Constructor | `MyApp(MessageService s){this.s=s;}` + `@Autowired` (optional if single ctor) | Enforced ( `final` ) | Excellent, `new MyApp(mock)` |  Preferred |
| Setter | `@Autowired void setService(MessageService s)` | Optional / reconfigurable | Good | Use for optional deps |
| Field | `@Autowired private MessageService s;` | Hidden | Poor, needs reflection / Spring test |  Avoid |

### Qualifiers & disambiguation

```java title="Java 25"

// Purpose: Dependency Injection: IoC container injects via constructor; depend on interface, not new; testable wiring
// Framework: @Component @Qualifier @Configuration @ComponentScan — Spring manages lifecycle and wiring; no manual new
// Roles: MessageService, EmailService, TwitterService — stereotype defines layer (controller/service/repository)
// Invariant: constructor injection — immutable, required deps; testable without container
```

Other resolution controls: `@Primary` (default bean), `@Profile`, `@ConditionalOnProperty`, `ObjectProvider<T>` for optional/lazy, `@Lazy` for deferred init.

## Virtual threads & DI (Java 25)

DI itself is thread-agnostic, but what you inject changes on Java 25:

```java title="Java 25 - inject virtual-thread executor via DI"

// Purpose: Dependency Injection: IoC container injects via constructor; depend on interface, not new; testable wiring
// Framework: @Configuration @Bean @Component — Spring manages lifecycle and wiring; no manual new
// Roles: ExecutorConfig, NotificationService — stereotype defines layer (controller/service/repository)
// Invariant: constructor injection — immutable, required deps; testable without container
```

> ScopedValue + DI: On Java 25, request-scoped context (correlation ID, tenant) should be a `ScopedValue`, not a `ThreadLocal` bean. Inject a holder or use `ScopedValue.where(...)` in the call site, see [[Threads]] for the `ScopedValue` vs `ThreadLocal` table.

## Service + component example (full)

```java title="Java 25"

// Purpose: Dependency Injection: IoC container injects via constructor; depend on interface, not new; testable wiring
// Framework: @Component @Autowired @Qualifier — Spring manages lifecycle and wiring; no manual new
// Roles: MyApplicationSetter, MyApplicationField, DiDemo — stereotype defines layer (controller/service/repository)
// Invariant: constructor injection — immutable, required deps; testable without container
```

## AOT Note (Java 25 / Boot 3.5)

Constructor injection is AOT-friendly, no reflection needed at runtime. Field injection requires reflection hints (`RuntimeHintsRegistrar`) for native image. Prefer constructor injection for GraalVM compatibility.

```java title="Java 25 - AOT hint for reflective DI (only if field injection remains)"

// Purpose: Dependency Injection: IoC container injects via constructor; depend on interface, not new; testable wiring
// Framework: @RegisterReflectionForBinding @Configuration — Spring manages lifecycle and wiring; no manual new
// Roles: AotConfig — stereotype defines layer (controller/service/repository)
// Invariant: constructor injection — immutable, required deps; testable without container
```

## Pros / cons

| Pros | Cons |
|---|---|
| Loose coupling → swap `Email`/`Twitter`/`Mock` without changing client | Over-injection hides complexity (many ctor args → SRP violation) |
| Easy unit testing (pass fakes) | Misuse (field injection, circular deps) masked until runtime |
| Centralised wiring → consistent scope/lifecycle | Debugging wiring errors (`NoSuchBeanDefinitionException`, `NoUniqueBeanDefinitionException`) |
| Enables AOP/TX/Security proxies transparently | Requires understanding of qualifiers/profiles/conditions |
| Constructor injection is AOT/native-image friendly | Field injection needs extra AOT hints |

## Interview Q&A

Q: IoC vs DI? IoC is the principle ("invert who controls flow/creation"); DI is the concrete pattern implementing IoC by injecting dependencies.

Q: Why is constructor injection preferred? Immutability, fail-fast on missing deps, no reflection in tests, prevents circular field-injection cycles, and is AOT/native-image friendly.

**Q: `@Autowired(required=false)` vs `Optional<T>` vs `ObjectProvider<T>`?** All express optional deps; `ObjectProvider` also gives `getIfAvailable()`, stream, and lazy access.

**Q: How does `@Qualifier` vs `@Primary` work?** `@Primary` marks the default when multiple candidates exist; `@Qualifier("name")` picks a specific one; `@Qualifier` wins over `@Primary`.

Q: Can you DI without Spring? Yes, manual constructor wiring, Dagger/Guice, or service locator; Spring just automates it and adds lifecycle/AOP.

**Q: What does `@Lazy` do?** Defers bean creation until first use; can also break circular deps by injecting a lazy proxy.

Q: How does DI interact with virtual threads (Java 25)? DI is unchanged, but inject `AsyncTaskExecutor` backed by `Executors.newVirtualThreadPerTaskExecutor()` for async work. With `spring.threads.virtual.enabled=true`, Boot auto-configures it. Use `ScopedValue` for context instead of `ThreadLocal`.


<!-- SR -->
IoC vs DI?:: IoC is the principle ("invert who controls flow/creation"); DI is the concrete pattern implementing IoC by injecting dependencies. #flashcard
Why is constructor injection preferred?:: Immutability, fail-fast on missing deps, no reflection in tests, prevents circular field-injection cycles, and is AOT/native-image friendly. #flashcard
`@Autowired(required=false)` vs `Optional<T>` vs `ObjectProvider<T>`?:: All express optional deps; `ObjectProvider` also gives `getIfAvailable()`, stream, and lazy access. #flashcard
How does `@Qualifier` vs `@Primary` work?:: `@Primary` marks the default when multiple candidates exist; `@Qualifier("name")` picks a specific one; `@Qualifier` wins over `@Primary`. #flashcard
Can you DI without Spring?:: Yes, manual constructor wiring, Dagger/Guice, or service locator; Spring just automates it and adds lifecycle/AOP. #flashcard
What does `@Lazy` do?:: Defers bean creation until first use; can also break circular deps by injecting a lazy proxy. #flashcard
How does DI interact with virtual threads (Java 25)?:: DI is unchanged, but inject `AsyncTaskExecutor` backed by `Executors.newVirtualThreadPerTaskExecutor()` for async work. With `spring.threads.virtual.enabled=true`, Boot auto-configures it. Use `ScopedValue` for context instead of `ThreadLocal`. #flashcard

## Pitfalls
- Injecting too many collaborators → extract a façade/service.
- Field injection with `required=true` masking missing beans in tests, also needs AOT reflection hints.
- Using `new` inside a Spring bean for a dependency that should be injected (bypasses proxy/TX).
- `@Component` on abstract classes or with `final` methods that prevent CGLIB proxying.
- Injecting a platform-thread `TaskExecutor` on Java 25 IO-bound services, use virtual-thread executor instead.

## Related
- [[Spring Core]] • [[Spring Framework]] • [[Spring Security]] • [[Spring Transaction]] • [[Threads]]
- [[README|Java MOC]]

---
*Category: Spring • Part of [[README|Java MOC]] • Java 25*
