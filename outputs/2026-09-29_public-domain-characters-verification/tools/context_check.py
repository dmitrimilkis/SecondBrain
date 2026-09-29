#!/usr/bin/env python3
"""Check 2: is each evidence quote actually about the character it is filed under?

For every evidence quote we look at a window of text around its location and test
whether any of the character's name tokens (name + aka) appears there. Quotes whose
window never mentions the character are printed with context for manual review.
"""
import re
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import verify  # noqa: E402

STOP = {"the", "of", "and", "a", "an", "mr", "mrs", "dr", "miss", "lady", "sir", "prince", "princess",
        "count", "king", "queen", "captain", "inspector", "general", "professor", "bishop", "old", "as",
        "in", "this", "translation", "later", "born", "real", "name", "called", "also", "given", "his", "her",
        "known", "from", "by", "on", "to", "two", "con", "men", "who", "is", "was"}


def tokens(ch):
    raw = ch["name"] + " " + ch.get("aka", "")
    raw = verify.fold(raw)
    toks = {t.lower() for t in re.findall(r"[A-Za-z][A-Za-z'\-]{2,}", raw)} - STOP
    return toks


def main(books, window=700):
    flagged = 0
    total = 0
    for book in books:
        data = verify.load_data(book)
        secs = verify.load(book)
        for ch in data["characters"]:
            toks = tokens(ch)
            for ev in ch["evidence"]:
                total += 1
                hits = verify.locate(secs, verify.norm(ev["quote"]), book)
                if not hits:
                    print(f"!! MISSING {book}/{ch['name']}: {ev['quote'][:60]}")
                    flagged += 1
                    continue
                h = hits[0]
                t = h["sec"]["ntext"]
                a, b = max(0, h["pos"] - window), h["pos"] + len(ev["quote"]) + window
                ctx = t[a:b].lower()
                if not any(re.search(r"\b" + re.escape(tok) + r"\b", ctx) for tok in toks):
                    flagged += 1
                    print(f"-- {book} / {ch['name']} [{h['label']}] ({ev['supports']})")
                    print(f"   QUOTE: {ev['quote'][:120]}")
                    c0, c1 = max(0, h['pos'] - 350), h['pos'] + len(ev['quote']) + 150
                    print(f"   CTX: ...{t[c0:c1]}...\n")
    print(f"checked {total} quotes; {flagged} need manual review")


if __name__ == "__main__":
    bks = sys.argv[1:] or sorted(p.stem for p in verify.DATA.glob("*.py"))
    main(bks)
