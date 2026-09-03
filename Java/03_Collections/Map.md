---
title: "Map"
category: Collections
tags: [java, collections, map]
created: 2026-01-18
updated: 2026-09-02
---

# Map — java.util.Map

Part of [[README|Java MOC]]

Map stores key to value pairs. Keys are unique, values can repeat. It is not a Collection.

## Implementations

- HashMap: hash table, no order, one null key, many null values, O(1) get and put, backed by buckets, default capacity 16, load factor 0.75
- LinkedHashMap: HashMap plus insertion or access order, useful for LRU
- TreeMap: red black tree, sorted by key, O(log n), no null keys, needs Comparable or Comparator
- Hashtable: legacy synchronized map, no nulls, avoid
- ConcurrentHashMap: thread safe, no nulls, segment level locking
- EnumMap: array backed for enum keys, very fast

Since Java 21, LinkedHashMap implements SequencedMap with firstEntry, lastEntry and reversed.

## When to use which

- general lookup without order: HashMap
- need insertion order or LRU: LinkedHashMap
- need sorted keys or range ops: TreeMap
- need concurrency: ConcurrentHashMap
- enum keys: EnumMap

## Example

```java
// Map — key→value; HashMap/LinkedHashMap/TreeMap selection
Map<String,Integer> m = new HashMap<>();
m.put("a",1); m.put("b",2); m.put("a",3);
System.out.println(m.get("a"));
System.out.println(m.containsKey("b"));

for (var e : m.entrySet())
    System.out.println(e.getKey() + "=" + e.getValue());

m.getOrDefault("x", 0);
m.putIfAbsent("c", 5);
m.computeIfAbsent("d", k -> k.length());

var sorted = new TreeMap<>(m);
System.out.println(sorted.firstKey());

var ordered = new LinkedHashMap<String,Integer>();
ordered.put("b",2); ordered.put("a",1);
System.out.println(ordered);
```

Note: mutating a key so its hashCode changes while in a HashMap loses the entry. Keep keys immutable.

## Interview questions

How does HashMap work?
Array of buckets, hash to index, collisions form a list then a tree after 8 entries, rehash when size exceeds capacity times load factor.

Can HashMap have null keys? TreeMap?
HashMap yes one null key. TreeMap no, null cannot be compared.

HashMap vs ConcurrentHashMap?
HashMap is not thread safe and allows nulls. ConcurrentHashMap is thread safe, denies nulls, and allows concurrent reads and writes.

<!-- SR -->
How does HashMap handle collisions?:: List then tree after 8 entries in a bucket, plus rehash on resize. #flashcard
Can HashMap have a null key?:: Yes one null key, TreeMap no. #flashcard
When to use LinkedHashMap?:: When you need insertion order or an LRU cache. #flashcard
When to use ConcurrentHashMap?:: When you need thread safe map access without global locking. #flashcard
