---
title: Invariant Library
type: guide
category: Coding Patterns
tags:
  - invariants
  - proofs
  - pattern-recognition
---

# Invariant Library

> An invariant is the statement that remains true while the algorithm progresses.

| Pattern | Core invariant |
|---|---|
| Prefix Sum | Stored prefix state represents the aggregate through a fixed boundary. |
| Prefix Sum + HashMap | The map contains prior prefix states needed to derive the current target relation. |
| Two Pointers | Pointer movement only discards candidates proven unable to improve the answer. |
| Sliding Window | The active window satisfies the maintained constraint after each adjustment. |
| Frequency Counting | Stored counts exactly represent the relevant multiset/frequency state. |
| Fast & Slow Pointers | Relative pointer speed exposes the required cycle or midpoint property. |
| In-place Reversal | Every processed node points to the correct reversed prefix and unprocessed nodes remain reachable. |
| Monotonic Stack | Stack entries are unresolved candidates maintained in monotonic order. |
| Heap / Top K | The heap contains the best K candidates according to the selected ordering. |
| Binary Search | If a valid answer exists, it remains inside the current search interval. |
| BFS | Nodes are processed in nondecreasing distance from the source in an unweighted graph. |
| DFS | The recursive or explicit stack represents the currently explored frontier/path. |
| Shortest Path | Relaxation/finality maintains the algorithm's distance invariant. |
| Union Find | Every node's representative identifies its current connected component. |
| Trie | A node represents exactly the prefix spelled by its path from the root. |
| Backtracking | Current state contains exactly the choices made on the current branch. |
| DP | Each state stores the correct answer for its precisely defined subproblem. |
| Greedy | The chosen local decision is proven safe without needing an excluded alternative. |
| Matrix Traversal | Visited cells are processed at most once under the chosen traversal. |
| Bit Manipulation | Maintained bit state encodes exactly the required parity/mask/property. |
| Cyclic Sort | Values in the processed region are placed at canonical indices whenever possible. |
| Kadane | Running state is the best subarray answer ending at the current position. |
| Segment Tree | Each node stores its interval aggregate and parents combine child state correctly. |

## Proof prompts

- What does the state mean?
- What is true before the next operation?
- Why is the transition safe?
- What candidates become permanently irrelevant?
- What does termination imply?

If you can describe the code but not its invariant, you memorized an implementation rather than learned the pattern.
