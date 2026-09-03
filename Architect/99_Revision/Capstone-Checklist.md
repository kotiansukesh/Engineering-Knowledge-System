---
title: "Capstone Checklist"
category: "Revision"
tags: [capstone, checklist, design-review]
created: 2026-09-03
completed: false
---

# Capstone Checklist — Design Gate

Tick before calling any design done (`completed: true` only when all pass).

## Scope & quality
- [ ] C1 context + C2 containers drawn (actors, boundaries, protocols)
- [ ] Quality scenarios written (stimulus→response→measure) + top-3 risks
- [ ] Fitness functions named (what fails the build?)

## Data & integration
- [ ] State map: system-of-record per entity; consistency choice (CAP/PACELC) justified
- [ ] Contracts versioned (REST/OAS or proto); idempotency + ordering stated
- [ ] Migration plan: expand-migrate-contract + rollback + backfill

## NFRs
- [ ] SLOs (p50/p95/p99 + availability) + burn-rate alerts + dashboard link
- [ ] Security: OAuth scopes, secrets mgmt, PII encryption/redaction
- [ ] Resilience: breaker/bulkhead/fallback + chaos test named
- [ ] Cost: unit-cost metric + rightsizing/HPA-KEDA story

## Operate & govern
- [ ] Helm + GitOps + canary + probes/PDBs; image pin + CVE gate
- [ ] ADRs for irreversible calls; RFC link; runbook + GameDay date
- [ ] Compliance scope named (PCI/SOC2/DPDP) with evidence location

```dataview
TASK FROM "Architect/99_Revision/Capstone-Checklist" WHERE !completed
```
<!-- Concept: capstone = prove it ships, survives, and can be explained to an auditor. -->
