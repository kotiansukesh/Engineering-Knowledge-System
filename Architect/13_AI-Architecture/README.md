---
title: AI Architecture
type: folder-MOC
category: Architect/13_AI-Architecture
tags: [architecture, ai, agentic-ai]
---

# AI Architecture

AI architecture applies the same constraint-driven reasoning to systems where models, context, tools and probabilistic behavior are first-class components.

## Learning map

- [[13_AI-Architecture/01 - AI System Architecture]]
- [[13_AI-Architecture/02 - Model Gateway and Routing]]
- [[13_AI-Architecture/03 - RAG Architecture]]
- [[13_AI-Architecture/04 - Agent Architecture]]
- [[13_AI-Architecture/05 - Tool and Integration Architecture]]
- [[13_AI-Architecture/06 - Memory Architecture]]
- [[13_AI-Architecture/07 - Evaluation Architecture]]
- [[13_AI-Architecture/08 - AI Observability]]
- [[13_AI-Architecture/09 - AI Security and Guardrails]]
- [[13_AI-Architecture/10 - AI Cost Engineering]]
- [[13_AI-Architecture/11 - Enterprise AI Platform]]

## AI architecture loop

**Requirement → AI suitability → model/context choice → tools/agents → data → evaluation → security → observability → cost → failure modes → governance**

## Engineering implementation bridge

Use the AI vault for implementation depth, while this folder focuses on architecture decisions and system-level trade-offs.

- [[AI/01_Fundamentals/README|AI Fundamentals]]
- [[AI/02_RAG-Engineering/README|RAG Engineering]]
- [[AI/03_Agentic-AI/README|Agentic AI]]
- [[AI/04_Production-Platform/README|Production AI Platform]]
- [[AI/06_Architecture-Governance/README|AI Governance]]

Architecture work should link back to implementation evidence where useful: evaluation results, latency/cost measurements, failure-injection results, security controls and operational constraints.

## Principle

Do not use an agent because a deterministic workflow is sufficient. Add autonomy when uncertainty, tool use or adaptation requirements justify it.
