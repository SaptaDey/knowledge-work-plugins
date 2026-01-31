---
name: legal
description: Complete legal skill for contract review, NDA triage, compliance navigation, risk assessment, and templated responses. Use when reviewing contracts against playbook, triaging NDAs, handling data subject requests, assessing legal risks, preparing for legal meetings, or generating templated legal responses. Trigger phrases include "review this contract", "triage this NDA", "respond to this DSR", "assess the risk of", "brief me for", "vendor check on", "legal response for".
---

# Legal Skill

Accelerate legal workflows with structured frameworks for contract review, compliance, risk assessment, and templated responses.

## Core Capabilities

- **Contract Review**: Analyze contracts against organizational playbook
- **NDA Triage**: Screen and classify NDAs for approval routing
- **Compliance**: Navigate privacy regulations (GDPR, CCPA, etc.)
- **Risk Assessment**: Classify and score legal risks
- **Meeting Briefing**: Prepare for legally-relevant meetings
- **Canned Responses**: Generate templated responses for common inquiries

## Quick Commands

| Command | Usage | Description |
|---------|-------|-------------|
| `/review-contract` | `/review-contract` | Review contract against playbook |
| `/triage-nda` | `/triage-nda` | NDA pre-screening |
| `/respond` | `/respond [inquiry-type]` | Generate templated response |
| `/brief` | `/brief [daily\|topic\|incident]` | Generate contextual briefing |
| `/vendor-check` | `/vendor-check [vendor]` | Check vendor agreement status |

---

## Contract Review

### Process

1. **Identify contract type** (MSA, SaaS, vendor, partnership, etc.)
2. **Extract key terms** (parties, term, fees, liability, IP, termination)
3. **Compare against playbook** (standard positions, acceptable ranges)
4. **Flag deviations** with severity classification
5. **Generate redline suggestions**

### Deviation Classification

| Flag | Meaning | Action |
|------|---------|--------|
| **GREEN** | Acceptable as-is or minor deviation | Proceed |
| **YELLOW** | Moderate deviation, needs review | Negotiate or escalate |
| **RED** | Significant issue, unacceptable position | Reject or executive approval |

### Output Format

```markdown
# Contract Review: [Document Name]

## Summary
| Field | Value |
|-------|-------|
| Type | [Contract type] |
| Counterparty | [Company name] |
| Value | [$Amount] |
| Term | [Duration] |

## Overall Assessment: [GREEN/YELLOW/RED]

## Key Findings

### RED Issues
| Clause | Issue | Our Position | Recommendation |
|--------|-------|--------------|----------------|

### YELLOW Issues
| Clause | Issue | Our Position | Recommendation |
|--------|-------|--------------|----------------|

### Notable GREEN Terms
- [Favorable term]

## Redline Suggestions
1. Section [X]: [Suggested language]

## Business Impact
[How deviations affect the business]

## Recommendation
[Proceed / Negotiate / Reject / Escalate]
```

---

## NDA Triage

### Classification Criteria

**GREEN (Standard — Auto-approve):**
- Mutual NDA
- Standard term (1-3 years)
- Standard carveouts present
- No non-standard obligations

**YELLOW (Needs Review):**
- One-way (we're disclosing)
- Extended term (>3 years)
- Missing standard carveouts
- Unusual jurisdiction
- Residuals clause concerns

**RED (Significant Issues):**
- Perpetual term
- Missing key carveouts
- Onerous obligations
- Liability concerns
- Requires executive approval

### Required Carveouts

Standard NDAs should carve out:
- Publicly available information
- Previously known information
- Independently developed information
- Information received from third parties
- Information required by law to disclose

### Residuals Clause Analysis

**Acceptable**: Limits to unaided memory, excludes trade secrets
**Concerning**: Broad residuals without limitations
**Unacceptable**: Allows derivative works from confidential info

### Output Format

```markdown
# NDA Triage: [Counterparty]

## Classification: [GREEN/YELLOW/RED]

## Summary
| Field | Value | Flag |
|-------|-------|------|
| Direction | Mutual/One-way | |
| Term | [Duration] | |
| Governing Law | [Jurisdiction] | |

## Carveout Analysis
| Carveout | Present | Notes |
|----------|---------|-------|
| Public information | ✓/✗ | |
| Prior knowledge | ✓/✗ | |
| Independent development | ✓/✗ | |
| Third-party receipt | ✓/✗ | |
| Legal requirement | ✓/✗ | |

## Issues Found
- [Issue 1]
- [Issue 2]

## Routing
[Auto-approve / Legal review / Executive approval]
```

---

## Compliance

### Supported Regulations

- **GDPR** (EU)
- **CCPA/CPRA** (California)
- **LGPD** (Brazil)
- **POPIA** (South Africa)
- **PIPEDA** (Canada)

### Data Subject Request Handling

**DSR Types:**
- Access (what data we hold)
- Deletion (right to be forgotten)
- Portability (data export)
- Correction (fix inaccuracies)
- Objection (opt-out of processing)

**Response Timeline:**
| Regulation | Standard | Extension |
|------------|----------|-----------|
| GDPR | 30 days | +60 days |
| CCPA | 45 days | +45 days |

### DPA Review Checklist

- [ ] Data processing purposes defined
- [ ] Subprocessor requirements
- [ ] Security measures specified
- [ ] Breach notification timeline
- [ ] Data retention and deletion
- [ ] Cross-border transfer mechanisms
- [ ] Audit rights
- [ ] Termination obligations

---

## Risk Assessment

### Severity × Likelihood Matrix

|  | Low Likelihood | Medium | High |
|--|----------------|--------|------|
| **High Severity** | Medium | High | Critical |
| **Medium Severity** | Low | Medium | High |
| **Low Severity** | Low | Low | Medium |

### Risk Classification

**Critical**: Immediate action required, executive notification
**High**: Prioritize resolution, regular monitoring
**Medium**: Address in normal course, document mitigation
**Low**: Monitor, no immediate action needed

### When to Escalate to Outside Counsel

- Litigation threatened or filed
- Regulatory investigation
- Material M&A transaction
- Novel legal questions
- Bet-the-company decisions
- Criminal or fraud allegations

### Risk Assessment Output

```markdown
# Legal Risk Assessment: [Matter]

## Risk Score: [Critical/High/Medium/Low]

## Assessment
| Factor | Rating | Notes |
|--------|--------|-------|
| Severity | [H/M/L] | |
| Likelihood | [H/M/L] | |
| Financial Exposure | [$Range] | |
| Reputational Impact | [H/M/L] | |

## Analysis
[Description of the risk]

## Recommended Actions
1. [Immediate action]
2. [Follow-up action]

## Monitoring
[How to track this risk]

## Escalation
[Required/Not required] — [Reason]
```

---

## Canned Responses

### Supported Inquiry Types

| Type | Description |
|------|-------------|
| **DSR** | Data subject requests |
| **Discovery Hold** | Litigation hold notices |
| **Vendor Questions** | Security questionnaires |
| **NDA Request** | Incoming NDA requests |
| **Privacy Inquiry** | Customer privacy questions |
| **Subpoena** | Legal process responses |
| **Insurance** | Incident notifications |

### Escalation Triggers

Certain phrases/situations require individualized attention:
- Litigation threats
- Regulatory references
- Media involvement
- Executive names
- Specific dollar amounts
- Criminal allegations

---

## Meeting Briefing

### Briefing Types

**Daily Briefing:**
- Calendar items with legal relevance
- Pending action items
- Deadlines approaching

**Topic Briefing:**
- Deep dive on specific matter
- Background research
- Key considerations

**Incident Briefing:**
- Incident summary
- Legal exposure assessment
- Recommended response

### Output Format

```markdown
# Legal Briefing: [Topic]

## Summary
[One paragraph overview]

## Background
[Relevant history and context]

## Key Considerations
- [Consideration 1]
- [Consideration 2]

## Risks
| Risk | Likelihood | Impact |
|------|------------|--------|

## Recommended Position
[What legal recommends]

## Talking Points
- [Point 1]
- [Point 2]

## Action Items
- [ ] [Action with owner and deadline]
```

---

## Tool Connections

| Category | Placeholder | Examples |
|----------|-------------|----------|
| Chat | `~~chat` | Slack, Microsoft Teams |
| Cloud Storage | `~~cloud storage` | Box, Egnyte, Google Drive |
| Project Tracker | `~~project tracker` | Jira, matter management |
| Email | `~~email` | Microsoft 365, Gmail |
| Calendar | `~~calendar` | Microsoft 365, Google Calendar |

### Working Without Connectors

All frameworks work manually:
- Paste contract text for review
- Enter NDA terms for triage
- Type inquiry details for responses

Connectors enhance context gathering and tracking.
