---
title: "Multi-Agent Patterns"
category: agentic
tags: [ai, agents, patterns, orchestration]
weeks: "12-15"
created: 2026-09-02
completed: false
---

# Multi-Agent Patterns

> Part of [[README|03_Agentic-AI]] • `agentic` • Weeks 12–15

## Intent

Catalog of collaboration patterns — choose based on task complexity and autonomy needs.

## Patterns

| Pattern | Flow | Use When |
|---------|------|----------|
| **Sequential** | Planner → Researcher → Coder → Reviewer | Linear pipelines |
| **Parallel fan-out** | Planner fans to 3 workers → aggregator | Independent subtasks |
| **Hierarchical** | Manager agent delegates to specialists | Complex goals with sub-ownership |
| **Debate / Review** | Coder ↔ Reviewer loop until pass | Quality-critical output |
| **Human-in-the-loop** | Gate before side effects | DB writes, deploys, external sends |

## Framework Trade-offs

| Framework | Strength | Trade-off |
|-----------|----------|-----------|
| **LangGraph** | Explicit state machines, checkpointing | More boilerplate |
| **AutoGen** | Conversational group chat, flexible | Harder to enforce determinism |
| **Assistants API** | Managed threads/tools | Less control, vendor lock |

## Code Sketch (LangGraph)

```python
from langgraph.graph import StateGraph
graph = StateGraph(state_schema=AgentState)
graph.add_node("planner", planner_node)
graph.add_node("researcher", researcher_node)
graph.add_edge("planner", "researcher")
graph.add_conditional_edges("researcher", should_review, {"yes": "reviewer", "no": "__end__"})
app = graph.compile(checkpointer=postgres_checkpointer)  # memory + audit
```

## Interview Q&A

- **Q:** How to prevent agent loops? **A:** Max iterations, explicit termination tool, HITL gate.
- **Q:** LangGraph vs AutoGen? **A:** LangGraph for deterministic workflows + checkpointing; AutoGen for exploratory multi-agent chat.

## Related

- [[Architecting Agentic AI Solutions]] • [[Enterprise AI Operations Platform]] • [[AI/07_Cross-Cutting/01_MCP|MCP]]

---
*Category: agentic*
