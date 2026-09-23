---
title: "Study Plan — Java / Spring"
category: planning
tags: [study-plan, tasks, java, spring, jvm, concurrency, spaced-repetition]
created: 2026-09-26
completed: false
problems-solved: []
problems-solved-dates: {}
excalidraw: ""
---

# Study Plan — Java / Spring Practice

> Use with **Tasks plugin** (`Cmd+P → Tasks: Create or edit task`). Filter by `#java` tag.

---

## Weekly Schedule (Recurring)

### Monday — Core Java & JVM
- [ ] 🔄 **JVM Memory Model** — Review 1 concept [[Java/01_Core-Java/JVM Memory Model]] #java/core/jvm 📅 every Monday
- [ ] 🔄 **Java 25 Features** — Review 1 JEP [[Java/00_Java-25-Overview]] #java/core/java25 📅 every Monday
- [ ] 🔄 **Generics / Collections** — Practice 1 pattern [[Java/03_Collections]] #java/core/generics 📅 every Monday
- [ ] 🔄 **Streams / Lambdas** — Practice 1 pattern [[Java/01_Core-Java/Streams API]] #java/core/streams 📅 every Monday

### Tuesday — OOP & Design Patterns
- [ ] 🔄 **OOP Principles** — Review 1 principle [[Java/02_OOP]] #java/oop/principles 📅 every Tuesday
- [ ] 🔄 **Design Patterns** — Implement 1 pattern [[Java/06_Design-Patterns]] #java/oop/patterns 📅 every Tuesday
- [ ] 🔄 **Spring Core** — Review 1 concept [[Java/05_Spring]] #java/spring/core 📅 every Tuesday

### Wednesday — Concurrency
- [ ] 🔄 **Thread Model / Virtual Threads** — Review 1 concept [[Java/04_Concurrency]] #java/concurrency/threads 📅 every Wednesday
- [ ] 🔄 **Synchronization / Locks** — Practice 1 pattern #java/concurrency/locks 📅 every Wednesday
- [ ] 🔄 **Structured Concurrency** — Practice 1 task scope #java/concurrency/structured 📅 every Wednesday

### Thursday — Spring Ecosystem
- [ ] 🔄 **Spring Boot 3.5** — Review 1 feature [[Java/05_Spring]] #java/spring/boot 📅 every Thursday
- [ ] 🔄 **Spring Data / Transactions** — Practice 1 pattern #java/spring/data 📅 every Thursday
- [ ] 🔄 **Spring Security / WebFlux** — Review 1 topic #java/spring/security 📅 every Thursday

### Friday — Modern Java, Java 21 LTS, LLD
- [ ] 🔄 **Modern Java (Records, Sealed, Pattern Matching)** — Practice [[Java/08_Modern-Java]] #java/modern/features 📅 every Friday
- [ ] 🔄 **Java 21 LTS Features** — Review 1 feature [[Java/09_Java-21-LTS]] #java/modern/java21 📅 every Friday
- [ ] 🔄 **LLD / Machine Coding** — Practice 1 problem [[Java/10_LLD-Machine-Coding]] #java/lld/machine-coding 📅 every Friday

### Saturday — Mock Interview / Coding
- [ ] 🔄 **Timed Java Interview** — 5 Q&A + 1 coding problem (45 min) #java/mock 📅 every Saturday
- [ ] 🔄 **LeetCode / LLD Practice** — Solve 1 medium problem #java/practice 📅 every Saturday

### Sunday — Review & Spaced Repetition
- [ ] 🔄 **SR Review** — Review all notes where `sr-due <= today` #java/sr 📅 every Sunday
- [ ] 🔄 **Stale Review** — Review notes not reviewed in >7 days #java/stale 📅 every Sunday
- [ ] 🔄 **Update Frontmatter** — Set `reviewed = today`, `sr-due = next interval` #java/admin 📅 every Sunday

---

## Spaced Repetition Intervals

After reviewing a concept **cold** (without looking at notes):

| Repetition | Interval | When to Set `sr-due` |
|------------|----------|---------------------|
| 1st | +3 days | `sr-due = today + 3d` |
| 2nd | +7 days | `sr-due = today + 7d` |
| 3rd | +14 days | `sr-due = today + 14d` |
| 4th | +30 days | `sr-due = today + 30d` |
| 5th | +90 days | `sr-due = today + 90d` |

**Rule**: Only advance interval if you recall it *cold* (no hints, no peeking). If you struggle, reset to +3 days.

---

## How to Track Progress

In the note's frontmatter, add:

```yaml
completed: true          # When you've deeply studied the note
reviewed: "2026-09-26"   # Last review date
sr-due: "2026-09-29"     # Next spaced repetition due date
```

---

## Quick Filters (Tasks Plugin)

```tasks
# All Java tasks due this week
not done
tag includes #java
due before 2026-10-03
```

```tasks
# Concurrency practice
not done
tag includes #java/concurrency
```

```tasks
# Spring practice
not done
tag includes #java/spring
```

```tasks
# LLD / Machine Coding
not done
tag includes #java/lld
```

---

## Progress Tracking

| Week | Core JVM | OOP/Patterns | Concurrency | Spring | Modern/LLD | Total |
|------|----------|--------------|-------------|--------|------------|-------|
| 1 | /4 | /3 | /3 | /3 | /3 | /16 |
| 2 | /4 | /3 | /3 | /3 | /3 | /16 |
| 3 | /4 | /3 | /3 | /3 | /3 | /16 |
| 4 | /4 | /3 | /3 | /3 | /3 | /16 |

*Update manually each week. Target: ~16 topics × 5 reps = 80 reviews over 90 days.*

---

## Related

- [[Dashboard|Java Dashboard]]
- [[Java/99_Revision/Interview-Bank|Java Interview Bank]]
- [[README|Java MOC]]
- [[Master Dashboard|Global Dashboard]]
- [[_templates/Java Note Template.md|Java Note Template]]
- [[_templates/Java Diagram.excalidraw.md|Excalidraw Template]]