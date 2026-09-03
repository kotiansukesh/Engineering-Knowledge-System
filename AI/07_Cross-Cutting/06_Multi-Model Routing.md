---
title: "Multi-Model Routing"
category: cross-cutting
tags: [ai, routing, multi-model, fallback, interview, 2026-trend]
created: 2026-09-02
updated: 2026-09-03
completed: false
---

# Multi-Model Routing — GPT/Claude/Gemini/Open-Weights

> Part of [[README|07_Cross-Cutting]] • `cross-cutting` • From **Phase 04 (Week 17+)** — the AI Gateway's brain: route by **latency / capability / cost** with fallback.

## Intent

Dynamically choose the cheapest capable model per query (e.g., Haiku for fact lookup, Sonnet for coding, Gemini for long context, self-hosted Llama for cheap bulk) — with **fallbacks** on 429/timeout.

## When to Use / NOT

| Use | Avoid |
|-----|-------|
| Platform serves varied workloads (search vs code vs QA) | Single model suffices (toy) — static `model="gpt-4o-mini"` cheaper to operate |
| Need cost/latency SLOs across tenants | Routing without eval — mis-routes hard queries to weak model |

## Runnable Code — Router + Fallback (Python)

```python
# config: cost/latency/capability table — 2026 snapshot
MODELS = {
    "haiku":   {"cost":0.25, "latency":400, "cap":"fast-fact", "provider":"anthropic"},
    "sonnet":  {"cost":3.0,  "latency":900, "cap":"code/reasoning", "provider":"anthropic"},
    "gpt-4o-mini":{"cost":0.15,"latency":500,"cap":"fast-fact","provider":"openai"},
    "gpt-4o":  {"cost":2.5, "latency":1100,"cap":"reasoning","provider":"openai"},
    "gemini-2.5-flash":{"cost":0.3,"latency":600,"cap":"long-context","provider":"google"},
    "llama-3.3-70b":{"cost":0.1, "latency":800,"cap":"bulk","provider":"self-host"},
}
# 1) Classifier — rule + tiny model
def route(query: str, domain: str) -> str:
    if len(query) > 8000: return "gemini-2.5-flash"  # long context
    if domain == "code":  return "sonnet"
    if is_simple_fact(query): return "haiku"  # or gpt-4o-mini — A/B via eval
    return "gpt-4o-mini"

# 2) Fallback chain — retry cheaper on failure
FALLBACK = {"sonnet":["haiku","gpt-4o-mini"], "gpt-4o":["gpt-4o-mini","haiku"]}

async def ask_resilient(query: str):
    model = route(query, domain="search")
    for m in [model] + FALLBACK.get(model, []):
        try:
            with tracer.start_as_current_span("llm", attributes={"llm.model": m}):
                return await llm.chat.completions.create(model=m, messages=build(query))
        except (RateLimitError, TimeoutError):
            continue
    raise RuntimeError("all fallbacks exhausted")
```

**Gateway wiring (Phase 04):** Router lives in `api/gateway/router.py`; reads per-tenant policy from config; emits `llm.model` span + cost metric to Langfuse/Prometheus.

## Pros / Cons

| Pros | Cons |
|------|------|
| 30–50% cost cut vs single frontier model | Classifier errors — gate via eval harness |
| Long-context → Gemini, code → Sonnet | Vendor sprawl — pin versions, handle per-provider quirks |
| Fallback survives 429 without user error | Need unified message schema |

## How It Compares

|  | Single Model (gpt-4o) | Router (this note) | Cascading (small→large on fail) |
|--|---|---|---|
| Cost | High, flat | 30–50% lower (eval-gated) | Medium (extra call on fail) |
| Latency | p95 fixed | p50 lower (cheap hits) | p95 higher |
| Use | MVP | Platform (Weeks 17+) | Simple fallback-only |

## Interview Q&A

**Q: How do you decide the route?**  
Classifier: `is_simple_fact()` (regex + 1k training set) + domain + context length; validate via weekly eval — faithfulness must not drop >1% vs frontier.

**Q: Open-weight when?**  
Bulk ingest, offline judge, or tenants with data-residency; self-host Llama on K8s (Phase 05) — cost $0.10/1M vs $2.50.

**Q: Fallback vs routing?**  
Routing = choose **before** call; fallback = retry **after** failure. Use both — router picks Sonnet, fallback to Haiku on 429.

**Q: How to A/B test?**  
Langfuse experiment: 10% traffic to candidate route, compare `faithfulness`, `cost_per_1k`, `p95` — promote if cost ↓ and faithfulness ≥ baseline.

## Pitfalls

- Routing without eval — hard queries on cheap model hallucinate; gate with [[02_AI Evaluation|Evaluation]].
- No provider abstraction — `openai` vs `anthropic` message formats differ; wrap in unified `ask()` adapter.
- No fallback — single vendor outage = outage; ship fallback Day 1.

## Related

- [[05_Cost Optimization|Cost Optimization]] • [[03_LLM Observability|Observability]] • [[02_AI Evaluation|Evaluation]] • [[AI/04_Production-Platform/01_AI Gateway|AI Gateway]] • [[AI/06_Architecture-Governance/01_SWARC4AI Syllabus|SWARC4AI]]

---
*Category: cross-cutting • Interview-ready*
