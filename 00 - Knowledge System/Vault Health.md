---
title: "Vault Health"
type: MOC
category: "Knowledge System"
status: active
---

# Vault Health

The CLI health report is the authoritative diagnostic for repository-level health.

Run:

```bash
python3 scripts/validate-vault-health.py
```

## In Obsidian

Use Dataview to inspect notes with incomplete metadata or stale review state:

```dataview
TABLE WITHOUT ID file.link AS "Note", type AS "Type", domain AS "Domain", reviewed AS "Reviewed", "last-verified" AS "Verified"
FROM ""
WHERE file.name != "README" AND (type = null OR title = null OR reviewed = null)
SORT file.path ASC
LIMIT 50
```

## Human review categories

- intentional orphan
- needs linking
- duplicate concept
- consolidation candidate
- deprecated
- freshness review

Health diagnostics never auto-delete knowledge.
