#!/usr/bin/env python3
"""
Update all folder READMEs with enhanced Dataview + Tasks template.
"""

import os
from pathlib import Path
from datetime import datetime

VAULT_ROOT = Path("/Users/sukesh/Documents/GitHub/Obsidian")
VAULTS = {
    "Java": "Java",
    "Architect": "Architect", 
    "AI": "AI",
    "Coding Patterns": "Coding Patterns"
}

def get_folders(vault_path: Path) -> list:
    """Get all subdirectories that contain .md files (excluding _templates, _attachments, node_modules)."""
    folders = []
    for item in vault_path.iterdir():
        if item.is_dir() and item.name not in ["_templates", "_attachments", "node_modules", ".obsidian", ".git"]:
            # Check if folder has markdown files
            md_files = list(item.rglob("*.md"))
            if md_files:
                folders.append(item.name)
    return sorted(folders)

def generate_folder_readme(vault: str, folder: str) -> str:
    """Generate folder README content from template."""
    category = f"{vault}/{folder}"
    
    # Clean folder name for display
    display_name = folder.replace("_", " ").replace("-", " ")
    
    template = f'''---
title: "{display_name} README"
category: "{category}"
type: "folder-MOC"
tags: [MOC, folder]
created: "{datetime.now().strftime("%Y-%m-%d")}"
completed: false
reviewed: ""
sr-due: ""
---

# {display_name}

> Part of [[README|{vault} MOC]] • `{category}`

## Progress Overview

```dataviewjs
const pages = dv.pages(`"{category}"`).where(p => p.category && p.file.name != "README");
const total = pages.length;
const done = pages.where(p => p.completed).length;
const pct = total ? Math.round(done/total*100) : 0;
const bar = (p, w=20) => "█".repeat(Math.round(p/100*w)) + "░".repeat(w-Math.round(p/100*w));
dv.paragraph(`**Total: ${{total}} notes | Completed: ${{done}} | Remaining: ${{total-done}}** — \`${{pct}}%\``);
dv.paragraph(`\`${{bar(pct)}}\` **${{pct}}%**`);
if (total === done && total > 0) dv.paragraph(`🎉 *All notes completed!*`);
```

> **Fallback (if DataviewJS disabled):**
```dataview
TABLE WITHOUT ID
 length(rows) as "Total",
 length(filter(rows, (r) => r.completed)) as "Completed",
 length(filter(rows, (r) => !r.completed)) as "Remaining"
FROM "{category}"
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
FROM "{category}"
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
FROM "{category}"
WHERE category AND file.name != "README" AND (reviewed OR "sr-due")
SORT "sr-due" ASC
```

## Practice Tasks (from Notes)

```tasks
not done
path includes {category}
sort by due
group by filename
limit 20
```

## Quick Links

- [[README|← Back to {vault} MOC]]
- [[Master Dashboard|📊 Master Dashboard]]

---

*Folder: {category} • Part of [[README|{vault} MOC]]*
'''
    return template

def main():
    print("Updating folder READMEs...")
    
    for vault_name, vault_key in VAULTS.items():
        vault_path = VAULT_ROOT / vault_key
        folders = get_folders(vault_path)
        
        print(f"\n{vault_name}: {len(folders)} folders")
        
        for folder in folders:
            readme_path = vault_path / folder / "README.md"
            content = generate_folder_readme(vault_name, folder)
            
            readme_path.write_text(content, encoding='utf-8')
            print(f"  ✅ {folder}/README.md")
    
    print("\n✅ All folder READMEs updated!")

if __name__ == "__main__":
    main()