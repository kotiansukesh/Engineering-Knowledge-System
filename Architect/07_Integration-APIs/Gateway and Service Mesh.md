---
title: "Gateway and Service Mesh"
category: integration
tags: [gateway, service-mesh, istio, rate-limit, interview]
created: 2026-09-03
completed: false
---

# Gateway and Service Mesh

> Part of [[README|07 Integration MOC]] • `integration` • **Edge vs mesh.** Interviews test **what lives in the gateway vs the sidecar**.

## TL;DR for interviews

> **Gateway = north-south** (edge: auth, rate-limit, routing). **Mesh = east-west** (mTLS, retries, canary). Don't push business logic into either.

## Separation

| Concern | Gateway (Spring Cloud Gateway / Kong) | Mesh (Istio / Linkerd) |
|---------|--------------------------------------|------------------------|
| TLS termination, WAF | ✅ | — |
| Auth (JWT verify), rate-limit | ✅ | — |
| Version/canary routing at edge | ✅ | ✅ (finer, per-service) |
| mTLS service-to-service | — | ✅ |
| Retries, timeouts, circuit break | Edge coarse | ✅ per-hop, telemetry-driven |
| Business rules | ❌ never | ❌ never |

```yaml
# Concept: edge route — strip prefix, rate-limit, forward identity downstream
spring:
  cloud:
    gateway:
      routes:
        - id: orders
          uri: lb://orders-service
          predicates: [Path=/api/v1/orders/**]
          filters:
            - StripPrefix=2
            - name: RequestRateLimiter # Concept: 100 rps per API key
              args: { redis-rate-limiter.replenishRate: 100, burstCapacity: 200 }
```

## Quick Check

- [ ] Gateway vs mesh — one-sentence split?
- [ ] Where does JWT verification happen?
- [ ] How do you canary 5% to v2?

## Pitfalls

- Fat gateway with business logic — becomes an untestable monolith at the edge.
- Retries at both gateway AND mesh → retry amplification (cap total attempts).

## Interview Q&A

- **Q: Do we need a mesh on day one?** A: No — gateway + client retries + OTel suffice; add mesh when you need mTLS everywhere and per-hop policy.
- **Q: Rate-limit where?** A: Edge per-tenant (gateway + Redis); per-service concurrency limits in mesh/app.

## Related

- [[REST Maturity and Contracts]] • [[Kafka Messaging and Idempotency]] • [[../08_NonFunctional-Ops/Security OAuth2 and JWT|Security OAuth2 and JWT]]
