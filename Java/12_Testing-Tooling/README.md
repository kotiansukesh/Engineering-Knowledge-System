---
title: "12 Testing & Tooling"
category: "Java/12_Testing-Tooling"
type: "folder-MOC"
tags: [MOC, java, testing, tooling]
created: "2026-09-30"
completed: false
---

# 12 Testing & Tooling

> Feedback loops are part of Java engineering, not an afterthought.

## Topics

- [[JUnit 5|JUnit 5]] — unit-test structure, parameterized tests and assertions.
- [[Testcontainers|Testcontainers]] — realistic integration tests against disposable dependencies.
- [[Maven and Gradle|Maven and Gradle]] — build lifecycle, dependency management and reproducibility.

## Testing Pyramid for Backend Java

**Pure unit tests → component/integration tests → contract tests where needed → a small number of end-to-end tests**

The correct mix depends on architecture and failure modes.

## Related

- [[../05_Spring/README|Spring]]
- [[../11_JVM-Performance/README|JVM & Performance]]
- [[../README|Java MOC]]
