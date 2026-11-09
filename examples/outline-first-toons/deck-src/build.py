#!/usr/bin/env python3
"""Assemble outline-first.html from the fragments in this folder.

DECK-BUILD-SPEC.md section 5: a shared head (CSS, icons) and tail (scripts),
plus one HTML fragment for each topic. To regenerate one section, replace its
fragment and run this script again.

Usage:
  python3 deck-src/build.py

Fragment order:
  head.html, title.html, agenda.html,
  topic-N.html for each N in TOPIC_ORDER (the time-plan order in OUTLINE.md),
  tail.html
"""
import pathlib
import re
import sys

SRC = pathlib.Path(__file__).resolve().parent
OUT = SRC.parent / "outline-first.html"

# Live order from the OUTLINE.md time plan.
TOPIC_ORDER = [1, 2, 3, 4, 5, 6, 7]

# Outline text that must not appear in the deck (OUTLINE-CONVENTIONS.md sections 3 and 4).
# A slide that teaches a tag must show it in <code>; this check reads the raw HTML,
# so such a slide must escape the bracket as &#91; inside <code>.
FORBIDDEN = ["[Seed]", "[Research]", "[All]", "[Technical]", "[Core]", "[Brief]",
             "[Self-guided]", "[TBD", "[UNVERIFIED", "[!", "Speaker notes:", "Main points:",
             "outline-only working aid"]


def fail(message):
    sys.exit("BUILD FAILED: " + message)


def read(name):
    path = SRC / name
    if not path.is_file():
        fail(f"fragment {name} does not exist in {SRC}.")
    return path.read_text(encoding="utf-8").rstrip("\n") + "\n"


def main():
    parts = [read("head.html"), read("title.html"), read("agenda.html")]
    for n in TOPIC_ORDER:
        text = read(f"topic-{n}.html")
        if not re.match(rf'<!-- TOPIC {n}: [^\n]+ -->\n<section id="s{n}">', text):
            fail(f'topic-{n}.html must start with "<!-- TOPIC {n}: Title -->" '
                 f'and then <section id="s{n}">.')
        parts.append(text)
    parts.append(read("tail.html"))
    html = "".join(parts)

    leaked = [t for t in FORBIDDEN if t in html]
    if leaked:
        fail("outline tag text is in the deck: " + ", ".join(leaked) + ".")

    OUT.write_text(html, encoding="utf-8")
    slides = len(re.findall(r"<section(?![^>]*\bid=\"s\d+\")[ >]", html))
    print(f"Wrote {OUT} ({len(TOPIC_ORDER)} topics, {slides} slides).")


if __name__ == "__main__":
    main()
