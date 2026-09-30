---
title: Agent Architecture
type: note
category: Architect/13_AI-Architecture
difficulty: Hard
tags: [architecture, ai, agents]
---

# Agent Architecture

An agent is justified when the system must select actions dynamically under uncertainty.

## Boundaries

**Planner/reasoner → tools → state/memory → policy/guardrails → evaluator → human control**

## Questions

- Could a deterministic workflow solve this?
- What actions are permitted?
- What is the maximum autonomy?
- How is repeated looping prevented?
- Which actions require approval?
- How is the final outcome evaluated?
## Autonomy boundary

Model autonomy should be bounded by explicit policy.

Define:

- allowed tools and arguments;
- maximum turns or execution budget;
- state transitions;
- approval points;
- retry and cancellation rules;
- termination conditions;
- evaluator or verifier responsibilities.

Prefer a deterministic workflow when the decision space is known.

## Failure modes

Test looping, wrong tool selection, malformed arguments, stale state, conflicting tool results, prompt injection and partial completion.

## Evidence

Compare the agent with the simplest viable workflow. Measure task success, intervention rate, latency, cost and unsafe-action rate. Record where autonomy materially improves the task and where it does not.
