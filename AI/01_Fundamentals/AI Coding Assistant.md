---
title: AI Coding Assistant
category: AI/01_Fundamentals
tags:
- project
- coding-assistant
- tool-calling
- repo-scoped
created: 2026-09-02
completed: false
reviewed: ''
sr-due: ''
difficulty: Medium
excalidraw: ''
source: ''
type: note
weeks: ''
---

## 🎯 Intent
CLI/chat assistant that answers coding questions using LLM APIs + tool calling (file search, execution) — scoped to the repo, never the shell.

## 💡 Why It Matters
- **Interview signal**: "How did you scope what the assistant was allowed to do?" and "How do you know its answers are grounded?" — constraint-first design is the answer
- **Production reality**: Grounded answers = context builder (open files + git scope) → tools (`search_code`, `read_file`) → structured output with citations
- **Failure mode**: Reads wrong file (detectable) vs fabricates APIs (silent). References in output are the guardrail.

## 🧩 Diagram: Scoped Coding Assistant Flow
```mermaid
flowchart LR
    U["User Query<br/>(IDE or chat)"] --> CTX["Context Builder:<br/>open files + git scope"]
    CTX --> T[Tool: search_code(query)]
    CTX --> R[Tool: read_file(path)]
    T --> L[LLM]
    R --> L
    L --> SO[Structured Output:<br/>{answer, code_snippet, references}]
    SO --> U
    style CTX fill:#e3f2fd
    style SO fill:#e8f5e9
```

## 💻 Code: Repo-Scoped Assistant with Path Jail (Python)
```python
from pydantic import BaseModel
from pathlib import Path
from typing import Optional

class CodeAnswer(BaseModel):
    answer: str
    code_snippet: Optional[str] = None
    references: list[str] = []  # file paths actually read

# Tools the assistant is granted — scoped to repo, NEVER the shell
TOOLS = [
    {"name": "search_code", "description": "Search the repo for matching symbols/strings",
     "params": {"query": "str"}},
    {"name": "read_file", "description": "Read one file within the repo root",
     "params": {"path": "str"}},
]

# Guardrail: read_file MUST refuse paths outside workspace root
async def read_file(path: str, workspace_root: str) -> str:
    root = Path(workspace_root).resolve()
    target = (root / path).resolve()
    if not target.is_relative_to(root):
        raise PermissionError(f"Path {path} escapes workspace")
    return target.read_text()

async def search_code(query: str, workspace_root: str) -> list[str]:
    # ripgrep / git grep / LSP — return matching file paths
    pass

# Agent loop (max 5 tool rounds)
async def agent_loop(user_query: str, workspace_root: str) -> CodeAnswer:
    messages = [{"role": "user", "content": user_query}]
    for _ in range(5):
        resp = await llm.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=[{"type": "function", "function": t} for t in TOOLS],
            response_format={"type": "json_schema", "json_schema": {"name": "CodeAnswer", "schema": CodeAnswer.model_json_schema()}}
        )
        if not resp.choices[0].message.tool_calls:
            return CodeAnswer.model_validate_json(resp.choices[0].message.content)
        # Execute tools
        for call in resp.choices[0].message.tool_calls:
            if call.function.name == "search_code":
                result = await search_code(**json.loads(call.function.arguments), workspace_root=workspace_root)
            elif call.function.name == "read_file":
                result = await read_file(**json.loads(call.function.arguments), workspace_root=workspace_root)
            messages.append({"role": "tool", "tool_call_id": call.id, "content": json.dumps(result)})
    raise RuntimeError("Max tool iterations reached")
```

## ✅ When to Use / ❌ When NOT to Use
| Scenario | Use? | Reason |
|---|---|---|
| Repo-scoped code Q&A, explain-this-file | ✅ | Grounded, verifiable |
| Boilerplate generation (verifiable by reading code) | ✅ | References make it checkable |
| Blind code generation pasted without review | ❌ | Ungrounded = hallucination risk |
| Anything touching secrets/production access | ❌ | Scope violation = security incident |

## ⚖️ Trade-offs
| Aspect | Scoped Coding Assistant | General Chat LLM | IDE Copilot Integration |
|---|---|---|---|
| **Grounding** | Repo tools, citations | Model memory only | Editor context |
| **Failure Mode** | Reads wrong file (detectable) | Fabricates APIs | Suggests out-of-context code |
| **Build Cost** | Hours (Phase 01 project) | None | None |

## 🆚 Vs. Alternatives
| Aspect | Scoped Assistant | General Chat LLM | IDE Copilot |
|---|---|---|---|
| **Grounding** | Repo tools, citations | Model memory | Editor context |
| **Failure Mode** | Reads wrong file | Fabricates APIs | Out-of-context suggestions |
| **Cost** | Build hours | None | License |

## ⚠️ Pitfalls
1. **Granting shell or write access early** — first failure mode becomes irreversible
2. **Letting assistant answer without `references`** — ungrounded answers look correct and aren't
3. **Ignoring token budgets** — dumping whole repo into context costs money and degrades quality
4. **Trusting generated API calls** — models invent signatures. Every snippet is read before use.

## 🎤 Interview Q&A (Senior Depth)

**Q1: "How did you scope what the coding assistant was allowed to do?"**
> **Answer**: Read-only, repo-relative tools with a path jail — `search_code` and `read_file` — and structured output that must carry references. No shell, no writes, no network. The constraint is the feature.

**Q2: "How do you know its answers are grounded?"**
> **Answer**: Because every answer carries references to files it actually read, and the structured schema makes an ungrounded answer visible instead of plausible prose.

**Q3: "What is the real cost of an unscoped coding assistant?"**
> **Answer**: Fabricated APIs that compile in review and fail in CI — plus, with write or shell access, a single bad tool call is a security incident, not a bad answer.

**Q4: "How do you handle context budget for large repos?"**
> **Answer**: Don't dump the whole repo. Use `search_code` to find relevant files, then `read_file` on top 3-5 hits. The tool selection *is* the retrieval step.

**Q5: "Why structured output instead of free text?"**
> **Answer**: Free text hides missing citations. `CodeAnswer` forces `references: list[str]` — if empty, answer failed grounding check. The schema *is* the quality gate.

## 🔗 Related
- [[03_LLM APIs]] • [[06_Tool Calling]] • [[AI Backend Template]] • [[AI Evaluation]]