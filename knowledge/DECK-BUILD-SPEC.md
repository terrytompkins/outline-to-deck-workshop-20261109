# DECK BUILD SPEC (Phase 2)

Technical rules for turning the approved OUTLINE.md into a Reveal.js deck. The rendering of each tag is defined in OUTLINE-CONVENTIONS.md (base tags) and the active style guide (style tags). This file covers everything else.

## 1. Output

- **One self-contained HTML file**, named in BRIEF.md, that opens from a `file://` URL or any static web server.
- **External scripts only from cdnjs, at pinned versions.** Never "latest" or a major-only version. Known-good pins, used in working decks as of November 2, 2026 (confirm they still resolve before building):
  - `https://cdnjs.cloudflare.com/ajax/libs/reveal.js/5.1.0/reset.css`
  - `https://cdnjs.cloudflare.com/ajax/libs/reveal.js/5.1.0/reveal.min.css`
  - `https://cdnjs.cloudflare.com/ajax/libs/reveal.js/5.1.0/reveal.min.js`
  - `https://cdnjs.cloudflare.com/ajax/libs/reveal.js/5.1.0/plugin/notes/notes.min.js`
  - `https://cdnjs.cloudflare.com/ajax/libs/mermaid/11.12.0/mermaid.min.js` (only if the outline has diagrams)
- **Everything else inline:** CSS, JavaScript, icons and charts as inline SVG, logos as data URIs. No web fonts unless the style guide requires them; use system font stacks with fallbacks.
- **Do not** use Claude's built-in Slides artifact type, PowerPoint, or any other format.

## 2. Mapping from the outline

| Outline | Deck |
|---|---|
| Front matter | Title slide, then agenda slide linking to each top-level section (`#/s3`) in time-plan order |
| `## N. Title` | `<section id="sN">` stack; its first child is the horizontal slide (main points) |
| `### N.M Title`, `#### N.M.K Title` | Further `<section>` children in the same stack, in numeric order |
| Section number | Shown as a number chip in the heading |
| A stack with children | A subtle "more below" cue on its first slide |
| `[Self-guided]` priority in the time plan | A small "self-guided" label beside that section in the agenda |

- **Delimit each topic** with an HTML comment: `<!-- TOPIC 3: Measuring results -->`, so sections can be found and regenerated individually.
- **Keep slides sparse.** If a subsection's text won't fit at the base font size, move detail into speaker notes or split it into a continuation slide titled `3.2 (continued)`. Never shrink text below the autofit floor.
- **Strip** every working-aid tag and outline-only section (OUTLINE-CONVENTIONS.md §3). **Render** every other tag as specified. **Report** unknown tags and missing required fields before building the affected slide.

### 2.1 Base layout and class names
Every style guide may restyle these, but the placement below is the default, and the class names are fixed so `tools/check-deck.py` can find them.

| Element | Class | Default placement |
|---|---|---|
| Footer ("As of", sources) | `footer` | Bottom-left, 56px from the left edge, 22px from the bottom; right edge clear of the page number |
| Page number | `.pgnum` | Bottom-right, about 120px from the right edge so it clears the navigation arrows |
| "More below" cue | `.more` | Top-right of a stack's first slide |
| Try it yourself badge | `.tiy` | Top-right of the slide |
| Speaker notes | `aside.notes` | Not visible |
| Decorative or navigational extras (background art, "next section" lines) | add `.chrome` | Anywhere; excluded from collision checks |

**Fixed sizes for chrome.** Footer, page number, cue, and badge text use fixed pixel sizes (14px or more), not `em`, so autofit never shrinks them below the readable minimum.

## 3. Reveal.js configuration

```js
Reveal.initialize({
  width: 1280, height: 720, margin: 0.04, minScale: 0.2, maxScale: 1.6,
  center: false, hash: true, controls: true, progress: true,
  slideNumber: false,            // page numbers are drawn inside each slide (see §4)
  transition: 'fade', transitionSpeed: 'fast',
  plugins: [ RevealNotes ]
});
```

## 4. Known pitfalls

1. **Never set `position` on `.reveal .slides section`.** Reveal.js positions slides absolutely. A rule like `position: relative` stacks every slide after the first below the viewport: slides look blank, and nothing appears in the console. Anchor footers, badges, and cues with `position: absolute` on the children only.
2. **Reveal's built-in slide number collides with the navigation arrows** (both sit bottom-right). Turn it off and draw a page number inside each slide where the style guide puts it.
3. **Mermaid renders badly inside hidden slides.** Initialize with `startOnLoad: false` and run Mermaid on a slide's diagrams the first time that slide is shown (`ready` and `slidechanged` events). Hide unprocessed `pre.mermaid` blocks so raw diagram source never flashes.
4. **Autofit must account for the footer.** Shrink a slide's content font only until no content element overlaps the footer and nothing overflows, with a floor (0.62em). Exclude footer and `.chrome` elements from the check. Re-run after a diagram renders.
5. **Claude's in-chat file preview doesn't load CDN scripts**, so a correct deck can look broken there. Test in a real browser or with the checker.
6. **Mermaid themes:** use `theme: 'base'` with `themeVariables` from the style guide, and color individual nodes with `classDef` lines inside the diagram source. Appending CSS through `themeCSS` is unreliable.
7. **Slide-level layout rules lose to the generic section rule.** `.reveal .slides section { padding: … }` is more specific than `.reveal .cover`, so write slide-class rules as `.reveal .slides section.cover`. Reveal also sets `display: block` on the current slide, so don't lay out a whole slide with flexbox; use padding, or a flex wrapper inside the slide.

## 5. Build approach

- Assemble the deck with a script: a shared head (CSS, config) and tail (scripts), plus one HTML fragment per topic. Regenerating a section then means replacing one fragment.
- Make changes to an existing deck with exact-string replacements that must match exactly once, so a bad edit fails loudly.
- Generate charts from numbers in the outline, never from estimates. Caption conceptual shapes "Illustrative, not measured data."
- Speaker notes: one `<aside class="notes">` per slide, holding every "Speaker notes:" line for that slide.

## 6. Verification checklist

Run on every slide before calling the deck done. `tools/check-deck.py` automates checks 1–5 and the leaked-text part of 7.

1. **Visible:** each slide's box is inside the viewport when it is the current slide.
2. **No overflow:** content fits the 1280×720 frame.
3. **No footer collision:** no content element overlaps the footer band.
4. **Diagrams rendered:** every `pre.mermaid` produced an SVG.
5. **No console errors** on load or while navigating.
6. **Look at screenshots** (contact sheets of every changed slide): spacing, contrast, truncated labels, callout placement.
7. **Tag audit:** no working-aid tag text (`[Seed]`, `[Research]`, audience or priority tags) appears in visible slide text (a slide that teaches the tags shows them in `code` formatting, which the audit skips); every `[TBD: …]` from the outline appears as a placeholder chip; every `Speaker notes:` line appears in a notes block. Notes may also hold text that a rendering rule adds (an `[UNVERIFIED]` reason, a quick check's "pause" prompt), but nothing else the outline doesn't contain.
8. **No individual names** in visible text or speaker notes, except the presenter on the title slide (if BRIEF.md says so) and authors within source citations.

Report the results as numbers ("142 slides checked; 0 overflow; 0 collisions; 4 of 4 diagrams rendered; 0 console errors") plus any slide that needed an exception.
