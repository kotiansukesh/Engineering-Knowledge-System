---
title: gRPC and Observability (C5–C7)
category: AI/04_Production-Platform
tags:
- ai
- grpc
- protobuf
- observability
- prometheus
- opentelemetry
- kubernetes
weeks: 21-24
created: 2026-09-02
completed: false
reviewed: "2026-09-29"
sr-due: "2026-09-30"
excalidraw: ''
difficulty: Medium
source: ''
type: note
---

## Why it Matters

Make the platform **scalable, deployable, and observable**, Helm, K8s, gRPC, Prometheus, OpenTelemetry.

## Diagram

```mermaid
flowchart LR
 AIFast["FastAPI AI layer"] -->|"gRPC + Protobuf"| J1["Spring: user-svc"]
 AIFast --> J2["Spring: doc-svc"]
 J1 --> PG[(PostgreSQL)]
 subgraph obs["Observability"]
 OT["OpenTelemetry"] --> LS["Langfuse / Phoenix"]
 OT --> PR["Prometheus"]
 PR --> GR["Grafana"]
 end
 AIFast -.-> OT
 J1 -.-> OT
```

## Code

```proto
syntax = "proto3";

package platform.v1;

// The seam between the Python AI layer and the Java/Spring estate.
service DocumentService {
 rpc GetDocuments(DocumentQuery) returns (DocumentList);
}

message DocumentQuery {
 string query = 1;
 uint32 top_k = 2;
 string tenant = 3;
}

message Document {
 string id = 1;
 string title = 2;
 float score = 3;
}

message DocumentList {
 repeated Document documents = 1;
}
```

## When to use / not

- **Use:** for cross-language service-to-service calls between the Python AI layer and the Java/Spring estate; protobuf is the contract both sides compile against.
- **NOT:** for browser-facing APIs (keep REST/SSE there) or for internal Python-to-Python calls where a typed HTTP client is enough.

## Trade-offs

| Choice | Cost |
|--------|------|
| gRPC between layers | Schema is now a compilation step; contract changes touch both sides |
| OTel everywhere | Sampling decisions matter; 100% tracing is expensive at LLM call volume |
| Two trace backends | Correlation work to join a user request across languages |

## Vs

| Aspect | gRPC + Protobuf | REST/JSON | GraphQL |
|--------|------------------|-----------|---------|
| Contract | Compiled, both languages | OpenAPI, advisory | Schema, query-driven |
| Streaming | HTTP/2 bidi | SSE one-way | Subscriptions |
| Fit here | AI layer ↔ Spring estate | Client ↔ gateway | Not needed |

## Pitfalls

- Protobuf without a versioning convention; a field rename breaks both sides at once.
- Tracing without propagation across the gRPC boundary, the trace dies at the language seam, exactly where you need it.
- LLM traces in the same backend as infra metrics, so a token-billing query and a p95 query fight each other.
- Sampling set to 100% "to be safe" on a path that makes an LLM call per span.

## Interview q&a

- **Q:** Why gRPC between the AI layer and the Spring services? **A:** Because the boundary crosses two languages and changes often, and a compiled protobuf contract makes a breaking change a build failure rather than a runtime 500. Streaming answers also map cleanly onto HTTP/2.
- **Q:** How do you trace one user request across Python and Java? **A:** OpenTelemetry context propagation through the gRPC metadata, the trace ID crosses the boundary in headers, so Langfuse and Prometheus see the same request. Without that, the trace dies exactly where the two estates meet.
- **Q:** What is the observability signal you would not ship without? **A:** Per-request cost. Latency and error rates are standard; token cost per request is the metric that makes an AI platform a system you can reason about financially, not just operationally.

## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the trigger keyword for gRPC and Observability (C5–C7)? :: **A:** [trigger keywords] #flashcard

#flashcard
**Q:** Key hyperparameter for gRPC and Observability (C5–C7)? :: **A:** [hyperparameter + typical range] #flashcard

#flashcard
**Q:** When do you NOT use gRPC and Observability (C5–C7)? :: **A:** [anti-pattern scenarios] #flashcard

#flashcard
**Q:** Cost order of magnitude for gRPC and Observability (C5–C7)? :: **A:** [GPU hours / $ per 1M tokens] #flashcard

## Practice Tasks (Tasks Plugin)
- [ ] Restate the intent from memory 📅 2026-09-30
- [ ] Code the config without looking 📅 2026-10-02
- [ ] Answer all Interview Q&A aloud 📅 2026-10-06
- [ ] Review flashcards (Spaced Repetition) 📅 2026-09-30

```tasks
not done
path includes 04_Production-Platform
sort by due
limit 10
```

## Related
- [[README|AI MOC]]
- [[04_Production-Platform/README|04_Production-Platform Folder]]

---

*Category: AI/04_Production-Platform • Part of [[README|AI MOC]]*