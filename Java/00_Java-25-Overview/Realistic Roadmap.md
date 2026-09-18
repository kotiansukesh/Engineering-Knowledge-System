---
title: "Realistic roadmap, Java vault"
category: overview
tags: [roadmap, java, plan]
created: 2026-09-04
completed: false
---
## Why it Matters

This note is the **map of what is actually in the vault right now**: 191 markdown files across `00` to `10` plus `99_Revision`, ordered by **dependency, not by topic**. It matters because the vault is too large to read cover to cover, and without order you hit Spring's JPA proxies before core Java and bounce off. Every phase has an entry, an exit criterion, and "what to skip on a second pass", so progress is measurable instead of open-ended.

Core ideas:
- **Phases are sequenced by dependency**: core Java → OOP → collections → DSA → concurrency → modern Java/LTS delta → Spring → patterns + LLD → revision. Each phase is the prerequisite of the next.
- **Every phase has an exit criterion** you can fail ("explain heap vs stack, PECS, terminal vs intermediate ops"), so you know when to move on instead of guessing.
- **Build rule + review rule**: run one snippet per note at its `--release` flag and break it once; mark `completed: true` and `reviewed: YYYY-MM-DD` only when you can answer the note's Q&A without looking.
- **Fast tracks exist**: backend interview in 4 weeks (0→3, 5→7, then mocks), architect pivot, or Java 25 delta only in half a day.

## Diagram

```mermaid
flowchart LR
 P0[P0 orientation, 2 days] --> P1[P1 core Java, 10 to 12 days]
 P1 --> P2[P2 OOP and SOLID, 4 to 5 days]
 P2 --> P3[P3 collections, 4 to 5 days]
 P3 --> P4[P4 DSA foundations, 7 to 9 days]
 P4 --> P5[P5 concurrency, 5 to 6 days]
 P5 --> P6[P6 modern Java and LTS delta, 5 to 6 days]
 P6 --> P7[P7 Spring, 10 to 14 days]
 P7 --> P8[P8 patterns and LLD, 10 to 14 days]
 P8 --> P9[P9 revision and mocks, ongoing]
```

## Code

The roadmap is run, not read. Verify the toolchain in P0 and compile every note snippet at that note's own release flag:
```bash

```

## When to use / NOT

| Use | Avoid |
|-----|-------|
| Follow the phase order, each is the prerequisite of the next (Spring before patterns is deliberate) | Jumping to `05_Spring` or `08_Modern-Java` first, JPA proxies and AOP make no sense without core Java + OOP |
| Use the exit criterion to decide when a phase is done | Reading every note in a folder before moving on, "coverage" is not fluency |
| Pair `07_DSA` with the 20 `Coding Patterns` outside `Java/` | DSA without patterns, you re-derive the approach for every problem |
| The fast tracks when the deadline is real (4-week backend, architect pivot, Java 25 delta only) | Doing all nine phases when you have 4 weeks, the plan is 10 weeks long |

## Trade-offs

- **Dependency ordering**: each phase lands on prepared ground (proxies after OOP, JPA after collections), but it front-loads core Java, so the exciting topics (Spring, Loom) arrive weeks in.
- **Fixed exit criteria per phase**: progress is measurable and re-visits are short, but the criteria are self-graded, so honesty is load-bearing; the Dashboard and `reviewed` dates are the audit trail.
- **10 phases over roughly 10 weeks at 60-90 min/day**: realistic and covers the full backend + DSA + LLD surface, but it is ~80-100 hours, so compress it with a fast track if the deadline is sooner.
- **Three LTS JDKs (17/21/25) installed simultaneously**: every snippet runs at its own `--release` and preview features work, but per-note JDK switching and language levels are real setup cost in P0.
- **Vault-incremental**: the plan reuses 191 existing notes and their Q&A/SR cards instead of new courses, but it inherits their gaps, the note set, not the plan, is the ceiling.

## Vs

**How to move through the vault: phase order vs folder order**

| Aspect | Phase order (this note) | Folder order (`00` to `10`) |
|--------|-------------------------|-----------------------------|
| Principle | dependency, Spring after core Java | alphabetical / numeric |
| Result | each phase lands on prepared ground | JPA proxies before OOP, bounce off |
| Use | the actual study path | finding a file |

**`99_Revision/Study Plan` tasks vs per-note `completed` flags**

| Aspect | Study Plan tasks | Per-note `completed` + `reviewed` |
|--------|------------------|-----------------------------------|
| Granularity | day-by-day schedule | per concept |
| Tracks | what to do this week | what you actually know |
| Use together | yes, the plan says when, the note says whether | the Dashboard rolls them up |

## Pitfalls

- **Jumping to `05_Spring` first.** JPA proxies and AOP assume core Java and OOP; without them the phase feels random and you conclude "Spring is too hard".
- **Treating the exit criteria as a formality.** They are self-graded, so honesty is load-bearing: if you cannot explain heap vs stack or PECS aloud, phase 1 is not done, move back, not forward.
- **Reading without compiling.** The plan is build-first, one snippet per note at its `--release`, break it once. Interviewers ask you to write code, not summarise notes.
- **Cramming `08_Modern-Java` and `09_Java-21-LTS` cover to cover.** They overlap by design; the note tells you exactly which notes to read per pass, so follow the passes instead of both folders.
- **Ignoring the fast tracks when the deadline is real.** The full plan is ~10 weeks; a 4-week deadline needs phases 0-3, 5-7, then mocks, not all ten phases at double speed.
- **Skipping phase 9.** Revision and mocks are ongoing, not a phase you finish; without them the earlier phases do not convert into interview performance.

## Interview Q&A

**Q1. How do you actually prepare for a Java backend interview with a full vault of notes?**
I sequence by dependency rather than topic: core Java, then OOP/SOLID, then collections, then DSA, then concurrency, then the modern Java / LTS delta, then Spring, then patterns and LLD, with ongoing revision and mocks. Each phase has an explicit exit criterion, e.g. "explain heap vs stack, PECS, and terminal vs intermediate ops" for core Java, or "write `newVirtualThreadPerTaskExecutor` from memory and say when NOT to use virtual threads" for concurrency. I run one snippet per note at its `--release` flag instead of only reading, and I only mark a note `completed` when I can answer its Q&A aloud without looking.

**Q2. What would you do differently if the interview is in four weeks?**
I would cut the full 10-week plan to the fast track: phases 0 to 3 (orientation, core Java, OOP, collections), then 5 to 7 (concurrency, modern Java and the LTS delta, Spring), then mocks. That deliberately defers deep design-pattern and LLD work, because in four weeks Spring + concurrency + DSA basics are what screening rounds actually test. If the role is more architect-leaning I would instead weight phases 2, 5, 7, and 8, spending extra time on transaction propagation, the security filter chain, and two LLD builds end to end.

How do you prepare for a Java backend interview with a full vault of notes?:: Sequence by dependency: core Java, OOP, collections, DSA, concurrency, LTS delta, Spring, patterns, then mocks. Each phase has an exit criterion; run one snippet per note at its `--release` and mark `completed` only when you can answer its Q&A aloud. #flashcard
What would you do differently if the interview is in four weeks?:: Cut to the fast track: phases 0-3 (orientation, core Java, OOP, collections), then 5-7 (concurrency, LTS delta, Spring), then mocks. Defer deep patterns and LLD; for an architect-leaning role, weight phases 2, 5, 7, 8 with extra transaction propagation and security filter chain. #flashcard

## Related

- [[Java 25 Roadmap]] • [[../99_Revision/Study Plan|Study Plan]] • [[Interview Strategy]] • [[README|Java MOC]]
- [[../../Coding Patterns/README|Coding Patterns]] (20 patterns, paired with phase 4)

---
*Category: overview*

# Realistic roadmap, Java vault

> Map of what is actually in `Java/` right now. 191 markdown files across 00 to 10 plus 99. Start at [[README|Java MOC]] if you want progress bars, use this note if you want order and dependencies.

# P0 tooling: three LTS JDKs is the minimum (17, 21, 25)

sdk install java 25-tem
sdk install java 21-tem
sdk install java 17-tem

# per note: match the --release to the note's era

javac --release 17 CheatSheet.java # core, OOP, collections notes
javac --release 21 Loom.java # concurrency, Java 21 notes

# 25 preview features (StructuredTaskScope, primitive patterns):

javac --enable-preview --release 25 Structured.java
java --enable-preview Structured

# progress is tracked in frontmatter, not in your head

# completed: true

# reviewed: 2026-09-17

```
Java 25 one-liner the P6 exit demands you deliver in 60 seconds:
```java
// ScopedValue (JEP 506, final), the ThreadLocal replacement story
static final ScopedValue<String> REQ = ScopedValue.newInstance();
ScopedValue.where(REQ, "id-1").run(() -> log(REQ.get()));
```

```

## How to Read this

- Assumes 60 to 90 minutes a day, 5 days a week.
- Each phase lists entry, exit, and what to skip on a second pass.
- **Build rule:** run one snippet per note at its `--release` flag, break it once, then move on.
```
mermaid
flowchart LR
 P0[00 orientation] --> P1[01 core java]
 P1 --> P2[02 OOP + SOLID]
 P2 --> P3[03 collections]
 P3 --> P4[07 DSA + coding patterns]
 P4 --> P5[04 concurrency]
 P5 --> P6[08 modern + 09 Java 21 + 25 delta]
 P6 --> P7[05 Spring]
 P7 --> P8[06 patterns + 10 LLD]
 P8 --> P9[99 revision + mocks]
```

## Phase 0, Orientation, 2 Days

Folder: [[README|00_Java-25-Overview]]

Read in this order:

1. [[Java 25 Roadmap]]
2. [[LTS Evolution 8 to 25]]
3. [[Interview Strategy]]
4. [[Whats New in Java 25]]

Exit: you can say in 60 seconds what changed at 8, 17, 21, and 25. If not, do not start phase 1 yet.

Tooling: install JDK 17, 21, 25. Set per note `javac --release 17` or `21` or `25`. Use preview flag only for 25 structured concurrency notes.

## Phase 1, Core Java, 10 to 12 Days

Folder: `01_Core-Java`, about 30 notes including 15 under `Types/`.

Week 1a: [[Classes]], [[Interface]], [[Method Overload]], [[Object Class]], [[Wrapper Class]], [[Abstract Class]], [[Final Class]], [[Immutable Class]], [[POJO Class]], [[Singleton Class]]

Week 1b: `Types/Nested Classes Overview` plus inner, static nested, anonymous, method local. Then [[String Handling]], [[Enums]], [[Annotations]], [[Exception Handling]], [[Serialization]]

Week 1c: [[JVM Memory Model]], [[Generics]], [[Lambdas and Functional Interfaces]], [[Streams API]], [[Optional]], [[Date and Time API]], [[IO and NIO]]

Exit: explain heap versus stack, PECS, stream terminal versus intermediate ops, and why `Optional` is not for fields. This is 90 percent of screening questions.

Skip on revisit: reread only [[01_Core-Java/Cheat Sheet|core cheat sheet]].

## Phase 2, oop and SOLID, 4 to 5 Days

Folder: `02_OOP`, 23 notes.

Order: [[00 - OOP Overview]], [[Abstraction]], [[Encapsulation]], [[Inheritance]], [[Polymorphism]], [[Interfaces]], then the six SOLID files plus [[SOLID-Summary]], then [[Class-Relationships]], [[Law-of-Demeter]], [[Pragmatic-Principles-DRY-YAGNI-KISS]].

Exit: give one Java example each for **dependency inversion** and Liskov violation, and say when inheritance hurts.

Skip on revisit: [[02_OOP/Cheat Sheet|OOP cheat sheet]] only.

## Phase 3, Collections, 4 to 5 Days

Folder: `03_Collections`, 14 notes.

Order: [[Collection]], [[List]], [[Set]], [[Map]], [[Queue]], then [[ArrayList]], [[LinkedList]], [[Vector]], [[Stack]], [[HashSet]], [[TreeSet]], [[Sorted Set]].

Exit: draw the hierarchy from memory, state null and ordering rules per impl, and compare `ArrayList` growth against `Vector`. Note where **sequenced collections** change the answer.

Skip on revisit: [[03_Collections/Cheat Sheet|collections cheat sheet]].

## Phase 4, dsa Foundations, 7 to 9 Days

Folder: `07_DSA`, 12 notes. Pair with `Coding Patterns`, 20 patterns, kept outside `Java/`.

Order: [[Array]], [[Linked List]] then singly and doubly, [[Stack]], [[Queue]], [[HashMap]], [[Trees]], [[Heap]], [[Graph]], then [[07_DSA/Cheat Sheet|DSA cheat sheet]].

Then coding patterns in three blocks: prefix and pointers and sliding window first, tree and graph traversal second, DP and backtracking and intervals last. [[../99_Revision/Study Plan|Study Plan]] days 34 to 40 cover these in order, follow that.

Exit: state time and space for each structure and solve one easy plus one medium per pattern block without hints.

## Phase 5, Concurrency, 5 to 6 Days

Folder: `04_Concurrency`, 8 notes.

Order: [[Threads]], [[Executor Framework]], [[CompletableFuture]], [[Locks and Synchronizers]], [[Atomics and Volatile]], [[Concurrent Collections]].

Key point: platform versus **virtual threads** is the whole phase. Remember `synchronized` no longer pins since Java 24, so old blog posts about pinning are stale.

Exit: write `newVirtualThreadPerTaskExecutor` from memory and say when not to use virtual threads (CPU bound, JNI).

## Phase 6, Modern Java and lts Delta, 5 to 6 Days

Folders: `08_Modern-Java` (8 notes) and `09_Java-21-LTS` (10 notes) plus 25 delta in `00_Java-25-Overview`.

Do not read both folders cover to cover. They overlap by design.

First pass: [[01 Records]], [[02 Sealed Classes]], [[03 Pattern Matching]], [[04 Sequenced Collections]], [[05 Virtual Threads - Loom]].

Second pass: `09_Java-21-LTS/01 Virtual Threads` for JEP 444 detail, then record patterns, switch patterns, generational ZGC, foreign function and memory API. Skim string templates and unnamed classes, both changed after 21.

Third pass: [[Whats New in Java 25]] plus `08_Modern-Java/06 ScopedValue` and `08 Compact Object Headers and Performance`. ScopedValue is the **ThreadLocal** replacement story interviewers ask about.

Exit: deliver the 60 second whats new answer from [[Interview Strategy]] with one JEP number per claim.

## Phase 7, Spring, 10 to 14 Days

Folder: `05_Spring`, 10 notes. Prereq is phases 1 to 3, else JPA and proxy sections will feel random.

Follow [[../99_Revision/Study Plan|Study Plan]] days 52 to 61: core and Boot, MVC, JPA, transaction plus executors, security, then stop. Do not mix patterns into this phase.

Exit: build one controller to service to repository slice with validation, `ProblemDetail` error handler, one `@Transactional` method, and `spring.threads.virtual.enabled=true` set on purpose with a reason.

## Phase 8, Patterns and LLD, 10 to 14 Days

Folders: `06_Design-Patterns` (29 notes, 23 GoF plus DAO and DI) and `10_LLD-Machine-Coding` (19 notes).

Patterns order: creational 5 first ([[Singleton]], [[Builder]], [[Factory Method]], [[Abstract Factory]], [[Prototype]]), then structural as Spring uses them (proxy, adapter, decorator, facade), then behavioral staples ([[Strategy]], [[Observer]], [[Template Method]], [[Command]], [[Chain of Responsibility]]). Leave visitor, mediator, memento for last, lowest interview weight.

LLD order: [[00_Method-How-to-Answer-LLD]], [[00_UML-Class-and-Sequence-Diagrams]], then [[01_Parking-Lot]], [[06_LRU-Cache]], [[05_ATM]], [[11_Splitwise]], [[12_Movie-Ticket-Booking]]. The rest are variants once you can do those five cleanly.

Exit: whiteboard parking lot or LRU cache in 35 minutes with class diagram, thread safety callout, and one pattern named per class.

## Phase 9, Revision and Mocks, Ongoing

Folder: `99_Revision`.

Work [[../99_Revision/Study Plan|Study Plan]] days 4 to 61 for the core plus backend track.

Weekly loop: 5 random Q and A cards, 1 DSA plus 1 concurrency snippet on paper, 1 whiteboard explanation, mark reviewed dates. [[Dashboard|The Dashboard]] shows stale notes older than 7 days.

## Fast Tracks

- Backend interview in 4 weeks: phases 0 to 3, then 5 to 7, then mocks. Defer LLD and DP depth.
- Architect pivot: phases 2, 5, 7, 8 carry most weight. Spend extra on transaction propagation, security filter chain, and two LLD builds end to end.
- Java 25 delta only: phase 6 third pass plus interview strategy one liners. Half a day if phases 1 to 5 are solid.
