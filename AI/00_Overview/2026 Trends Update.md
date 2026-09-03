---
title: "2026 Trends Update"
category: overview
tags: [ai, trends, 2026, mcp, agentic-rag, graphrag, interview]
created: 2026-09-03
completed: false
---

# 2026 Trends Update — What Changed Since This Roadmap

> Part of [[README|00 Overview]] • `overview` • Delta on top of your 36-week plan — read before Phase 02. If an interviewer asks "are you current?" answer from here.

## Why this note

Your temporary roadmap (Weeks 1–36) is solid — this note patches it for **late-2025 / 2026** reality without breaking the sequence. Certifications reinforce building; these trends shape **how you build**.

## 6 Trends to Weave In (no phase move needed)

| # | Trend (2026) | What changed | Where to apply (no new phase) |
|---|---------------|--------------|-------------------------------|
| **1** | **MCP is standard** | Anthropic MCP (Nov 2024) → ecosystem: 1000+ servers, SSE transport, resources + prompts. No longer "additional topic" — it's **the** tool bus. | **Week 5** (`02_RAG`): use MCP `search_docs` instead of bare function schema. **Week 11**: all 7 agents via MCP. See [[AI/07_Cross-Cutting/01_MCP|MCP]]. |
| **2** | **Reasoning models** | `o1`/`o3`, Claude Sonnet 4, Gemini 2.5 Flash — explicit reasoning, higher cost, need routing. 2026 interview Q: "when to use reasoning vs fast model?" | **Week 17** ([[AI/07_Cross-Cutting/06_Multi-Model Routing|Multi-Model Routing]]): route hard/code → reasoning; fact lookup → Haiku/mini. Record cost delta. |
| **3** | **Agentic RAG + GraphRAG** | Vanilla RAG → **Agentic RAG** (planner decides retrieval strategy) + **GraphRAG** (entity graph + community detection for multi-hop). | **Week 8–9** ([[AI/02_RAG-Engineering/RAG Variants and Retrieval Strategies|RAG Variants]]): add variant `graph_retrieve()` using graph store; compare precision@k vs hybrid. |
| **4** | **AI Evaluation is gating** | LLM-as-judge (RAGAS/Phoenix) now required in AI interviews — "how do you know it works?" | **Week 6** ([[AI/07_Cross-Cutting/02_AI Evaluation|Evaluation]]): golden set + CI gate **before** Phase 03. No eval → no platform. |
| **5** | **LLM Observability = OTel** | Langfuse + Phoenix both export via OTel; traces include `retrieval.precision@k` + `faithfulness` | **Week 24** ([[AI/07_Cross-Cutting/03_LLM Observability|Observability]]): OTel collector → Langfuse + Prometheus from Day 1 of prod. |
| **6** | **Cost as first-class** | Semantic cache (Redis + vector), batching, context compression (30–50%) now interview table stakes | **Week 10** ([[AI/07_Cross-Cutting/05_Cost Optimization|Cost Optimization]]): build the `$/1k queries` table; revisit Week 34. |

## What NOT to add

- **Agent frameworks churn** — LangGraph vs AutoGen vs CrewAI: pick one in Week 11, don't chase weekly. NUS-ISS will force opinion — stick to it.
- **Training foundation models from scratch** — out of scope. This is **applied AI platform engineering** (backend + AI).
- **New cert** — no. Use these trends as **interview depth** on existing phases.

## Updated weekly deltas (patch your tracker)

- **Week 5:** Add `import from mcp import Client` — list your first MCP server.
- **Week 8:** Add column `GraphRAG precision@k` to variant table.
- **Week 10:** Add row `reasoning vs fast: cost $/1k = $8.20 vs $1.10, faithfulness +3%` — routing decision.
- **Week 14:** Add `indirect injection` test to `eval/golden_injection.jsonl`.
- **Week 24:** Add `semantic_cache_hit_rate` to Grafana.

## Interview line for "are you current?"

> "Since late 2024, MCP standardized tool integration — we run all 7 agents via MCP. We measure RAG with RAGAS on a golden set gated in CI, observe via OTel into Langfuse/Phoenix, and route reasoning vs fast models by eval'd faithfulness vs cost. GraphRAG is a variant we A/B'd in Week 8 with modest gains on multi-hop queries."

## Related

- [[Roadmap Overview]] • [[Weekly Tracker]] • [[Tech Stack]] • [[AI/07_Cross-Cutting/README|07 Cross-Cutting]] • [[Certification Guide]]

---
*Category: overview • 2026-trends*
