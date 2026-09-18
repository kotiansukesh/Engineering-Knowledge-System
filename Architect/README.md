---
title: Architect Master MOC
category: MOC
tags: [architect, moc, roadmap]
created: 2026-09-03
completed: false
---
# Architect Master moc

Java/Spring backend (13+ yrs) → Software Architect. 24 weeks, 6–8h/week, 5 days/week.

## 24-Week Timeline

| Phase | Weeks | Theme | Outcome |
| ----- | ----- | ------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| 0 | 0 | [[00_Overview/README\|Setup + Tech Stack]] | Vault, Java 21/25 + Spring Boot 3.5 baseline runs |
| 1 | 1–2 | [[01_Architecture-Foundations/What-is-Architecture\|Architecture Foundations]] | Define architecture, roles, 4+1 views, principles |
| 2 | 3–4 | [[02_Requirements-Quality-Attributes/Quality-Scenarios\|Requirements + Quality Attributes]] | ISO 25010, scenarios, fitness functions |
| 3 | 5–6 | Styles + Patterns | Monolith → modular → microservices decision log |
| 4 | 7–8 | DDD + Modelling (C4) | Bounded contexts, C4 L1–L3 of platform |
| 5 | 9–10 | Data Architecture | Postgres + Redis + Kafka patterns |
| 6 | 11–12 | Messaging + Event-Driven | Outbox, sagas, idempotency |
| 7 | 13–14 | APIs + Integration | REST maturity, versioning, gateway |
| 8 | 15–16 | Security Architecture | OAuth2/OIDC, zero-trust, secrets |
| 9 | 17–18 | Observability + SRE | SLOs, tracing, incident ADRs |
| 10 | 19–20 | Cloud + K8s + IaC | EKS deployment, autoscaling, cost |
| 11 | 21–22 | ADRs + Docs + Review | 10 ADRs,arc42 doc, review checklist |
| 12 | 23–24 | Capstone + Interview Prep | Event-driven reference arch + mock interviews |

## Platform Evolution (Running Thread)

```text
Java monolith (W1) → modular monolith (W5) → microservices (W11) → event-driven (W24)
Each phase: extend the SAME platform, record decision in ADR.
```
- W1–4: Monolith on Spring Boot 3.5 + Postgres. C4 context/container.
- W5–8: Modularize (ArchUnit boundaries), extract 1 service.
- W9–14: Kafka events, outbox, saga for Order→Payment.
- W15–24: K8s, observability, security hardening, capstone ADR set.

## Progress (Dataviewjs per Folder)

```dataviewjs
const folders = ["00_Overview","01_Architecture-Foundations","02_Requirements-Quality-Attributes"];
for (const f of folders) {
 const pages = dv.pages(`"${f}"`).where(p => p.completed !== undefined);
 const done = pages.where(p => p.completed).length;
 dv.paragraph(`**${f}**: ${done}/${pages.length} done`);
}
```

## Certification map

| Goal | Covers | Notes |
|------|--------|-------|
| iSAQB CPSA-F | Phases 1–2, 4, 11 (views, qualities, DDD, docs) | Scenario + views focus |
| TOGAF EA | Phase 11 (ADM, principles, stakeholders) | Map principles to ADM phases |
| AWS SA Associate | Phases 6, 10 (messaging, EKS, data) | Hands-on: EKS + MSK/SQS lab |

## Folders

- [[00_Overview/README|00 Overview]], [[00_Overview/Roadmap Overview|Roadmap]], [[00_Overview/Study Plan - Architect|Study Plan]], [[00_Overview/Dashboard|Dashboard]], [[00_Overview/Tech Stack|Tech Stack]]
- [[01_Architecture-Foundations/What-is-Architecture|01 Architecture Foundations]]
- [[02_Requirements-Quality-Attributes/Quality-Scenarios|02 Requirements + Quality Attributes]]

## Study Plan

See [[00_Overview/Study Plan - Architect|Study Plan - Architect]] and [[00_Overview/Dashboard|Dashboard]].
