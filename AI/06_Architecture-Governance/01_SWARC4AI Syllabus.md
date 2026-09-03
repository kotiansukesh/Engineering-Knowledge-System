---
title: "SWARC4AI Syllabus (iSAQB)"
category: governance
tags: [ai, isaqb, architecture, governance, compliance]
weeks: "31-36"
created: 2026-09-02
completed: false
---

# SWARC4AI Syllabus — iSAQB CPSA-A

> Part of [[README|06_Architecture-Governance]] • `governance` • Weeks 31–36

## Intent

Internationally recognized, vendor-neutral architecture certification — bridge traditional enterprise architecture with AI's unique concerns.

## Syllabus (Official iSAQB)

| Block | Topics |
|-------|--------|
| **Intro & Fundamentals** | Classify AI/ML/GenAI; risks vs traditional software |
| **Compliance, Security & Alignment** | GDPR, **EU AI Act**, copyright, security pitfalls, AI ethics |
| **Design & Development** | ML/data-science lifecycle, process models, data requirements, non-determinism, **model drift**, AI design patterns |
| **Data Management** | Acquisition, labeling, efficient **data pipelines & architectures** |
| **Quality & Operation** | Hardware, **cost & sustainability (Green IT)**, drift types, **MLOps** pipelines, CI/CD, deployment strategies |
| **GenAI & Architectures** | LLMs, **GenAI patterns** (RAG, prompt eng., agentic workflows), **GenAI cost management** |

## How to Use It Here

Don't just pass the exam — **embed each concern in your platform**:

- EU AI Act risk classification → threat model for [[AI/03_Agentic-AI/Enterprise AI Operations Platform|AI Operations Platform]]
- Quality attributes (security, explainability, sustainability) → architecture decision records (ADRs)
- MLOps + drift handling → pipeline for embeddings/model routing (see [[AI/07_Cross-Cutting/02_AI Evaluation|Evaluation]])
- Green IT → cost/energy dashboard

## Interview Q&A

- **Q:** Why iSAQB after CKAD? **A:** CKAD proves you can *deploy*; iSAQB proves you can *govern* — you need both for Staff/Principal.
- **Q:** EU AI Act relevance? **A:** Risk-tiered obligations (high-risk AI needs conformity, logging, human oversight) — your audit logs + HITL gates satisfy them.

## Related

- [[02_Final Capstone Governance]] • [[AI/07_Cross-Cutting/README|Cross-Cutting]] • [[AI/00_Overview/Certification Guide|Certification Guide]]

---
*Category: governance*
