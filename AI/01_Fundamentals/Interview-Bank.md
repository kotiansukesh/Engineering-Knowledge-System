---
title: "Interview Bank — AI Fundamentals"
category: revision
tags: [ai-fundamentals, interview, revision]
created: 2026-09-23
completed: false
reviewed: ""
sr-due: ""
problems-solved: []
problems-solved-dates: {}
excalidraw: ""
---

# Interview Bank — AI Fundamentals (Phase 01)

> Curated index of killer questions from [[01_Fundamentals/README|01_Fundamentals]] notes. Each links to source note for full answer.

---

## LLM Fundamentals

| # | Question | Source |
|---|---|---|
| 1 | Walk me through a single transformer forward pass, from tokens to logits. Where would you inject a steering vector? | [[01_LLM Fundamentals]] |
| 2 | Why does causal attention use a triangular mask? What breaks if you remove it? | [[01_LLM Fundamentals]] |
| 3 | Explain RoPE. Why not learned absolute positions? | [[01_LLM Fundamentals]] |
| 4 | What are Chinchilla scaling laws? How do they guide training compute allocation? | [[01_LLM Fundamentals]] |
| 5 | How does KV caching work? Memory cost for 32k context on Llama-3-70B? | [[01_LLM Fundamentals]] |

---

## Embeddings & Vector Search

| # | Question | Source |
|---|---|---|
| 1 | How does HNSW achieve sub-linear search? Key parameters (M, efConstruction, efSearch)? | [[02_Embeddings and Vector Search]] |
| 2 | When does cosine similarity fail as a relevance signal? (Anisotropy, length bias, domain mismatch) | [[02_Embeddings and Vector Search]] |
| 3 | Explain Product Quantization. How does it reduce memory? | [[02_Embeddings and Vector Search]] |
| 4 | How do you evaluate retrieval quality offline? (Recall@k, nDCG@k, MRR, latency/recall curve) | [[02_Embeddings and Vector Search]] |
| 5 | Design hybrid retrieval for enterprise RAG (10M docs, p99 < 100ms). | [[02_Embeddings and Vector Search]] |

---

## LLM APIs

| # | Question | Source |
|---|---|---|
| 1 | Design a resilient LLM client: rate limits, timeouts, provider failures, fallbacks. | [[03_LLM APIs]] |
| 2 | How do you implement structured output reliably across providers (OpenAI, Anthropic, Vertex, self-hosted)? | [[03_LLM APIs]] |
| 3 | Explain the cost model for LLM APIs. Optimization strategies? | [[03_LLM APIs]] |
| 4 | How do you handle streaming responses in a synchronous API? | [[03_LLM APIs]] |
| 5 | Strategy for provider deprecation / model sunset? | [[03_LLM APIs]] |

---

## Prompt Engineering

| # | Question | Source |
|---|---|---|
| 1 | System vs user prompt — difference and why it matters? | [[04_Prompt Engineering]] |
| 2 | How do you test prompts systematically? (Golden set, LLM-as-judge, regression suite) | [[04_Prompt Engineering]] |
| 3 | Chain-of-thought — when does it help vs hurt? | [[04_Prompt Engineering]] |
| 4 | Few-shot vs zero-shot — decision rule? | [[04_Prompt Engineering]] |
| 5 | How do you prevent prompt injection? | [[04_Prompt Engineering]] |

---

## Structured Outputs

| # | Question | Source |
|---|---|---|
| 1 | What if LLM returns invalid JSON? | [[05_Structured Outputs]] |
| 2 | JSON mode vs tool calling — when to use which? | [[05_Structured Outputs]] |
| 3 | How do you handle schema drift across model versions? | [[05_Structured Outputs]] |
| 4 | `additionalProperties: false` — when to use? | [[05_Structured Outputs]] |
| 5 | Structured output vs answer-level eval — which catches what? | [[05_Structured Outputs]] |

---

## Tool Calling

| # | Question | Source |
|---|---|---|
| 1 | Tool calling vs RAG — what's the difference? | [[06_Tool Calling]] |
| 2 | How to prevent infinite tool loops? | [[06_Tool Calling]] |
| 3 | Parallel vs sequential tool calls — when to use which? | [[06_Tool Calling]] |
| 4 | MCP vs provider tool calling — what changes? | [[06_Tool Calling]] |
| 5 | How do you validate tool arguments without slowing down? | [[06_Tool Calling]] |

---

## FastAPI Backend

| # | Question | Source |
|---|---|---|
| 1 | How to stream LLM tokens via FastAPI? | [[02_FastAPI Backend]] |
| 2 | FastAPI vs Spring for AI services? | [[02_FastAPI Backend]] |
| 3 | Dependency injection — why does it matter for LLM clients? | [[02_FastAPI Backend]] |
| 4 | How do you handle backpressure when streaming to slow clients? | [[02_FastAPI Backend]] |
| 5 | What's the scaling model for FastAPI in production? | [[02_FastAPI Backend]] |

---

## AI Backend Template (Project)

| # | Question | Source |
|---|---|---|
| 1 | Why start every AI project from a schema-first template? | [[AI Backend Template]] |
| 2 | What would you remove from this template for a real service? | [[AI Backend Template]] |
| 3 | How do you keep four mini-projects from forking four templates? | [[AI Backend Template]] |
| 4 | Minimum viable feature set for this template? | [[AI Backend Template]] |
| 5 | How does this template evolve into Enterprise Document Search (Phase 02)? | [[AI Backend Template]] |

---

## Phase 01 Checklist (Gates)

| # | Question | Source |
|---|---|---|
| 1 | How do you know your AI backend is production-shaped rather than a notebook? | [[Checklist]] |
| 2 | Why gate tool calling separately from structured output? | [[Checklist]] |
| 3 | What would you add to this checklist after Phase 02? | [[Checklist]] |
| 4 | How do you handle the "it works on my machine" problem? | [[Checklist]] |
| 5 | What's the cost of skipping a gate? | [[Checklist]] |

---

## Prompt Playground (Project)

| # | Question | Source |
|---|---|---|
| 1 | Difference between prompt playground and eval harness? | [[Prompt Playground]] |
| 2 | How do you stop prompt changes being made on taste? | [[Prompt Playground]] |
| 3 | Why build one when providers offer consoles? | [[Prompt Playground]] |
| 4 | Minimal feature set for a useful playground? | [[Prompt Playground]] |
| 5 | How do you handle prompt versioning across model upgrades? | [[Prompt Playground]] |

---

## AI Coding Assistant (Project)

| # | Question | Source |
|---|---|---|
| 1 | How did you scope what the coding assistant was allowed to do? | [[AI Coding Assistant]] |
| 2 | How do you know its answers are grounded? | [[AI Coding Assistant]] |
| 3 | What is the real cost of an unscoped coding assistant? | [[AI Coding Assistant]] |
| 4 | How do you handle context budget for large repos? | [[AI Coding Assistant]] |
| 5 | Why structured output instead of free text? | [[AI Coding Assistant]] |

---

[[AI/README|← Back to AI MOC]] • [[AI/99_Revision/Interview-Bank|Master Interview Bank]]