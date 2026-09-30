---
title: "11 JVM & Performance"
category: "Java/11_JVM-Performance"
type: "folder-MOC"
tags: [MOC, java, jvm, performance]
created: "2026-09-30"
completed: false
---

# 11 JVM & Performance

> Production-oriented JVM knowledge: diagnose first, tune second.

## Topics

- [[JVM Diagnostics|JVM Diagnostics]] — thread dumps, heap, GC and native-memory investigation.
- [[Garbage Collection|Garbage Collection]] — G1, ZGC, generational behavior and pause/throughput trade-offs.
- [[JIT and Profiling|JIT and Profiling]] — warmup, compilation, allocation, JFR and measurement.

## Operating Principle

**Observe → form a hypothesis → measure → change one variable → compare → keep or revert.**

Do not treat JVM flags as configuration folklore.

## Related

- [[../01_Core-Java/JVM Memory Model|JVM Memory Model]]
- [[../04_Concurrency/README|Concurrency]]
- [[../12_Testing-Tooling/README|Testing & Tooling]]
- [[../README|Java MOC]]
