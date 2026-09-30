---
title: "Architecture Case Studies"
category: Architect/99_Revision
tags: [architecture, case-study]
created: 2026-09-30
type: case-study
---

# Architecture Case Studies

> Three applied designs for practicing constraint-driven architecture. These are exercises, not templates to copy.

## 1. E-commerce flash sale

**Constraint:** a short traffic spike with strict checkout latency.

**Design stance:** protect checkout availability with admission control, asynchronous intake where appropriate, idempotent inventory reservation, and a clear reconciliation model.

**Trade-off:** stale read-side inventory information can be tolerated only if reservation semantics prevent oversell.

## 2. Core banking ledger

**Constraint:** correctness of financial state dominates throughput optimization.

**Design stance:** transactional writes, explicit idempotency, append-only audit/ledger semantics where justified, and asynchronous processing only outside the critical financial invariant.

**Trade-off:** stronger consistency and auditability increase coordination and operational cost.

## 3. AI knowledge platform

**Constraint:** answer quality, freshness and inference cost must be balanced.

**Design stance:** retrieval + reranking only where measured useful, evaluation in the delivery path, caching where invalidation is understood, and explicit cost/latency budgets.

**Trade-off:** fresher retrieval can increase indexing and serving cost; aggressive caching can reduce cost while increasing staleness.

## Practice questions

For each case:

1. What are the actual requirements and exclusions?
2. Which quality attributes dominate, and how are they measured?
3. What is the simplest viable architecture?
4. What failure would hurt most?
5. Which alternative did you reject?
6. What evidence would cause you to redesign it?

## Related

- [[Architect/06_Data-Architecture/02_Consistency-CAP-PACELC|Consistency]]
- [[Architect/06_Data-Architecture/03_Event-Sourcing-CQRS|Event Sourcing and CQRS]]
- [[Architect/08_NonFunctional-Ops/03_Performance-SLOs|SLOs]]
- [[Architect/08_NonFunctional-Ops/06_Cost-FinOps|FinOps]]
- [[Architect/09_Governance-Documentation/02_ADRs|ADRs]]
