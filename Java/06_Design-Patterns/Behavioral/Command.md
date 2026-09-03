---
title: "Command"
category: Design-Patterns
group: Behavioral
tags: [design-patterns, behavioral, command]
pattern: command
source: "https://refactoring.guru/design-patterns/command"
created: 2026-09-02
updated: 2026-09-02
---
# Command

> Category: Behavioral • Source: [Refactoring.Guru — Command](https://refactoring.guru/design-patterns/command) • Part of [[README|Java MOC]] → [[06_Design-Patterns/README|Design Patterns MOC]]

## Intent

Turns a request into an object so it can be stored, queued, or undone.

## Problem

Editor actions are tied to buttons. That blocks undo, queueing, and logging.

## Solution

Put each action behind a command interface with execute and undo. An invoker holds commands and keeps history. Records make queued commands immutable.

## Structure

```
Invoker → Command → Receiver (Editor). Copy and Paste are record commands. History stack enables undo.
```

## Trade-offs

Use when you need to parameterize actions, queue them, or support undo. Commands decouple invoker from receiver. The cost is one small type per action; records keep that cheap.

## Java example

```java

// Purpose: Command encapsulates request as object; invoker decoupled from receiver; supports undo/queue
// Participants: Cmd, Copy, Paste
// Structure: sealed hierarchy + records — exhaustive, immutable composition
// Behavior: wrapping/composition at runtime; no direct new of concrete in client
// Invariant: favors composition and abstraction over concrete coupling
```

Records keep data immutable and concise. Sealed plus switch makes the dispatch exhaustive without extra types.

## Versus

| Pattern | Use when |
|---------|----------|
| Command | Request as object, undo and queue |
| Strategy | Algorithm swap, not a queued request |

## Interview Q&A

**Q: Why store a command?**

To queue, log, or undo work. If you do not need those, a direct method call is simpler.

**Q: What is the simplest Java 25 way to write this?**

Record for data, sealed interface for the closed set, and switch for dispatch. Keep the example to about ten lines and use var at the call site.

---

*Category: Behavioral • Tags: design-patterns • Source: refactoring.guru*
