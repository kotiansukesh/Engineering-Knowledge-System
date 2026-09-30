---
title: "JPMS Migration and Tooling"
category: "Java/01_Core-Java"
tags: [java, jpms, modules, migration, jdeps, jlink]
created: "2026-09-30"
completed: false
difficulty: "Advanced"
type: concept
---

# JPMS Migration and Tooling

> Companion to JPMS. Use JPMS for the module model; use this note when migrating a real codebase.

## Migration Strategy

1. Inventory dependencies with build-tool reports and jdeps.
2. Identify package ownership and split packages.
3. Create a small module boundary around a stable API.
4. Add requires/exports deliberately.
5. Add opens only where framework reflection requires it.
6. Keep third-party automatic modules isolated while migrating.
7. Test on the module path.
8. Use jlink only when a custom runtime has a measurable deployment benefit.

## Useful Tools

```bash
jdeps --summary app.jar
jdeps --print-module-deps app.jar
jlink --add-modules java.base,java.sql --output runtime
```

The exact command depends on the application and its dependency graph.

## Module Descriptor Example

```java
module com.example.orders {
    requires java.sql;

    exports com.example.orders.api;
    opens com.example.orders.persistence
        to org.hibernate.orm.core;
}
```

exports controls compile-time/readability access. opens enables deep reflection for the specified modules.

## Migration Pitfalls

- Split packages.
- Automatic module names that change when JAR filenames change.
- Framework reflection that was previously unrestricted on the classpath.
- Assuming Maven/Gradle dependency resolution is equivalent to JPMS readability.
- Introducing JPMS without a deployment or encapsulation requirement.

## When Not to Adopt JPMS

For a small service, library, or application where classpath packaging already provides adequate boundaries, JPMS may add migration cost without a meaningful benefit.

## Related

- JPMS
- [[Java/01_Core-Java/../12_Testing-Tooling/Maven and Gradle|Maven and Gradle]]
- [[Java/01_Core-Java/../05_Spring/Spring Boot|Spring Boot]]
