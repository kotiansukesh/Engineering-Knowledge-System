---
title: "Enterprise AI Operations Platform"
category: agentic
tags: [ai, project, agents, orchestration]
weeks: "11-16"
created: 2026-09-02
completed: false
type: project
---

# Enterprise AI Operations Platform — Capstone (Weeks 11–16)

> Part of [[README|03_Agentic-AI]] • `project` • The phase where a chatbot becomes an **enterprise system**.

## Intent

Evolve [[AI/02_RAG-Engineering/Enterprise Document Search|Enterprise Document Search]] into a 7-agent platform with orchestration, memory, human approval, monitoring, and audit logs. This is your NUS-ISS capstone.

## Agents

| Agent | Role |
|-------|------|
| **Planner** | Breaks goal into tasks, DAGs workflows |
| **Researcher** | RAG + web/tool search, synthesizes context |
| **Database Agent** | PG/pgvector/Redis queries, data access |
| **Coding Agent** | Generates/refactors code, runs tests |
| **QA Agent** | Evaluation harness, regression checks |
| **Reviewer** | Code/policy review, compliance gate |
| **Security Agent** | Prompt injection, secret handling, sandboxing |

## Capabilities

- [ ] **Orchestration:** LangGraph state machine or AutoGen group chat; Planner → workers → Reviewer flow.
- [ ] **Memory:** Short-term (conversation) + long-term (PG + vector store per user/project).
- [ ] **Human approval:** HITL gates before DB writes / code merges / external calls.
- [ ] **Monitoring:** Per-agent latency, success rate, token cost → Prometheus (Phase 04).
- [ ] **Audit logs:** Who/what/when for every agent action — required for [[AI/06_Architecture-Governance/README|governance]].

## Architecture Sketch

```
User goal → Planner (DAG) → [Researcher ∥ Database Agent ∥ Coding Agent]
                              ↓
                         QA Agent → Reviewer (HITL gate) → Security Agent
                              ↓
                         Audit log + Memory write + Response
```

## Success Criteria

- Multi-step goal ("research + query DB + draft code + review") completes with HITL gate and auditable trace.

## Related

- [[Architecting Agentic AI Solutions]] • [[Multi-Agent Patterns]] • [[AI/04_Production-Platform/README|04_Production (harden)]]

---
*Category: agentic*
