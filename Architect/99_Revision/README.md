---
title: "Revision Hub"
category: "Revision"
tags: [architect, revision, moc]
created: 2026-09-03
completed: false
---

# 99_Revision — Hub

> MOC for final prep: progress, links, cases, capstone.

## Progress
```dataview
TABLE completed AS Done, category AS Category
FROM "Architect"
WHERE completed != null
SORT file.name ASC
```
```dataviewjs
const ps = dv.pages('"Architect"').where(p => p.completed !== undefined);
const done = ps.where(p => p.completed).length;
dv.paragraph(`**Architect: ${done}/${ps.length} (${ps.length?Math.round(done/ps.length*100):0}%)**`);
const folders = ["08_NonFunctional-Ops","09_Governance-Documentation","99_Revision"];
for (const f of folders) {
  const q = dv.pages(`"${f}"`).where(p => p.completed !== undefined);
  const d = q.where(p => p.completed).length;
  dv.paragraph(`**${f}**: ${d}/${q.length}`);
}
```

## Map
- [[Interview-Bank|Interview Bank]] — rapid Q&A per topic
- [[Case-Studies|Case Studies]] — e-commerce · banking · AI platform
- [[../10_System-Design-Interviews/README|System Design Drills]] — TinyURL · Twitter · Uber · WhatsApp · Rate Limiter · Notifications · Instagram · YouTube · Dropbox · Crawler · Ticketmaster · Yelp
- [[Capstone-Checklist|Capstone Checklist]] — end-to-end design gate
- [[../08_NonFunctional-Ops/01_Security-OAuth2-JWT|Security]] · [[../09_Governance-Documentation/02_ADRs|ADRs]]

## Open tasks
```dataview
TASK WHERE !completed
SORT file.mtime ASC LIMIT 30
```
<!-- Concept: revision = retrieve + apply; hub routes you to bank, cases, capstone. -->
