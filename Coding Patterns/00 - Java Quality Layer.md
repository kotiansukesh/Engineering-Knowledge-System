---
title: Java Quality Layer
type: guide
category: Coding Patterns
tags:
  - java
  - implementation
  - interview-prep
---

# Java Quality Layer

> Java choices can introduce correctness, performance, or readability problems even when the algorithm is sound.

| Pattern | Java concerns |
|---|---|
| Prefix Sum | use long when cumulative values can overflow int; avoid unnecessary boxing |
| Sliding Window | update counts consistently; avoid repeated substring allocation |
| HashMap | correct key/value types; consider initial capacity for known large input |
| BFS | prefer ArrayDeque; keep visited representation compact |
| DFS | recursion depth may overflow the stack; know the iterative alternative |
| Heap | use PriorityQueue; comparator must not overflow |
| Graph | adjacency lists usually scale better than matrices for sparse graphs |
| DP | verify dimensions; consider rolling arrays |
| Union Find | path compression + union by rank/size |
| Trie | understand node allocation cost |
| Sorting | know whether the operation mutates input and whether stability matters |
| Binary Search | use overflow-safe midpoint and explicit interval semantics |
| Backtracking | undo state exactly; avoid shared mutable state |
| Bit Manipulation | use explicit masks and understand signed integer behavior |

## Java interview checklist

- [ ] Correct primitive width
- [ ] Correct collection semantics
- [ ] Comparator cannot overflow
- [ ] Queue/deque uses appropriate implementation
- [ ] No unnecessary hot-loop allocations
- [ ] Recursion depth considered
- [ ] Input mutation intentional
- [ ] Edge cases tested
- [ ] Complexity includes auxiliary memory
