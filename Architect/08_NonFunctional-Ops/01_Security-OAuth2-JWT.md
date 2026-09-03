---
title: "Security — OAuth2, OIDC & JWT"
category: "Non-Functional & Ops"
tags: [security, oauth2, oidc, jwt, spring-security]
created: 2026-09-03
completed: false
---

# Security — OAuth2, OIDC & JWT

> **Intent:** Authenticate once at an IdP, authorize everywhere downstream with short-lived signed tokens; never roll your own auth.

## 1. When to Use
- SPAs/mobile calling Spring resource servers.
- Service-to-service via client-credentials + mTLS.
- Any multi-tenant SaaS needing SSO.

**When NOT:** Public clients storing long-lived secrets; opaque sessions at web scale without a session store; putting PII/permissions blobs in JWT claims.

## 2. Example (Spring Boot 3.5 + K8s)

```java
// Resource server: validate JWT, enforce scopes
@Bean SecurityFilterChain api(HttpSecurity h) throws Exception {
    return h.authorizeHttpRequests(a -> a
            .requestMatchers("/public/**").permitAll()
            .requestMatchers("/admin/**").hasAuthority("SCOPE_admin")
            .anyRequest().authenticated())
        .oauth2ResourceServer(o -> o.jwt(Customizer.withDefaults()))
        .sessionManagement(s -> s.sessionCreationPolicy(STATELESS))
        .build(); // short TTL (5-15m) + refresh rotation
```

## 3. Pros / Cons
| Pros | Cons |
|---|---|
| Stateless scale; single SSO | Token revocation is hard (need denylist/short TTL) |
| Delegated login (Google/Entra/Keycloak) | Claim bloat → header size; key rotation ops |
| Scopes = coarse authz standard | Fine-grained authz still needs local policy (OPA/Cedar) |

## 4. Vs
- **Vs session cookie:** sessions revoke instantly but need sticky/shared store; JWT scales statelessly but revocation lags.
- **Vs mTLS-only:** mTLS proves identity, OAuth adds delegated scopes + user consent.

## 5. Interview Q&A
**Q: Where do you store tokens in a SPA?**
A: Access token in memory, refresh in HttpOnly Secure SameSite cookie (BFF pattern); never localStorage (XSS theft).

**Q: How do you handle revocation?**
A: Short TTL + refresh rotation + denylist (Redis) checked at gateway; critical ops re-check IdP/introspection.

**Q: JWT vs opaque?**
A: JWT for edge scale (verify locally via JWKS); opaque at gateway when instant revoke/audit matters.

## 6. Pitfalls
- Accepting `none` alg or skipping `iss`/`aud` validation.
- Long-lived access tokens (hours/days).
- Trusting client-supplied roles without server mapping.

## 7. Links
- [[05_Cloud-K8s-Deploy-Helm|K8s Deploy]] · [[05_Compliance-Audit]] · [[04_API-Gateway-BFF]]
