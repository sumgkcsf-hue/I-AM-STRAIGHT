# I-AM-STRAIGHT installer for Claude Code (Windows). Copies files on this PC only. No internet.
# Use:  ./install.ps1            -> installs for you (all projects)
#       ./install.ps1 -Project   -> installs only in the current folder
#       ./install.ps1 -Remove    -> removes it
param([switch]$Project, [switch]$Remove)
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$from = Join-Path $here "skills\i-am-straight"
if ($Project) { $to = Join-Path (Get-Location) ".claude\skills\i-am-straight" } else { $to = Join-Path $env:USERPROFILE ".claude\skills\i-am-straight" }
if ($Remove) {
    if (Test-Path $to) { Remove-Item -Recurse -Force $to; Write-Host "Removed: $to" } else { Write-Host "Nothing to remove at $to" }
    exit 0
}
if (-not (Test-Path (Join-Path $from "SKILL.md"))) { Write-Host "I cannot find skills\i-am-straight\SKILL.md next to this script. Run this from the I-AM-STRAIGHT folder."; exit 1 }
New-Item -ItemType Directory -Force -Path $to | Out-Null
Copy-Item -Force -Path (Join-Path $from "SKILL.md") -Destination $to
Write-Host "Done. I copied one file to:"
Write-Host "  $to\SKILL.md"
Write-Host ""
Write-Host "Next: start Claude Code and type  /i-am-straight"
Write-Host "To stop it, say:  stop straight"
Write-Host "I did not change any other file on your PC."
