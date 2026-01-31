---
name: finance
description: Complete finance and accounting skill for journal entries, reconciliation, financial statements, variance analysis, close management, and audit support. Use when preparing journal entries, reconciling accounts, generating financial statements, analyzing variances, managing month-end close, or supporting SOX compliance. Trigger phrases include "prepare journal entry for", "reconcile", "income statement for", "variance analysis on", "close status", "SOX testing for", "flux analysis".
---

# Finance Skill

Streamline finance and accounting workflows with structured frameworks for journal entries, reconciliation, financial reporting, and audit support.

## Core Capabilities

- **Journal Entry Preparation**: Proper debits/credits with documentation
- **Reconciliation**: GL to subledger, bank, intercompany
- **Financial Statements**: Income statement, balance sheet, cash flow
- **Variance Analysis**: Budget vs. actual with driver decomposition
- **Close Management**: Month-end close tracking and optimization
- **Audit Support**: SOX 404 compliance and control testing

## Quick Commands

| Command | Usage | Description |
|---------|-------|-------------|
| `/je` | `/je [type] [period]` | Prepare journal entry |
| `/recon` | `/recon [account] [period]` | Account reconciliation |
| `/income-statement` | `/income-statement [period]` | Generate income statement |
| `/flux` | `/flux [area] [periods]` | Variance/flux analysis |
| `/sox` | `/sox [control-area] [period]` | SOX compliance testing |

---

## Journal Entry Preparation

### Standard Entry Types

**AP Accrual:**
```
Dr. Expense Account         $X,XXX
    Cr. Accrued Liabilities     $X,XXX
```

**Fixed Asset Capitalization:**
```
Dr. Fixed Assets            $X,XXX
    Cr. Accounts Payable        $X,XXX
```

**Prepaid Amortization:**
```
Dr. Expense Account         $X,XXX
    Cr. Prepaid Expense         $X,XXX
```

**Payroll Accrual:**
```
Dr. Salary Expense          $X,XXX
Dr. Benefits Expense        $X,XXX
    Cr. Accrued Payroll         $X,XXX
```

**Revenue Recognition:**
```
Dr. Deferred Revenue        $X,XXX
    Cr. Revenue                 $X,XXX
```

### Journal Entry Format

```markdown
# Journal Entry: [Description]

**Date:** [Date]
**Period:** [Month/Year]
**Preparer:** [Name]
**Reviewer:** [Name]

## Entry
| Account | Description | Debit | Credit |
|---------|-------------|-------|--------|
| [Acct #] | [Description] | $X,XXX | |
| [Acct #] | [Description] | | $X,XXX |
| **Total** | | **$X,XXX** | **$X,XXX** |

## Supporting Documentation
- [Document 1]
- [Document 2]

## Purpose/Rationale
[Why this entry is being made]

## Approval
| Role | Name | Date |
|------|------|------|
| Preparer | | |
| Reviewer | | |
```

### Approval Matrix

| Entry Amount | Approval Required |
|--------------|-------------------|
| < $10,000 | Staff Accountant |
| $10,000 - $100,000 | Accounting Manager |
| $100,000 - $500,000 | Controller |
| > $500,000 | CFO |

---

## Reconciliation

### GL to Subledger

```markdown
# Reconciliation: [Account Name]

**Period:** [Month/Year]
**Account:** [Account Number]

## Summary
| Description | Amount |
|-------------|--------|
| GL Balance | $X,XXX |
| Subledger Balance | $X,XXX |
| Difference | $X,XXX |

## Reconciling Items

### Timing Differences
| Item | Amount | Expected Clear Date |
|------|--------|---------------------|

### Adjustments Needed
| Item | Amount | Action Required |
|------|--------|-----------------|

### Items Under Investigation
| Item | Amount | Age | Owner |
|------|--------|-----|-------|

## Conclusion
[Reconciled / Adjustments required / Investigation needed]
```

### Bank Reconciliation

```markdown
# Bank Reconciliation: [Account]

**Period End:** [Date]

## Summary
| Description | Amount |
|-------------|--------|
| Bank Balance per Statement | $X,XXX |
| Add: Deposits in Transit | $X,XXX |
| Less: Outstanding Checks | ($X,XXX) |
| Adjusted Bank Balance | $X,XXX |
| GL Balance | $X,XXX |
| Difference | $0 |

## Outstanding Items
### Deposits in Transit
| Date | Reference | Amount |
|------|-----------|--------|

### Outstanding Checks
| Check # | Date | Payee | Amount |
|---------|------|-------|--------|

## Stale Items (>90 days)
[Items requiring follow-up]
```

### Reconciling Item Categories

- **Timing**: Will clear naturally (deposits in transit, outstanding checks)
- **Adjustments**: Require JE to correct (errors, omissions)
- **Investigation**: Need research before resolution

---

## Financial Statements

### Income Statement Format

```markdown
# Income Statement
## For the Period Ended [Date]

| | Current Period | Prior Period | Variance | % |
|--|----------------|--------------|----------|---|
| **Revenue** | | | | |
| Product Revenue | $X,XXX | $X,XXX | $X | X% |
| Service Revenue | $X,XXX | $X,XXX | $X | X% |
| **Total Revenue** | **$X,XXX** | **$X,XXX** | | |
| | | | | |
| **Cost of Revenue** | | | | |
| [Line items] | | | | |
| **Gross Profit** | **$X,XXX** | **$X,XXX** | | |
| **Gross Margin** | **X%** | **X%** | | |
| | | | | |
| **Operating Expenses** | | | | |
| Sales & Marketing | $X,XXX | $X,XXX | | |
| R&D | $X,XXX | $X,XXX | | |
| G&A | $X,XXX | $X,XXX | | |
| **Total OpEx** | **$X,XXX** | **$X,XXX** | | |
| | | | | |
| **Operating Income** | **$X,XXX** | **$X,XXX** | | |
| **Operating Margin** | **X%** | **X%** | | |
```

### Key Metrics

| Metric | Formula |
|--------|---------|
| Gross Margin | Gross Profit / Revenue |
| Operating Margin | Operating Income / Revenue |
| Net Margin | Net Income / Revenue |
| Revenue Growth | (Current - Prior) / Prior |

---

## Variance Analysis

### Waterfall Analysis

```markdown
# Variance Analysis: [Area]

## Period: [Current] vs. [Prior/Budget]

## Summary
| Description | Amount |
|-------------|--------|
| [Prior/Budget] | $X,XXX |
| [Current Actual] | $X,XXX |
| Total Variance | $X,XXX (X%) |

## Variance Decomposition

```
[Prior/Budget]: $100,000
        |
        +-- Volume: +$15,000 (more units sold)
        |
        +-- Price: -$5,000 (lower ASP)
        |
        +-- Mix: +$3,000 (higher-margin products)
        |
[Actual]: $113,000
```

## Detailed Drivers

| Driver | Impact | Explanation |
|--------|--------|-------------|
| Volume | +$15,000 | [Explanation] |
| Price | -$5,000 | [Explanation] |
| Mix | +$3,000 | [Explanation] |

## Materiality Assessment
[Whether variance requires management attention]

## Recommendations
- [Action item based on analysis]
```

### Materiality Thresholds

| Line Item | Threshold |
|-----------|-----------|
| Revenue | ±5% or $100K |
| Gross Margin | ±200 bps |
| Operating Expenses | ±10% or $50K |
| Net Income | ±5% |

---

## Close Management

### 5-Day Close Calendar

| Day | Activities |
|-----|------------|
| Day 1 | Subledger closes, cash reconciliation, revenue cutoff |
| Day 2 | AP accruals, prepaid amortization, fixed asset entries |
| Day 3 | Payroll accrual, intercompany reconciliation |
| Day 4 | Management review, flux analysis, adjustments |
| Day 5 | Final review, financial statement preparation |

### Close Status Tracker

```markdown
# Month-End Close Status: [Month]

## Overall Status: [On Track / At Risk / Behind]

## Task Status
| Task | Owner | Due | Status | Notes |
|------|-------|-----|--------|-------|
| Cash reconciliation | | Day 1 | ✓ | |
| Revenue cutoff | | Day 1 | In Progress | |
| AP accruals | | Day 2 | Pending | |

## Blockers
- [Blocker with owner and resolution plan]

## Risks
- [Risk with mitigation]
```

---

## Audit Support

### SOX 404 Control Testing

**Control Categories:**
- Revenue recognition
- Cash and treasury
- Procure-to-pay
- Payroll
- Financial close
- IT General Controls (ITGC)

### Sample Selection

| Population Size | Sample Size |
|-----------------|-------------|
| 1-10 | All |
| 11-50 | 10 |
| 51-250 | 25 |
| 251+ | 30-40 |

### Testing Documentation

```markdown
# Control Test: [Control Name]

## Control Information
| Field | Value |
|-------|-------|
| Control ID | [ID] |
| Control Owner | [Name] |
| Frequency | [Daily/Weekly/Monthly/Quarterly] |
| Type | [Preventive/Detective] |

## Test Objective
[What we're testing]

## Sample Selection
- Population: [N items]
- Sample Size: [N items]
- Selection Method: [Random/Systematic/Targeted]

## Test Results
| Sample # | Item | Test Performed | Result | Exception |
|----------|------|----------------|--------|-----------|

## Conclusion
| Result | Count |
|--------|-------|
| Pass | N |
| Fail | N |
| N/A | N |

## Deficiency Classification
[No deficiency / Deficiency / Significant Deficiency / Material Weakness]
```

### Deficiency Classification

- **Deficiency**: Control doesn't operate as designed but compensating controls exist
- **Significant Deficiency**: More than remote likelihood of more-than-inconsequential misstatement
- **Material Weakness**: Reasonable possibility of material misstatement

---

## Tool Connections

| Category | Placeholder | Examples |
|----------|-------------|----------|
| Data Warehouse | `~~data warehouse` | Snowflake, BigQuery, Databricks |
| Chat | `~~chat` | Slack, Microsoft Teams |
| Email | `~~email` | Microsoft 365, Gmail |
| Cloud Storage | `~~cloud storage` | Microsoft 365, Google Drive |

### Working Without Connectors

All frameworks work manually:
- Enter transaction details for JEs
- Input balances for reconciliation
- Provide data for variance analysis

Connectors enable automated data retrieval.
