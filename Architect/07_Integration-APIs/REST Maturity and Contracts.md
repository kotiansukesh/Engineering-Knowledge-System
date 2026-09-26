---
title: REST Maturity and Contracts
category: 'integration tags: [rest, openapi, contracts, versioning, interview] created:
  2026-09-03 completed: false'
reviewed: ''
sr-due: ''
difficulty: Easy
excalidraw: ''
tags: []
created: '2026-09-27'
completed: false
source: ''
type: note
weeks: ''
---

## Why it Matters

An API is a compiled dependency of someone else's code, which makes evolution the actual hard part, not the verbs. Contract-first with OpenAPI, additive-only change and consumer-driven tests in CI is what lets a public API add features for years without breaking clients, and idempotency keys are what make retry-safe `POST` possible at all.

## Diagram

```mermaid
graph LR
 OAS[openapi.yaml: source of truth] --> GEN[generated OrderApi interface]
 GEN --> IMPL["thin @RestController impl"]
 OAS --> DOC[docs + client SDKs]
 OAS --> PACT[consumer contract tests in CI]
 CL[client] -.breaks build on incompatible change.-> PACT
```

## Code

```java
// Contract-first: implement the generated interface, not a freehand controller
@RestController
public class OrderController implements OrderApi {
 @Override
 public ResponseEntity<OrderDto> getOrder(UUID id) {
 return ResponseEntity.ok(service.find(id)); // 404 via exception handler
 }
}

// POST made retry-safe: idempotency key, server-side dedupe
@PostMapping("/payments")
public ResponseEntity<PaymentDto> pay(@RequestBody PaymentReq req,
 @RequestHeader("Idempotency-Key") String key) {
 return payments.pay(req, key) // unique index on (paymentId, key)
 .map(ResponseEntity::ok)
 .orElse(ResponseEntity.accepted().build()); // in-flight duplicate
}
```

## When to use / not

**Use when:**
- Public or partner-facing APIs, browsers, mobile, third parties all speak HTTP/JSON.
- Evolution over years matters: additive-only change inside a versioned path.
- Semantic caching, proxyability and tooling (OpenAPI, curl) are worth more than wire efficiency.

**When NOT:**
- Internal high-throughput or streaming calls, gRPC's binary frames and bidi streams win.
- Wrapping a domain model directly, expose a contract-shaped DTO, never an entity graph.

## Trade-offs

| Pros | Cons |
|---|---|
| Universal tooling, browsers and curl | JSON payload tax and per-call schema negotiation |
| Versioned additive evolution keeps clients working | Contract drift without generated interfaces + CI checks |
| GET/PUT/DELETE retry-safe by semantics | POST needs an idempotency key to be safe to retry |
| ETag/304 caching for free | HATEOAS (L3) rarely earns its complexity |

## Vs

| Aspect | REST + OpenAPI | gRPC + Protobuf |
|---|---|---|
| Wire | JSON, human-readable | Binary, compact |
| Schema | OpenAPI (often after the fact) | Protobuf, enforced and generated |
| Streaming | Workarounds (SSE/WebSocket) | Native bidi streaming |
| Browser/public edge | | Needs grpc-web proxy |
| Evolution | Additive fields, alias on rename | reserved numbers, never reuse |

## Pitfalls

- `POST` for everything (L0 in disguise), loses caching + retry semantics.
- Breaking rename of a JSON field without alias/dual-write.

## Interview q&a

- **Q: How do you evolve an API without breaking clients?** A: Additive changes only, optional fields, deprecate-then-remove with sunset header, Pact consumer tests in CI.
- **Q: Cursor vs offset pagination?** A: Cursor is stable under inserts and O(1) seeks; offset drifts and degrades.

## Related

- [[gRPC and Protobuf]] • [[Gateway and Service Mesh]] • [[Architect/08_NonFunctional-Ops/01_Security-OAuth2-JWT.md|Security OAuth2 and JWT]]

# REST Maturity and Contracts

> Part of [[README|07 Integration MOC]] • `integration` • **Richardson levels 0–3 + contracts.** Interviews test **idempotency, versioning, and OpenAPI-first**, not just verbs.

## TL;DR for Interviews

> **L2 (verbs + resources) is the production default; L3 (HATEOAS) rarely pays off.** Contract = **OpenAPI + consumer-driven tests (Pact)** + **backwards-compatible evolution** (additive, never rename/remove).

## Richardson Maturity

| Level | Meaning | Verdict |
|-------|---------|---------|
| L0 | Single endpoint, RPC-over-HTTP | Legacy SOAP tunnels, avoid |
| L1 | Resources, one verb | Partial, stepping stone |
| L2 | Resources + verbs + status codes | Production default |
| L3 | L2 + HATEOAS links | Only for discoverable public APIs |

## Spring Contract-First (OpenAPI Generator)

```java
// openapi.yaml → generated OrderApi interface; impl stays thin
// Concept: contract is the source of truth; code follows it
@RestController
public class OrderController implements OrderApi {
 @Override
 public ResponseEntity<OrderDto> getOrder(UUID id) {
 // Concept: 404 via exception handler, not null body
 return ResponseEntity.ok(service.find(id));
 }
}
```

## Rules that Matter

- **Idempotent methods:** `GET/PUT/DELETE` safe to retry; `POST` needs an **idempotency key** header.
- **Versioning:** URI (`/v1`) for public APIs; additive-only inside a version; **never break field types**.
- **Pagination:** cursor (`after`/`limit`) over offset for large sets; always envelope errors (`code`, `message`, `traceId`).

## Quick Check

- [ ] L2 vs L3, when is HATEOAS worth it?
- [ ] How do you make `POST /payments` idempotent?
- [ ] URI vs header versioning trade-off?
- [ ] What goes in a standard error envelope?
