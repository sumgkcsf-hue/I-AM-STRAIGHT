# Helping

Thank you. You do not need to be an expert.

## The easiest way to help

Found an answer that is still too hard? Open an issue. Paste the answer and say which AI tool gave it. That is enough.

## Changing the rules

1. Edit `RULES.md`. It is the only place the rules live.
2. Run `python scripts/sync.py`. It rewrites every tool file.
3. Run `python -m unittest discover -s tests`.
4. Open a pull request. Say in simple words what you changed and why.

## Please keep

- Short sentences. Easy words.
- A kind voice. Never "just", "simply" or "obviously".
- No internet calls, no keys, no accounts. This project must work offline.

## Adding a tool

Add a short file for the tool in the place that tool reads, and add it to `scripts/sync.py`. Add a line to `INSTALL.md`.
