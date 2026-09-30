---
title: "Note Contract"
type: reference
category: "Knowledge System"
status: active
---

# Note Contract

Use this frontmatter for new durable notes:

```yaml
---
title: "Concept name"
domain: Java | Coding Patterns | AI | Architect | Cross-Domain
type: concept | pattern | reference | exercise | project | ADR | failure | evaluation | MOC
level: foundation | intermediate | advanced | expert
status: draft | active | reviewed | deprecated
tags: []
prerequisites: []
related: []
implementation: ""
evidence: []
source: []
applies-to: ""
introduced: ""
last-verified: ""
reviewed: ""
sr-due: ""
---
```

## Rules

- `title` is human-readable and stable.
- `domain` identifies the owning knowledge area.
- `type` determines how the note should be used.
- `prerequisites` and `related` contain Obsidian paths when known.
- `source` records provenance; prefer official documentation/specifications for fast-changing technology.
- `last-verified` is required for version-sensitive notes.
- Do not add metadata merely to satisfy a schema; metadata must have a query or workflow consumer.
- Existing domain-specific fields remain valid.
