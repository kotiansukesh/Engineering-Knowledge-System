---
title: "Study Plans — Index"
category: Revision
tags: [plan, MOC, revision]
created: 2026-09-02
updated: 2026-09-02
---

# Study Plans — Pick Your Track

> You have **2 focused plans** (split from the old 30-day mega-plan). Start with **Java**, then **Spring**. Your dashboard is `Java/Dashboard.html`.

## 🟠 Java Plan — 21 Days (Core Java + DSA + Patterns)

> **File:** `[[Java Plan|99_Revision/Java Plan]]` • **Goal:** Java 25 fluency without Spring

| Week | Days | Focus | Key Notes |
|------|------|-------|-----------|
| W1 | 1-6 | Foundations | `01_Core-Java` (Classes → Streams/Optional/Date/Time) |
| W2 | 7-11 | OOP + Collections | `02_OOP` • `03_Collections` (Sequenced) |
| W3 | 12-21 | Concurrency + DSA + 20 Patterns + Mocks | `04_Concurrency` (virtual threads) • `07_DSA` • `Coding Patterns` |

**Start here:** [[Java Plan|→ Open Java Plan (21 days)]]

```dataview
TABLE WITHOUT ID file.link as "File", category as "Category"
FROM "Java/99_Revision"
WHERE contains(file.name, "Plan")
SORT file.name ASC
```

## 🟢 Spring Plan — 14 Days (Boot 3.5 + Patterns)

> **File:** `[[Spring Plan|99_Revision/Spring Plan]]` • **Prereq:** Java Plan Weeks 1-2 • **Goal:** Production Spring

| Week | Days | Focus | Key Notes |
|------|------|-------|-----------|
| W1 | 1-6 | Spring Core + Boot + MVC + JPA + Tx | `05_Spring` (Boot, MVC, JPA, Security, Transaction) + virtual threads |
| W2 | 7-14 | Security + GoF Patterns as Spring uses them + Mocks | `06_Design-Patterns` • full Controller→Service→Repo build |

**Next:** [[Spring Plan|→ Open Spring Plan (14 days)]]

## Combined (Legacy)

- [[30-Day Plan|30-Day Combined (legacy)]] — old 30-day mega-plan, kept for reference

## How to use

1. Open `Java/Dashboard.html` → chips `☕ Java Plan / 🍃 Spring Plan` filter progress + week view
2. In the markdown plan, tick `- [ ]` per day → set `completed: true` + `reviewed: 2026-09-03` in that note's frontmatter → `Java/README.md` Dataview turns ✅
3. Daily: 15 min SR queue (`#flashcard`) + 30 min Practice (LeetCode links in each note)

---
*Category: Revision • Part of [[README|Java MOC]] • Dashboard: `Java/Dashboard.html`*
