---
title: "Design, Compare and Analyze LLM Architectures (Coursera C2)"
category: rag
tags: [ai, architecture, coursera, cost]
weeks: "7-10"
created: 2026-09-02
completed: false
---

# Design, Compare and Analyze LLM Architectures — Coursera Course 2

> Part of [[README|02_RAG-Engineering]] • `rag` • Weeks 7–10

## Intent

Go beyond "it works" — compare architectures on quality, latency, and **cost**; run variant experiments on your own platform.

## Key Topics (C2)

- System flow analysis: self-host vs managed API cost models.
- **RAG variants:** naive, hybrid (BM25+vector), reranking, query expansion, HyDE.
- **Context compression** (LLMLingua-style), retrieval strategies, caching.
- Cost comparisons: tokens, embeddings, vector storage, reranker calls.

## Experiments to Run (on [[Enterprise Document Search]])

| Variant | Change | Metric |
|---------|--------|--------|
| Naive RAG | top-k vector only | precision@5, faithfulness |
| Hybrid | BM25 + vector (RRF) | + recall |
| + Reranker | cross-encoder rerank top-20→5 | + precision, + latency |
| + Compression | compress context 50% | tokens saved vs quality delta |
| + Query expansion | multi-query / HyDE | recall on ambiguous queries |

## Code Example

```python
# hybrid search — Reciprocal Rank Fusion
def rrf(rank_lists, k=60):
    scores = {}
    for lst in rank_lists:
        for rank, doc_id in enumerate(lst, 1):
            scores[doc_id] = scores.get(doc_id, 0) + 1/(k+rank)
    return sorted(scores, key=scores.get, reverse=True)
```

## Interview Q&A

- **Q:** When does hybrid beat pure vector? **A:** Keyword-heavy queries (IDs, error codes) where BM25 catches exact terms vectors miss.
- **Q:** How to compare self-host vs managed cost? **A:** Model cost per 1k tokens vs GPU hourly + throughput; include ops overhead.

## Pitfalls

- Optimizing for retrieval precision while ignoring answer faithfulness — measure both.

## Related

- [[01_LLM Engineering with RAG]] • [[Enterprise Document Search]] • [[AI/07_Cross-Cutting/05_Cost Optimization|Cost Optimization]]

---
*Category: rag*
