---
name: product-management
description: Complete product management skill for specs, roadmaps, user research, metrics, competitive analysis, and stakeholder communication. Use when writing PRDs or feature specs, planning roadmaps, synthesizing user research, tracking product metrics, analyzing competitors, or communicating with stakeholders. Trigger phrases include "write a spec for", "PRD for", "roadmap update", "synthesize this research", "analyze these metrics", "competitive analysis of", "stakeholder update", "what should we build".
---

# Product Management Skill

Transform product work with structured frameworks for specs, roadmaps, research synthesis, metrics analysis, and stakeholder communication.

## Core Capabilities

- **Feature Specs**: Write structured PRDs with user stories and requirements
- **Roadmap Management**: Plan and prioritize using RICE, MoSCoW, ICE
- **User Research**: Synthesize qualitative and quantitative research
- **Metrics Tracking**: Define, track, and analyze product metrics
- **Competitive Analysis**: Feature comparisons and positioning analysis
- **Stakeholder Comms**: Tailored updates for different audiences

## Quick Commands

| Command | Usage | Description |
|---------|-------|-------------|
| `/write-spec` | `/write-spec [feature]` | Write PRD/feature spec |
| `/roadmap` | `/roadmap [update\|create\|prioritize]` | Manage roadmap |
| `/research` | `/research [synthesize]` | Synthesize user research |
| `/metrics` | `/metrics [review]` | Analyze product metrics |
| `/competitive` | `/competitive [competitor]` | Competitive analysis |
| `/update` | `/update [audience]` | Generate stakeholder update |

---

## Feature Specs (PRDs)

### Structure

```markdown
# [Feature Name]

## Problem Statement
[What problem we're solving and for whom]

## Goals
- [Goal 1 with measurable outcome]
- [Goal 2]

## Non-Goals
- [Explicitly out of scope]

## User Stories
As a [user type], I want to [action] so that [benefit].

### Acceptance Criteria
- Given [context], when [action], then [outcome]

## Requirements

### P0 (Must Have)
- [Requirement]

### P1 (Should Have)
- [Requirement]

### P2 (Nice to Have)
- [Requirement]

## Success Metrics
| Metric | Baseline | Target | Timeline |
|--------|----------|--------|----------|

## Open Questions
- [Question needing resolution]

## Timeline
| Phase | Date | Deliverable |
|-------|------|-------------|
```

### Writing Standards

**User Stories (INVEST):**
- **I**ndependent
- **N**egotiable
- **V**aluable
- **E**stimable
- **S**mall
- **T**estable

**Acceptance Criteria (Given/When/Then):**
- Given [precondition]
- When [action]
- Then [expected result]

---

## Roadmap Management

### Formats

**Now/Next/Later:**
```
| Now (0-6 weeks) | Next (6-12 weeks) | Later (12+ weeks) |
|-----------------|-------------------|-------------------|
| [Feature] | [Feature] | [Feature] |
```

**Quarterly Themes:**
```
| Q1: [Theme] | Q2: [Theme] | Q3: [Theme] | Q4: [Theme] |
|-------------|-------------|-------------|-------------|
```

**OKR-Aligned:**
```
Objective: [Objective]
├── KR1: [Key Result] → [Feature 1], [Feature 2]
├── KR2: [Key Result] → [Feature 3]
```

### Prioritization Frameworks

**RICE Score:**
```
Score = (Reach × Impact × Confidence) / Effort

Reach: Users affected per quarter
Impact: 3=Massive, 2=High, 1=Medium, 0.5=Low, 0.25=Minimal
Confidence: 100%/80%/50%
Effort: Person-months
```

**MoSCoW:**
- **Must Have**: Critical for launch
- **Should Have**: Important but not critical
- **Could Have**: Nice to have
- **Won't Have**: Explicitly excluded

**ICE Score:**
```
Score = Impact × Confidence × Ease
(Each rated 1-10)
```

### Capacity Planning

Typical allocation:
- 60-70% Feature work
- 20% Tech debt
- 10% Unplanned/buffer

---

## User Research Synthesis

### Methodology

**Thematic Analysis:**
1. Extract observations from each source
2. Code observations into themes
3. Cluster themes into patterns
4. Identify insights and opportunities

**Triangulation:**
- Cross-reference qualitative + quantitative
- Look for convergence across methods
- Note divergence for further investigation

### Output Format

```markdown
# Research Synthesis: [Topic]

## Overview
- **Sources**: [N interviews, N survey responses, etc.]
- **Period**: [Date range]
- **Confidence**: [High/Medium/Low]

## Key Findings

### Finding 1: [Title]
**Evidence**: [Quote or data point]
**Frequency**: [X of Y participants]
**Impact**: [High/Medium/Low]

## User Segments
| Segment | Size | Characteristics | Needs |
|---------|------|-----------------|-------|

## Opportunity Areas
1. [Opportunity with evidence]

## Recommendations
- [Recommendation with rationale]

## Open Questions
- [Question for further research]
```

---

## Metrics Tracking

### Metrics Hierarchy

**North Star Metric**: Single metric capturing core value

**L1 Health Indicators:**
- Acquisition
- Activation
- Engagement
- Retention
- Monetization
- Satisfaction

**L2 Diagnostics**: Deeper metrics explaining L1 movement

### Goal Setting (OKRs)

**Objective**: Qualitative, inspirational
**Key Results**: Quantitative, measurable

Format: "Increase [metric] from [baseline] to [target] by [date]"

### Review Cadences

| Cadence | Duration | Focus |
|---------|----------|-------|
| Weekly | 15-30 min | Key metrics, anomalies |
| Monthly | 30-60 min | Full dashboard, trends |
| Quarterly | 60-90 min | Strategic review, goal-setting |

### Metrics Review Output

```markdown
# Metrics Review — [Period]

## Summary
[One paragraph on overall health]

## Scorecard
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|

## Trend Analysis
[Key trends with explanations]

## Bright Spots
- [Positive signal]

## Areas of Concern
- [Issue needing attention]

## Recommended Actions
1. [Action with rationale]
```

---

## Competitive Analysis

### Framework

**Landscape Mapping:**
- Direct competitors (same solution, same market)
- Indirect competitors (different solution, same problem)
- Adjacent competitors (same solution, different market)

**Feature Comparison:**
| Capability | Us | Competitor A | Competitor B |
|------------|-----|--------------|--------------|
| [Feature] | ✓✓ | ✓ | ✗ |

Rating: ✓✓ (best in class), ✓ (has it), ~ (partial), ✗ (missing)

**Positioning Analysis:**
- Their positioning statement
- Target audience
- Key differentiators
- Pricing strategy

### Output Format

```markdown
# Competitive Analysis: [Competitor]

## Overview
| Field | Value |
|-------|-------|
| Founded | [Year] |
| Funding | [Amount] |
| Target Market | [Segment] |

## Feature Comparison
[Matrix]

## Positioning
**Their Message**: [How they position]
**Our Counter**: [Our differentiation]

## Strengths & Weaknesses
| Strengths | Weaknesses |
|-----------|------------|

## Strategic Implications
- [Implication for our roadmap]
```

---

## Stakeholder Communications

### Templates by Audience

**Executive Update:**
```
## TL;DR
[One sentence summary]

## Status: [Green/Yellow/Red]

## Progress
- [Key milestone]

## Risks
- [Risk with mitigation]

## Asks
- [What you need from them]
```

**Engineering Update:**
```
## Shipped
- [Feature/fix]

## In Progress
- [Work item] — [Status]

## Blockers
- [Blocker needing resolution]

## Decisions Needed
- [Decision with options]
```

### Status Framework

- **Green**: On track, no concerns
- **Yellow**: At risk, mitigation in place
- **Red**: Off track, escalation needed

---

## Tool Connections

| Category | Placeholder | Examples |
|----------|-------------|----------|
| Project Tracker | `~~project tracker` | Linear, Jira, Asana, Monday |
| Chat | `~~chat` | Slack, Microsoft Teams |
| Documents | `~~documents` | Notion, Confluence, Google Docs |
| Design | `~~design` | Figma |
| Analytics | `~~analytics` | Amplitude, Mixpanel, Pendo |
| Support | `~~support` | Intercom, Zendesk |
| Transcripts | `~~transcripts` | Fireflies, Dovetail |

### Working Without Connectors

All frameworks work manually:
- Input feature ideas directly
- Paste research notes
- Enter metrics data
- Type competitive intel

Connectors enhance but aren't required.
