---
title: "LLM APIs"
category: fundamentals
tags: [ai, llm, api, streaming]
weeks: "2"
created: 2026-09-02
completed: false
---

# LLM APIs

> Part of [[README|01_Fundamentals]] • `fundamentals` • Week 2

## Intent

Call managed LLM APIs reliably: retries, streaming, fallback, cost tracking.

## Key Points

- Providers: OpenAI, Anthropic (Claude), Gemini — unified via thin adapter (see [[AI/07_Cross-Cutting/06_Multi-Model Routing|Multi-Model Routing]]).
- Must handle: rate limits (429), timeouts, streaming partials, token counting.
- Track usage per request for cost optimization.

## Code Example

```python
import openai, tenacity

client = openai.AsyncOpenAI()

@tenacity.retry(stop=tenacity.stop_after_attempt(3), wait=tenacity.wait_exponential())
async def chat_with_retry(messages: list[dict]) -> str:
    resp = await client.chat.completions.create(
        model="gpt-4o-mini", messages=messages, temperature=0.2
    )
    return resp.choices[0].message.content
```

## Pros / Cons

| Pros | Cons |
|------|------|
| No infra, fast iteration | Vendor lock-in, per-token cost |
| Always latest models | Rate limits, data governance concerns |

## Vs Table

| Aspect | Managed API | Self-hosted (open-weight) |
|--------|-------------|---------------------------|
| Cost | Pay per token | GPU infra + ops |
| Latency | Network bound | Colocation possible |
| Control | Limited | Full (fine-tuning, privacy) |

Trade-off analysis deepens in [[AI/02_RAG-Engineering/02_Design LLM Architectures|02_Design LLM Architectures]].

## Interview Q&A

- **Q:** How to handle 429? **A:** Exponential backoff + jitter, plus token bucket rate limiting client-side.
- **Q:** How to estimate cost? **A:** Count input/output tokens per call; dashboard in [[AI/07_Cross-Cutting/05_Cost Optimization|Cost Optimization]].

## Pitfalls

- Logging raw prompts with PII. Redact before observability.

## Related

- [[04_Prompt Engineering]] • [[05_Structured Outputs]] • [[AI/07_Cross-Cutting/05_Cost Optimization|Cost Optimization]]

---
*Category: fundamentals*
