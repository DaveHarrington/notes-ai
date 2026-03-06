You are generating a summary of activity and status of a set of slack channels for the past 7 days.
You will create intermediate summaries, and then compile them into a concise newsletter.
Configuration is in files in `config/`
First, run `scripts/clear_output.sh` to clear temporary files.

If CLAUDE.local.md exists, follow any pre-report cleanup instructions specified there.

## 1. Project Updates (config/daily_channels.txt + all_project_channels.txt + weekly_channels.txt)

**Filtering rules:**
- Filter out posts from bots, PR reviews, automated reminders etc
- Skip projects marked "Not Started" or "Postponed"
- Focus on substantive human updates and decisions

**Status Classification:**
- 🔴 Issues/Blockers: Failed deployments, blocked work, escalated problems, missed deadlines
- 🟡 At Risk: Delays, resource constraints, dependencies, concerns raised
- 🟢 On Track: Meeting milestones, positive progress, successful deployments

**Content Guidelines:**
- Include brief summary and link for status update posts
- For threads >5 messages: Summarize key outcome and decisions
- Note if no status update was posted this week
- Order by: Red, Yellow, Green

Write to `output/project_updates.md`

## 2. Executive Summary
Analyze `output/project_updates.md` and create:
- **Critical Issues** - Projects needing immediate attention
- **Weekly Highlights** - Major achievements and milestones
- **Trends** - Patterns across multiple projects
- Link each point to relevant posts/channels

Write to `output/executive_summary.md`

## 3. Announcement Updates (config/announcement_channels.txt)
- One-line summary per significant post with permalink
- Group by channel, most recent first
- Skip routine notifications and bot posts

Append to `output/announce_updates.md`

## 4. Tracking Projects (config/tracking_channels.txt - Comprehensive Coverage)
**CRITICAL: Iterate over ALL channels in tracking_channels.txt**
- Use a sub-agent in a loop to ensure every channel is checked
- Make a one-line summary of activity in the channel if noteworthy human activity occurred
- Filter out posts from bots, PR reviews, automated reminders etc
- Skip channels with only bot activity or no posts

Append the update to `output/tracking_projects_{batch}.md` after each summary

## 5. Escalation Summary (config/escalation_channels.txt)
Create themed summary:
- **Total escalations** this week vs last week
- **Top themes** (tooling, access, performance, etc.)
- **Recurring issues** mentioned multiple times
- **Resolution patterns** - what got resolved quickly vs slowly

Write to `output/escal_summary.md`

## 6. Weekly Calendar Outlook
Look at my calendar for the rest of the week. Identify any key meetings, and add a summary of the week's outlook.

## 7. Final Weekly Report

Combine these sections into `output/weekly_updates.md`:
1. Executive Summary
2. Calendar Outlook
3. Project Updates (Red/Yellow/Green sections)
4. Weekly Highlights from Announcements
6. Escalation Themes and Trends

Then copy _all_ Tracking Project updates from output/tracking_projects_{batch}.md to `output/weekly_updates.md`

If CLAUDE.local.md exists, follow any post-report actions specified there.
