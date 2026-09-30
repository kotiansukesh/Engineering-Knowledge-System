---
title: "AI Engineering Study Plan"
category: "AI/99_Revision"
tags: [study-plan, roadmap, ai-engineering, architecture, certifications]
created: "2026-09-30"
completed: false
difficulty: Advanced
reviewed: ""
sr-due: ""
type: study-plan
weeks: "1-36"
---

# AI Engineering Study Plan

> **36-week integrated path:** 20-week engineering core + 16-week certification and capstone extension.

The certifications are validation overlays. The recurring Enterprise AI Platform is the main project; external courses should deepen or validate the work rather than create duplicate projects.

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
**Validation:** Coursera LLM/RAG learning can reinforce the retrieval and architecture foundations.

### Week 6 — Memory + Multi-Agent
State, durable memory, planner/executor/reviewer, delegation.
**Build:** constrained multi-agent workflow.
**Gate:** budgets, terminal states, failure handling.
**Validation:** use LLM architecture material to compare synchronous/asynchronous, managed/self-hosted and other realistic system choices.

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
**Validation:** Coursera production/deployment material may be used here if it maps to the current implementation.

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
**Validation:** prepare for the NUS-ISS agent architecture material using the existing agent and platform artifacts.

### Week 18 — Enterprise AI Platform
Shared services, tenancy, platform boundaries, governance, reusable capabilities, build vs buy.

### Week 19 — Capstone
**ingest → retrieve → reason → act → evaluate → observe → govern**

### Week 20 — Architecture Review
Produce architecture diagram, ADR set, evaluation report, failure-injection report, cost model, security model, migration plan, and senior design walkthrough.

## Phase 5 — Certification Validation Extension (Weeks 21–36)

The extension converts the 20-week engineering core into externally validated evidence. Do not restart the learning sequence.

### Weeks 21–22 — Coursera LLM / RAG Validation
Revisit the relevant LLM/RAG modules.
**Apply:** strengthen the Enterprise Document Search and RAG evaluation.
**Evidence:** retrieval benchmark, citations/grounding analysis, architecture comparison and cost/latency measurements.

### Weeks 23–24 — Coursera LLM Architecture
Use architecture-analysis material to compare realistic alternatives.
**Build:** architecture decision pack covering request flow, deployment model, managed vs self-hosted options, latency, cost, privacy and operational complexity.
**Evidence:** ADRs + trade-off table + measured benchmark.

### Weeks 25–27 — Production AI Platform Hardening
Map relevant Coursera production modules onto the existing platform.
**Add:** resilient microservices, AI gateway improvements, testing, gRPC where justified, streaming, retries, circuit breakers, caching, model routing and observability.
**Gate:** every added component must be justified by a requirement, failure mode or measured bottleneck.

### Weeks 28–30 — Kubernetes Certification Track
Deploy the complete AI platform:
- AI Gateway
- FastAPI services
- Spring Boot service
- PostgreSQL
- Redis
- vector store
- Kafka where justified
- Prometheus/Grafana or equivalent observability

**Choose:**
- **CKAD** for application-development and deployment depth.
- **CKA** for cluster administration and troubleshooting depth.

**Evidence:** manifests, probes, resources, autoscaling, networking, rollout/rollback and troubleshooting runbook.

### Weeks 31–33 — NUS-ISS Agentic Architecture Deepening
Use [[99_Revision/Certification Integration Roadmap|Certification Roadmap]] to align the course with existing agent artifacts.

**Focus:** logical/physical architecture, multi-agent collaboration, interoperability, framework selection and enterprise integration.

**Evidence:** logical architecture, physical architecture, orchestration ADR, human-approval boundaries and failure-injection report.

### Weeks 34–35 — iSAQB SWARC4AI / CPSA-A Path
Treat SWARC4AI as the AI-architecture Advanced Level module, not as a standalone CPSA-A certification.

**Focus:** AI architecture, compliance/security/alignment, data management, operational quality characteristics, GenAI platforms and case studies.

**Evidence:** architecture decision set, quality scenarios, governance/control mapping, lifecycle model and architecture review.

### Week 36 — Final Capstone Defense
The platform should demonstrate:

**ingest → retrieve → reason → act → evaluate → observe → govern → deploy → scale → defend**

Produce:
- architecture diagrams
- ADR set
- evaluation report
- failure-injection report
- security/control matrix
- cost model
- Kubernetes artifacts
- operational runbooks
- migration plan
- architecture review

## External Validation Map

| Stage | Engineering work | Validation |
|---|---|---|
| 1 | LLM + API foundations | — |
| 2 | RAG engineering | Coursera LLM/RAG |
| 3 | Agentic AI | NUS-ISS Agentic AI |
| 4 | Production AI platform | Coursera production modules |
| 5 | Kubernetes operations | CKAD or CKA |
| 6 | Enterprise AI architecture | iSAQB SWARC4AI / CPSA-A path |
| 7 | Capstone | Portfolio + architecture defense |

## Mastery Gate

A topic is mastered only when you can explain it, implement it, identify when not to use it, compare realistic alternatives, define measurable quality criteria, diagnose a failure, and defend the design under changed constraints.

## Weekly Ritual

**Learn → Build → Evaluate → Break → Explain → Record**

Use [[00 - AI Practice Engine|AI Practice Engine]].

## Related

- [[README|AI MOC]]
- [[Master Dashboard|Master Dashboard]]
- [[99_Revision/Certification Integration Roadmap|Certification Roadmap]]
- [[99_Revision/Interview Bank|Interview Bank]]
- [[99_Revision/Capstone Checklist|Capstone Checklist]]
- [[Architect/99_Revision/Study Plan|Architect Study Plan]]
