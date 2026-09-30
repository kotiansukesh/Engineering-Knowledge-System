---
title: "Kubernetes Auto-scaling for AI"
category: "AI/05_Kubernetes-Operations"
tags: [kubernetes, autoscaling, hpa, keda, gpu, scaling]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
reviewed: "2026-09-30"
sr-due: "2026-10-05"
type: "note"
---

# Kubernetes Auto-scaling for AI

## Intent
Select scaling signals and mechanisms that keep AI services within latency and cost targets under changing demand.

## Scaling Model
**Demand → queue → replicas/capacity → warm-up → capacity → latency**

AI workloads often make CPU a weak scaling signal. Queue depth, request concurrency, tokens/sec, GPU utilization, or provider quota may better represent the real bottleneck.

## Choices
| Mechanism | Best fit | Important limitation |
|---|---|---|
| HPA | request/CPU/custom metrics | reacts after demand changes |
| KEDA | event/queue-driven workloads | depends on reliable event metrics |
| VPA | resource recommendation/adjustment | can conflict with latency-sensitive serving patterns |
| Scale-to-zero | sparse workloads | cold-start/model-load latency |
| Predictive/pre-warming | predictable traffic | forecast error and idle cost |

## Decision Rule
Scale on the metric closest to the resource constraint that can be measured reliably. For asynchronous inference, queue age/depth is often more actionable than CPU; for synchronous serving, concurrency and latency may be better.

## Failure Modes
1. Oscillation → stabilization windows and sensible scale-down delays.
2. Cold-start spike → pre-warm capacity or minimum replicas.
3. Scaling on CPU while GPU is saturated → use GPU/queue-aware signals.
4. Metrics outage → define safe minimum capacity and alert.
5. Provider rate limit → scaling replicas cannot create provider capacity; enforce quotas and backpressure.

## Evaluation
Measure scale reaction time, p95/p99 latency, queue age, replica churn, GPU utilization, cold-start frequency, and cost per successful request.

## Practice
- [ ] Define a scaling signal for synchronous inference.
- [ ] Define one for asynchronous inference.
- [ ] Inject a sudden traffic spike and measure reaction time.
- [ ] Inject metrics loss and observe fallback behavior.
- [ ] Compare minimum-replica cost with cold-start latency.

## Senior Interview Prompts
1. Why can CPU-based HPA fail for GPU inference?
2. What causes autoscaling oscillation?
3. Why does scale-to-zero change the latency SLO?
4. How does provider rate limiting interact with replica scaling?
5. What evidence would justify predictive scaling?

## Flashcards
#flashcard
**Q:** What should an AI autoscaler measure? :: **A:** The metric closest to the actual bottleneck—often queue depth/age, concurrency, latency, tokens/sec, or GPU capacity rather than CPU alone.
