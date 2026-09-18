---
title: LLD & Machine Coding - MOC
category: LLD
tags: [lld, machine-coding, moc]
created: 2026-09-04
---
# LLD & Machine Coding

> Part of [[Java/README|Java MOC]] · Method: [[00_Method-How-to-Answer-LLD|How to Answer LLD]] · Diagrams: [[00_UML-Class-and-Sequence-Diagrams|UML Class & Sequence]]

Design a system in 45 minutes: clarify → enumerate use cases → classes/relationships → UML → code core → extensions/concurrency. Full loop in [[00_Method-How-to-Answer-LLD|the method note]].

Sources: [AlgoMaster LLD course intro](https://algomaster.io/learn/lld/course-introduction) · [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) (problems + class diagrams) · companion LLD Sheet + mock interviews on the course page.

## Study Loop (Course's 8 Steps, Compressed)

1. Read the drill note + class diagram. 2. Cover the code and re-derive the classes. 3. Do the Try It Yourself tasks. 4. Compare with the solution. 5. Say aloud why each class exists. 6. Revisit High-priority misses weekly.

## Easy

| Problem | Priority | Key Patterns |
|---|---|---|
| [[01_Parking-Lot\|Parking Lot]] | High | Singleton, Factory, Observer |
| [[02_Vending-Machine\|Vending Machine]] | Medium | State, Strategy |
| [[03_Logging-Framework\|Logging Framework]] | Medium | Chain of Responsibility, Observer, Singleton |
| [[04_Stack-Overflow\|Stack Overflow]] | Medium | Repository, Strategy (voting) |
| [[14_Snake-and-Ladder\|Snake and Ladder]] | High | Facade, Strategy (dice) |
| [[15_Task-Management-System\|Task Management System]] | Medium | Singleton, Facade, Observer |

## Medium

| Problem | Priority | Key Patterns |
|---|---|---|
| [[05_ATM\|ATM]] | High | State, Facade, Singleton |
| [[06_LRU-Cache\|LRU Cache]] | High | HashMap + Doubly-Linked List |
| [[07_Elevator-System\|Elevator System]] | High | State, Strategy (scheduling), Observer |
| [[08_Tic-Tac-Toe\|Tic-Tac-Toe]] | Medium | State, Command, Observer |
| [[09_Pub-Sub-System\|Pub-Sub System]] | Medium | Observer, Mediator, Singleton |
| [[16_Traffic-Signal-Control\|Traffic Signal Control]] | Medium | State, Singleton |
| [[17_Coffee-Vending-Machine\|Coffee Vending Machine]] | Medium | Strategy (recipe), Facade, Singleton |

## Hard

| Problem | Priority | Key Patterns |
|---|---|---|
| [[10_Chess-Game\|Chess Game]] | High | State, Strategy (pieces), Command |
| [[11_Splitwise\|Splitwise]] | High | Observer, Strategy (split), Factory |
| [[12_Movie-Ticket-Booking\|Movie Ticket Booking]] | High | Singleton, Observer, State (seat lock) |
| [[13_Ride-Sharing-Uber\|Ride Sharing (Uber)]] | High | Strategy (pricing/matching), Observer, Factory |
```dataview
TABLE difficulty AS Difficulty, tags AS Tags
FROM "Java/10_LLD-Machine-Coding"
WHERE category = "LLD" AND file.name != "README"
SORT file.name ASC
```