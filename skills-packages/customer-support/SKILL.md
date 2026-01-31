---
name: customer-support
description: Complete customer support skill for triaging tickets, drafting responses, escalating issues, researching customer context, and building knowledge base articles. Use when handling support tickets, responding to customer issues, assessing ticket priority (P1-P4), researching customer questions, packaging escalations for engineering/product/leadership, writing KB articles, or any customer-facing communication. Trigger phrases include "triage this ticket", "draft a response", "escalate this issue", "research this customer question", "write a KB article", "handle this support case".
---

# Customer Support Skill

Transform support interactions into delightful customer experiences. This skill provides complete workflows for triaging, responding, escalating, researching, and documenting customer support issues.

## Core Capabilities

- **Ticket Triage**: Categorize issues, assign priority (P1-P4), and route to appropriate teams
- **Response Drafting**: Write professional, empathetic customer communications
- **Escalation Management**: Structure and package escalations with full context
- **Customer Research**: Multi-source research with confidence-scored answers
- **Knowledge Management**: Create and maintain KB articles from resolved issues

## Quick Commands

| Command | Usage | Description |
|---------|-------|-------------|
| `/triage` | `/triage <ticket description>` | Categorize, prioritize, and route a ticket |
| `/draft-response` | `/draft-response <context>` | Draft a customer-facing response |
| `/escalate` | `/escalate <issue details>` | Package an escalation brief |
| `/research` | `/research <question>` | Research a customer question |
| `/kb-article` | `/kb-article <resolved ticket>` | Create a KB article from a resolution |

---

## Ticket Triage

### Category Taxonomy

Assign every ticket a **primary category** and optionally a **secondary category**:

| Category | Description | Signal Words |
|----------|-------------|-------------|
| **Bug** | Product behaving incorrectly | Error, broken, crash, not working, unexpected |
| **How-to** | Customer needs guidance | How do I, can I, where is, setting up |
| **Feature request** | Capability doesn't exist | Would be great if, wish I could, any plans to |
| **Billing** | Payment, subscription, pricing | Charge, invoice, payment, refund, upgrade |
| **Account** | Access, permissions, settings | Login, password, access, locked out |
| **Integration** | Third-party tools or APIs | API, webhook, integration, sync |
| **Security** | Security or compliance | Data breach, unauthorized, GDPR, SOC 2 |
| **Data** | Data quality or migration | Missing data, export, import, duplicates |
| **Performance** | Speed or availability | Slow, timeout, down, unavailable |

**Category Tips:**
- If both bug and feature request, bug is primary
- "It used to work" = Bug; "I want it different" = Feature request
- When in doubt, lean toward Bug

### Priority Framework

#### P1 — Critical
Production down, data loss/corruption, security breach, all users affected.
- **SLA**: Respond within 1 hour. Updates every 1-2 hours.

#### P2 — High
Major feature broken, key workflow blocked, no workaround.
- **SLA**: Respond within 4 hours. Updates every 4 hours.

#### P3 — Medium
Feature partially broken, workaround available, single user affected.
- **SLA**: Respond within 1 business day.

#### P4 — Low
Minor inconvenience, cosmetic issue, feature request.
- **SLA**: Respond within 2 business days.

### Routing Rules

| Route to | When |
|----------|------|
| **Tier 1** | How-to, known issues, billing, password resets |
| **Tier 2** | Bugs needing investigation, complex config, integration troubleshooting |
| **Engineering** | Confirmed bugs, infrastructure issues |
| **Product** | Feature requests with demand, design decisions |
| **Security** | Data access, vulnerabilities, compliance |
| **Billing/Finance** | Refunds, contract disputes |

### Triage Workflow

```
/triage <ticket text>
```

1. **Parse**: Extract core problem, symptoms, customer context, urgency signals
2. **Categorize**: Assign primary/secondary category and priority
3. **Check duplicates**: Search ~~support platform and ~~knowledge base for similar issues
4. **Route**: Recommend team based on category and complexity
5. **Output**: Structured triage with suggested initial response

**Output Format:**
```
## Triage: [One-line summary]

**Category:** [Primary] / [Secondary]
**Priority:** [P1-P4] — [Justification]
**Product area:** [Area/team]

### Issue Summary
[2-3 sentence summary]

### Key Details
- **Customer:** [Name/account]
- **Impact:** [Who and what affected]
- **Workaround:** [Available / Not available]
- **Related tickets:** [Links]

### Routing Recommendation
**Route to:** [Team]
**Why:** [Reasoning]

### Suggested Initial Response
[Draft response using appropriate template]
```

---

## Response Drafting

### Core Principles

1. **Lead with empathy**: Acknowledge before solving
2. **Be direct**: Bottom-line-up-front
3. **Be honest**: Never overpromise
4. **Be specific**: Concrete details, timelines, names
5. **Own it**: "We" not "the system"
6. **Close the loop**: Clear next step

### Response Structure

```
1. Acknowledgment (1-2 sentences)
2. Core Message (1-3 paragraphs)
3. Next Steps (1-3 bullets)
4. Closing (1 sentence)
```

### Tone by Situation

| Situation | Tone |
|-----------|------|
| Good news | Celebratory, warm |
| Routine update | Professional, concise |
| Technical response | Precise, patient |
| Delayed delivery | Accountable, specific |
| Bad news | Direct, empathetic |
| Issue/outage | Urgent, transparent |
| Escalation | Executive, confident |

### Response Templates

See `references/response-templates.md` for complete templates covering:
- Bug acknowledgment
- Billing/account issues
- Feature request decline
- Outage communication
- Follow-up after silence

---

## Escalation Management

### When to Escalate

**Escalate when:**
- Bug confirmed, needs code fix
- Multiple customers affected
- Production down or data at risk
- SLA breach imminent
- Customer threatening churn
- Security concern

### Escalation Format

```
ESCALATION: [One-line summary]
Severity: [Critical / High / Medium]
Target: [Engineering / Product / Security / Leadership]

IMPACT
- Customers affected: [Number]
- Workflow impact: [What's broken]
- Revenue at risk: [If applicable]
- SLA status: [Within / At risk / Breached]

ISSUE DESCRIPTION
[3-5 sentences]

REPRODUCTION STEPS (for bugs)
1. [Step]
2. [Step]
Expected: [X]
Actual: [Y]
Environment: [Details]

WHAT'S BEEN TRIED
1. [Action] → [Result]

CUSTOMER COMMUNICATION
- Last update: [Date]
- Customer expectation: [What/when]

WHAT'S NEEDED
- [Specific ask]
- Deadline: [Date]
```

### Follow-up Cadence

| Severity | Internal | Customer |
|----------|----------|----------|
| Critical | Every 2 hours | Every 2-4 hours |
| High | Every 4 hours | Every 4-8 hours |
| Medium | Daily | Every 1-2 days |

---

## Customer Research

### Source Prioritization

**Tier 1 — Official Sources (High Confidence)**
- Product documentation
- Knowledge base / wiki
- Policy documents

**Tier 2 — Organizational Context (Medium-High)**
- CRM records (~~CRM)
- Support tickets (~~support platform)
- Internal documents

**Tier 3 — Team Communications (Medium)**
- Chat history (~~chat)
- Email threads (~~email)
- Meeting notes

**Tier 4 — External Sources (Low-Medium)**
- Web search
- Community forums

### Confidence Levels

- **High**: Confirmed by official docs, multiple sources corroborate
- **Medium**: Found in informal sources, single source
- **Low**: Inferred from related info, sources outdated
- **Unable to Determine**: No relevant info found

### Research Output Format

```
**Direct Answer:** [Bottom-line answer]
**Confidence:** [High / Medium / Low]

**Supporting Evidence:**
- [Source 1]: [What it says]
- [Source 2]: [What it says]

**Caveats:**
- [Limitations or conditions]

**Recommendation:**
- [Ready to share? Verification needed?]
```

---

## Knowledge Management

### Article Types

**How-to Articles:**
```
# How to [task]

[Overview]

## Prerequisites
## Steps
## Verify It Worked
## Common Issues
## Related Articles
```

**Troubleshooting Articles:**
```
# [Problem description]

## Symptoms
## Cause
## Solution
## Prevention
## Still Having Issues?
```

**FAQ Articles:**
```
# [Question]

[Direct answer]

## Details
## Related Questions
```

**Known Issue Articles:**
```
# [Known Issue]: [Description]

**Status:** [Investigating / Workaround Available / Resolved]
**Last updated:** [Date]

## Symptoms
## Workaround
## Fix Timeline
## Updates
```

### Writing for Searchability

- Include exact error messages
- Use customer language, not internal jargon
- Include common synonyms
- Start with a sentence restating the problem

---

## Tool Connections

This skill works with these tool categories (configure your preferred tools):

| Category | Placeholder | Examples |
|----------|-------------|----------|
| Chat | `~~chat` | Slack, Microsoft Teams |
| Email | `~~email` | Microsoft 365, Gmail |
| Support platform | `~~support platform` | Intercom, Zendesk, Freshdesk |
| CRM | `~~CRM` | HubSpot, Salesforce |
| Knowledge base | `~~knowledge base` | Guru, Notion, Confluence |
| Project tracker | `~~project tracker` | Jira, Linear, Asana |

See `references/connectors.md` for MCP server configuration.
