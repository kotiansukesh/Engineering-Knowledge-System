---
title: RAG Architecture
type: note
category: Architect/13_AI-Architecture
difficulty: Hard
tags: [architecture, ai, rag]
---

# RAG Architecture

**Ingestion → normalization → chunking → embedding/indexing → retrieval → reranking → context construction → generation → citation/evaluation**

## Questions

- What is the freshness requirement?
- What is the retrieval quality target?
- How is tenant isolation enforced?
- How are access controls propagated?
- What happens when retrieval confidence is low?
- How are documents re-indexed?
