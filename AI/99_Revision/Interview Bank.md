---
title: "AI Interview Bank"
category: "AI/99_Revision"
tags: [ai, interview, revision]
created: "2026-09-30"
type: interview-bank
---

# AI Interview Bank

> A rehearsal index, not a second curriculum. The current learning schedule remains [[Study Plan]].

## How to use

1. Pick a question.
2. Answer aloud before opening the source note.
3. Ground the answer in an artifact you actually built.
4. Give one measurement or concrete failure mode where applicable.
5. Name the rejected alternative and the condition that would change the decision.
6. If you cannot answer, return to the relevant domain note or project evidence.

## Questions by capability

### LLM and RAG

- How do structured outputs change the contract between an LLM and an application?
- When is vector retrieval insufficient, and when would hybrid retrieval or reranking be justified?
- How do you evaluate retrieval separately from answer quality?
- How do you detect stale, irrelevant or adversarial retrieved content?

Relevant sources:
- [[AI/01_Fundamentals/README]]
- [[AI/02_RAG-Engineering/README]]
- [[AI/02_RAG-Engineering/RAG Variants and Retrieval Strategies]]
- [[AI/02_RAG-Engineering/Checklist]]

### Agentic systems

- When is a deterministic workflow preferable to an agent?
- What makes a tool contract safe and testable?
- How do you bound agent loops and termination?
- When does delegation justify its additional latency, cost and failure surface?
- What state must survive a process restart?

Relevant sources:
- [[AI/03_Agentic-AI/README]]
- [[AI/03_Agentic-AI/06_Tool Calling]]
- [[AI/03_Agentic-AI/Multi-Agent Patterns]]

### Production AI

- What belongs in an AI gateway?
- How would you route requests across models/providers?
- Which latency, quality and cost metrics matter together?
- How do retries, idempotency and degradation interact with LLM calls?
- What evidence would make you change the routing decision?

Relevant sources:
- [[AI/04_Production-Platform/README]]
- [[AI/04_Production-Platform/01_AI Gateway]]
- [[AI/04_Production-Platform/02_AI TDD and Evaluation]]

### Platform operations

- When does Kubernetes add value to an AI workload?
- What should be measured before introducing autoscaling?
- How would you recover from a failed deployment or overloaded model service?
- What operational evidence would justify GPU-specific infrastructure?

Relevant sources:
- [[AI/05_Kubernetes-Operations/README]]

### Enterprise AI architecture

- How do you define trust boundaries for agents and tools?
- How do you prevent tenant data leakage?
- What should be auditable in an AI system?
- How do governance requirements change the architecture?
- What would you redesign at 10× scale?

Relevant sources:
- [[AI/06_Architecture-Governance/README]]
- [[Architect/13_AI-Architecture/README]]
- [[Evidence/README]]

## Evidence rule

An interview answer is stronger when it can point to:

**requirement → design → implementation → measurement → failure → decision**

Do not invent metrics or claim production experience that the evidence does not support.
