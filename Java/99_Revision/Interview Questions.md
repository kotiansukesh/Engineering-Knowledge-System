---
title: "Interview Questions — Index"
category: Revision
tags: [interview, revision, MOC]
created: 2026-01-18
updated: 2026-09-02
---

# Interview Questions — Index

> Part of [[README|Java MOC]] • [[99_Revision/README|Revision MOC]] — **Do not duplicate Q&A here.** All Q&A lives in `01..07`; this file *indexes* it.

## All Interview Q&A — by Topic

```dataview
TABLE WITHOUT ID file.link as "Source Note", category as "Category"
FROM "Java"
WHERE category AND file.folder != "Java/99_Revision"
SORT category ASC, file.name ASC
```

> Tip: each source note has `## Interview Q&A` with `> Q:` / `> A:` flashcards. Open them directly — or `Ctrl+O` → `Interview`.

## Quick Filters

### Core Java & OOP
```dataview
TABLE WITHOUT ID file.link as "Note"
FROM "Java/01_Core-Java" OR "Java/02_OOP"
WHERE category
SORT file.path ASC
```

### Collections & DSA
```dataview
TABLE WITHOUT ID file.link as "Note"
FROM "Java/03_Collections" OR "Java/07_DSA"
WHERE category
SORT file.path ASC
```

### Concurrency & Spring & Patterns
```dataview
TABLE WITHOUT ID file.link as "Note"
FROM "Java/04_Concurrency" OR "Java/05_Spring" OR "Java/06_Design-Patterns"
WHERE category
SORT file.path ASC
```

## Cram Checklist — 7-Day Plan

- [ ] Day 1 — Core: `Object` vs `Wrapper` vs `POJO` vs `Singleton`; `Interface` default/static; `Method Overload` rules
- [ ] Day 2 — OOP: 4 pillars + 5 inheritance types (multiple/hybrid via interfaces); `super`/`final`/`sealed`
- [ ] Day 3 — Collections: `ArrayList` vs `LinkedList` vs `Vector`; `HashSet` vs `TreeSet`; `Queue`/`Deque` ops
- [ ] Day 4 — Concurrency: lifecycle (NEW/RUNNABLE/BLOCKED/WAITING/TIMED_WAITING/TERMINATED) + 4 creation ways + 7 issues
- [ ] Day 5 — Spring: IoC/DI/AOP + scopes/lifecycle; `@Transactional` propagation/proxy pitfall; Security filter chain
- [ ] Day 6 — Patterns: 22 GoF — be able to whiteboard Factory, Singleton, Observer, Strategy, Decorator intent
- [ ] Day 7 — DSA + Mock: Array/Linked List/Stack/Queue/HashMap/Tree complexities; do 5 timed mocks from this index

## Cross-Links

- [[Threads]] • [[Spring Framework]] • [[Spring Core]] • [[Dependency Injection]] • [[Spring Security]] • [[Spring Transaction]]
- [[Array]] • [[Linked List]] • [[Singly Linked List]] • [[Doubly Linked List]] • [[Stack]] • [[Queue]] • [[HashMap]] • [[Trees]]
- [[README|Java MOC]] • [[99_Revision/README|Revision MOC]]

---
*Category: Revision • Part of [[README|Java MOC]] • Source of truth: each topic's `## Interview Q&A`*
