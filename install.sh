#!/bin/sh
# I-AM-STRAIGHT installer for Claude Code (Mac, Linux, Git Bash). Copies files on this PC only. No internet.
# Use:  sh install.sh             -> installs for you (all projects)
#       sh install.sh --project   -> installs only in the current folder
#       sh install.sh --remove    -> removes it
here=$(cd "$(dirname "$0")" && pwd)
from="$here/skills/i-am-straight"
if [ "$1" = "--project" ]; then to="$(pwd)/.claude/skills/i-am-straight"; else to="$HOME/.claude/skills/i-am-straight"; fi
if [ "$1" = "--remove" ]; then
  if [ -d "$to" ]; then rm -rf "$to"; echo "Removed: $to"; else echo "Nothing to remove at $to"; fi
  exit 0
fi
if [ ! -f "$from/SKILL.md" ]; then echo "I cannot find skills/i-am-straight/SKILL.md next to this script. Run it from the I-AM-STRAIGHT folder."; exit 1; fi
mkdir -p "$to"
cp "$from/SKILL.md" "$to/SKILL.md"
echo "Done. I copied one file to:"
echo "  $to/SKILL.md"
echo ""
echo "Next: start Claude Code and type  /i-am-straight"
echo "To stop it, say:  stop straight"
echo "I did not change any other file on your PC."
