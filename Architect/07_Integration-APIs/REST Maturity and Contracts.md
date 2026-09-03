---
title: "REST Maturity and Contracts"
category: integration
tags: [rest, openapi, contracts, versioning, interview]
created: 2026-09-03
completed: false
---

# REST Maturity and Contracts

> Part of [[README|07 Integration MOC]] • `integration` • **Richardson levels 0–3 + contracts.** Interviews test **idempotency, versioning, and OpenAPI-first** — not just verbs.

## TL;DR for interviews

> **L2 (verbs + resources) is the production default; L3 (HATEOAS) rarely pays off.** Contract = **OpenAPI + consumer-driven tests (Pact)** + **backwards-compatible evolution** (additive, never rename/remove).

## Richardson Maturity

| Level | Meaning | Verdict |
|-------|---------|---------|
| L0 | Single endpoint, RPC-over-HTTP | Legacy SOAP tunnels — avoid |
| L1 | Resources, one verb | Partial — stepping stone |
| L2 | Resources + verbs + status codes | ✅ Production default |
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

## Rules That Matter

- **Idempotent methods:** `GET/PUT/DELETE` safe to retry; `POST` needs an **idempotency key** header.
- **Versioning:** URI (`/v1`) for public APIs; additive-only inside a version; **never break field types**.
- **Pagination:** cursor (`after`/`limit`) over offset for large sets; always envelope errors (`code`, `message`, `traceId`).

## Quick Check

- [ ] L2 vs L3 — when is HATEOAS worth it?
- [ ] How do you make `POST /payments` idempotent?
- [ ] URI vs header versioning trade-off?
- [ ] What goes in a standard error envelope?

## Pitfalls

- `POST` for everything (L0 in disguise) — loses caching + retry semantics.
- Breaking rename of a JSON field without alias/dual-write.

## Interview Q&A

- **Q: How do you evolve an API without breaking clients?** A: Additive changes only, optional fields, deprecate-then-remove with sunset header, Pact consumer tests in CI.
- **Q: Cursor vs offset pagination?** A: Cursor is stable under inserts and O(1) seeks; offset drifts and degrades.

## Related

- [[gRPC and Protobuf]] • [[Gateway and Service Mesh]] • [[../08_NonFunctional-Ops/Security OAuth2 and JWT|Security OAuth2 and JWT]]
