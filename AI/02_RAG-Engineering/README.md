---
title: "02 RAG Engineering"
type: folder-MOC
tags: [MOC, rag, coursera]
weeks: "5-10"
---

# 02_RAG-Engineering — Weeks 5–10 · Coursera C1 + C2

> From simple search to enterprise-grade RAG. Part of [[AI/README|AI MOC]]

**Certification:** Coursera **C1 LLM Engineering with RAG** (W5–6) → **C2 Design, Compare & Analyze LLM Architectures** (W7–10)  
**Platform evolution:** [[Enterprise Document Search]] — evolves from [[AI/01_Fundamentals/AI Backend Template|AI Backend Template]]

```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category", weeks as "Weeks"
FROM "AI/02_RAG-Engineering"
WHERE file.name != "README"
SORT file.name ASC
```

## Progress

```dataview
TABLE WITHOUT ID file.link as "Note", choice(completed, "✅", "⬜") as "Done"
FROM "AI/02_RAG-Engineering"
WHERE category
SORT file.name ASC
```

## Flow

1. [[01_LLM Engineering with RAG]] → ingest + pgvector + 12-factor
2. [[02_Design LLM Architectures]] → hybrid search, variants, cost comparison
3. [[Enterprise Document Search]] → the unified project
4. Cross-cutting: [[AI/07_Cross-Cutting/01_MCP|MCP]], [[AI/07_Cross-Cutting/02_AI Evaluation|Evaluation]]

[[AI/01_Fundamentals/README|← 01_Fundamentals]] • Next: [[AI/03_Agentic-AI/README|03_Agentic-AI]]
