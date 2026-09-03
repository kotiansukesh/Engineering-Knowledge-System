---
title: "Spring MVC"
category: Spring
tags: [spring, mvc, interview]
created: 2026-01-18
updated: 2026-09-02
---

# Spring MVC

> Part of [[README|Java MOC]] • `Spring` • Java 25 / Spring Boot 3.5 / Framework 6.2

## Intent
Expose HTTP endpoints as plain Java methods: map requests → controller methods → responses via annotations (`@RequestMapping`, `@GetMapping`), serialize bodies with Jackson, handle errors centrally (`@ControllerAdvice`), and run each request on a Java 25 virtual thread so blocking handlers scale like reactive without changing code.


> MVC on virtual threads is my default now. One request, one virtual thread, blocking code is fine. I only reach for WebFlux when I need streaming or true backpressure, otherwise it adds complexity you don't need.

## Definition
Spring MVC = Servlet-based web framework (`DispatcherServlet` as front controller) that routes HTTP to `@Controller` / `@RestController` methods, resolves arguments (`@PathVariable`, `@RequestBody`, `@RequestParam`), negotiates content, invokes the handler, and writes the result (view or JSON) via `HttpMessageConverter`. On Boot 3.5 + Java 25 with `spring.threads.virtual.enabled=true`, the embedded Tomcat dispatches each request on a virtual thread.

## Architecture, diagram description

```
 HTTP Request (virtual thread when spring.threads.virtual.enabled=true)
      │
      ▼
  Embedded Tomcat (VirtualThreadPerTaskExecutor)
      │
      ▼
  FilterChain (Security, OncePerRequestFilter, MDC)
      │
      ▼
 DispatcherServlet (Front Controller)
      │
      ├── HandlerMapping  →  finds @RestController method for (method, path)
      ├── HandlerAdapter  →  resolves args (@PathVariable, @Valid @RequestBody, @RequestParam)
      │        │
      │        ▼
      │   @RestController method on virtual thread
      │        │  return OrderDto / ResponseEntity<OrderDto> / void
      │        ▼
      ├── HandlerInterceptor (preHandle / postHandle / afterCompletion)
      ├── @ControllerAdvice / @ExceptionHandler  ← on exception
      └── HttpMessageConverter (MappingJackson2HttpMessageConverter)
               │  OrderDto record → JSON
               ▼
           HTTP Response (status, headers, body)

 Virtual thread note: Thread.sleep / JDBC / RestClient inside controller parks
 the virtual thread (JEP 491) - carrier thread is reused - no async needed.
```

## Core annotations & response handling

### Controller vs restcontroller

| Annotation | Semantics | When to use |
|---|---|---|
| `@Controller` | Returns view name (Thymeleaf/JSP) or `@ResponseBody` per method | MVC with server-rendered views |
| `@RestController` | `@Controller` + `@ResponseBody` on every method → JSON/XML | REST APIs (preferred) |
| `@RequestMapping` | Class or method level, any HTTP method | Base path / legacy |
| `@GetMapping` / `@PostMapping` / etc. | Shortcut for method + path | Idiomatic REST |

### Argument & return resolution

| Annotation | Binds from | Example |
|---|---|---|
| `@PathVariable` | URI segment `/orders/{id}` | `getById(@PathVariable Long id)` |
| `@RequestParam` | Query `?page=0&size=20` | `list(@RequestParam(defaultValue="0") int page)` |
| `@RequestBody` | JSON body → record/DTO | `create(@Valid @RequestBody CreateOrderRequest req)` |
| `@RequestHeader` | Header | `@RequestHeader("X-Request-Id") String rid` |
| `@CookieValue` | Cookie | `@CookieValue String session` |
| `@ModelAttribute` | Form / query → object | HTML form binding |
| `HttpServletRequest` | Raw servlet | Rare, low-level access |

### ResponseEntity, full HTTP control

| Factory | Status | Use |
|---|---|---|
| `ResponseEntity.ok(body)` | 200 | Success |
| `ResponseEntity.created(location).body(b)` | 201 + `Location` | POST create |
| `ResponseEntity.noContent().build()` | 204 | DELETE / void update |
| `ResponseEntity.status(202).body(b)` | 202 | Accepted / async |
| `ResponseEntity.notFound().build()` | 404 | Missing resource |

```java title="Java 25 - @RestController with records + ResponseEntity"

// Purpose: Spring MVC: DispatcherServlet → HandlerMapping → Controller → Service → Repository; JSON via HttpMessageConverter
// Framework: @RestController @RequestMapping @NotBlank @NotNull — Spring manages lifecycle and wiring; no manual new
// Roles: OrderController, CreateOrderRequest, OrderDto — stereotype defines layer (controller/service/repository)
// Invariant: stateless singleton controller; delegates to service; HTTP semantics via ResponseEntity
```

### Validation (Jakarta Validation on records)

```java title="Java 25 - record validation"

// Purpose: Spring MVC: DispatcherServlet → HandlerMapping → Controller → Service → Repository; JSON via HttpMessageConverter
// Framework: @NotBlank @Email @NotNull @DecimalMin — Spring manages lifecycle and wiring; no manual new
// Roles: CreateOrderRequest — stereotype defines layer (controller/service/repository)
// Invariant: constructor injection — immutable, required deps; testable without container
```

### Vs tables, MVC on virtual threads vs WebFlux

| Aspect | Spring MVC + virtual threads (Java 25) | Spring WebFlux (reactive) |
|---|---|---|
| Concurrency | One virtual thread per request, blocking is cheap (park) | Event loop + `Mono`/`Flux`, non-blocking |
| Code style | Imperative, `return dto;` / `Thread.sleep` ok | Reactive, `return Mono<Dto>` |
| JDBC/JPA | Direct (Hibernate blocks virtual thread) | Needs R2DBC for non-blocking |
| When to use | Default for IO-bound REST on Java 25 | Streaming, SSE, high-fan-out with backpressure |

| `@Controller` vs `@RestController` | Detail |
|---|---|
| `@Controller` | View resolver; need `@ResponseBody` per method for JSON |
| `@RestController` | Implicit `@ResponseBody`, every return is body |

## Exception handling, @controlleradvice

Three layers, most specific wins:

| Mechanism | Scope | Typical use |
|---|---|---|
| `@ExceptionHandler` inside controller | One controller | Controller-local fallback |
| `@ControllerAdvice` / `@RestControllerAdvice` | Global, all controllers | Centralised API error envelope |
| `ResponseStatusException` / `ErrorController` | Global | Quick `throw new ResponseStatusException(404)` |

```java title="Java 25 - Global exception handling (records for error body)"

// Purpose: Spring MVC: DispatcherServlet → HandlerMapping → Controller → Service → Repository; JSON via HttpMessageConverter
// Framework: @RestControllerAdvice @ExceptionHandler @Valid @ResponseStatus — Spring manages lifecycle and wiring; no manual new
// Roles: GlobalExceptionHandler, public, ApiError — stereotype defines layer (controller/service/repository)
// Invariant: stateless singleton controller; delegates to service; HTTP semantics via ResponseEntity
```

### Validation + ProblemDetail (RFC 9457, Boot 3.5)

```java title="Java 25 - ProblemDetail (Spring 6.2+)"

// Purpose: Spring MVC: DispatcherServlet → HandlerMapping → Controller → Service → Repository; JSON via HttpMessageConverter
// Framework: @RestControllerAdvice @ExceptionHandler — Spring manages lifecycle and wiring; no manual new
// Roles: ProblemAdvice — stereotype defines layer (controller/service/repository)
// Invariant: stateless singleton controller; delegates to service; HTTP semantics via ResponseEntity
```

### Interceptors vs filters vs advice

| Layer | Interface | Runs | Use |
|---|---|---|---|
| Filter | `jakarta.servlet.Filter` / `OncePerRequestFilter` | Before `DispatcherServlet` | Auth, logging, MDC, virtual-thread context |
| Interceptor | `HandlerInterceptor` | Around handler (pre/post) | Metrics, locale, header enrichment |
| Advice | `@ControllerAdvice` | On exception / `@InitBinder` | Error envelope, binder customisation |

## Virtual threads in MVC (Java 25)

```yaml title="Enable - application.yml"
spring.threads.virtual.enabled: true
```

| Without flag | With flag (Java 25) |
|---|---|
| Tomcat pool 200 platform threads | `newVirtualThreadPerTaskExecutor()`, unbounded virtual threads |
| `Thread.sleep` / JDBC blocks platform thread | Parks virtual thread (JEP 491, `synchronized` no longer pins) |
| Need `DeferredResult` / `Callable` for concurrency | Plain blocking controller scales to 10k+ concurrent |

```java title="Java 25 - blocking is now optimal in MVC"

// Purpose: Spring MVC: DispatcherServlet → HandlerMapping → Controller → Service → Repository; JSON via HttpMessageConverter
// Framework: @GetMapping @PathVariable @Async — Spring manages lifecycle and wiring; no manual new
// Invariant: constructor injection — immutable, required deps; testable without container
```

> Pinning note (JEP 491, Java 25): `synchronized` no longer pins virtual threads to carriers. Native frames still pin, avoid `synchronized(nativeCall)`.

## Pros / cons

| Pros | Cons |
|---|---|
| Simple imperative model, records as DTOs, `ResponseEntity` for HTTP semantics | Blocking handlers still hold DB locks, keep transactions short |
| `@ControllerAdvice` gives single error envelope for the whole API | Self-invocation or filter ordering bugs can bypass advice |
| Validation (`@Valid` on records) → automatic 400 without boilerplate | Multiple `@ControllerAdvice` ordering needs `@Order` |
| Virtual threads (Java 25) make blocking MVC as scalable as WebFlux | WebFlux still preferred for backpressure / SSE / streaming |
| Full filter/interceptor chain for cross-cutting concerns | Over-filtering adds latency, measure with Actuator metrics |

## Code example, full slice (Java 25)

```java title="Java 25"

// Purpose: Spring MVC: DispatcherServlet → HandlerMapping → Controller → Service → Repository; JSON via HttpMessageConverter
// Framework: @SpringBootApplication @NotBlank @NotNull @Positive — Spring manages lifecycle and wiring; no manual new
// Roles: MvcApplication, CreateOrderRequest, OrderDto — stereotype defines layer (controller/service/repository)
// Invariant: stateless singleton controller; delegates to service; HTTP semantics via ResponseEntity
```

## Interview Q&A

**Q: `DispatcherServlet` flow?** `FilterChain` → `DispatcherServlet` → `HandlerMapping` finds controller → `HandlerAdapter` resolves args → invoke method (on virtual thread) → `HttpMessageConverter` writes body → interceptors post-process. Exceptions bubble to `@ControllerAdvice`.

**Q: `@Controller` vs `@RestController`?** `@RestController = @Controller + @ResponseBody`, every method returns body (JSON). `@Controller` returns view names unless annotated with `@ResponseBody`.

**Q: Why `ResponseEntity`?** Full HTTP control: status, headers (`Location`, `ETag`), body. `ResponseEntity.created(location).body(dto)` for 201; `noContent()` for 204.

**Q: How does `@ControllerAdvice` work?** A bean with `@ExceptionHandler` methods that applies globally. Most specific handler wins; use `@Order` if multiple advices. For RFC 9457 use `ProblemDetail`.

Q: Validation with records? Put Jakarta annotations on record components (`record Req(@NotBlank String name){}`), annotate controller param with `@Valid`, handle `MethodArgumentNotValidException` in advice → 400 with field map.

Q: Filters vs Interceptors vs Advice? Filters (servlet, before dispatch), Interceptors (around handler inside dispatch), Advice (exception/result handling). Auth/MDC → filter; metrics/header → interceptor; errors → advice.

Q: How do virtual threads change MVC? With `spring.threads.virtual.enabled=true` (Boot 3.5, Java 25) each request is a virtual thread. Blocking `RestClient`/JDBC/`Thread.sleep` parks the virtual thread (JEP 491), no `DeferredResult` needed. Throughput jumps from ~200 to 10k+ concurrent with no code change.

Q: When to choose WebFlux over MVC + virtual threads? Streaming/SSE, backpressure, or gateway aggregation needing non-blocking composition. For typical CRUD + blocking JDBC, MVC + virtual threads is simpler and equally scalable on Java 25.


<!-- SR -->
`DispatcherServlet` flow?:: `FilterChain` → `DispatcherServlet` → `HandlerMapping` finds controller → `HandlerAdapter` resolves args → invoke method (on virtual thread) → `HttpMessageConverter` writes body → interceptors post-process. Exceptions bubble to `@ControllerAdvice`. #flashcard
`@Controller` vs `@RestController`?:: `@RestController = @Controller + @ResponseBody`, every method returns body (JSON). `@Controller` returns view names unless annotated with `@ResponseBody`. #flashcard
Why `ResponseEntity`?:: Full HTTP control: status, headers (`Location`, `ETag`), body. `ResponseEntity.created(location).body(dto)` for 201; `noContent()` for 204. #flashcard
How does `@ControllerAdvice` work?:: A bean with `@ExceptionHandler` methods that applies globally. Most specific handler wins; use `@Order` if multiple advices. For RFC 9457 use `ProblemDetail`. #flashcard
Validation with records?:: Put Jakarta annotations on record components (`record Req(@NotBlank String name){}`), annotate controller param with `@Valid`, handle `MethodArgumentNotValidException` in advice → 400 with field map. #flashcard
Filters vs Interceptors vs Advice?:: Filters (servlet, before dispatch), Interceptors (around handler inside dispatch), Advice (exception/result handling). Auth/MDC → filter; metrics/header → interceptor; errors → advice. #flashcard
How do virtual threads change MVC?:: With `spring.threads.virtual.enabled=true` (Boot 3.5, Java 25) each request is a virtual thread. Blocking `RestClient`/JDBC/`Thread.sleep` parks the virtual thread (JEP 491), no `DeferredResult` needed. Throughput jumps from ~200 to 10k+ concurrent with no code change. #flashcard
When to choose WebFlux over MVC + virtual threads?:: Streaming/SSE, backpressure, or gateway aggregation needing non-blocking composition. For typical CRUD + blocking JDBC, MVC + virtual threads is simpler and equally scalable on Java 25. #flashcard

## Pitfalls

- Returning `null` from `@RestController` → 200 with empty body, not 404, throw `NotFoundException` or return `ResponseEntity.notFound()`.
- Forgetting `@Valid` on `@RequestBody` record, validation silently skipped; always add `@Valid`.
- Multiple `@ControllerAdvice` without `@Order`, unpredictable handler precedence.
- Using field injection in controllers, prefer constructor injection (AOT-friendly, testable).
- `synchronized` + native call inside controller, still pins virtual thread (native frame); isolate native calls.
- Swallowing exceptions in controller and returning 200, breaks advice and clients; let exceptions propagate to advice.
- Not setting `spring.threads.virtual.enabled=true` on Java 25 IO-bound service, stays on 200-thread platform pool.

## Related

- [[Spring Boot]] • [[Spring Framework]] • [[Spring Core]] • [[Spring Data JPA]] • [[Spring Security]] • [[Threads]]
- [[README|Java MOC]]

---
*Category: Spring • Part of [[README|Java MOC]] • Java 25*
