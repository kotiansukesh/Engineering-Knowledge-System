---
title: "06 Architecture and Governance"
type: folder-MOC
tags: [MOC, architecture, governance, isaqb]
weeks: "31-36"
---
# 06_Architecture-Governance, Weeks 31–36 · ISAQB SWARC4AI

> Formalize architecture after building it. Part of [[AI/README|AI MOC]]

**Certification:** **iSAQB CPSA-A SWARC4AI**, 3-day (~24h), 20 Technical + 10 Method points
**Prereq:** Substantial AI systems built (Phases 01–05), course becomes reflection, not theory.
```dataview
TABLE WITHOUT ID file.link as "Note", category as "Category", weeks as "Weeks"
FROM "AI/06_Architecture-Governance"
WHERE file.name != "README"
SORT file.name ASC
```

## Progress

```dataview
TABLE WITHOUT ID file.link as "Note", choice(completed, "✅", "⬜") as "Done"
FROM "AI/06_Architecture-Governance"
WHERE category
SORT file.name ASC
```

## This Phase Formalizes

Quality attributes · Governance · Compliance · Model drift · AI lifecycle · MLOps · GenAI patterns · Enterprise integration

[[AI/05_Kubernetes-Operations/README|← 05_K8s-Ops]] • Next: [[AI/07_Cross-Cutting/README|07_Cross-Cutting]] • [[AI/99_Revision/README|99_Revision]]
