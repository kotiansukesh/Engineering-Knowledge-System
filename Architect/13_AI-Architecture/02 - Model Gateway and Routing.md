---
title: Model Gateway and Routing
type: concept
category: Architect/13_AI-Architecture
difficulty: Hard
tags: [architecture, ai, models]
---

# Model Gateway and Routing

A model gateway centralizes policy and routing without hiding important model-specific behavior.

## Responsibilities

- authentication
- model selection
- routing policy
- quotas
- fallback
- telemetry
- cost attribution
- safety policy

## Routing inputs

Quality requirement, latency budget, context size, tool capability, cost budget and failure state.

## Failure question

What happens when the preferred model is unavailable, slow or produces unacceptable evaluation results?
## Routing architecture

Keep policy separate from provider-specific adapters.

**Client → gateway policy → eligibility filter → routing decision → provider adapter → model → telemetry/evaluation**

The gateway should expose stable application-facing contracts while preserving enough provider metadata for debugging and evaluation.

## Routing policy

Evaluate:

- task type and required capability;
- quality threshold;
- latency/SLO budget;
- context and tool compatibility;
- availability and rate limits;
- cost budget;
- safety/data residency constraints.

Avoid routing solely on price or model name.

## Failure modes

- provider outage;
- timeout or partial response;
- rate-limit exhaustion;
- model capability mismatch;
- fallback that silently changes quality;
- routing feedback loop caused by stale evaluation data.

## Evidence

Compare at least two routing policies on the same workload and record quality, p95 latency, error rate and cost per successful task.
