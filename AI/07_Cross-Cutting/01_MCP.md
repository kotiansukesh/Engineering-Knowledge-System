---
title: "Model Context Protocol (MCP)"
category: AI/07_Cross-Cutting
tags: [ai, mcp, tools, integration, architecture]
created: 2026-09-30
completed: false
reviewed: "2026-09-29"
sr-due: "2026-09-30"
difficulty: Medium
type: concept
weeks: 5
---

# Model Context Protocol (MCP)

## Intent

MCP is an open protocol for connecting AI applications with servers that expose capabilities such as **tools, resources, and prompts**.

## Mental Model

```
AI host/client
     |
     | MCP
     v
MCP server
  |   |   |
tools resources prompts
```

The protocol separates the client/host from the server implementation so capabilities can be exposed through a standard interface.

## Transport

For current MCP implementations, distinguish:
- **stdio** for local process integrations
- **Streamable HTTP** for remote/networked integrations
- **SSE** primarily as a backwards-compatibility transport where supported

Do not describe WebSocket as a universal MCP transport.

## When MCP Helps

- multiple independently owned tools/services
- reusable integrations across AI hosts
- discoverable capability contracts
- shared resources/prompts
- platform-level governance and authorization

## When MCP Is Unnecessary

- one small in-process function
- a fixed contract where an extra protocol boundary adds no value
- latency-sensitive paths where the protocol hop is not justified

## Decision

MCP is an integration boundary, not an agent framework and not a replacement for authorization. Tool permissions, input validation, auditing, tenant isolation, and downstream authorization remain application responsibilities.

## Failure Modes

- untrusted tool/resource content treated as instructions
- excessive tool surface
- weak authorization around powerful tools
- stale capability metadata
- missing audit trail
- protocol/server version incompatibility

## Practice

Design a server exposing one read-only resource and one mutating tool. Define:
1. authentication/authorization
2. input validation
3. audit events
4. timeout
5. failure response
6. approval requirement for the mutating operation

## Related

- Tool Calling
- Guardrails
- AI Security
