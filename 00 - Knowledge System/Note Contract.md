---
title: "Note Contract"
type: reference
category: "Knowledge System"
status: active
---

# Note Contract

Use this frontmatter for new **durable knowledge notes**:

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
source-quality: []
applies-to: ""
introduced: ""
last-verified: ""
reviewed: ""
sr-due: ""
---
```

## Why `type` exists

`type` is a **semantic role**, not a generic file label.

Good values describe what the artifact is for:

- `concept` — explains a durable idea or mechanism.
- `pattern` — captures a reusable solution shape.
- `reference` — concise lookup material or authoritative reference.
- `exercise` — deliberate practice material.
- `project` — build/project definition or implementation record.
- `ADR` — architecture decision record.
- `failure` — failure experiment, incident analysis, or resilience lesson.
- `evaluation` — benchmark, evaluation, or assessment record.
- `MOC` — map of content / navigation note.

A specialized semantic value may be used when an existing workflow needs it (for example, a dashboard), but **do not use `type: note`**. If a file cannot be given a meaningful semantic role, it probably does not need a `type` field.

## What requires `type`

`type` is required for durable knowledge artifacts because Dataview, review workflows, navigation, and validation can use it to distinguish concepts, patterns, evidence, projects, decisions, failures, and other roles.

It is **not** required for every Markdown file.

The validator intentionally exempts:

- `README.md` navigation files
- `AGENTS.md` operating instructions
- template files/directories
- dashboard/control-plane support notes
- repository/tooling support files

## Rules

- `title` is human-readable and stable.
- `domain` identifies the owning knowledge area.
- `type` determines how the note should be used.
- `prerequisites` and `related` contain Obsidian paths when known.
- `source` records provenance; prefer official documentation/specifications for fast-changing technology.
- `last-verified` is required for version-sensitive notes.
- Do not add metadata merely to satisfy a schema; metadata must have a query or workflow consumer.
- Existing domain-specific fields remain valid.
- Do not use `type: note`; choose a meaningful role or omit `type` for support/navigation artifacts.

## Health

See Vault Health for diagnostics and review categories.
