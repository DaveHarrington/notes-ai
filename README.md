# Notes AI

Claude Code + Slack MCP == Manager Magic

## Overview

This tool helps engineering managers and team leads stay on top of information across numerous Slack channels by:
- Generating daily and weekly activity summaries
- Tracking project status updates across multiple channels
- Identifying issues and blockers from channel conversations
- Creating structured reports from unstructured Slack discussions

## Prerequisites

- Access to Slack MCP (Model Context Protocol) server
- Claude Code or similar AI assistant with MCP support
- (Optional) macOS with Apple Calendar for calendar integration
- (Optional) Obsidian

## Setup

`claude`

`/setup-channels`

## Usage

Ask Claude Code to generate summaries using natural language. Examples:

### Daily Update
Run first thing daily to get a personalised report:

```bash
claude /daily-updates
```

### Weekly Updates
Run once weekly for a more extensive report across Slack:

```bash
claude /weekly-updates
```

## Customization

### Personal Configuration (CLAUDE.local.md)

Create a `CLAUDE.local.md` file for personal preferences:

```bash
cp CLAUDE.local.md.example CLAUDE.local.md
# Edit CLAUDE.local.md with your preferences
```

Use this file to specify:
- Pre-report actions
- Post-report actions (e.g., copying reports to your notes directory)
