---
title: "05 Kubernetes Operations"
type: folder-MOC
tags: [MOC, kubernetes, ckad]
weeks: "25-30"
---
# 05_Kubernetes-Operations, Weeks 25–30 · CKAD / cka

> Deploy the hardened platform on Kubernetes and prove it. Part of [[AI/README|AI MOC]]

**Certification:** **CKAD** (or **CKA** if leaning platform engineering)
**Prereq:** [[AI/04_Production-Platform/README|04_Production]], you already have Helm charts, gRPC, observability.
```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category", weeks as "Weeks"
FROM "AI/05_Kubernetes-Operations"
WHERE file.name != "README"
SORT file.name ASC
```

## Progress

```dataview
TABLE WITHOUT ID file.link as "Note", choice(completed, "✅", "⬜") as "Done"
FROM "AI/05_Kubernetes-Operations"
WHERE category
SORT file.name ASC
```

## Stack to Deploy

FastAPI · Spring Boot · PostgreSQL (pgvector) · Redis · Vector DB · Kafka · Prometheus · Grafana

[[AI/04_Production-Platform/README|← 04_Production]] • Next: [[AI/06_Architecture-Governance/README|06_Governance]]
