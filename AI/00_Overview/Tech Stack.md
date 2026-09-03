---
title: "Tech Stack"
category: overview
tags: [ai, stack, tooling]
created: 2026-09-02
completed: false
---

# Tech Stack

> Part of [[README|AI MOC]] • `overview` • The concrete stack behind the platform evolution.

## Core Stack (Phase 01)

| Layer | Choice | Notes |
|-------|--------|-------|
| Language | **Python 3.12+** | FastAPI, type hints, `uv` |
| API | **FastAPI** + Pydantic v2 | Mirrors Spring Boot mental model |
| LLM Access | OpenAI / Anthropic / Gemini APIs | Start with one, add routing in [[AI/07_Cross-Cutting/06_Multi-Model Routing\|07]] |
| Structured Outputs | Pydantic / JSON mode / tool schemas | |
| Tools | Function calling, [[AI/07_Cross-Cutting/01_MCP\|MCP]] (from Phase 2) | |

## Data & Retrieval (Phase 02)

| Layer | Choice |
|-------|--------|
| OLTP | **PostgreSQL** + **pgvector** |
| Cache | **Redis** |
| Vector DB | pgvector → (optional) Qdrant/Weaviate for scale comparison |
| Search | BM25 + vector (hybrid), reranking |
| Embeddings | `text-embedding-3-*` / open-weight via Ollama |

## Agentic (Phase 03)

| Layer | Choice |
|-------|--------|
| Framework | **LangChain / LangGraph** or **AutoGen** — compare both, commit to one |
| Orchestration | LangGraph state machines / AutoGen group chat |
| Memory | Postgres + vector store for long-term memory |
| Approval | Human-in-the-loop gates |

## Production (Phase 04–05)

| Layer | Choice |
|-------|--------|
| RPC | **gRPC + Protobuf** |
| Packaging | **Helm** charts |
| Orchestration | **Kubernetes** (CKAD target) |
| Observability | **Prometheus + Grafana + OpenTelemetry** |
| Streaming | **Kafka** (optional, for platform completeness) |
| LLM Observability | **Langfuse / Arize Phoenix** ([[AI/07_Cross-Cutting/03_LLM Observability\|07]]) |

## Governance (Phase 06)

- **iSAQB SWARC4AI** concerns: quality attributes, EU AI Act, drift, MLOps, Green IT.

## Related

- [[Roadmap Overview]] • [[AI/01_Fundamentals/README|01_Fundamentals]] • [[AI/07_Cross-Cutting/README|Cross-Cutting]]

---
*Category: overview*
