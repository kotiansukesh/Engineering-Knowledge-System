---
title: "JVM Diagnostics"
category: "Java/11_JVM-Performance"
tags: [java, jvm, diagnostics, production]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
type: concept
---

# JVM Diagnostics

## Intent

Turn symptoms such as high CPU, latency spikes, thread starvation, GC pressure, or memory growth into evidence using standard JDK tooling.

## First Response

| Symptom | First evidence |
|---|---|
| High CPU | process CPU, thread dump, JFR |
| Long pauses | GC logs, JFR, heap occupancy |
| Heap growth | heap histogram, heap dump, allocation profile |
| Thread starvation | thread dump, executor metrics |
| Native-memory growth | Native Memory Tracking when enabled |

## Useful Commands

```bash
jcmd <pid> VM.version
jcmd <pid> Thread.print
jcmd <pid> GC.heap_info
jcmd <pid> GC.class_histogram
jcmd <pid> JFR.start name=investigation duration=60s filename=investigation.jfr
```

The exact availability and cost of commands depends on the JDK and process configuration.

## Rule

Never start by changing Xmx, GC, thread counts, or compiler flags. First capture evidence that distinguishes CPU, allocation, contention, I/O, and memory-retention problems.

## Practice

- [ ] Produce a thread dump and identify blocked/waiting threads.
- [ ] Capture a short JFR recording and locate allocation or CPU hotspots.
- [ ] Explain one production symptom using evidence rather than a guess.
