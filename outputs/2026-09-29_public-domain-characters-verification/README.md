# Verification kit: 15 famous public-domain books and their characters

This folder backs up [the character list](../2026-09-29_query-15-famous-public-domain-books-characters.md).

- `evidence.md`: every supporting quote (787), with its chapter, what it supports and how it was attributed.
- `reports/`: the output of the three automated checks as run on 2026-09-29.
- `tools/`: the scripts and the character data (`tools/data/*.py`, one file per book) the checks ran on.

## Re-running the checks

Needs Python 3.9+ and git (no other packages).

```sh
cd outputs/2026-09-29_public-domain-characters-verification/tools
./fetch_texts.sh               # fetch the 15 Standard Ebooks sources at the exact commits used, flatten into books/
python3 verify.py check        # check 1: every quote and quoted phrase is in the book, word for word; myths absent
python3 attribution_check.py   # check 2: every quote is about the character it is filed under
python3 specifics_check.py     # check 3: every number and proper name in a description is backed by a quote
```

Each script exits with a non-zero status if anything fails. To look things up by hand:

```sh
python3 verify.py find dracula "children of the night"      # where is this quote, with context
python3 verify.py grep hamlet "lord chamberlain"             # regex search with chapter labels
```

## How the data is laid out

Each `tools/data/<book>.py` holds a `BOOK` dict. For every character there is a `description`, an `evidence` list of
`{quote, supports}` pairs, and optionally `absent` (regex patterns that must *not* occur in the book), `not_quotes`
(quoted phrases in the description that are deliberately not from the book, such as "the Mad Hatter"), and
`allow_terms` (editorial terms exempt from check 3).

Matching ignores only typography: curly vs straight quotes, dash styles, accents and line breaks. Words and
capitalisation must match exactly.
