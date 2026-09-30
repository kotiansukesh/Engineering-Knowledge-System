---
title: "Batching and Caching"
category: "AI/04_Production-Platform"
tags: [serving, batching, caching, kv-cache, prefix-caching]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
reviewed: "2026-09-30"
sr-due: "2026-10-03"
type: concept
---

# Batching and Caching

## Intent
Choose batching and cache strategies that improve throughput or latency without violating correctness, freshness, isolation, or memory budgets.

## Decision Model
**Batching** combines work to improve hardware utilization. **Caching** avoids repeating work. They solve different problems and must be evaluated separately.

## Batching
| Strategy | Benefit | Risk |
|---|---|---|
| Static batch | simple high utilization for fixed workloads | waits for batch boundary |
| Dynamic batch | adapts to arrivals | scheduler complexity |
| Continuous batching | strong utilization for autoregressive generation | more complex scheduling |

## Caching
| Cache | Reuse target | Main correctness question |
|---|---|---|
| Exact response cache | identical requests | is response still valid? |
| Semantic cache | similar requests | are requests safely equivalent? |
| Prefix/KV cache | shared prompt prefixes | is prefix identical and reusable? |
| Application/data cache | deterministic external data | freshness/authorization |

## Decision Rule
Cache only when the reuse key captures the inputs that affect correctness. Do not use semantic similarity as proof that two requests have the same authorized or current answer.

## Failure Modes
1. Stale answer → TTL/version invalidation.
2. Cross-user data leak → include tenant/authorization context in cache identity.
3. Low hit rate → measure before adding cache complexity.
4. Cache stampede → request coalescing or bounded refresh.
5. Memory pressure → size limits and eviction policy.
6. Batch starvation → maximum wait time and fair scheduling.

## Evaluation
Measure cache hit rate, saved compute/tokens, stale-result rate, p50/p95 latency, batch size distribution, queue wait, GPU utilization, and cost per successful request.

## Practice
- [ ] Add an exact response cache with a correctness-aware key.
- [ ] Measure hit rate on a realistic workload.
- [ ] Inject stale data and verify invalidation.
- [ ] Compare dynamic vs continuous batching under mixed request lengths.
- [ ] Simulate a cache stampede.

## Senior Interview Prompts
1. Why is semantic caching harder than exact caching?
2. How can caching create a security problem?
3. When does batching improve throughput but hurt latency?
4. How do you choose a TTL?
5. What evidence justifies prefix/KV caching?

## Flashcards
#flashcard
**Q:** What must a cache key represent? :: **A:** Every input that can change correctness, freshness, or authorization of the result.

#flashcard
**Q:** Why can batching hurt tail latency? :: **A:** Requests may wait for batch formation or interact with heterogeneous request lengths, increasing queueing and scheduling delay.
