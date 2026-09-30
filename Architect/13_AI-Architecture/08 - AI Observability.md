---
title: AI Observability
type: concept
category: Architect/13_AI-Architecture
difficulty: Hard
tags: [architecture, ai, observability]
---

# AI Observability

Trace the complete request, not just the model call.

## Observe

- request
- model
- prompt/version
- retrieved context
- tool calls
- latency
- token usage
- cost
- errors
- evaluation result
- human intervention

Do not log sensitive prompts or retrieved data by default.
## Observability architecture

Propagate a correlation/trace identifier across the full request.

Capture enough metadata to reconstruct behavior without storing sensitive content unnecessarily:

- model/provider and version;
- prompt/template version;
- retrieval identifiers and scores;
- tool calls and outcomes;
- latency by stage;
- token usage and cost;
- errors/retries;
- evaluation result;
- human intervention.

## Operational signals

Define alerts around SLOs, error rates, latency, cost anomalies, tool failures and evaluation regressions.

## Failure modes

Test missing traces, high-cardinality telemetry, sensitive-data leakage and provider metadata loss.

## Evidence

Demonstrate one trace from request through retrieval/model/tools and show how an injected failure is diagnosed from telemetry.
