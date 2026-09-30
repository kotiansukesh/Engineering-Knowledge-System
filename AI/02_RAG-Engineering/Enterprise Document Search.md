---
title: Enterprise Document Search
category: AI/02_RAG-Engineering
tags:
- ai
- project
- rag
- pgvector
weeks: 5-10
created: 2026-09-02
completed: false
type: project
reviewed: "2026-09-29"
sr-due: "2026-09-30"
excalidraw: ''
difficulty: Medium
source: ''
---


## Why it Matters

Enterprise-grade semantic search that **replaces** the generic "build a semantic search engine" course exercise, aligned to C1/C2, production-minded.

## Diagram

```mermaid
flowchart LR
 IN["Ingest: POST /ingest"] --> CH["Chunk + metadata"]
 CH --> EM["Embed"]
 EM --> V[(pgvector)]
 Q["Query: POST /ask<br/>{query, filters}"] --> H["Hybrid BM25 + vector"]
 H --> RK["Rerank"]
 RK --> L["LLM"]
 L -->|"stream + citations"| C["Client"]
 H -.-> E["Eval harness<br/>(Phase 04 gate)"]
```

## Code

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Enterprise Document Search")

class SearchRequest(BaseModel):
 query: str
 filters: dict[str, str] = Field(default_factory=dict)
 top_k: int = 5

class SearchHit(BaseModel):
 doc_id: str
 snippet: str
 score: float

@app.post("/ask")
async def ask(req: SearchRequest) -> list[SearchHit]:
 # hybrid: BM25 + vector, merged with RRF, then reranked (see variants note)
 raise NotImplementedError # retrieval + rerank + LLM compose

@app.post("/ingest")
async def ingest(documents: list[dict]) -> dict:
 # chunk with metadata (dept, acl), embed, upsert into pgvector
 return {"ingested": len(documents)}

@app.get("/health")
async def health() -> dict[str, str]:
 return {"status": "ok"}
```

## When to use / not

- **Use:** as the Phase 02 centerpiece, one search service that Phase 03 sees as a tool and Phase 04 sees as a microservice.
- **NOT:** as a replacement for the transactional search estate; this is the AI retrieval layer over documents the enterprise already owns.

## Trade-offs

- Hybrid search measurably beats naive on eval set; citations verifiable; streaming <300ms TTFB.

## Vs

| Aspect | This service | Existing enterprise search (ES/Solr) | Vector-only demo |
|--------|-------------|----------------------------------------|------------------|
| Strength | Semantic + keyword + rerank, citations | Mature ops, proven at scale | Semantic similarity |
| Filters/ACL | First-class (dept, acl metadata) | Mature | Usually missing |
| Eval | Golden set, CI gate | Rarely measured | None |

## Pitfalls

- Ignoring document permissions in the retrieval layer, the search returns what the ranking model liked, not what the user may see.
- Chunking without metadata; filters and ACLs are retrofitted painfully.
- Returning citations the LLM did not actually use; citation and context must come from the same retrieved set.
- No version on the embedding model, re-embedding an old index alongside a new one silently splits relevance.

## Interview q&a

- **Q:** How do you handle document-level permissions in a RAG service? **A:** Filters are part of the retrieval query, not a post-filter after ranking. Metadata like department and ACL travels with the chunk, so a ranking model never promotes a document the user cannot read.
- **Q:** Why hybrid BM25 plus vector instead of vector alone? **A:** Because enterprise queries are mixed, identifiers, codes and exact names are keyword-shaped, intent questions are semantic. Hybrid with RRF handles both; either alone loses one class of query.
- **Q:** What happens when the search is wrong? **A:** It tells you, citations are returned with every answer, so a wrong answer traces to a retrieval failure you can inspect, rather than a model confidence you cannot.

## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the trigger keyword for Enterprise Document Search? :: **A:** Not specified #flashcard

#flashcard
**Q:** Key hyperparameter for Enterprise Document Search? :: **A:** Not specified #flashcard

#flashcard
**Q:** When do you NOT use Enterprise Document Search? :: **A:** [anti-pattern scenarios] #flashcard

#flashcard
**Q:** Cost order of magnitude for Enterprise Document Search? :: **A:** Not specified #flashcard

## Practice Tasks (Tasks Plugin)
- [ ] Restate the intent from memory 📅 2026-09-30
- [ ] Code the config without looking 📅 2026-10-02
- [ ] Answer all Interview Q&A aloud 📅 2026-10-06
- [ ] Review flashcards (Spaced Repetition) 📅 2026-09-30

```tasks
not done
path includes 02_RAG-Engineering
sort by due
limit 10
```

## Related
- [[README|AI MOC]]
- 02_RAG-Engineering Folder

---

*Category: AI/02_RAG-Engineering • Part of [[README|AI MOC]]*