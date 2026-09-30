---
title: "RAG Variants and Retrieval Strategies"
category: "AI/02_RAG-Engineering"
tags: [ai, rag, retrieval, reranking]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
reviewed: "2026-09-30"
sr-due: "2026-10-03"
type: "note"
---

# RAG Variants and Retrieval Strategies

## Intent
Choose retrieval strategies from measured failure modes rather than stacking techniques because they are available.

## Retrieval Ladder
**Naive vector → hybrid retrieval → query transformation → reranking → compression**.

Each step adds latency, infrastructure, or another model decision. The goal is not maximum sophistication; it is sufficient retrieval quality within the application's latency and cost budget.

## Decision Rules
| Symptom | Candidate change | Verify with |
|---|---|---|
| Exact identifiers or rare terms missed | Hybrid lexical + vector | recall@k on keyword-heavy set |
| Relevant docs appear but poor ordering | Reranker | precision@k / nDCG |
| Query is ambiguous | Query expansion / multi-query | recall and duplicate rate |
| Short query lacks semantic signal | Query transformation such as HyDE | recall on short-query set |
| Too much context | Compression / tighter retrieval | answer quality + token cost |
| Simple queries already pass | Keep baseline | latency/cost regression test |

## Architecture
~~~~mermaid
flowchart LR
Q[Query] --> V[Vector]
Q --> K[Lexical]
V --> H[Hybrid merge]
K --> H
H --> R[Reranker]
R --> C[Context] --> L[LLM] --> E[Evaluation]
~~~~

## Real Trade-offs
| Variant | Main benefit | Main cost/risk |
|---|---|---|
| Hybrid | lexical + semantic recall | two retrieval paths to operate |
| Multi-query | higher recall for ambiguous queries | extra generation calls and duplicates |
| HyDE | can improve low-signal queries | generated hypothesis can bias retrieval |
| Reranking | better ordering | additional inference latency |
| Compression | lower context cost | may remove evidence needed for answer |

## Evaluation
Use a versioned golden set. Measure retrieval recall@k, precision@k or nDCG where relevant, answer groundedness, latency, token cost, and failure rate. Evaluate each change against the same baseline.

## Failure Modes
1. Stacking variants without evaluation → latency grows without proven quality gain.
2. Tuning k by intuition → select k from retrieval experiments.
3. HyDE on exact factual lookup → generated text may dilute exact-match evidence.
4. Reranking too many candidates → latency budget is consumed before generation.
5. Metadata filters applied too late → irrelevant documents consume retrieval budget.

## Practice
- [ ] Build a baseline vector retriever.
- [ ] Add lexical retrieval and compare recall.
- [ ] Add reranking and measure precision/latency.
- [ ] Create 10 ambiguous queries and test query expansion.
- [ ] Remove one optimization and document whether quality actually regresses.

## Senior Interview Prompts
1. When does hybrid retrieval beat pure vector search?
2. What evidence justifies adding a reranker?
3. Why can HyDE hurt factual retrieval?
4. How do you choose candidate k and final k?
5. How do you prove a retrieval optimization is worth its latency?

## Flashcards
#flashcard
**Q:** What is the governing principle for RAG variants? :: **A:** Add a retrieval technique only when an observed failure mode and evaluation show that its benefit justifies its cost.

#flashcard
**Q:** What does a reranker optimize compared with a bi-encoder retriever? :: **A:** Retrieval produces a candidate set efficiently; reranking spends more computation to improve ordering/precision within that set.
