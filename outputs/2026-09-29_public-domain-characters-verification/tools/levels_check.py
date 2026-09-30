#!/usr/bin/env python3
"""Level-note check (automated): the facts from the books themselves in the easy-reads level notes.

Every example quoted in a level note (levels.EXAMPLES) must occur in that book word for word, and
every "about N words" figure (levels.WORDS) must be within 3% of a plain count of the
whitespace-separated words in the Standard Ebooks text. (Lexile measures and grade bands come from
outside sources, which are linked next to each level; they cannot be checked against the books.)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import levels  # noqa: E402
import verify  # noqa: E402


def main():
    total = bad = 0
    for book, examples in levels.EXAMPLES.items():
        secs = verify.load(book)
        for ex in examples:
            total += 1
            hits = [h for h in verify.locate(secs, verify.norm(ex), book) if h["exact"]]
            if hits:
                print(f"OK       {book}: \"{ex}\" ({hits[0]['label']})")
            else:
                bad += 1
                print(f"MISSING  {book}: \"{ex}\"")
    for book, what, part, claimed in levels.WORDS:
        total += 1
        secs = [s for s in verify.load(book) if not s["parent"]]
        if part:
            secs = secs[part[0]:part[1]]
        n = sum(len(s["text"].split()) for s in secs)
        ok = abs(n - claimed) <= 0.03 * claimed
        bad += not ok
        print(f"{'OK' if ok else 'OFF':8} {book} ({what}): about {claimed:,} words claimed, {n:,} counted")
    print(f"checked {total} level-note facts, {bad} problems")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
