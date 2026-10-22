# Install I-AM-STRAIGHT

Nothing here needs an account, a key or the internet. Every step only copies text files on your own PC.

## Claude Code

**Windows:** in PowerShell, from this folder:
```
./install.ps1
```
**Mac or Linux:**
```
sh install.sh
```
It copies the skill to `~/.claude/skills/i-am-straight`. Start Claude Code and type `/i-am-straight`.

**Only one project?** Use `./install.ps1 -Project` (or `sh install.sh --project`). It copies to `.claude/skills` in the folder you are in.

**Always on?** Add this one line to your `CLAUDE.md` file (the installer will show you the text, it will not change the file by itself):
```
Follow the rules in ~/.claude/skills/i-am-straight/SKILL.md in every answer.
```

**Remove it:** delete the folder `~/.claude/skills/i-am-straight`.

## Codex, opencode and other agents

Copy `AGENTS.md` into your project folder. Done.

## Cursor

Copy `.cursor/rules/i-am-straight.mdc` into your project at the same path.

## Gemini CLI

Copy `GEMINI.md` into your project folder.

## GitHub Copilot

Copy `.github/copilot-instructions.md` into your project at the same path.

## Cline / Windsurf

Cline: copy `.clinerules/i-am-straight.md`. Windsurf: copy `.windsurfrules`.

## Local models (no internet)

**Ollama:**
1. Run `ollama list` and pick a model you have.
2. Open `ollama/Modelfile` and change the `FROM` line to that model name.
3. Run `ollama create straight -f ollama/Modelfile`
4. Run `ollama run straight`

**LM Studio:** open a chat, find "System Prompt", paste the text from `PASTE-ME.txt`.

## Any chat AI

Open `PASTE-ME.txt`, copy everything, paste it as your first message.

## Check that it works

```
python -m unittest discover -s tests
python checker/straight_check.py examples/before-after.md
```

## Change the rules

Edit `RULES.md`, then run `python scripts/sync.py`. It rewrites every tool file from that one page.
