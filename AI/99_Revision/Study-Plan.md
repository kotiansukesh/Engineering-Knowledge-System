---
title: "AI Engineering Study Plan"
category: "AI/99_Revision"
tags: [study-plan, roadmap, ai-engineering, architecture]
created: "2026-09-30"
completed: false
difficulty: Advanced
reviewed: ""
sr-due: ""
type: study-plan
weeks: "1-20"
---

# AI Engineering Study Plan

> **20 weeks.** Each week has a learning target, implementation target, and evidence gate.

## Phase 1 — Foundations (Weeks 1–4)

### Week 1 — LLM + API Foundations
LLM fundamentals, tokenization, inference parameters, APIs, structured outputs, tool calling.
**Build:** AI Code Assistant API.
**Evidence:** API + response contract + latency/cost notes.

### Week 2 — Embeddings + Retrieval
Embeddings, similarity, indexes, metadata filters, retrieval evaluation.
**Build:** semantic document search.
**Evidence:** retrieval dataset + precision/recall measurements.

### Week 3 — RAG Engineering
Ingestion, chunking, metadata, hybrid retrieval, reranking, context assembly, citations.
**Build:** enterprise Q&A baseline.
**Evidence:** retrieval + answer evaluation.

### Week 4 — RAG Quality
Query rewriting, multi-query, corrective/adaptive RAG, freshness, attribution.
**Build:** evaluated RAG pipeline.
**Gate:** justify every retrieval stage with a metric.

## Phase 2 — Agentic AI (Weeks 5–8)

### Week 5 — Agent Fundamentals
Agent loop, tool contracts, state, planning, termination.
**Build:** single-agent tool workflow.
**Gate:** prove why an agent is needed instead of a workflow.

### Week 6 — Memory + Multi-Agent
State, durable memory, planner/executor/reviewer, delegation.
**Build:** constrained multi-agent workflow.
**Gate:** budgets, terminal states, failure handling.

### Week 7 — Evaluation + Safety
Task success, tool correctness, groundedness, error analysis, guardrails, human approval.
**Build:** agent evaluation harness.
**Gate:** reproduce a failure and demonstrate the control.

### Week 8 — Production Agents
Observability, retries, timeouts, idempotency, audit trails, deployment.
**Build:** production-shaped agent.
**Gate:** failure-injection report.

## Phase 3 — Production AI Platform (Weeks 9–14)

### Week 9 — AI Gateway
Routing, quotas, retries, circuit breakers, provider abstraction.
**Build:** model gateway.

### Week 10 — Inference & Serving
Serving, batching, caching, streaming, GPU utilization.
**Build:** measured serving path.

### Week 11 — Data & Evaluation Platform
Dataset versioning, evaluation datasets, model/evaluation registry.
**Build:** repeatable evaluation pipeline.

### Week 12 — Observability
Traces, tokens, latency, cost, quality metrics, failure taxonomy.
**Build:** AI observability dashboard.

### Week 13 — Kubernetes for AI
Deployments, probes, resources, autoscaling, GPU scheduling.
**Build:** deploy an AI workload on Kubernetes.

### Week 14 — Reliability & Cost
Capacity planning, rate limits, graceful degradation, caching, model routing.
**Build:** load/failure test.
**Gate:** measured bottleneck → smallest useful architecture change.

## Phase 4 — Governance & Architecture (Weeks 15–20)

### Week 15 — AI Security
Prompt injection, data leakage, tool authorization, secrets, tenant isolation, supply chain.

### Week 16 — Governance
Model inventory, risk classification, lineage, auditability, human oversight, controls.

### Week 17 — AI Architecture
Boundaries, quality attributes, decisions, ADRs, model gateway, RAG and agent architecture.

### Week 18 — Enterprise AI Platform
Shared services, tenancy, platform boundaries, governance, reusable capabilities, build vs buy.

### Week 19 — Capstone
**ingest → retrieve → reason → act → evaluate → observe → govern**

### Week 20 — Architecture Review
Produce architecture diagram, ADR set, evaluation report, failure-injection report, cost model, security model, migration plan, and senior design walkthrough.

## Mastery Gate

A topic is mastered only when you can explain it, implement it, identify when not to use it, compare realistic alternatives, define measurable quality criteria, diagnose a failure, and defend the design under changed constraints.

## Weekly Ritual

**Learn → Build → Evaluate → Break → Explain → Record**

Use [[00 - AI Practice Engine|AI Practice Engine]].

## Related

- [[README|AI MOC]]
- [[Master Dashboard|Master Dashboard]]
- [[99_Revision/Interview Bank|Interview Bank]]
- [[99_Revision/Capstone Checklist|Capstone Checklist]]
- [[Architect/99_Revision/Study Plan|Architect Study Plan]]
