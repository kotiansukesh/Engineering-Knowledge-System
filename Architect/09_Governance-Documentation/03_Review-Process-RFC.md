---
title: "Review Process — RFCs & Design Reviews"
category: "Governance & Docs"
tags: [rfc, design-review, governance, process]
created: 2026-09-03
completed: false
---

# Review Process — RFCs & Design Reviews

> **Intent:** De-risk big changes cheaply: written proposal → async comments → time-boxed review → decision + ADR; code is the last step.

## 1. When to Use
- New service, public API, data-model or topology change.
- Cross-team dependency or migration.
- Any spend/scale/security tradeoff.

**When NOT:** Tiny PRs needing a 10-person council; review-as-rubber-stamp; RFCs with no alternatives or rollout plan.

## 2. Example (Spring Boot 3.5 + K8s)

```java
# RFC template (1-3 pages)
# 1. Problem + goals/non-goals  2. Options (≥2, with tradeoffs)
# 3. Proposal (C4-C2 diagram + API sketch + data impact)
# 4. NFRs: perf budget, SLO, cost, security, observability
# 5. Rollout: expand-migrate-contract, feature flag, rollback
# 6. Open questions + decision deadline + owners
```

## 3. Pros / Cons
| Pros | Cons |
|---|---|
| Catches coupling/security/cost early | Async latency (SLA: 48h first pass) |
| Async = inclusive across zones | Review fatigue without triage/lanes |
| Paper trail for audits | Heavyweight authors avoid writing |

## 4. Vs
- **Vs PR review:** PR reviews code correctness; RFC reviews *direction* — rejecting direction in PR is 10× costlier.
- **Vs ADRs:** RFC is the debate; ADR is the verdict.

## 5. Interview Q&A
**Q: What triggers an RFC?**
A: New datastore/broker, public/partner API, cross-boundary sync call, schema break, infra topology or IAM model change.

**Q: Who must attend?**
A: Author + owning team + one each from affected teams + security/data on call; quorum > titles.

**Q: How do you avoid bike-shedding?**
A: Time-box 45m, pre-read required, decide by deadline (owner decides, dissent recorded), prototype spikes for unknowns.

## 6. Pitfalls
- No measurable acceptance (SLO/cost/latency missing).
- Approving without data-migration/rollback section.
- RFC merged but no ADR written.

## 7. Links
- [[02_ADRs]] · [[01_C4-Modeling]] · [[04_TOGAF-iSAQB-Primer]]
