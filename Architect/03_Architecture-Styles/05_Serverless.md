---
title: "Serverless"
category: "Architecture Styles"
tags: [architecture, serverless, lambda, faas, spring-cloud-function]
created: 2026-09-03
completed: false
---
## Why it Matters

Serverless converts ops cost into per-invocation cost and makes elasticity someone else's problem. That is a winning trade for spiky, rare or glue workloads, and a losing one for sustained throughput and sub-100ms latency paths, the bill and the cold starts will tell you which side you are on.

## Diagram

```mermaid
graph LR
 E1[S3 upload] --> Fn[label(...)]
 E2[API Gateway /events] --> Fn
 E3[SQS queue] --> Fn
 Fn --> D[(DynamoDB)]
 Fn --> E2b[SNS/EventBridge]
 Fn --> C[(CloudWatch traces)]
 SFN[Step Functions orchestrates] -.calls.-> Fn
```

## Code

```java
// Spring Cloud Function — same code runs on Lambda, Azure Functions, Cloud Run, or locally
@Bean
Function<OrderPlaced, ShipmentLabel> label() {
 return e -> shipping.labelFor(e.orderId()); // pure, stateless, cheap to cold-start
}

// Cold-start hygiene that matters more than the framework choice:
// - no spring-boot-starter-web on a function runtime (it boots a server you never use)
// - -Dspring.main.lazy-initialization=true, trim starters, GraalVM native image
// - keep functions small, stateless, IDEMPOTENT — retried triggers must be safe to re-run
```
```java
// Idempotency is the correctness contract of serverless, not an optimisation:
// every trigger (S3 event, queue message, webhook) is at-least-once delivery.
boolean alreadyHandled = seen.putIfAbsent(e.eventId(), true) != null;
if (alreadyHandled) return Label.skipped(); // dedupe key → no double shipment
```
State goes to managed stores (DynamoDB/S3/queues), never to the function's own memory, a frozen warm instance is not a database.

## When to use / not

- Spiky/rare workloads (webhooks, nightly jobs, image processing) where idle servers waste money.
- Event handlers (S3 upload → thumbnail; queue → notification).
- MVPs needing zero ops.

**When NOT:** sustained high throughput (cheaper on containers), <100 ms latency-sensitive paths with heavy frameworks, long-running connections (websockets), or workloads needing VPC + provisioned DB tuning.

## Trade-offs

| Pros | Cons |
|---|---|
| Zero server ops, auto-scale to zero | Cold starts (esp. JVM without native image) |
| Pay-per-use economics for spiky loads | Execution limits (timeout, memory, payload) |
| Fast to ship glue/event code | Vendor lock-in on triggers + IAM wiring |
| Managed HA by default | Observability is scattered (many tiny units) |

## Vs

- **Vs Containers/K8s:** containers = steady-state control + cost; serverless = elasticity − control.
- **Vs [[04_Event-Driven-Architecture|EDA]]:** serverless *consumes* events; EDA is the pattern, FaaS one runtime for it.

## Pitfalls

- "Lambda pinball": chains of functions calling functions, latency + cost explode; orchestrate with Step Functions instead.
- Hidden VPC + NAT costs dwarfing compute savings.
- No idempotency on retried triggers → double-charges/emails.

## Interview q&a

**Q: How do you tame JVM cold starts on Lambda?**
A: GraalVM native, SnapStart, provisioned concurrency for hot paths, trim starters, lazy init.

**Q: Where does Spring fit in serverless?**
A: Spring Cloud Function for portable function signatures; avoid full Boot web stack per function.

## Related

- [[04_Event-Driven-Architecture]] · [[03_Microservices]]

# Serverless (FaaS + Managed Services)

> **Intent:** Run code as short-lived functions triggered by events, with the platform owning provisioning, scaling, and patching, you pay per invocation and operate (almost) nothing.

## 2. Spring Example
```java
// Spring Cloud Function, same code runs on Lambda, Cloud Run, or locally
@Bean Function<OrderPlaced, ShipmentLabel> label() {
 return e -> shipping.labelFor(e.orderId());
}
// Cold-start tips: spring-cloud-function + GraalVM native image,
// -Dspring.main.lazy-initialization=true, keep deps lean (no spring-boot-starter-web on Lambda)
```
Rule: keep functions small, stateless, idempotent; push state to managed stores (DynamoDB/S3/queues).
