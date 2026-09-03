---
title: "gRPC and Protobuf"
category: integration
tags: [grpc, protobuf, latency, streaming, interview]
created: 2026-09-03
completed: false
---

# gRPC and Protobuf

> Part of [[README|07 Integration MOC]] • `integration` • **Binary RPC for service-to-service.** Interviews test **when gRPC beats REST and schema evolution rules**.

## TL;DR for interviews

> **gRPC = HTTP/2 + Protobuf + codegen.** Pick it for **low-latency internal calls and streaming**; keep **REST at the edge** for browsers/public clients.

## When gRPC Wins

| Need | gRPC | REST |
|------|------|------|
| Payload size / speed | ✅ binary, ~5–10× smaller | JSON tax |
| Streaming (bidi, server-push) | ✅ native | SSE/WS workarounds |
| Browser / public API | ❌ needs grpc-web proxy | ✅ universal |
| Debuggability (`curl`) | ❌ needs `grpcurl` | ✅ trivial |

## Protobuf Evolution Rules

```proto
// Concept: field numbers are the contract — never reuse, never change type
syntax = "proto3";
message Order {
  string id = 1;
  int64 total_cents = 2;   // Concept: money as integer minor units
  // string status = 3;    // DEPRECATED — reserve it, don't delete
  reserved 3;
  OrderStatus status_v2 = 4;
}
enum OrderStatus { UNKNOWN = 0; PLACED = 1; PAID = 2; }
```

```java
// Concept: deadline propagates; never block a virtual thread on an unbounded stub call
ManagedChannel ch = ManagedChannelBuilder.forTarget("orders:9090").usePlaintext().build();
OrderServiceGrpc.OrderServiceBlockingStub stub =
    OrderServiceGrpc.newBlockingStub(ch).withDeadlineAfter(300, TimeUnit.MILLISECONDS);
```

## Quick Check

- [ ] Why `reserved` instead of deleting a field?
- [ ] Which 4 call types does gRPC support?
- [ ] Why deadlines on every stub call?

## Pitfalls

- Reusing a retired field number — silently corrupts old clients.
- No deadline → one slow downstream parks threads (even virtual ones pile up).

## Interview Q&A

- **Q: gRPC vs REST for payments authorize?** A: gRPC if internal mesh call with 50ms budget + streaming settlement updates; REST at public edge.
- **Q: How do you version Protobuf?** A: Additive fields, `reserved` numbers, `UNKNOWN = 0` default, dual-serve during rollout.

## Related

- [[REST Maturity and Contracts]] • [[Kafka Messaging and Idempotency]] • [[Gateway and Service Mesh]]
