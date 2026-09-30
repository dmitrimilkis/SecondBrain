#!/usr/bin/env python3
"""Flatten a Standard Ebooks source repo into one plain-text file.

Each spine item (chapter/scene/book) becomes a section headed by a marker line:
    @@@ <file-stem> | <section title>
so any quote found later can be traced back to its chapter.
"""
import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

BLOCK = {"p", "h1", "h2", "h3", "h4", "h5", "h6", "br", "div", "blockquote",
         "tr", "li", "section", "article", "header", "footer", "hgroup", "table"}
SKIP_FILES = {"titlepage", "imprint", "colophon", "uncopyright", "halftitlepage",
              "toc", "loi", "endnotes", "dedication"}


class TextGrabber(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.title = None
        self._in_title = False
        self._skip = 0  # inside <a epub:type="noteref"> etc.

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self._in_title = True
        if tag == "a" and "noteref" in (a.get("epub:type") or ""):
            self._skip += 1
        if tag in BLOCK:
            self.out.append("\n")

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag == "a" and self._skip:
            self._skip -= 1
        if tag in BLOCK:
            self.out.append("\n")

    def handle_data(self, data):
        if self._in_title:
            self.title = (self.title or "") + data
            return
        if self._skip:
            return
        self.out.append(data)


def spine_files(repo: Path):
    opf = (repo / "src/epub/content.opf").read_text(encoding="utf-8")
    manifest = dict(re.findall(r'<item[^>]*?href="([^"]+)"[^>]*?id="([^"]+)"', opf))
    # manifest maps href->id in attribute order href,id; build id->href robustly
    id2href = {}
    for m in re.finditer(r"<item\b([^>]*)/?>", opf):
        attrs = dict(re.findall(r'(\S+?)="([^"]*)"', m.group(1)))
        if "id" in attrs and "href" in attrs:
            id2href[attrs["id"]] = attrs["href"]
    order = re.findall(r'<itemref[^>]*idref="([^"]+)"', opf)
    return [repo / "src/epub" / id2href[i] for i in order if i in id2href]


def clean(text: str) -> str:
    text = text.replace("⁠", "").replace("­", "")
    text = re.sub(r"[ \t    ]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def main(repo_dir: str, out_txt: str):
    repo = Path(repo_dir)
    parts, index = [], []
    for f in spine_files(repo):
        stem = f.stem
        if stem in SKIP_FILES:
            continue
        source = f.read_text(encoding="utf-8")
        articles = re.findall(r'<article id="([^"]+)"[^>]*>(.*?)</article>', source, flags=re.S)
        if len(articles) > 1:
            # one file holding many short pieces (e.g. Aesop's fables): one section per piece,
            # so every quote can be traced to its own fable or tale
            for art_id, chunk in articles:
                heading = re.search(r"<h[1-6][^>]*>(.*?)</h[1-6]>", chunk, flags=re.S)
                title = html.unescape(re.sub(r"<[^>]+>", "", heading.group(1)).strip()) if heading else art_id
                g = TextGrabber()
                g.feed(chunk)
                body = clean("".join(g.out))
                parts.append(f"@@@ {stem}-{art_id} | {title}\n{body}\n")
                index.append({"file": f"{stem}-{art_id}", "title": title, "chars": len(body)})
            continue
        g = TextGrabber()
        g.feed(source)
        body = clean("".join(g.out))
        title = html.unescape((g.title or stem).strip())
        parts.append(f"@@@ {stem} | {title}\n{body}\n")
        index.append({"file": stem, "title": title, "chars": len(body)})
    Path(out_txt).write_text("\n".join(parts), encoding="utf-8")
    Path(out_txt).with_suffix(".index.json").write_text(json.dumps(index, indent=1), encoding="utf-8")
    print(f"{out_txt}: {len(index)} sections, {sum(i['chars'] for i in index):,} chars")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
