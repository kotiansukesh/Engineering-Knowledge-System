---
title: RAG Engineering Exit Gate
category: AI/02_RAG-Engineering
tags: [ai, rag, checklist, evaluation]
created: 2026-09-30
completed: false
type: gate
difficulty: Medium
---

# RAG Engineering Exit Gate

> **The deliverable is evidence, not the retrieval feature.**
>
> Use this gate when the master [[Study Plan]] reaches RAG engineering.

## Exit criteria

- [ ] Documents are ingested with stable IDs and metadata.
- [ ] Vector retrieval works with a documented index configuration.
- [ ] Hybrid retrieval is compared with vector-only retrieval where justified.
- [ ] Reranking is tested only if it improves a measured objective.
- [ ] A golden evaluation set contains easy, ambiguous, multi-hop and out-of-scope queries.
- [ ] Precision@k and recall@k (or an explicitly justified alternative) are measured.
- [ ] p95 latency and token/cost impact are recorded.
- [ ] Answer claims can be traced to retrieved evidence.
- [ ] At least one retrieval failure is reproduced and explained.
- [ ] The chosen retrieval architecture has an ADR or equivalent decision record.

## Required comparison

| Variant | Precision@5 | Recall@5 | p95 latency | Tokens/query | Cost/query | Notes |
|---|---:|---:|---:|---:|---:|---|
| Vector only | | | | | | |
| Hybrid | | | | | | |
| Hybrid + rerank | | | | | | |

Do not call a variant an improvement until the comparison is populated under controlled conditions.

## Failure experiments

At minimum test:
- irrelevant documents;
- missing documents;
- ambiguous query;
- stale document;
- adversarial/injected document content;
- large retrieved context.

For each failure record:
**trigger → observed behavior → root cause → mitigation → residual risk**

## Decision rules

- Accuracy without latency/cost is incomplete evidence.
- A reranker without a measurable gain is unnecessary complexity.
- A large golden set is not automatically a good golden set; query diversity matters.
- Retrieval metrics do not prove answer correctness; evaluate grounding separately.

## Related

- [[Study Plan]]
- [[AI/01_Fundamentals/Checklist|AI Foundation Exit Gate]]
- [[AI/02_RAG-Engineering/RAG Variants and Retrieval Strategies|RAG Variants and Retrieval Strategies]]
- [[AI/07_Cross-Cutting/02_AI Evaluation|AI Evaluation]]
- [[Evidence/README|Evidence]]
