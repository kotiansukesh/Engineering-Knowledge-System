---
title: "Structured Outputs"
category: fundamentals
tags: [ai, structured-outputs, pydantic, json]
weeks: "3"
created: 2026-09-02
completed: false
---

# Structured Outputs

> Part of [[README|01_Fundamentals]] • `fundamentals` • Week 3

## Intent

Force LLM to emit validated schemas (JSON/Pydantic) instead of free text — enables tool chaining and reliable parsing.

## Key Points

- Methods: JSON mode, function calling with schema, provider structured-output APIs.
- Always validate with Pydantic; retry with error feedback on parse failure.
- Foundation for [[06_Tool Calling|Tool Calling]].

## Code Example

```python
from pydantic import BaseModel, Field

class MeetingNotes(BaseModel):
    summary: str = Field(description="2-3 sentence summary")
    decisions: list[str]
    action_items: list[dict]  # {owner, task, due}

# openai: response_format={"type": "json_schema", "json_schema": {...}}
# anthropic: tool with input_schema = MeetingNotes.model_json_schema()
```

## Pros / Cons

| Pros | Cons |
|------|------|
| Deterministic parsing | Extra tokens, latency |
| Composable with tools | Schema drift across models |

## Interview Q&A

- **Q:** What if LLM returns invalid JSON? **A:** Validate → on error, reprompt with validation message; cap retries.
- **Q:** JSON mode vs tool calling? **A:** JSON mode for single schema; tools when LLM must *choose* between schemas/actions.

## Related

- [[04_Prompt Engineering]] • [[06_Tool Calling]] • [[AI Backend Template]]

---
*Category: fundamentals*
