---
title: "AI Engineering Syllabus"
category: "AI/99_Revision"
tags: [syllabus, ai-engineering, architecture, certifications]
created: "2026-09-30"
completed: false
type: syllabus
---

# AI Engineering Syllabus

> **This is a domain syllabus, not a second calendar.**
>
> The repository-wide [[Study Plan]] is the only learning calendar. Use this page to understand the AI domain and to jump to the material required by the current master-plan phase.

## How to use this page

1. Open [[Study Plan]] and identify the current phase/week.
2. Come here only for the relevant AI capability.
3. Learn the minimum required concepts.
4. Build the corresponding [[Build Lab/README|Build Lab]] artifact.
5. Record measurements, failures and decisions in [[Evidence/README|Evidence]].
6. Return to the master plan.

Do **not** complete this page from top to bottom unless the master plan explicitly requires it.

## AI learning spine

**LLM APIs → Retrieval → RAG → Tools → Agents → Evaluation → Production Platform → Governance → AI Architecture**

### Foundation

- LLM fundamentals, tokenization, inference parameters
- API contracts and structured outputs
- embeddings and similarity search
- metadata filtering and retrieval evaluation
- chunking, hybrid retrieval, reranking and context assembly
- citations, grounding and freshness

### Agentic AI

- workflow vs agent decision
- tool contracts and authorization
- agent loop, state and termination
- memory and durable state
- planning and delegation
- constrained multi-agent systems
- human approval and safety boundaries

### Evaluation and reliability

- task success and tool correctness
- groundedness and attribution
- datasets and repeatable evaluation
- error taxonomy
- retries, timeouts and idempotency
- audit trails and failure injection

### AI platform engineering

- model gateway and provider abstraction
- routing, quotas and rate limits
- caching and streaming
- inference/serving trade-offs
- observability: traces, tokens, latency, cost and quality
- Kubernetes deployment and operations
- capacity, graceful degradation and cost control

### Enterprise AI architecture

- security and prompt-injection defenses
- data leakage and tenant isolation
- governance, lineage and auditability
- platform boundaries and shared services
- architecture decisions and quality attributes
- build vs buy and managed vs self-hosted trade-offs

## Build progression

The preferred spine is one evolving system:

**AI Code Assistant → Semantic Search → RAG → Agent Workflow → Evaluated Agent → AI Gateway → AI Platform → Enterprise AI Platform**

Do not create a new project merely because a course or note suggests one.

## Evidence gate

A capability is not complete because its notes were read. Require:

- implementation;
- test/evaluation;
- measurement;
- failure experiment;
- trade-off explanation;
- evidence linked from the [[Evidence/README|Evidence]] domain.

## Certification overlay

Use [[AI/99_Revision/Certification Integration Roadmap|Certification Integration Roadmap]] only when the master plan reaches the relevant validation stage. Certifications validate the engineering path; they do not create another study calendar.

## Related

- [[Study Plan]]
- [[00 - Start Here]]
- [[AI/README]]
- [[Build Lab/README]]
- [[Evidence/README]]
