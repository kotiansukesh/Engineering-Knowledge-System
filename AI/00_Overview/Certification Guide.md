---
title: "Certification Guide"
category: overview
tags: [ai, certification, nus-iss, coursera, ckad, isaqb]
created: 2026-09-02
completed: false
---

# Certification Guide

> Part of [[README|AI MOC]] • `overview` • All 4 certs in sequence — what, when, why.

## 1. Coursera — Microservices Architecture for AI Systems (7 courses)

| Course | Weeks | Theme | Platform Task |
|--------|-------|-------|---------------|
| **C1: LLM Engineering with RAG** | 5–6 | RAG, pgvector, 12-factor for AI | Enterprise Document Search v1 |
| **C2: Design, Compare & Analyze LLM Architectures** | 7–10 | Architecture trade-offs, cost vs. self-host, RAG variants | RAG variant experiments + cost comparison |
| **C3: Architect Resilient LLM Microservices** | 17–18 | 12-factor, fault tolerance | AI Gateway + resilience patterns |
| **C4: Refactor & Test LLM Microservices** | 19–20 | TDD, refactoring for AI services | AI TDD + evaluation harness |
| **C5: Analyze & Deploy Scalable LLM Architectures** | 21–22 | Perf diagnosis, Helm, K8s autoscaling, rollouts | Helm charts + autoscaling |
| **C6: Design Scalable AI Systems & Components** | 23 | Components, platform architecture | Platform architecture refinement |
| **C7: Integrate & Optimize AI Services** | 24 | gRPC/Protobuf, Prometheus | gRPC + monitoring integration |

> **Rule:** Don't create separate course projects — evolve the platform.

## 2. NUS-ISS — Architecting Agentic AI Solutions

- **When:** Weeks 11–16 (Phase 03) — after you know agents/tools/MCP/RAG/orchestration.
- **Format:** 4-day intensive (~32h), part of Graduate Certificate in Architecting AI Systems.
- **Audience:** Senior SWEs, Tech Leads, Enterprise Architects with solid backend experience.
- **Core topics:** Logical/physical architecture for agent systems; multi-agent collaboration; frameworks (LangChain, AutoGen, Assistants APIs); microservices/containers/serverless deployment; API gateway/service mesh/monitoring; model selection + RAG pipelines.
- **Quality attributes:** autonomy, scalability, security, fault tolerance, explainability.
- **Capstone:** [[AI/03_Agentic-AI/Enterprise AI Operations Platform|Enterprise AI Operations Platform]] (7 agents).

## 3. CKAD (or CKA) — Kubernetes

- **When:** Weeks 25–30 (Phase 05) — you already have a production-grade platform to deploy.
- **Why CKAD:** App-centric (deploy FastAPI, Spring Boot, PG, Redis, vector DB, Kafka, Prometheus, Grafana on K8s). Choose **CKA** if leaning platform/infra.
- **Validates:** manifests, Helm, autoscaling, config/secrets, networking, troubleshooting.

## 4. iSAQB CPSA-A — SWARC4AI (Software Architecture for AI)

- **When:** Weeks 31–36 (Phase 06) — after substantial building, to formalize.
- **Format:** 3-day (~24h), Advanced Level, 20 Tech + 10 Method points toward CPSA-A exam.
- **Syllabus:** AI/ML/GenAI classification & risks; compliance (GDPR, **EU AI Act**, copyright), security, ethics; ML lifecycle, requirements, non-determinism, drift, design patterns; data acquisition/labeling/pipelines; hardware, cost, **Green IT**, drift types, MLOps/CI/CD; GenAI patterns (RAG, prompt eng., agentic workflows), LLM cost management.
- **Capstone:** Same platform + governance, drift handling, enterprise integration, threat models.

## Sequencing Logic

```
Fundamentals → RAG (C1/C2) → Agentic (NUS-ISS) → Harden (C3-C7) → Deploy (CKAD) → Govern (iSAQB)
```

Each step assumes the previous. NUS-ISS *before* hardening so you design the ecosystem before productionizing it.

## Related

- [[Roadmap Overview]] • [[AI/04_Production-Platform/README|04 Production]] • [[AI/06_Architecture-Governance/README|06 Governance]]

---
*Category: overview*
