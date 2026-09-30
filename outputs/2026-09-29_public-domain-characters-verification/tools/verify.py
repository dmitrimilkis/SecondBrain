#!/usr/bin/env python3
"""Quote finder / verifier for the extracted book texts.

Usage:
  verify.py find <book> "<quote>" [context_chars]   # locate a quote, show context
  verify.py grep <book> "<regex>" [max_hits]         # regex search with locations
  verify.py check [<book> ...]                       # verify every evidence quote in data/*.py
"""
import importlib.util
import re
import signal
import sys
signal.signal(signal.SIGPIPE, signal.SIG_DFL)
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
BOOKS = HERE / "books"
DATA = HERE / "data"

ROMAN = r"[IVXLCDM]+"


def fold(s: str) -> str:
    """Strip accents/stress marks (Maude's 'Natásha' -> 'Natasha')."""
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def norm(s: str) -> str:
    s = fold(s)
    s = s.replace("⁠", "").replace("­", "")
    s = re.sub("[‘’ʼ′]", "'", s)
    s = re.sub("[“”″]", '"', s)
    s = re.sub("[‒–—―−]", "-", s)
    s = s.replace("…", "...")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def load(book: str):
    raw = (BOOKS / f"{book}.txt").read_text(encoding="utf-8")
    secs = []
    for chunk in raw.split("@@@ ")[1:]:
        head, _, body = chunk.partition("\n")
        stem, _, title = head.partition(" | ")
        secs.append({"stem": stem.strip(), "title": title.strip(), "text": body})
    # compute human-readable labels
    parents = {"volume": None, "book": None, "part": None}
    for s in secs:
        kind = s["stem"].split("-")[0]
        if kind == "epilogue":
            # epilogues sit outside the volume/book/part hierarchy
            if len(s["text"]) < 600:  # heading only, e.g. "First Epilogue: 1813-20"
                parents = {"volume": s["title"], "book": None, "part": None}
                s["label"], s["parent"] = s["title"], True
                continue
            if s["stem"] == "epilogue":  # a single epilogue chapter
                parents = {"volume": None, "book": None, "part": None}
        is_parent = kind in parents and len(s["text"]) < 600
        if is_parent:
            parents[kind] = s["title"]
            if kind == "volume":
                parents["book"] = parents["part"] = None
            if kind == "book":
                parents["part"] = None
            s["label"] = s["title"]
            s["parent"] = True
            continue
        t = s["title"]
        if re.fullmatch(ROMAN + r"(:.*)?", t):
            t = "Chapter " + t
        chain = [p for p in (parents["volume"], parents["book"], parents["part"]) if p]
        s["label"] = ", ".join(chain + [t])
        s["parent"] = False
        s["ntext"] = norm(s["text"])
    return secs


def scene_of(sec, pos_in_norm):
    """For plays: find the last 'Scene <ROMAN>' header before a position."""
    hits = list(re.finditer(r"Scene (" + ROMAN + r") ", sec["ntext"][:pos_in_norm]))
    return f"Scene {hits[-1].group(1)}" if hits else None


def locate(secs, needle_norm, book):
    out = []
    low = needle_norm.lower()
    for s in secs:
        if s["parent"]:
            continue
        i = s["ntext"].find(needle_norm)
        exact = True
        if i < 0:
            i = s["ntext"].lower().find(low)
            exact = False
        if i >= 0:
            lab = s["label"]
            if book == "hamlet":
                sc = scene_of(s, i)
                if sc:
                    lab = f"{lab}, {sc}"
            out.append({"label": lab, "stem": s["stem"], "pos": i, "exact": exact, "sec": s})
    return out


def cmd_find(book, quote, ctx=250):
    secs = load(book)
    hits = locate(secs, norm(quote), book)
    if not hits:
        print("NOT FOUND")
        return 1
    for h in hits:
        t = h["sec"]["ntext"]
        a, b = max(0, h["pos"] - ctx), h["pos"] + len(norm(quote)) + ctx
        print(f"[{h['label']}] ({'exact' if h['exact'] else 'case-insensitive'})")
        print("   ..." + t[a:b] + "...")
    return 0


def cmd_grep(book, rx, maxhits=30):
    secs = load(book)
    n = 0
    r = re.compile(rx, re.I)
    for s in secs:
        if s["parent"]:
            continue
        for m in r.finditer(s["ntext"]):
            lab = s["label"]
            if book == "hamlet":
                sc = scene_of(s, m.start())
                lab = f"{lab}, {sc}" if sc else lab
            a, b = max(0, m.start() - 160), m.end() + 160
            print(f"[{lab}] ...{s['ntext'][a:b]}...")
            n += 1
            if n >= maxhits:
                print(f"(stopped at {maxhits})")
                return
    print(f"({n} hits)")


def load_data(book):
    p = DATA / f"{book}.py"
    spec = importlib.util.spec_from_file_location(book, p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.BOOK


def cmd_check(books):
    total = bad = 0
    report = []
    for book in books:
        data = load_data(book)
        secs = load(book)
        for ch in data["characters"]:
            for ev in ch["evidence"]:
                total += 1
                hits = locate(secs, norm(ev["quote"]), book)
                exact = [h for h in hits if h["exact"]]
                if not exact:
                    bad += 1
                    status = "CASE-ONLY" if hits else "MISSING"
                    report.append(f"{status}: {book} / {ch['name']}: {ev['quote'][:90]}")
                ev["_found"] = [h["label"] for h in exact]
            # every fragment quoted inside the description must also be verbatim in the book
            for frag in re.findall(r'"([^"]+)"', ch["description"]):
                for part in re.split(r"\.\.\.|…", frag):
                    part = part.strip(" ,;:.!?-")
                    if len(part) < 4 or part in ch.get("not_quotes", []):
                        continue
                    total += 1
                    hits = locate(secs, norm(part), book)
                    if not any(h["exact"] for h in hits):
                        bad += 1
                        status = "DESC-QUOTE CASE-ONLY" if hits else "DESC-QUOTE MISSING"
                        report.append(f"{status}: {book} / {ch['name']}: \"{part[:90]}\"")
            for neg in ch.get("absent", []):
                total += 1
                # "in:<part of a section label>::<regex>" limits the search to matching sections,
                # e.g. no kiss in "Little Snow-White" although other tales in the book have one
                scope = None
                if neg.startswith("in:"):
                    scope, neg = neg[3:].split("::", 1)
                pat = re.compile(neg, re.I)
                pool = [s for s in secs if not s["parent"] and (scope is None or scope in s["label"])]
                if scope is not None and not pool:
                    bad += 1
                    report.append(f"SCOPE NOT FOUND: {book} / {ch['name']}: {scope}")
                    continue
                found = [s["label"] for s in pool if pat.search(s["ntext"])]
                if found:
                    bad += 1
                    report.append(f"PRESENT (should be absent): {book} / {ch['name']}: /{neg}/ in {found[:3]}")
    print("\n".join(report) if report else "all quotes found verbatim; all 'absent' patterns absent")
    print(f"checked {total} items, {bad} problems")
    return bad


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "find":
        sys.exit(cmd_find(sys.argv[2], sys.argv[3], int(sys.argv[4]) if len(sys.argv) > 4 else 250))
    elif cmd == "grep":
        cmd_grep(sys.argv[2], sys.argv[3], int(sys.argv[4]) if len(sys.argv) > 4 else 30)
    elif cmd == "check":
        books = sys.argv[2:] or sorted(p.stem for p in DATA.glob("*.py"))
        sys.exit(1 if cmd_check(books) else 0)
