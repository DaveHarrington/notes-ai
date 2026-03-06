You are generating a report identifying DEVXP project channels that need more attention based on activity over the past 30 days.

**⚠️ ACCURACY OVER SPEED ⚠️**
This analysis must be thorough and accurate. Do NOT prioritize speed over correctness. Follow the mandatory 3-step fallback process for EVERY channel that shows no initial results.

## Analysis Requirements

Get the best practices for project channels from Canvas with ID: F09S9GKNRLJ

**CRITICAL: Accuracy Over Speed**
- Do NOT batch process channels and move on
- For EACH channel, follow the complete 3-step fallback process from CLAUDE.md
- Verify results before marking any channel as "No Activity"

For each channel in DEVXP_PROJECTS, analyze the past 14 days for adherence to the best practices, e.g.:

1. **Weekly Status Updates**
   - Look for regular posts (ideally weekly) describing:
     - Project goals
     - Current status
     - Future plans / next steps
   - These may appear as thread summaries, status posts, or updates

2. **Action Items & Engagement**
   - Meeting notes or discussion summaries
   - Ideas, proposals, or technical discussions
   - Links to PRs with context/discussion (not just bot notifications)
   - Problem-solving conversations
   - Decision-making threads


**Filtering rules:**
- Ignore ALL bot messages (automated reminders, build notifications, triagebot)

## MANDATORY: 3-Step Fallback Process for Each Channel

For **EVERY** channel in DEVXP_PROJECTS, you MUST follow this process:

### Step 1: MCP Search with Timeframe
- Search using Slack MCP tools with `after:2025-11-08` (30 days ago)
- If you get results → Analyze them
- If you get NO results → Proceed to Step 2

### Step 2: MCP Search WITHOUT Timeframe
- Search the same channel using MCP WITHOUT date filters
- This checks if the channel exists and is accessible
- If you get results → Channel exists but had "No Activity" in timeframe
- If you get NO results → Proceed to Step 3

**ONLY** mark a channel as "No Activity" after completing both steps.

## Evaluation Criteria

A channel **needs more attention** if it shows:
- ❌ No weekly status updates in the past month
- ❌ No regular updates describing goals/status/plans
- ❌ Minimal action items (< 3 substantive discussions/notes in 30 days)
- ❌ Only reactive posts without forward planning
- ⚠️ Irregular updates (gaps > 2 weeks between status posts)

A channel is **healthy** if it has:
- ✅ Regular status updates (weekly or bi-weekly)
- ✅ Clear articulation of goals, status, and plans
- ✅ Active engagement (meeting notes, discussions, ideas)
- ✅ Mix of status updates and action items

## Output Format

Write a brief report to `output/project_report.md` with:

### Projects Requiring More Attention

For each channel needing attention:
- **\#channel-name** - Brief reason (e.g., "No status updates in 30 days, minimal discussion" or "Irregular updates, no clear goals stated")

### Summary
- Total channels analyzed: X
- Channels needing attention: Y
- Common patterns observed

### Data Quality Notes

Document any issues found during analysis:
- Channel name discrepancies between DEVXP_PROJECTS and actual channel names
- Channels found in different workspaces (salesforce-internal vs slack-pde)
- Any search errors or access issues

Keep the main report concise - just list channels and brief reasons. The goal is a quick actionable report with complete accuracy.
