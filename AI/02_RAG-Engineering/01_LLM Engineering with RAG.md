---
title: "LLM Engineering with RAG (Coursera C1)"
category: rag
tags: [ai, rag, coursera, pgvector]
weeks: "5-6"
created: 2026-09-02
completed: false
---

# LLM Engineering with RAG — Coursera Course 1

> Part of [[README|02_RAG-Engineering]] • `rag` • Weeks 5–6

## Intent

Build a production-aware RAG pipeline: ingest → chunk → embed → store (pgvector) → retrieve → generate — with 12-factor discipline.

## When to Use / NOT

- **Use:** Enterprise doc search, knowledge assistants, any domain where LLM needs private context.
- **NOT:** When data fits in context window trivially or when freshness requires live tool calls over indexed retrieval.

## Key Topics (C1)

- RAG architecture (naive → advanced), chunking strategies, embedding choice.
- **pgvector** on PostgreSQL: `vector` type, HNSW/IVFFlat indexes, metadata filtering.
- 12-factor for LLM apps (config, dependencies, disposability, logs).

## Code Example

```sql
-- pgvector setup
CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE docs (
  id SERIAL PRIMARY KEY,
  content TEXT,
  metadata JSONB,
  embedding vector(1536)
);
CREATE INDEX ON docs USING hnsw (embedding vector_cosine_ops);

-- hybrid: vector + metadata filter
SELECT content FROM docs
WHERE metadata->>'department' = 'engineering'
ORDER BY embedding <=> :query_embedding LIMIT 5;
```

```python
# ingest sketch
from pgvector.psycopg import register_vector
chunks = chunk_text(doc, size=512, overlap=50)
embeddings = await embed_batch(chunks)
await insert_many([(c, m, e) for c,m,e in zip(chunks, metas, embeddings)])
```

## Pros / Cons

| Pros | Cons |
|------|------|
| Grounds LLM in private data | Chunking/embedding quality is critical |
| Postgres-native (no new infra) | Vector search tuning (index, distance) |

## Interview Q&A

- **Q:** pgvector vs dedicated vector DB? **A:** pgvector reuses PG ops/joins/transactions; dedicated DBs scale vectors further — compare in [[02_Design LLM Architectures]].
- **Q:** Chunk size trade-off? **A:** Small → precise but fragmented; large → context-rich but noisy. Evaluate retrieval precision@k.

## Pitfalls

- Not normalizing embeddings before cosine distance.
- Missing citations → hallucination risk (addressed in [[Enterprise Document Search]]).

## Related

- [[02_Design LLM Architectures]] • [[Enterprise Document Search]] • [[AI/07_Cross-Cutting/02_AI Evaluation|Evaluation]]

---
*Category: rag*
