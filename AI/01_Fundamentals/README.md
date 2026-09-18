---
title: "01 Fundamentals"
type: folder-MOC
tags: [MOC, fundamentals]
weeks: "1-4"
---
# 01_Fundamentals, Weeks 1–4 · no Certifications

> Build the muscle. Keep exactly as planned, no certs, pure engineering. Part of [[AI/README|AI MOC]]

**Focus:** Python · FastAPI · LLM APIs · Prompt Engineering · Structured Outputs · Tool Calling
```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category", weeks as "Weeks"
FROM "AI/01_Fundamentals"
WHERE file.name != "README"
SORT file.name ASC
```

## Progress

```dataview
TABLE WITHOUT ID file.link as "Note", choice(completed, "✅", "⬜") as "Done"
FROM "AI/01_Fundamentals"
WHERE category
SORT file.name ASC
```

## This Phase Builds

- [[AI Backend Template]], reusable FastAPI scaffold for all later phases
- 3 mini-projects: [[AI Coding Assistant]], [[Meeting Notes Generator]], [[Prompt Playground]]

[[AI/README|← Back to AI MOC]] • Next: [[AI/02_RAG-Engineering/README|02_RAG-Engineering]]
