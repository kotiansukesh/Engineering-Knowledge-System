---
title: "Non-Functional Requirements & Ops"
type: folder-MOC
tags: [MOC, 08-nonfunctional-ops]
---
# Non-Functional Requirements & ops

> Non-Functional Requirements & Ops, the notes below. | Part of [[Architect/README\|Architect MOC]]

## Ops

| Note | Covers |
|---|---|
| [[Architect/08_NonFunctional-Ops/01_Security-OAuth2-JWT\|01_Security-OAuth2-JWT]] | Grant flows, token lifetimes, key rotation |
| [[Architect/08_NonFunctional-Ops/02_Observability-OTel-Prometheus\|02_Observability-OTel-Prometheus]] | Metrics/logs/traces; SLO burn alerts |
| [[Architect/08_NonFunctional-Ops/03_Performance-SLOs\|03_Performance-SLOs]] | Latency percentiles; error budgets |
| [[Architect/08_NonFunctional-Ops/04_Resilience-Chaos\|04_Resilience-Chaos]] | Failure injection; steady-state hypotheses |
| [[Architect/08_NonFunctional-Ops/05_Cloud-K8s-Deploy-Helm\|05_Cloud-K8s-Deploy-Helm]] | Workload kinds, probes, HPA, chart structure |
| [[Architect/08_NonFunctional-Ops/06_Cost-FinOps\|06_Cost-FinOps]] | Unit economics; commit vs on-demand |
```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category"
FROM "Architect/Architect/08_NonFunctional-Ops"
WHERE file.name != "README"
SORT file.name ASC
```
[[Architect/README|← Back to Architect MOC]]

---
*Category: Architect/Architect/08_NonFunctional-Ops*
