#!/usr/bin/env python3
"""
Create cross-vault links between related concepts.
"""

import yaml
import re
from pathlib import Path

VAULT_ROOT = Path('/Users/sukesh/Documents/GitHub/Obsidian')

CROSS_LINKS = {
    # Java Concurrency <-> Architect Message Queues
    'Java/04_Concurrency/Concurrent Collections.md': {
        'links': [
            ('Architect/10_System-Design-Interviews/ASYNC-02-Message-Queues.md', 'Message Queues - distributed concurrency'),
            ('Architect/10_System-Design-Interviews/ASYNC-03-Event-Driven-Architecture.md', 'Event-driven patterns'),
        ]
    },
    'Java/04_Concurrency/Executor Framework.md': {
        'links': [
            ('Architect/10_System-Design-Interviews/ASYNC-01-Async-Patterns.md', 'Async patterns in distributed systems'),
        ]
    },
    'Java/04_Concurrency/CompletableFuture.md': {
        'links': [
            ('Architect/10_System-Design-Interviews/ASYNC-01-Async-Patterns.md', 'Async composition patterns'),
        ]
    },
    
    # Java Patterns <-> Architect Design Patterns
    'Java/06_Design-Patterns/Behavioral/Observer.md': {
        'links': [
            ('Architect/04_Design-Patterns-Building-Blocks/01_Enterprise-Patterns.md', 'Enterprise patterns - Observer'),
        ]
    },
    'Java/06_Design-Patterns/Behavioral/Command.md': {
        'links': [
            ('Architect/10_System-Design-Interviews/ASYNC-02-Message-Queues.md', 'Command pattern = message'),
        ]
    },
    'Java/06_Design-Patterns/Structural/Proxy.md': {
        'links': [
            ('Architect/10_System-Design-Interviews/NET-01-Load-Balancer.md', 'Proxy pattern for load balancing'),
        ]
    },
    
    # Coding Patterns <-> System Design
    'Coding Patterns/01_Array/03 - Sliding Window.md': {
        'links': [
            ('Architect/10_System-Design-Interviews/BB-04-Rate-Limiter.md', 'Sliding window rate limiting'),
            ('Architect/10_System-Design-Interviews/CACHE-02-Cache-Strategies.md', 'Sliding window cache eviction'),
        ]
    },
    'Coding Patterns/01_Array/02 - Two Pointers.md': {
        'links': [
            ('Architect/10_System-Design-Interviews/DB-05-Sharding.md', 'Two-pointer for range queries across shards'),
        ]
    },
    'Coding Patterns/05_Trees_Graphs/03 - BFS.md': {
        'links': [
            ('Architect/10_System-Design-Interviews/INT-03-Web-Crawler.md', 'Web crawler graph traversal'),
        ]
    },
    'Coding Patterns/05_Trees_Graphs/02 - DFS.md': {
        'links': [
            ('Architect/10_System-Design-Interviews/INT-03-Web-Crawler.md', 'DFS for deep crawling'),
        ]
    },
    'Coding Patterns/07_Backtracking_DP/01 - Backtracking.md': {
        'links': [
            ('Architect/10_System-Design-Interviews/OOD-01-Design-Parking-Lot.md', 'State space search in OOD'),
        ]
    },
    'Coding Patterns/07_Backtracking_DP/02 - Dynamic Programming.md': {
        'links': [
            ('Architect/10_System-Design-Interviews/DB-01-Database-Internals.md', 'DP for query optimization'),
        ]
    },
    'Coding Patterns/03_Stack_Heap/02 - Top K Elements.md': {
        'links': [
            ('Architect/10_System-Design-Interviews/NET-01-Load-Balancer.md', 'Least connections = min heap'),
            ('Architect/10_System-Design-Interviews/INT-02-Twitter-Timeline.md', 'Merge k sorted lists = heap'),
        ]
    },
    'Coding Patterns/05_Trees_Graphs/05 - Trie.md': {
        'links': [
            ('Architect/10_System-Design-Interviews/NET-05-API-Gateway.md', 'Trie for URL routing'),
            ('Architect/10_System-Design-Interviews/INT-08-Design-Autocomplete.md', 'Trie for autocomplete'),
        ]
    },
    
    # AI <-> System Design
    'AI/02_RAG-Engineering/Enterprise Document Search.md': {
        'links': [
            ('Architect/10_System-Design-Interviews/DB-04-Vector-Databases.md', 'Vector DB internals'),
            ('Architect/10_System-Design-Interviews/INT-08-Design-Autocomplete.md', 'Prefix search with vectors'),
        ]
    },
    'AI/02_RAG-Engineering/RAG Variants and Retrieval Strategies.md': {
        'links': [
            ('Architect/10_System-Design-Interviews/DB-04-Vector-Databases.md', 'Vector search in RAG'),
        ]
    },
}

def add_cross_links(file_path: Path, links: list):
    """Add cross-vault links to a note's Related section."""
    content = file_path.read_text(encoding='utf-8')
    if not content.startswith('---'):
        return False
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    fm = yaml.safe_load(parts[1]) or {}
    body = parts[2]
    
    # Find or create Related section
    link_lines = []
    for target, desc in links:
        link_lines.append(f"- [[{target}|{target.split('/')[-1].replace('.md', '')}]] — {desc}")
    
    new_links = '\n'.join(link_lines)
    
    if '## Related' in body:
        # Append to existing Related section
        pattern = r'(## Related\n)(.*?)(?=\n## |\Z)'
        def repl(m):
            return m.group(1) + m.group(2).rstrip() + '\n' + new_links + '\n'
        body = re.sub(pattern, repl, body, flags=re.DOTALL)
    else:
        # Add Related section before footer
        body += f"\n\n## Related\n\n{new_links}\n"
    
    new_fm = "---\n" + yaml.dump(fm, sort_keys=False, allow_unicode=True, default_flow_style=False) + "---\n"
    file_path.write_text(new_fm + body, encoding='utf-8')
    return True

def main():
    added = 0
    for source_rel, data in CROSS_LINKS.items():
        source_path = VAULT_ROOT / source_rel
        if not source_path.exists():
            print(f"  MISSING: {source_rel}")
            continue
        
        if add_cross_links(source_path, data['links']):
            print(f"  LINKED: {source_rel} -> {len(data['links'])} targets")
            added += 1
    
    print(f"\nTotal cross-links added: {added}")

if __name__ == '__main__':
    main()