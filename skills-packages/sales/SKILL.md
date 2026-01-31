---
name: sales
description: Complete sales skill for prospecting, call preparation, competitive intelligence, pipeline management, and deal execution. Use when researching prospects or accounts, preparing for sales calls, analyzing competitors, reviewing pipeline health, creating sales forecasts, drafting outreach, summarizing calls, or getting daily briefings. Trigger phrases include "research [company]", "prep me for my call with", "competitive intel on", "pipeline review", "forecast my deals", "draft outreach to", "summarize this call", "morning briefing", "what's on my plate today".
---

# Sales Skill

Transform your sales workflow with AI-powered research, preparation, and deal execution. Works standalone with web research, supercharged when connected to your CRM and sales tools.

## Core Capabilities

- **Account Research**: Deep company and contact intelligence
- **Call Prep**: Comprehensive meeting preparation with agendas
- **Competitive Intelligence**: Battle cards and comparison matrices
- **Pipeline Management**: Health analysis, prioritization, and forecasting
- **Outreach Drafting**: Personalized cold outreach with research
- **Call Processing**: Summaries, action items, and follow-ups
- **Daily Briefings**: Prioritized daily action plans

## Quick Commands

| Command | Usage | Description |
|---------|-------|-------------|
| `/research` | `/research [company]` | Research account or contact |
| `/call-prep` | `/call-prep [company]` | Prepare for a sales call |
| `/competitive` | `/competitive [competitor]` | Generate competitive intel |
| `/pipeline` | `/pipeline` | Review pipeline health |
| `/forecast` | `/forecast` | Generate sales forecast |
| `/outreach` | `/outreach [prospect]` | Draft personalized outreach |
| `/call-summary` | `/call-summary` | Process call notes/transcript |
| `/briefing` | `/briefing` | Get daily sales briefing |

---

## Account Research

Research companies or contacts to get actionable sales intelligence.

### What You Get

- **Company Overview**: Industry, size, funding, leadership
- **Recent News**: Funding rounds, leadership changes, product launches
- **Hiring Signals**: Growth indicators from job postings
- **Key People**: Decision makers and their backgrounds
- **Tech Stack**: Tools they use (when detectable)
- **Prior Relationships**: Existing connections (with CRM)

### Output Format

```
## Account Research: [Company]

### Company Overview
| Field | Value |
|-------|-------|
| Industry | [Industry] |
| Size | [Employees/Revenue] |
| Founded | [Year] |
| Funding | [Stage/Amount] |
| HQ | [Location] |

### Recent News
- [Date]: [News item] — [Why it matters]

### Key People
| Name | Title | Background | LinkedIn |
|------|-------|------------|----------|
| [Name] | [Title] | [Summary] | [URL] |

### Signals & Insights
- [Signal 1 with sales relevance]
- [Signal 2 with sales relevance]

### Recommended Approach
[How to engage based on research]
```

---

## Call Preparation

Get fully prepared for any sales call with context, research, and strategy.

### How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│  ALWAYS (works standalone)                                       │
│  ✓ Company and attendee research                                │
│  ✓ Web search for recent news                                   │
│  ✓ Prep brief with agenda and questions                         │
├─────────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (with connectors)                                  │
│  + CRM: account history, contacts, opportunities                │
│  + Email: recent threads, open commitments                      │
│  + Chat: internal discussions, colleague insights               │
│  + Transcripts: prior call recordings, key moments              │
│  + Calendar: auto-find meeting, pull attendees                  │
└─────────────────────────────────────────────────────────────────┘
```

### Output Format

```
# Call Prep: [Company]

**Meeting:** [Type] — [Date/Time]
**Attendees:** [Names with titles]
**Your Goal:** [What you want to accomplish]

## Account Snapshot
| Field | Value |
|-------|-------|
| Status | [Prospect/Opportunity/Customer] |
| Last Touch | [Date and summary] |

## Who You're Meeting
### [Name] — [Title]
- **Background:** [Career history]
- **Role in Deal:** [Decision maker/Champion/Evaluator]
- **Talking Point:** [Personal connection to reference]

## Context & History
- [Key points from prior interactions]
- [Open commitments or action items]

## Suggested Agenda
1. **Open** — [Reference point]
2. **[Topic]** — [Discussion point]
3. **Next Steps** — [Proposed follow-up]

## Discovery Questions
1. [Question about situation]
2. [Question about pain points]
3. [Question about timeline]

## Potential Objections
| Objection | Response |
|-----------|----------|
| [Likely objection] | [How to address] |
```

### Meeting Type Variations

- **Discovery**: Focus on questions, qualification signals
- **Demo**: Tailored examples, technical requirements
- **Negotiation**: Address concerns, justify value
- **Check-in/QBR**: Review wins, expansion opportunities

---

## Competitive Intelligence

Research competitors and generate interactive battle cards.

### Output Components

- **Comparison Matrix**: Feature-by-feature comparison
- **Positioning Analysis**: How competitors position vs. you
- **Talk Tracks**: What to say when competitor comes up
- **Objection Handling**: Responses to competitive claims
- **Landmine Questions**: Questions to set and defuse

### Battle Card Format

```
# Competitive Battle Card: [Competitor]

## Quick Comparison
| Capability | Us | Them |
|------------|-----|------|
| [Feature] | ✓ | ✗ |

## Positioning
**Their Message:** [How they position]
**Our Counter:** [How we respond]

## When They Come Up
**If customer mentions [Competitor]:**
[Talk track]

## Objection Handling
| They Say | You Say |
|----------|---------|
| "[Claim]" | "[Response]" |

## Landmines to Set
- Ask about [topic that exposes weakness]

## Win/Loss Themes
- **We Win When:** [Scenarios]
- **We Lose When:** [Scenarios]
```

---

## Pipeline Management

### Pipeline Review

Analyze pipeline health, prioritize deals, and get action recommendations.

**Health Dimensions:**
- Stage distribution
- Deal velocity
- Coverage ratio
- Risk concentration

**Output:**
- Health score by dimension
- Priority action list
- Deal prioritization matrix
- Risk flags (stale, stuck, past close date)
- Pipeline shape analysis
- Weekly action plan

### Forecast Generation

Generate weighted forecast with scenarios and gap analysis.

**Output:**
- Forecast summary (commit vs. upside)
- Best/likely/worst scenarios
- Pipeline by stage with probabilities
- Risk flags affecting forecast
- Gap analysis to target
- Recommendations

---

## Outreach Drafting

Research a prospect then draft personalized cold outreach.

### Process

1. **Research First**: Always research before drafting
2. **Find Hooks**: Identify personalization opportunities
3. **Draft Options**: Email + LinkedIn messaging
4. **Follow-up Sequence**: Multi-touch cadence

### Output Format

```
## Research Summary
[Key findings relevant to outreach]

## Email Draft
**Subject:** [Option 1] / [Option 2]

[Personalized email body]

## LinkedIn Message
[Shorter, conversational version]

## Follow-up Sequence
- Day 3: [Follow-up 1]
- Day 7: [Follow-up 2]
- Day 14: [Break-up email]
```

---

## Call Processing

Process call notes or transcripts into actionable outputs.

### What You Get

- **Internal Summary**: Key discussion points, signals, next steps
- **Customer Follow-up Email**: Draft ready to send
- **Action Items**: With owners and due dates
- **Competitive Intel**: Any competitor mentions
- **CRM Updates**: Fields to update (with CRM connected)

---

## Daily Briefing

Get a prioritized daily sales briefing.

### Modes

- **Morning**: Today's meetings, priority actions, pipeline alerts
- **End-of-Day**: Wrap-up, tomorrow prep, wins/losses

### Output Format

```
# Daily Briefing — [Date]

## Priority Action
[Single most important thing to do]

## Today's Numbers
| Metric | Value |
|--------|-------|
| Pipeline | $X |
| Meetings | N |
| Follow-ups Due | N |

## Today's Meetings
| Time | Company | Type | Prep Status |
|------|---------|------|-------------|

## Pipeline Alerts
- [Alert 1]
- [Alert 2]

## Suggested Actions
1. [Action with rationale]
```

---

## Tool Connections

| Category | Placeholder | Examples |
|----------|-------------|----------|
| CRM | `~~CRM` | HubSpot, Salesforce, Close, Pipedrive |
| Chat | `~~chat` | Slack, Microsoft Teams |
| Email | `~~email` | Microsoft 365, Gmail |
| Calendar | `~~calendar` | Microsoft 365, Google Calendar |
| Enrichment | `~~enrichment` | Clay, ZoomInfo, Apollo |
| Transcripts | `~~transcripts` | Fireflies, Gong, Chorus |

### Working Without Connectors

This skill works standalone:
- Web research for account intelligence
- Manual pipeline data entry
- Paste call notes for processing
- Type meeting details for prep

Connectors enhance but aren't required.
