---
title: List
category: Collections
tags:
- java
- collections
- list
created: 2026-01-18
updated: 2026-09-04
pattern: 3
difficulty: Easy
completed: false
reviewed: ''
sr-due: ''
excalidraw: ''
source: ''
type: note
---

## Why it Matters

The **ordered, indexed** collection: **duplicates allowed**, positional `get`/`set`, and , since Java 21 , **`SequencedCollection`** access (`getFirst`, `getLast`, `reversed`). The default choice when order matters.

## Diagram

```mermaid
flowchart TD
 L["List"] --> AL["ArrayList
resizable array"]
 L --> LL["LinkedList
nodes + Deque"]
 L --> V["Vector (legacy)
Stack (legacy)"]
```

## Code

```java
// List — ordered, indexed, duplicates allowed
List<String> list = new ArrayList<>(List.of("b","a","c"));
System.out.println(list.get(1)); // => a
list.add("a");
System.out.println(list); // => [b, a, c, a]
list.set(1, "z");
System.out.println(list.getFirst()); // => b
System.out.println(list.getLast());
System.out.println(list.reversed()); // => [a, c, z, b]

var nums = List.of(1,2,2,3);
Set<Integer> dedup = new LinkedHashSet<>(nums);
```
Memory note: List.of is immutable and compact. ArrayList copies on growth.

## When to use / not

| Impl | Pick when |
|------|-------------|
| `ArrayList` | Random access, mostly append (default) |
| `LinkedList` | Frequent insert/remove at ends + deque ops |
| `CopyOnWriteArrayList` | Read-heavy, thread-safe iteration |
| `Vector`/`Stack` | Legacy only , do not use in new code |

## Trade-offs

- Indexed access + `SequencedCollection` ends (`getFirst`/`getLast`/`reversed`).
- Middle insert/remove is O(n) for array impls; index access O(n) for linked.
- `List.of` immutability vs `ArrayList` mutability confuses , check before `add`.

## Vs

| | `ArrayList` | `LinkedList` | `CopyOnWriteArrayList` |
|--|-------------|----------------|--------------------------|
| `get(i)` | O(1) | O(n) | O(1) |
| Ends insert | amortised O(1) | O(1) | O(n) copy |
| Threads | no | no | safe, snapshot iteration |

## Pitfalls

- `List.of(...)` is immutable , `add` throws `UnsupportedOperationException`.
- `remove(int)` vs `remove(Object)` overloads: `list.remove(1)` removes by index, not value `1`.
- `Arrays.asList` is fixed-size , `add` fails; wrap in `new ArrayList<>(...)` for growth.

## Interview q&a

**Q: List vs Set?**
List is ordered, indexed, allows duplicates. Set has no index, no duplicates, membership is O(1) for HashSet.

**Q: ArrayList vs LinkedList?**
ArrayList is array backed, O(1) get, O(n) insert in middle. LinkedList is node based, O(n) get, O(1) insert at ends when you have the node.

## Related

- [[Java/03_Collections/Collection|Collection]] • [[Java/03_Collections/Set/Set|Set]] (ordered vs unique)
- [[Java/07_DSA/Array|Array]] (contiguous backing) • [[Java/08_Modern-Java/04 Sequenced Collections|Sequenced Collections]]

What defines a List?:: Ordered, indexed, allows duplicates and nulls. #flashcard
When to use ArrayList vs LinkedList?:: ArrayList for random access, LinkedList when you need frequent insert or remove at ends and deque ops. #flashcard
What did Java 21 add to List?:: SequencedCollection with getFirst, getLast and reversed. #flashcard

# List , Java.util.List

> Part of [[README|Java MOC]]

> List is an ordered collection with index access. It allows duplicates and nulls. Order is insertion order.

Since Java 21, List is a SequencedCollection, so it has getFirst, getLast, addFirst, addLast, removeFirst, removeLast, and reversed.

## Contract

- ordered by index, from 0 to size minus 1
- allows duplicates, add returns true even if duplicate
- allows nulls except where implementation forbids
- index ops like get, set, add at index, remove at index

## Implementations

- ArrayList: resizable array, 1.5x growth, fast get and set O(1), add O(1) amortized, insert or remove in middle O(n)
- LinkedList: doubly linked list, fast insert or remove at ends, slow get O(n), allows nulls, implements Deque too
- Vector: legacy synchronized resizable array, 2x growth, synchronized per method, prefer ArrayList
- Stack: legacy LIFO over Vector, prefer ArrayDeque
- CopyOnWriteArrayList: thread safe for read heavy cases, copy on write
