---
title: "Serverless"
category: "Architecture Styles"
tags: [architecture, serverless, lambda, faas, spring-cloud-function]
created: 2026-09-03
completed: false
---

# Serverless (FaaS + Managed Services)

> **Intent:** Run code as short-lived functions triggered by events, with the platform owning provisioning, scaling, and patching — you pay per invocation and operate (almost) nothing.

## 1. When to Use
- Spiky/rare workloads (webhooks, nightly jobs, image processing) where idle servers waste money.
- Event handlers (S3 upload → thumbnail; queue → notification).
- MVPs needing zero ops.

**When NOT:** sustained high throughput (cheaper on containers), <100 ms latency-sensitive paths with heavy frameworks, long-running connections (websockets), or workloads needing VPC + provisioned DB tuning.

## 2. Spring Example

```java
// Spring Cloud Function — same code runs on Lambda, Cloud Run, or locally
@Bean Function<OrderPlaced, ShipmentLabel> label() {
    return e -> shipping.labelFor(e.orderId());
}
// Cold-start tips: spring-cloud-function + GraalVM native image,
// -Dspring.main.lazy-initialization=true, keep deps lean (no spring-boot-starter-web on Lambda)
```

Rule: keep functions small, stateless, idempotent; push state to managed stores (DynamoDB/S3/queues).

## 3. Pros / Cons
| Pros | Cons |
|---|---|
| Zero server ops, auto-scale to zero | Cold starts (esp. JVM without native image) |
| Pay-per-use economics for spiky loads | Execution limits (timeout, memory, payload) |
| Fast to ship glue/event code | Vendor lock-in on triggers + IAM wiring |
| Managed HA by default | Observability is scattered (many tiny units) |

## 4. Vs
- **Vs Containers/K8s:** containers = steady-state control + cost; serverless = elasticity − control.
- **Vs [[04_Event-Driven-Architecture|EDA]]:** serverless *consumes* events; EDA is the pattern, FaaS one runtime for it.

## 5. Interview Q&A
**Q: How do you tame JVM cold starts on Lambda?**
A: GraalVM native, SnapStart, provisioned concurrency for hot paths, trim starters, lazy init.

**Q: Where does Spring fit in serverless?**
A: Spring Cloud Function for portable function signatures; avoid full Boot web stack per function.

## 6. Pitfalls
- "Lambda pinball": chains of functions calling functions — latency + cost explode; orchestrate with Step Functions instead.
- Hidden VPC + NAT costs dwarfing compute savings.
- No idempotency on retried triggers → double-charges/emails.

## 7. Links
- [[04_Event-Driven-Architecture]] · [[03_Microservices]]

<!-- Concept: serverless = rent elasticity, don't buy servers; best as event glue, worst as a place to host a monolith. -->
