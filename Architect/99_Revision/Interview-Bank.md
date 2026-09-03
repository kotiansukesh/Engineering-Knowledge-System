---
title: "Interview Bank"
category: "Revision"
tags: [interview, questions, architect]
created: 2026-09-03
completed: false
---

# Interview Bank

> 3 Q&A per note — jump to the source for depth.

## 08 NonFunctional-Ops
- Security: token storage? revocation? JWT vs opaque? → [[../08_NonFunctional-Ops/01_Security-OAuth2-JWT|Security-OAuth2-JWT]]
- Observability: RED vs USE? cardinality? head vs tail sampling? → [[../08_NonFunctional-Ops/02_Observability-OTel-Prometheus|Observability]]
- Performance: set SLO? pool sizing? JFR vs profiler? → [[../08_NonFunctional-Ops/03_Performance-SLOs|Performance-SLOs]]
- Resilience: safe GameDay? backpressure? chaos order? → [[../08_NonFunctional-Ops/04_Resilience-Chaos|Resilience-Chaos]]
- K8s: zero-downtime schema? promotion gates? HPA for consumers? → [[../08_NonFunctional-Ops/05_Cloud-K8s-Deploy-Helm|K8s-Deploy]]
- FinOps: first 3 wins? attribution? perf vs cost? → [[../08_NonFunctional-Ops/06_Cost-FinOps|Cost-FinOps]]

## 09 Governance-Documentation
- C4: C2 vs C3? freshness? when C1 enough? → [[../09_Governance-Documentation/01_C4-Modeling|C4-Modeling]]
- ADR: 5 sections? supersede? approvers? → [[../09_Governance-Documentation/02_ADRs|ADRs]]
- RFC: triggers? attendees? anti-bikeshed? → [[../09_Governance-Documentation/03_Review-Process-RFC|Review-RFC]]
- TOGAF: ADM phases? iSAQB core? startup slice? → [[../09_Governance-Documentation/04_TOGAF-iSAQB-Primer|TOGAF-iSAQB]]
- Compliance: PCI scope? deletion vs backups? SOC2 evidence? → [[../09_Governance-Documentation/05_Compliance-Audit|Compliance]]

## Core (00-07) rapid links
- [[../04_Design-Patterns-Building-Blocks/02_Resilience-Circuit-Breaker-Retry|Circuit-Breaker]] · [[../03_Architecture-Styles/03_Microservices|Microservices]] · [[../03_Architecture-Styles/04_Event-Driven-Architecture|EDA]]
- Patterns: [[../04_Design-Patterns-Building-Blocks/05_Decomposition-Bounded-Context|Decomposition]] · [[../04_Design-Patterns-Building-Blocks/06_Saga-Outbox-Inbox|Saga-Outbox]] · [[../04_Design-Patterns-Building-Blocks/07_Discovery-Config-Registry|Discovery-Config]] · [[../04_Design-Patterns-Building-Blocks/04_API-Gateway-BFF|Gateway-BFF]]

```dataview
TABLE completed AS Done FROM "Architect/08_NonFunctional-Ops" SORT file.name ASC
```
<!-- Concept: bank = index, not duplicate; answers live in source notes. -->
