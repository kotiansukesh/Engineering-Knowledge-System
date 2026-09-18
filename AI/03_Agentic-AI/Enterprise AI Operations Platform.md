---
title: "Enterprise AI Operations Platform"
category: agentic
tags: [ai, project, agents, orchestration]
weeks: "11-16"
created: 2026-09-02
completed: false
type: project
---
## Why it Matters

Evolve [[AI/02_RAG-Engineering/Enterprise Document Search|Enterprise Document Search]] into a 7-agent platform with orchestration, memory, human approval, monitoring, and audit logs. This is your NUS-ISS capstone.

## Diagram

```mermaid
flowchart TB
 U["User request"] --> G["Gateway<br/>(auth, routing, budget)"]
 G --> PL["Planner Agent"]
 PL --> RET["Retrieval Agent<br/>MCP search_docs"]
 PL --> EX["Executor Agent"]
 EX --> SEC["Security Agent<br/>guards"]
 SEC -->|"high risk"| HITL["Human gate"]
 SEC --> RV["Reviewer Agent"]
 RV --> AUD["Auditor Agent"]
 AUD --> MM[(Memory store)]
 AUD --> LOG[(Audit log)]
 AUD --> R["Response + citations"]
```

## Code

```python
from typing import Literal
from pydantic import BaseModel

class Action(BaseModel):
 name: str
 params: dict
 risk: Literal["low", "medium", "high"]

POLICY = {"high": "require_human", "medium": "require_review", "low": "auto"}

def gate_for(action: Action) -> str:
 """Risk decides the gate before the action runs, not after."""
 return POLICY[action.risk]

## When to use / NOT

- **Use:** when the same operations work needs planning, retrieval, execution and review as separable, auditable steps — the Phase 03 deliverable.
- **NOT:** for request/response features with no side effects; the agent layer is pure overhead there.

## Trade-offs

- Multi-step goal ("research + query DB + draft code + review") completes with HITL gate and auditable trace.

## Vs

| Aspect | 7 specialised agents | One general agent | Non-agent pipeline |
|--------|------------------------|-------------------|---------------------|
| Failure isolation | Per agent | Whole context | Per stage |
| Audit story | Per action, per agent | One opaque trace | Clean but rigid |
| Cost | Highest | Medium | Lowest |

## Pitfalls

- Agents sharing one context window until it costs more than the work.
- A security agent that only logs; without a gate it is observability, not a control.
- Memory written for every run and never summarised or decayed.
- Budgets defined per request but never enforced in code — a loop is a bill.

## Interview Q&A

- **Q:** Why seven agents instead of one with all the tools? **A:** Separation of concern, failure isolation and auditability. A security agent with its own budget can veto an executor without sharing a context window, and every action has a named owner in the audit trail.
- **Q:** How is risk actually enforced? **A:** As a policy mapping applied before execution — high risk requires a human, medium requires review, low is automatic. The enforcement is in code, not in a prompt hoping the model asks permission.
- **Q:** What is the failure mode you worry about most? **A:** A silently growing budget. A stuck retry loop in an agent with tool access is both an incident and a large invoice, which is why per-run step and token budgets are enforced, not monitored.

## Related

- [[Architecting Agentic AI Solutions]] • [[Multi-Agent Patterns]] • [[AI/04_Production-Platform/README|04_Production (harden)]]

---
*Category: agentic*

# Enterprise AI Operations Platform — Capstone (Weeks 11–16)

> Part of [[README|03_Agentic-AI]] • `project` • The phase where a chatbot becomes an **enterprise system**.

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
User goal → Planner (DAG) → [Researcher ∥ Database Agent ∥ Coding Agent] ↓
 QA Agent → Reviewer (HITL gate) → Security Agent
 ↓
 Audit log + Memory write + Response
```

# Every Agent Action is Written to the Audit log before it Executes, so a

# Decision can be Reconstructed Even if the run is Interrupted.

# Audit.append({"agent": "Executor", "Action": Action, "Ts": Now()})
```