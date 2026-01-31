---
name: productivity
description: Complete productivity skill for task management, memory/context building, and daily workflow optimization. Use when managing tasks, tracking commitments, building workplace memory (people, projects, acronyms), planning your day, syncing with external tools, or when you need Claude to understand your workplace shorthand. Trigger phrases include "what's on my plate", "add a task", "remember this", "who is [name]", "what does [acronym] mean", "start my productivity system", "update my tasks".
---

# Productivity Skill

Transform Claude into your workplace collaborator who speaks your internal language, tracks your commitments, and keeps you organized.

## Core Capabilities

- **Task Management**: Track tasks in a simple TASKS.md file with visual dashboard
- **Memory System**: Two-tier memory that decodes workplace shorthand (people, projects, acronyms)
- **Daily Workflows**: Initialize and update your productivity system
- **External Sync**: Connect with calendars, task trackers, chat, and email

## Quick Commands

| Command | Usage | Description |
|---------|-------|-------------|
| `/start` | `/start` | Initialize the productivity system |
| `/update` | `/update [--comprehensive]` | Sync tasks and refresh memory |

---

## Task Management

### File Location

Tasks are tracked in `TASKS.md` in the current working directory.

### Format

```markdown
# Tasks

## Active
- [ ] **Task title** - context, for whom, due date
  - Sub-bullets for details

## Waiting On
- [ ] **Waiting item** - who, since when

## Someday
- [ ] **Future task** - context

## Done
- [x] ~~Completed task~~ (date)
```

### Task Interactions

**"What's on my plate" / "My tasks":**
- Read TASKS.md
- Summarize Active and Waiting On
- Highlight overdue/urgent items

**"Add a task" / "Remind me to":**
- Add to Active with `- [ ] **Task**` format
- Include context (who, due date)

**"Done with X" / "Finished X":**
- Change `[ ]` to `[x]`
- Add strikethrough and date
- Move to Done section

**"What am I waiting on":**
- Read Waiting On section
- Note duration of each wait

### Extracting Tasks

When summarizing meetings or conversations, offer to add:
- Commitments made ("I'll send that over")
- Action items assigned
- Follow-ups mentioned

Always ask before adding.

### Visual Dashboard

A `dashboard.html` file provides a visual task manager:
- Drag-and-drop task reordering
- Auto-saves changes
- Syncs with TASKS.md in real-time

---

## Memory System

### The Goal

Transform shorthand into understanding:

```
User: "ask todd to do the PSR for oracle"
              ↓ Claude decodes
"Ask Todd Martinez (Finance lead) to prepare the Pipeline Status Report
 for the Oracle Systems deal ($2.3M, closing Q2)"
```

### Architecture

```
CLAUDE.md          ← Hot cache (~30 people, common terms)
memory/
  glossary.md      ← Full decoder ring (everything)
  people/          ← Complete profiles
  projects/        ← Project details
  context/         ← Company, teams, tools
```

### Working Memory (CLAUDE.md)

Target ~50-80 lines. Covers 90% of daily decoding.

```markdown
# Memory

## Me
[Name], [Role] on [Team].

## People
| Who | Role |
|-----|------|
| **Todd** | Todd Martinez, Finance lead |
| **Sarah** | Sarah Chen, Engineering (Platform) |
→ Full list: memory/glossary.md

## Terms
| Term | Meaning |
|------|---------|
| PSR | Pipeline Status Report |
| P0 | Drop everything priority |
→ Full glossary: memory/glossary.md

## Projects
| Name | What |
|------|------|
| **Phoenix** | DB migration, Q2 launch |
→ Details: memory/projects/

## Preferences
- 25-min meetings with buffers
- Async-first, Slack over email
```

### Deep Memory (memory/)

**glossary.md** - Complete decoder ring:
- All acronyms and terms
- All nicknames → full names
- All project codenames

**people/{name}.md** - Individual profiles:
- Also known as (nicknames)
- Role, team, reports to
- Communication preferences
- Context and notes

**projects/{name}.md** - Project details:
- Codename and aliases
- Status, key people
- Context and timeline

**context/company.md** - Company context:
- Tools and systems
- Team structure
- Processes

### Lookup Flow

```
1. Check CLAUDE.md (hot cache)
   → Found? Use it.

2. Search memory/glossary.md
   → Found? Use it.

3. Search memory/people/, projects/
   → Found? Use detailed info.

4. Ask user
   → "What does X mean? I'll remember it."
```

### Adding Memory

**When user says "remember this" or "X means Y":**

1. Glossary items → memory/glossary.md (+ CLAUDE.md if frequent)
2. People → memory/people/{name}.md (+ CLAUDE.md if important)
3. Projects → memory/projects/{name}.md (+ CLAUDE.md if active)
4. Preferences → CLAUDE.md Preferences section

### Promotion/Demotion

**Promote to CLAUDE.md:**
- Frequently used terms/people
- Part of active work

**Demote to memory/ only:**
- Project completed
- Person no longer frequent contact
- Term rarely used

---

## Commands

### /start — Initialize System

1. **Check existing files**: TASKS.md, CLAUDE.md, memory/, dashboard.html
2. **Create missing files** with templates
3. **Open dashboard**: Tell user "Dashboard ready at dashboard.html"
4. **Bootstrap memory** (first run):
   - Ask for task list source
   - Analyze tasks for shorthand
   - Decode interactively (names, acronyms, projects)
   - Write memory files

**Bootstrap Questions:**
```
Task: "Send PSR to Todd re: Phoenix blockers"

I see some terms I want to understand:
1. **PSR** - What does this stand for?
2. **Todd** - Who is Todd? (full name, role)
3. **Phoenix** - Is this a project codename?
```

### /update — Sync and Refresh

**Default mode:**
1. Load TASKS.md and memory/
2. Sync from external sources (~~project tracker, GitHub)
3. Compare and offer to add new tasks
4. Triage stale items (30+ days, past due dates)
5. Decode tasks for memory gaps
6. Fill gaps interactively

**--comprehensive mode:**
All of the above, plus:
- Deep scan of ~~chat, ~~email, ~~calendar
- Flag missed todos from activity
- Suggest new memories (people, projects)
- Offer cleanup (stale projects, inactive people)

**Output:**
```
Update complete:
- Tasks: +3 from Asana, 1 completed, 2 triaged
- Memory: 2 gaps filled, 1 project enriched
- All tasks decoded ✓
```

---

## Tool Connections

| Category | Placeholder | Examples |
|----------|-------------|----------|
| Chat | `~~chat` | Slack, Microsoft Teams |
| Email | `~~email` | Microsoft 365, Gmail |
| Calendar | `~~calendar` | Microsoft 365, Google Calendar |
| Project tracker | `~~project tracker` | Asana, Linear, Jira, Monday, ClickUp |
| Documents | `~~documents` | Notion, Google Drive |

See `references/connectors.md` for MCP configuration.

## Working Without Connectors

This skill works fully offline:
- Tasks in local TASKS.md
- Memory in local files
- Dashboard as local HTML
- Manual input for external context

External tools enhance but aren't required.
