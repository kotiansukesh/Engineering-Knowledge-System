---
title: "Java 25 Roadmap"
category: overview
tags: [java25, roadmap, overview, lts]
created: 2026-09-03
completed: false
---

# Java LTS Roadmap — 8 → 25 Learning Path

> Part of [[README|00 Overview]] • `overview` • **Restructured 2026-09-03:** LTS evolution first, then SE → Modern → Concurrency → Spring → Patterns → DSA. Every note targets its LTS `--release` — search `Java 8/11/17/21/25` to audit.

## Summary

**One vault, five LTS stops:** [[Java 8 LTS Overview|8]] → [[Java 11 LTS Overview|11]] → [[Java 17 LTS Overview|17]] → [[../09_Java-21-LTS/00 Java 21 Overview|21]] → [[Whats New in Java 25|25]]. You already have 7 SE folders (01–07) + `99_Revision`; `00` is the map, `08` + `09` are the LTS deep dives.

## Phases at a Glance (restructured)

| Phase | Folder(s) | Weeks | LTS Focus | Key Outcome |
|-------|-----------|-------|-----------|-------------|
| **P0** | [[README|00 Overview]] | 0 | Tooling + [[LTS Evolution 8 to 25|LTS map]] | JDK 8→25 installed, plan pinned |
| **P1** | [[Java 8 LTS Overview|Java 8]] + [[../01_Core-Java/README|01 Core]] | 1–2 | **Java 8**: lambdas, Streams, `java.time`, `Optional`, `CompletableFuture` | SE fundamentals (90% interview Qs) |
| **P2** | [[Java 11 LTS Overview|Java 11]] + [[../01_Core-Java/README|01 Core]] | 3 | **Java 11**: `var`, `HttpClient`, String/Files sugar, JAXB removal | "What's new 8→11?" answered |
| **P3** | [[Java 17 LTS Overview|Java 17]] + [[../02_OOP/README|02 OOP]] + [[../08_Modern-Java/README|08 Modern]] (records/sealed) | 4–5 | **Java 17**: `record`, `sealed`, pattern `instanceof`, switch expr, text blocks | Modern baseline (interview 70%) |
| **P4** | [[../09_Java-21-LTS/README|09 Java 21 LTS]] + [[../03_Collections/README|03 Collections]] (Sequenced) | 6–7 | **Java 21 LTS**: virtual threads, Sequenced, record/switch patterns, ZGC gen, FFM | Concurrency leap |
| **P5** | [[Whats New in Java 25|Whats New 25]] + [[../08_Modern-Java/README|08 Modern]] (ScopedValue, headers) | 8 | **Java 25**: ScopedValue final, Structured Concurrency preview, compact headers, JEP 491 | "Delta 21→25" crisply |
| **P6** | [[../04_Concurrency/README|04 Concurrency]] | 8–9 | Loom deep dive (21→25 pinning fix) | Concurrency whiteboard |
| **P7** | [[../05_Spring/README|05 Spring]] | 9 | Boot 3.5 + virtual threads (`spring.threads.virtual.enabled`) | Backend interview |
| **P8** | [[../06_Design-Patterns/README|06 Patterns]] | 9–10 | 22 GoF as Spring uses them | Pattern whiteboard |
| **P9** | [[../07_DSA/README|07 DSA]] + [[../../Coding Patterns/README|Coding Patterns]] | 10 | DSA + 20 patterns | Coding interview |
| **P10** | [[../99_Revision/README|99 Revision]] | 10 | Mocks, SR, overdue sweep | Offer-ready |

> **Reading paths:** `8-only` = P1 • `17+` = P1→P3 • `21+` = P3→P4 • `25` = P5 alone for delta • **Full LTS** = P0..P10 in **10 weeks**

## Weekly Cadence (each study day)

- **Build 60%** — run the runnable snippet at its `--release` (`8`/`11`/`17`/`21`/`25`), break it
- **Study 25%** — Intent → When/NOT → Vs Table
- **Evaluate 15%** — answer 3–5 `## Interview Q&A` flashcards, mark `reviewed: YYYY-MM-DD`

## Tooling

| Tool | Version | Command |
|------|---------|---------|
| JDKs | **8, 11, 17, 21, 25 LTS** | `sdk install java 25-tem && sdk install java 21-tem && sdk install java 17-tem` — `sdk use java 21-tem` per note |
| Build | Maven 3.9+ / Gradle 8.10+ | `maven.compiler.release=17` (change per phase) |
| IDE | IntelliJ 2025.2+ | Per-module SDK = phase LTS, Language Level = same (preview for 25 `StructuredTaskScope`) |
| Verify | Any | `java --version` → expect phase LTS; `javac --release 21 Main.java` |
| Preview | 25 only | `javac --enable-preview --release 25` + `java --enable-preview` |

## Folder Map (what to open when)

```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category"
FROM "Java"
WHERE file.name = "README"
SORT file.folder ASC
```

## Related

- [[LTS Evolution 8 to 25]] • [[Java 8 LTS Overview]] • [[Java 11 LTS Overview]] • [[Java 17 LTS Overview]] • [[Whats New in Java 25]] • [[Study Plan - Java 25|Study Plan]] • [[Interview Strategy]] • [[../README|Java MOC]]

---
*Category: overview*
