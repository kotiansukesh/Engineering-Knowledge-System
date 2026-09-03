---
title: "Java 11 LTS Overview"
category: overview
tags: [java11, lts, overview, jep, interview]
created: 2026-09-03
completed: false
---

# Java 11 LTS Overview (Sep 2018) — The Quiet LTS

> Part of [[README|00 Overview]] • `overview` • **First LTS after 8.** Interviews test **var, new String/HttpClient APIs, single-file launch, and what was removed (Java EE, `var` limits).**

## TL;DR for interviews

> **Java 11 = Java 8 +** `var` (JEP 286), `String`/`Files`/`Collection` sugar, **`HttpClient` (standard)**, **single-file `java Hello.java`**, **nest-based access**, **ZGC/Epsilon (experimental)**, and **removals**: Java EE/CORBA (`javax.xml.bind` etc → Jakarta), `javac -source 8` no more.

## Must-Know Features

| Feature | JEP | 60-sec answer |
|---------|-----|---------------|
| **`var`** (LVTI) | 286 | `var x = List.of(1,2)` — **local only**, needs initializer, not field/param |
| **New String APIs** | — | `isBlank(), strip(), lines(), repeat(n)` |
| **`Collection`/`Files` sugar** | — | `List.of/CopyOf`, `Set.of`, `Map.of`, `Files.readString/writeString` |
| **`HttpClient`** (standard) | 321 | `HttpClient.newHttpClient().send(req, BodyHandlers.ofString())` — replaces `HttpURLConnection` |
| **Single-file launch** | 330 | `java Hello.java` — no `javac` |
| **Nest-based access** | 181 | `private` across nestmates without synthetic bridge — `String` ↔ inner |
| **ZGC / Epsilon (exp)** | 333/318 | Sub-ms GC introduced (prod in 21 as generational) |
| **Removals** | 320 | `javax.xml.bind` (JAXB), `javax.activation` → add Maven dep `jakarta.xml.bind` |

## Runnable Java 11 (`--release 11`)

```java
import java.net.http.*;
import java.net.URI;
import java.nio.file.*;
import java.util.*;

void demo11() throws Exception {
    var name = " Ava "; // var — local only, inferred String
    System.out.println(name.strip() + " blank? " + name.isBlank());
    System.out.println("hi\nlo".lines().toList());
    System.out.println("na".repeat(3));

    var list = List.of("a","b"); // immutable
    // Files sugar
    Path p = Path.of("/tmp/demo.txt");
    // Files.writeString(p, "hello 11"); String s = Files.readString(p);

    // HttpClient — standard in 11
    var client = HttpClient.newHttpClient();
    var req = HttpRequest.newBuilder(URI.create("https://example.com")).GET().build();
    // var resp = client.send(req, HttpResponse.BodyHandlers.ofString());
}
```

## When to Use / NOT

| Use | Avoid |
|-----|-------|
| `var` for verbose generics `var m = new HashMap<String,List<Integer>>()` | `var` for primitives obscuring type `var x = 1` (is `int`? `long`?) — explicit better |
| `List.of` for constants | `List.of(null)` → NPE; mutable need `new ArrayList<>(List.of(...))` |
| `HttpClient` for new HTTP | `HttpURLConnection` for new code |

## Vs — Java 8 → 11

| Before (8) | Java 11 |
|------------|---------|
| `String.trim().isEmpty()` | `strip().isBlank()` (Unicode-aware) |
| `HttpURLConnection` | `HttpClient` (HTTP/2, async `sendAsync`) |
| `javac Hello.java; java Hello` | `java Hello.java` |
| `javax.xml.bind` on JDK | Add `jakarta.xml.bind:jakarta.xml.bind-api` |

## Quick Check

- [ ] Where can `var` NOT be used? (field, param, no initializer, `var x = null`)
- [ ] `strip()` vs `trim()`?
- [ ] How to replace `JAXB` after 11 removal?
- [ ] `List.of` vs `Arrays.asList`?

## Pitfalls

- `var` with diamond: `var m = new ArrayList<>()` → `ArrayList<Object>` — specify `new ArrayList<String>()`.
- Assuming `Files.readString` streams large files — loads all into heap.

## Related

- [[Java 8 LTS Overview]] ← prev • [[Java 17 LTS Overview]] → next • [[LTS Evolution 8 to 25]] • [[Whats New in Java 25]]

---
*Category: overview • java11*
