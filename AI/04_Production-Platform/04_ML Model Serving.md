---
title: "ML Model Serving"
category: "AI/04_Production-Platform"
tags: [serving, inference, vllm, triton, llm]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
reviewed: "2026-09-30"
sr-due: "2026-10-02"
type: "note"
---

# ML Model Serving

## Intent
Understand the serving boundary for self-hosted models: request scheduling, batching, KV-cache pressure, GPU utilization, streaming, and operational failure handling.

## Architecture
~~~~mermaid
flowchart LR
C[Client] --> G[Gateway] --> S[Inference server]
S --> Q[Scheduler / batcher] --> GPU[Model + KV cache]
GPU --> S --> G --> C
S --> M[Metrics + traces]
~~~~

## Decision Rule
Choose managed/provider inference when operational ownership is not a differentiator. Self-host when latency control, data residency, model customization, throughput economics, or deployment constraints justify the operational burden.

## Serving Choices
| Requirement | Candidate | Key evidence |
|---|---|---|
| Standard hosted model | Provider API | latency, price, residency |
| Self-hosted LLM inference | vLLM/TGI-class server | throughput, compatibility, GPU utilization |
| Multi-model serving | Triton-style platform | model mix and scheduling requirements |
| Custom inference graph | Specialized runtime | measurable kernel/latency need |

## Core Mechanisms
- **Continuous batching:** admits requests as sequences finish instead of waiting for a fixed batch boundary.
- **KV cache:** stores attention state for generated sequences; long contexts and concurrent requests increase memory pressure.
- **Streaming:** improves time-to-first-token/user perception but does not reduce total compute by itself.
- **Admission control:** protects the system when demand exceeds GPU capacity.

## Trade-offs
| Decision | Option A | Option B | Choose based on |
|---|---|---|---|
| Hosting | Managed | Self-hosted | operational burden vs control/economics |
| Scheduling | Simple batching | Continuous batching | workload shape and utilization |
| Model replicas | More replicas | Larger shared pool | isolation vs utilization |
| Context length | Shorter limit | Longer limit | product need vs KV memory/latency |

## Failure Modes
1. GPU OOM → cap context/concurrency and enforce admission control.
2. Queue explosion → bounded queue, load shedding, backpressure.
3. Slow model → inspect token generation latency separately from queue latency.
4. Replica imbalance → measure per-replica queue depth and utilization.
5. Warm-up spikes → readiness only after model initialization and health checks.
6. Provider/runtime incompatibility → pin tested model/runtime combinations.

## Evaluation
Benchmark with representative prompt lengths and output lengths. Record time-to-first-token, inter-token latency, p50/p95/p99 latency, tokens/sec, queue time, GPU utilization, memory headroom, error rate, and cost per successful request.

## Practice
- [ ] Load-test short and long contexts separately.
- [ ] Increase concurrency until queueing becomes the dominant latency component.
- [ ] Inject GPU saturation and verify load shedding.
- [ ] Compare one large replica with multiple smaller replicas using the same workload.
- [ ] Document the self-host vs provider decision using measured evidence.

## Senior Interview Prompts
1. Why can higher GPU utilization increase latency?
2. What is the relationship between context length, KV cache, and concurrency?
3. How do you distinguish queue latency from model latency?
4. When does self-hosting stop making economic sense?
5. How would you design graceful degradation under GPU exhaustion?

## Flashcards
#flashcard
**Q:** What are the two major latency components before generation work? :: **A:** Queue/scheduling delay and model inference time; measure them separately.

#flashcard
**Q:** Why does KV-cache pressure matter for concurrent LLM serving? :: **A:** Each active sequence consumes memory for attention state, so concurrency and context length can become memory limits before raw compute does.
