---
title: "Learning Graph"
type: reference
category: "Knowledge System"
status: active
---

# Learning Graph

The vault is a graph, not a folder tree.

## Edge vocabulary

- **prerequisite** — must understand first.
- **builds-on** — extends a concept.
- **used-by** — implementation dependency.
- **cross-domain** — same engineering principle in another domain.
- **evidence-for** — evidence demonstrating a claim.
- **decision-for** — ADR that governs the choice.
- **failure-of** — failure experiment for the concept.
- **review-with** — concepts that should be recalled together.

## Example graph

```mermaid
flowchart LR
  JavaConcurrency[Java Concurrency] --> Distributed[Distributed Systems]
  JavaConcurrency --> AgentParallelism[Agent Parallelism]
  Distributed --> AIPlatform[AI Platform]
  RAG[RAG] --> Agentic[Agentic AI]
  Agentic --> AIPlatform
  AIPlatform --> AIArchitecture[AI Architecture]
  Distributed --> AIArchitecture
  CodingPatterns[Pattern Recognition] --> Algorithms[Algorithms]
  Algorithms --> Backend[Backend Engineering]
  Backend --> Architecture[Architecture]
```

## Graph discipline

Prefer a small number of meaningful edges over dense link spam. If two notes are related only because they share a keyword, do not link them.

Use the edge vocabulary in frontmatter where the relationship matters to navigation or review.
