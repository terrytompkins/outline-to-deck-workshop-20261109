# SmartArt-Style Layouts for Outline-to-Deck: Design Exploration

Nov 10, 2026 · @Terry Tompkins

## Context

The proposal: add a SmartArt-style **Layouts** tag family to the outline-to-deck workshop, so an outline tag like "Vertical action list" becomes a designed visual in the Reveal.js deck. The more PowerPoint-like features the builder offers, the easier adoption gets.

- **Repo:** [terrytompkins/outline-to-deck-workshop-20261109](https://github.com/terrytompkins/outline-to-deck-workshop-20261109) (public)
- **How it works today:** a Claude Project with knowledge files and an instruction prompt runs two phases. Phase 1 builds a tagged Markdown outline (OUTLINE.md). Phase 2 compiles the approved outline into one self-contained Reveal.js HTML deck.
- **Key files:** `PROJECT-INSTRUCTIONS.md`, `knowledge/OUTLINE-CONVENTIONS.md` (tags), `knowledge/DECK-BUILD-SPEC.md` (Phase 2 rules), `knowledge/styles/STYLE-*.md` (swappable style guides), `tools/check-deck.py` (verification).

The existing design already has the seams a layout layer needs:

- **A closed tag vocabulary.** Every tag is either rendered or stripped, never left to judgment; unknown tags stop the build for that slide.
- **Style guides own rendering.** Callouts (`> [!TIP]`) and slide types (`[Quick check]`) are declared per style guide with required fields, frequency limits and proposal rules.
- **Mermaid passthrough.** Fenced `mermaid` blocks render as diagrams (pinned mermaid 11.12.0 from cdnjs), with emphasis classes such as `key`, `good`, `warn` supplied by the style guide's `classDef` lines.
- **Inline SVG already allowed.** `Suggested visual:` tells Phase 2 to design an inline SVG.
- **A checker.** `tools/check-deck.py` verifies visibility, overflow, footer collision, diagram rendering, console errors and tag leakage.

## What SmartArt is, and the core design principle

The principle: **authors write bullets, not diagram code.** A tag picks the layout; Phase 2 compiles the bullets into whichever renderer fits.

SmartArt breaks down into four parts, and each one maps onto the workshop:

| SmartArt part | What it does in PowerPoint | Outline-to-deck equivalent |
| --- | --- | --- |
| Layout with meaning | List, process, cycle, hierarchy, relationship, matrix, pyramid | A layout tag naming the layout |
| Bullet text as data | You type bullets in the text pane; the layout arranges them | Nested Markdown bullets under the tag |
| Theme-driven styling | Colors and shapes follow the deck theme | Layout tokens in the active STYLE-\*.md guide |
| "Convert to SmartArt" | One click turns existing bullets into a layout | Proposal rules: in Phase 1, Claude suggests a layout when bullets fit one |

Why bullets in, layout out:

- The outline stays readable as an outline, and on GitHub.
- Switching layouts means editing one tag, not rewriting diagram source.
- Mermaid, HTML/CSS or SVG becomes an implementation detail of Phase 2.
- The outline remains the single source of truth, which PowerPoint SmartArt cannot offer.

The proposal rules are probably the biggest adoption lever. Claude noticing five sequential bullets and suggesting a Process layout is the "Convert to SmartArt" experience, and it may matter more than the visuals themselves.

## Renderer strategy: HTML first, Mermaid where it's strong, SVG for geometry

Mermaid is the wrong tool for most of the SmartArt gallery. The most-used layouts, lists and processes, render better as HTML/CSS built from style-guide tokens.

Why HTML/CSS wins for list-type layouts:

- Text stays sharp, selectable and accessible.
- It works with the existing autofit logic (0.62em floor) instead of scaling as one SVG block.
- **Reveal fragments give SmartArt's "one by one" build animation** for free.
- No new dependency: flexbox, grid and CSS `clip-path` cover lists, processes, chevrons and matrices.

| Layout family | PowerPoint examples | Best renderer |
| --- | --- | --- |
| Vertical / action list | Vertical Bullet List, Vertical Box List | HTML/CSS |
| Process | Basic Process, Basic Chevron Process | HTML/CSS (`clip-path` for chevrons) |
| Timeline | Basic Timeline | HTML/CSS; Mermaid `timeline` as an alternative |
| Comparison | Two/three columns, pros and cons | HTML/CSS grid |
| Hierarchy | Organization Chart, Hierarchy | Mermaid `flowchart TD` |
| Mind map / radial | Radial List | Mermaid `mindmap` |
| Matrix | Basic Matrix (2x2) | CSS grid; Mermaid `quadrantChart` when items have positions |
| Cycle | Basic Cycle | Generated inline SVG (Mermaid cycles look awkward) |
| Pyramid / funnel | Basic Pyramid, Funnel | Inline SVG or CSS |
| Venn | Basic Venn | Inline SVG |

Framing for the workshop: "SmartArt-style layouts, rendered with HTML first, Mermaid where it's strong, SVG for the geometric shapes." The build spec already permits inline SVG via `Suggested visual:`, so nothing here adds a dependency beyond the pinned Mermaid script.

## Outline syntax

Recommendation: a **fenced `layout` block**, following the existing Mermaid precedent. It keeps the square-bracket vocabulary clean and binds the tag tightly to the bullets it governs.

**Option A (recommended): fenced block**

````markdown
### 4.2 Rolling out the presentation builder

```layout vertical-action-list
- Pilot: two teams build a real deck
  - Collect friction points
- Template: publish the IDEXX style guide
- Train: run a workshop session
- Scale: open it to the org
```

Speaker notes: Each step is gated on the one before it.
````

- The info string names the layout (`layout vertical-action-list`).
- Contents are plain nested bullets; `Label: detail` splits a bold label from body text.
- On GitHub it shows as a code block, which is acceptable; the deck is what matters.
- A slide can hold more than one layout block if the catalog's limits allow.

**Option B: heading-level tag**

```markdown
### 4.2 [Layout: Process] Rolling out the presentation builder

Main points:
- Pilot
- Template
- Train
- Scale
```

- Reads more like "Convert to SmartArt": the bullets are already there, the tag restyles them.
- Drawbacks: one layout per slide, the tag sits apart from the bullets it governs, and it collides with the existing rule of at most one slide-type tag per heading.

Either way, the rules mirror the existing tag families: an unknown layout name, or bullets in the wrong shape for that layout, stops the build for that slide and is reported. Nothing is guessed.

## Changes to the repo

One new knowledge file plus small additions to four existing files.

### New: `knowledge/LAYOUTS.md` (style-independent catalog)

Each layout entry defines what the layout means and accepts. Style guides only decide how it looks.

| Field | Purpose | Example (Process) |
| --- | --- | --- |
| Name | Tag value used in the outline | `process` |
| PowerPoint equivalent | Helps PowerPoint users find it | Basic Process, Basic Chevron Process |
| Data shape | What bullets it accepts | Flat list; optional one level of sub-bullets |
| Item limits | Min/max items and label length | 3–7 steps; labels ≤ 4 words |
| Renderer | HTML/CSS, Mermaid or SVG | HTML/CSS with `clip-path` chevrons |
| Fallback | Layout to use if limits are exceeded | `vertical-action-list` |
| Build animation | Whether items reveal one by one | Reveal fragments, one per step |
| Proposal rule | When Claude suggests it in Phase 1 | 3–7 bullets that describe ordered steps |

Candidate data shapes to standardize: flat list; list with one level of sub-bullets; label/detail pairs; tree (hierarchy); 2x2 (four labeled quadrants).

### Existing files

- **`knowledge/styles/STYLE-*.md`:** add layout tokens (fills, connector color, chevron shape, emphasis), the same way they supply Mermaid `classDef` lines today. Switching styles restyles every layout, just as SmartArt follows the theme.
- **`knowledge/OUTLINE-CONVENTIONS.md`:** add a row to the tag-family table (Layouts → own block → Rendered per LAYOUTS.md), a short section on the fenced `layout` block, and the unknown-layout / wrong-shape stop rule.
- **`knowledge/DECK-BUILD-SPEC.md`:** add a fixed class name for layout containers (e.g. `.layout` plus `.layout-<name>`), the renderer choice per layout, and how layouts interact with autofit.
- **`tools/check-deck.py`:** add checks that every layout block rendered and that no item labels were truncated.
- **`PROJECT-INSTRUCTIONS.md`:** list LAYOUTS.md among the knowledge files.

## Risks and open questions

Strict item and label limits in the catalog matter more than the choice of renderer.

| Risk | Why it matters | Mitigation |
| --- | --- | --- |
| Mermaid layout control is limited | No fixed node sizes or reliable wrap points; long labels break hierarchy diagrams | Tight label-length limits; HTML/SVG for anything geometric |
| Autofit interaction | HTML layouts follow the 0.62em floor; Mermaid and SVG scale as a whole | Rule: split the slide into a "(continued)" slide before shrinking a layout |
| No direct manipulation | Users can't drag boxes as in PowerPoint | Position it as a feature: the outline is the source of truth |
| Mermaid in hidden slides | Already a known pitfall (build spec §4.3) | Reuse the lazy-render-on-`slidechanged` pattern |
| Style-guide drift | Each style guide needs tokens for every layout | Neutral defaults in STYLE-NEUTRAL.md; guides override only what they change |

Open questions:

- [ ] Fenced block (Option A) or heading tag (Option B), or support both?
- [ ] Should layouts count toward a style guide's frequency limits, like callouts do?
- [ ] Is build animation on by default, or opt-in per layout block?
- [ ] How should a layout name be spelled: kebab-case (`vertical-action-list`) or PowerPoint's names (`Vertical Action List`)?

## First slice and next steps

Start with four layouts that cover most real use and exercise all three renderers' trade-offs, then test the bullets-in, layout-out contract on the field-guide demo before cataloging the rest.

| Layout | Renderer | Why it's in the first slice |
| --- | --- | --- |
| Vertical action list | HTML/CSS | Most common SmartArt use; tests label/detail pairs and fragments |
| Process / chevron | HTML/CSS | Tests `clip-path` shapes and the fallback rule |
| Hierarchy | Mermaid `flowchart TD` | Tests tree-shaped bullets and Mermaid label limits |
| 2x2 matrix | CSS grid | Tests a fixed-position data shape |

Next steps:

1. Draft `knowledge/LAYOUTS.md` with the four entries, including data shape, limits, fallback and proposal rule for each.
2. Add layout tokens for the four layouts to `STYLE-FIELD-GUIDE.md` (and neutral defaults to `STYLE-NEUTRAL.md`).
3. Update `OUTLINE-CONVENTIONS.md` and `DECK-BUILD-SPEC.md` with the new tag family and class names.
4. Add one sample slide per layout to `examples/field-guide-demo/OUTLINE.md` and rebuild `deck.html`.
5. Extend `tools/check-deck.py` with the layout checks and run it on the demo deck.
6. Test the proposal rules: give Phase 1 an outline with plain bullets and see whether Claude suggests the right layouts.
7. Decide whether to catalog the remaining families (timeline, comparison, mind map, cycle, pyramid/funnel, Venn).
