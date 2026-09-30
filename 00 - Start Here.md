---
title: "Start Here"
type: MOC
domain: Cross-Domain
status: active
created: 2026-09-30
tags: [start-here, onboarding, learning-path]
---

# Start Here

> **You do not need to read this repository. You need to use it.**

This vault contains hundreds of notes because it is both a learning system and a long-term reference system. The folders are **not** the order in which you should study.

## Your path

**Backend Expert → AI Engineer → AI Platform Engineer → AI Architect**

Your existing backend experience is the starting point. Do not restart from beginner Java unless the baseline below exposes a real gap.

## The first 7 days

### Day 1 — Orient

Read:

1. [[README]]
2. [[00 - Knowledge System/Knowledge Model]]
3. [[Build Lab/README]]
4. [[Evidence/README]]

Then open [[Study Plan]].

**Do not open the Java/AI/Architect folders yet.**

### Day 2 — Baseline

Without notes, rate yourself:

| Capability | Green | Yellow | Red |
|---|---|---|---|
| Spring Boot backend | I can build/debug comfortably | Some gaps | Significant gap |
| Java concurrency | I can explain and diagnose | Some gaps | Significant gap |
| LLM APIs | I can build a production-shaped call | Some gaps | New |
| Embeddings/vector search | I can explain and implement | Some gaps | New |
| RAG | I can build/evaluate one | Some gaps | New |
| Distributed systems | I can reason about failures | Some gaps | Significant gap |
| System architecture | I can defend trade-offs | Some gaps | Significant gap |
| DSA patterns | I can solve common mediums | Some gaps | Significant gap |

Study only yellow/red areas.

### Days 3–7 — Build, don't browse

Start **Week 1: LLM API + structured application** from [[Study Plan]].

Build the first slice of the AI Code Assistant:

**code + question → backend → LLM → structured response**

Add:

- input validation;
- timeout;
- retry policy;
- structured response;
- tests;
- basic latency/cost observation.

The objective is to understand the entire request path, not to learn every LLM concept.

## What to study next

### Phase 1 — AI Engineering Foundations

**Weeks 1–3**

LLM APIs → structured outputs → embeddings → retrieval → RAG.

Primary material:

- [[AI/01_Fundamentals/README]]
- [[AI/02_RAG-Engineering/README]]

Project spine:

- [[Build Lab/03 RAG System/README]]

## Phase 2 — Agentic AI

**Weeks 4–6**

Tool contracts → agent loop → state → bounded single-agent workflows → constrained multi-agent comparison.

Primary material:

- [[AI/03_Agentic-AI/README]]

Project:

- [[Build Lab/04 Agent System/README]]

## Phase 3 — Production AI Platform

**Weeks 7–9**

Evaluation → gateway/routing → reliability → observability → platform operations.

Primary material:

- [[AI/04_Production-Platform/README]]
- [[AI/05_Kubernetes-Operations/README]]

Projects:

- [[Build Lab/05 AI Gateway/README]]
- [[Build Lab/06 AI Platform/README]]

Kubernetes is an operations capability, not a prerequisite for understanding AI application engineering.

## Phase 4 — Architecture

**Weeks 10–11**

Requirements → NFRs → architecture styles → data → integration → reliability.

Primary material:

- [[Architect/01_Architecture-Foundations/README]]
- [[Architect/02_Requirements-Quality-Attributes/README]]
- [[Architect/03_Architecture-Styles/README]]
- [[Architect/06_Data-Architecture/README]]
- [[Architect/07_Integration-APIs/README]]
- [[Architect/08_NonFunctional-Ops/README]]

Apply every concept to the AI platform you already built.

## Phase 5 — Enterprise AI Architecture

**Week 12**

Governance → security → tenancy → AI architecture → migration → architecture defense.

Primary material:

- [[AI/06_Architecture-Governance/README]]
- [[Architect/12_Enterprise-Architecture/README]]
- [[Architect/13_AI-Architecture/README]]

Capstone:

- [[Build Lab/07 Enterprise AI Platform/README]]

## What about Java?

Java is **supporting infrastructure**, not your first curriculum.

Use it when the project exposes a gap:

- Spring → [[Java/05_Spring/README]]
- concurrency → [[Java/04_Concurrency/README]]
- JVM/performance → [[Java/11_JVM-Performance/README]]
- testing → [[Java/12_Testing-Tooling/README]]
- LLD → [[Java/10_LLD-Machine-Coding/README]]

Do not spend 12 weeks relearning Java simply because the vault contains a 12-week Java plan.

## What about Coding Patterns?

Keep it alive with **2–3 problems per week**.

Use [[Coding Patterns/99_Revision/Study-Plan]] and [[Coding Patterns/00 - Pattern Decision Tree]].

Only switch to an intensive DSA block if your baseline shows a meaningful gap or an upcoming interview requires it.

## What counts as “done”?

A note is not done because you read it.

For an important topic, produce:

- a working implementation;
- a test/evaluation;
- one measured observation;
- one failure experiment;
- one alternative/trade-off;
- a short explanation from memory.

Record the artifact in [[Evidence/README]].

## Keep the 12-week plan coherent

The repository contains deeper reference material than the 12-week spine requires. Do not expand the schedule merely because more notes exist.

- Use domain syllabi for capability coverage.
- Use the master [[Study Plan]] for timing.
- Use [[Build Lab/README]] for the project sequence.
- Use [[Evidence/README]] to prove capability.

## Your navigation rule

When you feel lost:

1. Return here.
2. Check [[Study Plan]].
3. Identify the current week's outcome.
4. Open only the MOC for that domain.
5. Read only the notes needed for the current outcome.
6. Build something.
7. Record evidence.
8. Continue.

> **The repository is the library. [[Study Plan]] is the curriculum. [[Build Lab/README]] is the classroom. [[Evidence/README]] is the exam.**
