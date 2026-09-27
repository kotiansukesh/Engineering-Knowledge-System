---
title: Stack Overflow
category: Java/10_LLD-Machine-Coding
difficulty: Easy
tags:
- lld
- machine-coding
- stack-overflow
source: https://github.com/ashishps1/awesome-low-level-design
created: 2026-09-04
pattern: 6
completed: false
reviewed: ''
sr-due: ''
excalidraw: ''
type: note
---

## Why it Matters

- Reputation is *derived* state, not stored data: it is the projection of every vote ever cast. Keeping vote storage and reputation computation separate is what lets you change the scoring rule without touching the vote path.
- Voting is a lost-update trap with money-like consequences: two concurrent upvotes that both read `reputation=41` and write `51` silently steal points from a user, so check-then-act on shared counters is the core concurrency lesson.
- The content tree (question → answer → comment) shares behaviour across types, all votable, none identical, which is exactly where an interface beats inheritance and where a scattered `instanceof` chain rots.

## Diagram

![[_attachments/stackoverflow-class-diagram.png]]
*Source: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) , use alongside the class table above.*
*Runtime flow: ask → answer → accept.*
```mermaid
flowchart LR
 A[Post question + tags] --> B[Answers arrive]
 B --> C[Votes rank answers]
 C --> D[Asker accepts one]
 D --> E[Reputation to author]
```
## Code
```java
javaimport java.util.*;

class User { String name; int rep; User(String n) { name = n; } }

abstract class Post { int votes; void upvote() { votes++; } void downvote() { votes--; } }

class Question extends Post {
 String title; Set<String> tags = new HashSet<>(); List<Answer> answers = new ArrayList<>();
 Answer accepted;
 Question(String t, String... tg) { title = t; tags.addAll(Arrays.asList(tg)); }
 void accept(Answer a) { accepted = a; }
}

class Answer extends Post { User author; String body; Answer(User u, String b) { author = u; body = b; } }

class StackOverflowDemo {
 void upvoteAnswer(Answer a) { a.upvote(); a.author.rep += 10; } // voting -> reputation rule
 void downvoteAnswer(Answer a) { a.downvote(); a.author.rep -= 2; }
 public static void main(String[] a) {
 StackOverflowDemo so = new StackOverflowDemo();
 User bob = new User("bob");
 Question q = new Question("How does HashMap work?", "java", "collections");
 Answer ans = new Answer(bob, "Array of bins + treeify at 8.");
 q.answers.add(ans);
 so.upvoteAnswer(ans); so.upvoteAnswer(ans); so.downvoteAnswer(ans);
 q.accept(ans);
 System.out.println("votes=" + ans.votes + " rep=" + bob.rep + " accepted=" + (q.accepted == ans));
 }
}
```
## When to use / not

**Use when** a system stores user-generated content whose value is ranked by aggregate community signal, Q&A sites, review platforms, forums with karma, bug trackers with voting.
**Use** a repository/index layer when search by attribute (tag, keyword, status) is a first-class requirement; an in-memory index per attribute is honest at interview scale.
**Use** an observer seam for milestone reactions (badges) so adding a new badge never edits the vote path.
**NOT when** content has no ranking or derived score, a CMS or a document store gains nothing from a vote service or reputation projection; a plain repository is the whole design.
**NOT when** the ranking signal is time-only (a blog index), sorting by created_at needs no strategy and no projection.

## Trade-offs

- **Stored reputation vs computed on read:** storing the running total gives O(1) reads but risks drift from the vote log on any missed update; computing by replay is always consistent but costs a scan per profile. Interview answer: store the total, but make the vote service the *only* writer.
- **Post-level vs user-level locking:** locking the post makes vote + reputation atomic per post; locking the user is coarser (one user's many posts serialize) but simpler. Pick by which contention you expect, and say so.
- **Denormalized tag index vs query scan:** maintaining per-tag lists gives fast filtered feeds but must be updated on every retag; a full scan is correct and simple until the dataset is large. Choose by stated scale, never by default.
- **Observer badges vs polling:** push-based badges react instantly but the observer runs *inside* the vote transaction (keep it cheap); polling milestones are simpler to reason about but lag.
- **`synchronized` vs `AtomicInteger`:** atomics win for a single counter; a multi-field update (votes, reputation, accepted-flag) needs a lock or a transactional seam, mixing the two is how you get partial updates.

## Vs

- **Vs [[15_Task-Management-System|Task Management System]]:** Stack Overflow models *content* with an emergent rank; tasks model an *ongoing process* with an owner and status. The shared part is the observer for reactions (badge vs assignment notification); the difference is that votes accumulate forever while a task terminates.
- **Vs [[09_Pub-Sub-System|Pub-Sub System]]:** the badge observer here is a in-process fan-out to one or two listeners; pub-sub is that pattern scaled to durable per-subscriber queues with replay. Same shape, different delivery contract.
- **Vs a vote as a boolean flag:** an idempotent `(userId, postId, dir)` vote record supports undo, recount, and audit; a bare `++counter` supports none of them. The record is the design, the counter is the optimisation.
- **Vs [[04_Stack-Overflow|Reddit/HN-style]] ranking:** a pure score sum ranks by consensus; time-decay (HN) ranks by recency. If the requirement says "trending", the vote service needs a decay strategy, not just an add.

## Pitfalls

- **Lost updates on concurrent votes** — read-modify-write on reputation without a lock or atomic is the canonical bug; two upvotes land as one. Fix the race, don't apologise for it.
- **Double-voting / vote flipping** — no vote record means a user can upvote twice (or undo a downvote by upvoting). Persist intent per (user, post) and make re-voting an update, not an insert.
- **Reputation drift** — a vote path that updates votes but throws before updating reputation, or an exception in the badge observer that rolls back the whole vote. Keep side effects out of the transaction or make them failure-isolated.
- **Two accepted answers** — the accepted flag must be a per-question exclusive constraint; setting it on the answer alone allows two.
- **Strategy scattered across services** — vote-weight rules (`+10`, `−2`) hardcoded in three places diverge; one `VoteStrategy` is the single source.
- **Tag index inconsistent with posts** — retagging a question that does not refresh the tag index returns stale results in search; update index and post under one operation.
- **Unbounded comment trees** — modelling replies as recursive lists without depth limits or pagination turns a question page into a graph traversal; bound it or paginate by design.

## Interview q&a

- **Prevent double-voting / allow vote reversal?** Store `Map<(userId, postId), Vote>`; reversal applies the inverse reputation delta.
- **Scale search by tag?** Inverted index `tag → questionIds`; keyword search moves to a full-text index (out of scope for the demo).

Prevent double-voting / allow vote reversal?:: Store `Map<(userId, postId), Vote>`; reversal applies the inverse reputation delta. #flashcard
Scale search by tag?:: Inverted index `tag → questionIds`; keyword search moves to a full-text index (out of scope for the demo). #flashcard

## Related

- [[06_Design-Patterns/Behavioral/Strategy\|Strategy]], [[06_Design-Patterns/Behavioral/Observer\|Observer]], [[02_OOP/SOLID-Single-Responsibility\|SRP]]
- Source: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

# Stack Overflow

> Part of [[README|Java MOC]] -> [[10_LLD-Machine-Coding/README|LLD MOC]]

## Requirements

- Users post questions, answers, comments; one accepted answer per question
- Upvote/downvote questions and answers; reputation changes (+10 answer upvote, −2 downvote given, etc.)
- Search questions by tag/keyword; close or tag questions

## Classes & Relationships

| Class | Role | Pattern |
|---|---|---|
| `User` | id, reputation, badges | , |
| `Question` / `Answer` / `Comment` | votable content tree | , |
| `VoteService` | applies vote + reputation delta | [[06_Design-Patterns/Behavioral/Strategy\|Strategy]] (vote weight rules) |
| `QuestionRepository` | tag/keyword index | [[06_Design-Patterns/Extra/DAO Pattern\|DAO/Repository]] |
| `BadgeService` (optional) | observes reputation milestones | [[06_Design-Patterns/Behavioral/Observer\|Observer]] |

## Concurrency

Make vote + reputation update atomic (`synchronized` on the post or `AtomicInteger` votes) , lost updates otherwise.

## Try it Yourself

1. Add bounties: a user stakes reputation on a question; award it to the accepted answer. Where does the escrow live?
2. Add tag follow + a home feed of newest questions in followed tags (reuse the Observer seam).
3. Add close-voting (5 votes closes); model the question lifecycle as a State.
