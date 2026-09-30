---
title: Coding Patterns Diagram Guide
type: reference
domain: coding-patterns
tags: [dsa, diagrams]
---

# Diagram Guide

Use diagrams only when they make the invariant easier to see.

- **Flowchart:** algorithm steps.
- **State diagram:** pointer/window/graph state transitions.
- **Excalidraw:** spatial algorithms, matrix movement, tree/graph traversal state, memory layout.
- Avoid decorative diagrams.

## Example

```mermaid
flowchart LR
    A[Expand right] --> B{Constraint violated?}
    B -->|No| C[Continue]
    B -->|Yes| D[Move left]
    D --> B
```

This explains the sliding-window control loop without mixing it with implementation details.
