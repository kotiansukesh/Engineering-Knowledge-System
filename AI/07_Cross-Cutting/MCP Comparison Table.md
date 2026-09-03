---
title: "MCP Comparison Table"
category: cross-cutting
tags: [ai, comparison, rag]
created: 2026-09-02
---

# Cross-Phase Comparison Tables

## 1. Reranker vs No-Reranker

| Scenario | Retrieval Only | +Reranker (cross-encoder) | Delta |
|----------|---------------|--------------------------|-------|
| **Precision@5** | ~0.45 on keyword-heavy queries | ~0.55–0.60 | +15–25% |
| **Latency per query** | 80–120 ms (vector only) | 180–250 ms (+80–120 ms) | +80–120 ms |
| **Cost per query** | embedding-only + 1 LLM call | embedding + reranker call + 1 LLM call | +30–50% tokens |
| **When to choose** | Summarization, open-ended chat, high-throughput UI | High-stakes QA, legal/medical, exact-answer required | — |
| **When to skip** | Latency-sensitive real-time chat, bulk ingestion | When precision gain doesn't justify cost/latency | — |

*Fill in your own numbers from Phase 02 experiments.*

## 2. pgvector vs Dedicated Vector DB

| Aspect | pgvector (PostgreSQL) | Qdrant / Weaviate |
|--------|----------------------|-------------------|
| **Deployment** | Single DB, no extra container | Separate service, Helm chart or managed |
| **Scale** | ~10k–50k vectors (depends on hardware) | >100k, horizontal scale |
| **Transactions** | Full ACID, joins, filtering in SQL | Eventually consistent, limited SQL-like filters |
| **Payload size** | JSONB columns, moderate | Dedicated payload fields, larger |
| **Ops overhead** | None new if PG already running | New service: monitor, scale, upgrade, backups |
| **Cost** | $0 if PG already running | $0.50–$2.00 / month per GB + VM/containers |
| **When to choose** | Existing PG estate, <50k vectors, need SQL joins | Growing beyond 50k, multi-tenant, need advanced vector features |
| **When to skip** | Prototype / early phases, keeping stack minimal | Production at scale with many tenants |

*Populate with your own benchmark numbers.*

## 3. Managed API vs Self-Hosted Cost

| Dimension | Managed (OpenAI/Anthropic) | Self-Hosted (Llama-3-8B via Ollama/Oobabooga) |
|-----------|----------------------------|-----------------------------------------------|
| **$/1k tokens** | $0.00015 – $0.03 (model-dependent) | $0.10 – $0.50 (GPU hourly + electricity) |
| **Latency** | 200–800 ms (network + provider) | 500–2000 ms (depends on GPU, batch size) |
| **Model updates** | Instant (provider handles) | You rebuild container, pin version |
| **Rate limits** | Provider-enforced (e.g. 350 RPM) | Your infra limit (can over-provision) |
| **Data governance** | Provider stores prompts unless you opt-out | Full control, on-prem if needed |
| **When to choose** | Prototype, <5M tokens/month, want fastest iteration | >5M tokens/month, compliance, cost optimization |
| **Break-even** | ≈ 5M tokens / month → self-host cheaper after | — |

*Replace with your actual token counts and cloud spend.*