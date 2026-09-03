---
title: "Interview Bank"
category: revision
tags: [ai, interview, revision]
created: 2026-09-02
completed: false
---

# Interview Bank — AI Platform

> Part of [[README|99_Revision]] • `revision` • Curated Q&A aggregated from `00..07`. Source of truth remains in each note.

## How to Use

- This is a **cram index** — answers live in source notes (linked). Don't duplicate.
- For spaced repetition, add `sr-due: YYYY-MM-DD` to source notes; [[README|Dashboard]] tracks due.

## Fundamentals (01)

- Why Pydantic v2 for LLM outputs? → [[AI/01_Fundamentals/01_Python for AI|Python for AI]]
- FastAPI streaming for LLM tokens? → [[AI/01_Fundamentals/02_FastAPI Backend|FastAPI Backend]]
- Tool calling vs RAG? → [[AI/01_Fundamentals/06_Tool Calling|Tool Calling]]

## RAG (02)

- pgvector vs dedicated vector DB? → [[AI/02_RAG-Engineering/01_LLM Engineering with RAG|C1]]
- When does hybrid beat pure vector? → [[AI/02_RAG-Engineering/02_Design LLM Architectures|C2]]
- Why rerank? → [[AI/02_RAG-Engineering/RAG Variants and Retrieval Strategies|RAG Variants]]

## Agentic (03)

- LangGraph vs AutoGen vs Assistants API? → [[AI/03_Agentic-AI/Multi-Agent Patterns|Multi-Agent Patterns]]
- How to prevent agent loops? → [[AI/03_Agentic-AI/Multi-Agent Patterns|Multi-Agent Patterns]]

## Production (04)

- Why circuit breaker for LLM? → [[AI/04_Production-Platform/01_AI Gateway|AI Gateway]]
- How to TDD a non-deterministic LLM service? → [[AI/04_Production-Platform/02_AI TDD and Evaluation|AI TDD]]

## K8s (05)

- Why StatefulSet for PG? → [[AI/05_Kubernetes-Operations/01_Kubernetes Deployment|K8s Deployment]]
- CKAD vs CKA? → [[AI/05_Kubernetes-Operations/02_CKAD Preparation|CKAD Prep]]

## Governance (06)

- Why iSAQB after CKAD? → [[AI/06_Architecture-Governance/01_SWARC4AI Syllabus|SWARC4AI]]
- EU AI Act risk tiers? → [[AI/06_Architecture-Governance/01_SWARC4AI Syllabus|SWARC4AI]]

## Cross-Cutting (07)

- MCP vs plain tool calling? → [[AI/07_Cross-Cutting/01_MCP|MCP]]
- Hallucination detection? → [[AI/07_Cross-Cutting/02_AI Evaluation|Evaluation]]
- Semantic cache invalidation? → [[AI/07_Cross-Cutting/05_Cost Optimization|Cost Optimization]]

## 2026 Trends (from [[AI/00_Overview/2026 Trends Update|2026 Trends]])

- Why MCP is now the tool bus, not "additional"? → [[AI/00_Overview/2026 Trends Update|Trends]] + [[AI/07_Cross-Cutting/01_MCP|MCP]]
- Reasoning vs fast model routing? → [[AI/07_Cross-Cutting/06_Multi-Model Routing|Multi-Model Routing]]
- GraphRAG vs hybrid search? → [[AI/02_RAG-Engineering/RAG Variants and Retrieval Strategies|RAG Variants]] + [[AI/00_Overview/2026 Trends Update|Trends]]
- How do you gate AI changes in CI? → [[AI/07_Cross-Cutting/02_AI Evaluation|Evaluation]] + [[AI/04_Production-Platform/02_AI TDD and Evaluation|AI TDD]]

---

Use Dataview to live-aggregate all Q&A (source stays in notes):

```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category"
FROM "AI"
WHERE category AND file.folder != "AI/99_Revision"
SORT file.path ASC
```

[[README|← Back to 99_Revision]]

---
*Category: revision*
