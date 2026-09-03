---
title: "Tool Calling"
category: fundamentals
tags: [ai, tool-calling, function-calling, mcp]
weeks: "4"
created: 2026-09-02
completed: false
---

# Tool Calling

> Part of [[README|01_Fundamentals]] • `fundamentals` • Week 4

## Intent

Let LLM decide *when* and *how* to call your functions — bridge between reasoning and action.

## Key Points

- Define tools as JSON schemas (name, description, parameters). LLM returns tool call → you execute → feed result back.
- Patterns: single tool, parallel tools, sequential chaining, tool-choice forcing.
- [[AI/07_Cross-Cutting/01_MCP|MCP]] standardizes this in Phase 02+.

## Code Example

```python
tools = [{
  "type": "function",
  "function": {
    "name": "search_docs",
    "description": "Search enterprise docs by query",
    "parameters": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}
  }
}]
# LLM returns: {"tool_calls": [{"function": {"name": "search_docs", "arguments": '{"query":"..."}'}}]}
# You: results = await search_docs(**json.loads(args)); feed back as tool message
```

## Pros / Cons

| Pros | Cons |
|------|------|
| LLM orchestrates workflow | Latency per tool round-trip |
| Extensible (add tools without retraining) | Hallucinated arguments — validate |

## Interview Q&A

- **Q:** Tool calling vs RAG? **A:** RAG is retrieval-augmented generation; tool calling is general function dispatch. RAG often *uses* a search tool.
- **Q:** How to prevent infinite tool loops? **A:** Max iterations + explicit finish tool.

## Pitfalls

- Not validating tool arguments — LLM can hallucinate params.

## Related

- [[05_Structured Outputs]] • [[AI/07_Cross-Cutting/01_MCP|MCP]] • [[AI/03_Agentic-AI/README|Agentic AI]]

---
*Category: fundamentals*
