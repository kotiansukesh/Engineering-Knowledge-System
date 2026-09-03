---
title: "Case Studies"
category: "Revision"
tags: [case-study, ecommerce, banking, ai]
created: 2026-09-03
completed: false
---

# Case Studies — 3 Applied Designs

## Case 1: E-commerce Flash Sale (10x spike)
- **Context:** 5k→50k rps for 2h, checkout p95<800ms, PG primary melts.
- **Design:** CDN + read replicas; Kafka order-intake (keyed by customer); outbox → inventory reserve with idempotency keys; KEDA on lag; canary deploy; Redis last-known-price fallback.
- **NFRs:** SLO 99.9% checkout; OTel burn-rate alerts; WAF + rate-limit at gateway.
- **Tradeoff:** Eventual stock counts (oversell guard via reserve-then-confirm) for survival.
- Links: [[../08_NonFunctional-Ops/03_Performance-SLOs|Perf]] · [[../08_NonFunctional-Ops/04_Resilience-Chaos|Chaos]] · [[../06_Data-Architecture/04_Caching-CDN|Caching]]

## Case 2: Core Banking Ledger (never wrong)
- **Context:** Money moves; auditors + DPDP; zero lost writes.
- **Design:** Modular monolith first; event-sourcing for ledger (append-only) + CQRS read models; Postgres SERIALIZABLE for transfers; mTLS + OAuth client-credentials; Flyway expand-migrate-contract; HSM-backed keys.
- **NFRs:** Strong consistency (PACELC: choose consistency on partition); SOC2/PCI evidence-as-code; per-txn audit trail.
- **Tradeoff:** Throughput for correctness; async only at edges (notifications).
- Links: [[../06_Data-Architecture/03_Event-Sourcing-CQRS|ES-CQRS]] · [[../09_Governance-Documentation/05_Compliance-Audit|Compliance]] · [[../02_ADRs|ADRs]]

## Case 3: AI Platform (RAG + evals)
- **Context:** RAG over 10M docs, p95 chat<2s, GPU bill exploding, hallucinations risky.
- **Design:** Gateway (BFF) → retrieval svc (vector DB + rerank) → LLM svc (prompt registry, evals); async ingest pipeline (Kafka); Redis semantic cache; FinOps: spot GPUs, scale-to-zero, unit cost per 1k queries.
- **NFRs:** Groundedness evals in CI; PII redaction pre-index; trace per prompt (OTel gen_ai attrs).
- **Tradeoff:** Freshness vs cost (incremental index, not realtime-everything).
- Links: [[../08_NonFunctional-Ops/06_Cost-FinOps|FinOps]] · [[../08_NonFunctional-Ops/02_Observability-OTel-Prometheus|OTel]] · [[../03_Review-Process-RFC|RFC]]
<!-- Concept: same toolbox, different stakes — sale=survive, bank=correct, AI=grounded+cheap. -->
