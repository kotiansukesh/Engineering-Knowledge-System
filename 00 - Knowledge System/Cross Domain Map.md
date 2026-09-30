---
title: "Cross Domain Map"
type: reference
category: "Knowledge System"
status: active
---

# Cross-Domain Map

| Concept | Java / Backend | AI | Architect |
|---|---|---|---|
| Concurrency | executors, virtual threads, locks | parallel tool calls, agent workers | throughput and contention |
| Caching | local/distributed caches | semantic/prompt/model-result caching | latency, consistency, cost |
| Transactions | Spring transactions, DB isolation | tool workflows and state transitions | consistency boundaries |
| Security | authn/authz, secrets | prompt injection, tool permissions, data controls | threat models and trust boundaries |
| Observability | Micrometer, JFR, logs/traces | token/cost/latency/traces/evaluation | SLOs and operational evidence |
| Messaging | Kafka/RabbitMQ/events | async agents and event-driven workflows | decoupling and failure isolation |
| Resilience | timeouts, retries, circuit breakers | model/tool fallback, bounded retries | degraded-mode architecture |
| Search | indexes, query planning | embeddings, hybrid retrieval, reranking | information architecture |

Use this page to deliberately transfer mechanisms between domains instead of learning the same idea four times.
