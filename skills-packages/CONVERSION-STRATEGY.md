# Plugin to Skill Package Conversion Strategy

## Overview

This document outlines the strategy for converting Knowledge Work Plugins (Cowork/Claude Code format) to Anthropic Skill Packages (Claude Desktop App format).

## Key Differences

| Aspect | Plugin Format | Skill Package Format |
|--------|--------------|---------------------|
| **Entry Point** | `.claude-plugin/plugin.json` | `SKILL.md` with frontmatter |
| **Structure** | Multiple skills + commands folders | Single SKILL.md + references/ |
| **Commands** | Separate `commands/*.md` files | Integrated into SKILL.md body |
| **Tool Connections** | `.mcp.json` with HTTP servers | Documented in references/connectors.md |
| **Trigger** | Slash commands + auto-trigger | Description-based auto-trigger |

## Conversion Rules

### 1. SKILL.md Frontmatter
```yaml
---
name: [plugin-name]
description: [Comprehensive description covering all skills. Include ALL trigger phrases like "Use when...", "Trigger when user asks...", "Activate for..."]
---
```

### 2. Body Structure
```markdown
# [Plugin Name] Skill

[Brief overview]

## Core Capabilities
- [Skill 1 summary]
- [Skill 2 summary]
- ...

## [Skill 1 Name]
[Full skill content from original SKILL.md]

## [Skill 2 Name]
[Full skill content from original SKILL.md]

## Commands
### /[command-name]
[Command workflow from original command.md]

## Tool Connections
[Summary of required MCP servers with setup instructions]
```

### 3. References Directory
- `references/connectors.md` - MCP server configuration
- `references/[skill-specific].md` - Any skill-specific references
- Preserve original reference files structure

### 4. Assets Directory
- Copy over any assets (templates, HTML files, etc.)
- Maintain original paths where possible

## Placeholder Handling

The `~~placeholder` pattern is preserved with documentation:
- `~~CRM` → "Your CRM (HubSpot, Salesforce, etc.)"
- `~~chat` → "Your chat tool (Slack, Teams, etc.)"
- These are documented in references/connectors.md

## File Size Guidelines

Per skill-creator guidelines:
- Keep SKILL.md under 500 lines when possible
- Move detailed reference material to references/
- Use progressive disclosure pattern for large skills
