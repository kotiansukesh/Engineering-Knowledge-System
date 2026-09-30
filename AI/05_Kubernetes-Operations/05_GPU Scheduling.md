---
title: "GPU Scheduling"
category: "AI/05_Kubernetes-Operations"
tags: [kubernetes, gpu-scheduling, mig, topology, bin-packing]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
reviewed: "2026-09-30"
sr-due: "2026-10-04"
type: "note"
---

# GPU Scheduling

## Intent
Choose GPU allocation and placement strategies that balance isolation, utilization, latency, and cost.

## Scheduling Choices
| Strategy | Benefit | Cost/Risk |
|---|---|---|
| Exclusive GPU | strong isolation/predictability | lower utilization for small workloads |
| MIG | hardware partitioning on supported GPUs | capacity fragmentation and configuration constraints |
| Time-slicing | shares a GPU across workloads | contention and weaker isolation |
| Topology-aware placement | better locality | fewer placement options |

## Decision Rule
Prefer the simplest allocation model that meets workload isolation and performance requirements. Sharing is attractive for small/bursty workloads; exclusive allocation is easier to reason about for latency-sensitive or memory-heavy workloads.

## Capacity Model
Track at least:
- GPU count and type
- allocatable partitions
- requested vs actual memory
- utilization over time
- queue/pending duration
- workload latency
- failure/OOM rate

A GPU can be highly allocated but poorly utilized. Measure useful work, not only allocation percentage.

## Failure Modes
1. Fragmentation → compatible workloads and placement policies; periodically review node pools.
2. Contention → isolate latency-sensitive workloads.
3. Wrong GPU class → explicit node selection and validation.
4. Topology mismatch → inspect locality requirements before forcing affinity.
5. Sharing hides memory pressure → monitor per-workload failure and latency, not only device utilization.

## Evaluation
Compare strategies using utilization, p95 latency, queue time, OOM rate, throughput, and cost per successful request/job.

## Practice
- [ ] Run two workloads with different GPU memory profiles.
- [ ] Compare exclusive and shared allocation.
- [ ] Create a placement rule for a GPU class.
- [ ] Inject contention and observe tail latency.
- [ ] Document the allocation decision with measured evidence.

## Senior Interview Prompts
1. When does MIG help and when does it create fragmentation?
2. Why can time-slicing hurt latency?
3. What metrics reveal poor bin-packing?
4. How do topology constraints affect scheduling?
5. What is more useful than raw GPU utilization for cost analysis?

## Flashcards
#flashcard
**Q:** What is the core trade-off in GPU sharing? :: **A:** Higher utilization/capacity efficiency versus contention, predictability, and isolation.

#flashcard
**Q:** Why is allocated GPU percentage insufficient? :: **A:** A fully allocated GPU can still be idle or blocked by memory/queue constraints; useful throughput and latency must be measured.
