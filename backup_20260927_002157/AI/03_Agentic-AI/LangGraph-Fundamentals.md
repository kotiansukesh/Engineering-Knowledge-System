---
title: "LangGraph Fundamentals"
category: agentic
tags: [ai, agents, langgraph, state, tools, streaming]
weeks: "11-13"
created: 2026-09-04
completed: false
reviewed: ""
sr-due: ""
problems-solved: []
problems-solved-dates: {}
excalidraw: ""
---
## Why it Matters

How to build stateful agent graphs in LangGraph without turning them into spaghetti. Covers state, nodes, memory, ReAct loops, streaming, and the workflow shapes you will reuse everywhere.

## Diagram

```mermaid
flowchart TB
 S["State schema<br/>(TypedDict)"] --> N1["Node: retrieve"]
 N1 --> C{"Conditional edge"}
 C -->|"relevant"| N2["Node: generate"]
 C -->|"not relevant"| N3["Node: rewrite"]
 N3 --> N1
 N2 --> E(["END"])
 C -->|"max rounds"| E
 E -.-> CK[("Postgres checkpointer<br/>memory + resume")]
```

## Code

```python
from typing import TypedDict, Literal
from langgraph.graph import StateGraph, END

class State(TypedDict):
 query: str
 messages: list[dict]
 retrieved: list[str]
 rounds: int

def retrieve(state: State) -> dict: ... # hybrid search → state["retrieved"]
def generate(state: State) -> dict: ... # answer + citations
def rewrite(state: State) -> dict: ... # query rewrite for retry

def route(state: State) -> Literal["generate", "rewrite", "__end__"]:
 """Every loop needs an explicit terminal branch."""
 if state.get("retrieved"): return "generate"
 if state["rounds"] >= 2: return END
 return "rewrite"

g = StateGraph(State)
g.add_node("retrieve", retrieve); g.add_node("generate", generate); g.add_node("rewrite", rewrite)
g.set_entry_point("retrieve")
g.add_conditional_edges("retrieve", route, {"generate": "generate", "rewrite": "rewrite", END: END})
g.add_edge("rewrite", "retrieve"); g.add_edge("generate", END)

## When to use / NOT

- **Use:** for stateful, loopable, multi-step agent flows where you need visible control flow, memory and replayable state.
- **NOT:** for linear request/response; the graph ceremony is only earned when there is branching, looping or resumable state.

## Trade-offs

| Choice | Cost |
|--------|------|
| Explicit graph | Verbose; simple flows carry framework weight |
| Checkpointer memory | A store that grows unless you summarise/decay it |
| Conditional edges | Control flow is now code you debug, not prompt behaviour |

## Vs

| Aspect | LangGraph | AutoGen | Plain async code |
|--------|-----------|---------|-------------------|
| Control flow | Explicit graph, visible | Conversational, emergent | Yours to write |
| State | Typed schema + checkpointing | Message history | Manual |
| Best for | Deterministic workflows with loops | Multi-agent dialogue | Simple pipelines |

## Pitfalls

| Pitfall | What happens | Fix |
|---------|--------------|-----|
| Bloated state | Whole chat history plus blobs passed to every node, slow and costly | Store ids and summaries in state, fetch full docs only where needed |
| Missing end edge | Reviewer loop never terminates, run burns tokens until killed | Always map a terminal branch to end and add a max round guard |
| Split tool pairs | Trimming drops a tool result but keeps the call, model hallucinates | Trim at message pair boundaries, keep tool call and result together |
| No human gate | Agent writes to prod or sends mail without approval | Put a gate node before side effects, route to end until a human approves |

## Interview Q&A

- **Q:** How do you prevent infinite loops in reviewer cycles? **A:** Step cap plus a pass threshold plus an escape edge. Reviewer returns a score, the conditional edge routes to end after N rounds regardless, and low stakes loops log instead of retrying forever.
- **Q:** When do you pick LangGraph over AutoGen? **A:** LangGraph when the flow must be repeatable and auditable, with explicit state and checkpoints. AutoGen when the value is in open ended agent discussion and strict ordering would get in the way.
- **Q:** When should you not orchestrate at all? **A:** Single model call answers it, latency budget is tight, or failure cost is low. Orchestration adds latency, cost, and failure points, so a chain of three agents for a one paragraph summary is waste.
- **Q:** What does checkpointing buy beyond crash recovery? **A:** Resume from any step, replay a failed run for debugging, time travel to compare planner outputs, and a free audit log of who decided what. Pair with Postgres and thread ids map to sessions.

## Related

- [[Multi-Agent Patterns]] • [[Architecting Agentic AI Solutions]] • [[Enterprise AI Operations Platform]] • [[AI/07_Cross-Cutting/01_MCP|MCP]]

---
*Category: agentic*

# LangGraph Fundamentals

> Part of [[README|03_Agentic-AI]] • `agentic` • Weeks 11–13
> Watch: [freeCodeCamp — LangGraph Complete Course for Beginners](https://www.youtube.com/watch?v=jGg_1h0qzaM)

## State schema and graph wiring

Everything in LangGraph flows through a shared **state** dict. Nodes read it and return updates. Edges define order. Conditional edges define branching. Keep state small and explicit or debugging becomes painful.

```
pythonfrom typing import TypedDict, Annotatedfrom langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
 messages: Annotated[list, add_messages]
 plan: str
 draft: str
 approved: bool

def planner(state: AgentState) -> dict:
 return {"plan": "steps for: " + state["messages"][-1].content}

def researcher(state: AgentState) -> dict:
 return {"draft": "findings for plan: " + state["plan"]}

def reviewer(state: AgentState) -> dict:
 ok = len(state["draft"]) > 20
 return {"approved": ok}

def route(state: AgentState) -> str:
 return "end" if state["approved"] else "researcher"

graph = StateGraph(AgentState)
graph.add_node("planner", planner)
graph.add_node("researcher", researcher)
graph.add_node("reviewer", reviewer)
graph.add_edge(START, "planner")
graph.add_edge("planner", "researcher")
graph.add_edge("researcher", "reviewer")
graph.add_conditional_edges("reviewer", route, {"researcher": "researcher", "end": "__end__"})
app = graph.compile()
```
```
mermaidflowchart TD
 planner --> researcher --> reviewer
 reviewer -- needs work --> researcher
 reviewer -- approved --> END
```

Rule of thumb: one node does one job, and routing logic lives in small functions, never buried inside a prompt.

## Stateful chatbot with memory

A stateless graph forgets everything between calls. A **checkpointer** fixes that by persisting state per thread. Pass a thread id in config and the same conversation resumes where it left off. Postgres is the right choice in production because it gives memory plus an audit trail.

```
pythonfrom langgraph.checkpoint.postgres import PostgresSaverfrom langgraph.graph.message import trim_messages

checkpointer = PostgresSaver.from_conn_string("postgresql://user:pass@localhost:5432/agents")
checkpointer.setup()
app = graph.compile(checkpointer=checkpointer)

config = {"configurable": {"thread_id": "session-42"}}

# Trim before Each Call so Long Chats fit the Window.

# Keep System Prompt, Keep Last n Tokens, Drop the Middle.

def trim(state: AgentState) -> dict:
 trimmed = trim_messages(
 state["messages"],
 strategy="last",
 max_tokens=4000,
 include_system=True,
 )
 return {"messages": trimmed}

app.invoke({"messages": [("user", "summarise what we agreed yesterday")]}, config)
```

Trimming strategy that works: keep the system message, keep tool results attached to their calls (never split a pair), and summarise anything older than your token budget into one short recap message instead of deleting it silently.

## ReAct Tool Loop

The **ReAct loop** is think, act, observe, repeat. Bind tools to the model, run the tool calls it requests, feed results back, and stop when it answers directly or hits a step cap.
```
pythonfrom langchain_core.tools import tool
import requests

@tool
def calculator(expression: str) -> str:
 """Evaluate a simple arithmetic expression."""
 allowed = set("0123456789+-*/(). ")
 if not set(expression) <= allowed:
 return "error: unsupported characters"
 return str(eval(expression, {"__builtins__": {}})) # sketch only, sandbox in prod

@tool
def web_search(query: str) -> str:
 """Search the web and return top snippets."""
 resp = requests.get("https://api.example-search.com/search", params={"q": query}, timeout=10)
 resp.raise_for_status()
 hits = resp.json().get("results", [])[:5]
 return "\n".join(f"- {h['title']}: {h['snippet']}" for h in hits)

tools = [calculator, web_search]
model = chat_model.bind_tools(tools)

def agent_node(state: AgentState) -> dict:
 return {"messages": [model.invoke(state["messages"])]}

def tool_node(state: AgentState) -> dict:
 last = state["messages"][-1]
 results = []
 for call in last.tool_calls:
 fn = {"calculator": calculator, "web_search": web_search}[call["name"]]
 results.append(fn.invoke(call["args"]))
 return {"messages": results}

def route_tools(state: AgentState) -> str:
 last = state["messages"][-1]
 if getattr(last, "tool_calls", None):
 return "tools"
 return "__end__"

graph = StateGraph(AgentState)
graph.add_node("agent", agent_node)
graph.add_node("tools", tool_node)
graph.add_edge(START, "agent")
graph.add_conditional_edges("agent", route_tools, {"tools": "tools", "__end__": "__end__"})
graph.add_edge("tools", "agent")
app = graph.compile(checkpointer=checkpointer)
```

Always cap the loop (for example 10 tool rounds). An uncapped tool loop is how demos burn money.

## Streaming output

Two kinds worth using. **Token streaming** pushes partial text to the UI. **Custom events** push progress signals (plan ready, tool started, draft scored) so the UI never looks dead.

```
python

# Token Stream

for chunk, meta in app.stream({"messages": [("user", "plan the launch")]}, config, stream_mode="messages"):
 print(chunk.content, end="", flush=True)

# Custom Events from Inside any Node

from langgraph.config import get_stream_writer

def researcher(state: AgentState) -> dict:
 writer = get_stream_writer()
 writer({"event": "research_started", "plan": state["plan"]})
 draft = "..."
 writer({"event": "research_done", "chars": len(draft)})
 return {"draft": draft}

for mode, payload in app.stream({"messages": [("user", "go")]}, config, stream_mode=["messages", "custom"]):
 print(mode, payload)
```

Pick token mode for chat text, custom mode for everything a progress bar or status line would show.

## Workflow Trio

### Prompt Chaining

Split one hard task into ordered steps where each step feeds the next. Each node has its own prompt and its own output contract.
```
pythondef outline(state: AgentState) -> dict:
 return {"plan": llm.invoke(f"Outline in 5 bullets: {state['messages'][-1].content}").content}

def expand(state: AgentState) -> dict:
 return {"draft": llm.invoke(f"Expand this outline into a memo:\n{state['plan']}").content}

def tighten(state: AgentState) -> dict:
 return {"draft": llm.invoke(f"Cut this to 150 words, keep facts:\n{state['draft']}").content}

chain = StateGraph(AgentState)
chain.add_node("outline", outline)
chain.add_node("expand", expand)
chain.add_node("tighten", tighten)
chain.add_edge(START, "outline")
chain.add_edge("outline", "expand")
chain.add_edge("expand", "tighten")
chain.add_edge("tighten", "__end__")
```

Use chaining when quality matters more than latency and each step is verifiable on its own.

### Router and classifier

One fast model decides the route, heavier nodes do the work. Keep the classifier prompt short and return a single label.

```
pythondef classify(state: AgentState) -> dict: label = llm.invoke(
 f"Reply with one word (billing, tech, other): {state['messages'][-1].content}"
 ).content.strip().lower()
 return {"plan": label}

def route_intent(state: AgentState) -> str:
 return state["plan"] if state["plan"] in ("billing", "tech") else "other"

router = StateGraph(AgentState)
router.add_node("classify", classify)
router.add_node("billing", billing_node)
router.add_node("tech", tech_node)
router.add_node("other", fallback_node)
router.add_edge(START, "classify")
router.add_conditional_edges("classify", route_intent, {"billing": "billing", "tech": "tech", "other": "other"})
```

Log every routing decision with the input. Silent misroutes are the top failure in router setups.

### Parallel fan out and fan in

For the document analyzer example, split a doc into sections, score each in parallel, then merge. **Fan out** sends one state copy to N nodes. **Fan in** waits for all of them before the aggregator runs.
```
pythondef split_doc(state: AgentState) -> dict:
 text = state["messages"][-1].content
 return {"plan": text} # real version: chunk ids list

def score_risks(state: AgentState) -> dict:
 return {"draft": "risks: ..."}

def score_costs(state: AgentState) -> dict:
 return {"approved": False} # placeholder: cost flag

def merge_scores(state: AgentState) -> dict:
 return {"draft": f"merged: {state['draft']} + cost flag {state['approved']}"}

fan = StateGraph(AgentState)
fan.add_node("split", split_doc)
fan.add_node("risks", score_risks)
fan.add_node("costs", score_costs)
fan.add_node("merge", merge_scores)
fan.add_edge(START, "split")
fan.add_edge("split", "risks")
fan.add_edge("split", "costs")
fan.add_edge("risks", "merge")
fan.add_edge("costs", "merge")
fan.add_edge("merge", "__end__")
```

Fan out only for independent subtasks. If two branches need each other mid flight, that is not parallel work, it is a sequence wearing a costume.

## Orchestrator worker and planner executor

Two shapes for harder jobs.

Orchestrator worker: one **orchestrator** breaks the goal into tasks and hands them to worker nodes, then merges results. Good when subtasks vary per input and you cannot hardcode the split.

Planner executor: a **planner** writes a full plan first, an executor runs it step by step, and a checker replans on failure. Good when the path is long and blind execution drifts.

```
python

# Orchestrator Worker Sketch

def orchestrator(state: AgentState) -> dict:
 tasks = llm.invoke(f"Split into 3 subtasks: {state['messages'][-1].content}").content
 return {"plan": tasks}

# Planner Executor Sketch

def planner(state: AgentState) -> dict:
 return {"plan": llm.invoke(f"Write numbered steps: {state['messages'][-1].content}").content}

def executor(state: AgentState) -> dict:
 return {"draft": llm.invoke(f"Run step 1 of this plan:\n{state['plan']}").content}
```

Default to orchestrator worker for variable work, planner executor when you need a visible plan a human can approve first.

# App = G.compile(checkpointer=postgres_checkpointer)
```