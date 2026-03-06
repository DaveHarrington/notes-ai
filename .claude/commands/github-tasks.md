You are generating a summary of the user's current open tasks on GitHub.

**User Information:**
- GitHub Username: dharrington (infer from git config if needed)

## Process

### 1. Gather Open PRs Authored by User
```bash
gh search prs --author=@me --state=open --json number,title,repository,url,updatedAt,createdAt,isDraft --limit 50
```

### 2. Gather PRs Awaiting User's Review (personal requests only)
Use `user-review-requested:@me` to get only PRs where the user was individually asked to review (excludes team-based review requests):
```bash
gh search prs --state=open "user-review-requested:@me" --json number,title,repository,url,updatedAt,createdAt,author --limit 50
```

### 3. Gather Open Issues Assigned to User
```bash
gh search issues --assignee=@me --state=open --json number,title,repository,url,updatedAt,createdAt,labels --limit 50
```

### 4. Format Output

Present the results grouped into three sections. Within each section, sort by most recently updated first.

**Format:**

```
# Open GitHub Tasks

## My Open PRs
| Repo | PR | Title | Updated | Draft |
|------|-----|-------|---------|-------|
| repo-name | [#number](url) | title | relative date | Yes/No |

## Reviews Requested
| Repo | PR | Title | Author | Updated |
|------|-----|-------|--------|---------|
| repo-name | [#number](url) | title | author | relative date |

## Assigned Issues
| Repo | Issue | Title | Labels | Updated |
|------|-------|-------|--------|---------|
| repo-name | [#number](url) | title | labels | relative date |
```

**Guidelines:**
- Use relative dates (e.g., "today", "yesterday", "3 days ago", "2 weeks ago")
- If a section has no items, show "None" instead of an empty table
- For draft PRs, include a "Draft" indicator
- Show the repo short name (not the full owner/name), e.g. `docs` not `slack/docs`
- Add a count summary at the top: "X open PRs, Y reviews requested, Z assigned issues"
