---
title: "Spring Security"
category: Spring
tags: [spring, security, authentication, authorization, oauth2, java25, virtual-threads]
created: 2026-01-18
updated: 2026-09-02
---

# Spring Security

> Part of [[README|Java MOC]] • `Spring` • Java 25 / Spring Security 6.5 / Boot 3.5
I keep coming back to this when debugging concurrency.


## Intent
Provide authentication (who you are), authorization (what you can do), and protection (CSRF, session, headers, password encoding) as a declarative, filter-chain layer on top of Spring MVC / WebFlux, so that business endpoints stay focused on business logic.


> Security config is confusing at first. Filters, chains, context, it clicks once you trace a request through the chain once. And please stop putting SecurityContext in ThreadLocal on virtual threads, use the new context propagation instead.

## Definition
Spring Security is a filter-chain framework (`SecurityFilterChain`) that intercepts every HTTP request, builds an `Authentication` object, delegates to an `AuthenticationManager` / `AuthenticationProvider` chain (backed by `UserDetailsService`), establishes a `SecurityContext`, and enforces access rules (`authorizeHttpRequests`, `@PreAuthorize`) before the request reaches controllers.

## Architecture, diagram description

```
  HTTP Request (on virtual thread when spring.threads.virtual.enabled=true)
      │
      ▼
  DelegatingFilterProxy (web.xml / Boot auto-config)
      │
      ▼
  FilterChainProxy → ordered SecurityFilterChain
      │  e.g. SecurityContextPersistenceFilter
      │       UsernamePasswordAuthenticationFilter (extracts username/password)
      │       BasicAuthenticationFilter / BearerTokenAuthenticationFilter
      │       CsrfFilter, CorsFilter, ExceptionTranslationFilter
      │       AuthorizationFilter (formerly FilterSecurityInterceptor)
      ▼
  Authentication Object (principal, credentials, authorities)
      │  filter → AuthenticationManager.authenticate(auth)
      ▼
  ProviderManager → iterates AuthenticationProviders
      │  DaoAuthenticationProvider ──▶ UserDetailsService ──▶ DB / LDAP / OIDC
      │  JwtAuthenticationProvider ──▶ JwtDecoder
      │  LdapAuthenticationProvider ...
      ▼
  On success: SecurityContextHolder.getContext().setAuthentication(auth)
      │  (ThreadLocal on platform threads; propagated via DelegatingSecurityContext* on virtual threads)
      ▼
  Controller / Resource Server (SecurityContext available via @AuthenticationPrincipal)

  OAuth2 / OIDC extension:
  Client → Authorization Server (Cognito / Azure AD / Okta / Keycloak)
         → obtains access_token / id_token (JWT)
         → Resource Server validates JWT via JwtDecoder
```

Additional diagram: ![[Pasted image 20211019220915.png]]

### Core security chain elements
| Component | Role |
|---|---|
| `DelegatingFilterProxy` | Bridges servlet container filter to Spring `FilterChainProxy` |
| `SecurityFilterChain` | Ordered list of `Filter`s for matched request patterns |
| `Authentication` | Token holding `principal`/`credentials`/`authorities`; `authenticated` flag |
| `AuthenticationManager` / `ProviderManager` | Entry point; delegates to providers |
| `AuthenticationProvider` | Knows how to authenticate one type (DAO, JWT, LDAP) |
| `UserDetailsService` | Loads `UserDetails` from persistence; throws `UsernameNotFoundException` if absent |
| `SecurityContext` / `SecurityContextHolder` | Holds current `Authentication`, see virtual-thread notes below |
| `PasswordEncoder` | Hash & verify passwords (`BCryptPasswordEncoder`, `Argon2`) |

## Virtual threads & securitycontext (Java 25)

> Enable virtual threads: `spring.threads.virtual.enabled=true` (Boot 3.2+/3.5, Java 25). Each HTTP request then runs on a virtual thread, `SecurityContext` propagation must be virtual-thread-aware.

### The problem with `ThreadLocal` on virtual threads

`SecurityContextHolder` defaults to `MODE_THREADLOCAL`. With platform threads (pool of ~200), this is fine. With virtual threads (millions, short-lived), `ThreadLocal` is expensive and `InheritableThreadLocal` does not propagate into `StructuredTaskScope` or `newVirtualThreadPerTaskExecutor()` children.

### Java 25 / Spring Security 6.5 solution

| Concern | Platform threads (legacy) | Virtual threads (Java 25) |
|---|---|---|
| `SecurityContextHolder` strategy | `MODE_THREADLOCAL` | `MODE_THREADLOCAL` still works per-request (each virtual thread has its own `ThreadLocal`), but cross-thread propagation needs help |
| Propagating context to child tasks | `DelegatingSecurityContextRunnable` / `DelegatingSecurityContextExecutor` | Same wrappers still work, plus `ScopedValue` support (Spring Security 6.4+ can store context in `ScopedValue` when available) |
| `@Async` with security | `@EnableAsync` + `DelegatingSecurityContextAsyncTaskExecutor` | Virtual-thread executor + `DelegatingSecurityContextExecutor` or `ContextPropagation` |
| Reactive | `ReactiveSecurityContextHolder` / Reactor `Context` | Unchanged |

```java title="Java 25 - SecurityConfig with virtual threads"

// Purpose: Spring Security: filter chain; authentication → authorization; SecurityContext per request
// Framework: @Configuration @EnableWebSecurity @EnableMethodSecurity @Bean — Spring manages lifecycle and wiring; no manual new
// Roles: SecurityConfig — stereotype defines layer (controller/service/repository)
// Invariant: constructor injection — immutable, required deps; testable without container
```

```java title="Java 25 - manual propagation with virtual threads"

// Purpose: Spring Security: filter chain; authentication → authorization; SecurityContext per request
// Roles: VirtualSecurityDemo — stereotype defines layer (controller/service/repository)
// Invariant: constructor injection — immutable, required deps; testable without container
```

Key rules for Java 25:
- `SecurityContextHolder.MODE_INHERITABLETHREADLOCAL` is not sufficient for virtual-thread executors or `StructuredTaskScope`, always wrap with `DelegatingSecurityContext*`.
- Spring Security 6.4+ supports `ScopedValue`-backed `SecurityContext` (transparent when `ScopedValue` is used), prefer it for new code; falls back to `ThreadLocal` otherwise.
- `spring.threads.virtual.enabled=true` does not change the `SecurityContextHolder` strategy automatically, add the `DelegatingSecurityContextAsyncTaskExecutor` bean if you use `@Async` with security.

### JWT resource server (`application.yml`), Java 25
```yaml title="Java 25 - application.yml"
spring:
  threads:
    virtual:
      enabled: true
  security:
    oauth2:
      resourceserver:
        jwt:
          issuer-uri: https://cognito-idp.eu-west-1.amazonaws.com/eu-west-1_xxx
```

## AOT Hints for Security (Java 25 / GraalVM)

```java title="Java 25 - AOT hints for Security"

// Purpose: Spring Security: filter chain; authentication → authorization; SecurityContext per request
// Framework: @ImportRuntimeHints @Configuration @Override — Spring manages lifecycle and wiring; no manual new
// Roles: SecurityHints — stereotype defines layer (controller/service/repository)
// Invariant: constructor injection — immutable, required deps; testable without container
```
- Most Spring Security filters / providers are auto-registered by Boot's AOT engine. Add hints only for custom `UserDetails`, `GrantedAuthority` impls, or custom `JwtDecoder`.

## OAuth2.0 & OIDC, Terminology

| Term | Meaning |
|---|---|
| Resource Owner | End user owning the protected resource |
| Resource Server | Hosts/protects the resource (your Spring API) |
| Client | App requesting access on behalf of owner |
| Authorization Server | Issues & validates tokens (AWS Cognito, Azure AD, Okta, Keycloak, Spring Authorization Server) |
| Access Token | Short-lived bearer token for API calls |
| ID Token (OIDC) | JWT with identity claims (OIDC layer atop OAuth2) |
| Public / Confidential Client | Public = browser/mobile (cannot keep secret); Confidential = backend/Cron that can |

OIDC = identity layer on OAuth2; provides `id_token`, `userinfo`, standard scopes (`openid profile email`).

## Pros / cons

| Pros | Cons |
|---|---|
| Comprehensive: authN, authZ, OAuth2/OIDC, CSRF, headers, session | Configuration surface is large, defaults matter |
| Declarative (`@PreAuthorize`, `hasRole`) + DSL (`HttpSecurity`) | Filter ordering/debugging non-trivial |
| Pluggable `AuthenticationProvider`, `UserDetailsService` | JWT/session mix or multiple chains easy to misconfigure |
| Battle-tested, integrates with Boot Actuator / Micrometer | Password-encoder migration & legacy `WebSecurityConfigurerAdapter` migration |
| Virtual-thread-aware context propagation (6.4+/Java 25) | Must wrap executors with `DelegatingSecurityContext*` for virtual threads |

## Interview Q&A

Q: Authentication vs Authorization? Authentication verifies identity (who you are); Authorization checks permissions (what you may access) after authentication.

**Q: What is `DelegatingFilterProxy`?** A servlet filter that delegates to Spring's `FilterChainProxy`, allowing security filters to be Spring beans.

Q: How does JWT resource-server validation work? `BearerTokenAuthenticationFilter` extracts `Authorization: Bearer *** `JwtDecoder` verifies signature/expiry/issuer, maps claims to `GrantedAuthority`, sets `SecurityContext`.

**Q: Where is `SecurityContext` stored for reactive apps?** Not `ThreadLocal`, it's in `ReactiveSecurityContextHolder` / Reactor `Context`.

Q: CSRF, when to disable? Safe to disable for stateless JWT APIs (no cookie session); keep enabled for browser form-login apps.

Q: How to test secured endpoints? `@WebMvcTest` + `@WithMockUser`, `@WithUserDetails`, or `SecurityMockMvcRequestPostProcessors.jwt()`.

Q: How does SecurityContext work with virtual threads (Java 25)? Each virtual thread has its own `ThreadLocal`, so per-request isolation still works. For child virtual threads / `StructuredTaskScope` / `@Async`, wrap with `DelegatingSecurityContextRunnable` / `DelegatingSecurityContextAsyncTaskExecutor`. Spring Security 6.4+ also supports `ScopedValue`-backed context. `MODE_INHERITABLETHREADLOCAL` alone is insufficient for virtual executors.

**Q: Does `spring.threads.virtual.enabled=true` affect Security?** It moves the web layer to virtual threads. Add a `DelegatingSecurityContextAsyncTaskExecutor` backed by `Executors.newVirtualThreadPerTaskExecutor()` for async security propagation.


<!-- SR -->
Authentication vs Authorization?:: Authentication verifies identity (who you are); Authorization checks permissions (what you may access) after authentication. #flashcard
What is `DelegatingFilterProxy`?:: A servlet filter that delegates to Spring's `FilterChainProxy`, allowing security filters to be Spring beans. #flashcard
How does JWT resource-server validation work?:: `BearerTokenAuthenticationFilter` extracts `Authorization: Bearer *** `JwtDecoder` verifies signature/expiry/issuer, maps claims to `GrantedAuthority`, sets `SecurityContext`. #flashcard
Where is `SecurityContext` stored for reactive apps?:: Not `ThreadLocal`, it's in `ReactiveSecurityContextHolder` / Reactor `Context`. #flashcard
CSRF, when to disable?:: Safe to disable for stateless JWT APIs (no cookie session); keep enabled for browser form-login apps. #flashcard
How to test secured endpoints?:: `@WebMvcTest` + `@WithMockUser`, `@WithUserDetails`, or `SecurityMockMvcRequestPostProcessors.jwt()`. #flashcard
How does SecurityContext work with virtual threads (Java 25)?:: Each virtual thread has its own `ThreadLocal`, so per-request isolation still works. For child virtual threads / `StructuredTaskScope` / `@Async`, wrap with `DelegatingSecurityContextRunnable` / `DelegatingSecurityContextAsyncTaskExecutor`. Spring Security 6.4+ also supports `ScopedValue`-backed context. `MODE_INHERITABLETHREADLOCAL` alone is insufficient for virtual executors. #flashcard
Does `spring.threads.virtual.enabled=true` affect Security?:: It moves the web layer to virtual threads. Add a `DelegatingSecurityContextAsyncTaskExecutor` backed by `Executors.newVirtualThreadPerTaskExecutor()` for async security propagation. #flashcard

## Pitfalls
- Storing passwords without `PasswordEncoder` or using weak hashes (MD5/SHA-1).
- Exposing `SecurityContext` across threads without `DelegatingSecurityContextRunnable` / `DelegatingSecurityContextExecutor`, especially with virtual threads where `InheritableThreadLocal` does not propagate.
- `permitAll()` ordering mistakes, more specific matchers must come before `anyRequest()`.
- Mixing stateful sessions with stateless JWT without separating `SecurityFilterChain`s (`@Order` + `securityMatcher`).
- Not rotating JWT keys / ignoring `exp`/`aud` validation.
- Forgetting AOT hints for custom `UserDetails` / `JwtDecoder` in native image.

## Related
- [[Spring Framework]] • [[Spring Core]] • [[Dependency Injection]] • [[Spring Transaction]] • [[Threads]]
- [[README|Java MOC]]

---
*Category: Spring • Part of [[README|Java MOC]] • Java 25*
