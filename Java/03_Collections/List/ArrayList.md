---
title: ArrayList
category: Java/03_Collections/List
tags:
- java
- collections
- list
created: 2026-01-18
pattern: 1
difficulty: Easy
completed: false
reviewed: ''
sr-due: ''
excalidraw: ''
source: ''
type: note
---

## Why it Matters

The **default `List`**: a **resizable array** with **O(1) random access**, amortised O(1) append, and 1.5x growth. Cache-friendly and compact , reach for it unless you need deque ends or concurrency.

## Diagram

```mermaid
flowchart LR
 A["element[] (cap 10)"] --> F["add() until full"]
 F --> G["grow 1.5x:
copy to new array"]
 G --> A
```

## Code

```java
// ArrayList — resizable array, O(1) random access, 1.5x growth
var list = new ArrayList<String>();
list.add("a"); list.add("b"); list.add("c");
System.out.println(list.get(1)); // => b
list.add(1, "z");
System.out.println(list); // => [a, z, b, c]
list.remove("z");
System.out.println(list.getFirst()); // => a
System.out.println(list.reversed());

var big = new ArrayList<Integer>(10_000);

var imm = List.of("a","b","c");
```
Pitfalls: concurrent modification during iteration throws. Use iterator.remove or CopyOnWriteArrayList for concurrent cases. List.of does not allow null.

## When to use / not

| Use | NOT |
|-----|-----|
| Random access, append-mostly, iteration | Frequent insert/remove in the middle (O(n) shifts) |
| Size upfront via `new ArrayList<>(n)` when known | Concurrent mutation → `ConcurrentModificationException`; use copy-on-write |
| `List.of` for small immutable constants | `null` elements with `List.of` (forbidden) |

## Trade-offs

- O(1) get/set, cache-friendly, lowest memory per element.
- Presizable to avoid 1.5x regrowth churn.
- Middle insert/remove shifts O(n); concurrent iteration is fail-fast.

## Vs

- vs LinkedList: ArrayList faster for get and append, LinkedList faster for deque ops
- vs Vector: ArrayList is unsynchronized, 1.5x growth, preferred
- vs CopyOnWriteArrayList: ArrayList for single thread, copy on write for many readers

## Pitfalls

- Concurrent modification during iteration throws , use `iterator.remove` or `CopyOnWriteArrayList`.
- `List.of` forbids `null`; `ArrayList` allows it , don't mix assumptions.
- Repeated growth without presizing is O(n²) churn , pass expected capacity.

## Interview q&a

**Q: How does `ArrayList` grow?** Backed by `Object[]` (capacity 10 on first add); grows ~1.5x (`old + old/2`) with `Arrays.copyOf` , presize via `new ArrayList<>(n)` for bulk loads.

**Q: Cost of middle insert/remove?** O(n) , elements shift. `get`/`set` by index stay O(1).

**Q: `ArrayList` vs `Vector`?** `ArrayList` is unsynchronized with 1.5x growth; `Vector` is legacy synchronized with 2x growth. Prefer `ArrayList`.

## Related

- [[Java/03_Collections/List/List|List]] • [[Java/07_DSA/Array|Array]] (growth, amortised analysis)
- [[Java/08_Modern-Java/04 Sequenced Collections|Sequenced Collections]] (`getFirst`/`reversed`)

How does ArrayList grow?:: Backed by an array that grows by about 1.5x when full. #flashcard
What is the cost of adding in the middle of an ArrayList?:: O(n) because elements shift. #flashcard
What is get by index cost in ArrayList?:: O(1). #flashcard
When should you size an ArrayList upfront?:: When you know the expected size, to avoid repeated resizing. #flashcard

# ArrayList , Java.util.ArrayList

> Part of [[Java/03_Collections/List/List|List]]

> ArrayList is the default List. It is a resizable array, ordered, allows duplicates and nulls.

## Internals

- backs with Object[] of default capacity 10 when first element added
- grows by about 1.5x when full: newCapacity = old + old/2
- stores elements contiguously, so cache friendly
- not synchronized
- since Java 21 implements SequencedCollection

## Time Complexity

- get and set by index: O(1)
- add at end: O(1) amortized, O(n) when resizing
- add or remove in middle: O(n) to shift
- contains and indexOf: O(n)
- iteration: O(n)
