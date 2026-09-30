---
title: AI Gateway
category: AI/04_Production-Platform
tags: [ai, gateway, resilience, routing]
created: 2026-09-30
completed: false
reviewed: "2026-09-29"
sr-due: "2026-09-30"
difficulty: Medium
type: concept
weeks: 9
---

# AI Gateway

## Intent

Provide one policy boundary for provider routing, quotas, resilience, observability, and cost controls when multiple services consume models.

## Architecture

```
Client → AI Gateway → policy/routing → Provider A/B
                    ├→ quota/rate limit
                    ├→ timeout/retry/circuit breaker
                    ├→ telemetry
                    └→ fallback/degradation
```

## When to Use / When Not

- **Use:** multiple services/providers need consistent policy and observability.
- **Avoid:** a single small prototype where the gateway adds a failure hop without solving a real problem.

## Real Trade-offs

| Decision | Benefit | Cost / Risk | Evidence to collect |
|---|---|---|---|
| Central gateway | Consistent policy | New critical dependency | gateway availability + latency |
| Provider routing | Cost/quality control | Wrong route can reduce quality | task-level eval by route |
| Semantic cache | Lower repeated cost/latency | Stale/wrong reuse | hit rate + cache correctness |
| Provider fallback | Better resilience | Different output quality | fallback success + quality delta |

## Failure Modes

- retry storms
- circuit breaker never recovering
- cache returning stale results
- tenant quota starvation
- hidden provider rate limits

## Practice

Implement one provider adapter, one timeout policy, one quota, and one fallback. Load-test the gateway and record p95/p99 latency, error rate, provider failures, and cost per successful request.
