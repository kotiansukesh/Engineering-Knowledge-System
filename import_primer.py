#!/usr/bin/env python3
"""
Import system-design-primer content into Architect vault.
Creates structured notes in unified template format.
"""

import re
import yaml
from pathlib import Path
from datetime import datetime

VAULT_ROOT = Path("/Users/sukesh/Documents/GitHub/Obsidian")
TARGET_FOLDER = VAULT_ROOT / "Architect" / "10_System-Design-Interviews"
SOURCE_FILE = Path("/Users/sukesh/.hermes/cache/web/github.com-789bde9df7.md")

# Read full source content
full_content = SOURCE_FILE.read_text(encoding='utf-8')

# Section definitions from the primer
SECTIONS = [
    # Foundational
    ("System Design Topics: Start Here", "FND-01-System-Design-Overview", "Easy", "1-2", ["study-guide", "interview-prep", "scalability"]),
    ("Performance vs Scalability", "FND-02-Performance-vs-Scalability", "Easy", "1", ["performance", "scalability", "tradeoffs"]),
    ("Latency vs Throughput", "FND-03-Latency-vs-Throughput", "Easy", "1", ["latency", "throughput", "tradeoffs"]),
    ("Availability vs Consistency (CAP Theorem)", "FND-04-CAP-Theorem", "Medium", "2", ["cap-theorem", "consistency", "availability", "partition-tolerance"]),
    ("Consistency Patterns", "FND-05-Consistency-Patterns", "Medium", "2", ["weak-consistency", "eventual-consistency", "strong-consistency"]),
    ("Availability Patterns", "FND-06-Availability-Patterns", "Medium", "2", ["failover", "replication", "active-passive", "active-active", "sla"]),
    ("Domain Name System (DNS)", "FND-07-DNS", "Easy", "2", ["dns", "records", "caching", "ttl"]),
    ("Content Delivery Network (CDN)", "FND-08-CDN", "Easy", "2", ["cdn", "push-cdn", "pull-cdn", "static-content"]),
    ("Load Balancer", "NET-01-Load-Balancer", "Medium", "2", ["load-balancer", "layer4", "layer7", "horizontal-scaling", "ssl-termination"]),
    ("Reverse Proxy", "NET-02-Reverse-Proxy", "Easy", "2", ["reverse-proxy", "web-server", "security", "caching"]),
    ("Application Layer & Microservices", "NET-03-Microservices-Service-Discovery", "Medium", "3", ["microservices", "service-discovery", "consul", "etcd", "zookeeper"]),
    
    # Database
    ("Relational Database (RDBMS)", "DB-01-RDBMS", "Medium", "3", ["rdbms", "acid", "sql", "transactions"]),
    ("Master-Slave Replication", "DB-02-Master-Slave-Replication", "Medium", "3", ["replication", "master-slave", "read-replicas"]),
    ("Master-Master Replication", "DB-03-Master-Master-Replication", "Medium", "3", ["replication", "master-master", "multi-master"]),
    ("Federation (Functional Partitioning)", "DB-04-Federation", "Medium", "3", ["federation", "functional-partitioning", "database-splitting"]),
    ("Sharding", "DB-05-Sharding", "Hard", "3", ["sharding", "consistent-hashing", "partitioning", "shard-key"]),
    ("Denormalization", "DB-06-Denormalization", "Medium", "3", ["denormalization", "read-performance", "materialized-views"]),
    ("SQL Tuning", "DB-07-SQL-Tuning", "Medium", "3", ["sql-tuning", "indexes", "query-optimization"]),
    ("NoSQL", "DB-08-NoSQL", "Medium", "4", ["nosql", "key-value", "document", "wide-column", "graph"]),
    ("SQL vs NoSQL", "DB-09-SQL-vs-NoSQL", "Medium", "4", ["sql", "nosql", "polyglot-persistence"]),
    
    # Cache
    ("Cache Overview", "CACHE-01-Cache-Overview", "Easy", "4", ["cache", "caching-strategies", "layers"]),
    ("Cache Strategies", "CACHE-02-Cache-Strategies", "Medium", "4", ["cache-aside", "write-through", "write-behind", "refresh-ahead"]),
    ("When to Update Cache", "CACHE-03-Cache-Update-Strategies", "Medium", "4", ["cache-update", "invalidation", "eviction"]),
    
    # Asynchronism
    ("Asynchronism Overview", "ASYNC-01-Asynchronism-Overview", "Easy", "5", ["async", "message-queues", "task-queues", "back-pressure"]),
    ("Message Queues", "ASYNC-02-Message-Queues", "Medium", "5", ["message-queues", "kafka", "rabbitmq", "pub-sub"]),
    ("Task Queues", "ASYNC-03-Task-Queues", "Medium", "5", ["task-queues", "celery", "background-jobs"]),
    ("Back Pressure", "ASYNC-04-Back-Pressure", "Medium", "5", ["back-pressure", "flow-control", "rate-limiting"]),
    
    # Communication
    ("TCP vs UDP", "NET-04-TCP-vs-UDP", "Easy", "5", ["tcp", "udp", "transport-layer"]),
    ("RPC", "COMM-01-RPC", "Medium", "5", ["rpc", "grpc", "thrift", "service-to-service"]),
    ("REST", "COMM-02-REST", "Medium", "5", ["rest", "api-design", "http", "resource-oriented"]),
    
    # Security
    ("Security", "NET-05-Security", "Medium", "5", ["security", "auth", "encryption", "https", "oauth"]),
    
    # Appendix
    ("Powers of Two Table", "FND-12-Powers-of-Two", "Easy", "1", ["reference", "estimation"]),
    ("Latency Numbers Every Programmer Should Know", "FND-13-Latency-Numbers", "Easy", "1", ["reference", "latency", "back-of-envelope"]),
    ("Additional System Design Interview Questions", "REF-01-Additional-Interview-Questions", "Medium", "6", ["interview", "questions", "practice"]),
    ("Real World Architectures", "REF-02-Real-World-Architectures", "Medium", "6", ["case-studies", "real-world", "architectures"]),
    ("Company Architectures", "REF-03-Company-Architectures", "Medium", "6", ["company-architectures", "netflix", "uber", "airbnb"]),
    ("Company Engineering Blogs", "REF-04-Company-Engineering-Blogs", "Easy", "1", ["blogs", "resources", "learning"]),
    
    # System Design Interview Questions with Solutions
    ("Design Pastebin/URL Shortener", "INT-01-URL-Shortener-Pastebin", "Medium", "7", ["url-shortener", "pastebin", "base62", "hashing"]),
    ("Design Twitter Timeline", "INT-02-Twitter-Timeline", "Hard", "7", ["twitter", "timeline", "fan-out", "news-feed", "search"]),
    ("Design Web Crawler", "INT-03-Web-Crawler", "Hard", "7", ["web-crawler", "crawling", "url-frontier", "politeness", "deduplication"]),
    ("Design Mint.com", "INT-04-Mint-Financial-Aggregation", "Hard", "7", ["mint", "financial", "aggregation", "banking"]),
    ("Design Social Graph", "INT-05-Social-Graph", "Hard", "7", ["social-graph", "graph-database", "relationships"]),
    ("Design Key-Value Store for Search", "INT-06-Key-Value-Store-for-Search", "Hard", "7", ["key-value-store", "search", "query-cache"]),
    ("Design Amazon Sales Rank", "INT-07-Amazon-Sales-Rank", "Hard", "7", ["sales-rank", "ranking", "real-time"]),
    ("Design System on AWS", "INT-08-System-on-AWS", "Hard", "7", ["aws", "cloud", "scaling"]),
    
    # Object-Oriented Design
    ("Design Hash Map", "OOD-01-Hash-Map", "Medium", "8", ["hash-map", "data-structure", "ood"]),
    ("Design LRU Cache", "OOD-02-LRU-Cache", "Medium", "8", ["lru-cache", "cache", "data-structure", "ood"]),
    ("Design Call Center", "OOD-03-Call-Center", "Medium", "8", ["call-center", "ood", "system-design"]),
    ("Design Deck of Cards", "OOD-04-Deck-of-Cards", "Easy", "8", ["deck-of-cards", "ood"]),
    ("Design Parking Lot", "OOD-05-Parking-Lot", "Medium", "8", ["parking-lot", "ood", "state-machine"]),
    ("Design Chat Server", "OOD-06-Chat-Server", "Medium", "8", ["chat-server", "ood", "websocket"]),
    
    # Study Guide & Interview Approach
    ("Study Guide", "FND-09-Study-Guide", "Easy", "1", ["study-guide", "timeline", "interview-prep"]),
    ("How to Approach System Design Interview", "FND-10-Interview-Approach", "Easy", "1", ["interview", "approach", "4-step-framework"]),
    ("Back-of-the-Envelope Calculations", "FND-11-Back-of-Envelope", "Easy", "1", ["estimation", "capacity-planning", "back-of-envelope"]),
    
    # ByteByteGo Patterns
    ("Scaling: From Zero to Millions of Users", "BB-01-Scaling-Zero-to-Millions", "Easy", "1", ["scaling", "architecture", "load-balancer", "caching", "cdn", "sharding", "replication"]),
    ("Back-of-the-Envelope Estimation", "BB-02-Back-of-Envelope-Estimation", "Easy", "1", ["estimation", "back-of-envelope", "capacity-planning"]),
    ("System Design Interview Framework", "BB-03-System-Design-Framework", "Easy", "2", ["interview", "framework", "4-step"]),
    ("Design a Rate Limiter", "BB-04-Rate-Limiter", "Medium", "2", ["rate-limiter", "token-bucket", "sliding-window", "distributed"]),
    ("Design Consistent Hashing", "BB-05-Consistent-Hashing", "Medium", "2", ["consistent-hashing", "ketama", "virtual-nodes"]),
    ("Design a Key-Value Store", "BB-06-Key-Value-Store", "Medium", "3", ["key-value-store", "lsm-tree", "sstable", "compaction"]),
    ("Design a Unique ID Generator (Snowflake)", "BB-07-Unique-ID-Generator-Snowflake", "Medium", "3", ["unique-id", "snowflake", "distributed-id"]),
    ("Design a URL Shortener (TinyURL)", "BB-08-URL-Shortener", "Medium", "3", ["url-shortener", "base62", "analytics"]),
    ("Design a Web Crawler", "BB-09-Web-Crawler", "Hard", "3", ["web-crawler", "url-frontier", "politeness", "deduplication"]),
    ("Design a Notification System", "BB-10-Notification-System", "Medium", "4", ["notification", "push", "pull", "websocket", "fcm", "apns"]),
    ("Design a News Feed System", "BB-11-News-Feed-System", "Hard", "4", ["news-feed", "fan-out", "ranking", "pull-vs-push"]),
    ("Design a Chat System (WhatsApp/Slack)", "BB-12-Chat-System", "Hard", "4", ["chat", "websocket", "presence", "message-ordering"]),
    ("Design Search Autocomplete", "BB-13-Search-Autocomplete", "Hard", "4", ["autocomplete", "trie", "redis", "elasticsearch"]),
    ("Design YouTube (Video Streaming)", "BB-14-YouTube-Video-Streaming", "Hard", "5", ["video-streaming", "transcoding", "cdn", "hls", "dash"]),
    ("Design Google Drive (File Sync)", "BB-15-Google-Drive-File-Sync", "Hard", "5", ["file-sync", "operational-transform", "crdt", "conflict-resolution"]),
    ("Design a Proximity Service (Yelp Nearby)", "BB-16-Proximity-Service", "Hard", "5", ["proximity", "geohash", "quadtree", "s2-geometry"]),
    ("Design Nearby Friends (Social Proximity)", "BB-17-Nearby-Friends", "Hard", "6", ["nearby-friends", "geohash", "social-graph", "fan-out"]),
    ("Design Google Maps (Navigation)", "BB-18-Google-Maps", "Hard", "6", ["maps", "routing", "a-star", "contraction-hierarchies", "road-network"]),
    ("Design a Distributed Message Queue (Kafka-like)", "BB-19-Distributed-Message-Queue", "Hard", "6", ["message-queue", "kafka", "partitions", "consumer-groups", "exactly-once"]),
    ("Design Metrics, Monitoring and Alerting", "BB-20-Metrics-Monitoring-Alerting", "Medium", "6", ["metrics", "monitoring", "alerting", "prometheus", "grafana", "red-use"]),
    ("Design Ad Click Event Aggregation", "BB-21-Ad-Click-Event-Aggregation", "Hard", "7", ["stream-processing", "windowing", "exactly-once", "aggregation"]),
    ("Design Hotel Reservation System", "BB-22-Hotel-Reservation-System", "Hard", "7", ["hotel-reservation", "acid", "distributed-transactions", "saga"]),
    ("Design Distributed Email Service", "BB-23-Distributed-Email-Service", "Hard", "7", ["email", "smtp", "queue", "retry", "spam-filtering"]),
    ("Design S3-like Object Storage", "BB-24-S3-like-Object-Storage", "Hard", "7", ["object-storage", "s3", "multipart-upload", "versioning", "consistency"]),
    ("Design Real-time Gaming Leaderboard", "BB-25-Real-time-Gaming-Leaderboard", "Hard", "8", ["leaderboard", "redis", "sorted-sets", "sharding", "real-time"]),
    ("Design Payment System", "BB-26-Payment-System", "Hard", "8", ["payment", "idempotency", "reconciliation", "ledger"]),
    ("Design Digital Wallet", "BB-27-Digital-Wallet", "Hard", "8", ["digital-wallet", "balance", "transactions", "audit-trail"]),
    ("Design Stock Exchange (Matching Engine)", "BB-28-Stock-Exchange-Matching-Engine", "Hard", "8", ["stock-exchange", "order-book", "matching-engine", "latency"]),
]


def extract_section_content(full_content: str, section_title: str):
    """Extract content for a specific section from the primer. Returns (content, extracted_heading)."""
    # Try multiple possible heading formats and variations
    title_variations = [
        section_title,
        section_title.replace(" (CAP Theorem)", ""),
        section_title.replace(" (RDBMS)", ""),
        section_title.replace("Overview", ""),
        section_title.replace("vs ", "vs. "),
    ]
    
    for variation in title_variations:
        patterns = [
            rf"## {re.escape(variation)}",
            rf"### {re.escape(variation)}",
            rf"## {re.escape(variation.lower())}",
            rf"### {re.escape(variation.lower())}",
        ]
        
        for pattern in patterns:
            match = re.search(pattern, full_content, re.IGNORECASE)
            if match:
                start = match.start()
                # Find end of current line (after the heading)
                line_end = full_content.find('\n', start)
                if line_end == -1:
                    line_end = len(full_content)
                # Find next LEVEL-2 heading AFTER the current line (not level-3)
                next_match = re.search(r'^##\s+', full_content[line_end+1:], re.MULTILINE)
                if next_match:
                    end = line_end + 1 + next_match.start()
                else:
                    end = min(start + 8000, len(full_content))
                extracted_heading = full_content[start:line_end].strip()
                section_text = full_content[start:end].strip()
                # Limit size
                if len(section_text) > 8000:
                    section_text = section_text[:8000] + "\n\n... (see primer for full content)"
                return section_text, extracted_heading
    
    # Special handling for known sections with different headings
    special_mappings = {
        "Availability vs Consistency (CAP Theorem)": "## Availability vs consistency",
        "Consistency Patterns": "## Consistency patterns",
        "Availability Patterns": "## Availability patterns",
        "Content Delivery Network (CDN)": "## Content delivery network",
        "Load Balancer": "## Load balancer",
        "Reverse Proxy": "## Reverse proxy (web server)",
        "Application Layer & Microservices": "## Application layer",
        "Relational Database (RDBMS)": "## Database",
        "Master-Slave Replication": "### Master-slave replication",
        "Master-Master Replication": "### Master-master replication",
        "Federation (Functional Partitioning)": "#### Federation",
        "Sharding": "#### Sharding",
        "Denormalization": "#### Denormalization",
        "SQL Tuning": "#### SQL tuning",
        "NoSQL": "### NoSQL",
        "SQL vs NoSQL": "### SQL or NoSQL",
        "Cache Overview": "## Cache",
        "Cache Strategies": "### When to update the cache",
        "Asynchronism Overview": "## Asynchronism",
        "Message Queues": "### Message queues",
        "Task Queues": "### Task queues",
        "Back Pressure": "### Back pressure",
        "TCP vs UDP": "### Transmission control protocol (TCP)",
        "RPC": "### Remote procedure call (RPC)",
        "REST": "### Representational state transfer (REST)",
        "Security": "## Security",
        "Powers of Two Table": "#### Powers of two table",
        "Latency Numbers Every Programmer Should Know": "#### Latency numbers every programmer should know",
        "Design Pastebin/URL Shortener": "### Design Pastebin.com (or Bit.ly)",
        "Design Twitter Timeline": "### Design the Twitter timeline and search",
        "Design Web Crawler": "### Design a web crawler",
        "Design Mint.com": "### Design Mint.com",
        "Design Social Graph": "### Design the data structures for a social network",
        "Design Key-Value Store for Search": "### Design a key-value store for a search engine",
        "Design Amazon Sales Rank": "### Design Amazon's sales ranking by category feature",
        "Design System on AWS": "### Design a system that scales to millions of users on AWS",
        "Design Hash Map": "### Design a hash map",
        "Design LRU Cache": "### Design a least recently used cache",
        "Design Call Center": "### Design a call center",
        "Design Deck of Cards": "### Design a deck of cards",
        "Design Parking Lot": "### Design a parking lot",
        "Design Chat Server": "### Design a chat server",
        "Study Guide": "## Study guide",
        "How to Approach System Design Interview": "## How to approach a system design interview question",
        "Back-of-the-Envelope Calculations": "### Back-of-the-envelope calculations",
    }
    
    if section_title in special_mappings:
        pattern = special_mappings[section_title]
        match = re.search(re.escape(pattern), full_content, re.IGNORECASE)
        if match:
            start = match.start()
            # Find end of current line
            line_end = full_content.find('\n', start)
            if line_end == -1:
                line_end = len(full_content)
            # Find next LEVEL-2 heading AFTER the current line (for level-2 headings)
            # For level-3/4 headings, find next heading of same or higher level
            heading_level = pattern.count('#')
            if heading_level == 2:
                next_match = re.search(r'^##\s+', full_content[line_end+1:], re.MULTILINE)
            else:
                next_match = re.search(r'^#{2,3}\s+', full_content[line_end+1:], re.MULTILINE)
            
            if next_match:
                end = line_end + 1 + next_match.start()
            else:
                end = min(start + 8000, len(full_content))
            extracted_heading = full_content[start:line_end].strip()
            section_text = full_content[start:end].strip()
            if len(section_text) > 8000:
                section_text = section_text[:8000] + "\n\n... (see primer for full content)"
            return section_text, extracted_heading
    
    return "", None


def parse_primer_content(content: str, title: str) -> dict:
    """Parse primer content into structured sections."""
    parsed = {
        "summary": "",
        "intent": "",
        "why_it_matters": "",
        "requirements": [],
        "constraints": [],
        "when_use": [],
        "when_avoid": [],
        "tradeoffs": [],
        "pitfalls": [],
    }
    
    if not content:
        return parsed
    
    # Extract summary (first paragraph after heading)
    lines = content.split('\n')
    first_para = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('![') and not line.startswith('*['):
            first_para.append(line)
        elif first_para:
            break
    if first_para:
        parsed["summary"] = ' '.join(first_para[:3])[:500]
    
    # Look for structured sections in primer content
    content_lower = content.lower()
    
    # Extract requirements (look for "requirements", "functional", "non-functional")
    req_matches = re.findall(r'(?i)(?:requirements?|functional requirements?|non-functional requirements?)[:\s]*\n?(.*?)(?:\n\n|\n#|\n\*|\Z)', content, re.DOTALL)
    if req_matches:
        for match in req_matches[:2]:
            items = re.findall(r'[-*]\s*(.+)', match)
            if items:
                parsed["requirements"].extend(items[:5])
    
    # Extract constraints
    constraint_matches = re.findall(r'(?i)constraints?[:\s]*\n?(.*?)(?:\n\n|\n#|\n\*|\Z)', content, re.DOTALL)
    if constraint_matches:
        for match in constraint_matches[:2]:
            items = re.findall(r'[-*]\s*(.+)', match)
            if items:
                parsed["constraints"].extend(items[:5])
    
    # Extract trade-offs (look for "trade-off", "pros and cons", "advantages/disadvantages")
    tradeoff_matches = re.findall(r'(?i)(?:trade-?off|pros? and cons?|advantages? and disadvantages?)[:\s]*\n?(.*?)(?:\n\n|\n#|\n\*|\Z)', content, re.DOTALL)
    if tradeoff_matches:
        for match in tradeoff_matches[:2]:
            # Try to parse as dimension/this/alt
            lines = match.split('\n')
            for line in lines:
                line = line.strip()
                if ':' in line and not line.startswith('-'):
                    parts = line.split(':', 1)
                    parsed["tradeoffs"].append({
                        "dimension": parts[0].strip(),
                        "this": parts[1].strip()[:100],
                        "alt": "See primer"
                    })
    
    # Extract pitfalls (look for "pitfall", "disadvantage", "caveat", "limitation")
    pitfall_matches = re.findall(r'(?i)(?:pitfall|disadvantage|caveat|limitation)[:\s]*\n?(.*?)(?:\n\n|\n#|\n\*|\Z)', content, re.DOTALL)
    if pitfall_matches:
        for match in pitfall_matches[:2]:
            items = re.findall(r'[-*]\s*(.+)', match)
            if items:
                parsed["pitfalls"].extend(items[:5])
    
    # Extract when to use / avoid (look for "when to use", "use case", "avoid")
    use_matches = re.findall(r'(?i)(?:when to use|use case)[:\s]*\n?(.*?)(?:\n\n|\n#|\n\*|\Z)', content, re.DOTALL)
    if use_matches:
        items = re.findall(r'[-*]\s*(.+)', use_matches[0])
        parsed["when_use"] = items[:5]
    
    avoid_matches = re.findall(r'(?i)(?:when.*avoid|avoid when|not suitable)[:\s]*\n?(.*?)(?:\n\n|\n#|\n\*|\Z)', content, re.DOTALL)
    if avoid_matches:
        items = re.findall(r'[-*]\s*(.+)', avoid_matches[0])
        parsed["when_avoid"] = items[:5]
    
    # Default why_it_matters based on title/category
    if "CAP" in title or "Consistency" in title or "Availability" in title:
        parsed["why_it_matters"] = """- **Interview signal**: CAP theorem is the #1 distributed systems question
- **Production impact**: Every distributed database decision is a CP vs AP choice
- **Core concept**: You cannot have all three - networks WILL partition"""
    elif "Load Balancer" in title:
        parsed["why_it_matters"] = """- **Interview signal**: Entry point for any scalable system design
- **Production impact**: Single point of failure if not configured correctly
- **Core concept**: L4 vs L7, algorithms, health checks, SSL termination"""
    elif "Cache" in title:
        parsed["why_it_matters"] = """- **Interview signal**: Cache strategy reveals system design maturity
- **Production impact**: Wrong strategy causes stale data or thundering herd
- **Core concept**: Cache-aside vs write-through vs write-behind vs refresh-ahead"""
    elif "Sharding" in title:
        parsed["why_it_matters"] = """- **Interview signal**: Horizontal scaling differentiates junior/senior
- **Production impact**: Shard key choice locks you in for years
- **Core concept**: Consistent hashing, hot spots, rebalancing"""
    elif "Message Queue" in title or "Asynchronism" in title:
        parsed["why_it_matters"] = """- **Interview signal**: Async processing is key to scalability
- **Production impact**: Decouples services, enables retries, buffers spikes
- **Core concept**: At-least-once vs exactly-once, ordering, dead letter queues"""
    elif "TCP vs UDP" in title:
        parsed["why_it_matters"] = """- **Interview signal**: Transport layer choice affects everything
- **Production impact**: UDP for real-time, TCP for reliability
- **Core concept**: Connectionless vs connection-oriented, head-of-line blocking"""
    elif "RPC" in title or "gRPC" in title:
        parsed["why_it_matters"] = """- **Interview signal**: Service-to-service communication backbone
- **Production impact**: Contract-first, schema evolution, latency
- **Core concept**: Protocol buffers, HTTP/2, streaming, code generation"""
    elif "REST" in title:
        parsed["why_it_matters"] = """- **Interview signal**: Most common API style, but often misused
- **Production impact**: Cacheability, versioning, HATEOAS
- **Core concept**: Resources, verbs, status codes, hypermedia"""
    
    # Generate intent from first meaningful paragraph
    if first_para:
        parsed["intent"] = ' '.join(first_para[:2])[:400]
    
    return parsed


def build_interview_problem_section(title: str, parsed: dict) -> str:
    """Build Problems section for interview problems with actual requirements."""
    reqs = parsed.get("requirements", [])
    constraints = parsed.get("constraints", [])
    
    # Default requirements based on problem type
    if not reqs:
        if "URL Shortener" in title or "Pastebin" in title:
            reqs = [
                "Shorten long URLs to short aliases (e.g., bit.ly/abc123)",
                "Redirect short URL to original URL",
                "Custom aliases support",
                "Expiration / TTL for links",
                "Analytics: click count, referrers, geography"
            ]
        elif "Twitter" in title or "Timeline" in title:
            reqs = [
                "Post tweets (text, media)",
                "Follow/unfollow users",
                "Generate home timeline (fan-out)",
                "Generate user timeline",
                "Search tweets",
                "Handle 100M+ users, 500M tweets/day"
            ]
        elif "Web Crawler" in title:
            reqs = [
                "Crawl web pages starting from seed URLs",
                "Extract links and content",
                "Respect robots.txt and crawl delays (politeness)",
                "Handle deduplication (URL frontier)",
                "Scale to billions of pages",
                "Support incremental / priority crawling"
            ]
        elif "Mint" in title:
            reqs = [
                "Aggregate financial accounts (bank, credit, investment)",
                "Transaction categorization",
                "Budget tracking and alerts",
                "Net worth calculation",
                "Secure credential handling (OAuth, Plaid)"
            ]
        elif "Social Graph" in title:
            reqs = [
                "Follow/unfollow, friend connections",
                "Friend recommendations (mutual friends, graph algorithms)",
                "Privacy controls",
                "Scale to billions of users/edges",
                "Real-time feed generation"
            ]
        elif "Key-Value" in title and "Search" in title:
            reqs = [
                "High-throughput key-value storage",
                "Secondary index / query support",
                "Range queries",
                "Strong consistency for writes",
                "Horizontal scaling"
            ]
        elif "Amazon" in title and "Sales Rank" in title:
            reqs = [
                "Real-time sales rank per category",
                "Handle millions of products",
                "Hourly/daily rank updates",
                "Category hierarchy support",
                "Low-latency reads"
            ]
        elif "System on AWS" in title:
            reqs = [
                "Design scalable web application on AWS",
                "Multi-AZ deployment",
                "Auto-scaling, load balancing",
                "RDS/DynamoDB for data",
                "CloudFront CDN, S3 for static assets",
                "CloudWatch monitoring"
            ]
        elif "Hash Map" in title:
            reqs = [
                "put(key, value), get(key), remove(key)",
                "O(1) average time complexity",
                "Handle collisions (chaining or open addressing)",
                "Dynamic resizing",
                "Thread-safe variant"
            ]
        elif "LRU Cache" in title:
            reqs = [
                "get(key) - return value or -1",
                "put(key, value) - insert/update, evict LRU if at capacity",
                "O(1) time for both operations",
                "Fixed capacity"
            ]
        elif "Call Center" in title:
            reqs = [
                "Employees: Respondent, Manager, Director",
                "Incoming calls routed to available employee",
                "Escalation if not handled in time",
                "Track call statistics"
            ]
        elif "Deck of Cards" in title:
            reqs = [
                "52 cards, 4 suits, 13 ranks",
                "Shuffle, deal, reset",
                "Multiple decks support"
            ]
        elif "Parking Lot" in title:
            reqs = [
                "Multiple floors, spots per floor",
                "Vehicle types: car, truck, motorcycle, EV",
                "Entry/exit, ticketing, payment",
                "Find available spot efficiently"
            ]
        elif "Chat Server" in title:
            reqs = [
                "1-on-1 and group chat",
                "Message history",
                "Online/offline presence",
                "Push notifications",
                "Scale to millions of concurrent users"
            ]
        else:
            reqs = ["See primer for detailed requirements"]
    
    if not constraints:
        constraints = [
            "High availability (99.9%+)",
            "Horizontal scalability",
            "Fault tolerance",
            "Low latency (p99 < 100ms for reads)",
            "Data durability"
        ]
    
    section = f"""## Problems

### System Design Problem: {title}

**Requirements:**
"""
    for r in reqs[:8]:
        section += f"- {r}\n"
    
    section += "\n**Constraints:**\n"
    for c in constraints[:6]:
        section += f"- {c}\n"
    
    section += "\n"
    return section


def create_note(title: str, filename: str, difficulty: str, weeks: str, tags: list, source_content: str):
    """Create a unified note from source content."""
    category = "Architect/10_System-Design-Interviews"
    
    # Extract relevant content from source
    body_content, extracted_heading = extract_section_content(source_content, title)
    
    # Parse structured content from primer
    parsed = parse_primer_content(body_content, title)
    
    # Build frontmatter
    fm = {
        "title": title,
        "category": category,
        "tags": tags,
        "created": datetime.now().strftime("%Y-%m-%d"),
        "completed": False,
        "difficulty": difficulty,
        "reviewed": "",
        "sr-due": "",
        "source": "https://github.com/donnemartin/system-design-primer",
        "excalidraw": "",
        "weeks": weeks,
        "type": "note"
    }
    
    # Build note body
    body = f"# {title}\n\n"
    body += f"> Part of [[README|MOC]] • `{category}`"
    if weeks:
        body += f" • Weeks {weeks}"
    body += f"\n> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → System Design Interviews Diagram`\n\n"
    
    # Add Intent / Why it Matters from parsed content or defaults
    if parsed.get("intent"):
        body += f"## Intent\n\n{parsed['intent']}\n\n"
    elif "INT-" in filename or "OOD-" in filename:
        body += "## Intent\n\nSystem design interview problem from system-design-primer with solution approach.\n\n"
    else:
        body += f"## Intent\n\n{parsed.get('summary', 'Core system design concept from the primer.')}\n\n"
    
    if parsed.get("why_it_matters"):
        body += f"## Why it Matters\n\n{parsed['why_it_matters']}\n\n"
    elif "INT-" in filename or "OOD-" in filename:
        body += "## Why it Matters\n\n- **Interview signal**: Classic system design problem testing end-to-end design skills\n- **Production impact**: Patterns used in real-world systems at scale\n- **Core concepts**: Covers requirements gathering, API design, data modeling, scaling\n\n"
    else:
        body += "## Why it Matters\n\n- **Interview signal**: Frequently asked in system design interviews\n- **Production impact**: Fundamental to scalable system design\n- **Core concept**: Key building block for distributed systems\n\n"
    
    # Add full extracted content (cleaned)
    if body_content:
        # Clean up the extracted content - remove the heading that was extracted
        if extracted_heading:
            body_content = body_content.replace(extracted_heading, '', 1)
        # Also remove any remaining level 2/3 heading at the start
        body_content = re.sub(r'^#{2,3}\s+.+$', '', body_content, count=1, flags=re.MULTILINE)
        body_content = body_content.strip()
        body += body_content + "\n\n"
    
    # Problems section - use parsed requirements/constraints for interview problems
    if "## Problems" not in body:
        if "INT-" in filename or "OOD-" in filename:
            body += build_interview_problem_section(title, parsed)
        else:
            body += f"""## Problems

### System Design Problem: {title}

**Requirements:**
- See primer for detailed requirements

**Constraints:**
- High availability, scalability, fault tolerance

"""
    
    # Code / Example
    if "## Code / Example" not in body:
        class_name = title.replace(' ', '').replace('-', '').replace('(', '').replace(')', '').replace('/', '')
        body += f"""## Code / Example

```java
// Java 25 / Spring Boot 3.5: Core concept for {title}
// Architecture pattern - implementation varies by system

record {class_name}Config(
    String component,
    int capacity,
    String strategy
) {{
    static {class_name}Config ofDefaults() {{
        return new {class_name}Config(
            "{title}",
            10000,
            "default"
        );
    }}
}}
```

### Concrete Example
- **Input:** Design requirements
- **Output:** Architecture diagram + component specs
- **Explanation:** See primer for step-by-step design

"""
    
    # When to Use / When NOT
    if "## When to Use / When NOT" not in body:
        when_use = parsed.get("when_use", [])
        when_avoid = parsed.get("when_avoid", [])
        if when_use or when_avoid:
            body += "## When to Use / When NOT\n\n| **Use When** | **Avoid When** |\n|--------------|----------------|\n"
            max_rows = max(len(when_use), len(when_avoid))
            for i in range(max_rows):
                use = when_use[i] if i < len(when_use) else ""
                avoid = when_avoid[i] if i < len(when_avoid) else ""
                body += f"| {use} | {avoid} |\n"
            body += "\n"
        else:
            body += """## When to Use / When NOT

| **Use When** | **Avoid When** |
|--------------|----------------|
| Building this system from scratch | Managed service covers need |
| Learning architecture patterns | Simple CRUD applications |
| Interview preparation | Requirements don't match |

"""
    
    # Trade-offs
    if "## Trade-offs" not in body:
        tradeoffs = parsed.get("tradeoffs", [])
        if tradeoffs:
            body += "## Trade-offs\n\n| Dimension | This Approach | Alternative |\n|-----------|---------------|-------------|\n"
            for t in tradeoffs:
                body += f"| {t['dimension']} | {t['this']} | {t['alt']} |\n"
            body += "\n"
        else:
            body += """## Trade-offs

| Dimension | This Approach | Alternative |
|-----------|---------------|-------------|
| Complexity | | |
| Operational Burden | | |
| Latency | | |
| Consistency | | |
| Cost at Scale | | |

"""
    
    # Vs Table
    if "## Vs Table" not in body:
        body += """## Vs Table

| Aspect | This Design | Managed Service | Decision Rule |
|--------|-------------|-----------------|---------------|
| Flexibility | Full | Limited | Need custom logic? → Self-host |
| Time to Market | Weeks | Hours | Prototype? → Managed |
| Cost at Scale | Optimizable | Fixed/marginal | High volume? → Self-host |

"""
    
    # Pitfalls
    if "## Pitfalls" not in body:
        pitfalls = parsed.get("pitfalls", [])
        if pitfalls:
            body += "## Pitfalls\n\n"
            for p in pitfalls:
                body += f"- {p}\n"
            body += "\n"
        else:
            body += """## Pitfalls

- Underestimating operational complexity
- Ignoring failure modes
- Not planning for 10x scale
- Skipping monitoring/alerting in MVP
- Premature optimization before measuring

"""
    
    # Interview Q&A
    body += f"""## Interview Q&A (Senior Depth)

**Q1: Walk me through the high-level architecture for {title}.**
**A:** [Key components, data flow, boundaries. Use back-of-envelope to justify scale.]

**Q2: What are the key trade-offs in this design?**
**A:** [CAP, Latency vs Throughput, Build vs Buy, SQL vs NoSQL, Sync vs Async. Cite specific choices.]

**Q3: How does this scale to 10x traffic?**
**A:** [Stateless services, sharding, read replicas, caching layers, async processing via message queues. Identify bottlenecks.]

**Q4: What happens when [critical component] fails?**
**A:** [Retries, circuit breakers, fallback, graceful degradation, data recovery, replay.]

**Q5: How do you monitor and debug this in production?**
**A:** [RED metrics: rate, errors, duration. USE metrics: utilization, saturation, errors. Structured logging, correlation IDs. SLO-based alerting.]

"""
    
    # Flashcards
    body += f"""## Flashcards (Spaced Repetition)

#flashcard
**Q:** What is the core pattern for {title}? :: **A:** [Key algorithm/architecture from primer] #flashcard

#flashcard
**Q:** When do you use {title}? :: **A:** [Trigger scenarios from primer] #flashcard

#flashcard
**Q:** Key trade-off in {title}? :: **A:** [Main trade-off] #flashcard

#flashcard
**Q:** Scale bottleneck for {title}? :: **A:** [Primary bottleneck] #flashcard

"""
    
    # Practice Tasks
    body += f"""## Practice Tasks (Tasks Plugin)

- [ ] Explain the architecture from memory 📅 {{date:YYYY-MM-DD, +1}}
- [ ] Draw the system diagram without looking 📅 {{date:YYYY-MM-DD, +3}}
- [ ] Answer all Interview Q&A aloud 📅 {{date:YYYY-MM-DD, +7}}
- [ ] Review flashcards (Spaced Repetition) 📅 {{date:YYYY-MM-DD, +1}}

```tasks
not done
path includes 10_System-Design-Interviews
sort by due
limit 10
```

"""
    
    body += """## Related

- [[Architect/10_System-Design-Interviews/README|System Design Interviews Folder]]
- [[Architect/03_Architecture-Styles/README|Architecture Styles]]
- [[Architect/08_NonFunctional-Ops/README|Non-Functional Requirements]]
- [[Architect/07_Integration-APIs/README|Integration Patterns]]

---

*Category: """ + category + """ • Part of [[README|MOC]]*"""
    
    # Write note
    fm_yaml = "---\n" + yaml.dump(fm, sort_keys=False, allow_unicode=True, default_flow_style=False) + "---\n"
    TARGET_FOLDER.mkdir(parents=True, exist_ok=True)
    (TARGET_FOLDER / f"{filename}.md").write_text(fm_yaml + "\n\n" + body, encoding='utf-8')
    print(f"  ✅ {filename}.md")


def main():
    print("Importing system-design-primer content...")
    
    for title, filename, difficulty, weeks, tags in SECTIONS:
        create_note(title, filename, difficulty, weeks, tags, full_content)
    
    print(f"\nDone! Created {len(SECTIONS)} notes in {TARGET_FOLDER}")


if __name__ == "__main__":
    main()