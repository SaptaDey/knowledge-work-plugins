# Connectors Configuration

## How Tool References Work

This skill uses `~~category` placeholders for tool-agnostic workflows. Replace with your specific tools.

## Available Connectors

| Category | Placeholder | Recommended | Alternatives |
|----------|-------------|-------------|--------------|
| Chat | `~~chat` | Slack | Microsoft Teams |
| Email | `~~email` | Microsoft 365 | Gmail |
| Support platform | `~~support platform` | Intercom | Zendesk, Freshdesk, HubSpot Service Hub |
| CRM | `~~CRM` | HubSpot | Salesforce, Pipedrive |
| Knowledge base | `~~knowledge base` | Guru, Notion | Confluence, Help Scout |
| Project tracker | `~~project tracker` | Atlassian (Jira) | Linear, Asana |
| Cloud storage | `~~cloud storage` | Microsoft 365 | Google Drive, Dropbox |

## MCP Server Configuration

Add to your Claude Desktop settings or `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "slack": {
      "type": "http",
      "url": "https://mcp.slack.com/mcp"
    },
    "intercom": {
      "type": "http",
      "url": "https://mcp.intercom.com/mcp"
    },
    "hubspot": {
      "type": "http",
      "url": "https://mcp.hubspot.com/anthropic"
    },
    "guru": {
      "type": "http",
      "url": "https://mcp.api.getguru.com/mcp"
    },
    "atlassian": {
      "type": "http",
      "url": "https://mcp.atlassian.com/v1/mcp"
    },
    "notion": {
      "type": "http",
      "url": "https://mcp.notion.com/mcp"
    },
    "ms365": {
      "type": "http",
      "url": "https://microsoft365.mcp.claude.com/mcp"
    }
  }
}
```

## Customizing for Your Stack

1. **Identify your tools** for each category above
2. **Find the MCP server URL** for each tool (check the tool's documentation or MCP registry)
3. **Update the configuration** with your specific URLs
4. **Test each connection** before using in production

## Working Without Connectors

This skill works standalone with reduced functionality:
- Provide ticket text directly
- Paste customer context manually
- Research using web search only
- Document responses externally

The skill adapts to available tools automatically.
