---
title: "Annotations"
category: Core-Java
tags: [java, annotations, interview, java25]
created: 2026-01-18
updated: 2026-09-02
---
# Annotations

> Annotations are metadata tags (`@Override`, `@Deprecated`, `@SuppressWarnings`) that attach declarative information to code elements. They do not change program logic directly, tools, compilers, and frameworks read them to enforce rules, generate code, or configure behavior.

## Why it matters

Attach machine-readable metadata to classes, methods, fields, and other elements without polluting business logic. Annotations enable declarative programming, frameworks act on *what* is declared rather than imperative wiring.

## When to use it

| Use | Avoid |
|-----|-------|
| Marking metadata for frameworks (Spring, JPA, JUnit) | Replacing type safety, don't use strings where an enum/type would do |
| Compiler checks (`@Override`, `@SuppressWarnings`) | Putting business logic inside annotation processors |
| Code generation / validation at compile or runtime | Over-annotating trivial code, adds noise without value |

### Built-in vs custom annotations

| Annotation | Purpose |
|------------|---------|
| `@Override` | Compiler verifies method actually overrides a supertype method |
| `@Deprecated` | Marks API as obsolete; compiler warns on usage |
| `@SuppressWarnings` | Silences specific compiler warnings |

Custom annotation declaration:

```java
import java.lang.annotation.*;
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
@interface Author { String name(); String date() default ""; }

class Service {
    @Author(name = "Sukesh", date = "2026-09-02")
    public void process() { System.out.println("working"); }
}
public class AnnotationsDemo {
    public static void main(String[] args) throws Exception {
        var m = Service.class.getMethod("process");
        var a = m.getAnnotation(Author.class);
        System.out.println(a.name() + " " + a.date());
    }
}
```

> **Rules:** Annotation elements are implicitly `abstract` methods, allowed types are primitives, `String`, `Class`, `enum`, other annotations, and arrays thereof. No `void`, no generics.

### Retention and target

Two core meta-annotations control *where* and *how long* an annotation lives:

```java
import java.lang.annotation.*;

// Retention — how long annotation is kept (SOURCE < CLASS < RUNTIME)
@Retention(RetentionPolicy.SOURCE)
@Retention(RetentionPolicy.CLASS)
@Retention(RetentionPolicy.RUNTIME)

// Target — which elements the annotation can annotate
@Target(ElementType.TYPE)
@Target(ElementType.FIELD)
@Target(ElementType.METHOD)
@Target(ElementType.PARAMETER)
@Target(ElementType.CONSTRUCTOR)
    }
}
```

| Retention | Kept in | Reflection? | Example |
|-----------|---------|-------------|---------|
| `SOURCE` | Source only | No | `@Override`, `@SuppressWarnings` |
| `CLASS` | `.class` file | No | Default if unspecified |
| `RUNTIME` | `.class` + JVM | Yes (`getAnnotation()`) | Spring, JPA, JUnit annotations |

> **Common mistake:** Forgetting `@Retention(RUNTIME)`, annotation exists in source/class but `getAnnotation()` returns `null` at runtime.

### Annotation processing

Two processing models, compile-time and runtime:

```java
import java.lang.annotation.*;
import java.lang.reflect.Method;

// Runtime retention enables reflective access
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
@interface RolesAllowed { String[] value(); }

class SecureService {
    @RolesAllowed({"ADMIN", "EDITOR"})
    public void deletePost() {}
}
```

**Compile-time processing (APT / Pluggable Annotation Processors):**

```java
// Processor runs during javac, generates code, validates, reports errors
import javax.annotation.processing.*;
import javax.lang.model.element.*;
import javax.tools.Diagnostic;

@SupportedAnnotationTypes("com.example.Builder")
@SupportedSourceVersion(javax.lang.model.SourceVersion.RELEASE_25)
public class BuilderProcessor extends AbstractProcessor {
 @Override
 public boolean process(Set<? extends TypeElement> annotations, RoundEnvironment roundEnv) {
 for (Element e : roundEnv.getElementsAnnotatedWith(Builder.class)) {
 // Generate source files, validate, or emit compiler errors
 processingEnv.getMessager().printMessage(Diagnostic.Kind.NOTE, "Processing " + e);
    }
}
```

| Model | When | How | Use case |
|-------|------|-----|----------|
| Runtime (Reflection) | JVM execution | `getAnnotation()` / `isAnnotationPresent()` | DI, routing, security checks |
| Compile-time (APT) | `javac` compilation | `AbstractProcessor` | Code generation (Lombok, MapStruct, Dagger) |

## A quick example

> **Java 25:** Annotations unchanged, `@Retention`/`@Target`/`@Inherited` and `AbstractProcessor` (APT) behave identically. `import module java.base` does not affect annotation resolution; runtime retention still required for `getAnnotation()`. No new annotation language feature in 25.

Runnable Java 25, custom annotation with retention/target and runtime processing:

```java
import java.lang.annotation.*;
import java.lang.reflect.Method;

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
@interface Retry {
 int attempts() default 3;
 long delayMs() default 1000;
 Class<? extends Throwable>[] retryOn() default {Exception.class};
}

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
    }
}
```

## Trade-offs
- Declarative, co-located metadata, no external XML/config drift.
- Enables powerful frameworks (Spring, Hibernate, JUnit) with minimal boilerplate.
- Compile-time checks (`@Override`) catch errors early.
## How it compares

| Aspect | Annotation | Interface |
|--------|------------|-----------|
| Purpose | Metadata / declarative config | Contract / behavior |
| Keyword | `@interface` | `interface` |
| Can have methods? | Elements only (restricted types, no body) | Abstract, default, static, private methods |
## Interview notes

**Q1. What are the retention policies and why do they matter?**
`SOURCE` (discarded after compilation), `CLASS` (in bytecode, not at runtime), `RUNTIME` (available via reflection). Framework annotations need `RUNTIME`; pure compile-time checks use `SOURCE`. Default is `CLASS`.

**Q2. How does annotation processing work at compile time vs runtime?**
Compile-time: `AbstractProcessor` runs during `javac`, can generate source files or emit errors (Lombok, Dagger). Runtime: reflection (`getAnnotation()`, `isAnnotationPresent()`) reads `RUNTIME` annotations to configure behavior (Spring, JUnit).
## Related

- [[Classes]]
- [[Interface]]
- [[Enums]]
- [[Types/Abstract Class|Abstract Class]]

## Pitfalls

- Forgetting `@Retention(RUNTIME)`, annotation invisible at runtime, `getAnnotation()` returns `null`.
- Using annotation where an interface/enum is more type-safe, annotations with `String` values lose compile-time checking.
- Over-annotating, every field/method annotated adds noise; use annotations only when a framework or tool consumes them.
- Expecting `@Inherited` on methods/fields, it only applies to class-level annotations.
- Mutable annotation elements, annotation values should be immutable; arrays should be defensively handled.
- Confusing `getAnnotation()` (checks inheritance) with `getDeclaredAnnotation()` (does not).

---
*Category: Core-Java • java25*
