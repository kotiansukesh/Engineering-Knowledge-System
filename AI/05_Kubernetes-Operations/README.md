---
title: "05 Kubernetes Operations README"
category: "AI/05_Kubernetes-Operations"
type: "folder-MOC"
tags: [MOC, folder]
created: "2026-09-27"
completed: false
reviewed: ""
sr-due: ""
---

# 05 Kubernetes Operations

> **Supporting operations track — not a prerequisite for learning LLMs, RAG or agent fundamentals.**
>
> Enter this domain when the AI platform needs repeatable deployment, scaling, workload isolation, GPU scheduling, or Kubernetes-specific operational evidence.

## Scope

Prioritize the smallest operational slice required by the current project:

1. containers and deployment basics;
2. health, rollout and configuration management;
3. resource requests/limits and autoscaling;
4. observability and failure recovery;
5. workload isolation and policy;
6. GPU scheduling/Kubeflow only when the workload actually requires them.

Do not study Kubernetes features for their own sake. A working AI platform with measured operational requirements comes before platform-specific breadth.

> Part of [[README|AI MOC]] • `AI/05_Kubernetes-Operations`

## Progress Overview

```dataviewjs
const category = dv.current().category;
const pages = dv.pages(`"${category}"`).where(p => p.category != null && p.file.name != "README");
const total = pages.length;
const done = pages.where(p => p.completed === true).length;
const pct = total ? Math.round(done/total*100) : 0;
const bar = (p, w=20) => "█".repeat(Math.round(p/100*w)) + "░".repeat(w-Math.round(p/100*w));
dv.paragraph(`**Total: ${total} notes | Completed: ${done} | Remaining: ${total-done}** — \`${pct}%\``);
dv.paragraph(`\`${bar(pct)}\` **${pct}%**`);
if (total === done && total > 0) dv.paragraph(`🎉 *All notes completed!*`);
```

> **Fallback (if DataviewJS disabled):**
```dataview
TABLE WITHOUT ID
 length(rows) as "Total",
 length(filter(rows, (r) => r.completed)) as "Completed",
 length(filter(rows, (r) => !r.completed)) as "Remaining"
FROM "AI/05_Kubernetes-Operations"
WHERE category AND file.name != "README"
GROUP BY true
```

## Notes Index

```dataview
TABLE WITHOUT ID
 file.link as "Note",
 category as "Category",
 choice(completed, "✅", "⬜") as "Done",
 difficulty as "Difficulty",
 reviewed as "Last Reviewed",
 "sr-due" as "SR Due"
FROM "AI/05_Kubernetes-Operations"
WHERE category AND file.name != "README"
SORT file.name ASC
```

## Spaced Repetition Status

```dataview
TABLE WITHOUT ID
 file.link as "Note",
 reviewed as "Last Reviewed",
 "sr-due" as "Due",
 choice(!reviewed, "🔴 Never", choice(date(now)-reviewed > dur(7 days), "🟡 Stale", "🟢 Fresh")) as "Status"
FROM "AI/05_Kubernetes-Operations"
WHERE category AND file.name != "README" AND (reviewed OR "sr-due")
SORT "sr-due" ASC
```

## Practice Tasks (from Notes)

```tasks
not done
path includes AI/05_Kubernetes-Operations
sort by due
group by filename
limit 20
```


## Quick Links

- [[README|← Back to AI MOC]]
- [[Master Dashboard|📊 Master Dashboard]]

---

*Folder: AI/05_Kubernetes-Operations • Part of [[README|AI MOC]]*