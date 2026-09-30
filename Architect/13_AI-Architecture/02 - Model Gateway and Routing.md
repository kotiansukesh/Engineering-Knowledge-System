---
title: Model Gateway and Routing
type: note
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
