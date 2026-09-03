---
title: "AI Gateway (C3 — Resilient Microservices)"
category: production
tags: [ai, gateway, resilience, 12-factor]
weeks: "17-18"
created: 2026-09-02
completed: false
---

# AI Gateway — Coursera C3

> Part of [[README|04_Production-Platform]] • `production` • Weeks 17–18

## Intent

12-factor LLM gateway: config, statelessness, disposability, logs — plus fault tolerance for non-deterministic AI calls.

## Key Topics (C3)

- 12-factor app methodology applied to LLM services.
- Fault tolerance: timeouts, retries (exponential + jitter), **circuit breakers**, **rate limiting**, **caching** (semantic cache).
- AI Gateway patterns: auth, model routing, fallback models, request hedging.

## Architecture

```
Client → AI Gateway (FastAPI/Envoy) → [Model Router → OpenAI | Claude | Gemini | open-weight]
                 ├─ Rate limiter (Redis token bucket)
                 ├─ Circuit breaker (per-provider)
                 ├─ Semantic cache (Redis + vector)
                 └─ Prometheus metrics + OTel traces
```

## Code Sketch

```python
from tenacity import retry, wait_exponential, stop_after_attempt
import redis.asyncio as redis

@retry(wait=wait_exponential(multiplier=0.5, max=4), stop=stop_after_attempt(3))
async def call_llm_with_gateway(model: str, messages: list):
    # gateway handles routing + fallback
    return await gateway.chat(model=model, messages=messages)

# circuit breaker pseudo
if breaker.is_open("openai"):
    return await gateway.chat(model="claude-haiku", messages=messages)
```

## Interview Q&A

- **Q:** Why circuit breaker for LLM? **A:** Provider outages cascade; breaker fails fast to fallback model.
- **Q:** Semantic cache? **A:** Embed query → if cosine > threshold, return cached answer — saves tokens. See [[AI/07_Cross-Cutting/05_Cost Optimization|Cost Optimization]].

## Related

- [[02_AI TDD and Evaluation]] • [[03_gRPC and Observability]] • [[AI/07_Cross-Cutting/05_Cost Optimization|Cost Optimization]]

---
*Category: production*
