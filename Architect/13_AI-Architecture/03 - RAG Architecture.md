---
title: RAG Architecture
type: concept
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
## Architecture decisions

Decide explicitly:

- source-of-truth and document ownership;
- chunking strategy and metadata schema;
- vector-only versus hybrid retrieval;
- reranking criteria;
- freshness and re-indexing model;
- authorization propagation;
- citation/grounding requirements;
- behavior when evidence is missing or conflicting.

## Failure modes

Test irrelevant retrieval, missing documents, stale content, ambiguous queries, unauthorized content, adversarial content and oversized context.

## Evidence

Use a fixed evaluation set. Measure retrieval quality separately from answer quality, then measure end-to-end latency, token usage and cost. Record a retrieval failure and the design change that addresses it.
