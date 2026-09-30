---
title: AI Evaluation Architecture
type: concept
category: Architect/13_AI-Architecture
difficulty: Hard
tags: [architecture, ai, evaluation]
---

# AI Evaluation Architecture

Evaluation is part of architecture because model behavior changes over time.

## Evaluation layers

- offline datasets
- retrieval metrics
- task success
- safety
- groundedness
- latency
- cost
- regression tests
- human review

## Fitness function

Define measurable thresholds before changing prompts, models, retrieval or agent policies.
## Evaluation design

Treat evaluation as a production subsystem, not a one-time benchmark.

Define:

- representative and adversarial datasets;
- deterministic checks where possible;
- retrieval metrics;
- task-success metrics;
- safety/constraint checks;
- human-review sampling;
- regression thresholds;
- versioning of datasets, prompts, models and evaluators.

## Fitness function

Set thresholds before changing the system. A change is acceptable only when it satisfies the required quality constraints without violating latency, reliability, safety or cost budgets.

## Failure modes

Test evaluator blind spots, dataset leakage, distribution shift and metric gaming.

## Evidence

Maintain a golden evaluation set and record baseline versus changed-system results, including regressions.
