---
title: "Flexible Constructors and Module Imports"
category: Modern-Java
tags: [java25, jep513, jep511, constructor, modules]
created: 2026-09-03
completed: false
---

# Flexible Constructors & Module Imports — Java 25 (JEP 513, 511)

> **JEP 513** — statements before `super()`/`this()`: validate/compute before delegating. **JEP 511** — `import module java.base`: one import for all public types in a module.

## Why it matters

JEP 513 removes the "super must be first" workaround (static helpers). JEP 511 declutters scripts/small programs (not for large codebases — explicit imports still preferred).

## Runnable Java 25

```java
// Point — Flexible constructors (JEP 513) + module imports
class Point {
    int x, y;
    Point(int x, int y) { this.x = x; this.y = y; }
}
// PositivePoint — Flexible constructors (JEP 513) + module imports
class PositivePoint extends Point {
    PositivePoint(int x, int y) {
        if (x < 0 || y < 0) throw new IllegalArgumentException("negative");
        int nx = Math.max(x, 0);
        super(nx, y);
    }
}
// Box — Flexible constructors (JEP 513) + module imports

class Box {
    String s;
    Box(String s) { this.s = s; }
    Box() {
        String def = System.getenv("BOX_DEFAULT");
        if (def == null) def = "default";
        this(def);
    }
}

import module java.base;

void demo() {
    List<String> l = List.of("a","b");
    Path p = Path.of("/tmp/x");
    System.out.println(l + " " + p);
}
```

## How it compares

| Before 25 | Java 25 |
|-----------|---------|
| `super()` must be first statement | Statements before `super()`/`this()` allowed |
| `import java.util.*; import java.io.*;` | `import module java.base;` (one) |
| Static helper `static int validate(int x){...}` | Inline `if (x<0) throw...` before super |

## Interview Q&A

**Q: Can you `return` before `super()`?**  
No — `super()`/`this()` must be executed exactly once, no `return`/`throw` skipping it (unless you throw exception).

**Q: Does `import module` import transitive modules?**  
No — only public types exported by that module. `import module java.base` doesn't import `java.sql`.

**Q: When to use module import in production?**  
Rarely — prefer explicit imports for clarity; module import shines in demos, scripts, `jshell`.

## Pitfalls

- Using module import in large codebase — obscures dependencies; prefer explicit.
- Accessing `this` before `super()` — still forbidden; only static logic / params allowed.

## Related

- [[01 Records]] (compact constructor vs flexible super) • [[03 Pattern Matching]] • [[../01_Core-Java/Classes|Classes]]

---
*Category: Modern-Java • java25*
