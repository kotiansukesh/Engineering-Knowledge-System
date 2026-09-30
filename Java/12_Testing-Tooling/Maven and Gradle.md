---
title: "Maven and Gradle"
category: "Java/12_Testing-Tooling"
tags: [java, maven, gradle, build]
created: "2026-09-30"
completed: false
difficulty: "Medium"
type: "note"
---

# Maven and Gradle

## Intent

Make builds reproducible, dependency-aware and explicit about the Java version.

## Build Contract

A production Java build should make these facts visible:

- Java language/release target;
- dependency versions and scopes;
- test execution;
- packaging;
- static analysis/formatting where adopted;
- reproducible CI behavior.

## Maven Example

```xml
<properties>
  <maven.compiler.release>25</maven.compiler.release>
</properties>
```

The build, not the IDE, should decide which Java APIs and syntax are allowed.

## Dependency Hygiene

- keep direct dependencies explicit;
- inspect transitive dependencies;
- remove unused dependencies;
- pin or centrally manage versions;
- treat major framework upgrades as migration work, not version-number edits.

## Practice

- [ ] Build a small Java service with Maven.
- [ ] Set the compiler release explicitly.
- [ ] Run the build in CI using the same JDK family as local development.
- [ ] Explain one dependency conflict and how you diagnosed it.
