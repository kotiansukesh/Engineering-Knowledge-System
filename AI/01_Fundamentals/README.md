---
title: "01 Fundamentals"
type: folder-MOC
tags: [MOC, ai, fundamentals]
weeks: "1-4"
created: 2026-09-02
completed: false
reviewed:
sr-due:
---

# 01_Fundamentals, Weeks 1–4

> Build the muscle. Keep exactly as planned, no certs, pure engineering. Part of [[AI/README|AI MOC]]

**Focus:** Python · FastAPI · LLM APIs · Prompt Engineering · Structured Outputs · Tool Calling

```dataview
TABLE WITHOUT ID file.link as "Note", pattern as "Pat", category as "Category", weeks as "Weeks", difficulty as "Diff"
FROM "AI/01_Fundamentals"
WHERE file.name != "README"
SORT file.name ASC
```

## Progress (Spaced Repetition)

```dataview
TABLE WITHOUT ID
  file.link as "Note",
  choice(completed, "✅", "⬜") as "Done",
  choice(reviewed, "🔁", "⏳") as "Reviewed",
  choice(sr-due, "📅 " + sr-due, "—") as "SR Due"
FROM "AI/01_Fundamentals"
WHERE category
SORT file.name ASC
```

## This Phase Builds
- [[AI Backend Template]] — reusable FastAPI scaffold for all later phases
- 3 mini-projects: [[AI Coding Assistant]], [[Prompt Playground]], (Meeting Notes Generator — use [[AI Backend Template]] as base)

[[AI/README|← Back to AI MOC]] • Next: [[AI/02_RAG-Engineering/README|02_RAG-Engineering]]

---
*Category: AI/01_Fundamentals*