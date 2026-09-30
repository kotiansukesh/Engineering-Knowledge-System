---
title: Engineering AI Architecture Study Plan
type: plan
domain: shared
status: active
created: 2026-09-30
reviewed:
next_review:
tags:
  - study-plan
  - backend
  - ai
  - architecture
---

# Engineering → AI → Architecture

> **Target path:** Backend Expert → AI Engineer → AI Architect (Agentic + Enterprise AI Systems)

This is the **master plan** across the four vaults. It is intentionally practical: every week produces evidence, not just notes.

## The learning loop

**Learn → Understand → Build → Break → Explain → Review**

Use the domain vault for detailed notes and the master plan only for direction and evidence.

## 12-week roadmap

| Week | Focus | Learn | Build / Practice | Evidence |
|---:|---|---|---|---|
| 1 | LLM + API foundations | Tokens, prompts, system instructions, temperature, model APIs | **AI Code Assistant API** with Spring Boot | Working REST API + prompt experiments |
| 2 | Embeddings + vector search | Embeddings, similarity, indexing, vector DB / Azure AI Search | **Document semantic search** | Retrieval examples + relevance observations |
| 3 | RAG | Chunking, indexing, retrieval, context injection | **Enterprise Q&A Bot** | Retrieval evaluation + failure cases |
| 4 | AI application engineering | Structured output, tool calling, validation, retries | Add tools and structured responses to the Q&A system | Tool-call tests + error handling |
| 5 | Agents | Agent loop, planning, tools, state, memory | **Single-agent task system** | Trace of decisions + tool execution |
| 6 | Multi-agent systems | Delegation, orchestration, handoffs, shared state | **Multi-agent workflow** | Architecture diagram + failure injection |
| 7 | AI reliability | Evaluation, hallucination, grounding, guardrails, observability | Build an **AI evaluation harness** | Quality/latency/cost measurements |
| 8 | AI platform engineering | Model gateway, routing, caching, rate limits, secrets, tenancy | **Enterprise AI Gateway** | ADR + benchmark + operational design |
| 9 | Architecture foundations | Requirements, estimation, NFRs, constraints, architecture styles | Design a production version of the AI platform | Requirements + NFR scenarios |
| 10 | Distributed systems | Data ownership, consistency, messaging, idempotency, resilience | Failure-inject the AI platform | Failure matrix + degraded modes |
| 11 | Enterprise AI architecture | Security, governance, cost, deployment, observability, migration | **Enterprise AI Platform architecture** | ADRs + threat model + cost model |
| 12 | Architecture defense | Trade-offs, redesign, review, communication | Blind design + changed-constraint redesign | Architecture review + portfolio case study |

## Weekly structure

### Monday — Learn

- [ ] Study the core concepts.
- [ ] Create/update only the essential notes.
- [ ] Write the mental model in your own words.

### Tuesday — Understand

- [ ] Implement a minimal example.
- [ ] Identify the invariant/mechanism.
- [ ] Draw one focused diagram if it materially helps.

### Wednesday — Build

- [ ] Extend the example into the week's project.
- [ ] Keep the implementation small enough to understand end-to-end.

### Thursday — Break

- [ ] Introduce one failure or changed constraint.
- [ ] Measure what happens.
- [ ] Record the result in Evidence.

### Friday — Explain

- [ ] Explain the concept without notes.
- [ ] Explain one alternative.
- [ ] Explain one failure mode.
- [ ] Explain the design in ≤5 minutes.

### Weekend — Review

- [ ] Review mistakes.
- [ ] Re-test the weakest concept.
- [ ] Update `reviewed` / `next_review`.
- [ ] Write one ADR or architecture decision when applicable.

## Cross-vault practice

| Capability | Vault | Question |
|---|---|---|
| Java | Java | How do I implement it? |
| Coding Patterns | Coding Patterns | How do I solve the problem efficiently? |
| AI | AI | How do I build and operate AI behavior? |
| Architecture | Architect | How do I design the whole system under constraints? |

Do not duplicate the same explanation in all four vaults. Link the concepts conceptually using the shared cross-vault contract.

## The three anchor projects

### Project 1 — AI Code Assistant

Weeks 1–3.

**Goal:** learn LLM APIs, embeddings and RAG by building rather than reading.

Minimum capabilities:

- code + question input;
- explanation/refactoring response;
- document ingestion;
- semantic retrieval;
- grounded answer.

### Project 2 — Agent Platform

Weeks 4–8.

**Goal:** move from AI application development to agentic engineering.

Minimum capabilities:

- structured outputs;
- tool calling;
- agent state;
- retries/timeouts;
- model routing;
- evaluation;
- tracing;
- cost/latency measurement;
- guardrails.

### Project 3 — Enterprise AI Platform

Weeks 9–12.

**Goal:** demonstrate architecture-level thinking.

Minimum deliverables:

- requirements;
- measurable NFRs;
- architecture diagram;
- data-flow diagram;
- security/threat model;
- ADRs;
- failure matrix;
- observability plan;
- cost model;
- deployment model;
- migration plan;
- redesign after a changed constraint.

## Promotion gates

### Backend → AI Engineer

- [ ] Can call an LLM API from a production-style Spring Boot service.
- [ ] Can explain embeddings and vector retrieval.
- [ ] Can build a basic RAG pipeline.
- [ ] Can evaluate retrieval and answer quality.
- [ ] Can handle retries, timeouts, validation and secrets.

### AI Engineer → AI Architect

- [ ] Can design an agent system from requirements.
- [ ] Can compare orchestration approaches without starting from a technology choice.
- [ ] Can model failure and degraded behavior.
- [ ] Can reason about security, cost and observability.
- [ ] Can define measurable evaluation criteria.
- [ ] Can redesign the system when a constraint changes.

### Architecture mastery

A topic is not marked mastered because the note is complete.

Require:

- [ ] one blind design;
- [ ] one failure injection;
- [ ] one trade-off defense;
- [ ] one measured experiment;
- [ ] one redesign after a changed constraint;
- [ ] one concise explanation from memory.

## What not to do

- Do not create notes for every tutorial paragraph.
- Do not build dashboards before the learning workflow is useful.
- Do not add an agent where a deterministic function is sufficient.
- Do not choose infrastructure before defining constraints.
- Do not treat completion counts as mastery.
- Do not create a diagram merely because a note has a "Diagram" heading.
- Do not duplicate concepts across vaults.

## Current focus

**Week:** 1  
**Primary outcome:** working AI Code Assistant API  
**Secondary:** keep Java/Spring implementation quality high  
**Architecture practice:** capture requirements, constraints and trade-offs for the project

## Review

```tasks
not done
sort by due
limit 15
```

## Related

- [[_shared/README]]
- [[_shared/Diagram-Guide]]
- [[Architect/99_Revision/Study Plan]]
- [[Coding Patterns/99_Revision/Study-Plan]]
