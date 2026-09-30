---
title: "LTS Evolution 8 to 25"
category: "Java/00_Java-25-Overview"
tags: [lts, java, roadmap, interview]
created: "2026-09-30"
completed: false
difficulty: "Medium"
reviewed: "2026-09-30"
sr-due: "2026-10-07"
type: "note"
---

# LTS Evolution: Java 8 → 11 → 17 → 21 → 25

> Use this note to explain the major LTS deltas. It is a historical map, not a second learning curriculum.

## One-line Story

- **8** — functional programming foundations: lambdas, Streams, java.time, Optional.
- **11** — standard library and platform cleanup: HttpClient, local var, String/Files improvements, Java EE/CORBA removals.
- **17** — modern data modeling and language features: records, sealed types, pattern matching for instanceof, text blocks, strong encapsulation.
- **21** — modern concurrency and pattern matching: virtual threads, sequenced collections, record patterns, pattern matching for switch, generational ZGC.
- **25** — scoped context and JVM ergonomics: Scoped Values final, compact object headers, flexible constructors, module imports, compact source files; structured concurrency and stable values remain preview.

## Release Map

| LTS | Key additions | Engineering focus |
|---|---|---|
| 8 | Lambdas, Streams, java.time, Optional | functional style and core APIs |
| 11 | HttpClient, local var, String/Files APIs | platform cleanup and HTTP |
| 17 | Records, sealed types, pattern instanceof, text blocks | modeling and exhaustive logic |
| 21 | Virtual threads, sequenced collections, record patterns, switch patterns | concurrency and modern syntax |
| 25 | ScopedValue, compact headers, flexible constructors, module imports | context propagation and JVM/language ergonomics |

## The 21 → 25 Distinction

Java 21 introduced virtual threads. Java 24 introduced JEP 491, which changed synchronized behavior so that synchronized blocks/methods no longer pin virtual threads in the old sense. Java 25 then finalised Scoped Values and continued the structured-concurrency work as preview APIs.

Do not attribute JEP 491 to Java 25.

## Preview Discipline

Java 25 includes preview APIs/features such as:

- Structured Concurrency (JEP 505)
- Stable Values (JEP 502)
- Primitive Types in Patterns (JEP 507)

Preview features can change. Always state the JDK release and preview flag when showing them.

## Interview Questions

**What changed from Java 8 to 17?**

The biggest story is language and data modeling: records, sealed types, pattern matching, text blocks, plus standard-library and platform changes from 9–16/11.

**Why is Java 21 important?**

Virtual threads changed the practical concurrency model for blocking workloads, while record/switch patterns improved data-oriented code.

**What is genuinely new in Java 25?**

ScopedValue is final, compact object headers became a product feature, and several language improvements became final. Structured concurrency is still preview.

**Should I learn every non-LTS release?**

No. Learn the LTS milestones and use non-LTS releases to understand where a feature originated or changed before becoming final.

## Related

- [[Java 8 LTS Overview]]
- [[Java 11 LTS Overview]]
- [[Java 17 LTS Overview]]
- [[../09_Java-21-LTS/README|Java 21 Deep Dive]]
- [[Whats New in Java 25]]
- [[Java 25 Roadmap]]
