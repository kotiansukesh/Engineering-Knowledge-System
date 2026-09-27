#!/usr/bin/env python3
"""
Fix frontmatter titles after rename - remove category prefix from title.
"""

import yaml
import re
from pathlib import Path

TARGET = Path("/Users/sukesh/Documents/GitHub/Obsidian/Architect/10_System-Design-Interviews")

# Category prefixes to strip
PREFIXES = ['FND-', 'NET-', 'DB-', 'CACHE-', 'ASYNC-', 'COMM-', 'REF-', 'INT-', 'OOD-', 'BB-']

# Manual title corrections for specific files
TITLE_CORRECTIONS = {
    "FND-04-CAP-Theorem.md": "Availability vs Consistency (CAP Theorem)",
    "FND-05-Consistency-Patterns.md": "Consistency Patterns",
    "FND-06-Availability-Patterns.md": "Availability Patterns",
    "FND-11-Back-of-Envelope.md": "Back-of-the-Envelope Calculations",
    "NET-03-Microservices-Service-Discovery.md": "Application Layer & Microservices",
    "NET-05-Security.md": "Security",
    "DB-09-SQL-vs-NoSQL.md": "SQL vs NoSQL",
    "CACHE-02-Cache-Strategies.md": "Cache Strategies",
    "CACHE-03-Cache-Update-Strategies.md": "When to Update Cache",
    "ASYNC-01-Asynchronism-Overview.md": "Asynchronism Overview",
    "ASYNC-04-Back-Pressure.md": "Back Pressure",
    "REF-01-Additional-Interview-Questions.md": "Additional System Design Interview Questions",
    "REF-02-Real-World-Architectures.md": "Real World Architectures",
    "REF-03-Company-Architectures.md": "Company Architectures",
    "REF-04-Company-Engineering-Blogs.md": "Company Engineering Blogs",
    "INT-01-URL-Shortener-Pastebin.md": "Design Pastebin / URL Shortener",
    "INT-02-Twitter-Timeline.md": "Design Twitter Timeline",
    "INT-03-Web-Crawler.md": "Design Web Crawler",
    "INT-04-Mint-Financial-Aggregation.md": "Design Mint.com",
    "INT-05-Social-Graph.md": "Design Social Graph",
    "INT-06-Key-Value-Store-for-Search.md": "Design Key-Value Store for Search",
    "INT-07-Amazon-Sales-Rank.md": "Design Amazon Sales Rank",
    "INT-08-System-on-AWS.md": "Design System on AWS",
    "OOD-01-Hash-Map.md": "Design Hash Map",
    "OOD-02-LRU-Cache.md": "Design LRU Cache",
    "OOD-03-Call-Center.md": "Design Call Center",
    "OOD-04-Deck-of-Cards.md": "Design Deck of Cards",
    "OOD-05-Parking-Lot.md": "Design Parking Lot",
    "OOD-06-Chat-Server.md": "Design Chat Server",
    "BB-01-Scaling-Zero-to-Millions.md": "Scaling: From Zero to Millions of Users",
    "BB-02-Back-of-Envelope-Estimation.md": "Back-of-the-Envelope Estimation",
    "BB-03-System-Design-Framework.md": "System Design Interview Framework",
    "BB-04-Rate-Limiter.md": "Design a Rate Limiter",
    "BB-05-Consistent-Hashing.md": "Design Consistent Hashing",
    "BB-06-Key-Value-Store.md": "Design a Key-Value Store",
    "BB-07-Unique-ID-Generator-Snowflake.md": "Design a Unique ID Generator (Snowflake)",
    "BB-08-URL-Shortener.md": "Design a URL Shortener (TinyURL)",
    "BB-09-Web-Crawler.md": "Design a Web Crawler",
    "BB-10-Notification-System.md": "Design a Notification System",
    "BB-11-News-Feed-System.md": "Design a News Feed System",
    "BB-12-Chat-System.md": "Design a Chat System (WhatsApp/Slack)",
    "BB-13-Search-Autocomplete.md": "Design Search Autocomplete",
    "BB-14-YouTube-Video-Streaming.md": "Design YouTube (Video Streaming)",
    "BB-15-Google-Drive-File-Sync.md": "Design Google Drive (File Sync)",
    "BB-16-Proximity-Service.md": "Design a Proximity Service (Yelp Nearby)",
    "BB-17-Nearby-Friends.md": "Design Nearby Friends (Social Proximity)",
    "BB-18-Google-Maps.md": "Design Google Maps (Navigation)",
    "BB-19-Distributed-Message-Queue.md": "Design a Distributed Message Queue (Kafka-like)",
    "BB-20-Metrics-Monitoring-Alerting.md": "Design Metrics, Monitoring and Alerting",
    "BB-21-Ad-Click-Event-Aggregation.md": "Design Ad Click Event Aggregation",
    "BB-22-Hotel-Reservation-System.md": "Design Hotel Reservation System",
    "BB-23-Distributed-Email-Service.md": "Design Distributed Email Service",
    "BB-24-S3-like-Object-Storage.md": "Design S3-like Object Storage",
    "BB-25-Real-time-Gaming-Leaderboard.md": "Design Real-time Gaming Leaderboard",
    "BB-26-Payment-System.md": "Design Payment System",
    "BB-27-Digital-Wallet.md": "Design Digital Wallet",
    "BB-28-Stock-Exchange-Matching-Engine.md": "Design Stock Exchange (Matching Engine)",
}

def clean_title_from_filename(filename: str) -> str:
    """Generate clean title from filename."""
    # Remove .md
    title = filename.replace('.md', '')
    
    # Remove category prefix
    for prefix in PREFIXES:
        if title.startswith(prefix):
            title = title[len(prefix):]
            break
    
    # Replace hyphens with spaces
    title = title.replace('-', ' ')
    
    # Fix common abbreviations
    replacements = {
        'Api': 'API', 'Aws': 'AWS', 'Ssl': 'SSL', 'Rest': 'REST', 
        'Rpc': 'RPC', 'Sql': 'SQL', 'Nosql': 'NoSQL', 'Lru': 'LRU',
        'Ood': 'OOD', 'Tcp': 'TCP', 'Udp': 'UDP', 'Http': 'HTTP',
        'Grpc': 'gRPC', 'Json': 'JSON', 'Xml': 'XML', 'Html': 'HTML',
        'Css': 'CSS', 'Js': 'JS', 'Ts': 'TS', 'Ci': 'CI', 'Cd': 'CD',
        'Sla': 'SLA', 'Slo': 'SLO', 'Sli': 'SLI', 'Mttr': 'MTTR',
        'Mtbf': 'MTBF', 'Rto': 'RTO', 'Rpo': 'RPO', 'Ddos': 'DDoS',
        'Oauth': 'OAuth', 'Jwt': 'JWT', 'Api': 'API', 'Sdk': 'SDK',
        'Cli': 'CLI', 'Gui': 'GUI', 'Ui': 'UI', 'Ux': 'UX'
    }
    
    for k, v in replacements.items():
        title = title.replace(k, v)
    
    return title

def main():
    print("Fixing frontmatter titles...")
    
    for file_path in TARGET.glob("*.md"):
        if file_path.name == "README.md":
            continue
            
        content = file_path.read_text(encoding='utf-8')
        if not content.startswith('---'):
            continue
        
        parts = content.split('---', 2)
        if len(parts) < 3:
            continue
            
        fm = yaml.safe_load(parts[1]) or {}
        body = parts[2]
        
        # Get correct title
        if file_path.name in TITLE_CORRECTIONS:
            title = TITLE_CORRECTIONS[file_path.name]
        else:
            title = clean_title_from_filename(file_path.name)
        
        fm['title'] = title
        fm['category'] = "Architect/10_System-Design-Interviews"
        
        # Write back
        new_fm = "---\n" + yaml.dump(fm, sort_keys=False, allow_unicode=True, default_flow_style=False) + "---\n"
        file_path.write_text(new_fm + body, encoding='utf-8')
        print(f"  ✅ {file_path.name} → {title}")

if __name__ == "__main__":
    main()