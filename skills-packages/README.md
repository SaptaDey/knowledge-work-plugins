# Knowledge Work Skills

**Skills that turn Claude into a specialist for your role, team, and company.**

These are Anthropic Skill packages converted from the Knowledge Work Plugins. They work with Claude Desktop app, Claude Code, and any environment that supports the Anthropic Skills format.

## Installation

### One-Click Install (Claude Desktop)

1. Download the `.skill` file for your role
2. Open Claude Desktop Settings
3. Go to Skills section
4. Click "Add Skill" and select the downloaded file
5. The skill activates automatically

### Manual Install

Copy the skill folder to your Claude skills directory:

```bash
# macOS/Linux
cp -r skills-packages/[skill-name] ~/.claude/skills/

# Windows
xcopy /E skills-packages\[skill-name] %USERPROFILE%\.claude\skills\
```

### Claude Code

```bash
# Install directly from this repo
claude skills add ./skills-packages/[skill-name]
```

## Available Skills

| Skill | Description | Best For |
|-------|-------------|----------|
| **[productivity](./productivity)** | Task management, memory system, daily workflows | Everyone |
| **[sales](./sales)** | Prospecting, call prep, pipeline, outreach | Sales Teams |
| **[customer-support](./customer-support)** | Triage, responses, escalations, KB articles | Support Teams |
| **[product-management](./product-management)** | Specs, roadmaps, research, metrics | Product Managers |
| **[marketing](./marketing)** | Content, campaigns, brand voice, analytics | Marketing Teams |
| **[legal](./legal)** | Contracts, NDAs, compliance, risk assessment | Legal Teams |
| **[finance](./finance)** | Journal entries, reconciliation, close, audit | Finance Teams |
| **[data](./data)** | SQL, visualization, dashboards, validation | Data/Analytics |
| **[enterprise-search](./enterprise-search)** | Cross-tool search, activity digests | Everyone |
| **[bio-research](./bio-research)** | Clinical trials, pipelines, single-cell | Life Sciences |

## How Skills Work

Each skill is a self-contained folder with:

```
skill-name/
├── SKILL.md              # Main skill file (required)
├── references/           # Supporting documentation
│   ├── connectors.md     # Tool connection guide
│   └── [topic].md        # Topic-specific references
└── assets/               # Templates, files used in output
```

### SKILL.md Structure

```yaml
---
name: skill-name
description: What the skill does and when to use it. Include trigger phrases.
---

# Skill Name

[Skill content - workflows, frameworks, templates]
```

### Automatic Triggering

Skills activate automatically based on the description. Include phrases like:
- "Use when..."
- "Trigger phrases include..."
- "Activate for..."

## Connecting Your Tools

Skills work standalone but are enhanced with MCP tool connections.

### Tool Categories

Skills use `~~placeholder` notation for tool-agnostic workflows:

| Placeholder | Examples |
|-------------|----------|
| `~~chat` | Slack, Microsoft Teams |
| `~~email` | Microsoft 365, Gmail |
| `~~CRM` | HubSpot, Salesforce |
| `~~project tracker` | Jira, Linear, Asana |
| `~~knowledge base` | Notion, Confluence, Guru |
| `~~data warehouse` | Snowflake, BigQuery, Databricks |

### MCP Configuration

Add MCP servers to your Claude settings:

```json
{
  "mcpServers": {
    "slack": {
      "type": "http",
      "url": "https://mcp.slack.com/mcp"
    },
    "hubspot": {
      "type": "http",
      "url": "https://mcp.hubspot.com/anthropic"
    }
  }
}
```

See each skill's `references/connectors.md` for specific configurations.

## Customizing Skills

### For Your Company

1. **Add company context**: Edit SKILL.md to include your terminology, processes
2. **Swap tools**: Update `~~placeholder` references to your actual tools
3. **Adjust workflows**: Modify templates to match how your team works

### For Your Role

1. **Combine skills**: Install multiple skills for cross-functional work
2. **Add references**: Create new reference files for your domain knowledge
3. **Extend triggers**: Update description to include your common phrases

## Creating .skill Packages

To package a skill for distribution:

```bash
# Using the skill-creator tool
python scripts/package_skill.py ./skills-packages/[skill-name]

# Or manually
cd skills-packages/[skill-name]
zip -r ../[skill-name].skill .
```

## Comparison: Plugins vs Skills

| Feature | Cowork Plugins | Desktop Skills |
|---------|---------------|----------------|
| Format | Multiple folders | Single SKILL.md + references |
| Commands | Separate `/command.md` | Integrated in SKILL.md |
| Triggering | Slash commands + auto | Description-based auto |
| MCP Config | `.mcp.json` in folder | In Claude settings |
| Distribution | Plugin marketplace | .skill file or folder |

## Contributing

1. Fork this repository
2. Create or modify skills
3. Test with Claude Desktop or Claude Code
4. Submit a pull request

## License

Apache 2.0 - See [LICENSE](../LICENSE)
