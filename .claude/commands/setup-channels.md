You are helping the user set up their Slack channel configuration files.

Run the interactive channel setup script:

```bash
python3 setup_channels.py
```

This script will guide the user through configuring each channel list file:
- daily_channels.txt - Critical channels for daily monitoring
- weekly_channels.txt - Channels for weekly summaries
- all_project_channels.txt - All project channels to track
- tracking_channels.txt - Long-term experiments and research
- escalation_channels.txt - Incident and high-priority channels
- announcement_channels.txt - Company and team announcements

The script will:
1. Show descriptions and examples for each channel type
2. Display existing channels if files already exist
3. Allow user to keep, replace, or add to existing lists
4. Accept channels in multiple formats (comma-separated, space-separated, or one per line)
5. Save formatted channel lists to config/ directory

After the script completes, offer to commit the changes if the user wants.
