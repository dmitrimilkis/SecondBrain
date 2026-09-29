#!/usr/bin/env python3
"""Check 4 (automated): no invented specifics.

Every number (digits or number words) and every proper name in a description, outside the
quoted fragments (which check 1 already verifies word for word), must also occur in:
  - that character's own evidence quotes (the supports notes do NOT count: they are my words),
  - the chapter labels where those quotes sit (e.g. "1812" in "Book IV, Part I: 1812"),
  - the character's name/aka, the names/akas of other characters in the same book
    (their own entries carry the evidence for them), or the book's title/author/edition line.
A capitalised word that merely starts a sentence is treated as an ordinary word if the
books use it in lower case somewhere. Anything left over is printed for review, and
deliberate editorial terms can be whitelisted per character with "allow_terms".
"""
import re
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import verify  # noqa: E402

NUMWORDS = set(("two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen "
                "seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred thousand "
                "second third fourth fifth dozen").split())
TITLES = set("Mr Mrs Dr Miss Lady Sir Prince Princess Count Countess King Queen Captain Inspector General Professor "
             "Bishop Saint St Lord Uncle Aunt Monsieur Madame Mademoiselle Don Hon".split())


def expand(text):
    out = set()
    for w in re.findall(r"\d[\d,]*\d|\d|[A-Za-z][A-Za-z'\-]*", verify.norm(text)):
        w = w.lower()
        out.add(w)
        for part in re.split(r"[-']", w):
            if part:
                out.add(part)
        if w.endswith("'s"):
            out.add(w[:-2])
    out |= {w[:-1] for w in list(out) if w.endswith("s")}
    return out


def lower_vocab():
    vocab = set()
    for p in verify.BOOKS.glob("*.txt"):
        vocab |= set(re.findall(r"\b[a-z][a-z'\-]*\b", verify.fold(p.read_text(encoding="utf-8"))))
    return vocab


def strip_quoted(desc, extra):
    desc = verify.norm(desc)
    for t in extra:
        desc = desc.replace(t, " ")
    return re.sub(r'"[^"]*"', ' "" ', desc)


def main(books):
    vocab = lower_vocab()
    flagged = 0
    for book in books:
        data = verify.load_data(book)
        secs = verify.load(book)
        meta = " ".join(str(data[k]) for k in ("title", "author", "year", "edition"))
        others = " ".join(c["name"] + " " + c.get("aka", "") for c in data["characters"])
        for ch in data["characters"]:
            labels = []
            for e in ch["evidence"]:
                h = verify.locate(secs, verify.norm(e["quote"]), book)
                labels.append(h[0]["label"] if h else "")
            pool = expand(" ".join(e["quote"] for e in ch["evidence"]) + " " + " ".join(labels) + " " + meta + " " + others)
            allowed = list(ch.get("not_quotes", [])) + list(ch.get("allow_terms", []))
            desc = strip_quoted(ch["description"], allowed)
            missing = []
            for m in re.finditer(r"\d[\d,]*\d|\d|[A-Za-z][A-Za-z'\-]*", desc):
                tok = m.group(0)
                parts = [tok.lower()] + [p for p in re.split(r"[-']", tok.lower()) if p]
                if tok[0].isdigit():
                    if tok.lower() not in pool:
                        missing.append(tok)
                    continue
                if tok[0].isupper():
                    low = tok.lower()
                    base = low[:-2] if low.endswith("'s") else low.rstrip("'")
                    if tok in TITLES or base in pool or low in pool:
                        continue
                    before = desc[:m.start()].rstrip()
                    sentence_start = before == "" or before[-1] in ".!?:(" or before.endswith('""')
                    if sentence_start and tok.lower() in vocab:
                        continue
                    missing.append(tok)
                    continue
                for p in parts:
                    if p in NUMWORDS and p not in pool:
                        missing.append(p)
            missing = list(dict.fromkeys(missing))
            if missing:
                flagged += 1
                print(f"{book} / {ch['name']}: {', '.join(missing)}")
    print(f"characters with unsupported specifics: {flagged}")
    return 1 if flagged else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or sorted(p.stem for p in verify.DATA.glob("*.py"))))
