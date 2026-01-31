---
name: data
description: Complete data analytics skill for SQL queries, data exploration, visualization, statistical analysis, dashboard building, and data validation. Use when writing SQL queries, exploring datasets, creating visualizations, building dashboards, running statistical analysis, or validating data work before sharing. Trigger phrases include "write a query for", "explore this data", "create a visualization of", "build a dashboard for", "analyze this statistically", "validate this analysis", "what does this data show".
---

# Data Skill

Write SQL, explore datasets, create visualizations, and build dashboards with confidence.

## Core Capabilities

- **SQL Queries**: Correct, performant SQL across all major dialects
- **Data Exploration**: Profile datasets to understand shape and quality
- **Data Visualization**: Publication-quality charts with Python
- **Dashboard Building**: Self-contained HTML dashboards with Chart.js
- **Statistical Analysis**: Descriptive stats, trends, hypothesis testing
- **Data Validation**: QA analyses before sharing with stakeholders

## Quick Commands

| Command | Usage | Description |
|---------|-------|-------------|
| `/write-query` | `/write-query [description]` | Write optimized SQL |
| `/explore-data` | `/explore-data [table]` | Profile a dataset |
| `/create-viz` | `/create-viz [data] [type]` | Create visualization |
| `/build-dashboard` | `/build-dashboard [description]` | Build HTML dashboard |
| `/analyze` | `/analyze [question]` | Answer data question |
| `/validate` | `/validate [analysis]` | QA before sharing |

---

## SQL Queries

### Supported Dialects

- **PostgreSQL** (Aurora, RDS, Supabase, Neon)
- **Snowflake**
- **BigQuery** (Google Cloud)
- **Redshift** (Amazon)
- **Databricks SQL**
- **MySQL** / **SQL Server**

### Dialect-Specific Patterns

**Date Functions:**
| Operation | PostgreSQL | Snowflake | BigQuery |
|-----------|------------|-----------|----------|
| Current date | `CURRENT_DATE` | `CURRENT_DATE()` | `CURRENT_DATE()` |
| Add days | `date + INTERVAL '7 days'` | `DATEADD(day, 7, date)` | `DATE_ADD(date, INTERVAL 7 DAY)` |
| Truncate | `DATE_TRUNC('month', date)` | `DATE_TRUNC('month', date)` | `DATE_TRUNC(date, MONTH)` |

**String Functions:**
| Operation | PostgreSQL | Snowflake | BigQuery |
|-----------|------------|-----------|----------|
| Case-insensitive | `ILIKE` | `ILIKE` | `LOWER() LIKE` |
| Split | `SPLIT_PART()` | `SPLIT_PART()` | `SPLIT()` returns array |

### Common Patterns

**Window Functions:**
```sql
-- Ranking
ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY created_at DESC)

-- Running total
SUM(revenue) OVER (ORDER BY date ROWS UNBOUNDED PRECEDING)

-- Moving average
AVG(revenue) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)

-- Lag/Lead
LAG(value, 1) OVER (PARTITION BY entity ORDER BY date)
```

**CTEs for Readability:**
```sql
WITH
base_users AS (
    SELECT user_id, created_at
    FROM users
    WHERE status = 'active'
),
user_metrics AS (
    SELECT user_id, COUNT(*) as events
    FROM events
    GROUP BY user_id
)
SELECT * FROM user_metrics;
```

**Cohort Retention:**
```sql
WITH cohorts AS (
    SELECT user_id, DATE_TRUNC('month', first_activity) as cohort
    FROM users
)
SELECT
    cohort,
    COUNT(DISTINCT user_id) as cohort_size,
    COUNT(DISTINCT CASE WHEN activity_month = cohort THEN user_id END) as month_0
FROM cohorts
GROUP BY cohort;
```

**Funnel Analysis:**
```sql
WITH funnel AS (
    SELECT
        user_id,
        MAX(CASE WHEN event = 'view' THEN 1 END) as step_1,
        MAX(CASE WHEN event = 'signup' THEN 1 END) as step_2
    FROM events
    GROUP BY user_id
)
SELECT
    SUM(step_1) as viewed,
    SUM(step_2) as signed_up,
    100.0 * SUM(step_2) / NULLIF(SUM(step_1), 0) as conversion_pct
FROM funnel;
```

---

## Data Exploration

### Profiling Output

```markdown
# Data Profile: [Table/File]

## Overview
| Metric | Value |
|--------|-------|
| Rows | N |
| Columns | N |
| Size | X MB |

## Column Analysis
| Column | Type | Nulls | Unique | Sample Values |
|--------|------|-------|--------|---------------|

## Data Quality
| Issue | Count | % |
|-------|-------|---|
| Null values | N | X% |
| Duplicates | N | X% |

## Distributions
[Key column distributions]

## Patterns
- [Pattern 1]
- [Pattern 2]

## Recommendations
- [Data quality issue to address]
```

### Quality Checks

- **Completeness**: Null rates by column
- **Uniqueness**: Duplicate detection
- **Validity**: Values within expected ranges
- **Consistency**: Cross-column logic checks
- **Timeliness**: Data freshness

---

## Data Visualization

### Chart Selection Guide

| Data Type | Comparison | Composition | Distribution | Relationship |
|-----------|------------|-------------|--------------|--------------|
| Categorical | Bar chart | Stacked bar | - | - |
| Time series | Line chart | Area chart | - | - |
| Numerical | - | - | Histogram | Scatter |
| Part-to-whole | - | Pie/Donut | - | - |

### Python Patterns

**Line Chart (matplotlib):**
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(dates, values, marker='o')
ax.set_xlabel('Date')
ax.set_ylabel('Value')
ax.set_title('Trend Over Time')
plt.tight_layout()
```

**Bar Chart (seaborn):**
```python
import seaborn as sns
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df, x='category', y='value', ax=ax)
ax.set_title('Comparison by Category')
```

**Interactive (plotly):**
```python
import plotly.express as px
fig = px.line(df, x='date', y='value', color='segment')
fig.update_layout(title='Interactive Trend')
```

### Design Principles

- **Clarity**: One message per chart
- **Simplicity**: Remove chart junk
- **Accessibility**: Colorblind-friendly palettes
- **Context**: Include baselines and benchmarks

---

## Dashboard Building

### Self-Contained HTML Dashboard

Creates standalone HTML files with:
- KPI cards with trends
- Interactive charts (Chart.js)
- Sortable data tables
- Filter dropdowns
- Responsive design
- No server required

### Dashboard Structure

```markdown
# Dashboard: [Name]

## KPIs
| Metric | Value | Trend |
|--------|-------|-------|

## Charts
1. [Chart type]: [What it shows]
2. [Chart type]: [What it shows]

## Filters
- [Filter 1]
- [Filter 2]

## Data Table
[Sortable table with key data]
```

---

## Statistical Analysis

### Descriptive Statistics

- Count, Mean, Median, Mode
- Standard Deviation, Variance
- Min, Max, Range
- Percentiles (25th, 50th, 75th, 95th, 99th)

### Trend Analysis

- Period-over-period growth
- Moving averages
- Seasonality detection
- Trend line fitting

### Anomaly Detection

- Z-score method (>3 standard deviations)
- IQR method (1.5× interquartile range)
- Contextual anomalies (deviation from expected pattern)

### Hypothesis Testing

- t-test (compare two groups)
- Chi-square (categorical relationships)
- Correlation analysis (relationships between variables)

### Cautious Claims

When presenting findings:
- State confidence levels
- Note sample sizes
- Acknowledge limitations
- Distinguish correlation from causation

---

## Data Validation

### Pre-Delivery Checklist

- [ ] Query logic verified
- [ ] Joins produce expected row counts
- [ ] Filters applied correctly
- [ ] Calculations spot-checked
- [ ] Edge cases handled
- [ ] Results make business sense

### Common Pitfalls

| Pitfall | Detection | Prevention |
|---------|-----------|------------|
| Join explosion | Row count check | Verify join keys |
| Survivorship bias | Compare populations | Include churned users |
| Incomplete periods | Check date ranges | Filter to complete periods |
| Division by zero | Check denominators | Use NULLIF |
| Time zone issues | Spot check | Explicit timezone handling |

### Validation Output

```markdown
# Validation: [Analysis Name]

## Methodology Review
- [x] Appropriate method for question
- [x] Data sources correct
- [ ] Sample size adequate

## Calculation Checks
| Check | Result | Notes |
|-------|--------|-------|
| Row counts | ✓ | |
| Totals reconcile | ✓ | |

## Sanity Checks
- [Check 1]: [Result]
- [Check 2]: [Result]

## Known Limitations
- [Limitation 1]

## Confidence Level
[High/Medium/Low] — [Explanation]

## Ready to Share?
[Yes/No] — [Conditions if any]
```

---

## Tool Connections

| Category | Placeholder | Examples |
|----------|-------------|----------|
| Data Warehouse | `~~data warehouse` | Snowflake, BigQuery, Databricks, Redshift |
| BI Tool | `~~BI tool` | Hex, Mode, Looker |
| Analytics | `~~analytics` | Amplitude, Mixpanel |
| Project Tracker | `~~project tracker` | Jira, Linear |

### Working Without Connectors

All capabilities work with:
- Pasted data or CSV files
- Manual query execution
- Local Python environment
- Exported HTML dashboards

Connectors enable direct database access and automated data retrieval.
