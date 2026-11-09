# STYLE GUIDE: Toons

An original classic-cartoon look. It uses no characters, logos, title cards, or catchphrases from any studio.

## 1. Identity
- **Concept:** a hand-inked Saturday-morning cartoon. Thick black outlines, flat saturated color, hard offset shadows, sunburst and halftone backgrounds. Callouts are speech bubbles, so the audience learns who is "talking" at a glance. The deck can be dense without feeling heavy, because the look carries the fun and the text stays plain.
- **Use for:** internal learning sessions, workshops, team events, any talk where a light tone helps a mostly non-technical audience relax.
- **Avoid for:** executive readouts, customer-facing material, and brand-controlled corporate decks (use the organization's brand guide). Do not use any studio's characters, logos, or catchphrases.

## 2. Tokens

| Token | Value | Use |
|---|---|---|
| `--ink` | `#1A1A1A` | Body text, every outline and hard shadow |
| `--paper` | `#FFF8E7` | Vertical slide background |
| `--yellow` | `#FFD93D` | Top-level slide background, TIP tab, number chips |
| `--yellow-tint` | `#FFF1B0` | TIP panel |
| `--red` | `#D4271F` | Section badges, WATCHOUT tab, bullets, progress bar |
| `--red-tint` | `#FFE3DF` | WATCHOUT panel, Myth cards, `[TBD]` chip |
| `--blue` | `#1B5FC4` | Links on paper, REMEMBER tab, Try it yourself badge |
| `--blue-tint` | `#DCEAFF` | REMEMBER panel, Quick check answer |
| `--purple` | `#6B3FB5` | UNDERTHEHOOD tab |
| `--purple-tint` | `#EDE3FA` | UNDERTHEHOOD panel |
| `--green` | `#17792F` | FIELDNOTE tab, Fact cards, Recap checks |
| `--green-tint` | `#DDF4E3` | FIELDNOTE panel, Fact cards, outcome panel |
| `--orange` | `#FF7A1A` | Cover rays only (decoration, never behind text) |
| `--line` | `#CDBB86` | Table rules |
| `--caption` | `#4A4A4A` | Footer, captions, page number |

- **Type:** headings `"Marker Felt", "Chalkboard SE", "Comic Sans MS", "Comic Neue", system-ui, sans-serif` at 700. Body `"Avenir Next", "Segoe UI", system-ui, sans-serif` at 400, so long text stays plain and readable. Code `ui-monospace, Menlo, Consolas, monospace`.
- **Scale:** base 34px at 1280×720. h2 1.32em, h3 1.05em, body lists 0.7em. Footer, page number, and cue at a fixed 14px. Nothing visible below 14px.
- **Contrast:** white text only on `--red`, `--blue`, `--purple`, `--green`, `--ink`. Ink text on `--yellow`, `--paper`, and every tint. Never white on `--yellow` or `--orange`. Never `--blue` text on `--yellow`. Callout labels use the darker shade of their color on the tint: red `#A3160F`, blue `#12479A`, purple `#54308F`, green `#136B30`, yellow `#7A5200`.
- **Outline and shadow:** every panel, card, badge, and frame has a 3px `--ink` outline and a hard shadow of `4px 4px 0 --ink`. No blur anywhere.

## 3. Base elements
- **Title slide:** `--red` field with sunburst rays (alternating `--red` and `--orange`, a conic gradient). The text sits on one cream card with a 5px ink outline, a 12px hard shadow, and rounded corners. Series name in a `--yellow` pill with an ink outline; title in ink with a `--yellow` hard text shadow; date line in ink.
- **Top-level slide:** `--yellow` background with a faint halftone dot tile in a slightly darker yellow. The heading starts with a **starburst badge**: the section number in white on `--red`, a 12-point star with an ink outline.
- **Vertical slide:** `--paper` background. The heading starts with a small number chip: ink text on `--yellow`, 2.5px ink outline, 2px hard shadow.
- **"More below" cue:** top-right, ink, a down chevron with "More below!".
- **Footer:** bottom-left. "As of" in ink bold, sources in `--caption` with dotted underlines.
- **Page number:** bottom-right, left of the navigation arrows, `--caption`, tabular figures.
- **`[TBD: …]` chip:** dashed `--red` border, `--red-tint` fill, text "TBD: description", red text `#A3160F`.
- **`[UNVERIFIED]` tag:** small grey pill (`#ECECEC`, text `#555555`), "Unverified".
- **`[Try it yourself]`:** top-right badge on `--blue` with a compass icon and white text, 3px ink outline. Time on the line under the heading; steps as a numbered list (red circles with white numbers, joined by a line); the outcome in a `--green-tint` panel labeled "You should see".
- **Tables:** header text `--blue`, 3px ink rule under the header, `--line` row rules.
- **Charts:** series order `--red`, `--blue`, `--yellow` (with ink outline), `--green`, `--purple`. Lines 5px. Axis in ink; gridlines off.
- **Mermaid:** emphasis classes `good`, `warn`, `key`. `theme: 'base'`; `primaryColor #FFFFFF`, `primaryBorderColor #1A1A1A`, `primaryTextColor #1A1A1A`, `lineColor #1A1A1A`. Node outlines 2.5px. Emphasis via `classDef good fill:#DDF4E3,stroke:#1A1A1A`, `classDef warn fill:#FFE3DF,stroke:#1A1A1A`, `classDef key fill:#1B5FC4,stroke:#1A1A1A,color:#FFFFFF`.
- **Embedded frame (`Embed:`):** 4px ink outline, rounded corners, 6px hard shadow.
- **Motion:** none. The only movement is Reveal's own fade between slides and click-to-reveal fragments. A cartoon look needs no animation.

## 4. Callouts
Syntax: `> [!TYPE] optional title`. Rendering for all: a **speech bubble**. A rounded panel with a 3px ink outline and a hard shadow, a colored tab on the left holding the icon, the label (or title) in bold in the dark shade of the callout color, then the text. A small tail points up from the top edge toward the slide's heading, as if the heading is speaking. The tab is part of the panel's shape, not a decorative stripe. On top-level slides the panel is white; on vertical slides it is the tint.

| Type | Default label | Purpose | Proposal rule | Icon | Tab color | Limit |
|---|---|---|---|---|---|---|
| `TIP` | Tip | A shortcut or better way to do something | A practical technique that saves time or effort and stands on its own | Lightbulb | `--yellow`, ink icon | 1 per slide |
| `REMEMBER` | Remember | The one thing to keep from this slide | A slide's single most important takeaway, when the slide has several points | Bookmark | `--blue` | 1 per slide; ≤ 2 per section |
| `WATCHOUT` | Watch out | A hazard, common mistake, or cost trap | A mistake attendees are likely to make, or a consequence that's easy to miss | Warning triangle | `--red` | 1 per slide |
| `UNDERTHEHOOD` | Under the hood | Technical depth that non-technical attendees can skip | Mechanism or detail that explains why, aimed at technical attendees | Gear | `--purple` | 1 per slide |
| `FIELDNOTE` | Field note | A real example, story, or observed result | An anonymized internal example or a published case that grounds an abstract point | Notebook | `--green` | 1 per slide; ≤ 3 per section |

## 5. Slide types

### `[Quick check]`
- **Purpose:** a fast, low-stakes question to the room; keeps attention and tests a key idea.
- **Proposal rule:** one after a section's key concept, when there's a common misconception or a surprising answer.
- **Required fields:** `Question:`, `Answer:`. Optional `Options:` followed by 2–4 bullets.
- **Rendering:** a "Quick check" label in `--blue` with a question-mark icon; the question large; options as outlined cards with a hard shadow; the answer in a `--blue-tint` outlined panel that appears on the next click (Reveal fragment). Speaker notes get "Pause for answers before revealing."
- **Limit:** 1 per section.

### `[Myth vs fact]`
- **Purpose:** correct common misconceptions directly.
- **Proposal rule:** when research or seeds surface beliefs the audience likely holds that are wrong.
- **Required fields:** one or more `Myth:` / `Fact:` line pairs (at most 3).
- **Rendering:** two columns. Myths in `--red-tint` outlined cards marked with an ×; facts in `--green-tint` outlined cards marked with a ✓. Each fact appears on a click.
- **Limit:** 2 per deck.

### `[Recap]`
- **Purpose:** a two-minute recap closing a section.
- **Proposal rule:** the last vertical slide of a Core section with four or more subsections.
- **Required fields:** `Points:` followed by 3 bullets (at most 4).
- **Rendering:** label "Quick recap"; points as a checklist with `--green` check icons; a footer line "Up next: [next section title]" generated from the time plan.
- **Limit:** 1 per section.

### `[Try it yourself]` (base type)
Rendered as described in §3.

## 6. Frequency and balance
- At most one callout per slide; a slide-type slide carries no callouts.
- Across the deck, at least half the vertical slides have no callout.
- Don't put WATCHOUT on two consecutive slides; it stops reading as a warning.
- Bubbles and hard shadows carry the style. When every slide has a bubble, none of them stand out.

## 7. Fallbacks for tags from other guides
| Tag | Render as |
|---|---|
| `[!NOTE]` | REMEMBER |
| `[!IMPORTANT]` | REMEMBER |
| `[!WARNING]`, `[!CAUTION]` | WATCHOUT |

## 8. Don'ts
- No studio characters, logos, title cards, or catchphrases, and no look-alikes of them (no "That's all folks", no ring-and-rabbit title card).
- No stock photos or clip art; icons are simple line drawings in one stroke weight.
- No blur, gradients (except the cover's rays), or soft shadows. Shadows are hard and offset.
- No animation, wiggle, or bounce. Motion is left out on purpose.
- Don't use the comic heading font for body text, tables, or footers. It stays on headings, badges, and labels.
- Don't color body text with callout colors; color identifies callout type only.
