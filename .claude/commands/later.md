You are reviewing the user's Slack "Later" (saved) posts and processing them into a tracking CSV and Obsidian tasks.

## Step 1: Search Slack for saved posts

Search Slack for `is:saved` posts. Limit to the past 3 days.

## Step 2: Load the processed record

Read the CSV file at `/Users/daveharrington/dev/notes-ai/data/later_processed.csv`.
This file tracks all previously processed Later items to avoid duplicates.
The columns are: `post_id,date_processed,summary,due_date,permalink`

The `post_id` is the message timestamp (ts) from Slack. Use this to deduplicate — skip any posts whose ts already appears in the CSV.

## Step 3: Review each NEW (unprocessed) post

For each new post:
1. Write a **one-line summary** (max ~80 chars) of what the post is about
2. Determine if the post mentions or implies a **due date** (e.g. "by Friday", "due March 5", "EOD tomorrow", "deadline is next week"). Convert to YYYY-MM-DD format. If no due date, leave blank.
3. Record the post's permalink URL

## Step 4: Append to CSV

Append one row per new post to `/Users/daveharrington/dev/notes-ai/data/later_processed.csv`:
```
post_id,date_processed,summary,due_date,permalink
```
- `post_id`: the Slack message `ts` value
- `date_processed`: today's date in YYYY-MM-DD
- `summary`: the one-line summary
- `due_date`: YYYY-MM-DD or empty
- `permalink`: the Slack permalink URL

Use a python script in /scripts/ to append to the CSV safely (proper quoting, etc).

## Step 5: Add tasks to Obsidian for posts with due dates

For each new post that HAS a due date, add a task to **today's daily note** in the `## Inbox` section.

Use the Obsidian MCP `edit-note` tool to append to today's daily note (vault: `notes`, folder: `Daily`, filename: `{today's date YYYY-MM-DD}.md`).

The task format is:
```
- [ ] Summary [link](permalink) 📅 YYYY-MM-DD
```

Where:
- Summary is the one-line summary
- `[link](permalink)` links to the Slack message
- `📅 YYYY-MM-DD` is the Obsidian Tasks plugin due date

If today's daily note doesn't exist yet, create it with the standard template first (copy structure from the most recent daily note).

**IMPORTANT**: Only append new tasks under `## Inbox`. Do not modify any other section.

To append under `## Inbox` specifically: read the current note content, find the `## Inbox` line, and insert the new tasks after any existing inbox items but before the next `##` section. Use the Edit tool on the file at `/Users/daveharrington/Notes/Daily/{date}.md` to do this precisely.

## Step 6: Print summary

Print a summary table of all reviewed posts:
```
| Status | Summary | Due Date |
|--------|---------|----------|
| ✅ New (task added) | Summary here | 2026-03-01 |
| ✅ New | Summary here | — |
| ⏭️ Already processed | Summary here | — |
```

Include counts at the end:
- Total saved posts found
- Already processed (skipped)
- New posts recorded
- Tasks added to Obsidian
