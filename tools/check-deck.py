#!/usr/bin/env python3
"""Check every slide of a Reveal.js deck built with this template.

Checks (DECK-BUILD-SPEC.md section 6, items 1-5 and the leaked-text part of 7):
  visible       the slide is inside the viewport when it is current
  overflow      content fits the 1280x720 frame
  footer        no content element overlaps the footer band
  diagrams      every pre.mermaid produced an SVG
  console       no console errors or page errors
  tags          no outline working-aid tags leaked into visible text
                (text inside <code> is skipped: that is how a deck shows a tag as an example)

Usage:
  pip install playwright && playwright install chromium
  python tools/check-deck.py deck.html
  python tools/check-deck.py deck.html --shots shots/          # also save a PNG per slide
  python tools/check-deck.py deck.html --map URL=FILE ...      # serve CDN files from local copies

--map is for sandboxes without internet access, e.g.
  --map https://cdnjs.cloudflare.com/ajax/libs/reveal.js/5.1.0/reveal.min.js=vendor/reveal.js
Exit code is 0 when every check passes, 1 otherwise.
"""
import argparse, json, pathlib, re, sys
from playwright.sync_api import sync_playwright

# Outline text that must never be visible on a slide. Add your BRIEF.md audience tags with --tags.
WORKING_AID_TAGS = ["[Seed]", "[Research]", "[All]", "[Technical]", "[Leadership/Business]",
                    "[Core]", "[Brief]", "[Self-guided]", "Coverage gaps", "Source reconciliation",
                    "outline-only working aid", "Changes by version", "Speaker notes:", "Main points:",
                    "[!", "[TBD", "[UNVERIFIED"]

WALK = r"""async (exclude) => {
  const out = [];
  const H = Reveal.getHorizontalSlides();
  for (let h = 0; h < H.length; h++) {
    const n = Math.max(1, H[h].querySelectorAll(':scope > section').length);
    for (let v = 0; v < n; v++) {
      Reveal.slide(h, v);
      await new Promise(r => setTimeout(r, 400));
      const s = Reveal.getCurrentSlide();
      const r = s.getBoundingClientRect();
      const label = ((s.querySelector('h1,h2,h3') || {}).textContent || s.id || '').trim().slice(0, 60);
      const visible = r.top > -5 && r.bottom < window.innerHeight + 5 && r.height > 100;
      const overflow = s.scrollHeight > s.clientHeight + 2;
      const ft = s.querySelector(':scope > footer');
      const limit = ft ? ft.getBoundingClientRect().top : r.bottom - 60 * Reveal.getScale();
      let collision = false;
      s.querySelectorAll(':scope > *:not(' + exclude + ')').forEach(el => {
        if (el.getBoundingClientRect().bottom > limit + 1) collision = true;
      });
      const mm = s.querySelectorAll('pre.mermaid').length;
      const mmok = s.querySelectorAll('pre.mermaid svg').length;
      const clone = s.cloneNode(true); clone.querySelectorAll('aside.notes, code').forEach(a => a.remove());
      out.push({h, v, label, visible, overflow, collision, mm, mmok, text: clone.textContent, fontSize: s.style.fontSize});
    }
  }
  return out;
}"""

# Class names fixed by DECK-BUILD-SPEC.md section 2.1
EXCLUDE = "footer,aside,.pgnum,.more,.tiy,.chrome,script,style"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("deck")
    ap.add_argument("--shots", help="directory for one PNG per slide")
    ap.add_argument("--map", nargs="*", default=[], help="URL=FILE pairs served instead of the network")
    ap.add_argument("--viewport", default="1600x900")
    ap.add_argument("--tags", nargs="*", default=[], help="extra tags to treat as leaked text, e.g. [Ops]")
    a = ap.parse_args()
    w, h = map(int, a.viewport.split("x"))
    mapping = dict(m.split("=", 1) for m in a.map)
    deck = pathlib.Path(a.deck).resolve()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": w, "height": h})
        errors = []
        page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
        page.on("pageerror", lambda e: errors.append(str(e)))
        def serve(body, ctype):
            return lambda route: route.fulfill(body=body, content_type=ctype)
        for url, f in mapping.items():
            ctype = "text/css" if url.endswith(".css") else "application/javascript"
            page.route(url, serve(pathlib.Path(f).read_bytes(), ctype))
        page.goto(deck.as_uri())
        page.wait_for_timeout(1500)
        slides = page.evaluate(WALK, EXCLUDE)
        if a.shots:
            out = pathlib.Path(a.shots); out.mkdir(parents=True, exist_ok=True)
            for i, s in enumerate(slides):
                page.evaluate(f"Reveal.slide({s['h']},{s['v']})")
                page.wait_for_timeout(500)
                page.screenshot(path=str(out / f"{i+1:03d}.png"))
        browser.close()

    problems = []
    for i, s in enumerate(slides):
        where = f"page {i+1} ({s['label']})"
        if not s["visible"]: problems.append(f"{where}: not visible")
        if s["overflow"]: problems.append(f"{where}: overflows the frame")
        if s["collision"]: problems.append(f"{where}: content overlaps the footer")
        if s["mm"] != s["mmok"]: problems.append(f"{where}: {s['mm'] - s['mmok']} diagram(s) not rendered")
        for t in WORKING_AID_TAGS + a.tags:
            if t in s["text"]: problems.append(f"{where}: working-aid text '{t}' is visible")
    problems += [f"console: {e}" for e in errors]

    shrunk = [f"page {i+1} ({s['fontSize']})" for i, s in enumerate(slides) if s["fontSize"]]
    diagrams = sum(s["mm"] for s in slides)
    print(f"{len(slides)} slides checked; {diagrams} diagram(s); {len(errors)} console error(s)")
    if shrunk: print("autofit reduced text on: " + ", ".join(shrunk))
    if problems:
        print("PROBLEMS:"); [print("  - " + x) for x in problems]; sys.exit(1)
    print("All checks passed.")

if __name__ == "__main__":
    main()
