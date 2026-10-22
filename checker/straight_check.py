"""I-AM-STRAIGHT checker. Reads an answer and says, kindly, if it is too hard to read.
Works offline. Needs only Python 3. Nothing is sent anywhere.
Use:  python checker/straight_check.py answer.txt        or        echo "text" | python checker/straight_check.py
Exit code 0 = fine, 1 = needs work."""
import re
import sys

OPENERS = ("great question", "certainly", "sure!", "of course", "absolutely", "i'd be happy to", "i would be happy to")
BAD_WORDS = ("just", "simply", "obviously", "clearly", "trivial", "trivially", "as you know", "of course")
HARD = {"initialize", "instantiate", "configuration", "parameter", "exception", "repository", "directory", "validate", "verify", "modify",
        "mutate", "replicate", "clone", "commit", "binary", "protocol", "deprecated", "asynchronous", "authentication", "architecture", "implementation", "dependency"}
MAX_WORDS_PER_SENTENCE = 15
MAX_SENTENCES = 5


def syllables(word: str) -> int:
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    groups = re.findall(r"[aeiouy]+", w)
    n = len(groups)
    if w.endswith("e") and not w.endswith(("le", "ee")) and n > 1:
        n -= 1
    return max(1, n)


def sentences(text: str) -> list:
    text = re.sub(r"```.*?```", " ", text, flags=re.S)            # code blocks are not prose
    text = re.sub(r"`[^`]*`", " ", text)
    parts = re.split(r"(?<=[.!?])\s+|\n+", text)
    return [p.strip(" >*-#0123456789.)") for p in parts if len(re.findall(r"[A-Za-z']+", p)) >= 2]


def check(text: str) -> dict:
    sents = sentences(text)
    words = re.findall(r"[A-Za-z']+", " ".join(sents))
    n_w, n_s = len(words), max(1, len(sents))
    syl = sum(syllables(w) for w in words)
    ease = 206.835 - 1.015 * (n_w / n_s) - 84.6 * (syl / max(1, n_w))                 # Flesch reading ease
    grade = 0.39 * (n_w / n_s) + 11.8 * (syl / max(1, n_w)) - 15.59
    notes = []
    low = text.lower().strip()
    for o in OPENERS:
        if low.startswith(o):
            notes.append(f'Start with the answer, not "{o}".')
    for i, s in enumerate(sents, 1):
        c = len(re.findall(r"[A-Za-z']+", s))
        if c > MAX_WORDS_PER_SENTENCE + 5:
            notes.append(f"Sentence {i} has {c} words. Try to cut it in two.")
    if len(sents) > MAX_SENTENCES + 3:
        notes.append(f"{len(sents)} sentences. Try 5 or fewer, then offer more.")
    for b in BAD_WORDS:
        if re.search(rf"\b{re.escape(b)}\b", low):
            notes.append(f'Remove "{b}". It can make a reader feel small.')
    hard = sorted({w.lower() for w in words if w.lower() in HARD})
    if hard:
        notes.append("Hard words: " + ", ".join(hard) + ". Use an easier word or explain it once.")
    score = max(0, min(100, round(ease)))
    score -= 5 * len(notes)
    return {"score": max(0, score), "reading_ease": round(ease, 1), "grade": round(grade, 1), "sentences": len(sents), "words": n_w,
            "avg_words_per_sentence": round(n_w / n_s, 1), "notes": notes}


def main() -> int:
    text = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else sys.stdin.read()
    r = check(text)
    print(f"Score {r['score']}/100  |  school grade about {r['grade']}  |  {r['sentences']} sentences, {r['avg_words_per_sentence']} words each")
    for n in r["notes"]:
        print(" -", n)
    ok = r["score"] >= 70 and r["grade"] <= 8 and not r["notes"]
    print("Looks easy to read." if ok else "Can be easier. Small changes help.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
