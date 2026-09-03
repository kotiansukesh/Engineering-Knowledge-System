---
title: "Array"
category: DSA
tags: [dsa, array]
created: 2026-01-18
updated: 2026-09-02
---

# Array

> Part of [[README|Java MOC]] • `DSA`

## Definition
An **array** is a contiguous block of memory holding equal-sized elements indexed by contiguous integers. Element address is computed arithmetically: `addr(i) = base + elem_size × (i - first_index)`, hence O(1) random access. Fixed capacity; dynamic growth requires reallocation (e.g., `ArrayList`).

> [!INFO] Address Formula
> `array_addr + elem_size * (i - first_index)`

## Characteristics
- **Homogeneous, indexed, zero-based** in Java; length fixed at allocation (`new int[n]`).
- **Cache-friendly** (locality), best sequential scan performance.
- **Multi-dimensional** arrays are arrays of arrays; two layouts exist (relevant for performance in row-major languages like Java/C).

### Multi-dimensional layouts
| Layout | Order | Java |
|---|---|---|
| **Row-major** | `(1,1)(1,2)(1,3)(1,4)…(2,1)…` | yes Java is row-major |
| **Column-major** | `(1,1)(2,1)(3,1)(1,2)…` | Fortran/MATLAB |

## Operations — complexity

| Operation | Complexity | Notes |
|---|---|---|
| Access `a[i]` / Write `a[i]=v` | **O(1)** | Direct address arithmetic |
| Search (unsorted) | **O(n)** | Linear scan |
| Search (sorted) | **O(log n)** | Binary search |
| Insert — end (if capacity) | **O(1)** | Amortised O(1) for dynamic array |
| Insert — beginning / middle | **O(n)** | Shift elements |
| Delete — end | **O(1)** |  |
| Delete — beginning / middle | **O(n)** | Shift elements |
| Traverse | **O(n)** |  |
| Sort (comparison) | **O(n log n)** |  |

### Summary Table (as in original)
|  | Add | Remove |
|---|---|---|
| **Beginning** | O(n) | O(n) |
| **End** | O(1) | O(1) |
| **Middle** | O(n) | O(n) |

## Java example

```java

// Purpose: Array: contiguous storage; O(1) index access; O(n) insert/delete; cache-friendly
// Representation: ArrayDemo — records/nodes; contiguous vs linked trade-off
// Operations: search, traverse
// Invariant: complexity assumes stated representation; handles empty/null boundaries
```

## Java 25 notes
- **Compact Object Headers (JEP 450, Java 25):** `-XX:+UseCompactObjectHeaders` reduces object header to 64-bit (8 B); arrays of objects/nodes benefit, ~10-20% heap saving for large `ArrayList`/`HashMap` node arrays. Enable in production for memory-bound workloads.
- **SequencedCollection (JEP 431):** `ArrayList` now implements `SequencedCollection`, use `addFirst`/`addLast`/`getFirst`/`getLast`/`reversed()` instead of index arithmetic. `var` keeps code concise.
- **Pattern matching:** use `if (obj instanceof String s)` and record patterns in loops where applicable (see Linked List / Trees).

## Pitfalls
- **Fixed size**, `ArrayIndexOutOfBoundsException`; check bounds or use `ArrayList`.
- **Shallow copy**, `clone()` / `Arrays.copyOf` on object arrays copies references, not deep clones.
- **Default values**, `new int[n]` fills with `0`, `new Object[n]` with `null` → NPE risk.
- **`==` vs `Arrays.equals`**, `==` compares identity, not contents.
- **Resizing cost**, repeated `copyOf` in a loop is O(n²); prefer `ArrayList` with initial capacity `new ArrayList<>(n)`.
- **Integer overflow** in binary search midpoint, use `mid = lo + (hi - lo)/2`.

## Interview Q&A
> **Java 25 tip:** Mention Compact Object Headers when asked about array memory overhead, shows you track runtime evolution.


**Q: Array vs ArrayList?** Array fixed, primitive-friendly, slightly faster; ArrayList dynamic, generic, richer API.

**Q: Why is random access O(1)?** Contiguous storage + arithmetic addressing.

**Q: Row-major vs column-major, why care?** Iteration order matching layout maximises cache hits (row-major → iterate rows inner loop).

<!-- SR -->
Array vs ArrayList?:: Array fixed, primitive-friendly, slightly faster; ArrayList dynamic, generic, richer API. #flashcard
Why is random access O(1)?:: Contiguous storage + arithmetic addressing. #flashcard
Row-major vs column-major, why care?:: Iteration order matching layout maximises cache hits (row-major → iterate rows inner loop). #flashcard

## Related
- [[Linked List]] • [[Stack]] • [[Queue]] • [[Java/07_DSA/HashMap|HashMap (DSA)]]
- [[README|Java MOC]]

## Solve with patterns
- [[Coding Patterns/01_Array/01 - Prefix Sum]]
- [[Coding Patterns/01_Array/02 - Two Pointers]]
- [[Coding Patterns/01_Array/03 - Sliding Window]]
- [[Coding Patterns/01_Array/04 - Frequency Counting]]
- [[Coding Patterns/04_Intervals_Search/02 - Modified Binary Search]]

## Practice
- [303. Range Sum Query Immutable](https://leetcode.com/problems/range-sum-query-immutable/)
- [525. Contiguous Array](https://leetcode.com/problems/contiguous-array/)
- [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)


---
*Category: DSA • Part of [[README|Java MOC]]*