---
title: "04 Production Platform"
type: folder-MOC
tags: [MOC, production, coursera, microservices]
weeks: "17-24"
---
# 04_Production-Platform, Weeks 17–24 · Coursera C3–C7

> Harden the platform you already have. Part of [[AI/README|AI MOC]]

**Certification:** Coursera **C3–C7** (5 courses), *Microservices Architecture for AI Systems*
**Mapping:** Each module extends [[AI/03_Agentic-AI/Enterprise AI Operations Platform|AI Operations Platform]], no separate projects.
```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category", weeks as "Weeks"
FROM "AI/04_Production-Platform"
WHERE file.name != "README"
SORT file.name ASC
```

## Progress

```dataview
TABLE WITHOUT ID file.link as "Note", choice(completed, "✅", "⬜") as "Done"
FROM "AI/04_Production-Platform"
WHERE category
SORT file.name ASC
```

## Module → Platform Mapping

| Coursera Module | Platform Work |
|-----------------|---------------|
| C3 Resilient LLM Microservices | [[01_AI Gateway]] + retries/circuit breakers/rate limiting |
| C4 Refactor & Test | [[02_AI TDD and Evaluation]] |
| C5 Deploy Scalable LLM Apps | Helm + K8s autoscaling + rollouts |
| C6 AI Components | Platform architecture refinement |
| C7 Integrate AI Services | [[03_gRPC and Observability]] |

Adds: Helm charts, autoscaling, Prometheus, OpenTelemetry, caching, model routing.

[[AI/03_Agentic-AI/README|← 03_Agentic]] • Next: [[AI/05_Kubernetes-Operations/README|05_K8s-Ops]]
