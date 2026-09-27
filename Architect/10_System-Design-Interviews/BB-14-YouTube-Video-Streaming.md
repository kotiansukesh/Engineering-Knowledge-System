---
title: Design YouTube (Video Streaming)
category: Architect/10_System-Design-Interviews
tags:
- cdn
- company/youtube
- concept/interview-prep
- dash
- difficulty/hard
- hls
- pattern/system-design
- transcoding
- video-streaming
created: '2026-09-27'
completed: false
difficulty: Hard
reviewed: '2026-09-14'
sr-due: '2026-09-28'
source: https://github.com/donnemartin/system-design-primer
excalidraw: ''
weeks: '5'
type: note
---






# Design YouTube (Video Streaming)

> Part of [[README|MOC]] • `Architect/10_System-Design-Interviews` • Weeks 5
> 🎨 **Visual diagram:** Create Excalidraw drawing from template: `Cmd+P → Excalidraw: New from template → System Design Interviews Diagram`

## Intent



## Why it Matters

- **Interview signal**: Frequently asked in system design interviews
- **Production impact**: Fundamental to scalable system design
- **Core concept**: Key building block for distributed systems

## Problems

### System Design Problem: Design YouTube (Video Streaming)

**Requirements:**
- See primer for detailed requirements

**Constraints:**
- High availability, scalability, fault tolerance

## Code / Example

```java
// Java 25 / Spring Boot 3.5: Core concept for Design YouTube (Video Streaming)
// Architecture pattern - implementation varies by system

record DesignYouTubeVideoStreamingConfig(
    String component,
    int capacity,
    String strategy
) {
    static DesignYouTubeVideoStreamingConfig ofDefaults() {
        return new DesignYouTubeVideoStreamingConfig(
            "Design YouTube (Video Streaming)",
            10000,
            "default"
        );
    }
}
```

### Concrete Example
- **Input:** Design requirements
- **Output:** Architecture diagram + component specs
- **Explanation:** See primer for step-by-step design

## When to Use / When NOT

| **Use When** | **Avoid When** |
|--------------|----------------|
| Building this system from scratch | Managed service covers need |
| Learning architecture patterns | Simple CRUD applications |
| Interview preparation | Requirements don't match |

## Trade-offs

| Dimension | This Approach | Alternative |
|-----------|---------------|-------------|
| Complexity | | |
| Operational Burden | | |
| Latency | | |
| Consistency | | |
| Cost at Scale | | |

## Vs Table

| Aspect | This Design | Managed Service | Decision Rule |
|--------|-------------|-----------------|---------------|
| Flexibility | Full | Limited | Need custom logic? → Self-host |
| Time to Market | Weeks | Hours | Prototype? → Managed |
| Cost at Scale | Optimizable | Fixed/marginal | High volume? → Self-host |

## Pitfalls

- Underestimating operational complexity
- Ignoring failure modes
- Not planning for 10x scale
- Skipping monitoring/alerting in MVP
- Premature optimization before measuring

## Interview Q&A (Senior Depth)

**Q1: Q1**
**A:** ('Design YouTube video streaming. Key components?', '1) Upload: chunked/resumable upload to S3. 2) Transcoding: async pipeline (FFmpeg) -> multiple resolutions (240p-8K), codecs (H.264, VP9, AV1), HLS/DASH segments. 3) CDN: segment caching, edge compute for manifest manipulation. 4) Manifest: MPD (DASH) / m3u8 (HLS) with adaptive bitrate. 5) Player: ABR algorithm (bandwidth estimation, buffer health). 6) Analytics: QoE metrics (startup time, rebuffer rate, bitrate).')

**Q2: Q2**
**A:** ('How does adaptive bitrate streaming (ABR) work?', 'Client measures: throughput (segment download time), buffer occupancy. Algorithm: BOLA (buffer occupancy), throughput-based, or hybrid. Switch up/down based on predicted bandwidth. Avoid oscillation (hysteresis).')

**Q3: Q3**
**A:** ('How do you handle transcoding at scale (500h uploaded/min)?', 'Async: upload -> S3 event -> SQS -> transcoding workers (spot instances). Priority queue: premium/short first. Parallel: segment-level parallelism. Output: per-resolution segments + manifest. Cache: popular videos pre-transcoded.')

**Q4: Q4**
**A:** ('How do you optimize CDN costs and latency?', 'Tiered caching: origin -> regional -> edge. Prefetch next segments. Segment duration: 2-6s (trade-off: latency vs overhead). Manifest at edge (Lambda@Edge/Cloudflare Workers). Peering with ISPs. Cache hit rate > 95%.')

**Q5: Q5**
**A:** ('How do you handle live streaming vs VOD?', 'Live: low-latency HLS (LL-HLS) or WebRTC. Segment duration 1-2s. Ingest: RTMP/SRT -> transcoder -> packager -> CDN. DVR: sliding window. VOD: pre-transcoded, full manifest. Live-to-VOD: clip and store after stream ends.')
## Flashcards (Spaced Repetition)

#flashcard
**Q:** Video streaming components? :: **A:** Upload (chunked) → Transcoding (FFmpeg, multi-res) → CDN (HLS/DASH segments) → Player (ABR) #flashcard

#flashcard
**Q:** Adaptive Bitrate (ABR)? :: **A:** Client measures throughput + buffer. Algorithm: BOLA, throughput-based, hybrid. Hysteresis #flashcard

#flashcard
**Q:** Transcoding at scale? :: **A:** Async: S3 event → SQS → spot workers. Priority queue. Segment-level parallelism. Pre-transcode popular #flashcard

#flashcard
**Q:** HLS vs DASH? :: **A:** HLS: Apple, .m3u8, TS segments. DASH: standard, .mpd, fMP4. Both adaptive. DASH more flexible #flashcard

#flashcard
**Q:** CDN optimization? :: **A:** Tiered: origin → regional → edge. Prefetch next segments. Segment 2-6s. Manifest at edge (Lambda@Edge) #flashcard

#flashcard
**Q:** Live vs VOD? :: **A:** Live: LL-HLS/WebRTC, 1-2s segments, RTMP/SRT ingest, DVR window. VOD: pre-transcoded, full manifest #flashcard

#flashcard
**Q:** Transcode pipeline? :: **A:** Upload → S3 → Event → MediaConvert/FFmpeg → Outputs (240p-8K, H.264/VP9/AV1) → S3 → CDN #flashcard

#flashcard
**Q:** QoE metrics? :: **A:** Startup time, rebuffer rate, bitrate, join time, error rate. Per-session tracking #flashcard

#flashcard
**Q:** Segment duration? :: **A:** 2-6s trade-off: shorter = lower latency, more overhead. Live: 1-2s for low latency #flashcard

#flashcard
**Q:** DRM? :: **A:** Widevine/PlayReady/FairPlay. Key rotation. License server. Offline playback support #flashcard

#flashcard
**Q:** Thumbnail/sprite? :: **A:** Generate at intervals. Sprite sheet for hover preview. WebVTT for chapters #flashcard

#flashcard
**Q:** Cost optimization? :: **A:** Tiered storage (hot/warm/cold). Spot instances for transcoding. Cache hit > 95% #flashcard

#flashcard
**Q:** Multi-CDN? :: **A:** DNS-based or client-side switching. Cedexis/Conviva. Failover on error/latency #flashcard

#flashcard
**Q:** Live-to-VOD? :: **A:** Clip and store after stream ends. Trim slate. Generate VOD manifest #flashcard

#flashcard
**Q:** Monitoring? :: **A:** Concurrent viewers, bitrate distribution, rebuffer ratio, CDN hit rate, origin bandwidth #flashcard
## Practice Tasks (Tasks Plugin)

- [ ] Explain the architecture from memory 📅 {date:YYYY-MM-DD, +1}
- [ ] Draw the system diagram without looking 📅 {date:YYYY-MM-DD, +3}
- [ ] Answer all Interview Q&A aloud 📅 {date:YYYY-MM-DD, +7}
- [ ] Review flashcards (Spaced Repetition) 📅 {date:YYYY-MM-DD, +1}

```tasks
not done
path includes 10_System-Design-Interviews
sort by due
limit 10
```

## Related

- [[Architect/10_System-Design-Interviews/README|System Design Interviews Folder]]
- [[Architect/03_Architecture-Styles/README|Architecture Styles]]
- [[Architect/08_NonFunctional-Ops/README|Non-Functional Requirements]]
- [[Architect/07_Integration-APIs/README|Integration Patterns]]

---

*Category: Architect/10_System-Design-Interviews • Part of [[README|MOC]]*