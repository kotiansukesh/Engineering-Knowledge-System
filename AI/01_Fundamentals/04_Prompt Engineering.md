---
title: "Prompt Engineering"
category: fundamentals
tags: [ai, prompting, llm]
weeks: "3"
created: 2026-09-02
completed: false
---

# Prompt Engineering

> Part of [[README|01_Fundamentals]] • `fundamentals` • Week 3

## Intent

Systematically design prompts that are testable, versioned, and evaluable — not vibes.

## Key Points

- Patterns: role + context + task + constraints + output format; few-shot; chain-of-thought (with caution); instruction hierarchy.
- Version prompts like code — store in repo, test with eval set (see [[AI/07_Cross-Cutting/02_AI Evaluation|AI Evaluation]]).
- [[Prompt Playground]] is your lab for this.

## Code Example

```python
SYSTEM = """You are a meeting-notes assistant.
Rules: Be concise. Use bullet points. Cite decisions as [D1], [D2].
Output JSON matching the MeetingNotes schema."""

FEW_SHOT = {"user": "Summarize: ...", "assistant": '{"summary": "..."}'}
```

## Pros / Cons

| Pros | Cons |
|------|------|
| No model retraining | Brittle across model versions |
| Fast to iterate | Non-deterministic — needs eval |

## Interview Q&A

- **Q:** System vs user prompt? **A:** System sets role/constraints; user provides task data. System has higher priority in instruction hierarchy.
- **Q:** How to test prompts? **A:** Golden set + LLM-as-judge + regression suite — [[AI/07_Cross-Cutting/02_AI Evaluation|Evaluation]].

## Pitfalls

- Prompt injection via user input — sanitize and use delimiters. See [[AI/07_Cross-Cutting/04_AI Security|Security]].

## Related

- [[03_LLM APIs]] • [[05_Structured Outputs]] • [[Prompt Playground]]

---
*Category: fundamentals*
