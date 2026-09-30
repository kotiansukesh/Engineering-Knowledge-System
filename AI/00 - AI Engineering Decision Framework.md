---
title: "AI Engineering Decision Framework"
category: "AI"
type: decision-framework
tags: [ai, architecture, decisions, rag, agents, evaluation]
created: "2026-09-30"
completed: false
difficulty: Advanced
reviewed: ""
sr-due: ""
---

# AI Engineering Decision Framework

## 1. Start With the Requirement

Capture:
- user/task
- data sources
- freshness requirement
- correctness/risk
- latency target
- throughput
- availability
- security/tenant boundaries
- cost ceiling
- reversibility

## 2. Choose the Simplest Execution Model

| Requirement | Starting point |
|---|---|
| Deterministic rules | Code / workflow |
| External knowledge | RAG |
| Dynamic tool choice | Single agent |
| Independent responsibilities | Multi-agent |
| High-risk external action | Agent + explicit authorization/HITL |

Do not add an agent merely because an LLM is present.

## 3. Choose Where Knowledge Comes From

**Prompt context → retrieval → tool/API → durable memory**

Ask whether the information is:
- static or dynamic
- authoritative or derived
- tenant-specific
- sensitive
- required for every request

## 4. Choose the Model

Evaluate:
- task quality
- structured-output reliability
- tool-use reliability
- context needs
- latency
- cost
- availability
- data/privacy constraints

Use an evaluation set instead of choosing from model reputation alone.

## 5. Define the Evaluation Before Optimizing

At minimum:
- task success / correctness
- groundedness when retrieval is used
- tool-call correctness when tools are used
- latency
- token/cost per successful task
- safety/security failures

## 6. Design the Failure Path

For each external dependency define:
**timeout → retry policy → idempotency → fallback/degradation → observability → escalation**

## 7. Architecture Review Questions

- What is the system boundary?
- What is the authoritative source?
- What happens when retrieval is wrong?
- What happens when the model is unavailable?
- What action requires authorization?
- What is the blast radius of a bad tool call?
- Which metric tells us the architecture is degrading?
- What is the migration path if the current choice becomes wrong?

## 8. Evidence Rule

A decision is not complete until it has:
**decision → rationale → evidence → consequence → review trigger**

Link major decisions to [[Architect/01_Architecture-Foundations/Architecture-Decisions-and-ADRs|ADRs]].
