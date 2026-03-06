#!/usr/bin/env python3
"""
Interactive setup script for channel configuration files.
Prompts the user to populate each channel list with appropriate channels.
"""

import os
from pathlib import Path
from typing import List

CONFIG_DIR = Path(__file__) / "config"

CHANNEL_CONFIGS = {
    "daily_channels.txt": {
        "name": "Daily Channels",
        "description": "Critical channels that require daily monitoring",
        "examples": ["#proj-urgent-feature", "#team-daily-standup", "#incidents-eng"],
        "use_cases": [
            "Critical project channels",
            "Active work streams",
            "Time-sensitive initiatives"
        ]
    },
    "weekly_channels.txt": {
        "name": "Weekly Channels",
        "description": "Channels monitored for weekly summaries",
        "examples": ["#proj-quarterly-planning", "#team-updates", "#working-group-api"],
        "use_cases": [
            "Project status channels",
            "Regular team updates",
            "Ongoing initiatives"
        ]
    },
    "all_project_channels.txt": {
        "name": "All Project Channels",
        "description": "Comprehensive list of all project channels to track",
        "examples": ["#proj-mobile-app", "#proj-api-v2", "#proj-performance"],
        "use_cases": [
            "All active project channels",
            "Cross-functional projects",
            "Team-wide initiatives"
        ]
    },
    "tracking_channels.txt": {
        "name": "Tracking Channels",
        "description": "Long-term tracking channels for experiments and research",
        "examples": ["#exp-new-framework", "#research-ml-ops", "#wg-security"],
        "use_cases": [
            "Experimental projects",
            "Research initiatives",
            "Long-running improvements",
            "Cross-functional working groups"
        ]
    },
    "escalation_channels.txt": {
        "name": "Escalation Channels",
        "description": "High-priority escalation and incident channels",
        "examples": ["#incidents", "#on-call-eng", "#sev1-alerts"],
        "use_cases": [
            "Incident channels",
            "On-call rotations",
            "Critical issue tracking"
        ]
    },
    "announcement_channels.txt": {
        "name": "Announcement Channels",
        "description": "Broadcast and announcement channels",
        "examples": ["#announcements", "#company-news", "#releases"],
        "use_cases": [
            "Company announcements",
            "Team-wide updates",
            "Policy changes",
            "Major releases"
        ]
    }
}


def print_header(text: str):
    """Print a formatted header."""
    print(f"\n{'=' * 70}")
    print(f"  {text}")
    print(f"{'=' * 70}\n")


def print_section(config_info: dict):
    """Print information about a channel configuration."""
    print(f"📋 {config_info['name']}")
    print(f"   {config_info['description']}\n")
    print("   Use cases:")
    for use_case in config_info['use_cases']:
        print(f"   • {use_case}")
    print(f"\n   Examples: {', '.join(config_info['examples'])}\n")


def normalize_channel_name(channel: str) -> str:
    """Normalize a channel name to start with #."""
    channel = channel.strip()
    if not channel:
        return ""
    if not channel.startswith('#'):
        channel = '#' + channel
    return channel


def get_channels_from_user() -> List[str]:
    """
    Prompt user to enter channels.
    Accepts multiple formats: comma-separated, space-separated, or one per line.
    """
    print("   Enter channel names (press Enter twice when done):")
    print("   You can enter multiple channels separated by commas, spaces, or one per line")
    print("   Channels can be entered with or without the # prefix\n")

    channels = []
    while True:
        try:
            line = input("   > ").strip()
            if not line:
                if channels:  # Empty line after entering some channels
                    break
                continue

            # Handle comma or space separated
            if ',' in line or ' ' in line:
                separators = [',', ' ']
                parts = [line]
                for sep in separators:
                    parts = [p for part in parts for p in part.split(sep)]
                for part in parts:
                    normalized = normalize_channel_name(part)
                    if normalized and normalized not in channels:
                        channels.append(normalized)
            else:
                normalized = normalize_channel_name(line)
                if normalized and normalized not in channels:
                    channels.append(normalized)

        except EOFError:
            break

    return channels


def show_current_channels(filename: str) -> List[str]:
    """Show current channels in a file if it exists."""
    filepath = CONFIG_DIR / filename
    if filepath.exists():
        with open(filepath, 'r') as f:
            existing = [line.strip() for line in f if line.strip() and not line.startswith('##')]
        if existing:
            print(f"   Current channels in {filename}:")
            for channel in existing:
                print(f"     • {channel}")
            return existing
    return []


def write_channels(filename: str, channels: List[str]):
    """Write channels to a configuration file."""
    filepath = CONFIG_DIR / filename
    CONFIG_DIR.mkdir(exist_ok=True)

    with open(filepath, 'w') as f:
        f.write(f"## {CHANNEL_CONFIGS[filename]['name']}\n")
        f.write(f"## {CHANNEL_CONFIGS[filename]['description']}\n")
        f.write(f"##\n")
        for channel in sorted(channels):
            f.write(f"{channel}\n")

    print(f"   ✓ Wrote {len(channels)} channels to {filename}\n")


def main():
    print_header("Channel Configuration Setup")
    print("This script will help you configure channel lists for daily updates,")
    print("weekly summaries, and other monitoring needs.\n")

    for filename, config_info in CHANNEL_CONFIGS.items():
        print_section(config_info)

        # Show existing channels if any
        existing = show_current_channels(filename)

        if existing:
            keep = input("   Keep existing channels? (y/n/add): ").strip().lower()
            if keep == 'y':
                print(f"   ✓ Keeping existing channels in {filename}\n")
                continue
            elif keep == 'add':
                print("   Add more channels to the existing list:\n")
                new_channels = get_channels_from_user()
                if new_channels:
                    all_channels = list(set(existing + new_channels))
                    write_channels(filename, all_channels)
                else:
                    print(f"   ✓ No changes to {filename}\n")
                continue
            # If 'n', continue to replace

        channels = get_channels_from_user()

        if channels:
            write_channels(filename, channels)
        else:
            print(f"   ⊘ Skipping {filename} (no channels entered)\n")

        print("-" * 70)

    print_header("Setup Complete!")
    print("Your channel configurations have been saved to the config/ directory.")
    print("\nNext steps:")
    print("  • Review the files in config/ to verify")
    print("  • Commit your changes: git add config/ && git commit -m 'Configure channels'")
    print("  • Test with: python3 scripts/process_daily_batch.py\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSetup cancelled by user.")
        exit(0)
