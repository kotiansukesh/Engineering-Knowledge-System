---
title: "Master Dashboard"
category: "AI"
type: "dashboard"
tags: [dashboard, dataview, sr, progress]
created: "2026-09-29"
completed: false
reviewed: "2026-09-29"
sr-due: "2026-09-30"
---

# Master Dashboard — AI Vault

> Real-time overview of all notes, spaced repetition status, and study progress.
> Open this note daily for your **Monday SR & Planning** ritual.

---

## 🎯 Today's Focus

```dataviewjs
const today = dv.date("now");
const due = dv.pages('"AI"').where(p => p.category && p.category.startsWith("AI/") && p["sr-due"] && dv.date(p["sr-due"]) <= today && p.file.name != "README" && p.type !== "folder-MOC" && p.type !== "root-MOC" && p.type !== "dashboard");
if (due.length > 0) {
    dv.table(["Note", "Category", "SR Due", "Days Overdue"], 
        due.sort(p => p["sr-due"]).map(p => [
            p.file.link,
            p.category,
            p["sr-due"],
            Math.floor((today - dv.date(p["sr-due"])) / (1000*60*60*24))
        ]));
} else {
    dv.paragraph("✅ **No notes due for review today!**");
}
```

---

## 📅 This Week's SR Schedule

```dataviewjs
const today = dv.date("now");
const weekEnd = dv.date(today).plus({days: 7});
const due = dv.pages('"AI"').where(p => p.category && p.category.startsWith("AI/") && p["sr-due"] && dv.date(p["sr-due"]) >= today && dv.date(p["sr-due"]) <= weekEnd && p.file.name != "README" && p.type !== "folder-MOC" && p.type !== "root-MOC" && p.type !== "dashboard");
if (due.length > 0) {
    dv.table(["Note", "Category", "SR Due", "Last Reviewed"], 
        due.sort(p => p["sr-due"]).map(p => [
            p.file.link,
            p.category,
            p["sr-due"],
            p.reviewed || "Never"
        ]));
} else {
    dv.paragraph("No SR reviews scheduled this week.");
}
```

---

## 📈 Progress by Phase

```dataviewjs
const phases = {
    "Phase 1: Foundations": ["AI/01_Fundamentals", "AI/02_RAG-Engineering"],
    "Phase 2: Agentic AI": ["AI/03_Agentic-AI"],
    "Phase 3: Production": ["AI/04_Production-Platform", "AI/05_Kubernetes-Operations"],
    "Phase 4: Governance": ["AI/06_Architecture-Governance", "AI/07_Cross-Cutting"]
};

for (const [phase, cats] of Object.entries(phases)) {
    const notes = dv.pages('"AI"').where(p => cats.includes(p.category) && p.file.name != "README" && p.type !== "folder-MOC" && p.type !== "root-MOC" && p.type !== "dashboard");
    const total = notes.length;
    const done = notes.where(p => p.completed === true).length;
    const pct = total ? Math.round(done/total*100) : 0;
    const bar = "█".repeat(Math.round(pct/10)) + "░".repeat(10-Math.round(pct/10));
    dv.paragraph(`**${phase}**: ${done}/${total} (\`${bar}\` ${pct}%)`);
}
```

---

## 🔴 Never Reviewed (Priority)

```dataview
TABLE WITHOUT ID
 file.link as "Note",
 category as "Category",
 difficulty as "Difficulty"
FROM "AI"
WHERE category AND category.startsWith("AI/") AND file.name != "README" AND type != "folder-MOC" AND type != "root-MOC" AND type != "dashboard" AND !reviewed
SORT category ASC, file.name ASC
LIMIT 20
```

---

## 🟡 Stale (>7 days since review)

```dataviewjs
const today = dv.date("now");
const stale = dv.pages('"AI"').where(p => p.category && p.category.startsWith("AI/") && p.reviewed && (today - dv.date(p.reviewed) > dv.duration({days: 7})) && p.file.name != "README" && p.type !== "folder-MOC" && p.type !== "root-MOC" && p.type !== "dashboard");
if (stale.length > 0) {
    dv.table(["Note", "Category", "Last Reviewed", "Days Ago"], 
        stale.sort(p => p.reviewed).map(p => [
            p.file.link,
            p.category,
            p.reviewed,
            Math.floor((today - dv.date(p.reviewed)) / (1000*60*60*24))
        ]));
} else {
    dv.paragraph("✅ No stale notes!");
}
```

---

## 📋 All Practice Tasks (Due Soon)

```tasks
not done
path includes AI
sort by due
limit 30
group by filename
```

---

## 🏷️ Tag Cloud (Top Concepts)

```dataviewjs
const notes = dv.pages('"AI"').where(p => p.category && p.category.startsWith("AI/") && p.file.name != "README" && p.type !== "folder-MOC" && p.type !== "root-MOC" && p.type !== "dashboard");
const tagCounts = {};
notes.forEach(p => {
    (p.tags || []).forEach(t => {
        if (!t.startsWith("#") && t !== "ai" && t !== "llm") {
            tagCounts[t] = (tagCounts[t] || 0) + 1;
        }
    });
});
const sorted = Object.entries(tagCounts).sort((a,b) => b[1]-a[1]).slice(0, 20);
if (sorted.length > 0) {
    dv.table(["Tag", "Count"], sorted.map(([tag, count]) => [`#${tag}`, count]));
}
```

---

## 🔗 Quick Actions

| Action | Link |
|--------|------|
| 📅 Open Study Plan | [[99_Revision/Study-Plan.md]] |
| 📝 Create New Note (Template) | `Cmd+P → Templates: Insert template → Unified-Note-Template` |
| 🎯 Daily Review Queue | [[Architect/_templates/Daily-Review-Queue]] |
| 📊 Folder MOCs | [[01_Fundamentals/README]], [[02_RAG-Engineering/README]], [[03_Agentic-AI/README]], [[04_Production-Platform/README]], [[05_Kubernetes-Operations/README]], [[06_Architecture-Governance/README]], [[07_Cross-Cutting/README]] |

---

*Category: AI Dashboard • Part of [[README|AI MOC]]*

## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the trigger keyword for {{title}}? :: **A:** [trigger keywords] #flashcard

#flashcard
**Q:** Key hyperparameter for {{title}}? :: **A:** [hyperparameter + typical range] #flashcard

#flashcard
**Q:** When do you NOT use {{title}}? :: **A:** [anti-pattern scenarios] #flashcard

#flashcard
**Q:** Cost order of magnitude for {{title}}? :: **A:** [GPU hours / $ per 1M tokens] #flashcard

## Practice Tasks (Tasks Plugin)
- [ ] Restate the intent from memory 📅 2026-09-30
- [ ] Code the config without looking 📅 2026-10-02
- [ ] Answer all Interview Q&A aloud 📅 2026-10-06
- [ ] Review flashcards (Spaced Repetition) 📅 2026-09-30

```tasks
not done
path includes AI
sort by due
limit 10
```

## Related
- [[README|AI MOC]]
- [[AI/README|AI Folder]]

---

*Category: {{category}} • Part of [[README|AI MOC]]*