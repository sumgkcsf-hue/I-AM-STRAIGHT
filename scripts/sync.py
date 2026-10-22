"""Make every tool file from RULES.md, so the rules are written once.
Run:  python scripts/sync.py        (no internet, no extra packages)
Writes: skills/i-am-straight/SKILL.md, AGENTS.md, GEMINI.md, .github/copilot-instructions.md, .cursor/rules/i-am-straight.mdc,
        .clinerules/i-am-straight.md, .windsurfrules, PASTE-ME.txt, ollama/Modelfile"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
rules = (ROOT / "RULES.md").read_text(encoding="utf-8").strip() + "\n"
body = rules.split("\n", 1)[1].strip() + "\n"          # drop the first title line
SHORT = "I-AM-STRAIGHT: talk in short, easy, gentle English. Rules are in RULES.md in the I-AM-STRAIGHT folder; they are copied below.\n\n"


def write(rel: str, text: str) -> None:
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", rel)


skill = ("---\nname: i-am-straight\n"
         "description: 'Answer in short, gentle, easy words for a reader who knows basic English: answer first, easy words, one idea at a time, numbered steps, never blame the reader. Invoke with /i-am-straight. Stays on until the person says stop straight.'\n"
         "license: MIT\n---\n\n# i-am-straight\n\n" + body)
write("skills/i-am-straight/SKILL.md", skill)
write(".cursor/skills/i-am-straight/SKILL.md", skill)
write("AGENTS.md", "# I-AM-STRAIGHT\n\nFor Codex, opencode and any agent that reads AGENTS.md. Follow these rules in every answer to the person.\n\n" + body)
write("GEMINI.md", "# I-AM-STRAIGHT\n\nFollow these rules in every answer to the person.\n\n" + body)
write(".github/copilot-instructions.md", "# I-AM-STRAIGHT\n\n" + body)
write(".cursor/rules/i-am-straight.mdc", "---\ndescription: Short, gentle, easy words for the reader\nalwaysApply: true\n---\n\n" + body)
write(".clinerules/i-am-straight.md", "# I-AM-STRAIGHT\n\n" + body)
write(".windsurfrules", "# I-AM-STRAIGHT\n\n" + body)
write("PASTE-ME.txt", "Paste everything below into any chat AI as your first message (or into its custom instructions). Nothing else is needed.\n\n" + SHORT + body)
system = (SHORT + body).replace('"""', "'''")
write("ollama/Modelfile", "# Local model with the I-AM-STRAIGHT rules. Change the next line to a model you have: run `ollama list`.\nFROM llama3.2\nPARAMETER temperature 0.3\nSYSTEM \"\"\"\n" + system + "\"\"\"\n")
