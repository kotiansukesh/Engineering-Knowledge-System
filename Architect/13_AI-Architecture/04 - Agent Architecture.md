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
