#!/usr/bin/env python3
"""
Clean up unnecessary frontmatter fields per vault.
Each vault only needs relevant fields.
"""

import yaml
from pathlib import Path

VAULT_ROOT = Path("/Users/sukesh/Documents/GitHub/Obsidian")

# Fields per vault
VAULT_FIELDS = {
    "Java": {
        "required": ["title", "category", "tags", "created", "completed", "reviewed", "sr-due", "difficulty", "pattern", "source", "excalidraw", "type"],
        "optional": [],
        "remove": ["leetcode", "problems-solved", "problems-solved-dates", "weeks"]
    },
    "Architect": {
        "required": ["title", "category", "tags", "created", "completed", "reviewed", "sr-due", "difficulty", "source", "excalidraw", "type"],
        "optional": ["weeks"],
        "remove": ["leetcode", "pattern", "problems-solved", "problems-solved-dates"]
    },
    "AI": {
        "required": ["title", "category", "tags", "created", "completed", "reviewed", "sr-due", "difficulty", "source", "excalidraw", "weeks", "type"],
        "optional": [],
        "remove": ["leetcode", "pattern", "problems-solved", "problems-solved-dates"]
    },
    "Coding Patterns": {
        "required": ["title", "category", "tags", "leetcode", "created", "completed", "reviewed", "sr-due", "difficulty", "pattern", "source", "problems-solved", "problems-solved-dates", "excalidraw", "type"],
        "optional": ["weeks"],
        "remove": []
    }
}

def parse_frontmatter(content: str):
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm = yaml.safe_load(parts[1]) or {}
            body = parts[2].lstrip('\n')
            return fm, body
    return {}, content

def process_vault(vault_name: str):
    vault_path = VAULT_ROOT / vault_name
    config = VAULT_FIELDS.get(vault_name, {"required": [], "optional": [], "remove": []})
    remove_fields = set(config["remove"])
    keep_fields = set(config["required"] + config["optional"])
    
    count = 0
    for md_file in vault_path.rglob("*.md"):
        if "_templates" in str(md_file) or "backup_" in str(md_file):
            continue
        
        content = md_file.read_text(encoding='utf-8')
        fm, body = parse_frontmatter(content)
        
        # Remove unwanted fields
        changed = False
        for field in list(fm.keys()):
            if field in remove_fields:
                del fm[field]
                changed = True
        
        # Ensure required fields exist with defaults
        defaults = {
            "title": md_file.stem,
            "category": str(md_file.parent.relative_to(vault_path)),
            "tags": [],
            "created": "2026-09-27",
            "completed": False,
            "reviewed": "",
            "sr-due": "",
            "difficulty": "",
            "source": "",
            "excalidraw": "",
            "type": "note",
        }
        if vault_name == "Coding Patterns":
            defaults["leetcode"] = []
            defaults["pattern"] = 0
            defaults["problems-solved"] = []
            defaults["problems-solved-dates"] = {}
        if vault_name == "Java":
            defaults["pattern"] = 0
        if vault_name in ["Architect", "AI"]:
            defaults["weeks"] = ""
        
        for field, default in defaults.items():
            if field not in fm:
                fm[field] = default
                changed = True
        
        if changed:
            fm_yaml = yaml.dump(fm, sort_keys=False, allow_unicode=True, default_flow_style=False)
            new_content = f"---\n{fm_yaml}---\n\n{body}"
            md_file.write_text(new_content, encoding='utf-8')
            count += 1
    
    print(f"{vault_name}: {count} files cleaned")
    return count

def main():
    total = 0
    for vault in ["Java", "Architect", "AI", "Coding Patterns"]:
        total += process_vault(vault)
    print(f"\nTotal: {total} files updated")

if __name__ == "__main__":
    main()