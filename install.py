#!/usr/bin/env python3
"""
MCP Installation Script

Interactive installer for Obsidian MCP, Obsidian Tasks MCP, and Calendar MCP servers.
"""

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


def check_command(command: str) -> bool:
    """Check if a command is available in PATH."""
    return shutil.which(command) is not None


def run_command(cmd: list, cwd: str = None, check: bool = True) -> subprocess.CompletedProcess:
    """Run a shell command."""
    return subprocess.run(cmd, cwd=cwd, check=check, capture_output=True, text=True)


def prompt_yes_no(message: str, default: bool = False) -> bool:
    """Prompt for yes/no answer."""
    suffix = " (Y/n): " if default else " (y/N): "
    while True:
        response = input(message + suffix).strip().lower()
        if not response:
            return default
        if response in ('y', 'yes'):
            return True
        if response in ('n', 'no'):
            return False
        print("Please enter 'y' or 'n'")


def prompt_with_default(message: str, default: str = None) -> str:
    """Prompt for input with optional default value."""
    if default:
        prompt = f"{message} [{default}]: "
    else:
        prompt = f"{message}: "

    response = input(prompt).strip()
    return response if response else (default or "")


def load_existing_settings(project_root: Path) -> tuple:
    """Load existing vault path and calendar name from settings."""
    settings_file = project_root / ".claude" / "settings.local.json"

    if not settings_file.exists():
        return "", ""

    try:
        with open(settings_file, 'r') as f:
            settings = json.load(f)

        env = settings.get('env', {})
        vault_path = env.get('OBSIDIAN_VAULT_PATH', '')
        calendar_name = env.get('CALENDAR_NAME', '')
        return vault_path, calendar_name
    except Exception:
        return "", ""


def save_to_settings(project_root: Path, key: str, value: str):
    """Save a value to .claude/settings.local.json."""
    settings_file = project_root / ".claude" / "settings.local.json"
    settings_file.parent.mkdir(parents=True, exist_ok=True)

    # Read existing settings
    if settings_file.exists():
        with open(settings_file, 'r') as f:
            settings = json.load(f)
    else:
        settings = {}

    # Ensure env object exists
    if 'env' not in settings:
        settings['env'] = {}

    # Set the value
    settings['env'][key] = value

    # Write back
    with open(settings_file, 'w') as f:
        json.dump(settings, f, indent=2)
        f.write('\n')


def install_obsidian_mcp(project_root: Path) -> bool:
    """Install Obsidian MCP."""
    print("\n=== Installing Obsidian MCP ===\n")

    # Check if bun is installed
    if not check_command('bun'):
        print("Obsidian MCP requires Bun to build.")
        print()
        if prompt_yes_no("Do you want to install Bun now?"):
            print("Installing Bun...")
            subprocess.run("curl -fsSL https://bun.sh/install | bash", shell=True, check=True)

            # Add bun to PATH for current session
            bun_install = Path.home() / ".bun"
            os.environ['BUN_INSTALL'] = str(bun_install)
            os.environ['PATH'] = f"{bun_install / 'bin'}:{os.environ['PATH']}"

            print("  ✓ Bun installed")
        else:
            print("Skipping Obsidian MCP installation (requires Bun)")
            print("To install Bun manually, run: curl -fsSL https://bun.sh/install | bash")
            return False

    # Initialize submodule
    print("Step 1: Initializing obsidian-mcp submodule...")
    run_command(['git', 'submodule', 'update', '--init', 'obsidian-mcp'], cwd=project_root)
    print("  ✓ Submodule initialized")

    # Install dependencies
    print("\nStep 2: Installing dependencies...")
    obsidian_mcp_dir = project_root / "obsidian-mcp"
    run_command(['npm', 'install'], cwd=obsidian_mcp_dir)
    print("  ✓ Dependencies installed")

    # Build
    print("\nStep 3: Building obsidian-mcp...")
    run_command(['npm', 'run', 'build'], cwd=obsidian_mcp_dir)
    print("  ✓ Build complete")

    print("  ✓ Obsidian MCP installed successfully")
    return True


def install_obsidian_tasks_mcp() -> bool:
    """Install Obsidian Tasks MCP."""
    print("\n=== Installing Obsidian Tasks MCP ===")
    print("This will use the npm package via npx (no build required)")
    print()
    print("  ✓ Obsidian Tasks MCP will be configured to use npx")
    return True


def configure_obsidian_vault(project_root: Path, existing_vault_path: str) -> str:
    """Configure Obsidian vault path."""
    print("\n=== Configure Obsidian Vault Path ===\n")

    if existing_vault_path:
        vault_path = prompt_with_default(
            "Enter the path to your Obsidian vault",
            existing_vault_path
        )
    else:
        vault_path = prompt_with_default(
            "Enter the path to your Obsidian vault (e.g., /Users/username/Documents/MyVault)"
        )

    if not vault_path:
        print("Error: Vault path cannot be empty")
        sys.exit(1)

    # Expand ~ to home directory
    vault_path = os.path.expanduser(vault_path)

    # Check if directory exists
    if not Path(vault_path).is_dir():
        print(f"Warning: Directory '{vault_path}' does not exist")
        if not prompt_yes_no("Do you want to continue anyway?"):
            print("Installation cancelled")
            sys.exit(1)

    print(f"  ✓ Vault path set to: {vault_path}")

    # Save to settings
    save_to_settings(project_root, 'OBSIDIAN_VAULT_PATH', vault_path)
    print("  ✓ Vault path saved to .claude/settings.local.json")

    return vault_path


def install_calendar_mcp(project_root: Path, existing_calendar_name: str) -> bool:
    """Install Calendar MCP."""
    print("\n=== Installing Calendar MCP ===\n")

    # Check if Homebrew is installed
    if not check_command('brew'):
        print("Error: Homebrew is not installed. Please install Homebrew first:")
        print('  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
        sys.exit(1)

    # Install ical-buddy
    print("Step 1: Installing ical-buddy...")
    if check_command('icalBuddy'):
        print("  ✓ ical-buddy is already installed")
    else:
        print("  Installing ical-buddy via Homebrew...")
        run_command(['brew', 'install', 'ical-buddy'])
        print("  ✓ ical-buddy installed successfully")

    # Initialize submodule
    print("\nStep 2: Initializing calendar-mcp submodule...")
    run_command(['git', 'submodule', 'update', '--init', 'calendar-mcp'], cwd=project_root)
    print("  ✓ Submodule initialized")

    # Install dependencies
    print("\nStep 3: Installing npm dependencies...")
    calendar_mcp_dir = project_root / "calendar-mcp"
    run_command(['npm', 'install'], cwd=calendar_mcp_dir)
    print("  ✓ Dependencies installed")

    # Build
    print("\nStep 4: Building calendar MCP...")
    run_command(['npm', 'run', 'build'], cwd=calendar_mcp_dir)
    print("  ✓ Build complete")

    # Configure calendar name
    print("\nStep 5: Configure calendar name")
    print()
    print("To find your calendar name, run: icalBuddy calendars")
    print("Note: This is usually your Salesforce email address")
    print()

    if existing_calendar_name:
        calendar_name = prompt_with_default(
            "Enter your calendar name",
            existing_calendar_name
        )
    else:
        calendar_name = prompt_with_default(
            "Enter your calendar name (e.g., janesmith@salesforce.com)"
        )

    if not calendar_name:
        print("Error: Calendar name cannot be empty")
        sys.exit(1)

    # Save to settings
    save_to_settings(project_root, 'CALENDAR_NAME', calendar_name)
    print("  ✓ Calendar name saved to .claude/settings.local.json")

    print("  ✓ Calendar MCP installed successfully")
    return True


def update_mcp_json(project_root: Path, installed_mcps: list, vault_path: str):
    """Update .mcp.json configuration."""
    print("\n=== Updating .mcp.json configuration ===\n")

    mcp_file = project_root / ".mcp.json"

    # Read existing config
    if mcp_file.exists():
        with open(mcp_file, 'r') as f:
            config = json.load(f)
    else:
        config = {'mcpServers': {}}

    # Ensure mcpServers exists
    if 'mcpServers' not in config:
        config['mcpServers'] = {}

    # Add configured MCPs
    if 'obsidian' in installed_mcps:
        config['mcpServers']['obsidian'] = {
            'type': 'stdio',
            'command': 'node',
            'args': [
                str(project_root / 'obsidian-mcp' / 'build' / 'main.js'),
                '$OBSIDIAN_VAULT_PATH'
            ]
        }

    if 'obsidian-tasks' in installed_mcps:
        config['mcpServers']['obsidian-tasks'] = {
            'type': 'stdio',
            'command': 'npx',
            'args': [
                '@jfim/obsidian-tasks-mcp',
                '$OBSIDIAN_VAULT_PATH'
            ]
        }

    if 'calendar' in installed_mcps:
        config['mcpServers']['calendar'] = {
            'type': 'stdio',
            'command': 'node',
            'args': [
                str(project_root / 'calendar-mcp' / 'dist' / 'index.js')
            ]
        }

    # Write config
    with open(mcp_file, 'w') as f:
        json.dump(config, f, indent=2)
        f.write('\n')

    print(f"  ✓ Updated {mcp_file}")


def update_settings_enabled_mcps(project_root: Path, installed_mcps: list):
    """Update enabledMcpjsonServers in .claude/settings.local.json."""
    print("\n=== Updating .claude/settings.local.json ===\n")

    settings_file = project_root / ".claude" / "settings.local.json"

    # Read existing settings
    if settings_file.exists():
        with open(settings_file, 'r') as f:
            settings = json.load(f)
    else:
        settings = {}

    # Ensure enabledMcpjsonServers exists
    if 'enabledMcpjsonServers' not in settings:
        settings['enabledMcpjsonServers'] = []

    # Add MCPs to enabled list (avoiding duplicates)
    for mcp in installed_mcps:
        if mcp not in settings['enabledMcpjsonServers']:
            settings['enabledMcpjsonServers'].append(mcp)

    # Write back
    settings_file.parent.mkdir(parents=True, exist_ok=True)
    with open(settings_file, 'w') as f:
        json.dump(settings, f, indent=2)
        f.write('\n')

    print(f"  ✓ Updated {settings_file}")
    print(f"  ✓ Enabled MCPs: {', '.join(settings['enabledMcpjsonServers'])}")


def main():
    """Main installation flow."""
    print("=== MCP Installation Script ===\n")

    # Get project root
    project_root = Path(__file__).parent.resolve()

    # Check prerequisites
    if not check_command('node'):
        print("Error: Node.js is not installed. Please install Node.js first:")
        print("  brew install node")
        sys.exit(1)

    if not check_command('npm'):
        print("Error: npm is not installed. Please install Node.js (which includes npm):")
        print("  brew install node")
        sys.exit(1)

    # Load existing settings
    existing_vault_path, existing_calendar_name = load_existing_settings(project_root)

    # Track which MCPs were installed
    installed_mcps = []
    vault_path = ""

    # Obsidian MCP
    if prompt_yes_no("\nDo you want to install Obsidian MCP?"):
        if install_obsidian_mcp(project_root):
            installed_mcps.append('obsidian')

    # Obsidian Tasks MCP
    if prompt_yes_no("\nDo you want to install Obsidian Tasks MCP?"):
        if install_obsidian_tasks_mcp():
            installed_mcps.append('obsidian-tasks')

    # Configure Obsidian vault path if any Obsidian MCP was installed
    if 'obsidian' in installed_mcps or 'obsidian-tasks' in installed_mcps:
        vault_path = configure_obsidian_vault(project_root, existing_vault_path)

    # Calendar MCP
    if prompt_yes_no("\nDo you want to install Calendar MCP (macOS only)?"):
        if install_calendar_mcp(project_root, existing_calendar_name):
            installed_mcps.append('calendar')

    # Update configuration files
    if installed_mcps:
        update_mcp_json(project_root, installed_mcps, vault_path)
        update_settings_enabled_mcps(project_root, installed_mcps)

    # Summary
    print("\n=== Installation Complete! ===\n")
    if installed_mcps:
        print("Installed MCPs:")
        for mcp in installed_mcps:
            print(f"  - {mcp}")
        print()
        print("Configuration has been written to .mcp.json")
        print("The MCP servers are ready to use in Claude Code.")
    else:
        print("No MCPs were installed.")
    print()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInstallation cancelled by user.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"\nError running command: {e}")
        if e.stderr:
            print(f"Error output: {e.stderr}")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)
