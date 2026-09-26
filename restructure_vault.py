#!/usr/bin/env python3
"""
Obsidian Vault Restructuring Script
Converts all notes across 4 vaults to Unified-Note-Template-v2.md structure.
Preserves valuable content (LeetCode problems, Interview Q&A, code examples).
"""

import os
import re
import yaml
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any

VAULT_ROOT = Path("/Users/sukesh/Documents/GitHub/Obsidian")
VAULTS = ["Java", "Architect", "AI", "Coding Patterns"]
BACKUP_DIR = VAULT_ROOT / f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

# Section mapping from old templates to unified template
SECTION_MAP = {
    # Java template sections
    "Why it Matters": "Why it Matters",
    "Diagram": "Diagram",
    "Code": "Code / Example",
    "Core Concepts": "Code / Example",  # merge into Code
    "When to use / not": "When to Use / When NOT",
    "When to use/not": "When to Use / When NOT",
    "Trade-offs": "Trade-offs",
    "Vs": "Vs Table",
    "Pitfalls": "Pitfalls",
    "Interview q&a": "Interview Q&A (Senior Depth)",
    "Interview Q&A": "Interview Q&A (Senior Depth)",
    "Related": "Related",
    
    # Architect template sections (with emojis)
    "🎯 Intent": "Intent",
    "💡 Why It Matters": "Why it Matters",
    "💡 Why it Matters": "Why it Matters",
    "🧩 Diagram": "Diagram",
    "💻 Code": "Code / Example",
    "✅ When to Use / ❌ When NOT to Use": "When to Use / When NOT",
    "When to Use / NOT": "When to Use / When NOT",
    "⚖️ Trade-offs": "Trade-offs",
    "🆚 Vs. Alternatives": "Vs Table",
    "🆚 Vs": "Vs Table",
    "⚠️ Pitfalls": "Pitfalls",
    "🎤 Interview Q&A": "Interview Q&A (Senior Depth)",
    "🔗 Related": "Related",
    
    # AI template sections (with emojis)
    "🎯 Intent": "Intent",
    "💡 Why It Matters": "Why it Matters",
    "🧩 Diagram": "Diagram",
    "💻 Code": "Code / Example",
    "✅ When to Use / ❌ When NOT": "When to Use / When NOT",
    "⚖️ Trade-offs": "Trade-offs",
    "🆚 Vs. Alternatives": "Vs Table",
    "⚠️ Pitfalls": "Pitfalls",
    "🎤 Interview Q&A": "Interview Q&A (Senior Depth)",
    "🔗 Related": "Related",
    "Key Points": "Why it Matters",  # merge
}

# Fields to preserve from old frontmatter
PRESERVE_FIELDS = [
    "title", "category", "tags", "leetcode", "created", "completed", 
    "reviewed", "sr-due", "difficulty", "source", "problems-solved", 
    "problems-solved-dates", "excalidraw", "weeks", "type", "pattern"
]

def parse_frontmatter(content: str) -> tuple[Dict, str]:
    """Parse YAML frontmatter and return (frontmatter_dict, body_content)."""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm = yaml.safe_load(parts[1]) or {}
            body = parts[2].lstrip('\n')
            return fm, body
    return {}, content

def extract_sections(body: str) -> Dict[str, str]:
    """Extract markdown sections (## Header) into a dict."""
    # Strip old footer first
    body = strip_old_footer(body)
    
    sections = {}
    current_section = "Preamble"
    current_content = []
    
    for line in body.split('\n'):
        match = re.match(r'^(#{2,3})\s+(.+)$', line)
        if match:
            level = len(match.group(1))
            section_name = match.group(2).strip()
            if current_content:
                sections[current_section] = '\n'.join(current_content).strip()
            current_section = section_name
            current_content = []
        else:
            current_content.append(line)
    
    if current_content:
        sections[current_section] = '\n'.join(current_content).strip()
    
    # Post-process: merge problem subsections into Problems section
    problem_subsections = [k for k in sections.keys() if re.match(r'^\d+\.\s', k)]
    if "Problems" in sections and problem_subsections:
        merged = [sections["Problems"]]
        for sub in sorted(problem_subsections):
            merged.append(sections[sub])
            del sections[sub]
        sections["Problems"] = '\n\n'.join(merged)
    
    return sections

def strip_old_footer(body: str) -> str:
    """Remove old footer lines (--- followed by *Category: ... *)."""
    lines = body.split('\n')
    # Find the last --- that precedes a *Category: line
    for i in range(len(lines) - 2, -1, -1):
        if lines[i].strip() == '---' and i + 1 < len(lines) and lines[i + 1].strip().startswith('*Category:'):
            # Remove from this --- to end
            return '\n'.join(lines[:i]).rstrip()
    return body

def clean_section_name(name: str) -> str:
    """Normalize section name by removing emojis and extra formatting."""
    # Remove emojis
    name = re.sub(r'[\U0001F300-\U0001FAFF]', '', name)
    # Remove markdown formatting
    name = re.sub(r'[*_`#]+', '', name)
    return name.strip()

def map_section(old_name: str) -> str:
    """Map old section name to unified template section."""
    cleaned = clean_section_name(old_name)
    
    # Direct match
    if cleaned in SECTION_MAP:
        return SECTION_MAP[cleaned]
    
    # Fuzzy match
    for key, value in SECTION_MAP.items():
        if cleaned.lower() in key.lower() or key.lower() in cleaned.lower():
            return value
    
    # Default: keep as-is but cleaned
    return cleaned

def merge_section_content(sections: Dict[str, str], target_section: str, source_sections: List[str]) -> str:
    """Merge content from multiple source sections into target."""
    merged = []
    for src in source_sections:
        if src in sections and sections[src].strip():
            merged.append(sections[src].strip())
    return '\n\n'.join(merged) if merged else ""

def convert_flashcards(content: str) -> str:
    """Convert various flashcard formats to unified #flashcard format."""
    # Java format: Q::A #flashcard
    content = re.sub(
        r'^(.+?)::\s*(.+?)\s+#flashcard$',
        r'#flashcard\n**Q:** \1 :: **A:** \2 #flashcard',
        content,
        flags=re.MULTILINE
    )
    # Already unified format: keep as-is
    return content

def ensure_flashcard_section(content: str) -> str:
    """Ensure Flashcards section exists with proper format."""
    if "## Flashcards" not in content and "## Flashcards (Spaced Repetition)" not in content:
        # Add at the end before Related
        flashcard_section = """

## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the trigger keyword for {{title}}? :: **A:** [trigger keywords] #flashcard

#flashcard
**Q:** Time/space complexity of {{title}}? :: **A:** Time: O(), Space: O() #flashcard

#flashcard
**Q:** When do you NOT use {{title}}? :: **A:** [mutating data / single query / need min-max] #flashcard

#flashcard
**Q:** Core Java 25 snippet for {{title}}? :: **A:** `record ... { static of(...) {} keyMethod() {} }` #flashcard
"""
        # Insert before Related section
        content = re.sub(r'(## Related)', flashcard_section + r'\1', content)
    return content

def ensure_tasks_section(content: str) -> str:
    """Ensure Practice Tasks section exists."""
    if "## Practice Tasks" not in content:
        tasks_section = """

## Practice Tasks (Tasks Plugin)
- [ ] Restate the intent from memory 📅 {{date:YYYY-MM-DD, +1}}
- [ ] Code the snippet without looking 📅 {{date:YYYY-MM-DD, +3}}
- [ ] Answer all Interview Q&A aloud 📅 {{date:YYYY-MM-DD, +7}}
- [ ] Review flashcards (Spaced Repetition) 📅 {{date:YYYY-MM-DD, +1}}

```tasks
not done
path includes {{file.folder}}
sort by due
limit 10
```
"""
        content = re.sub(r'(## Related)', tasks_section + r'\1', content)
    return content

def ensure_excalidraw_ref(content: str, category: str) -> str:
    """Add Excalidraw reference to the note header."""
    diagram_ref = f"> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → {category.replace('/', ' ').replace('_', ' ').lower()} Diagram`"
    
    if "🎨 **Visual diagram:**" not in content and "Visual diagram" not in content:
        # Add after the MOC link line
        content = re.sub(
            r'(> Part of \[\[README\|MOC\]\].*)\n',
            r'\1\n' + diagram_ref + '\n',
            content
        )
    return content

def build_unified_frontmatter(old_fm: Dict, vault: str, folder: str) -> Dict:
    """Build unified frontmatter from old frontmatter."""
    new_fm = {}
    
    # Preserve known fields
    for field in PRESERVE_FIELDS:
        if field in old_fm and old_fm[field] not in [None, "", [], {}]:
            new_fm[field] = old_fm[field]
    
    # Ensure required fields
    if "title" not in new_fm:
        new_fm["title"] = "{{title}}"
    if "category" not in new_fm:
        new_fm["category"] = folder
    if "tags" not in new_fm:
        new_fm["tags"] = []
    if "leetcode" not in new_fm:
        new_fm["leetcode"] = []
    if "created" not in new_fm:
        new_fm["created"] = datetime.now().strftime("%Y-%m-%d")
    if "completed" not in new_fm:
        new_fm["completed"] = False
    if "reviewed" not in new_fm:
        new_fm["reviewed"] = ""
    if "sr-due" not in new_fm:
        new_fm["sr-due"] = ""
    if "difficulty" not in new_fm:
        new_fm["difficulty"] = ""
    if "source" not in new_fm:
        new_fm["source"] = ""
    if "problems-solved" not in new_fm:
        new_fm["problems-solved"] = []
    if "problems-solved-dates" not in new_fm:
        new_fm["problems-solved-dates"] = {}
    if "excalidraw" not in new_fm:
        new_fm["excalidraw"] = ""
    if "weeks" not in new_fm:
        new_fm["weeks"] = ""
    if "type" not in new_fm:
        new_fm["type"] = "note"
    
    # Special handling per vault
    if vault == "Java" and "pattern" in old_fm:
        new_fm["pattern"] = old_fm["pattern"]
    if vault == "Coding Patterns" and "pattern" in old_fm:
        new_fm["pattern"] = old_fm["pattern"]
    
    return new_fm

def build_unified_body(sections: Dict[str, str], fm: Dict, vault: str, folder: str) -> str:
    """Build unified body content from extracted sections."""
    title = fm.get("title", "{{title}}")
    category = fm.get("category", folder)
    
    # Start with header
    body = f"# {title}\n\n"
    body += f"> Part of [[README|MOC]] • `{category}`"
    if fm.get("weeks"):
        body += f" • Weeks {fm['weeks']}"
    body += "\n"
    
    # Excalidraw reference with cleaner category name
    diagram_category = category.replace('/', ' ').replace('_', ' ').replace('-', ' ').lower()
    body += f"> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → {diagram_category} Diagram`\n\n"
    
    # Map and collect sections in unified order
    unified_order = [
        "Intent",
        "Why it Matters",
        "Diagram",
        "Problems",
        "Code / Example",
        "When to Use / When NOT",
        "Trade-offs",
        "Vs Table",
        "Pitfalls",
        "Interview Q&A (Senior Depth)",
        "Flashcards (Spaced Repetition)",
        "Practice Tasks (Tasks Plugin)",
        "Related"
    ]
    
    # Map old sections to unified
    mapped_sections = {}
    for old_name, content in sections.items():
        if old_name == "Preamble" and content.strip():
            # Preamble content goes to Intent if Intent is empty
            if "Intent" not in mapped_sections:
                # Clean up preamble - remove duplicate title and MOC links
                cleaned = clean_preamble(content.strip(), title)
                if cleaned:
                    mapped_sections["Intent"] = cleaned
        else:
            unified_name = map_section(old_name)
            if unified_name in mapped_sections:
                mapped_sections[unified_name] += "\n\n" + content.strip()
            else:
                mapped_sections[unified_name] = content.strip()
    
    # Build body in unified order
    for section in unified_order:
        if section in mapped_sections and mapped_sections[section].strip():
            content = mapped_sections[section].strip()
            
            # Special processing per section
            if section == "Code / Example":
                content = ensure_code_block_language(content)
            elif section == "Interview Q&A (Senior Depth)":
                content = ensure_qa_format(content)
            elif section == "Flashcards (Spaced Repetition)":
                content = convert_flashcards(content)
                # Replace template placeholders
                content = content.replace("{{title}}", title)
            elif section == "Practice Tasks (Tasks Plugin)":
                # Replace template placeholders with actual dates
                from datetime import datetime, timedelta
                today = datetime.now().strftime("%Y-%m-%d")
                day1 = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
                day3 = (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d")
                day7 = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
                content = content.replace("{{date:YYYY-MM-DD, +1}}", day1)
                content = content.replace("{{date:YYYY-MM-DD, +3}}", day3)
                content = content.replace("{{date:YYYY-MM-DD, +7}}", day7)
                content = content.replace("{{date:YYYY-MM-DD}}", today)
                content = content.replace("{{file.folder}}", folder)
            elif section == "Problems" and fm.get("leetcode"):
                # Problems section will be auto-populated from leetcode frontmatter
                pass
            
            body += f"## {section}\n\n{content}\n\n"
    
    # Ensure flashcards and tasks sections exist
    body = ensure_flashcard_section(body)
    body = body.replace("{{title}}", title)
    body = ensure_tasks_section(body)
    from datetime import datetime, timedelta
    today = datetime.now().strftime("%Y-%m-%d")
    day1 = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    day3 = (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d")
    day7 = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    body = body.replace("{{date:YYYY-MM-DD, +1}}", day1)
    body = body.replace("{{date:YYYY-MM-DD, +3}}", day3)
    body = body.replace("{{date:YYYY-MM-DD, +7}}", day7)
    body = body.replace("{{date:YYYY-MM-DD}}", today)
    body = body.replace("{{file.folder}}", folder)
    
    # Footer
    body += f"---\n\n*Category: {category} • Part of [[README|MOC]]"
    if vault == "Java" or vault == "Coding Patterns":
        body += " • Java 25"
    body += "*\n"
    
    return body

def clean_preamble(content: str, title: str) -> str:
    """Clean up preamble content - remove duplicate title and MOC links."""
    lines = content.split('\n')
    cleaned = []
    for line in lines:
        # Skip duplicate title
        if line.strip() == f"# {title}":
            continue
        # Skip MOC link lines that are duplicates
        if line.strip().startswith("> Part of [[") and "MOC" in line:
            continue
        cleaned.append(line)
    return '\n'.join(cleaned).strip()

def ensure_code_block_language(content: str) -> str:
    """Ensure code blocks have language specifiers."""
    # Add java to bare code blocks that look like Java
    content = re.sub(
        r'```\n(\s*(?:public|private|protected|static|class|interface|record|void|int|String|var|new|return|if|for|while)\b)',
        r'```java\n\1',
        content
    )
    content = re.sub(
        r'```\n(\s*(?:import|package)\b)',
        r'```java\n\1',
        content
    )
    return content

def ensure_qa_format(content: str) -> str:
    """Ensure Q&A format uses **Q:** **A:** style."""
    # Convert Q1. format to **Q1.** format
    content = re.sub(r'^(\d+\.)\s*\*\*(.+?)\*\*$', r'**\1 \2**', content, flags=re.MULTILINE)
    content = re.sub(r'^(Q\d+)\.\s*(.+)$', r'**\1:** \2', content, flags=re.MULTILINE)
    content = re.sub(r'^(A\d*)\.\s*(.+)$', r'**\1:** \2', content, flags=re.MULTILINE)
    return content

def process_note(file_path: Path, vault: str, folder: str, dry_run: bool = True) -> Dict:
    """Process a single note file."""
    content = file_path.read_text(encoding='utf-8')
    old_fm, body = parse_frontmatter(content)
    sections = extract_sections(body)
    
    new_fm = build_unified_frontmatter(old_fm, vault, folder)
    new_body = build_unified_body(sections, new_fm, vault, folder)
    
    # Build new content
    fm_yaml = yaml.dump(new_fm, sort_keys=False, allow_unicode=True, default_flow_style=False)
    new_content = f"---\n{fm_yaml}---\n\n{new_body}"
    
    result = {
        "file": str(file_path.relative_to(VAULT_ROOT)),
        "old_fm_keys": list(old_fm.keys()),
        "new_fm_keys": list(new_fm.keys()),
        "old_sections": list(sections.keys()),
        "new_sections": [s for s in [
            "Intent", "Why it Matters", "Diagram", "Problems", "Code / Example",
            "When to Use / When NOT", "Trade-offs", "Vs Table", "Pitfalls",
            "Interview Q&A (Senior Depth)", "Flashcards (Spaced Repetition)",
            "Practice Tasks (Tasks Plugin)", "Related"
        ] if s in new_body],
        "changed": content != new_content,
        "new_content": new_content if not dry_run else None
    }
    
    if not dry_run and result["changed"]:
        # Backup original
        backup_path = BACKUP_DIR / file_path.relative_to(VAULT_ROOT)
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file_path, backup_path)
        
        # Write new content
        file_path.write_text(new_content, encoding='utf-8')
    
    return result

def process_vault(vault: str, dry_run: bool = True) -> List[Dict]:
    """Process all notes in a vault."""
    vault_path = VAULT_ROOT / vault
    results = []
    
    # Files to skip entirely (special files that shouldn't use note template)
    skip_files = {
        "README.md", "Dashboard.md", "Dashboard.html", "Study Plan.md", 
        "FILE_NAMING.md", "Cheat Sheet.md", "Interview-Bank.md", 
        "DSA-Roadmap-AlgoMaster.md", "Master Dashboard.md",
        "Weekly Tracker.md", "Certification Guide.md", "2026 Trends Update.md",
        "Roadmap Overview.md", "Tech Stack.md", "Learning Philosophy.md",
        "Study Plan - Architect.md"
    }
    
    for md_file in vault_path.rglob("*.md"):
        # Skip templates, special files, node_modules
        rel_path = str(md_file.relative_to(vault_path))
        if any(skip in str(md_file) for skip in ["_templates", "node_modules"]):
            continue
        if md_file.name in skip_files:
            continue
        # Skip folder READMEs
        if md_file.name == "README.md" and md_file.parent != vault_path:
            continue
        
        folder = str(md_file.parent.relative_to(vault_path))
        result = process_note(md_file, vault, folder, dry_run)
        results.append(result)
    
    return results

def main():
    print("=" * 60)
    print("OBSIDIAN VAULT RESTRUCTURING")
    print("=" * 60)
    
    # Create backup directory
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Backup directory: {BACKUP_DIR}")
    
    # Dry run first
    print("\n--- DRY RUN ---")
    all_results = {}
    total_changes = 0
    
    for vault in VAULTS:
        print(f"\nProcessing {vault}...")
        results = process_vault(vault, dry_run=True)
        all_results[vault] = results
        changes = sum(1 for r in results if r["changed"])
        total_changes += changes
        print(f"  {len(results)} notes, {changes} would change")
        
        # Show sample changes
        for r in results[:3]:
            if r["changed"]:
                print(f"    ~ {r['file']}")
                print(f"      Old sections: {r['old_sections']}")
                print(f"      New sections: {r['new_sections']}")
    
    print(f"\nTotal: {total_changes} notes would change across all vaults")
    
    # Confirm before actual run
    if dry_run:
        print("\nDry run complete. Run with --apply to execute.")
        return
    
    # Actual run
    print("\n--- APPLYING CHANGES ---")
    for vault in VAULTS:
        print(f"\nProcessing {vault}...")
        results = process_vault(vault, dry_run=False)
        changes = sum(1 for r in results if r["changed"])
        print(f"  {changes} notes updated")
    
    print(f"\n✅ Restructuring complete. Backup at: {BACKUP_DIR}")

if __name__ == "__main__":
    import sys
    dry_run = "--apply" not in sys.argv
    main()