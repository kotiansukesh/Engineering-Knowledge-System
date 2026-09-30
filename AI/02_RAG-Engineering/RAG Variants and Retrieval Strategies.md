---
title: RAG Variants and Retrieval Strategies
category: AI/02_RAG-Engineering
tags:
- ai
- rag
- retrieval
- reranking
weeks: 8-9
created: 2026-09-02
completed: false
reviewed: "2026-09-29"
sr-due: "2026-09-30"
excalidraw: ''
difficulty: Medium
source: ''
type: note
---


## Why it Matters

The variants are not a menu of features, they are a ladder of cost, and the interview question is always "why did you stop where you stopped". This note gives the reasoning for each rung plus the evaluation harness that decides which rung a query actually needs, so the choice is data rather than fashion.

## Diagram

```mermaid
flowchart LR
 Q["Query"] --> N["Naive<br/>embed + top-k"]
 N -->|"keyword + semantic"| H["Hybrid<br/>BM25 + vector + RRF"]
 H -->|"ambiguous"| MQ["Multi-query<br/>LLM expands"]
 H -->|"short query"| HY["HyDE<br/>hypothetical doc"]
 H -->|"precision need"| RR["Reranker<br/>cross-encoder"]
 MQ --> CTX["Context"]
 HY --> CTX
 RR --> CTX
 CTX --> L["LLM + citations"]
 L -.-> EV["precision@k / MRR / faithfulness"]
```

## Code

```python

## When to use / NOT

- **Use:** multi-query when the query is ambiguous; HyDE for short low-signal queries; reranking when precision@k must be high; compression when context cost dominates.
- **NOT:** all of them at once — every variant adds latency and eval surface; adopt the rung your golden set says you need.

## Trade-offs

| Variant | What it costs |
|---------|----------------|
| Hybrid (RRF) | Two indexes to keep in sync |
| Multi-query | N extra LLM calls per query |
| HyDE | A generated doc can mislead retrieval |
| Reranking | Cross-encoder latency on every query |
| Compression | An extra model decision, possible information loss |

## Vs

| Axis | Naive top-k | Hybrid (BM25 + vector) | Reranking on top | Long-context / "stuff everything" |
|------|-------------|------------------------|------------------|----------------------------------|
| Precision@k on keyword-heavy queries | Low — exact terms missed | High — lexical match retained | Highest — cross-encoder reorders | Depends on where the answer sits in the window |
| Query-time cost | 1 embed + 1 LLM | 2 indexes, 1 LLM | Adds a cross-encoder pass per query | Many embeds, one very large LLM call |
| Latency p95 | Lowest | Low | Highest of the retrieval-only rungs | Context length sets the floor |
| Failure mode | Semantic drift on rare terms | Indexes drift apart | Precision gain too small to justify the ms | Lost in the middle; stale context after every doc edit |
| Why you stop here | Baseline to beat | When keyword + semantic both matter | Only when the measured precision gap clears the latency budget | Only while context fits one window |

## Pitfalls

- Stacking variants without re-running the eval — cost grows, accuracy may not.
- Tuning `k` in RRF by feel; it is a hyperparameter, measure it.
- HyDE on factual lookups — a hypothetical document is noise when an exact match exists.
- Reranking 100 candidates and blaming the model for latency; cap the candidate window.

## Interview Q&A

- **Q:** Why rerank? **A:** Bi-encoder (fast, recall) retrieves; cross-encoder (slow, precise) prefers — best of both.

## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the trigger keyword for RAG Variants and Retrieval Strategies? :: **A:** [trigger keywords] #flashcard

#flashcard
**Q:** Key hyperparameter for RAG Variants and Retrieval Strategies? :: **A:** [hyperparameter + typical range] #flashcard

#flashcard
**Q:** When do you NOT use RAG Variants and Retrieval Strategies? :: **A:** [anti-pattern scenarios] #flashcard

#flashcard
**Q:** Cost order of magnitude for RAG Variants and Retrieval Strategies? :: **A:** [GPU hours / $ per 1M tokens] #flashcard

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
- [[02_RAG-Engineering/README|02_RAG-Engineering Folder]]

---

*Category: AI/02_RAG-Engineering • Part of [[README|AI MOC]]*