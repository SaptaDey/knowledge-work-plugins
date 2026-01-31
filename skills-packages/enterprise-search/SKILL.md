---
name: enterprise-search
description: Complete enterprise search skill for finding anything across all your company's tools in one query. Use when searching across email, chat, documents, wikis, project trackers, or CRM. Also generates daily/weekly digests of activity. Trigger phrases include "search for", "find", "where is", "what do we know about", "daily digest", "weekly digest", "what happened this week", "catch me up on".
---

# Enterprise Search Skill

Find anything across all your company's tools in one query. No more switching between apps to find what you need.

## Core Capabilities

- **Unified Search**: Search across all connected sources simultaneously
- **Smart Decomposition**: Breaks natural language queries into source-specific searches
- **Knowledge Synthesis**: Combines results with deduplication and attribution
- **Activity Digests**: Daily or weekly summaries across all tools

## Quick Commands

| Command | Usage | Description |
|---------|-------|-------------|
| `/search` | `/search [query]` | Search across all sources |
| `/digest` | `/digest [daily\|weekly]` | Generate activity digest |

---

## Search Capabilities

### How It Works

```
User Query: "What did we decide about the Q2 pricing change?"
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│ QUERY DECOMPOSITION                                              │
│ Intent: Decision query                                          │
│ Entities: Q2, pricing                                           │
│ Time: Recent (implied)                                          │
│ Sources: Chat, Email, Documents, Knowledge Base                 │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│ PARALLEL EXECUTION                                               │
│ ~~chat: "pricing" in #product, #sales channels                  │
│ ~~email: threads with "pricing" + "Q2"                          │
│ ~~documents: docs containing "pricing decision"                 │
│ ~~knowledge base: articles tagged "pricing"                     │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│ SYNTHESIS                                                        │
│ Deduplicate → Rank → Attribute → Answer                         │
└─────────────────────────────────────────────────────────────────┘
```

### Query Types

| Type | Examples | Primary Sources |
|------|----------|-----------------|
| **Decision** | "What did we decide about X?" | Chat, Email, Documents |
| **Status** | "Where are we on project X?" | Project Tracker, Chat |
| **Document** | "Find the Q3 planning doc" | Documents, Knowledge Base |
| **Person** | "What's Sarah working on?" | Project Tracker, Chat |
| **Factual** | "What's our refund policy?" | Knowledge Base, Documents |
| **Temporal** | "What happened last week?" | All sources, time-filtered |
| **Exploratory** | "What do we know about X?" | All sources |

### Search Output Format

```
## Answer

[Synthesized answer with key information]

### Sources

| Source | Content | Relevance |
|--------|---------|-----------|
| [Source type] | [Summary] | [Link] |

### Confidence

[High/Medium/Low] — [Explanation]

### Related

- [Related topic 1]
- [Related topic 2]
```

---

## Knowledge Synthesis

### Deduplication

When the same information appears in multiple sources:
1. Keep the most authoritative version
2. Note corroboration ("confirmed in 3 sources")
3. Preserve unique details from each

### Confidence Levels

**High Confidence:**
- Multiple sources agree
- Recent, authoritative source
- Direct answer to query

**Moderate Confidence:**
- Single source
- Slightly dated
- Indirect answer

**Low Confidence:**
- Conflicting information
- Unclear relevance
- Requires interpretation

### Conflict Handling

When sources disagree:
1. Surface the conflict explicitly
2. Prioritize by recency and authority
3. Present both perspectives
4. Recommend resolution path

---

## Activity Digests

### Daily Digest

Scan all sources for today's activity:

```
# Daily Digest — [Date]

## Action Items
- [ ] [Item requiring your action]

## Decisions Made
- [Decision 1]: [Context and outcome]

## Activity by Topic

### [Topic/Project 1]
- [Activity summary]
- [Activity summary]

### [Topic/Project 2]
- [Activity summary]

## Mentions
- [Someone mentioned you in context]

## Documents Updated
| Document | Change | By |
|----------|--------|-----|

## Stats
| Metric | Count |
|--------|-------|
| Messages | N |
| Documents | N |
| Tasks | N |
```

### Weekly Digest

Broader summary for the week:

```
# Weekly Digest — [Week of Date]

## This Week's Highlights
- [Major highlight 1]
- [Major highlight 2]

## Key Decisions
| Decision | Made By | Date | Source |
|----------|---------|------|--------|

## Projects Status
| Project | Status | Activity |
|---------|--------|----------|

## Action Items Created
- [ ] [Item] (from [source])

## Upcoming
- [Upcoming event/deadline]
```

---

## Source Management

### Available Sources

| Category | Placeholder | What It Searches |
|----------|-------------|------------------|
| Chat | `~~chat` | Slack, Teams messages and channels |
| Email | `~~email` | Email threads and attachments |
| Cloud Storage | `~~cloud storage` | Google Drive, Dropbox, OneDrive |
| Project Tracker | `~~project tracker` | Jira, Asana, Linear tasks |
| CRM | `~~CRM` | HubSpot, Salesforce records |
| Knowledge Base | `~~knowledge base` | Notion, Confluence, Guru articles |

### Source Priority by Query Type

| Query Type | Priority Order |
|------------|---------------|
| Decision | Chat → Email → Documents |
| Status | Project Tracker → Chat → Email |
| Document | Cloud Storage → Knowledge Base |
| Person | Project Tracker → Chat → CRM |
| Factual | Knowledge Base → Documents |
| Exploratory | All sources equally |

### Rate Limiting

The skill monitors API limits and:
- Prioritizes most relevant sources first
- Gracefully degrades when limits hit
- Reports partial results with explanation

---

## Tool Connections

| Category | Placeholder | Examples |
|----------|-------------|----------|
| Chat | `~~chat` | Slack, Microsoft Teams |
| Email | `~~email` | Microsoft 365, Gmail |
| Cloud Storage | `~~cloud storage` | Google Drive, OneDrive, Dropbox |
| Project Tracker | `~~project tracker` | Jira, Asana, Linear, Monday |
| CRM | `~~CRM` | HubSpot, Salesforce |
| Knowledge Base | `~~knowledge base` | Notion, Confluence, Guru |

### MCP Configuration

See `references/connectors.md` for setup instructions.

### Minimum Viable Setup

Works with just one source connected. More sources = better results.

**Recommended starting point:**
1. Connect Chat (Slack/Teams)
2. Add Knowledge Base (Notion/Confluence)
3. Add Project Tracker

Each additional source improves answer quality and coverage.
