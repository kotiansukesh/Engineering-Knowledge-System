---
title: "Set"
category: "Java/03_Collections/Set"
tags: [java, collections]
created: "2026-09-29"
completed: false
difficulty: "Easy"
pattern: 0
reviewed: "2026-09-29"
sr-due: "2026-10-06"
source: ""
excalidraw: ""
type: concept
---

# Set

> Part of [[README|Java MOC]] • `Java/03_Collections/Set`
> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → Java Diagram`

## Intent

One sentence: what problem does this solve? Define the **key term** in **bold**.

## Why it Matters

The **uniqueness + membership** abstraction: **no duplicates**, **no index**, O(1) `contains` on hashes. Backed by a `Map` internally , the right tool for dedup, visited-sets, and allow-lists.

## Diagram

```mermaid
flowchart TD
 S["Set"] --> H["HashSet
via HashMap"]
 S --> LH["LinkedHashSet
insertion order"]
 S --> T["TreeSet
via TreeMap, sorted"]
```

## Code / Example

```java
// Java 25: var, record, sealed, pattern matching, SequencedCollection, virtual threads, Compact Object Headers
// Set — unique elements; HashSet/LinkedHashSet/TreeSet trades
var set = new HashSet<>(List.of("B","A","C","A"));
System.out.println(set);
System.out.println(set.add("A")); // => false
System.out.println(set.contains("B")); // => true

List<Integer> nums = List.of(1,2,2,3,3,3);
Set<Integer> unique = new HashSet<>(nums);

Set<String> ordered = new LinkedHashSet<>(List.of("B","A","C","A"));
System.out.println(ordered); // => [B, A, C]

Set<Integer> sorted = new TreeSet<>(List.of(5,1,3,1));
System.out.println(sorted); // => [1, 3, 5]

Set<Integer> a = new HashSet<>(Set.of(1,2,3));
Set<Integer> b = Set.of(2,3,4);
a.retainAll(b);
```

### Concrete Example

- **Input:**
- **Output:**
- **Explanation:**

## When to Use / When NOT

| **Use When** | **Avoid When** |
|--------------|----------------|
|  |  |
|  |  |
|  |  |

## Trade-offs

| Dimension | This Approach | Alternative |
|-----------|---------------|-------------|
| Complexity | | |
| Performance | | |
| Readability | | |
| Testability | | |

## Vs Table

| | `HashSet` | `LinkedHashSet` | `TreeSet` |
|--|-----------|-----------------|-----------|
| Order | none | insertion | sorted |
| Cost | O(1) avg | O(1) avg | O(log n) |
| Null | one | one | no |

## Pitfalls

- mutating an element so hashCode or equals changes while in a HashSet loses the element, contains and remove fail
- TreeSet needs Comparable or a Comparator at construction, otherwise ClassCastException
- HashSet iteration order is not stable across runs

## Interview Q&A (Senior Depth)

**Q: How does `HashSet` avoid duplicates?** Backed by `HashMap` , the element is the key, `add` delegates to map `put`.

**Q: What breaks if you mutate an element in a `HashSet`?** The hash changes, the bucket mismatches, so lookups fail.

**Q: When to use `Set` vs `List`?** `Set` for uniqueness and fast membership, `List` for order and index.

## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the trigger keyword for Set? :: **A:** Not specified #flashcard

#flashcard
**Q:** Time/space complexity of Set? :: **A:** Time: O(), Space: O() #flashcard

#flashcard
**Q:** When do you NOT use Set? :: **A:** [anti-pattern scenarios] #flashcard

#flashcard
**Q:** Core Java 25 snippet for Set? :: **A:** `var list = new ArrayList<>(List.of(...));` #flashcard

## Practice Tasks (Tasks Plugin)

- [ ] Restate the intent from memory 📅 {date:YYYY-MM-DD, +1}
- [ ] Code the snippet without looking 📅 {date:YYYY-MM-DD, +3}
- [ ] Answer all Interview Q&A aloud 📅 {date:YYYY-MM-DD, +7}
- [ ] Review flashcards (Spaced Repetition) 📅 {date:YYYY-MM-DD, +1}

```tasks
not done
path includes {file.folder}
sort by due
limit 10
```

## Related

- [[Java/03_Collections/Collection|Collection]] • [[Java/03_Collections/Map|Map]] (sets are maps inside)
- [[Java/01_Core-Java/Types/Object Class|Object Class]] (`equals`/`hashCode` contract)

How does HashSet avoid duplicates?:: Backed by HashMap, element is the key, add delegates to map put. #flashcard
What breaks if you mutate an element in a HashSet?:: Hash code changes and the bucket mismatches, so lookups fail. #flashcard
When to use Set vs List?:: Set for uniqueness and fast membership, List for order and index. #flashcard
How to dedup while keeping order?:: Use a LinkedHashSet, for example new ArrayList<>(new LinkedHashSet<>(list)). #flashcard

# Set , Java.util.Set

> Part of [[Java/03_Collections/README|Collections Framework]]
>
> No duplicates, no index. Membership with contains is the main operation. Backed by a Map internally.

Since Java 21, SequencedSet adds getFirst, getLast and reversed for LinkedHashSet.

## Contract

- no duplicates, add returns false if already present
- no index, no get by position
- one null allowed in HashSet and LinkedHashSet, not in TreeSet
- equals means same size and every element contained in the other

## Implementations

- HashSet backed by HashMap, no order, fastest, default choice. See [[Java/03_Collections/Set/HashSet|HashSet]]
- LinkedHashSet backed by LinkedHashMap, insertion order, slightly heavier
- TreeSet backed by TreeMap, sorted, range ops, O(log n). See [[Java/03_Collections/Set/TreeSet|TreeSet]] and [[Java/03_Collections/Set/Sorted Set|Sorted Set]]
- EnumSet bit vector for enums, fast

## Methods

- add, contains, remove, size, isEmpty
- addAll, retainAll for intersection, removeAll for difference
- iterator


---

*Category: Java/03_Collections/Set • Part of [[README|Java MOC]] • Java 25*