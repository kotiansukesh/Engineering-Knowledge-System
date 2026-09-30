---
title: "Certification Integration Roadmap"
category: "AI/99_Revision"
tags: [certifications, roadmap, coursera, nus-iss, kubernetes, isaqb]
created: "2026-09-30"
completed: false
difficulty: Advanced
reviewed: ""
sr-due: ""
type: certification-roadmap
---

# Certification Integration Roadmap

> Certifications are validation overlays on the engineering roadmap, not a replacement for implementation evidence.

## Principle

Use the sequence:

**Learn → Build → Measure → Harden → Validate → Defend**

Do not create separate course projects when the existing Enterprise AI Platform can absorb the same learning objectives.

## Current External Tracks

### 1. Coursera — LLM / LLM Architecture

Use the relevant courses as structured learning and validation around the existing RAG and architecture work.

Recommended placement:
- **Weeks 5–6:** RAG / LLM engineering content.
- **Weeks 7–8:** LLM architecture comparison and trade-offs.
- **Later modules:** production hardening, deployment, microservices and platform topics.

Evidence:
- retrieval benchmark
- architecture comparison
- cost/latency measurements
- ADR explaining build-vs-buy or managed-vs-self-hosted choices

Do not duplicate the vault's RAG project. Extend it.

### 2. NUS-ISS — Architecting Agentic AI Solutions

Place this after the agent fundamentals are understood and before the capstone becomes heavily platform-oriented.

The current NUS-ISS course is a 4-day course within the Graduate Certificate in Architecting AI Systems. It covers logical and physical architectures for agentic systems, multi-agent collaboration, frameworks and advanced software architecture techniques.

Use it to deepen:
- agent architecture
- multi-agent patterns
- interoperability
- logical vs physical architecture
- enterprise integration
- resilience and security decisions

Evidence:
- agent architecture diagram
- logical-to-physical mapping
- orchestration ADR
- human-approval boundaries
- failure-injection report

### 3. CKAD or CKA

Use Kubernetes certification preparation only after the AI platform has been deployed and operated.

**CKAD:** application-development orientation.

**CKA:** cluster administration and troubleshooting orientation.

Choose based on the intended role:
- AI application/platform engineering → CKAD
- deeper Kubernetes/platform ownership → CKA

Evidence:
- production-shaped Kubernetes deployment
- probes and resource limits
- autoscaling
- networking
- rollout/rollback
- troubleshooting runbook
- capacity and cost measurements

### 4. iSAQB CPSA-A / SWARC4AI

Treat SWARC4AI as an iSAQB Advanced Level module, not as a standalone replacement for the CPSA-A certification.

The module covers architecture for AI systems, including compliance/security/alignment, AI system design, data management, operational quality characteristics, GenAI architectures/platforms and case studies.

Place it after substantial AI architecture practice.

Evidence:
- architecture decision record set
- quality attribute scenarios
- governance/control mapping
- AI lifecycle model
- architecture review
- redesign under changed constraints

## Integrated Sequence

| Stage | Engineering work | External validation |
|---|---|---|
| 1 | LLM + API foundations | — |
| 2 | RAG engineering | Coursera LLM/RAG |
| 3 | Agentic AI | NUS-ISS Agentic AI |
| 4 | Production AI platform | Coursera production modules |
| 5 | Kubernetes operations | CKAD or CKA |
| 6 | Enterprise AI architecture | iSAQB SWARC4AI / CPSA-A path |
| 7 | Capstone defense | Portfolio + architecture review |

## Certification Gate

Before taking a certification, answer:

- What existing vault topic does it validate?
- What implementation evidence do I already have?
- What new capability will the course add?
- What will I deliberately not duplicate?
- What artifact will I produce afterward?

If these cannot be answered, defer the certification.

## Capstone

The same Enterprise AI Platform should evolve through the roadmap:

**ingest → retrieve → reason → act → evaluate → observe → govern → deploy → scale → defend**

The final portfolio should contain:
- architecture diagrams
- ADRs
- evaluation results
- failure-injection reports
- security controls
- cost model
- Kubernetes manifests
- operational runbooks
- migration plan
- architecture review

## Related

- [[AI/99_Revision/Study-Plan|AI Study Plan]]
- [[AI/00 - AI Practice Engine|AI Practice Engine]]
- [[Architect/99_Revision/Study Plan|Architect Study Plan]]
- [[Architect/13_AI-Architecture/README|AI Architecture]]
