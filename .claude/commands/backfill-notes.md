You are backfilling the user's daily notes with activity from the past work week.

**User Information:**
- Slack User ID: U03SC51Q3HV
- GitHub Username: dharrington (infer from git config if needed)

## Process

For each business day in the past 5 days (Mon-Fri):

### 1. Gather Slack Activity
Search Slack for messages FROM the user on that specific day:
- Use `slack_search_public` with query: `from:<@U03SC51Q3HV> on:YYYY-MM-DD`
- Focus on substantive messages (ignore simple reactions, "thanks", etc.)
- Look for:
  - Updates posted to project channels
  - Decisions or action items
  - Important discussions or threads (>3 messages)
- Identify meetings from channel names (e.g., messages in meeting-specific channels or calendar-related discussions)

### 2. Gather GitHub Activity
Use bash to search GitHub for the user's activity on that day (works globally, not repo-specific):
```bash
# Get PRs created or updated - this searches across ALL repositories
gh search prs --author=@me --updated=YYYY-MM-DD --json number,title,repository,url,updatedAt --limit 20

# Get issues commented on - this searches across ALL repositories
gh search issues --commenter=@me --updated=YYYY-MM-DD --json number,title,repository,url,updatedAt --limit 20
```

**Format GitHub items for Log section:**
- For PRs: `- [x] Created/Updated [repo PR #number](url) - title`
- For issues: `- [x] Commented on [repo issue #number](url) - title`
- Examples:
  - `- [x] Created [docs-bolt-app PR #8](https://github.com/blah) - Productionize app`

### 3. Update Daily Note
For each day, update `~/Notes/Daily/YYYY-MM-DD.md`:

**Add to Log section:**
- Prefix with `- [x]` for tasks/actions (mark as done since they happened in the past)
- Format: `[action/topic] - [brief context or link]`
- Examples:
  - `- [x] Updated \#proj-ai-test-selection with bug fix status`
  - `- [x] Reviewed PR for authentication refactor [link]`
  - `- [x] Committed changes to feature-branch`

**Add to Meetings section:**
- List meeting names or topics
- Use wiki-style links if it's a recurring meeting: `[[Meeting Name]]`
- Examples:
  - `- [[Engineering Managers Sync]]`
  - `- 1:1 with Jamie`
  - `- Design review for new feature`

**Guidelines:**
- Only add substantive items (skip routine messages)
- Keep items concise (one line each)
- Preserve existing content in the file
- If the daily note doesn't exist, create it with the standard template:
```markdown
# Tasks

## Daily
- [ ] Review [calendar](https://calendar.google.com/calendar/u/0/r)
- [ ] Read Recap
- [ ] Review [Slack Later](https://app.slack.com/client/E7T5PNK3P/later)
- [ ] Review [[TODO]]

## Log

# Meetings

# Notes
```

### 4. Summary Output
After processing all 5 days, provide a summary showing:
- Total items added to each day
- Any notable patterns or themes
- Which days had the most activity

**Important:**
- Skip weekends (Sat/Sun)
- If a daily note already exists, append to existing sections (don't overwrite)
- Use the Edit tool to update existing files
- Maintain the markdown formatting and task syntax
- Include actual Slack permalinks and GitHub URLs when available
