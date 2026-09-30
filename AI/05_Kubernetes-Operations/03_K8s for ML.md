---
title: "Kubernetes for ML"
category: "AI/05_Kubernetes-Operations"
tags: [kubernetes, ml, gpu, operator, scheduling]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
reviewed: "2026-09-30"
sr-due: "2026-10-03"
type: concept
---

# Kubernetes for ML

## Intent
Understand the Kubernetes primitives and platform components needed to run GPU-backed training and inference workloads reliably.

## Architecture
~~~~mermaid
flowchart LR
P[Pod] --> N[Node]
N --> G[GPU device plugin/operator]
P --> R[Resource requests/limits]
P --> Q[Quota]
N --> T[Topology / placement]
~~~~

## Decision Rule
Use Kubernetes for ML when shared scheduling, isolation, deployment automation, or platform standardization outweighs its operational complexity. For a small team with one managed endpoint, a managed inference service may be simpler.

## Core Mechanisms
- GPU device plugins expose allocatable GPU resources to Kubernetes.
- Resource requests participate in scheduling; they are not a guarantee that a model fits in GPU memory.
- Node labels, taints/tolerations, affinity, and topology rules constrain placement.
- Operators can automate GPU/runtime lifecycle but add another control plane dependency.
- Quotas prevent one workload/team from consuming the entire cluster.

## Real Trade-offs
| Decision | Option A | Option B | Choose based on |
|---|---|---|---|
| Platform | K8s GPU cluster | Managed ML service | operational ownership vs control |
| Placement | General scheduling | Affinity/topology rules | locality, GPU type, network/storage needs |
| Isolation | Namespace/quota | Dedicated cluster/node pool | blast radius and utilization |
| GPU sharing | Exclusive GPU | MIG/time-slicing | workload isolation vs utilization |

## Failure Modes
1. Pod pending → inspect resource availability, taints, affinity, and quota before changing the image.
2. GPU visible but OOM → scheduler allocation does not prove model memory fit.
3. Node fragmentation → bin-packing/requests may leave unusable GPU capacity.
4. Noisy neighbor → quotas, dedicated pools, or stronger isolation.
5. Operator upgrade breaks workloads → version and test operator/runtime combinations.

## Evaluation
Measure GPU utilization, pending time, scheduling latency, utilization per allocated GPU, job completion rate, failure rate, and cost per successful training/inference workload.

## Practice
- [ ] Deploy a GPU-requesting pod and inspect scheduler events.
- [ ] Add node affinity for a GPU class.
- [ ] Apply namespace resource quotas.
- [ ] Simulate a pending pod caused by insufficient GPU capacity.
- [ ] Compare exclusive GPU allocation with a sharing strategy for two representative workloads.

## Senior Interview Prompts
1. Why can a GPU pod remain Pending when GPUs exist in the cluster?
2. What does a device plugin/operator actually provide?
3. How do quotas and taints solve different problems?
4. When is Kubernetes the wrong abstraction for ML serving?
5. How do you diagnose poor GPU utilization?

## Flashcards
#flashcard
**Q:** Does requesting one GPU guarantee that the model fits in GPU memory? :: **A:** No. Scheduling allocates a resource; model memory requirements, KV cache, framework overhead, and concurrency still determine fit.

#flashcard
**Q:** What is the purpose of taints and tolerations? :: **A:** Taints repel workloads from selected nodes; tolerations allow specific workloads to be scheduled there.
