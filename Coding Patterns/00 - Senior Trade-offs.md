---
title: Senior Trade-offs
type: guide
category: Coding Patterns
tags:
  - senior-interview
  - trade-offs
  - java
---

# Senior Trade-offs

> At senior level, correctness is the baseline. Explain why an approach fits the constraints and what changes if the constraints change.

## Trade-off checklist

1. Correctness / invariant
2. Time complexity
3. Space complexity
4. Input mutation
5. Stability / ordering requirements
6. Expected vs worst-case behavior
7. Integer overflow
8. Allocation / GC pressure
9. Readability and maintainability
10. Alternative under changed constraints

## Example: HashMap vs sort + two pointers

| Concern | HashMap | Sort + two pointers |
|---|---|---|
| Typical time | O(n) expected | O(n log n) |
| Auxiliary memory | O(n) | Depends on sort |
| Original order | Preserved | Input may be reordered |
| Original indices | Natural to retain | Requires bookkeeping |
| Predictability | Hashing assumptions | Deterministic comparison behavior |
| Best fit | Fast lookup / index retention | Ordering enables pointer reasoning |

## Java-specific review

- Is int safe or should long be used?
- Can HashMap/HashSet allocation dominate?
- Is ArrayDeque preferable to LinkedList for queue/deque behavior?
- Is recursion depth safe?
- Is a comparator overflow-safe?
- Can DP memory be compressed?
- Does the algorithm mutate caller-owned input?

After solving, identify one production concern that would matter at scale: memory ceiling, latency, concurrency, observability, streaming, or backpressure.
