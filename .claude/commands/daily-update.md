You are generating a summary of activity and status of a series of channels. Look back $1 days. If $1 is not specified, default to 1.

First, run `scripts/clear_output.sh` to clear temporary files.

If CLAUDE.local.md exists, follow any pre-report cleanup instructions specified there.

1. **Gather project updates**
Iterate over the channels listed in config/daily_channels.txt

**Filtering rules:**
- Ignore ALL bot messages (U00, automated reminders, build notifications, triagebot, etc.)
- Ignore PR review links
- Focus on substantive updates from humans only

**Content guidelines:**
- For threads >3 messages: Summarize key outcome and link to thread start
- For single updates: One sentence with key information
- Include channel links using format: [Channel Name](https://slack-pde.slack.com/archives/CHANNEL_ID)
- Include specific message permalinks for important updates

2. **Executive Summary Structure**
- "Requires Attention" - Issues, blockers, or concerning trends
- "Making Progress" - Positive developments and milestones
- Keep each bullet to one line with reason and channel link

3. **Project Status Categories**
Use consistent status indicators:
- ⚠️ Issues/Blockers
- ✅ On Track
- 🚀 Major Progress
- 📊 Steady Progress
- 💤 No Activity

4. **Calendar**
Look at today's calendar. Add a brief summary of the day.

If CLAUDE.local.md exists, follow any post-report actions specified there.
