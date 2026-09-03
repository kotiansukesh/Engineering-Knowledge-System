---
title: "gRPC and Observability (C5–C7)"
category: production
tags: [ai, grpc, protobuf, observability, prometheus, opentelemetry, kubernetes]
weeks: "21-24"
created: 2026-09-02
completed: false
---

# gRPC and Observability — Coursera C5–C7

> Part of [[README|04_Production-Platform]] • `production` • Weeks 21–24

## Intent

Make the platform **scalable, deployable, and observable** — Helm, K8s, gRPC, Prometheus, OpenTelemetry.

## Key Topics

| Course | Topics | Deliverable |
|--------|--------|-------------|
| **C5** Analyze & Deploy Scalable LLM Architectures | Diagnose RAG bottlenecks, Helm on K8s, **autoscaling** (HPA), **managed rollouts** | Helm charts + HPA |
| **C6** Design Scalable AI Systems & Components | Component boundaries, platform architecture | Architecture diagrams |
| **C7** Integrate & Optimize AI Services | **gRPC + Protobuf** for prediction services, **Prometheus** monitoring | gRPC services + dashboards |

## gRPC Sketch

```protobuf
// ai_platform.proto
service PredictionService {
  rpc Predict(PredictRequest) returns (PredictResponse);
  rpc StreamPredict(PredictRequest) returns (stream Token);
}
message PredictRequest { string query = 1; map<string,string> filters = 2; }
```

## Observability Stack

- **Prometheus** — latency, throughput, error rate, token cost per endpoint.
- **OpenTelemetry** — trace: gateway → retrieval → LLM → response.
- **Grafana** dashboards + alerts (p95 latency, hallucination rate, cost spike).

## Hardening Checklist (by W24)

- [ ] gRPC services for retrieval + prediction
- [ ] Helm charts (per service)
- [ ] HPA (CPU + custom metric: queue depth)
- [ ] Prometheus + Grafana dashboards
- [ ] OTel traces across gateway → agents → LLM
- [ ] Retries / circuit breakers / rate limiting / caching / model routing (from C3)

## Related

- [[01_AI Gateway]] • [[AI/05_Kubernetes-Operations/README|05_K8s-Operations]] • [[AI/07_Cross-Cutting/03_LLM Observability|LLM Observability]]

---
*Category: production*
