---
title: "Kubernetes Cost Management"
category: "AI/05_Kubernetes-Operations"
tags: [kubernetes, cost, finops, gpu, rightsizing]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
reviewed: "2026-09-30"
sr-due: "2026-10-06"
type: "note"
---

# Kubernetes Cost Management

## Intent
Turn cluster and GPU consumption into unit economics that can guide capacity, architecture, and workload decisions.

## Cost Model
**Infrastructure cost / useful workload output = unit cost**

Useful output might be successful inference requests, generated tokens, training runs, or completed jobs. Raw GPU-hour spend alone is not enough.

## Cost Levers
| Lever | Benefit | Risk |
|---|---|---|
| Rightsizing | removes unused capacity | throttling/eviction if too aggressive |
| Autoscaling | matches capacity to demand | cold starts and churn |
| Spot/preemptible capacity | lower compute price | interruption/retry overhead |
| GPU sharing | higher utilization | contention/isolation trade-offs |
| Dedicated pools | predictable performance | lower aggregate utilization |
| Showback/chargeback | exposes ownership | allocation complexity |

## Decision Rule
Optimize for cost per successful unit of work while preserving the required reliability and latency SLOs. A cheaper GPU that increases retries or latency can increase total cost.

## Cost Attribution
Track by team/workload/model/environment:
- GPU and CPU consumption
- storage/network cost
- idle allocation
- successful workload volume
- retry/failure overhead
- estimated cost per successful request/job/token

## Failure Modes
1. Optimize utilization while violating latency SLO → include SLOs in cost decisions.
2. Use spot for non-checkpointable jobs → interruption cost erases savings.
3. Charge back raw infrastructure → teams optimize around allocation rather than outcomes.
4. Ignore idle reservations → capacity appears justified while unused.
5. Optimize GPU price but ignore model efficiency → lower $/GPU-hour can still mean higher $/task.

## Practice
- [ ] Calculate cost per successful inference request.
- [ ] Identify idle GPU capacity from a sample workload.
- [ ] Compare on-demand and interruptible capacity including retry cost.
- [ ] Build a team/workload showback table.
- [ ] Propose one cost reduction and state the SLO guardrail.

## Senior Interview Prompts
1. Why is cost per GPU-hour a weak AI cost metric?
2. When do spot instances make sense for ML?
3. How do you prevent cost optimization from degrading SLOs?
4. What should be included in unit economics?
5. How would you find the largest cost-reduction opportunity?

## Flashcards
#flashcard
**Q:** What is a useful AI infrastructure cost metric? :: **A:** Cost per successful unit of work, such as successful request, token, or completed training job, with SLO constraints.
