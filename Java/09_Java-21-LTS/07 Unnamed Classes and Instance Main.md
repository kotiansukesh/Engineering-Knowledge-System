---
title: "Unnamed Classes and Instance Main — JEP 445 (Java 21 Preview)"
category: java21
tags: [java21, jep445, preview, interview]
created: 2026-09-03
completed: false
---

# Unnamed Classes and Instance Main — JEP 445 (Java 21 Preview)

> On-ramp: `void main(){}` and unnamed class `class Hello { void main(){...}}` — no `public static void main(String[] args)` boilerplate. **Preview in 21** (JEP 445), still evolving in 25.

## Intent

Lower ceremony for beginners/scripts — `java Hello.java` direct launch (JEP 458 in 21 also).

## Runnable Java 21 (Preview)

```bash
javac --enable-preview --release 21 Hello.java && java --enable-preview Hello
# Or: java --source 21 --enable-preview Hello.java
```

```java
// Unnamed classes + instance main — compact entry point
void main() {
    System.out.println("hello on 21");
}
```

**Prod LTS (no preview):**
```java
// Unnamed classes + instance main — compact entry point
public class Hello {
// Entry point — classic form; Java 25 also allows void main()
    public static void main(String[] args) { System.out.println("hello"); }
}
```

## Interview Q&A

**Q: Ship `void main(){}`?**  
No — preview; prod stays `public static void main(String[] args)`. Mention as on-ramp, not prod.

**Q: `java Hello.java` without compile?**  
Yes, JEP 458: Single-file source launcher — `java Hello.java` runs directly on 21.

## Pitfalls

- Confusing instance main with `public static` — instance `main` is non-static, no args.

## Related

- [[00 Java 21 Overview]] • [[05 String Templates]] • [[../01_Core-Java/Classes|Classes]]

---
*Category: java21*
