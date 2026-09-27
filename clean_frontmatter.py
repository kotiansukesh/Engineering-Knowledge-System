#!/usr/bin/env python3
"""
Clean frontmatter in each vault to only keep vault-specific fields.
"""

import yaml
import re
from pathlib import Path
from datetime import datetime

VAULT_ROOT = Path("/Users/sukesh/Documents/GitHub/Obsidian")

# Allowed fields per vault
VAULT_FIELDS = {
    "Java": {
        "allowed": ["title", "category", "tags", "created", "completed", "difficulty", "pattern", "reviewed", "sr-due", "source", "excalidraw", "type"],
        "remove": ["leetcode", "problems-solved", "problems-solved-dates", "weeks"]
    },
    "Architect": {
        "allowed": ["title", "category", "tags", "created", "completed", "difficulty", "reviewed", "sr-due", "source", "excalidraw", "weeks", "type"],
        "remove": ["leetcode", "pattern", "problems-solved", "problems-solved-dates"]
    },
    "AI": {
        "allowed": ["title", "category", "tags", "created", "completed", "difficulty", "reviewed", "sr-due", "source", "excalidraw", "weeks", "type"],
        "remove": ["leetcode", "pattern", "problems-solved", "problems-solved-dates"]
    },
    "Coding Patterns": {
        "allowed": ["title", "category", "tags", "leetcode", "created", "completed", "difficulty", "pattern", "source", "problems-solved", "problems-solved-dates", "reviewed", "sr-due", "excalidraw", "type"],
        "remove": ["weeks"]
    }
}

DEFAULTS = {
    "Java": {
        "pattern": 0,
        "difficulty": "Easy",
        "source": "",
        "excalidraw": "",
        "type": "note"
    },
    "Architect": {
        "difficulty": "Medium",
        "source": "",
        "excalidraw": "",
        "weeks": "",
        "type": "note"
    },
    "AI": {
        "difficulty": "Medium",
        "source": "",
        "excalidraw": "",
        "weeks": "",
        "type": "note"
    },
    "Coding Patterns": {
        "pattern": 1,
        "difficulty": "Easy",
        "source": "https://blog.algomaster.io/p/20-dsa-patterns",
        "problems-solved": [],
        "problems-solved-dates": {},
        "excalidraw": "",
        "type": "note"
    }
}

def parse_frontmatter(content: str):
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm_text = parts[1]
            # Only quote unquoted values containing colons
            def quote_if_needed(match):
                prefix = match.group(1)
                value = match.group(2).strip()
                # Already quoted?
                if value.startswith('"') or value.startswith("'"):
                    return match.group(0)
                # Contains colon and not empty?
                if ':' in value and value:
                    return f'{prefix}"{value}"'
                return match.group(0)
            
            fm_text = re.sub(r'^(\s*title:\s*)(.+)$', quote_if_needed, fm_text, flags=re.MULTILINE)
            fm_text = re.sub(r'^(\s*category:\s*)(.+)$', quote_if_needed, fm_text, flags=re.MULTILINE)
            fm_text = re.sub(r'^(\s*source:\s*)(.+)$', quote_if_needed, fm_text, flags=re.MULTILINE)
            
            # Fix empty arrays/objects
            fm_text = re.sub(r':\s*\[\s*\]', ': []', fm_text)
            fm_text = re.sub(r':\s*\{\s*\}', ': {}', fm_text)
            
            try:
                fm = yaml.safe_load(fm_text) or {}
            except yaml.YAMLError as e:
                print(f"YAML parse error, skipping: {e}")
                fm = {}
            body = parts[2].lstrip('\n')
            return fm, body
    return {}, content

def clean_vault(vault_name: str):
    vault_path = VAULT_ROOT / vault_name
    config = VAULT_FIELDS.get(vault_name, {"allowed": [], "remove": []})
    defaults = DEFAULTS.get(vault_name, {})
    allowed = set(config["allowed"])
    
    count = 0
    for md_file in vault_path.rglob("*.md"):
        if any(skip in str(md_file) for skip in ["_templates", "_attachments", "node_modules", "backup_"]):
            continue
        if md_file.name == "README.md":
            continue
            
        content = md_file.read_text(encoding='utf-8')
        fm, body = parse_frontmatter(content)
        
        # Remove disallowed fields
        for field in list(fm.keys()):
            if field not in allowed:
                del fm[field]
        
        # Add missing defaults
        for field, default in defaults.items():
            if field not in fm or fm[field] in [None, "", [], {}]:
                fm[field] = default
        
        # Ensure tags is list
        if "tags" in fm and isinstance(fm["tags"], str):
            fm["tags"] = [fm["tags"]]
        elif "tags" not in fm or fm["tags"] is None:
            fm["tags"] = []
        
        # Ensure leetcode is list (for Coding Patterns)
        if "leetcode" in fm and isinstance(fm["leetcode"], str):
            fm["leetcode"] = [fm["leetcode"]]
        elif "leetcode" not in fm and vault_name == "Coding Patterns":
            fm["leetcode"] = []
        
        # Normalize null/None values to empty strings or empty lists
        for field in ["reviewed", "sr-due", "source", "excalidraw", "weeks"]:
            if field in fm and fm[field] is None:
                fm[field] = ""
        
        if "tags" in fm and fm["tags"] is None:
            fm["tags"] = []
        
        # Fix category format
        folder = md_file.parent.relative_to(vault_path)
        expected_cat = f"{vault_name}/{folder}"
        if fm.get("category") != expected_cat:
            fm["category"] = expected_cat
        
        # Remove any remaining disallowed fields (in case they weren't caught)
        allowed = set(config["allowed"])
        for field in list(fm.keys()):
            if field not in allowed:
                del fm[field]
        
        # Write back - use custom YAML representer for clean output
        def clean_representer(dumper, data):
            if data is None or data == "":
                return dumper.represent_scalar('tag:yaml.org,2002:str', '')
            if isinstance(data, list) and len(data) == 0:
                return dumper.represent_sequence('tag:yaml.org,2002:seq', [])
            return dumper.represent_data(data)
        
        yaml.add_representer(type(None), lambda d, v: d.represent_scalar('tag:yaml.org,2002:str', ''))
        
        fm_yaml = "---\n" + yaml.dump(fm, sort_keys=False, allow_unicode=True, default_flow_style=False, width=1000) + "---\n"
        new_content = fm_yaml + "\n" + body
        md_file.write_text(new_content, encoding='utf-8')
        count += 1
    
    print(f"{vault_name}: {count} notes cleaned")
    return count

def main():
    print("Cleaning frontmatter per vault...")
    total = 0
    for vault in ["Java", "Architect", "AI", "Coding Patterns"]:
        total += clean_vault(vault)
    print(f"\nTotal: {total} notes updated")

if __name__ == "__main__":
    main()