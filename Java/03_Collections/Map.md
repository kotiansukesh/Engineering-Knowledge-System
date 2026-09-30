---
title: "Map"
category: "Java/03_Collections"
tags: [java, collections]
created: "2026-09-29"
completed: false
difficulty: "Easy"
pattern: 0
reviewed: "2026-09-29"
sr-due: "2026-10-06"
source: ""
excalidraw: ""
type: "note"
---

# Map

> Part of [[README|Java MOC]] • `Java/03_Collections`
> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → Java Diagram`

## Intent

One sentence: what problem does this solve? Define the **key term** in **bold**.

## Why it Matters

The **key→value lookup** abstraction: **unique keys**, O(1) average access with hashing, O(log n) with trees. Maps back caches, indexes, frequency tables, and configs , pick the impl by ordering and concurrency needs.

## Diagram

```mermaid
flowchart TD
 MAP["Map"] --> H["HashMap
O(1), no order"]
 MAP --> LH["LinkedHashMap
insertion/access order"]
 MAP --> T["TreeMap
sorted O(log n)"]
 MAP --> CH["ConcurrentHashMap
thread-safe"]
```

## Code / Example

```java
// Java 25: var, record, sealed, pattern matching, SequencedCollection, virtual threads, Compact Object Headers
// Map — key→value; HashMap/LinkedHashMap/TreeMap selection
Map<String,Integer> m = new HashMap<>();
m.put("a",1); m.put("b",2); m.put("a",3);
System.out.println(m.get("a")); // => 3
System.out.println(m.containsKey("b")); // => true

for (var e : m.entrySet())
 System.out.println(e.getKey() + "=" + e.getValue());

m.getOrDefault("x", 0);
m.putIfAbsent("c", 5);
m.computeIfAbsent("d", k -> k.length());

var sorted = new TreeMap<>(m);
System.out.println(sorted.firstKey()); // => a

var ordered = new LinkedHashMap<String,Integer>();
ordered.put("b",2); ordered.put("a",1);
System.out.println(ordered); // => {b=2, a=1}
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

| | `HashMap` | `TreeMap` | `ConcurrentHashMap` |
|--|-----------|-----------|---------------------|
| Order | none | sorted by key | none |
| Cost | O(1) avg | O(log n) | O(1) avg, thread-safe |
| Null key | one | no | no |

## Pitfalls

- Mutable keys whose `hashCode` changes lose their entries , keep keys immutable (records).
- `get` returning `null` is ambiguous (absent vs mapped-to-null) , use `containsKey` or `getOrDefault`.
- `TreeMap` rejects `null` keys; `ConcurrentHashMap` rejects all `null`s.

## Interview Q&A (Senior Depth)

**Q: How does HashMap work?**
Array of buckets, hash to index, collisions form a list then a tree after 8 entries, rehash when size exceeds capacity times load factor.

**Q: Can HashMap have null keys? TreeMap?**
HashMap yes one null key. TreeMap no, null cannot be compared.

**Q: HashMap vs ConcurrentHashMap?**
HashMap is not thread safe and allows nulls. ConcurrentHashMap is thread safe, denies nulls, and allows concurrent reads and writes.

## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the trigger keyword for Map? :: **A:** [trigger keywords] #flashcard

#flashcard
**Q:** Time/space complexity of Map? :: **A:** Time: O(), Space: O() #flashcard

#flashcard
**Q:** When do you NOT use Map? :: **A:** [anti-pattern scenarios] #flashcard

#flashcard
**Q:** Core Java 25 snippet for Map? :: **A:** `var list = new ArrayList<>(List.of(...));` #flashcard

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

- [[Java/03_Collections/Set/Set|Set]] (`HashSet` is a `HashMap`) • [[Java/07_DSA/HashMap|HashMap (DSA)]] (buckets, treeify, load factor)
- [[Java/08_Modern-Java/01 Records|Records]] (ideal immutable keys)

How does HashMap handle collisions?:: List then tree after 8 entries in a bucket, plus rehash on resize. #flashcard
Can HashMap have a null key?:: Yes one null key, TreeMap no. #flashcard
When to use LinkedHashMap?:: When you need insertion order or an LRU cache. #flashcard
When to use ConcurrentHashMap?:: When you need thread safe map access without global locking. #flashcard

# Map , Java.util.Map

> Part of [[README|Java MOC]]

> Map stores key to value pairs. Keys are unique, values can repeat. It is not a Collection.

## Implementations

- HashMap: hash table, no order, one null key, many null values, O(1) get and put, backed by buckets, default capacity 16, load factor 0.75
- LinkedHashMap: HashMap plus insertion or access order, useful for LRU
- TreeMap: red black tree, sorted by key, O(log n), no null keys, needs Comparable or Comparator
- Hashtable: legacy synchronized map, no nulls, avoid
- ConcurrentHashMap: thread safe, no nulls, segment level locking
- EnumMap: array backed for enum keys, fast

Since Java 21, LinkedHashMap implements SequencedMap with firstEntry, lastEntry and reversed.


---

*Category: Java/03_Collections • Part of [[README|Java MOC]] • Java 25*