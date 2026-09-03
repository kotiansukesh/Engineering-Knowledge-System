---
title: "Kubernetes Deployment"
category: kubernetes
tags: [ai, kubernetes, helm, deployment]
weeks: "25-27"
created: 2026-09-02
completed: false
---

# Kubernetes Deployment — Weeks 25–27

> Part of [[README|05_Kubernetes-Operations]] • `kubernetes`

## Intent

Run the entire AI platform on K8s — the deployment that validates CKAD skills and proves operational readiness.

## Services to Deploy

| Service | Manifests | Notes |
|---------|-----------|-------|
| AI Gateway (FastAPI) | Deployment + Service + Ingress | From [[AI/04_Production-Platform/01_AI Gateway\|AI Gateway]] |
| Spring Boot (platform) | Deployment + Service | Coexists with FastAPI — your Java leverage |
| PostgreSQL + pgvector | StatefulSet + PVC | Vector extension enabled |
| Redis | Deployment + Service | Cache + rate limiting |
| Vector DB (optional Qdrant) | Helm release | For scale comparison |
| Kafka | Strimzi / Helm | Event streaming (optional) |
| Prometheus + Grafana | kube-prometheus-stack | From [[AI/04_Production-Platform/03_gRPC and Observability\|C7]] |

## Checklist

- [ ] Namespace `ai-platform`, resource quotas, network policies
- [ ] ConfigMaps / Secrets (no hardcoded keys — see [[AI/07_Cross-Cutting/04_AI Security|Security]])
- [ ] Liveness/readiness probes per service
- [ ] Persistent volumes for PG/Redis
- [ ] Ingress + TLS

## Interview Q&A

- **Q:** Why StatefulSet for PG? **A:** Stable identity + persistent storage; Deployments don't guarantee that.

## Related

- [[02_CKAD Preparation]] • [[AI/07_Cross-Cutting/04_AI Security|Security]]

---
*Category: kubernetes*
