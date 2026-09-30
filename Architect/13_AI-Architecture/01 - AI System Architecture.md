---
title: AI System Architecture
type: concept
category: Architect/13_AI-Architecture
difficulty: Hard
tags: [architecture, ai]
---

# AI System Architecture

## Decision layers

1. Business outcome
2. Deterministic vs probabilistic boundary
3. Model capability requirement
4. Context/data architecture
5. Tool/integration boundary
6. Evaluation
7. Security
8. Observability
9. Cost and latency
10. Human control

## Questions

- What must be deterministic?
- Where can model uncertainty be tolerated?
- What is the failure containment boundary?
- What evidence proves quality?
## Architecture method

Use this sequence before choosing a framework or model:

1. Define the business outcome and failure cost.
2. Separate deterministic controls from probabilistic behavior.
3. Define quality, latency, availability, privacy and cost targets.
4. Choose the least autonomous mechanism that satisfies the requirement.
5. Define data, tool, model and human-control boundaries.
6. Design evaluation and observability before implementation.
7. Identify degraded modes and rollback paths.

## Failure modes to test

- model produces a plausible but incorrect result;
- retrieval or context is unavailable;
- a tool is unavailable or returns malformed data;
- latency or cost budget is exceeded;
- a downstream action succeeds partially;
- sensitive data crosses an unintended boundary.

## Architecture evidence

A defensible design should include:

- one architecture diagram with trust and failure boundaries;
- explicit quality-attribute targets;
- rejected alternatives and why they were rejected;
- at least one failure experiment;
- measured quality, latency and cost results;
- an ADR for consequential decisions.
