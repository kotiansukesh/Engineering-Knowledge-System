---
title: "Agent Workflow"
type: reference
category: "Knowledge System"
status: active
---

# Agent Workflow

AI agents working on this repository must preserve the vault's graph and validation rules.

## Operating loop

**START → Identify domain → Read MOC → Read target note → Check prerequisites → Find evidence → Change → Validate → Inspect links/metadata → Report**

## Retrieval rules

1. Start with the relevant MOC.
2. Read the target note and its prerequisites.
3. Search for existing canonical concepts before creating a duplicate.
4. Reuse existing evidence and ADRs when applicable.
5. Prefer official sources for fast-changing technology facts.

## Write rules

- Preserve useful existing knowledge.
- Prefer one canonical concept note.
- Use stable frontmatter.
- Create meaningful links, not link spam.
- Keep generated state out of prose when Dataview can derive it.
- Do not silently delete content; consolidate deliberately.

## Verification rules

Before completion:

```bash
python3 scripts/validate-vault.py
python3 scripts/validate-vault-health.py
```

Then inspect the changed paths, unresolved links, metadata errors and health warnings.
