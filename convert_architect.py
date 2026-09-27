#!/usr/bin/env python3
"""
Convert older Architect vault notes to unified template format.
Fixes emoji headers, section names, malformed frontmatter.
"""

import re
import yaml
from pathlib import Path
from datetime import datetime

VAULT_ROOT = Path("/Users/sukesh/Documents/GitHub/Obsidian/Architect")

# Emoji header mapping
EMOJI_SECTION_MAP = {
    "🎯 Intent": "Intent",
    "💡 Why It Matters": "Why it Matters",
    "💡 Why it Matters": "Why it Matters",
    "🧩 Diagram": "Diagram",
    "💻 Code": "Code / Example",
    "💻 Code:": "Code / Example",
    "✅ When to Use / ❌ When NOT to Use": "When to Use / When NOT",
    "✅ When to Use / ❌ When NOT": "When to Use / When NOT",
    "⚖️ Trade-offs": "Trade-offs",
    "🆚 Vs. Alternatives": "Vs Table",
    "🆚 Vs": "Vs Table",
    "⚠️ Pitfalls": "Pitfalls",
    "🎤 Interview Q&A (Senior Depth)": "Interview Q&A (Senior Depth)",
    "🎤 Interview Q&A": "Interview Q&A (Senior Depth)",
    "🔗 Related": "Related",
    "🔗 Related\n---": "Related",
    "TL;DR for Interviews": "Interview Q&A (Senior Depth)",  # Merge into Q&A
    "Quick Check": "Practice Tasks (Tasks Plugin)",  # Convert to practice tasks
    "Core Design": "Code / Example",
    "Spring Kafka, Idempotent Consumer": "Code / Example",
    "Outbox (Producer Side)": "Code / Example",
    "Comparison": "Vs Table",
    "URL Shortening Flow": "Code / Example",
    "URL Redirecting Flow": "Code / Example",
    "Additional Considerations": "When to Use / When NOT",
    "Conclusion": "Why it Matters",
    "Key Takeaways": "Why it Matters",
    "Best Practices": "Pitfalls",
    "Dos": "Pitfalls",
    "Don'ts": "Pitfalls",
    "Time Management": "Pitfalls",
}

def parse_frontmatter(content: str):
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm = yaml.safe_load(parts[1]) or {}
            body = parts[2].lstrip('\n')
            return fm, body
    return {}, content

def extract_sections(body: str):
    sections = {}
    current_section = "Preamble"
    current_content = []
    
    for line in body.split('\n'):
        match = re.match(r'^(#{2,3})\s+(.+)$', line)
        if match:
            if current_content:
                sections[current_section] = '\n'.join(current_content).strip()
            current_section = match.group(2).strip()
            current_content = []
        else:
            current_content.append(line)
    
    if current_content:
        sections[current_section] = '\n'.join(current_content).strip()
    
    return sections

def clean_section_name(name: str) -> str:
    # Remove emojis
    name = re.sub(r'[\U0001F300-\U0001FAFF]', '', name)
    # Remove markdown formatting
    name = re.sub(r'[*_`#]+', '', name)
    return name.strip()

def map_section(old_name: str) -> str:
    cleaned = clean_section_name(old_name)
    return EMOJI_SECTION_MAP.get(cleaned, EMOJI_SECTION_MAP.get(old_name, cleaned))

def fix_frontmatter(fm: dict, folder: str) -> dict:
    """Fix and standardize frontmatter."""
    new_fm = {}
    
    # Standard fields
    field_defaults = {
        "title": fm.get("title", "{{title}}"),
        "category": fm.get("category", f"Architect/{folder}"),
        "tags": fm.get("tags", []),
        "leetcode": fm.get("leetcode", []),
        "created": fm.get("created", datetime.now().strftime("%Y-%m-%d")),
        "completed": fm.get("completed", False),
        "reviewed": fm.get("reviewed", ""),
        "sr-due": fm.get("sr-due", ""),
        "difficulty": fm.get("difficulty", ""),
        "source": fm.get("source", ""),
        "pattern": fm.get("pattern", 0),
        "problems-solved": fm.get("problems-solved", []),
        "problems-solved-dates": fm.get("problems-solved-dates", {}),
        "excalidraw": fm.get("excalidraw", ""),
        "weeks": fm.get("weeks", ""),
        "type": fm.get("type", "note")
    }
    
    # Ensure tags is a list
    if isinstance(field_defaults["tags"], str):
        field_defaults["tags"] = [field_defaults["tags"]]
    elif not isinstance(field_defaults["tags"], list):
        field_defaults["tags"] = []
    
    # Ensure leetcode is a list
    if isinstance(field_defaults["leetcode"], str):
        field_defaults["leetcode"] = [field_defaults["leetcode"]]
    elif not isinstance(field_defaults["leetcode"], list):
        field_defaults["leetcode"] = []
    
    # Fix category format
    cat = field_defaults["category"]
    if not cat.startswith("Architect/"):
        if cat.startswith("Architect"):
            cat = cat.replace("Architect", "Architect")
        else:
            cat = f"Architect/{folder}"
    field_defaults["category"] = cat
    
    return field_defaults

def convert_qna_format(content: str) -> str:
    """Convert various Q&A formats to unified **Q:** **A:** format."""
    # Convert Q1: A: format
    content = re.sub(r'^\*\*(Q\d+)\*\*\s*(.+)$', r'**\1:** \2', content, flags=re.MULTILINE)
    content = re.sub(r'^\*\*(A\d*)\*\*\s*(.+)$', r'**\1:** \2', content, flags=re.MULTILINE)
    # Convert Q: A: format (already good)
    # Convert numbered Q format
    content = re.sub(r'^(\d+\.)\s*\*\*(.+?)\*\*$', r'**\1 \2**', content, flags=re.MULTILINE)
    return content

def convert_tasks(content: str) -> str:
    """Convert various task formats to Tasks plugin format."""
    # Convert checkbox format
    content = re.sub(r'^\-\s*\[\s*\]\s*(.+)$', r'- [ ] \1', content, flags=re.MULTILINE)
    content = re.sub(r'^\-\s*\[x\]\s*(.+)$', r'- [x] \1', content, flags=re.MULTILINE)
    return content

def build_unified_note(fm: dict, sections: dict, folder: str) -> str:
    """Build note in unified template format."""
    title = fm.get("title", "{{title}}")
    category = fm.get("category", f"Architect/{folder}")
    weeks = fm.get("weeks", "")
    
    # Sanitize title for Java record name
    java_name = re.sub(r'[^a-zA-Z0-9]', '', title.replace(' ', ''))
    if not java_name[0].isalpha():
        java_name = "Design" + java_name
    
    # Header
    body = f"# {title}\n\n"
    body += f"> Part of [[README|MOC]] • `{category}`"
    if weeks:
        body += f" • Weeks {weeks}"
    body += f"\n> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → {category.replace('/', ' ').replace('_', ' ').lower()} Diagram`\n\n"
    
    # Map sections
    mapped = {}
    for old_name, content in sections.items():
        if old_name == "Preamble" and content.strip():
            if "Intent" not in mapped:
                mapped["Intent"] = content.strip()
        else:
            unified_name = map_section(old_name)
            if unified_name in mapped:
                mapped[unified_name] += "\n\n" + content.strip()
            else:
                mapped[unified_name] = content.strip()
    
    # Section order
    section_order = [
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
    
    # Add default Problems section if missing
    if "Problems" not in mapped:
        mapped["Problems"] = f"### System Design Problem: {title}\n\n**Requirements:**\n- See note for detailed requirements\n\n**Constraints:**\n- High availability, scalability, fault tolerance\n"
    
    # Add default Code/Example if missing
    if "Code / Example" not in mapped:
        mapped["Code / Example"] = f"```java\n// Java 25: Core concept for {title}\n// Implementation varies by system\n\nrecord {java_name}Config(\n    String component,\n    int capacity,\n    String strategy\n) {{\n    static {java_name}Config ofDefaults() {{\n        return new {java_name}Config(\n            \"{title}\",\n            10000,\n            \"default\"\n        );\n    }}\n}}\n```\n\n### Concrete Example\n- **Input:** Design requirements\n- **Output:** Architecture diagram + component specs\n- **Explanation:** See note for step-by-step design"
    
    # Add default When to Use / When NOT
    if "When to Use / When NOT" not in mapped:
        mapped["When to Use / When NOT"] = "| **Use When** | **Avoid When** |\n|--------------|----------------|\n| Building this system from scratch | Using managed service |\n| Learning system design patterns | Simple CRUD applications |\n| Interview preparation | When requirements don't match |\n"
    
    # Add default Trade-offs
    if "Trade-offs" not in mapped:
        mapped["Trade-offs"] = "| Dimension | This Approach | Alternative |\n|-----------|---------------|-------------|\n| Complexity | High | Low (managed) |\n| Control | Full | Limited |\n| Operational Burden | High | Low |\n| Cost | Variable | Predictable |\n"
    
    # Add default Vs Table
    if "Vs Table" not in mapped:
        mapped["Vs Table"] = "| Aspect | This Design | Managed Service | Decision Rule |\n|--------|-------------|-----------------|---------------|\n| Flexibility | Full | Limited | Need custom logic? → Self-host |\n| Time to Market | Weeks | Hours | Prototype? → Managed |\n| Cost at Scale | Optimizeable | Fixed/marginal | High volume? → Self-host |\n"
    
    # Add default Pitfalls
    if "Pitfalls" not in mapped:
        mapped["Pitfalls"] = "- Underestimating operational complexity\n- Ignoring failure modes\n- Not planning for 10x scale\n- Skipping monitoring/alerting in MVP\n- Premature optimization before measuring\n"
    
    # Add default Interview Q&A
    if "Interview Q&A (Senior Depth)" not in mapped:
        mapped["Interview Q&A (Senior Depth)"] = f"""**Q1: Walk me through the high-level architecture for {title}.**
**A:** [Summarize key components and data flow. Use back-of-envelope to justify scale.]\n
**Q2: What are the key trade-offs in this design?**
**A:** [Consistency vs Availability, Latency vs Throughput, Build vs Buy, SQL vs NoSQL, Sync vs Async.]\n
**Q3: How does this scale to 10x traffic?**
**A:** [Horizontal scaling: stateless services, sharding, read replicas, caching layers, async processing.]\n
**Q4: What happens when [critical component] fails?**
**A:** [Failure handling: retries, circuit breakers, fallback, graceful degradation, data recovery.]\n
**Q5: How do you monitor and debug this in production?**
**A:** [Metrics: latency (p50/p99), error rate, throughput, saturation. Logging: structured, correlation IDs. Alerting: SLO-based.]\n"""
    
    # Convert existing Q&A format
    if "Interview Q&A (Senior Depth)" in mapped:
        mapped["Interview Q&A (Senior Depth)"] = convert_qna_format(mapped["Interview Q&A (Senior Depth)"])
    
    # Convert existing tasks
    if "Practice Tasks (Tasks Plugin)" in mapped:
        mapped["Practice Tasks (Tasks Plugin)"] = convert_tasks(mapped["Practice Tasks (Tasks Plugin)"])
    
    # Add Flashcards if missing
    if "Flashcards (Spaced Repetition)" not in mapped:
        mapped["Flashcards (Spaced Repetition)"] = f"""#flashcard
**Q:** What is the core pattern for {title}? :: **A:** [Key algorithm/architecture from note] #flashcard

#flashcard
**Q:** When do you use {title}? :: **A:** [Trigger scenarios from note] #flashcard

#flashcard
**Q:** Key trade-off in {title}? :: **A:** [Main trade-off] #flashcard

#flashcard
**Q:** Scale bottleneck for {title}? :: **A:** [Primary bottleneck] #flashcard"""
    
    # Add Practice Tasks if missing
    if "Practice Tasks (Tasks Plugin)" not in mapped:
        from datetime import timedelta
        today = datetime.now()
        day1 = (today + timedelta(days=1)).strftime("%Y-%m-%d")
        day3 = (today + timedelta(days=3)).strftime("%Y-%m-%d")
        day7 = (today + timedelta(days=7)).strftime("%Y-%m-%d")
        mapped["Practice Tasks (Tasks Plugin)"] = f"""- [ ] Explain the architecture from memory 📅 {day1}
- [ ] Draw the system diagram without looking 📅 {day3}
- [ ] Answer all Interview Q&A aloud 📅 {day7}
- [ ] Review flashcards (Spaced Repetition) 📅 {day1}

```tasks
not done
path includes {folder}
sort by due
limit 10
```"""
    
    # Convert tasks format if exists
    else:
        mapped["Practice Tasks (Tasks Plugin)"] = convert_tasks(mapped["Practice Tasks (Tasks Plugin)"])
        # Add Tasks plugin query if missing
        if "```tasks" not in mapped["Practice Tasks (Tasks Plugin)"]:
            from datetime import timedelta
            today = datetime.now()
            day1 = (today + timedelta(days=1)).strftime("%Y-%m-%d")
            day3 = (today + timedelta(days=3)).strftime("%Y-%m-%d")
            day7 = (today + timedelta(days=7)).strftime("%Y-%m-%d")
            mapped["Practice Tasks (Tasks Plugin)"] += f"""

```tasks
not done
path includes {folder}
sort by due
limit 10
```"""
    
    # Add default Related
    if "Related" not in mapped:
        mapped["Related"] = f"""- [[Architect/{folder}/README|{folder} Folder]]
- [[Architect/03_Architecture-Styles/README|Architecture Styles]]
- [[Architect/08_NonFunctional-Ops/README|Non-Functional Requirements]]
- [[Architect/07_Integration-APIs/README|Integration Patterns]]"""
    
    # Build body in order
    for section in section_order:
        if section in mapped and mapped[section].strip():
            body += f"## {section}\n\n{mapped[section].strip()}\n\n"
    
    # Footer
    body += f"---\n\n*Category: {category} • Part of [[README|MOC]]*"
    
    # Build frontmatter YAML
    fm_yaml = "---\n"
    for k, v in fm.items():
        if isinstance(v, list):
            fm_yaml += f"{k}:\n"
            for item in v:
                fm_yaml += f"  - {item}\n"
        else:
            fm_yaml += f"{k}: {v}\n"
    fm_yaml += "---\n"
    
    return fm_yaml + "\n\n" + body

def process_note(file_path: Path):
    content = file_path.read_text(encoding='utf-8')
    fm, body = parse_frontmatter(content)
    folder = file_path.parent.name
    
    # Fix frontmatter
    fm = fix_frontmatter(fm, folder)
    
    # Extract sections
    sections = extract_sections(body)
    
    # Build unified note
    new_content = build_unified_note(fm, sections, folder)
    
    # Write back
    file_path.write_text(new_content, encoding='utf-8')
    print(f"  ✅ {file_path.relative_to(VAULT_ROOT)}")

def main():
    print("Converting Architect vault notes to unified template...")
    
    # Skip the new system design notes (already unified) and READMEs
    skip_patterns = [
        "README.md",
        "Design-a-",
        "Scaling-From-Zero",
        "Back-of-the-Envelope",
        "System-Design-Interview-Framework",
        "backup_"
    ]
    
    count = 0
    for md_file in VAULT_ROOT.rglob("*.md"):
        if any(skip in str(md_file) for skip in ["_templates", "_attachments", "node_modules", "backup_"]):
            continue
        if md_file.name == "README.md":
            continue
        # Skip new system design notes (they already have unified format)
        if any(pattern in md_file.name for pattern in [
            "Design-a-", "Design-", "Scaling-From-Zero", "Back-of-the-Envelope", 
            "System-Design-Interview-Framework"
        ]):
            continue
        
        process_note(md_file)
        count += 1
    
    print(f"\nDone! Converted {count} notes")

if __name__ == "__main__":
    main()