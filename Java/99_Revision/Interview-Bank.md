---
title: "Interview Bank — Java"
category: Revision
tags: [java, interview, revision, bank]
created: 2026-09-03
updated: 2026-09-23
pattern: 0
difficulty: Easy
completed: false
reviewed: ""
sr-due: ""
problems-solved: []
problems-solved-dates: {}
excalidraw: ""
---

# Interview Bank — Java

> Curated index of **killer questions** across all Java topics. Each entry links to the source note. Target: 3-5 questions per topic, senior depth — answer includes artifact + metric + rejected alternative.

---

## Core Java & Types (01_Core-Java, Types)

### Classes, Objects, Types
- **Q: Class vs Object vs Record — when do you pick each?**
  - Source: `01_Core-Java/Classes.md`, `08_Modern-Java/01 Records.md`
  - Expected: Class = behaviour + identity + lifecycle; Record = transparent data carrier (state = identity); avoid record for JPA entities or mutable state.

- **Q: Can a Java file have multiple public classes?**
  - Source: `01_Core-Java/Classes.md`
  - Expected: No, only one `public` top-level class per `.java` file; name must match filename.

- **Q: Immutable Class — how to build one correctly in Java 25?**
  - Source: `01_Core-Java/Types/Immutable Class.md`
  - Expected: `record` preferred; if class: final fields, no setters, defensive copies, `List.copyOf`, constructor validation.

- **Q: POJO vs JavaBean vs Record — what's the difference?**
  - Source: `01_Core-Java/Types/POJO Class.md`, `01_Core-Java/Types/Wrapper Class.md`
  - Expected: POJO = plain class no framework ties; JavaBean = getter/setter conventions + no-arg ctor; Record = compiler-generated immutable carrier.

### Generics, Collections, Streams
- **Q: Why is `List<String>` not a subtype of `List<Object>`?**
  - Source: `01_Core-Java/Generics.md`
  - Expected: Invariance prevents heap pollution; use `List<? extends Object>` for read-only, `List<? super String>` for write-only (PECS).

- **Q: Stream vs parallel stream — when does parallel help/hurt?**
  - Source: `01_Core-Java/Streams API.md`
  - Expected: Help: CPU-bound, large N, splittable source (array, range); Hurt: small N, I/O-bound, high merge cost, stateful ops.

- **Q: `Optional` — when to use, when to avoid?**
  - Source: `01_Core-Java/Optional.md`
  - Expected: Use for return types signalling "no value"; avoid in fields, method parameters, collections, `Optional<Optional<T>>`.

### Exceptions, Serialization, Date/Time
- **Q: Checked vs unchecked — what's your policy?**
  - Source: `01_Core-Java/Exception Handling.md`
  - Expected: Checked for recoverable caller action; unchecked for programming errors; wrap checked at boundaries, don't leak.

- **Q: Serialization — what breaks it, how to fix?**
  - Source: `01_Core-Java/Serialization.md`
  - Expected: `serialVersionUID` mismatch, non-serializable fields, schema evolution; use `@Serial`, custom `readObject`/`writeObject`, or avoid Java serialization entirely (JSON/protobuf).

- **Q: `java.time` vs legacy `Date`/`Calendar` — why the new API?**
  - Source: `01_Core-Java/Date and Time API.md`
  - Expected: Immutable, thread-safe, fluent, ISO-8601, proper time-zone handling; legacy is mutable, 0-based months, broken DST.

### JVM Memory
- **Q: Heap vs stack vs metaspace — what lives where?**
  - Source: `01_Core-Java/JVM Memory Model.md`
  - Expected: Heap = objects; Stack = frames (primitives, refs); Metaspace = class metadata (native); Code Cache = JIT code.

---

## OOP & SOLID (02_OOP, Inheritance)

### 4 Pillars
- **Q: Encapsulation — why private fields + getters/setters isn't enough?**
  - Source: `02_OOP/Encapsulation.md`
  - Expected: Getters/setters expose internals; prefer behaviour methods (`accelerate()`, not `setSpeed()`); immutable/record preferred.

- **Q: Inheritance vs Composition — decision rule?**
  - Source: `02_OOP/Inheritance.md`, `02_OOP/Class-Relationships.md`
  - Expected: "Is-a" + Liskov substitutable → inheritance; "Has-a" or behaviour reuse → composition; sealed interfaces for closed hierarchies.

- **Q: Polymorphism — static vs dynamic dispatch?**
  - Source: `02_OOP/Polymorphism.md`
  - Expected: Overload = static (compile-time); Override = dynamic (runtime); `instanceof` pattern matching (Java 17+) is type-safe dispatch.

### SOLID
- **Q: SRP — what's a "reason to change" and how do you find it?**
  - Source: `02_OOP/SOLID-Single-Responsibility.md`
  - Expected: Group methods by change-axis (schema vs format vs provider); import groups are a smell; extract per axis.

- **Q: OCP — how to extend without modifying?**
  - Source: `02_OOP/SOLID-Open-Closed.md`
  - Expected: Abstractions + Strategy/Template Method; new behaviour = new class implementing interface, not editing existing.

- **Q: LSP — `Square extends Rectangle` — why is it a violation?**
  - Source: `02_OOP/SOLID-Liskov-Substitution.md`
  - Expected: `setWidth`/`setHeight` breaks `Square` invariant; subtypes must strengthen postconditions, weaken preconditions.

- **Q: ISP — why fat interfaces hurt?**
  - Source: `02_OOP/SOLID-Interface-Segregation.md`
  - Expected: Clients depend on methods they don't use; split into role interfaces (`Printable`, `Scannable`) not `Machine`.

- **Q: DIP — how does Spring implement it?**
  - Source: `02_OOP/SOLID-Dependency-Inversion.md`, `05_Spring/Dependency Injection.md`
  - Expected: High-level modules depend on abstractions (`OrderService` → `PaymentProcessor`); Spring injects concrete at runtime.

---

## Collections (03_Collections)

- **Q: `ArrayList` vs `LinkedList` — when is LinkedList actually faster?**
  - Source: `03_Collections/List/ArrayList.md`, `03_Collections/List/LinkedList.md`
  - Expected: Almost never for random access; only `addFirst`/`removeFirst` in tight loops; cache misses make ArrayList win usually.

- **Q: `HashSet` vs `TreeSet` — complexity and ordering?**
  - Source: `03_Collections/Set/HashSet.md`, `03_Collections/Set/TreeSet.md`
  - Expected: HashSet = O(1) avg, no order; TreeSet = O(log n), sorted; both fail `contains` on mutable elements without `equals`/`hashCode`.

- **Q: `SequencedCollection` (Java 21) — what problem does it solve?**
  - Source: `08_Modern-Java/04 Sequenced Collections.md`, `09_Java-21-LTS/02 Sequenced Collections.md`
  - Expected: Unified `getFirst`/`getLast`/`addFirst`/`addLast`/`reversed()`; `LinkedHashSet`/`LinkedHashMap` now have first/last access.

---

## Concurrency (04_Concurrency)

- **Q: Virtual threads (Java 21/25) — how do they differ from platform threads?**
  - Source: `04_Concurrency/Threads.md`, `08_Modern-Java/05 Virtual Threads - Loom.md`
  - Expected: M:N scheduling, cheap creation (millions), park on blocking I/O, no pool exhaustion; pinning on `synchronized`/native/JNI.

- **Q: `StructuredTaskScope` (Java 25 preview) — what's the win?**
  - Source: `08_Modern-Java/05 Virtual Threads - Loom.md`
  - Expected: Automatic error handling (fail-fast/cancel-all), deadline propagation, structured concurrency; no orphaned subtasks.

- **Q: `ScopedValue` vs `ThreadLocal` — why the new API?**
  - Source: `08_Modern-Java/06 ScopedValue.md`
  - Expected: Immutable, no `remove()` leaks, cheap inheritance to child virtual threads, built for structured concurrency.

- **Q: `CompletableFuture` vs virtual threads + blocking code — which when?**
  - Source: `04_Concurrency/CompletableFuture.md`, `04_Concurrency/Executor Framework.md`
  - Expected: CF for async composition; virtual threads for synchronous-looking blocking I/O (JDBC, REST); don't mix blocking in CF pool.

- **Q: `volatile` vs `AtomicInteger` vs `synchronized` — decision matrix?**
  - Source: `04_Concurrency/Atomics and Volatile.md`, `04_Concurrency/Locks and Synchronizers.md`
  - Expected: `volatile` = visibility only; `Atomic*` = CAS single var; `synchronized` = compound actions; `StampedLock` = read-heavy.

---

## Spring (05_Spring)

- **Q: `@Transactional` — what's the proxy pitfall?**
  - Source: `05_Spring/Spring Transaction.md`
  - Expected: Self-invocation bypasses proxy; fix: extract to separate bean or use `AopContext.currentProxy()` / AspectJ.

- **Q: `@Bean` vs `@Component` — when each?**
  - Source: `05_Spring/Spring Core.md`, `05_Spring/Dependency Injection.md`
  - Expected: `@Component` on your classes; `@Bean` in `@Configuration` for 3rd-party, conditional, composed wiring.

- **Q: Virtual threads in Spring Boot 3.5 — one config line?**
  - Source: `05_Spring/Spring Boot.md`, `05_Spring/Spring Core.md`
  - Expected: `spring.threads.virtual.enabled=true`; `@Async`, events, scheduling run on virtual threads; use `ScopedValue` for context.

- **Q: Spring Security filter chain — where does authentication happen?**
  - Source: `05_Spring/Spring Security.md`
  - Expected: `UsernamePasswordAuthenticationFilter` → `AuthenticationManager` → `Authentication` in `SecurityContext`; JWT filter before.

---

## Design Patterns (06_Design-Patterns)

- **Q: Factory Method vs Abstract Factory — concrete difference?**
  - Source: `06_Design-Patterns/Creational/Factory Method.md`, `06_Design-Patterns/Creational/Abstract Factory.md`
  - Expected: FM = one product, subclass decides; AF = families of related products, runtime switchable.

- **Q: Singleton — why enum is best in Java?**
  - Source: `06_Design-Patterns/Creational/Singleton.md`, `01_Core-Java/Types/Singleton Class.md`
  - Expected: Serialization-safe, thread-safe, no reflection break, lazy; `INSTANCE` enum constant.

- **Q: Strategy vs State — how to distinguish?**
  - Source: `06_Design-Patterns/Behavioral/Strategy.md`, `06_Design-Patterns/Behavioral/State.md`
  - Expected: Strategy = client chooses algorithm; State = object changes behaviour as internal state changes.

- **Q: Decorator vs Proxy — same structure, different intent?**
  - Source: `06_Design-Patterns/Structural/Decorator.md`, `06_Design-Patterns/Structural/Proxy.md`
  - Expected: Decorator adds behaviour (open-ended); Proxy controls access (lazy, remote, protection).

---

## DSA (07_DSA)

- **Q: ArrayList vs LinkedList — get(i) vs add/remove at head?**
  - Source: `07_DSA/Array.md`, `07_DSA/Linked List.md`
  - Expected: Array = O(1) get, O(n) insert/delete middle; Linked = O(1) head/tail, O(n) get; cache locality favours array.

- **Q: HashMap internals — Java 8+ treeify threshold?**
  - Source: `07_DSA/HashMap.md`
  - Expected: Bucket → tree when size > 8 & capacity > 64; untreeify at 6; prevents hash collision DoS.

- **Q: Tree traversal — recursive vs iterative (stack) space?**
  - Source: `07_DSA/Trees.md`
  - Expected: Recursive = O(h) call stack (risk StackOverflow); Iterative = O(h) explicit stack; Morris = O(1) space.

---

## Modern Java 8→25 (08_Modern-Java, 09_Java-21-LTS)

- **Q: Java 25 delta — name 4 features with JEP numbers?**
  - Source: `00_Java-25-Overview/Whats New in Java 25.md`, `08_Modern-Java/README.md`
  - Expected: JEP 450 (Compact Headers), JEP 491 (Sync pinning fix), JEP 506 (ScopedValue final), JEP 507 (Primitive patterns preview), JEP 513 (Module imports).

- **Q: Records + Sealed + Pattern Matching — how do they compose?**
  - Source: `08_Modern-Java/01 Records.md`, `08_Modern-Java/02 Sealed Classes.md`, `08_Modern-Java/03 Pattern Matching.md`
  - Expected: Sealed interface permits records; pattern matching deconstructs records in `switch`; exhaustive check.

- **Q: `SequencedCollection` — what methods did it add?**
  - Source: `08_Modern-Java/04 Sequenced Collections.md`
  - Expected: `getFirst()`, `getLast()`, `addFirst(E)`, `addLast(E)`, `reversed()` — on List, Deque, LinkedHashSet/Map.

---

## LLD / Machine Coding (10_LLD-Machine-Coding)

- **Q: Parking Lot — how to avoid double-booking a spot?**
  - Source: `10_LLD-Machine-Coding/01_Parking-Lot.md`
  - Expected: Single lock on `park`/`unpark` (or per-floor); `fits()` check + write under same lock; availability derived.

- **Q: LRU Cache — O(1) get/put, how?**
  - Source: `10_LLD-Machine-Coding/06_LRU-Cache.md`
  - Expected: `LinkedHashMap` (access-order) or `HashMap` + doubly-linked list; move-to-front on access; evict tail.

- **Q: Vending Machine — state machine for inventory + payment?**
  - Source: `10_LLD-Machine-Coding/02_Vending-Machine.md`
  - Expected: States: Idle → Selecting → Paying → Dispensing; Strategy for pricing; Observer for inventory alerts.

---

## Cram Plan (7-Day)

| Day | Focus | Key Notes |
|-----|-------|-----------|
| 1 | Core: Object/Wrapper/POJO/Singleton, Interface, Overload | `01_Core-Java/Classes.md`, `Types/*` |
| 2 | OOP: 4 pillars, 5 inheritance types, sealed, super/final | `02_OOP/*`, `Inheritance/*` |
| 3 | Collections: ArrayList/LinkedList/Vector, HashSet/TreeSet, Queue/Deque | `03_Collections/*`, `List/*`, `Set/*` |
| 4 | Concurrency: lifecycle, 4 creation ways, 7 issues, virtual threads | `04_Concurrency/*` |
| 5 | Spring: IoC/DI/AOP, scopes, @Transactional, Security filter chain | `05_Spring/*` |
| 6 | Patterns: 22 GoF — Factory, Singleton, Observer, Strategy, Decorator | `06_Design-Patterns/*` |
| 7 | DSA + Mock: Array/LL/Stack/Queue/HashMap/Tree complexities, 5 timed mocks | `07_DSA/*`, this Bank |

---

## Related

- [[README|Java MOC]] • [[99_Revision/README|Revision MOC]] • [[99_Revision/Study Plan|Study Plan]] • [[99_Revision/Interactive Setup|Interactive Setup]]
- [[07_DSA/Cheat Sheet|DSA Cheat Sheet]] • [[06_Design-Patterns/Cheat Sheet|Patterns Cheat Sheet]] • [[01_Core-Java/Cheat Sheet|Core Java Cheat Sheet]]

---

*Category: Revision • Part of [[README|Java MOC]] • Source of truth: each topic's `## Interview Q&A` section*