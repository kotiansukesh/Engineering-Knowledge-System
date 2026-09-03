---
title: "Enterprise Document Search"
category: rag
tags: [ai, project, rag, pgvector]
weeks: "5-10"
created: 2026-09-02
completed: false
type: project
---

# Enterprise Document Search — Project (Weeks 5–10)

> Part of [[README|02_RAG-Engineering]] • `project` • The RAG evolution of [[AI/01_Fundamentals/AI Backend Template|AI Backend Template]]

## Intent

Enterprise-grade semantic search that **replaces** the generic "build a semantic search engine" course exercise — aligned to C1/C2, production-minded.

## Features

- [ ] Ingest pipeline: PDF/MD → chunk (512/50 overlap) → embed → pgvector (HNSW)
- [ ] **Hybrid search:** BM25 + vector via RRF
- [ ] **Metadata filtering:** department, date, confidentiality
- [ ] **Citations:** answer → `[1][2]` grounded in retrieved chunks
- [ ] **Streaming responses** (SSE) with partial citations
- [ ] Evaluation harness: precision@k, faithfulness, latency

## Week 7+ Enhancements (from C2)

- RAG variants A/B (naive → hybrid → reranker)
- Context compression (target 30–50% token saving)
- Retrieval strategy comparison table
- **Cost comparison:** managed embeddings vs self-hosted, with/without reranker

## API Sketch

```
POST /search  {query, filters, top_k} → {results: [{content, score, metadata, citation_id}]}
POST /ask     {query, filters} → stream {token, citations[]}
POST /ingest  {documents[]} → {ingested, chunks}
```

## Success Criteria

- Hybrid search measurably beats naive on eval set; citations verifiable; streaming <300ms TTFB.

## Related

- [[01_LLM Engineering with RAG]] • [[02_Design LLM Architectures]] • [[AI/03_Agentic-AI/Enterprise AI Operations Platform|Next: AI Operations Platform]]

---
*Category: rag*
