# Connectors Configuration

## How Tool References Work

This skill uses `~~category` placeholders for tool-agnostic workflows. Replace with your specific tools.

## Available Connectors

| Category | Placeholder | Recommended | Alternatives |
|----------|-------------|-------------|--------------|
| Chat | `~~chat` | Slack | Microsoft Teams |
| Email | `~~email` | Microsoft 365 | Gmail |
| Calendar | `~~calendar` | Microsoft 365 | Google Calendar |
| Project tracker | `~~project tracker` | Asana | Linear, Jira, Monday, ClickUp, Notion |
| Documents | `~~documents` | Notion | Google Drive, Confluence |

## MCP Server Configuration

Add to your Claude Desktop settings or `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "slack": {
      "type": "http",
      "url": "https://mcp.slack.com/mcp"
    },
    "asana": {
      "type": "http",
      "url": "https://mcp.asana.com/mcp"
    },
    "linear": {
      "type": "http",
      "url": "https://mcp.linear.app/mcp"
    },
    "notion": {
      "type": "http",
      "url": "https://mcp.notion.com/mcp"
    },
    "ms365": {
      "type": "http",
      "url": "https://microsoft365.mcp.claude.com/mcp"
    },
    "atlassian": {
      "type": "http",
      "url": "https://mcp.atlassian.com/v1/mcp"
    }
  }
}
```

## Working Without Connectors

This skill works fully offline with local files:
- `TASKS.md` for task tracking
- `CLAUDE.md` and `memory/` for context
- `dashboard.html` for visual management

External tools enhance but aren't required.
