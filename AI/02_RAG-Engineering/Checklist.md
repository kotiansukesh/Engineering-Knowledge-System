---
title: "Phase 02 — RAG Engineering Checklist"
category: rag
tags: [ai, checklist]
created: 2026-09-02
completed: false
---

# Phase 02 — RAG Engineering Checklist

```dataview
TABLE WITHOUT ID item as "Done"
FROM "AI/02_RAG-Engineering/Checklist.md"
WHERE file.name = "Checklist.md"
SORT item ASC
```

- ✅ pgvector extension installed + HNSW index built
- ✅ Hybrid search (BM25 + vector) returns top-5
- ✅ Citations are grounded (each answer claim traced to a chunk)
- ✅ RAG variant A/B table built (naive vs hybrid vs reranker)
- ✅ Cost comparison table (tokens per query, with/without reranker)
