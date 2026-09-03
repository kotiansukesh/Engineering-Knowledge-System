---
title: "Spring Boot"
category: Spring
tags: [spring, boot, interview]
created: 2026-01-18
updated: 2026-09-02
---

# Spring Boot

> Part of [[README|Java MOC]] • `Spring` • Java 25 / Spring Boot 3.5 / Framework 6.2

## Intent
Make production-grade Spring applications trivial to create and run: auto-configuration over manual wiring, starters over dependency hell, externalised configuration (`application.yml`) over XML, and built-in observability (Actuator, Micrometer), with one flag (`spring.threads.virtual.enabled=true`) to run the entire stack on Java 25 virtual threads.


> Boot does a lot for you. Sometimes too much. I like the convention, but when auto-configuration surprises you, check the condition report first, that saves hours.

## Definition
Spring Boot = Spring Framework + opinionated auto-configuration + embedded server (Tomcat/Jetty/Undertow) + Actuator + Micrometer/Metrics + AOT/Native support. A `@SpringBootApplication` triggers `@EnableAutoConfiguration` + `@ComponentScan` + `@Configuration`, classpath scanning registers only matching `@Conditional` beans, and `SpringApplication.run()` boots an embedded container in a single `java -jar`.

## Architecture, diagram description

```
 Developer → @SpringBootApplication
                │
                ├── @EnableAutoConfiguration
                │     └── spring.factories / AutoConfiguration.imports
                │           ├── @ConditionalOnClass(JdbcTemplate.class) → DataSourceAutoConfiguration
                │           ├── @ConditionalOnWebApplication → DispatcherServletAutoConfiguration
                │           ├── @ConditionalOnProperty / @ConditionalOnMissingBean
                │           └── @EnableConfigurationProperties → @ConfigurationProperties beans
                ├── @ComponentScan → @Component / @Service / @Repository / @Controller
                └── @Configuration → @Bean definitions

 Runtime: SpringApplication
    │
    ├── Environment (application.yml → application-{profile}.yml → env vars → CLI args)
    ├── ApplicationContext (AOT-optimised on Java 25 native)
    ├── Embedded Server (Tomcat / Jetty / Undertow) - virtual threads when enabled
    └── Actuator endpoints (/actuator/health, /metrics, /info)
         └── Micrometer → Prometheus / OTLP

 Java 25: spring.threads.virtual.enabled=true
    └── TomcatProtocolHandler.setExecutor(Executors.newVirtualThreadPerTaskExecutor())
        @Async / @Scheduled → virtual-thread TaskExecutor automatically
```

Starters are dependency bundles; auto-configuration is conditional bean registration, together they eliminate boilerplate.

## Starters & Auto-Configuration

| Starter | Brings in | Auto-configures |
|---|---|---|
| `spring-boot-starter-web` | `spring-webmvc`, Tomcat, Jackson, validation | `DispatcherServlet`, `ObjectMapper`, error handling |
| `spring-boot-starter-data-jpa` | Hibernate, HikariCP, Spring Data | `DataSource`, `EntityManagerFactory`, `JpaTransactionManager` |
| `spring-boot-starter-security` | Spring Security filter chain | `SecurityFilterChain`, `PasswordEncoder` |
| `spring-boot-starter-validation` | Hibernate Validator | `LocalValidatorFactoryBean` |
| `spring-boot-starter-actuator` | Micrometer, Actuator | Health, metrics, env, beans endpoints |
| `spring-boot-starter-test` | JUnit 5, Mockito, AssertJ, MockMvc | `SpringBootTest` slice annotations |

### How auto-configuration decides

| Annotation | Condition | Effect |
|---|---|---|
| `@ConditionalOnClass` | Class on classpath | Enable config only if dependency present |
| `@ConditionalOnMissingBean` | No user-defined bean | Back off when user provides custom bean |
| `@ConditionalOnProperty` | `my.feature.enabled=true` | Toggle via `application.yml` |
| `@ConditionalOnWebApplication` | Servlet/reactive env | Web-only beans |
| `@AutoConfigureOrder` | Ordering hint | Controls config application order |

```java title="Java 25 - custom auto-configuration (library author)"

// Purpose: Spring Boot: auto-configuration via @Conditional; starters; actuator; opinionated defaults
// Framework: @AutoConfiguration @ConditionalOnClass @ConditionalOnProperty @EnableConfigurationProperties — Spring manages lifecycle and wiring; no manual new
// Roles: MyServiceAutoConfiguration — stereotype defines layer (controller/service/repository)
// Invariant: constructor injection — immutable, required deps; testable without container
```

Disable selectively:
```java

// Purpose: Spring Boot: auto-configuration via @Conditional; starters; actuator; opinionated defaults
// Framework: @SpringBootApplication — Spring manages lifecycle and wiring; no manual new
// Roles: App — stereotype defines layer (controller/service/repository)
// Invariant: constructor injection — immutable, required deps; testable without container
```
```yaml
spring.autoconfigure.exclude:
  - org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration
```

## Configuration, application.yml & Profiles

| Source (higher wins) | Example |
|---|---|
| CLI args | `--server.port=9090` |
| Env vars | `SPRING_DATASOURCE_URL` |
| `application-{profile}.yml` | `application-prod.yml` |
| `application.yml` | default |
| `@PropertySource` | custom `.properties` |

```yaml title="Java 25 - application.yml (Boot 3.5)"
spring:
  threads:
    virtual:
      enabled: true          # ← Java 25: Tomcat + @Async + scheduling → virtual threads
  application.name: demo-app
  datasource:
    url: jdbc:postgresql://localhost:5432/demo
    username: demo
    password: ${DB_PASSWORD:changeme}
    hikari.maximum-pool-size: 20
  jpa:
    hibernate.ddl-auto: validate
    open-in-view: false
    properties.hibernate.jdbc.batch_size: 25
  jackson.deserialization.fail-on-unknown-properties: false

server:
  port: 8080
  shutdown: graceful         # Boot 3.5 graceful shutdown on virtual threads

management:
  endpoints.web.exposure.include: health,info,metrics,prometheus
  endpoint.health.show-details: when-authorized
  metrics.tags.application: ${spring.application.name}

my:
  service:
    enabled: true
    endpoint: https://api.example.com
    timeout: 5s               # Duration binding (Java 25: supports Duration parsing)

---
spring.config.activate.on-profile: prod
server.port: 8443
my.service.endpoint: https://api.prod.example.com
```

### Type-safe binding with records (Java 25)

```java title="Java 25 - @ConfigurationProperties as record (Boot 3.5)"

// Purpose: Spring Boot: auto-configuration via @Conditional; starters; actuator; opinionated defaults
// Framework: @ConfigurationProperties @ConfigurationPropertiesScan @EnableConfigurationProperties @Service — Spring manages lifecycle and wiring; no manual new
// Roles: MyServiceProperties, Retry, MyService — stereotype defines layer (controller/service/repository)
// Invariant: constructor injection — immutable, required deps; testable without container
```

| Binding | `application.yml` | Java type |
|---|---|---|
| `Duration` | `5s`, `200ms`, `PT10S` | `java.time.Duration` |
| `DataSize` | `10MB`, `256KB` | `org.springframework.util.unit.DataSize` |
| `Period` | `7d` | `java.time.Period` |
| List/Map | `my.list[0]=a` / `my.map.key=val` | `List<String>`, `Map<String,String>` |

## Actuator, observability & virtual threads

| Endpoint | Purpose | Typical use |
|---|---|---|
| `/actuator/health` | Liveness/readiness (`db`, `redis`, `diskSpace`) | K8s probes |
| `/actuator/metrics` | Micrometer metrics (JVM, HTTP, Hikari, custom) | Prometheus scrape |
| `/actuator/info` | Build/git/app info | Deploy verification |
| `/actuator/env` | Resolved properties + origins | Debug config |
| `/actuator/beans` | Bean graph | Wiring issues |
| `/actuator/mappings` | HTTP mappings | Route audit |
| `/actuator/prometheus` | Prometheus exposition | Grafana |

```yaml title="Actuator security - expose selectively"
management:
  endpoints.web.exposure.include: health,info,metrics,prometheus
  endpoint.health.probes.enabled: true   # /actuator/health/liveness, /readiness for K8s
  metrics.distribution.percentiles-histogram.http.server.requests: true
```

### Virtual threads, one flag (Java 25 / Boot 3.5)

```yaml
spring.threads.virtual.enabled: true
```

| Component | Without flag | With `virtual.enabled=true` (Java 25) |
|---|---|---|
| Tomcat | `ThreadPoolExecutor` 200 threads | `Executors.newVirtualThreadPerTaskExecutor()`, unbounded virtual threads |
| Jetty/Undertow | Platform pool | Virtual-thread executor |
| **`@Async`** | Platform `SimpleAsyncTaskExecutor` | Virtual-thread `AsyncTaskExecutor` |
| **`@Scheduled`** | Platform scheduler | Virtual-thread scheduler |
| JDBC blocking | Holds platform thread | Parks virtual thread (JEP 491), cheap |

```java title="Java 25 - proving virtual threads"

// Purpose: Spring Boot: auto-configuration via @Conditional; starters; actuator; opinionated defaults
// Framework: @RestController @GetMapping @Configuration @Bean — Spring manages lifecycle and wiring; no manual new
// Roles: HelloController, AsyncVirtualConfig — stereotype defines layer (controller/service/repository)
// Invariant: stateless singleton controller; delegates to service; HTTP semantics via ResponseEntity
```

### AOT & GraalVM (Boot 3.5 / Java 25)

```bash
mvn -Pnative native:compile        # AOT → GraalVM native image
mvn spring-boot:process-aot        # AOT only, then: java -Dspring.aot.enabled=true -jar app.jar
```

```java title="Java 25 - RuntimeHints for native"

// Purpose: Spring Boot: auto-configuration via @Conditional; starters; actuator; opinionated defaults
// Framework: @ImportRuntimeHints @Override @RegisterReflectionForBinding — Spring manages lifecycle and wiring; no manual new
// Roles: AppHints — stereotype defines layer (controller/service/repository)
// Invariant: constructor injection — immutable, required deps; testable without container
```

## Pros / cons

| Pros | Cons |
|---|---|
| Zero XML, fast bootstrap with starters + auto-config | Auto-config magic can hide bean origin, use `/actuator/beans` + `--debug` |
| Embedded server → single `java -jar`, ideal for containers/K8s | Fat jar size / classpath conflicts if starters overlap |
| Externalised config + profiles + `@ConfigurationProperties` records | Property source ordering can surprise, higher wins |
| Actuator + Micrometer → prod-ready observability | Endpoints must be secured, don't expose `env`/`beans` publicly |
| Virtual threads (Java 25) eliminate pool tuning for IO-bound services | Requires Java 21+, driver must not pin carrier (JEP 491 fixes `synchronized`) |
| AOT/native: sub-100ms startup, low memory | Reflection-heavy code needs `RuntimeHints` for native |

## Code example, full boot 3.5 app (Java 25)

```java title="Java 25"

// Purpose: Spring Boot: auto-configuration via @Conditional; starters; actuator; opinionated defaults
// Framework: @SpringBootApplication @ConfigurationPropertiesScan @ConfigurationProperties @Service — Spring manages lifecycle and wiring; no manual new
// Roles: DemoApplication, OrderDto, MyProps — stereotype defines layer (controller/service/repository)
// Invariant: stateless singleton controller; delegates to service; HTTP semantics via ResponseEntity
```

### Slice test (Java 25)

```java title="Java 25"

// Purpose: Spring Boot: auto-configuration via @Conditional; starters; actuator; opinionated defaults
// Framework: @WebMvcTest @Autowired @Test — Spring manages lifecycle and wiring; no manual new
// Roles: OrderControllerTest — stereotype defines layer (controller/service/repository)
// Invariant: constructor injection — immutable, required deps; testable without container
```

## Interview Q&A

**Q: What does `@SpringBootApplication` compose?** `@SpringBootConfiguration` + `@EnableAutoConfiguration` + `@ComponentScan`. It enables auto-config, component scanning, and marks configuration class.

Q: How does auto-configuration work? `AutoConfiguration.imports` lists candidates; each has `@Conditional` guards (`OnClass`, `OnMissingBean`, `OnProperty`). Matching ones register beans; user beans with `@ConditionalOnMissingBean` take precedence.

Q: Starters vs auto-configuration? Starters are dependency descriptors (pom bundles); auto-configuration is conditional bean registration, starters pull jars, auto-config wires them.

**Q: `application.properties` vs `application.yml`?** Same semantics; YAML supports hierarchy, lists, and multi-document (`---` profiles), preferred for Boot.

Q: How does externalised config ordering work? CLI args > env vars > `application-{profile}.yml` > `application.yml` > defaults. Higher wins; `spring.config.import` adds extra sources.

Q: What is Actuator and how to secure it? Production endpoints (`health`, `metrics`, `env`, `beans`). Expose only `health`/`metrics`/`prometheus` publicly; secure `env`/`beans` behind management port or Spring Security (`requestMatchers("/actuator/**").hasRole("ADMIN")`).

**Q: What does `spring.threads.virtual.enabled=true` do?** Boot 3.2+ flag: replaces Tomcat/Jetty/Undertow executors and `@Async`/`@Scheduled` executors with `Executors.newVirtualThreadPerTaskExecutor()`. On Java 25 each request runs on a virtual thread, blocking (`Thread.sleep`, JDBC) parks the virtual thread (JEP 491), no pool tuning needed.

Q: When NOT to use virtual threads? CPU-bound batch, heavy computation, or JNI that pins, keep platform pool for those; virtual threads shine for IO-bound MVC/JDBC/RestClient.

Q: How to build a GraalVM native image? `mvn -Pnative native:compile` runs AOT (`process-aot`) generating `reflect-config.json`/`resource-config.json`; custom reflection needs `RuntimeHintsRegistrar` or `@RegisterReflectionForBinding`.


<!-- SR -->
What does `@SpringBootApplication` compose?:: `@SpringBootConfiguration` + `@EnableAutoConfiguration` + `@ComponentScan`. It enables auto-config, component scanning, and marks configuration class. #flashcard
How does auto-configuration work?:: `AutoConfiguration.imports` lists candidates; each has `@Conditional` guards (`OnClass`, `OnMissingBean`, `OnProperty`). Matching ones register beans; user beans with `@ConditionalOnMissingBean` take precedence. #flashcard
Starters vs auto-configuration?:: Starters are dependency descriptors (pom bundles); auto-configuration is conditional bean registration, starters pull jars, auto-config wires them. #flashcard
`application.properties` vs `application.yml`?:: Same semantics; YAML supports hierarchy, lists, and multi-document (`---` profiles), preferred for Boot. #flashcard
How does externalised config ordering work?:: CLI args > env vars > `application-{profile}.yml` > `application.yml` > defaults. Higher wins; `spring.config.import` adds extra sources. #flashcard
What is Actuator and how to secure it?:: Production endpoints (`health`, `metrics`, `env`, `beans`). Expose only `health`/`metrics`/`prometheus` publicly; secure `env`/`beans` behind management port or Spring Security (`requestMatchers("/actuator/**").hasRole("ADMIN")`). #flashcard
What does `spring.threads.virtual.enabled=true` do?:: Boot 3.2+ flag: replaces Tomcat/Jetty/Undertow executors and `@Async`/`@Scheduled` executors with `Executors.newVirtualThreadPerTaskExecutor()`. On Java 25 each request runs on a virtual thread, blocking (`Thread.sleep`, JDBC) parks the virtual thread (JEP 491), no pool tuning needed. #flashcard
When NOT to use virtual threads?:: CPU-bound batch, heavy computation, or JNI that pins, keep platform pool for those; virtual threads shine for IO-bound MVC/JDBC/RestClient. #flashcard
How to build a GraalVM native image?:: `mvn -Pnative native:compile` runs AOT (`process-aot`) generating `reflect-config.json`/`resource-config.json`; custom reflection needs `RuntimeHintsRegistrar` or `@RegisterReflectionForBinding`. #flashcard

## Pitfalls

- Excluding needed auto-config (`exclude = DataSourceAutoConfiguration.class`) then wondering why `DataSource` is missing, check `--debug` condition report.
- Putting `application.yml` in wrong location, Boot searches `classpath:`, `classpath:config/`, `file:./`, `file:./config/`; use `spring.config.import` for custom paths.
- Using `InheritableThreadLocal` for context with virtual threads, doesn't propagate to `StructuredTaskScope`; use `ScopedValue` or `TaskDecorator` / `ContextPropagation`.
- Exposing all Actuator endpoints publicly (`exposure.include=*`), leaks `env` secrets and bean graph.
- Defining `TaskExecutor` bean without virtual threads on Java 25 IO service, set `spring.threads.virtual.enabled=true` instead of custom pool sizing.
- Native image without hints, `NoSuchMethodException` at runtime; run `process-aot` and add `RuntimeHintsRegistrar`.
- Fat-jar classpath conflicts from overlapping starters, use `mvn dependency:tree` and `<exclusions>`.

## Related

- [[Spring Framework]] • [[Spring Core]] • [[Dependency Injection]] • [[Spring MVC]] • [[Spring Data JPA]] • [[Spring Security]] • [[Spring Transaction]] • [[Threads]]
- [[README|Java MOC]]

---
*Category: Spring • Part of [[README|Java MOC]] • Java 25*
