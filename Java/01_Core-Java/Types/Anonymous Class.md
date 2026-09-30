---
title: Anonymous Class
category: Java/01_Core-Java/Types
tags:
- java
- class
- java25
created: 2026-01-18
pattern: 2
difficulty: Easy
completed: false
reviewed: "2026-09-29"
sr-due: "2026-10-06"
excalidraw: ''
source: ''
type: note
---

# Anonymous Class
> Part of [[Java/01_Core-Java/README|Core Java]]

> A class without a name, declared and instantiated in a single expression. It is a one-shot subclass of a class or implementor of an interface, typically used for short-lived overrides.

## Why it Matters

Provide a quick, inline implementation where creating a named class would be ceremony, especially for callbacks, listeners, and strategy objects (before lambdas).

## Diagram

```mermaid
classDiagram
 class Runnable {
 <<interface>>
 +run() void
 }
 Runnable <|.. Anon["new Runnable() {...}
(one-shot impl)"] : inline
```

## Code

> **Java 25:** Anonymous classes unchanged, still `new Type() { ... }`; prefer lambdas/method refs for SAM types (`Runnable`, `Comparator`) and local `var` for inference. No compact-source change for anonymous bodies.

Runnable Java 25, anonymous class vs lambda:
```java
import java.util.*;

public class AnonymousClassDemo {
 public static void main(String[] args) {
 // Anonymous class implementing Comparator
 Comparator<String> byLengthAnon = new Comparator<String>() {
 @Override public int compare(String a, String b) {
 return Integer.compare(a.length(), b.length());
 }
 };

 // Same with lambda (preferred for functional interfaces)
 Comparator<String> byLengthLambda = Comparator.comparingInt(String::length);
 }
}
```

## When to use / not

| Use | Avoid |
|-----|-------|
| One-off `Comparator`, `Runnable`, event listener | Logic reused in multiple places, make a named class |
| Need to override a few methods inline | Modern Java with functional interface, prefer lambda / method reference |
| Quick prototyping in tests | Complex logic, anonymous class harms readability |

## Trade-offs

- Concise inline customization.
- Captures enclosing scope (effectively final locals).
- Verbose vs lambdas for functional interfaces.

## Vs

| Aspect | Anonymous Class | Lambda | Named Inner Class |
|--------|----------------|--------|-------------------|
| Name | None (synthetic) | None | Yes |
| Can extend/implement | Any class / interface | Functional interfaces only | Any |
| State / ctor | Instance init only | No state | Full |

## Pitfalls

- Capturing non-effectively-final locals → compile error.
- Overusing anonymous classes for multi-method interfaces makes code hard to read, name it.
- Anonymous classes hold implicit reference to enclosing instance (memory leak risk in long-lived listeners).

---
*Category: Core-Java • java25*

## Interview q&a

**Q1. Anonymous class vs lambda, what's the difference?**
Lambdas are for functional interfaces only and don't introduce a new scope (`this` is enclosing instance); anonymous classes create a real subclass with its own `this` and can have state.

**Q2. Can an anonymous class have a constructor?**
No explicit constructor, but can use an instance initializer `{ ... }`.
Anonymous class vs lambda, what's the difference?:: Lambdas are for functional interfaces only and don't introduce a new scope (`this` is enclosing instance); anonymous classes create a real subclass with its own `this` and can have state. #flashcard
Can an anonymous class have a constructor?:: No explicit constructor, but can use an instance initializer `{ ... }`. #flashcard

## Related

- [[Java/01_Core-Java/Types/Nested/Anonymous Inner Class|Anonymous Inner Class]] (nested variant)
- [[Interface]], functional interfaces & lambdas
- [[Java/01_Core-Java/Types/Nested Classes Overview|Nested Classes Overview]]
