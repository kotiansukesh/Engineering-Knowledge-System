---
title: "AI Backend Template"
category: fundamentals
tags: [ai, project, fastapi, template]
weeks: "1-4"
created: 2026-09-02
completed: false
type: project
---

# AI Backend Template — Project (Weeks 1–4)

> Part of [[README|01_Fundamentals]] • `project` • The scaffold everything else extends.

## Intent

Reusable FastAPI service that wraps LLM APIs with streaming, structured outputs, tool calling, and observability hooks. Not a demo — a template you'll evolve through Week 36.

## Features

- [ ] `POST /chat` — streaming + non-streaming, Pydantic validation
- [ ] LLM adapter (OpenAI/Anthropic/Gemini) with retries + fallback
- [ ] Structured output endpoint (`POST /extract`)
- [ ] Tool registry + executor
- [ ] `/health`, `/metrics` (Prometheus stub), request ID middleware
- [ ] Dockerfile + `uv` lockfile + `pytest` suite

## Repo Layout

```
ai-backend-template/
  app/
    main.py          # FastAPI app
    llm/             # adapters, retry, streaming
    tools/           # registry, executor
    schemas/         # Pydantic models
  tests/
  Dockerfile
  pyproject.toml
```

## Success Criteria

- Streams tokens via SSE, validates structured outputs, executes 2+ tools.
- `pytest` passes; `docker build` succeeds.

## Related

- [[02_FastAPI Backend]] • [[AI/02_RAG-Engineering/Enterprise Document Search|Enterprise Document Search]] (next evolution)

---
*Category: fundamentals*
