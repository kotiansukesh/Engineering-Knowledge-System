---
title: "A/B Testing for ML"
category: "AI/04_Production-Platform"
tags: [experimentation, ab-testing, ml, statistics, rollout]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
reviewed: "2026-09-30"
sr-due: "2026-10-15"
type: "note"
---

# A/B Testing for ML

## Intent
Use controlled experiments to estimate the effect of a model or system change while protecting users and respecting statistical and operational constraints.

## Experiment Contract
Before exposure, define:
- primary metric
- guardrail metrics
- eligible population
- randomization unit
- assignment mechanism
- minimum detectable effect
- experiment duration/sample requirement
- stopping rule
- rollback condition

## Primary vs Guardrail Metrics
A model can improve task quality while increasing latency, cost, errors, or harmful outcomes. Do not treat a single metric as the whole decision.

| Metric class | Examples |
|---|---|
| Primary | conversion, task success, accepted answer rate |
| Quality | accuracy, groundedness, human rating |
| Reliability | error rate, timeout rate |
| Performance | p95/p99 latency |
| Cost | cost/request, tokens/request |
| Safety | policy violation or escalation rate |

## Randomization
Choose the unit carefully. User-level randomization avoids contaminating repeated interactions; request-level randomization may be inappropriate when users build state across requests.

## Failure Modes
- Sample ratio mismatch → assignment or instrumentation problem.
- Peeking repeatedly → inflated false-positive risk.
- Novelty/seasonality → short experiments misrepresent long-term behavior.
- Metric gaming → local improvement harms another outcome.
- Small segment regression hidden by aggregate results.
- Experiment changes external systems and contaminates the control group.

## Practice
- [ ] Write an experiment contract for a model change.
- [ ] Choose a randomization unit and defend it.
- [ ] Define one primary and three guardrail metrics.
- [ ] Simulate a sample-ratio mismatch.
- [ ] Design a rollback rule before starting the experiment.

## Senior Interview Prompts
1. Why can request-level randomization be unsafe?
2. What is a guardrail metric?
3. How can an experiment look positive while the product gets worse?
4. Why should stopping rules be defined before the experiment?
5. When is a canary preferable to a full A/B experiment?
