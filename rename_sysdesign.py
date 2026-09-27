#!/usr/bin/env python3
"""
Rename all System Design Interview notes to consistent naming scheme.
"""

import os
import shutil
from pathlib import Path

TARGET = Path("/Users/sukesh/Documents/GitHub/Obsidian/Architect/10_System-Design-Interviews")

# New naming scheme: [Category]-[Number]-[Title].md
# Categories: FND (Foundational), NET (Networking), DB (Database), CACHE, ASYNC, COMM, SEC, REF, INT (Interview Problems), OOD, BB (ByteByteGo)

RENAME_MAP = {
    # Foundational (01-10)
    "01-System-Design-Overview.md": "FND-01-System-Design-Overview.md",
    "02-Performance-vs-Scalability.md": "FND-02-Performance-vs-Scalability.md",
    "03-Latency-vs-Throughput.md": "FND-03-Latency-vs-Throughput.md",
    "04-CAP-Theorem.md": "FND-04-CAP-Theorem.md",
    "05-Consistency-Patterns.md": "FND-05-Consistency-Patterns.md",
    "06-Availability-Patterns.md": "FND-06-Availability-Patterns.md",
    "07-DNS.md": "FND-07-DNS.md",
    "08-CDN.md": "FND-08-CDN.md",
    "52-Study-Guide.md": "FND-09-Study-Guide.md",
    "53-Interview-Approach.md": "FND-10-Interview-Approach.md",
    "54-Back-of-Envelope.md": "FND-11-Back-of-Envelope.md",
    "32-Powers-of-Two.md": "FND-12-Powers-of-Two.md",
    "33-Latency-Numbers.md": "FND-13-Latency-Numbers.md",
    
    # Networking (14-18)
    "09-Load-Balancer.md": "NET-01-Load-Balancer.md",
    "10-Reverse-Proxy.md": "NET-02-Reverse-Proxy.md",
    "11-Application-Layer-Microservices.md": "NET-03-Microservices-Service-Discovery.md",
    "28-TCP-vs-UDP.md": "NET-04-TCP-vs-UDP.md",
    "31-Security.md": "NET-05-Security.md",
    
    # Database (19-30)
    "12-RDBMS.md": "DB-01-RDBMS.md",
    "13-Master-Slave-Replication.md": "DB-02-Master-Slave-Replication.md",
    "14-Master-Master-Replication.md": "DB-03-Master-Master-Replication.md",
    "15-Federation.md": "DB-04-Federation.md",
    "16-Sharding.md": "DB-05-Sharding.md",
    "17-Denormalization.md": "DB-06-Denormalization.md",
    "18-SQL-Tuning.md": "DB-07-SQL-Tuning.md",
    "19-NoSQL.md": "DB-08-NoSQL.md",
    "20-SQL-vs-NoSQL.md": "DB-09-SQL-vs-NoSQL.md",
    
    # Caching (31-33)
    "21-Cache-Overview.md": "CACHE-01-Cache-Overview.md",
    "22-Cache-Strategies.md": "CACHE-02-Cache-Strategies.md",
    "23-Cache-Update-Strategies.md": "CACHE-03-Cache-Update-Strategies.md",
    
    # Asynchronism (34-37)
    "24-Asynchronism-Overview.md": "ASYNC-01-Asynchronism-Overview.md",
    "25-Message-Queues.md": "ASYNC-02-Message-Queues.md",
    "26-Task-Queues.md": "ASYNC-03-Task-Queues.md",
    "27-Back-Pressure.md": "ASYNC-04-Back-Pressure.md",
    
    # Communication (38-40)
    "29-RPC.md": "COMM-01-RPC.md",
    "30-REST.md": "COMM-02-REST.md",
    
    # Reference / Case Studies (41-44)
    "34-Additional-Interview-Questions.md": "REF-01-Additional-Interview-Questions.md",
    "35-Real-World-Architectures.md": "REF-02-Real-World-Architectures.md",
    "36-Company-Architectures.md": "REF-03-Company-Architectures.md",
    "37-Company-Engineering-Blogs.md": "REF-04-Company-Engineering-Blogs.md",
    
    # System Design Interview Problems (45-52) - Primer
    "38-Design-Pastebin-URL-Shortener.md": "INT-01-URL-Shortener-Pastebin.md",
    "39-Design-Twitter-Timeline.md": "INT-02-Twitter-Timeline.md",
    "40-Design-Web-Crawler.md": "INT-03-Web-Crawler.md",
    "41-Design-Mint.md": "INT-04-Mint-Financial-Aggregation.md",
    "42-Design-Social-Graph.md": "INT-05-Social-Graph.md",
    "43-Design-Key-Value-Store.md": "INT-06-Key-Value-Store-for-Search.md",
    "44-Design-Amazon-Sales-Rank.md": "INT-07-Amazon-Sales-Rank.md",
    "45-Design-System-on-AWS.md": "INT-08-System-on-AWS.md",
    
    # Object-Oriented Design (53-58)
    "46-Design-Hash-Map.md": "OOD-01-Hash-Map.md",
    "47-Design-LRU-Cache.md": "OOD-02-LRU-Cache.md",
    "48-Design-Call-Center.md": "OOD-03-Call-Center.md",
    "49-Design-Deck-of-Cards.md": "OOD-04-Deck-of-Cards.md",
    "50-Design-Parking-Lot.md": "OOD-05-Parking-Lot.md",
    "51-Design-Chat-Server.md": "OOD-06-Chat-Server.md",
    
    # ByteByteGo Patterns (59-86) - will renumber sequentially
    "Scaling-From-Zero-to-Millions-of-Users.md": "BB-01-Scaling-Zero-to-Millions.md",
    "Back-of-the-Envelope-Estimation.md": "BB-02-Back-of-Envelope-Estimation.md",
    "System-Design-Interview-Framework.md": "BB-03-System-Design-Framework.md",
    "Design-a-Rate-Limiter.md": "BB-04-Rate-Limiter.md",
    "Design-Consistent-Hashing.md": "BB-05-Consistent-Hashing.md",
    "Design-a-Key-Value-Store.md": "BB-06-Key-Value-Store.md",
    "Design-a-Unique-ID-Generator-Snowflake.md": "BB-07-Unique-ID-Generator-Snowflake.md",
    "Design-a-URL-Shortener-TinyURL.md": "BB-08-URL-Shortener.md",
    "Design-a-Web-Crawler.md": "BB-09-Web-Crawler.md",
    "Design-a-Notification-System.md": "BB-10-Notification-System.md",
    "Design-a-News-Feed-System.md": "BB-11-News-Feed-System.md",
    "Design-a-Chat-System-WhatsAppSlack.md": "BB-12-Chat-System.md",
    "Design-Search-Autocomplete.md": "BB-13-Search-Autocomplete.md",
    "Design-YouTube--Video-Streaming.md": "BB-14-YouTube-Video-Streaming.md",
    "Design-Google-Drive--File-Sync.md": "BB-15-Google-Drive-File-Sync.md",
    "Design-a-Proximity-Service-Yelp-Nearby.md": "BB-16-Proximity-Service.md",
    "Design-Nearby-Friends-Social-Proximity.md": "BB-17-Nearby-Friends.md",
    "Design-Google-Maps--Navigation.md": "BB-18-Google-Maps.md",
    "Design-a-Distributed-Message-Queue-Kafka-like.md": "BB-19-Distributed-Message-Queue.md",
    "Design-Metrics-Monitoring-and-Alerting.md": "BB-20-Metrics-Monitoring-Alerting.md",
    "Design-Ad-Click-Event-Aggregation.md": "BB-21-Ad-Click-Event-Aggregation.md",
    "Design-Hotel-Reservation-System.md": "BB-22-Hotel-Reservation-System.md",
    "Design-Distributed-Email-Service.md": "BB-23-Distributed-Email-Service.md",
    "Design-S3-like-Object-Storage.md": "BB-24-S3-like-Object-Storage.md",
    "Design-Real-time-Gaming-Leaderboard.md": "BB-25-Real-time-Gaming-Leaderboard.md",
    "Design-Payment-System.md": "BB-26-Payment-System.md",
    "Design-Digital-Wallet.md": "BB-27-Digital-Wallet.md",
    "Design-Stock-Exchange--Matching-Engine.md": "BB-28-Stock-Exchange-Matching-Engine.md",
}

# Files to DELETE (duplicates - keeping ByteByteGo version as it's more comprehensive)
DELETE_FILES = [
    # Duplicate: URL Shortener (keep BB-08)
    "38-Design-Pastebin-URL-Shortener.md",  # Actually this is primer, keep as INT-01
    # Duplicate: Web Crawler (keep BB-09)
    "40-Design-Web-Crawler.md",  # Keep as INT-03
    # These are NOT duplicates, they're different topics
]

# Actually, let's keep BOTH but with different prefixes so they're clearly separate sources
# Primer = INT- (Interview Problems from primer)
# ByteByteGo = BB- (ByteByteGo patterns)

def main():
    print("Renaming System Design Interview notes...")
    
    # First, verify all source files exist
    missing = []
    for src in RENAME_MAP.keys():
        if not (TARGET / src).exists():
            missing.append(src)
    
    if missing:
        print(f"Missing files: {missing}")
        return
    
    # Perform renames
    for src, dst in RENAME_MAP.items():
        src_path = TARGET / src
        dst_path = TARGET / dst
        
        if src_path.exists():
            if dst_path.exists():
                print(f"  SKIP (exists): {dst}")
            else:
                src_path.rename(dst_path)
                print(f"  ✅ {src} → {dst}")
        else:
            print(f"  MISSING: {src}")
    
    # Update frontmatter in renamed files
    update_frontmatter()
    
    print("\nDone!")

def update_frontmatter():
    """Update title and category in frontmatter of renamed files."""
    import yaml
    import re
    
    for src, dst in RENAME_MAP.items():
        file_path = TARGET / dst
        if not file_path.exists():
            continue
            
        content = file_path.read_text(encoding='utf-8')
        if not content.startswith('---'):
            continue
        
        parts = content.split('---', 2)
        if len(parts) < 3:
            continue
            
        fm = yaml.safe_load(parts[1]) or {}
        body = parts[2]
        
        # Update title from filename
        title = dst.replace('.md', '').replace('-', ' ')
        # Clean up category prefix
        for prefix in ['FND-', 'NET-', 'DB-', 'CACHE-', 'ASYNC-', 'COMM-', 'SEC-', 'REF-', 'INT-', 'OOD-', 'BB-']:
            if title.startswith(prefix):
                title = title[len(prefix):]
                break
        # Fix common patterns
        title = title.replace('Api', 'API').replace('Aws', 'AWS').replace('Ssl', 'SSL').replace('Rest', 'REST').replace('Rpc', 'RPC').replace('Sql', 'SQL').replace('Nosql', 'NoSQL').replace('Lru', 'LRU').replace('Ood', 'OOD')
        
        fm['title'] = title
        fm['category'] = "Architect/10_System-Design-Interviews"
        
        # Write back
        new_fm = "---\n" + yaml.dump(fm, sort_keys=False, allow_unicode=True, default_flow_style=False) + "---\n"
        file_path.write_text(new_fm + body, encoding='utf-8')

if __name__ == "__main__":
    main()