---
title: "RAG Variants and Retrieval Strategies"
category: rag
tags: [ai, rag, retrieval, reranking]
weeks: "8-9"
created: 2026-09-02
completed: false
---

# RAG Variants and Retrieval Strategies

> Part of [[README|02_RAG-Engineering]] • `rag` • Weeks 8–9

## Variants

| Variant | Idea | When |
|---------|------|------|
| Naive | Embed query → top-k | Baseline |
| Hybrid | BM25 + vector (RRF) | Keyword + semantic queries |
| Multi-query | LLM expands query → 3 variants | Ambiguous queries |
| HyDE | Generate hypothetical doc → embed | Short queries |
| Reranking | Cross-encoder rescores top-20→5 | High precision need |
| Context compression | Compress retrieved context | Cost/token limits |

## Evaluation

- **Retrieval:** precision@k, recall@k, MRR.
- **Answer:** faithfulness (LLM-as-judge), citation accuracy, hallucination rate.
- Keep a comparison table in [[Enterprise Document Search]] — that's your C2 deliverable.

## Interview Q&A

- **Q:** Why rerank? **A:** Bi-encoder (fast, recall) retrieves; cross-encoder (slow, precise) prefers — best of both.

## Related

- [[02_Design LLM Architectures]] • [[AI/07_Cross-Cutting/02_AI Evaluation|Evaluation]]

---
*Category: rag*
