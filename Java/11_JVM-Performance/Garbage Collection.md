---
title: "Garbage Collection"
category: "Java/11_JVM-Performance"
tags: [java, jvm, gc, g1, zgc]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
type: concept
---

# Garbage Collection

## Intent

Choose and tune a collector from workload requirements rather than from a generic claim that one collector is faster.

## Core Model

Garbage collection reclaims objects that are no longer reachable. The important production questions are:

- allocation rate;
- live-set size;
- pause-time requirements;
- throughput;
- heap size;
- tail latency;
- CPU budget.

## Collector Map

| Collector | Typical concern |
|---|---|
| G1 | balanced throughput and pause goals; common general-purpose choice |
| ZGC | very low pause goals, including large heaps |
| Serial | small heaps and simple environments |
| Parallel | throughput-oriented workloads |

Generational behavior exists in modern collectors, but implementation details differ. Do not reuse the old “Young/Old = one physical layout” mental model across every collector.

## Tuning Loop

1. Define an SLO.
2. Capture GC logs/JFR and application latency.
3. Establish allocation and live-set behavior.
4. Change one setting.
5. Compare the same workload.

## Pitfalls

- tuning from a single GC pause;
- increasing heap size without investigating retention;
- assuming low pause time means higher application throughput;
- quoting collector limits without measuring the application.

## Practice

- [ ] Explain G1 versus ZGC without naming a universal winner.
- [ ] Correlate a GC event with application latency.
- [ ] Identify a memory leak versus high allocation rate.
