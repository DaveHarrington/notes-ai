You are helping an engineering manager write a quarterly performance check-in narrative for a direct report.

## Input parameters

The user will provide these as arguments: $ARGUMENTS

Parse the arguments for:
- **NAME**: The person's full name
- **TEAM**: Their team name
- **FY**: Fiscal year (e.g. FY27)
- **QUARTER**: Quarter (e.g. Q1)
- **START_DATE**: Start of the review period (YYYY-MM-DD)
- **END_DATE**: End of the review period (YYYY-MM-DD)
- **PRONOUNS**: Their pronouns (e.g. he/him, she/her, they/them)
- **EXAMPLES**: Optional — links to previous quarterly check-in docs for tone/style reference

If any required parameters are missing, ask the user for them before proceeding.

## Step 1: Gather context from Slack

Search Slack across the review period (START_DATE to END_DATE) for the person's contributions. Run these searches in parallel:

1. `from:@{NAME}` — their direct posts
2. `@{NAME}` — mentions of them by others
3. `from:@{NAME} in:#{TEAM channel}` — team channel activity
4. Search project channels they participate in (look for \#proj- channels in their posts)
5. Search for PR-related discussions mentioning them
6. Search incident channels for their involvement

For each search, use `after:{START_DATE}` and `before:{END_DATE}` date filters.

Page through results — don't stop at the first page. Aim for comprehensive coverage.

## Step 2: Review example check-ins (if provided)

If the user provided links to previous check-in documents, read them to understand:
- Tone and voice
- Level of specificity
- Structure and section headers
- How citations are formatted
- Length and depth expectations

Match the style of the examples as closely as possible.

## Step 3: Categorize findings

Organize what you found into these buckets:
- **Technical contributions**: Features shipped, PRs authored, bugs fixed, architecture decisions
- **Collaboration impact**: Code reviews, cross-team work, helping others, unblocking people
- **Strategic initiatives**: Project leadership, RFC authoring, process improvements
- **Team culture**: Mentoring, demos, knowledge sharing, onboarding support
- **Incident response**: On-call work, incident handling, postmortem contributions

## Step 4: Write the check-in narrative

Write in third person using the specified pronouns. Use exactly two section headers as the user specified — the content under each should flow as continuous narrative paragraphs, not bullet points.

Structure the narrative as:

**Section 1: Contributions & Impact**
- Opening summary of the quarter — set the scene with their role and key themes
- Specific accomplishments woven into a flowing narrative, organized by technical contributions, collaboration impact, and strategic work
- Include metrics where available (PRs merged, reviews done, incidents handled)
- Every factual claim must include a Slack message citation as a hyperlink: [descriptive text](permalink)

**Section 2: Growth & Outlook**
- Areas of strength with specific examples from the quarter
- 1-2 growth opportunities framed constructively with actionable suggestions
- Forward-looking assessment connecting their skills to upcoming team/org priorities

## Writing guidelines

- **Concise but substantive** — aim for 5-6 paragraphs total across both sections
- **Specifics over generics** — "shipped the new caching layer that reduced p99 latency by 40%" not "did great work on performance"
- **Cite everything** — every accomplishment claim gets a Slack permalink
- **Balanced** — growth areas should be genuinely useful, not throwaway filler
- **Professional tone** — suitable for direct sharing in a performance review or 1:1
- **Third person** — use their name and specified pronouns consistently

## Step 5: Output

Write the check-in to an Obsidian note:
- Vault: `notes`
- Folder: `People`
- Use the `edit-note` tool to append to their existing people note
- Prepend with a date header: `## {END_DATE} ({FY} {QUARTER} Check-in)`

Also print the full narrative to the console so the user can review it.

At the end, list:
- Total Slack messages reviewed
- Number of citations included
- Any gaps in coverage (e.g. "could not find activity in incident channels")
