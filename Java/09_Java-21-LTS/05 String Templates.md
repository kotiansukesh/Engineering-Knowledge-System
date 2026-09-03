---
title: "String Templates — JEP 430 (Java 21 Preview)"
category: java21
tags: [java21, jep430, string-templates, interview, preview]
created: 2026-09-03
completed: false
---

# String Templates — JEP 430 (Java 21 Preview, Removed in 23)

> Preview interpolation: `STR."\{x} + \{y} = \{x+y}"` — **never finalized, withdrawn in Java 23**. Interview trap.

## Intent (had been)

Safe interpolation with template processors (`STR`, `FMT`, custom) — alternative to `+`/`String.format`.

## When to Use / NOT — Java 21 vs Now

| Java 21 Preview | Today (21 LTS prod) |
|---------|-----------------|
| `STR."Hello \{name}"` compiles with `--enable-preview` | **Don't ship** — removed in 23; use `"\{const}"` not available — use `String.format`, `MessageFormat`, or `StringBuilder` |
| `FMT."%02d\{d}"` | `String.format("%02d", d)` |

## Runnable Java 21 (Preview) — for interview recall

```bash
javac --enable-preview --release 21 Main.java && java --enable-preview Main
```

```java

```

**Today's replacement:**
```java
// String templates (preview) — safe interpolation vs concatenation
String s = "Hello %s, %d".formatted("Ava", 3);
String f = String.format("%04d", 42);
```

## Interview Q&A

**Q: String Templates final?**  
No — preview 21 & 22, **withdrawn** in 23 (JEP 430 removed). If interviewer asks `STR."..."`, say "preview then removed — use `formatted()`".

**Q: What ships on 21 LTS for strings?**  
Text blocks (`"""`), `formatted()`, `String.join`, `strip()` — not templates.

## Pitfalls

- Shipping `STR."..."` to prod — breaks on 23/25. Mention as historical preview only.

## Related

- [[00 Java 21 Overview]] • [[07 Unnamed Classes and Instance Main]] • [[../01_Core-Java/String Handling|String Handling]]

---
*Category: java21*
