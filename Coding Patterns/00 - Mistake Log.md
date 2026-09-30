---
title: "Mistake Log"
category: "Coding Patterns"
tags: [mistakes, review, interview-prep]
created: "2026-09-30"
---

# Mistake Log

> Record **reasoning failures**, not just syntax bugs. Repeated mistakes are signals that the pattern has not been internalized.

## Mistake template

```markdown
## YYYY-MM-DD — Problem

**Pattern I chose:**  
**Correct pattern:**  

### What I did

### Why it looked reasonable

### Where it broke

### Correct invariant

### Rule to remember

### Similar problem to retry
```

## Common failure categories

| Category | Example |
|---|---|
| Pattern miss | Used DFS when BFS was required for shortest unweighted path |
| Wrong invariant | Shrunk a window before restoring the required condition |
| Boundary error | Mixed inclusive and exclusive prefix indices |
| State definition | DP state does not contain enough information |
| Premature optimization | Optimized before establishing a correct brute-force model |
| Wrong data structure | Used HashSet where frequencies were required |
| Complexity miss | O(n²) solution hidden inside nested library calls |
| Mutation issue | Modified input when the algorithm assumed immutability |
| Proof gap | Could not explain why pointer movement was safe |

## Review rule

If the same mistake occurs **twice**, add a dedicated flashcard to the relevant pattern note.

If it occurs **three times**, add a “When NOT to use” rule to the pattern note.
