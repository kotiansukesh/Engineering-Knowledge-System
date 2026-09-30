---
title: "Java MOC"
category: "Java"
type: "folder-MOC"
tags: [MOC, folder]
created: "2026-09-29"
completed: false
reviewed: "2026-09-29"
sr-due: "2026-10-06"
---

# Java Knowledge Vault

> **Master MOC** for Java 25: Core, Modern, Collections, Concurrency, Design Patterns, DSA, LLD, Spring

---

## Progress Overview

```dataviewjs
const pages = dv.pages("#java").where(p => p.category && p.file.name != "README");
const total = pages.length;
const done = pages.where(p => p.completed === true).length;
const pct = total ? Math.round(done/total*100) : 0;
const bar = (p, w=20) => "█".repeat(Math.round(p/100*w)) + "░".repeat(w-Math.round(p/100*w));
dv.paragraph(`**Total: ${total} notes | Completed: ${done} | Remaining: ${total-done}** — \`${pct}%\``);
dv.paragraph(`\`${bar(pct)}\` **${pct}%**`);
if (total === done && total > 0) dv.paragraph(`🎉 *All notes completed!*`);
```

---

## Quick Navigation

| Category | Notes | Status | Description |
|----------|-------|--------|-------------|
| [[00_Java-25-Overview|Java 25 Overview]] | 9 | LTS evolution, roadmap, interview strategy |
| [[01_Core-Java|Core Java]] | 35 | Fundamentals, JPMS, FFM, Structured Concurrency, Module System |
| [[02_OOP|OOP Principles]] | 17 | SOLID, inheritance, encapsulation, class relationships |
| [[03_Collections|Collections]] | 11 | List, Set, Map, Queue, legacy, modern |
| [[04_Concurrency|Concurrency]] | 7 | Threads, locks, executors, CompletableFuture, virtual threads |
| [[05_Spring|Spring]] | 9 | Core, MVC, Boot, Security, Data JPA, Transactions |
| [[06_Design-Patterns|Design Patterns]] | 25 | Creational, Structural, Behavioral, Enterprise |
| [[07_DSA|Data Structures & Algorithms]] | 15 | Trees, graphs, segment tree, BIT, UF, topo sort, trie |
| [[08_Modern-Java|Modern Java (8-21)]] | 9 | Records, sealed, pattern matching, virtual threads |
| [[09_Java-21-LTS|Java 21 LTS]] | 11 | Deep dive on LTS features |
| [[10_LLD-Machine-Coding|LLD Machine Coding]] | 17 | 17 UML diagrams, class/sequence, real problems |
| [[99_Revision|Revision]] | 4 | Interview questions, study plan, interactive setup |

---

## Spaced Repetition Status

```dataview
TABLE WITHOUT ID
file.link as "Note",
reviewed as "Last Reviewed",
"sr-due" as "Due",
choice(!reviewed, "🔴 Never", choice(date(now)-reviewed > dur(7 days), "🟡 Stale", "🟢 Fresh")) as "Status"
FROM "Java"
WHERE category AND file.name != "README" AND (reviewed OR "sr-due")
SORT "sr-due" ASC
```

---

## Practice Tasks (All Categories)

```tasks
not done
path includes Java
sort by due
limit 30
```

---

## Recent Notes

```dataview
TABLE WITHOUT ID
file.link as "Note",
category as "Category",
choice(completed, "✅", "⬜") as "Done",
difficulty as "Difficulty",
reviewed as "Reviewed"
FROM "Java"
WHERE category AND file.name != "README"
SORT file.mtime DESC
LIMIT 15
```

---

## Folder Structure

```
Java/
├── 00_Java-25-Overview/       # LTS roadmap, interview strategy
├── 01_Core-Java/              # Core fundamentals + JPMS, FFM, Structured Concurrency
│   ├── Types/                 # Class types, nested classes
│   └── ... (35 notes)
├── 02_OOP/                    # OOP principles, SOLID
│   └── Inheritance/
├── 03_Collections/            # Collections framework
│   ├── List/                  # ArrayList, LinkedList, Legacy Collections
│   ├── Set/                   # HashSet, TreeSet, Sorted Set
│   └── ...
├── 04_Concurrency/            # Threads, locks, executors, virtual threads
├── 05_Spring/                 # Spring ecosystem
├── 06_Design-Patterns/        # 25 patterns, 12-section template
│   ├── Creational/            # Singleton, Builder, Factory, Abstract Factory, Prototype
│   ├── Structural/            # Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy
│   ├── Behavioral/            # Chain, Command, Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy, Template, Visitor
│   └── Extra/                 # DAO, Dependency Injection
├── 07_DSA/                    # Data structures & algorithms
│   ├── Trie, Segment Tree, Fenwick Tree, Union-Find, Topological Sort
│   └── ... (15 notes)
├── 08_Modern-Java/            # Java 8-21 features
├── 09_Java-21-LTS/            # Java 21 deep dive
├── 10_LLD-Machine-Coding/     # 17 LLD problems with UML diagrams
│   └── _attachments/          # 17 generated PNG diagrams
├── 99_Revision/               # Interview prep
├── _templates/                # Java-Note-Template.md, Pattern-Note-Template.md
└── README.md                  # This file
```

---

## Diagram Index (LLD)

All 17 LLD problems have **class diagrams** and **sequence/flow diagrams** generated in `_attachments/`:

| Problem | Class Diagram | Flow Diagram |
|---------|---------------|--------------|
| Parking Lot | `parkinglot-class-diagram.png` | ✅ Mermaid |
| Vending Machine | `vendingmachine-class-diagram.png` | ✅ State |
| Logging Framework | `loggingframework-class-diagram.png` | ✅ Flow |
| Stack Overflow | `stackoverflow-class-diagram.png` | ✅ Flow |
| ATM | `atm-class-diagram.png` | ✅ State |
| LRU Cache | `lrucache-class-diagram.png` | ✅ Flow |
| Elevator System | `elevatorsystem-class-diagram.png` | ✅ State |
| Tic-Tac-Toe | `tictactoe-class-diagram.png` | ✅ Flow |
| Pub-Sub System | `pubsubsystem-class-diagram.png` | ✅ Flow |
| Chess Game | `chessgame-class-diagram.png` | ✅ Flow |
| Splitwise | `splitwise-class-diagram.png` | ✅ Flow |
| Movie Ticket Booking | `movieticketbookingsystem-class-diagram.png` | ✅ State |
| Ride Sharing (Uber) | `ridesharingservice-class-diagram.png` | ✅ State |
| Snake & Ladder | `snakeandladder-class-diagram.png` | ✅ Flow |
| Task Management | `taskmanagement-class-diagram.png` | ✅ Flow |
| Traffic Signal | `trafficcontrol-class-diagram.png` | ✅ State |
| Coffee Vending | `coffeevending-class-diagram.png` | ✅ Flow |

---

## Templates

- **[[Java-Note-Template]]** — Standard note template (Core Java, Collections, DSA, etc.)
- **[[Pattern-Note-Template]]** — Design pattern template (12 sections, Java 25 features)

### Excalidraw Template

Create diagrams from template: `Cmd+P → Excalidraw: New from template → Java Diagram`

If template missing, create one with:
- Dark theme colors matching vault
- Standard shapes: class, interface, sequence, flowchart
- Mermaid-compatible styling

---

## Study Workflow

1. **Daily**: Review SR due notes (`sr-due` ≤ today)
2. **Weekly**: Complete practice tasks, update `reviewed` dates
3. **Per Topic**: 
   - Read note → Code snippet → Answer Q&A → Flashcards
   - Mark `completed: true` when confident
4. **LLD**: Practice one problem weekly; draw class diagram from memory

---

## Key Conventions

| Convention | Format |
|------------|--------|
| Category | `Java/<folder>` (e.g., `Java/06_Design-Patterns/Creational`) |
| Tags | `[java, category, specific]` |
| Pattern | `pattern: pattern-name` (for design patterns) |
| Difficulty | `Easy` / `Medium` / `Advanced` |
| SR Fields | `reviewed: "YYYY-MM-DD"`, `sr-due: "YYYY-MM-DD"` |
| Source | `source: "url"` or `source: ""` |

---

## Quick Commands

```bash
# View all notes needing review
# Dataview: WHERE date(now) - reviewed > dur(7 days)

# View incomplete patterns
# Dataview: WHERE category CONTAINS "Design-Patterns" AND completed = false

# Generate folder READMEs
# python3 generate_folder_readmes.py
```

---

*Part of [[Java MOC]] • Java 25 • 173 notes • 17 UML diagrams*