---
title: "Architect Master MOC"
pattern: 0
category: "MOC"
tags: [architect, moc, roadmap]
created: 2026-09-03
updated: 2026-09-23
completed: false
reviewed:
sr-due:
difficulty: Easy
---
# Architect Master MOC

> Java/Spring backend (13+ yrs) → Software Architect. 24 weeks, 6–8h/week, 5 days/week.
> Part of [[README|Vault MOC]] • [ Dashboard](Dashboard.html)

---

## 24-Week Timeline

| Phase | Weeks | Theme | Outcome |
| ----- | ----- | ----- | ------- |
| 0 | 0 | [[00_Overview/README|Setup + Tech Stack]] | Vault, Java 21/25 + Spring Boot 3.5 baseline runs |
| 1 | 1–2 | [[01_Architecture-Foundations/What-is-Architecture|Architecture Foundations]] | Define architecture, roles, 4+1 views, principles |
| 2 | 3–4 | [[02_Requirements-Quality-Attributes/Quality-Scenarios|Requirements + Quality Attributes]] | ISO 25010, scenarios, fitness functions |
| 3 | 5–6 | [[03_Architecture-Styles/README|Styles + Patterns]] | Monolith → modular → microservices decision log |
| 4 | 7–8 | [[05_DDD-Modeling/README|DDD + Modelling (C4)]] | Bounded contexts, C4 L1–L3 of platform |
| 5 | 9–10 | [[06_Data-Architecture/README|Data Architecture]] | Postgres + Redis + Kafka patterns |
| 6 | 11–12 | [[07_Integration-APIs/README|Messaging + Event-Driven]] | Outbox, sagas, idempotency |
| 7 | 13–14 | [[07_Integration-APIs/README|APIs + Integration]] | REST maturity, versioning, gateway |
| 8 | 15–16 | [[08_NonFunctional-Ops/README|Security Architecture]] | OAuth2/OIDC, zero-trust, secrets |
| 9 | 17–18 | [[08_NonFunctional-Ops/README|Observability + SRE]] | SLOs, tracing, incident ADRs |
| 10 | 19–20 | [[08_NonFunctional-Ops/README|Cloud + K8s + IaC]] | EKS deployment, autoscaling, cost |
| 11 | 21–22 | [[09_Governance-Documentation/README|ADRs + Docs + Review]] | 10 ADRs, arc42 doc, review checklist |
| 12 | 23–24 | [[10_System-Design-Interviews/README|Capstone + Interview Prep]] | Event-driven reference arch + mock interviews |

---

## Platform Evolution (Running Thread)

```text
Java monolith (W1) → modular monolith (W5) → microservices (W11) → event-driven (W24)
Each phase: extend the SAME platform, record decision in ADR.
```
- W1–4: Monolith on Spring Boot 3.5 + Postgres. C4 context/container.
- W5–8: Modularize (ArchUnit boundaries), extract 1 service.
- W9–14: Kafka events, outbox, saga for Order→Payment.
- W15–24: K8s, observability, security hardening, capstone ADR set.

---

## Progress (Spaced Repetition)

```dataviewjs
const folders = [
 ["00_Overview", "00 Overview"],
 ["01_Architecture-Foundations", "01 Foundations"],
 ["02_Requirements-Quality-Attributes", "02 Qualities"],
 ["03_Architecture-Styles", "03 Styles"],
 ["04_Design-Patterns-Building-Blocks", "04 Patterns"],
 ["05_DDD-Modeling", "05 DDD"],
 ["06_Data-Architecture", "06 Data"],
 ["07_Integration-APIs", "07 APIs"],
 ["08_NonFunctional-Ops", "08 Ops"],
 ["09_Governance-Documentation", "09 Governance"],
 ["10_System-Design-Interviews", "10 SysDesign"],
 ["99_Revision", "99 Revision"],
];
const bar = (p, w=14) => "█".repeat(Math.round(p/100*w)) + "░".repeat(w - Math.round(p/100*w));
const rows = folders.map(([folder, label]) => {
 const pages = dv.pages(`"Architect/${folder}"`).where(p => p.category && p.file.name != "README");
 const total = pages.length;
 const done = pages.where(p => p.completed).length;
 const pct = total ? Math.round(done/total*100) : 0;
 const stale = pages.where(p => !p.reviewed || (dv.date("now") - dv.date(p.reviewed)).days > 7).length;
 return [`[[Architect/${folder}/README|${label}]]`, total, done, `${pct}%`, `\`${bar(pct)}\` ${pct}%`, stale ? `⚠ ${stale}` : ""];
});
dv.table(["Phase", "Total", "Done", "%", "Progress", "Stale (>7d)"], rows);
```

---

## Certification map

| Goal | Covers | Notes |
|------|--------|-------|
| iSAQB CPSA-F | Phases 1–2, 4, 11 (views, qualities, DDD, docs) | Scenario + views focus |
| TOGAF EA | Phase 11 (ADM, principles, stakeholders) | Map principles to ADM phases |
| AWS SA Associate | Phases 6, 10 (messaging, EKS, data) | Hands-on: EKS + MSK/SQS lab |

---

## Folders

- [[00_Overview/README|00 Overview]], [[00_Overview/Roadmap Overview|Roadmap]], [[00_Overview/Study Plan - Architect|Study Plan]], [[00_Overview/Dashboard|Dashboard]], [[00_Overview/Tech Stack|Tech Stack]]
- [[01_Architecture-Foundations/What-is-Architecture|01 Architecture Foundations]]
- [[02_Requirements-Quality-Attributes/Quality-Scenarios|02 Requirements + Quality Attributes]]
- [[03_Architecture-Styles/README|03 Architecture Styles]]
- [[04_Design-Patterns-Building-Blocks/README|04 Design Patterns]]
- [[05_DDD-Modeling/README|05 DDD Modeling]]
- [[06_Data-Architecture/README|06 Data Architecture]]
- [[07_Integration-APIs/README|07 Integration APIs]]
- [[08_NonFunctional-Ops/README|08 Non-Functional Ops]]
- [[09_Governance-Documentation/README|09 Governance]]
- [[10_System-Design-Interviews/README|10 System Design Interviews]]
- [[99_Revision/README|99 Revision]]

---

## Study Plan

See [[00_Overview/Study Plan - Architect|Study Plan - Architect]] and [[00_Overview/Dashboard|Dashboard]].