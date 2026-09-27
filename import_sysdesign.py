#!/usr/bin/env python3
"""
Convert liquidslr system-design-notes to unified Obsidian template.
Creates notes in Architect/10_System-Design-Interviews/ and new folder for foundational patterns.
"""

import os
import re
from pathlib import Path
from datetime import datetime

SOURCE_DIR = Path("/tmp/sysdesign_notes")
TARGET_ROOT = Path("/Users/sukesh/Documents/GitHub/Obsidian/Architect")

# Mapping from source files to target locations
CHAPTER_MAP = {
    "01. Scaling": {
        "title": "Scaling: From Zero to Millions of Users",
        "folder": "10_System-Design-Interviews",
        "pattern": 1,
        "difficulty": "Easy",
        "tags": ["scaling", "architecture", "load-balancer", "caching", "cdn", "sharding", "replication"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/01.%20Scaling/Readme.md",
        "weeks": "1-2"
    },
    "02. Back Of the Envelope Estimation": {
        "title": "Back-of-the-Envelope Estimation",
        "folder": "10_System-Design-Interviews",
        "pattern": 2,
        "difficulty": "Easy",
        "tags": ["estimation", "capacity-planning", "latency", "throughput", "storage"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/02.%20Back%20Of%20the%20Envelope%20Estimation/Readme.md",
        "weeks": "2"
    },
    "03. System Design Framework": {
        "title": "System Design Interview Framework",
        "folder": "10_System-Design-Interviews",
        "pattern": 3,
        "difficulty": "Easy",
        "tags": ["interview", "framework", "process", "communication"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/03.%20System%20Design%20Framework/Readme.md",
        "weeks": "1"
    },
    "04. Rate Limiter": {
        "title": "Design a Rate Limiter",
        "folder": "10_System-Design-Interviews",
        "pattern": 4,
        "difficulty": "Medium",
        "tags": ["rate-limiting", "token-bucket", "leaking-bucket", "sliding-window", "redis", "api-gateway"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/04.%20Rate%20Limiter/Readme.md",
        "weeks": "3"
    },
    "05. Consistent Hashing": {
        "title": "Design Consistent Hashing",
        "folder": "10_System-Design-Interviews",
        "pattern": 5,
        "difficulty": "Medium",
        "tags": ["consistent-hashing", "sharding", "distributed-systems", "load-distribution"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/05.%20Consistent%20Hashing/Readme.md",
        "weeks": "3"
    },
    "06. Key-Value Store": {
        "title": "Design a Key-Value Store",
        "folder": "10_System-Design-Interviews",
        "pattern": 6,
        "difficulty": "Hard",
        "tags": ["key-value-store", "dynamo", "cassandra", "bigtable", "lsmtree", "consistency", "replication"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/06.%20Key-Value%20Store/Readme.md",
        "weeks": "4"
    },
    "07. Unique-Id Generator": {
        "title": "Design a Unique ID Generator (Snowflake)",
        "folder": "10_System-Design-Interviews",
        "pattern": 7,
        "difficulty": "Medium",
        "tags": ["unique-id", "snowflake", "distributed-id", "ticket-server", "uuid"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/07.%20Unique-Id%20Generator/Readme.md",
        "weeks": "3"
    },
    "08. URL Shortener": {
        "title": "Design a URL Shortener (TinyURL)",
        "folder": "10_System-Design-Interviews",
        "pattern": 8,
        "difficulty": "Medium",
        "tags": ["url-shortener", "base62", "hashing", "collision-resolution", "bloom-filter", "redirect"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/08.%20URL%20Shortener/Readme.md",
        "weeks": "4"
    },
    "09. Web Crawler": {
        "title": "Design a Web Crawler",
        "folder": "10_System-Design-Interviews",
        "pattern": 9,
        "difficulty": "Hard",
        "tags": ["web-crawler", "crawling", "politeness", "url-frontier", "deduplication", "robots-txt"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/09.%20Web%20Crawler/Readme.md",
        "weeks": "5"
    },
    "10. Notification System": {
        "title": "Design a Notification System",
        "folder": "10_System-Design-Interviews",
        "pattern": 10,
        "difficulty": "Medium",
        "tags": ["notification-system", "push-notification", "email", "sms", "webhook", "message-queue"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/10.%20Notification%20System/Readme.md",
        "weeks": "5"
    },
    "11. News Feed System": {
        "title": "Design a News Feed System",
        "folder": "10_System-Design-Interviews",
        "pattern": 11,
        "difficulty": "Hard",
        "tags": ["news-feed", "fan-out", "pull-vs-push", "ranking", "caching", "social-graph"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/11.%20News%20Feed%20System/Readme.md",
        "weeks": "6"
    },
    "12. Chat System": {
        "title": "Design a Chat System (WhatsApp/Slack)",
        "folder": "10_System-Design-Interviews",
        "pattern": 12,
        "difficulty": "Hard",
        "tags": ["chat-system", "websocket", "presence", "message-ordering", "group-chat", "push"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/12.%20Chat%20System/Readme.md",
        "weeks": "6"
    },
    "13. Search Autocomplete": {
        "title": "Design Search Autocomplete",
        "folder": "10_System-Design-Interviews",
        "pattern": 13,
        "difficulty": "Medium",
        "tags": ["autocomplete", "trie", "prefix-tree", "prefix-hash-tree", "ranking", "real-time"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/13.%20Search%20Autocomplete/Readme.md",
        "weeks": "7"
    },
    "14. Youtube": {
        "title": "Design YouTube / Video Streaming",
        "folder": "10_System-Design-Interviews",
        "pattern": 14,
        "difficulty": "Hard",
        "tags": ["video-streaming", "transcoding", "cdn", "adaptive-bitrate", "hls", "dash", "storage"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/14.%20Youtube/Readme.md",
        "weeks": "7"
    },
    "15. Google Drive": {
        "title": "Design Google Drive / File Sync",
        "folder": "10_System-Design-Interviews",
        "pattern": 15,
        "difficulty": "Hard",
        "tags": ["file-sync", "differential-sync", "conflict-resolution", "versioning", "dropbox"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/15.%20Google%20Drive/Readme.md",
        "weeks": "8"
    },
    "16. Proximity Service": {
        "title": "Design a Proximity Service (Yelp Nearby)",
        "folder": "10_System-Design-Interviews",
        "pattern": 16,
        "difficulty": "Hard",
        "tags": ["proximity", "geospatial", "quadtree", "geohash", "r-tree", "location-based"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/16.%20Proximity%20Service/Readme.md",
        "weeks": "8"
    },
    "17. Nearby Friends": {
        "title": "Design Nearby Friends (Social Proximity)",
        "folder": "10_System-Design-Interviews",
        "pattern": 17,
        "difficulty": "Hard",
        "tags": ["nearby-friends", "geospatial", "social-graph", "real-time", "pub-sub"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/17.%20Nearby%20Friends/README.md",
        "weeks": "9"
    },
    "18. Google Maps": {
        "title": "Design Google Maps / Navigation",
        "folder": "10_System-Design-Interviews",
        "pattern": 18,
        "difficulty": "Hard",
        "tags": ["maps", "navigation", "routing", "graph", "shortest-path", "traffic", "tiles"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/18.%20Google%20Maps/README.md",
        "weeks": "9"
    },
    "19. Distributed Message Queue": {
        "title": "Design a Distributed Message Queue (Kafka-like)",
        "folder": "10_System-Design-Interviews",
        "pattern": 19,
        "difficulty": "Hard",
        "tags": ["message-queue", "kafka", "pub-sub", "partitioning", "replication", "consumer-groups", "exactly-once"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/19.%20Distributed%20Message%20Queue/README.md",
        "weeks": "10"
    },
    "20. Metrics Monitoring and Alerting System": {
        "title": "Design Metrics Monitoring and Alerting",
        "folder": "10_System-Design-Interviews",
        "pattern": 20,
        "difficulty": "Medium",
        "tags": ["monitoring", "metrics", "alerting", "prometheus", "grafana", "observability", "slo"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/20.%20Metrics%20Monitoring%20and%20Alerting%20System/README.md",
        "weeks": "10"
    },
    "21. Ad Click Event Aggregation": {
        "title": "Design Ad Click Event Aggregation",
        "folder": "10_System-Design-Interviews",
        "pattern": 21,
        "difficulty": "Hard",
        "tags": ["ad-tech", "event-aggregation", "stream-processing", "flink", "exactly-once", "attribution"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/21.%20Ad%20Click%20Event%20Aggregation/README.md",
        "weeks": "11"
    },
    "22. Hotel Reservation System": {
        "title": "Design Hotel Reservation System",
        "folder": "10_System-Design-Interviews",
        "pattern": 22,
        "difficulty": "Hard",
        "tags": ["reservation", "booking", "distributed-transactions", "saga", "idempotency", "consistency"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/22.%20Hotel%20Reservation%20System/README.md",
        "weeks": "11"
    },
    "23. Distributed Email Service": {
        "title": "Design Distributed Email Service",
        "folder": "10_System-Design-Interviews",
        "pattern": 23,
        "difficulty": "Hard",
        "tags": ["email", "smtp", "queue", "retry", "spam", "deliverability", "attachments"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/23.%20Distributed%20Email%20Service/README.md",
        "weeks": "12"
    },
    "24. S3-like Object Storage": {
        "title": "Design S3-like Object Storage",
        "folder": "10_System-Design-Interviews",
        "pattern": 24,
        "difficulty": "Hard",
        "tags": ["object-storage", "s3", "erasure-coding", "multipart-upload", "versioning", "lifecycle"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/24.%20S3-like%20Object%20Storage/README.md",
        "weeks": "12"
    },
    "25. Real-time Gaming Leaderboard": {
        "title": "Design Real-time Gaming Leaderboard",
        "folder": "10_System-Design-Interviews",
        "pattern": 25,
        "difficulty": "Medium",
        "tags": ["leaderboard", "gaming", "redis", "sorted-set", "real-time", "ranking"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/25.%20Real-time%20Gaming%20Leaderboard/README.md",
        "weeks": "13"
    },
    "26. Payment System": {
        "title": "Design Payment System",
        "folder": "10_System-Design-Interviews",
        "pattern": 26,
        "difficulty": "Hard",
        "tags": ["payment", "transaction", "ledger", "idempotency", "reconciliation", "fraud", "pci-dss"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/26.%20Payment%20System/README.md",
        "weeks": "13"
    },
    "27.  Digital Wallet": {
        "title": "Design Digital Wallet",
        "folder": "10_System-Design-Interviews",
        "pattern": 27,
        "difficulty": "Hard",
        "tags": ["digital-wallet", "balance", "transaction", "ledger", "audit", "compliance"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/27.%20%20Digital%20Wallet/README.md",
        "weeks": "14"
    },
    "28. Stock Exchange": {
        "title": "Design Stock Exchange / Matching Engine",
        "folder": "10_System-Design-Interviews",
        "pattern": 28,
        "difficulty": "Hard",
        "tags": ["matching-engine", "order-book", "trading", "low-latency", "concurrency", "risk"],
        "leetcode": [],
        "source": "https://github.com/liquidslr/system-design-notes/blob/main/28.%20Stock%20Exchange/README.md",
        "weeks": "14"
    }
}

def clean_filename(name: str) -> str:
    """Convert chapter name to valid filename."""
    return re.sub(r'[^\w\s-]', '', name).strip().replace(' ', '-')

def parse_chapter(content: str, chapter_key: str) -> dict:
    """Parse chapter markdown into structured sections."""
    sections = {}
    current_section = "Introduction"
    current_content = []
    
    for line in content.split('\n'):
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

def convert_to_unified(sections: dict, meta: dict, chapter_key: str) -> str:
    """Convert parsed sections to unified template format."""
    title = meta["title"]
    category = f"Architect/{meta['folder']}"
    tags = meta["tags"]
    leetcode = meta["leetcode"]
    difficulty = meta["difficulty"]
    pattern = meta["pattern"]
    source = meta["source"]
    weeks = meta.get("weeks", "")
    
    # Build frontmatter
    fm = {
        "title": title,
        "category": category,
        "tags": tags,
        "leetcode": leetcode,
        "created": datetime.now().strftime("%Y-%m-%d"),
        "completed": False,
        "difficulty": difficulty,
        "pattern": pattern,
        "source": source,
        "reviewed": "",
        "sr-due": "",
        "problems-solved": [],
        "problems-solved-dates": {},
        "excalidraw": "",
        "weeks": weeks,
        "type": "note"
    }
    
    fm_yaml = "---\n" + "\n".join(f"{k}: {v}" if not isinstance(v, list) else f"{k}:\n" + "\n".join(f"  - {item}" for item in v) for k, v in fm.items()) + "\n---\n"
    
    # Build body
    body = f"# {title}\n\n"
    body += f"> Part of [[README|MOC]] • `{category}`"
    if weeks:
        body += f" • Weeks {weeks}"
    body += f"\n> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → {meta['folder'].replace('_', ' ').lower()} Diagram`\n\n"
    
    # Section order
    section_order = [
        "Introduction", "Intent", "Why it Matters", "Diagram", "Problems",
        "Code / Example", "When to Use / When NOT", "Trade-offs", "Vs Table",
        "Pitfalls", "Interview Q&A (Senior Depth)", "Flashcards (Spaced Repetition)",
        "Practice Tasks (Tasks Plugin)", "Related"
    ]
    
    # Map source sections to unified
    mapped = {}
    
    # Introduction -> Intent + Why it Matters
    if "Introduction" in sections:
        intro = sections["Introduction"]
        mapped["Intent"] = intro.split('\n')[0] if intro else ""
        mapped["Why it Matters"] = '\n'.join(intro.split('\n')[1:]) if len(intro.split('\n')) > 1 else ""
    
    # Step sections -> map appropriately
    for src_key, content in sections.items():
        if src_key == "Introduction":
            continue
        unified_key = map_section(src_key)
        if unified_key in mapped:
            mapped[unified_key] += "\n\n" + content
        else:
            mapped[unified_key] = content
    
    # Add Problems section if we have design problems
    mapped["Problems"] = f"### System Design Problem: {title}\n\n**Requirements:**\n- See chapter for detailed functional and non-functional requirements\n\n**Scale Estimates:**\n- See Back-of-the-Envelope Estimation chapter\n\n**API Endpoints:**\n- See chapter for API design\n\n**Constraints:**\n- High availability, scalability, fault tolerance\n"
    
    # Add Code/Example with Java snippet
    mapped["Code / Example"] = f"```java\n// Java 25: Core concept for {title}\n// This is a design pattern - implementation varies by system\n\nrecord {title.replace(' ', '').replace('-', '').replace('(', '').replace(')', '').replace('/', '')}Config(\n    String component,\n    int capacity,\n    String strategy\n) {{\n    static {title.replace(' ', '').replace('-', '').replace('(', '').replace(')', '').replace('/', '')}Config ofDefaults() {{\n        return new {title.replace(' ', '').replace('-', '').replace('(', '').replace(')', '').replace('/', '')}Config(\n            \"{title}\",\n            10000,\n            \"default\"\n        );\n    }}\n}}\n```\n\n### Concrete Example\n- **Input:** Design requirements from chapter\n- **Output:** Architecture diagram + component specs\n- **Explanation:** See chapter for step-by-step design"
    
    # Add When to Use / When NOT
    mapped.setdefault("When to Use / When NOT", "| **Use When** | **Avoid When** |\n|--------------|----------------|\n| Building this system from scratch | Using managed service (AWS SQS, Cloudflare, etc.) |\n| Learning system design patterns | Simple CRUD applications |\n| Interview preparation | When requirements don't match |\n")
    
    # Add Trade-offs
    mapped.setdefault("Trade-offs", "| Dimension | This Approach | Alternative |\n|-----------|---------------|-------------|\n| Complexity | High | Low (managed) |\n| Control | Full | Limited |\n| Operational Burden | High | Low |\n| Cost | Variable | Predictable |\n")
    
    # Add Vs Table
    mapped.setdefault("Vs Table", "| Aspect | This Design | Managed Service | Decision Rule |\n|--------|-------------|-----------------|---------------|\n| Flexibility | Full | Limited | Need custom logic? → Self-host |\n| Time to Market | Weeks | Hours | Prototype? → Managed |\n| Cost at Scale | Optimizeable | Fixed/marginal | High volume? → Self-host |\n")
    
    # Add Pitfalls
    mapped.setdefault("Pitfalls", "- Underestimating operational complexity\n- Ignoring failure modes (network partitions, disk failures)\n- Not planning for 10x scale from day one\n- Skipping monitoring/alerting in MVP\n- Premature optimization before measuring\n")
    
    # Add Interview Q&A (Senior Depth)
    mapped.setdefault("Interview Q&A (Senior Depth)", f"""**Q1: Walk me through the high-level architecture for {title}.**
**A:** [Summarize the 4-step framework: Requirements → High-level → Deep dive → Wrap-up. Key components: clients, API gateway, services, databases, caches, message queues. Use back-of-envelope to justify scale.]\n
**Q2: What are the key trade-offs in this design?**
**A:** [Consistency vs Availability (CAP), Latency vs Throughput, Build vs Buy, SQL vs NoSQL, Sync vs Async. Cite specific choices from chapter.]\n
**Q3: How does this scale to 10x traffic?**
**A:** [Horizontal scaling: stateless services, sharding, read replicas, caching layers, async processing via message queues. Identify bottlenecks from chapter.]\n
**Q4: What happens when [critical component] fails?**
**A:** [Failure handling from chapter: retries, circuit breakers, fallback, graceful degradation, data recovery.]\n
**Q5: How do you monitor and debug this in production?**
**A:** [Metrics: latency (p50/p99), error rate, throughput, saturation. Logging: structured, correlation IDs. Alerting: SLO-based, paging policies.]\n""")
    
    # Add Flashcards
    mapped["Flashcards (Spaced Repetition)"] = f"""#flashcard
**Q:** What is the core pattern for {title}? :: **A:** [Key algorithm/architecture from chapter] #flashcard

#flashcard
**Q:** When do you use {title.split('(')[0].strip()}? :: **A:** [Trigger scenarios from chapter] #flashcard

#flashcard
**Q:** Key trade-off in {title}? :: **A:** [Main trade-off: consistency/availability, latency/throughput, etc.] #flashcard

#flashcard
**Q:** Scale bottleneck for {title}? :: **A:** [Primary bottleneck from chapter] #flashcard"""
    
    # Add Practice Tasks
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
path includes {meta['folder']}
sort by due
limit 10
```"""
    
    # Add Related
    mapped.setdefault("Related", f"""- [[Architect/10_System-Design-Interviews/README|System Design Interviews Folder]]
- [[Architect/03_Architecture-Styles/README|Architecture Styles]]
- [[Architect/08_NonFunctional-Ops/README|Non-Functional Requirements]]
- [[Architect/07_Integration-APIs/README|Integration Patterns]]""")
    
    # Build final body
    for section in section_order:
        if section in mapped and mapped[section].strip():
            body += f"## {section}\n\n{mapped[section].strip()}\n\n"
    
    body += f"---\n\n*Category: {category} • Part of [[README|MOC]]*"
    
    return fm_yaml + "\n\n" + body

def map_section(src: str) -> str:
    """Map source section names to unified template sections."""
    src_lower = src.lower()
    if "step 1" in src_lower or "understand" in src_lower or "scope" in src_lower:
        return "Why it Matters"
    elif "step 2" in src_lower or "high.level" in src_lower or "buy.in" in src_lower:
        return "Diagram"
    elif "step 3" in src_lower or "deep dive" in src_lower:
        return "Code / Example"
    elif "step 4" in src_lower or "wrap" in src_lower:
        return "Interview Q&A (Senior Depth)"
    elif "algorithm" in src_lower or "approach" in src_lower or "design" in src_lower:
        return "Code / Example"
    elif "requirement" in src_lower:
        return "Why it Matters"
    elif "best practice" in src_lower or "dos" in src_lower or "don" in src_lower:
        return "Pitfalls"
    elif "time management" in src_lower:
        return "Pitfalls"
    elif "benefit" in src_lower:
        return "Why it Matters"
    elif "placement" in src_lower or "architecture" in src_lower:
        return "Diagram"
    elif "consideration" in src_lower or "challenge" in src_lower:
        return "Pitfalls"
    elif "comparison" in src_lower or "vs" in src_lower:
        return "Vs Table"
    elif "flow" in src_lower or "redirect" in src_lower or "shortening" in src_lower:
        return "Code / Example"
    elif "data model" in src_lower or "hash function" in src_lower:
        return "Code / Example"
    elif "additional" in src_lower or "scalability" in src_lower or "analytics" in src_lower:
        return "When to Use / When NOT"
    elif "conclusion" in src_lower or "takeaway" in src_lower:
        return "Why it Matters"
    else:
        return "Code / Example"

def main():
    print("Converting system design notes to unified template...")
    
    # Create target folder
    target_folder = TARGET_ROOT / "10_System-Design-Interviews"
    target_folder.mkdir(parents=True, exist_ok=True)
    
    for chapter_key, meta in CHAPTER_MAP.items():
        source_file = SOURCE_DIR / f"{chapter_key.replace(' ', '%20')}.md"
        if not source_file.exists():
            # Try with different encoding
            for f in SOURCE_DIR.iterdir():
                if chapter_key.replace('.', '').replace(' ', '') in f.name.replace('.', '').replace('%20', '').replace(' ', ''):
                    source_file = f
                    break
        
        if not source_file.exists():
            print(f"  ⚠ Source not found: {chapter_key}")
            continue
        
        content = source_file.read_text(encoding='utf-8')
        sections = parse_chapter(content, chapter_key)
        unified = convert_to_unified(sections, meta, chapter_key)
        
        filename = clean_filename(meta["title"]) + ".md"
        target_file = target_folder / filename
        target_file.write_text(unified, encoding='utf-8')
        print(f"  ✅ {filename}")
    
    print(f"\nDone! Created {len(CHAPTER_MAP)} notes in {target_folder}")
    
    # Update folder README
    update_folder_readme(target_folder)

def update_folder_readme(folder: Path):
    """Update the folder README with new notes."""
    readme = folder / "README.md"
    if readme.exists():
        # Just ensure it has the Dataview queries - they'll auto-pick up new notes
        print(f"  ℹ Folder README exists - Dataview will auto-include new notes")

if __name__ == "__main__":
    main()