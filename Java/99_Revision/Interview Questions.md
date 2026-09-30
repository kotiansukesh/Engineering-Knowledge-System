---
title: "Java Interview Index"
category: Java/99_Revision
tags: [interview, revision, MOC]
created: 2026-09-30
type: interview-bank
---

# Java Interview Index

> A searchable index over source-note interview material. It is not a separate study plan or cram calendar.

## All interview material

~~~dataview
TABLE WITHOUT ID
  file.link AS "Source Note",
  category AS "Category"
FROM "Java"
WHERE category AND file.folder != "Java/99_Revision"
SORT category ASC, file.name ASC
~~~

## Core Java and OOP

~~~dataview
TABLE WITHOUT ID file.link AS "Note"
FROM "Java/01_Core-Java" OR "Java/02_OOP"
WHERE category
SORT file.path ASC
~~~

## Collections and DSA

~~~dataview
TABLE WITHOUT ID file.link AS "Note"
FROM "Java/03_Collections" OR "Java/07_DSA"
WHERE category
SORT file.path ASC
~~~

## Concurrency, Spring and patterns

~~~dataview
TABLE WITHOUT ID file.link AS "Note"
FROM "Java/04_Concurrency" OR "Java/05_Spring" OR "Java/06_Design-Patterns"
WHERE category
SORT file.path ASC
~~~

## Rehearsal rule

Answer aloud first, then open the source note. Prefer:

**concept → concrete example → trade-off → failure mode**

Do not maintain dated cram schedules here. Use [[Study Plan]] for timing and [[Java/99_Revision/Study-Plan|Java Domain Syllabus]] for capability coverage.

## Related

- [[Java/README|Java MOC]]
- [[Java/99_Revision/Study-Plan|Java Domain Syllabus]]
- [[Coding Patterns/README|Coding Patterns]]
