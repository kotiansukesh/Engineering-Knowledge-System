---
title: Interview Strategy , Java 25
category: overview
tags:
- java25
- interview
- strategy
created: 2026-09-03
completed: false
pattern: 0
difficulty: Easy
reviewed: ''
sr-due: ''
excalidraw: ''
source: ''
type: note
---

## Why it Matters

Knowing the feature is not the same as **landing the answer**. This note converts the vault's canonical note structure into the **four-part interview answer**, Why it matters → When / When NOT → Code → Vs, plus the one-liner for the eight topics that actually get asked. It matters because interviewers reward *structured, bounded* answers: a candidate who says "records, probably, depends" loses to one who says "use a record for an immutable DTO, not for a JPA entity, and here is the three-line snippet".

Core ideas:
- **Every answer has the same shape**, so preparation transfers across questions.
- **One killer question per topic** (e.g. "does `synchronized` pin?" → "No since 24, JEP 491"), memorise the eight one-liners.
- **Code beats adjectives**: a 5-line runnable snippet ends every argument.
- **The mock loop is weekly and bounded**, 90 minutes, not an open-ended cram.

## Diagram

```mermaid
flowchart LR
 Q[interview question] --> W[1. Why it matters - one-sentence definition]
 W --> U[2. When / When NOT - one good, one bad case]
 U --> C[3. Code - 5-line runnable snippet]
 C --> V[4. Vs - compare to the alternative]
 V --> L[land the answer in about 60 seconds]
 L --> M[weekly mock loop, 90 min]
```

## Code

The answer template as a runnable Java 25 snippet, this is what "Code" means in the four-part answer:
```java
// Topic: record — 1. Why: immutable data carrier with free equals/hashCode/toString
record Point(int x, int y) {}

// 2. When / When NOT
Point dto = new Point(1, 2); // good: DTO, event, value key
// class Order {...} // NOT a record: JPA entity, needs mutation + no-arg ctor

// 3. Code — the 5-line snippet that ends the argument
String describe(Object o) {
 return o instanceof Point p ? "point " + p.x() + "," + p.y() : "other";
}

// 4. Vs — record vs class vs Lombok @Value
// record: language-level, final, one canonical constructor
// class + Lombok: mutable when you want it, but a dependency + IDE plugin
```
Deliver the same four beats for `ScopedValue`, virtual threads, `sealed`, or any canonical note in this vault.

## When to use / not

| Use | Avoid |
|-----|-------|
| The 4-part template (Why → When/NOT → Code → Vs) for *any* technical question | Monologue with no structure, you ramble past the 60-second mark |
| A killer one-liner with a JEP number ("no since 24, JEP 491") | Listing features vaguely ("records, sealed, probably threads?") |
| A 5-line runnable snippet on a whiteboard or shared screen | Abstract descriptions with no code, interviewers cannot verify depth |
| The weekly 90-minute mock loop (5 random Q&A, 1 DSA, 1 whiteboard, review) | Cramming the day before, answers do not survive nerves |

## Trade-offs

- **Structured 4-part answer**: sounds organised, covers what interviewers score, and is repeatable under stress; the risk is sounding rehearsed, so vary the example per question.
- **Killer one-liners**: fast, confident, memorable; but if the follow-up probes deeper ("why does JEP 491 fix it?") you must have the mechanism ready too.
- **Answering with code**: proves real fluency in seconds; costs whiteboard time and risks syntax slips, so keep snippets to 5 lines you have written before.
- **Mock loop weekly**: compounding, spaced repetition beats cramming; costs 90 minutes a week of real calendar time.

## Vs

**How to answer: structured 4-part vs unstructured**

| Aspect | 4-part (Why → When/NOT → Code → Vs) | Unstructured |
|--------|-------------------------------------|--------------|
| Time to land | ~60 seconds, bounded | 3 minutes, unbounded |
| Signals | structure, judgement, fluency | enthusiasm, maybe depth |
| Failure mode | sounds rehearsed if the example never varies | rambling past the actual question |

**`@Value`-style memorised one-liner vs understanding the mechanism**

| Aspect | Killer one-liner ("No since 24, JEP 491") | Mechanism answer |
|--------|------------------------------------------|-----------------|
| Speed | instant, confident | slower, costs interview time |
| Risk | follow-up "why?" must be ready | lower risk, harder to fake |
| Use | screening round, first pass | deep-dive round, senior roles |

## Pitfalls

- **Answering a different question than asked.** Pause, restate it in one sentence, then apply the 4-part template; answering the adjacent thing you prepared is the most common avoidable failure.
- **Listing features instead of taking a position.** "records, sealed, probably threads?" signals nothing. Pick one, state when and when not, and anchor it with code.
- **Quoting a JEP status you did not verify.** Final vs preview changes between releases, `StructuredTaskScope` is preview in 25, not final; check openjdk.org before the interview.
- **No code, only adjectives.** "it is more scalable" is untestable; a 5-line snippet ends the argument and proves you have written it.
- **Skipping the mock loop.** The plan assumes a weekly 90-minute mock; without it answers do not survive nerves, and you find out in the interview, not before.
- **Answering for the wrong level.** Screening wants breadth and crisp one-liners; senior deep-dives want the mechanism and the trade-off. Read the room before choosing depth.

## Interview q&a

**Q1. "What is new in Java 25?", answer it in 60 seconds.**
Java 25 is the LTS after 21. On top of 21's virtual threads, SequencedCollection, and record/switch patterns, Java 25 finalises **`ScopedValue` (JEP 506)** as the ThreadLocal replacement for Loom, adds **Structured Concurrency (JEP 505, preview)** via `StructuredTaskScope` for scoped fan-out, **compact object headers (JEP 450)** for memory, **flexible constructor bodies (JEP 513)**, **primitive patterns (JEP 507)**, and **module imports (JEP 511)**. Since Java 24 (JEP 491) `synchronized` no longer pins virtual threads, so existing `synchronized` code is safe around IO on 25.

**Q2. "Does `synchronized` pin a virtual thread?"**
Not since Java 24. JEP 491 lets a virtual thread unmount its carrier while blocked on a monitor, so `synchronized` behaves like `ReentrantLock` for pinning. Before 24, `synchronized` plus blocking IO pinned the carrier and could collapse throughput, which is why older blog posts say it does.

**Q3. "ScopedValue vs ThreadLocal?"**
`ThreadLocal` is mutable, requires `remove()` or it leaks, and is expensive with millions of virtual threads. `ScopedValue` (JEP 506, final) is immutable and bound for the duration of a scope, inherited automatically by child virtual threads and `StructuredTaskScope` forks, and cleared on scope exit with no `remove()` needed.

**Q4. "When NOT to use virtual threads?"**
CPU-bound computation, JNI/native calls that pin the carrier, or work that holds database locks for a long time. Virtual threads make blocking IO cheap, they do not make compute cheaper; for those use a sized platform-thread pool.

**Q5. "How do you actually prepare for a Java backend interview?"**
I follow a structured answer for every question: why it matters, when to use it and when not, a five-line code example, and a comparison to the alternative. I run a weekly 90-minute mock: five random Q&A cards, one DSA problem, one whiteboard explanation of a Java 25 feature, then mark `reviewed` dates so the spaced-repetition loop stays honest.

What is new in Java 25?:: Java 25 is the LTS after 21: ScopedValue final (506), Structured Concurrency preview (505), compact object headers (450), primitive patterns (507), flexible constructor bodies (513), module imports (511), and since 24 JEP 491 means `synchronized` no longer pins virtual threads. #flashcard
Does `synchronized` pin a virtual thread?:: Not since Java 24. JEP 491 lets a virtual thread unmount its carrier while blocked on a monitor, like `ReentrantLock`. Before 24 it pinned and could collapse throughput. #flashcard
ScopedValue vs ThreadLocal?:: ThreadLocal is mutable, needs `remove()` or it leaks, and is expensive with millions of virtual threads. ScopedValue is immutable, scope-bound, inherited by child threads, and cleared on scope exit. #flashcard
When NOT to use virtual threads?:: CPU-bound computation, JNI/native calls that pin the carrier, or long-held database locks. Virtual threads make blocking IO cheap, not compute cheaper; use a sized platform pool for those. #flashcard
How do you prepare for a Java backend interview?:: Every answer follows Why then When/NOT then Code then Vs; weekly 90-min mock of 5 random Q&A, 1 DSA, 1 whiteboard, then set `reviewed` dates for spaced repetition. #flashcard

## Related

- [[Whats New in Java 25]] • [[../08_Modern-Java/README|08 Modern Java]] • [[../99_Revision/Study Plan|Study Plan]] • [[../99_Revision/README|99 Revision MOC]]

---
*Category: overview • java25*

# Interview Strategy , Java 25

> Part of [[README|00 Overview]] • `overview` • How to answer Java 25 questions and crack backend interviews

## The 60-second "What's new in Java 25?" Answer

> "Java 25 is the LTS after 21. On top of 21's **virtual threads, SequencedCollection, record/pattern switch**, Java 25 finalizes **ScopedValue (JEP 506)** as the ThreadLocal replacement for Loom, introduces **Structured Concurrency (JEP 505 preview)** via `StructuredTaskScope` for scoped fan-out, **compact object headers (JEP 450)** for memory, **flexible constructor bodies (JEP 513)**, **primitive patterns (JEP 507)**, and **module imports (JEP 511)**. Since Java 24 (JEP 491) `synchronized` no longer pins virtual threads, so you can use `synchronized` around IO safely."

Deliver in **STAR + code**: name JEP, show 5-line snippet, state tradeoff.

## Answer Template (why → When/NOT → Code → vs)

Every vault note follows this. In interview, use it:

1. **Why it matters** (10s): one-sentence definition.
2. **When / When NOT** (15s): 1 good, 1 bad case.
3. **Code** (20s): runnable Java 25 snippet.
4. **Vs** (15s): compare to alternative (`record` vs `class`, `ScopedValue` vs `ThreadLocal`).

## Topic → Killer Question → One-liner

| Topic | Killer Q | One-liner |
|-------|----------|-----------|
| Virtual threads | Does `synchronized` pin? | No since 24 (JEP 491); on 21 it did |
| ScopedValue | Why not ThreadLocal with Loom? | TL leaks at millions of threads; SV is immutable + scope-bound + cheap |
| Records | When NOT to use record? | Mutable / JPA entity with lazy proxies / need inheritance |
| SequencedCollection | vs `list.get(0)`? | Works for List/Deque/LinkedHashSet; `.reversed()` too |
| Compact Headers | Heap saving? | 128→64 bit header, `-XX:+UseCompactObjectHeaders`, ~10-20% |
| Pattern matching | Primitive patterns? | JEP 507 , `case int i when i>0` without boxing |
| Flexible constructors | Before 24? | `super()` had to be first; now validate before super |
| Spring + Loom | Boot 3.5 + virtual threads? | `spring.threads.virtual.enabled=true`, Tomcat uses virtual threads |

## 30 Java 25 Flashcards (tap to Reveal in Dashboard.html)

Covered in `08_Modern-Java` + `04_Concurrency` , set `completed: true` per note to track.
```dataview
TABLE WITHOUT ID file.link as "Note", choice(completed, "✅", "⬜") as "Done"
FROM "Java/08_Modern-Java"
WHERE category
SORT file.name ASC
```

## Mock Loop (Weekly, 90 Min)

1. **15 min** , pick 5 random `## Interview Q&A` via `99_Revision` dashboard.
2. **45 min** , code 1 DSA (Coding Patterns) + 1 concurrency snippet on paper.
3. **15 min** , explain a Java 25 feature whiteboard-style (record/Virtual/ScopedValue).
4. **15 min** , review pitfalls + mark `reviewed: YYYY-MM-DD`.

45 min?:: , code 1 DSA (Coding Patterns) + 1 concurrency snippet on paper. #flashcard
15 min?:: , explain a Java 25 feature whiteboard-style (record/Virtual/ScopedValue). #flashcard
15 min?:: , review pitfalls + mark `reviewed: YYYY-MM-DD`. #flashcard

## Pitfalls Interviewers Hunt

- `new T()` / `T.class` with generics , erasure, won't compile.
- `- [ ]` tasks unchecked but claiming `completed: true` , dashboard exposes it.
- Claiming virtual threads for CPU-bound , use platform threads for CPU/JNI.
- `ThreadLocal` in virtual thread code , leak + JEP 506 question trap.
