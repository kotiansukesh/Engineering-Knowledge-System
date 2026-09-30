# Diagram Guide

A diagram should answer **one question**.

## Choose the simplest format

| Question | Diagram |
|---|---|
| What happens first/next? | Mermaid flowchart |
| Who calls whom? | Mermaid sequence diagram |
| How does state change? | Mermaid state diagram |
| Who owns what? | Mermaid class/component diagram |
| Where does it run? | Excalidraw deployment/topology |
| How does space/memory/concurrency work? | Excalidraw |

## Rules

1. One diagram = one question.
2. Keep labels short.
3. Prefer Mermaid when the diagram is deterministic and text-friendly.
4. Use Excalidraw when spatial arrangement or exploration is the point.
5. Do not use screenshots of diagrams when a maintainable source can be kept.
6. Keep runtime flow, structure and deployment views separate.
7. Every diagram should have a one-sentence explanation of what it teaches.

## Common failure

Do not put classes, runtime sequence, deployment topology and failure recovery into one giant diagram. Split them into focused views.
