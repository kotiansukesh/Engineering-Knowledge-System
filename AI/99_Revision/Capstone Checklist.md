---
title: "Capstone Checklist"
category: revision
tags: [ai, capstone, checklist, revision]
created: 2026-09-02
completed: false
---

# Capstone Checklist — Final Review

> Part of [[README|99_Revision]] • `revision` • Use before marking any phase complete.

## Platform Evolution — Did You Evolve, Not Rebuild?

- [ ] Phase 01 → 02: `AI Backend Template` extended into `Enterprise Document Search` (same repo/evolution, not a new repo)?
- [ ] Phase 02 → 03: RAG search became a tool for the `Researcher` agent — not duplicated?
- [ ] Phase 03 → 04: Agents hardened with gateway, resilience, TDD, Helm, gRPC, observability?
- [ ] Phase 04 → 05: Same Helm charts deployed to K8s — not rewritten?
- [ ] Phase 05 → 06: Governance artifacts (ADRs, quality scenarios, compliance matrix) added — not just features?

## Certification → Platform Trace

| Cert | Evidence in Platform |
|------|----------------------|
| Coursera C1/C2 | Eval table, variant experiments, cost comparison — in `Enterprise Document Search` |
| NUS-ISS | 7-agent orchestration, memory, HITL, audit logs — in `AI Operations Platform` |
| Coursera C3–C7 | Gateway, circuit breaker, Helm, HPA, gRPC, Prometheus dashboards |
| CKAD/CKA | `kubectl` deploys full stack, all pods healthy |
| iSAQB SWARC4AI | ADRs, quality scenarios, EU AI Act matrix, drift/MLOps, threat model |

## Interview Readiness

- [ ] Can whiteboard the 36-week timeline in 2 minutes?
- [ ] Can explain *why* NUS-ISS after RAG (ecosystem thinking) and *why* iSAQB last (formalize after building)?
- [ ] Can defend pgvector vs Qdrant, LangGraph vs AutoGen, CKAD vs CKA with trade-offs?

## Related

- [[README]] • [[AI/README|AI MOC]] • [[AI/06_Architecture-Governance/02_Final Capstone Governance|Final Capstone]]

---
*Category: revision*
