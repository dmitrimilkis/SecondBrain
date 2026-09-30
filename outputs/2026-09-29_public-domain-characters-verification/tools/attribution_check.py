#!/usr/bin/env python3
"""Check 2 (automated): is each evidence quote really about the character it is filed under?

Resolution rules, strongest first; a quote passes on the first rule that holds:
  NAME     - the character's name/alias appears within +-700 chars of the quote
  ROLE     - a role word the book uses for that character ("the Count", "the clerk",
             "the young man", "the Queen" ...) appears within +-700 chars
  SUBJECT  - the evidence note names someone else as the subject (e.g. a victim)
             and that proper name appears within +-700 chars
  NARRATOR - the quote is first-person and the passage is narrated by the character
             (whole-book narrators, the diary/journal headers in Dracula, Walton's
             letters and Victor's chapters in Frankenstein)
  SPEAKER  - a speech tag right next to the quote names the character
  CHAPTER  - weakest: the character is named elsewhere in the same chapter/section
Anything left over is printed in full for a manual look.
"""
import re
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import verify  # noqa: E402
from context_check import tokens  # noqa: E402

WINDOW = 700

# role words the texts use instead of names (lower-case)
ROLES = {
    ("alice", "The Queen of Hearts"): ["queen"],
    ("alice", "The Duchess"): ["duchess", "baby"],
    ("carol", "Bob Cratchit"): ["clerk"],
    ("carol", "The Ghost of Christmas Past"): ["ghost", "spirit", "apparition", "figure"],
    ("crime", "Rodion Romanovitch Raskolnikov"): ["young man"],
    ("crime", "Sonia Marmeladov"): ["my daughter", "my own daughter"],
    ("crime", "Semyon Zaharovitch Marmeladov"): ["clerk"],
    ("crime", "Alyona Ivanovna"): ["old woman", "pawnbroker"],
    ("dracula", "Count Dracula"): ["the count", "old man", "un-dead", "vampire"],
    ("dracula", "Lucy Westenra"): ["un-dead", "thing in the coffin"],
    ("dracula", "Quincey P. Morris"): ["dying man"],
    ("frankenstein", "Victor Frankenstein"): ["stranger"],
    ("frankenstein", "The Creature"): ["the being", "creature", "daemon", "fiend"],
    ("frankenstein", "Elizabeth Lavenza"): ["this child", "wedding night"],
    ("gatsby", "Jay Gatsby"): ["my neighbour"],
    ("hamlet", "King Claudius"): ["king", "uncle"],
    ("hamlet", "Queen Gertrude"): ["queen", "mother"],
    ("hamlet", "Ophelia"): ["sister"],
    ("holmes", "Irene Adler"): ["actress", "youth in an ulster"],
    ("holmes", "Dr. Watson"): ["my wife"],
    ("huckfinn", "Pap Finn"): ["pap"],
    ("huckfinn", "The King and the Duke"): ["fellows", "old fellow", "king", "duke"],
    ("miserables", "Jean Valjean"): ["said the man", "traveller", "a stranger"],
    ("miserables", "Cosette"): ["girl"],
    ("miserables", "Bishop Myriel"): ["bishop"],
    ("miserables", "The Thénardiers"): ["thenardier"],
    ("miserables", "Gavroche"): ["child", "boy", "lad"],
    ("mobydick", "Queequeg"): ["harpooneer", "savage", "cannibal", "pagan"],
    ("odyssey", "Polyphemus"): ["cyclops"],
    ("warpeace", "Pierre Bezukhov"): ["bezukhova"],
    ("warpeace", "Elen Kuragina"): ["his wife"],
    ("pinocchio", "Pinocchio"): ["piece of wood", "bit of wood"],  # before he is carved and named
    ("pinocchio", "Geppetto"): ["papa", "father"],
    ("pinocchio", "The Fox and the Cat"): ["assassins"],
}

WHOLE_BOOK_NARRATOR = {
    ("mobydick", "Ishmael"), ("gatsby", "Nick Carraway"),
    ("huckfinn", 'Huckleberry "Huck" Finn'), ("holmes", "Dr. Watson"),
}
FIRST_PERSON = re.compile(r"\b(I|[Mm]e|[Mm]y|[Mm]ine|[Mm]yself)\b")
DRACULA_HEADER = re.compile(r"(Jonathan Harker|Mina Murray|Mina Harker|Dr\. Seward|Lucy Westenra)'s (Journal|Diary)")
SPEECH_VERBS = r"(?:said|cried|replied|answered|exclaimed|asked|continued|resumed|muttered|shouted|remarked|observed|repeated)"


def narrator_ok(book, name, sec, pos, quote):
    # first-person voice in the quote or in the sentences right around it
    around = sec["ntext"][max(0, pos - 250): pos + len(quote) + 250]
    if not (FIRST_PERSON.search(quote) or FIRST_PERSON.search(around)):
        return False
    if (book, name) in WHOLE_BOOK_NARRATOR:
        return True
    if book == "dracula":
        heads = list(DRACULA_HEADER.finditer(sec["ntext"][:pos]))
        if heads:
            writer = heads[-1].group(1)
            return (name == "Jonathan Harker" and writer == "Jonathan Harker") or \
                   (name == "Dr. John Seward" and writer == "Dr. Seward") or \
                   (name == "Mina Harker" and writer.startswith("Mina"))
        # Jonathan's journal runs through chapters I-IV without repeated headers
        return name == "Jonathan Harker" and sec["stem"] in {"chapter-1", "chapter-2", "chapter-3", "chapter-4"}
    if book == "frankenstein":
        if name == "Robert Walton":
            return sec["stem"].startswith("letter") or "walton, in continuation" in sec["ntext"][:pos].lower()
        if name == "Victor Frankenstein":
            n = int(sec["stem"].split("-")[1]) if sec["stem"].startswith("chapter") else 0
            return 1 <= n <= 10 or 17 <= n <= 24  # XI-XVI are the Creature's own narrative
    return False


def speaker_ok(toks, text, pos, qlen):
    near = text[max(0, pos - 160): pos + qlen + 160]
    for m in re.finditer(SPEECH_VERBS + r"\s+(?:the\s+)?([A-Z][\w'\-]+)", near):
        if m.group(1).lower() in toks:
            return True
    for m in re.finditer(r"([A-Z][\w'\-]+)\s+" + SPEECH_VERBS, near):
        if m.group(1).lower() in toks:
            return True
    return False


def pronoun_speaker_ok(toks, text, pos, qlen):
    near = text[max(0, pos - 160): pos + qlen + 160]
    if not re.search(r"\b(he|she)\s+" + SPEECH_VERBS + r"|" + SPEECH_VERBS + r"\s+(he|she)\b", near):
        return False
    return has_any(text[max(0, pos - 3000): pos], toks)


def has_any(text, words):
    t = text.lower()
    return any(re.search(r"\b" + re.escape(w) + r"\b", t) for w in words)


def resolve(books):
    """Return one item per evidence quote: [rule, book, name, label, quote, text, pos, qlen, stem]."""
    items, resolved = [], {}
    for book in books:
        data = verify.load_data(book)
        secs = verify.load(book)
        for ch in data["characters"]:
            toks = sorted(tokens(ch))
            roles = ROLES.get((book, ch["name"]), [])
            for ev in ch["evidence"]:
                q = verify.norm(ev["quote"])
                h = verify.locate(secs, q, book)[0]
                sec, pos, text = h["sec"], h["pos"], h["sec"]["ntext"]
                win = text[max(0, pos - WINDOW): pos + len(q) + WINDOW]
                subject = [w.lower() for w in re.findall(r"\b[A-Z][a-z]{2,}\b", ev["supports"])]
                if has_any(win, toks):
                    rule = "NAME"
                elif roles and has_any(win, roles):
                    rule = "ROLE"
                elif subject and has_any(text[max(0, pos - 2000): pos + len(q) + 2000], subject):
                    rule = "SUBJECT"
                elif narrator_ok(book, ch["name"], sec, pos, ev["quote"]):
                    rule = "NARRATOR"
                elif speaker_ok(toks, text, pos, len(q)) or pronoun_speaker_ok(toks, text, pos, len(q)):
                    rule = "SPEAKER"
                elif has_any(text[max(0, pos - 1500): pos + len(q) + 1500], toks + list(roles)):
                    rule = "NEAR"
                elif has_any(text, toks) or (roles and has_any(text, roles)):
                    rule = "CHAPTER"
                else:
                    rule = "UNRESOLVED"
                resolved.setdefault((book, ch["name"]), []).append((rule, sec["stem"], pos))
                items.append([rule, book, ch["name"], h["label"], ev["quote"], text, pos, len(q), sec["stem"]])
    # LINKED: a weak quote sits in the same chapter within 4000 chars of another quote
    # for the same character that was attributed by a stronger rule
    for it in items:
        if it[0] in ("CHAPTER", "UNRESOLVED"):
            for rule2, stem2, pos2 in resolved[(it[1], it[2])]:
                if rule2 not in ("CHAPTER", "UNRESOLVED", "LINKED") and stem2 == it[8] and abs(pos2 - it[6]) <= 4000:
                    it[0] = "LINKED"
                    break
    return items


def main(books):
    items = resolve(books)
    tally, leftovers = {}, []
    for it in items:
        tally[it[0]] = tally.get(it[0], 0) + 1
        if it[0] in ("CHAPTER", "UNRESOLVED"):
            leftovers.append(tuple(it[:8]))
    total = sum(tally.values())
    print(f"{total} evidence quotes:", ", ".join(f"{k} {v}" for k, v in sorted(tally.items(), key=lambda x: -x[1])))
    for rule, book, name, label, quote, text, pos, qlen in leftovers:
        print(f"\n[{rule}] {book} / {name} [{label}]\n  QUOTE: {quote[:110]}")
        print(f"  NEAR : ...{text[max(0, pos - 260): pos + qlen + 120]}...")
    return 1 if leftovers else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or sorted(p.stem for p in verify.DATA.glob("*.py"))))
