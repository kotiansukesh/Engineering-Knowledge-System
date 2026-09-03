---
title: "AI TDD and Evaluation (C4 — Refactor and Test)"
category: production
tags: [ai, tdd, testing, evaluation]
weeks: "19-20"
created: 2026-09-02
completed: false
---

# AI TDD and Evaluation — Coursera C4

> Part of [[README|04_Production-Platform]] • `production` • Weeks 19–20

## Intent

Apply TDD and systematic refactoring to **non-deterministic** LLM services — test behavior, not string equality.

## Key Topics (C4)

- TDD for LLM microservices: schema tests, golden-set eval, LLM-as-judge, regression testing.
- Refactoring: extract prompt templates, version schemas, isolate LLM calls behind interfaces for mocking.
- Hallucination detection, faithfulness scoring.

## What to Test

| Layer | Test Type | Tool |
|-------|-----------|------|
| Schema | `Answer.model_validate` passes | Pydantic + pytest |
| Retrieval | precision@k on golden set | [[AI/07_Cross-Cutting/02_AI Evaluation\|Evaluation]] harness |
| Answer | Faithfulness / hallucination rate | LLM-as-judge |
| Regression | Diff vs baseline on 100 queries | Snapshot tests |

## Code Sketch

```python
def test_structured_output():
    raw = llm.generate(prompt, schema=Answer)
    parsed = Answer.model_validate_json(raw)
    assert parsed.citations  # must cite

def test_retrieval_regression(golden_set):
    for q, expected_ids in golden_set:
        got = await search(q)
        assert precision_at_k(got, expected_ids, k=5) >= 0.8
```

## Interview Q&A

- **Q:** How to TDD an LLM feature? **A:** Write eval (golden Q→A + metrics) first, then iterate prompt/retrieval until eval passes — eval is the "test."

## Related

- [[01_AI Gateway]] • [[AI/07_Cross-Cutting/02_AI Evaluation|AI Evaluation]] • [[AI/07_Cross-Cutting/03_LLM Observability|Observability]]

---
*Category: production*
