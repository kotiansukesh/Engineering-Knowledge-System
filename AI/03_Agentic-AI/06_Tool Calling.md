---
title: "Tool Calling"
category: "AI/03_Agentic-AI"
tags:
- ai
- agent
- tool-calling
- reliability
created: "2026-09-30"
completed: false
difficulty: "Medium"
reviewed: "2026-09-30"
sr-due: "2026-10-02"
type: "note"
---

# Tool Calling

## Intent
Learn how an LLM selects and invokes typed capabilities, and how to turn that probabilistic decision into a reliable application boundary.

## Core Model
`model -> tool selection -> schema validation -> authorization -> execution -> result normalization -> model`

Tool calling is not execution by itself. The model proposes an action; application code remains responsible for validation, permissions, idempotency, timeouts, and side effects.

## Decision Rule
Use tool calling when the system must act on external state or obtain information that should not be hallucinated.

Do not use it when deterministic application code can perform the operation without model-driven selection.

| Requirement | Mechanism |
|---|---|
| Fixed sequence of known operations | Deterministic workflow |
| Model must choose among bounded capabilities | Tool calling |
| Long-running or stateful coordination | Workflow/agent runtime |
| External integration standardization | Tool/API boundary such as MCP |

## Minimal Implementation
~~~~python
from typing import Literal
from pydantic import BaseModel

class GetOrder(BaseModel):
    order_id: str

class ToolResult(BaseModel):
    status: Literal["ok", "error"]
    data: dict

def execute_get_order(args: GetOrder, principal: str) -> ToolResult:
    return ToolResult(status="ok", data={"order_id": args.order_id})
~~~~

The important boundary is not the schema alone: validate arguments, authorize the caller, enforce timeouts, record the invocation, and make side effects idempotent where retries are possible.

## Real Trade-offs
| Decision | Option A | Option B | Choose based on |
|---|---|---|---|
| Tool schema | Strict typed schema | Free-form arguments | Prefer strict schemas when incorrect arguments can cause costly or unsafe actions |
| Execution | Synchronous | Async/job | Use async when work can exceed request timeout or needs durable retry |
| Side effects | Direct write | Idempotency-keyed command | Use idempotency for retries and duplicate model/tool calls |
| Tool count | Small curated set | Large dynamic catalog | Curate tools when selection errors and context cost become material |

## Failure Modes
1. **Malformed arguments** → reject before execution; return structured validation errors.
2. **Unauthorized action** → authorize outside the model; never treat a model instruction as permission.
3. **Duplicate side effect** → idempotency key + deduplication store.
4. **Tool timeout** → bounded timeout, cancellation, retry only when safe.
5. **Prompt injection through tool output** → treat tool results as untrusted data; do not let returned text redefine policy.
6. **Tool drift** → version schemas/contracts and run compatibility tests.

## Evaluation
Measure separately:
- tool-selection accuracy
- argument validity
- execution success rate
- duplicate-action rate
- policy/authorization violations
- end-to-end task success
- p50/p95 latency and cost

A high task-success score can hide unsafe or unreliable tool behavior, so evaluate the trajectory and side effects, not only the final answer.

## Practice
- [ ] Build a read-only tool and validate malformed arguments.
- [ ] Add authorization outside the model.
- [ ] Add an idempotency key and simulate duplicate calls.
- [ ] Inject a timeout and define the retry rule.
- [ ] Record a trace containing request, selected tool, validated args, result status, latency, and cost.

## Senior Interview Prompts
1. Why is tool calling not equivalent to an API call?
2. Where should authorization live and why?
3. How do you make a payment/order tool safe under retries?
4. When would a deterministic workflow replace an agent?
5. How would you evaluate tool choice independently from final-answer quality?

## Flashcards

#flashcard
**Q:** What does the model control in tool calling, and what must the application control? :: **A:** The model proposes a tool and arguments; application code validates, authorizes, executes, observes, and governs side effects.

#flashcard
**Q:** What is the key defense against duplicate side effects? :: **A:** Idempotency keys plus server-side deduplication for retryable commands.

## Related
- [[00 - AI Engineering Decision Framework]]
- [[00 - AI Practice Engine]]
- [[07_Cross-Cutting/01_MCP]]
- [[11_Guardrails]]
