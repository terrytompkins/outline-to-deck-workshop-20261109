# STYLE GUIDE: Field Guide

## 1. Identity
- **Concept:** a trail guide for an unfamiliar subject. Each top-level topic is a trail with a numbered trail marker. A small, consistent set of margin callouts tells the reader what kind of information they're looking at: a tip, something to remember, a hazard, a look under the hood, a real-world field note. The audience learns to read the callouts at a glance, so the deck can be dense without feeling dense.
- **Use for:** teaching sessions, workshops, onboarding, how-to talks; anything attendees will revisit on their own.
- **Avoid for:** executive readouts and brand-controlled corporate decks (use the organization's brand guide).

## 2. Tokens

| Token | Value | Use |
|---|---|---|
| `--ink` | `#1E2B2E` | Body text |
| `--spruce` | `#1F5C4F` | Primary: headings accents, trail markers, links |
| `--spruce-deep` | `#16443A` | Cover and section fields |
| `--moss` | `#E6F0EC` | Tint panels, top-level slide background |
| `--surface` | `#FFFFFF` | Vertical slide background |
| `--line` | `#D5DDD9` | Rules, table borders |
| `--caption` | `#5C6B67` | Footer, captions |
| `--sun` / `--sun-tint` | `#E0A21B` / `#FDF3DC` | TIP |
| `--sky` / `--sky-tint` | `#2F6F9F` / `#E4EEF6` | REMEMBER |
| `--signal` / `--signal-tint` | `#C8501F` / `#FBE6DD` | WATCHOUT |
| `--slate` / `--slate-tint` | `#4B5563` / `#EEF0F3` | UNDERTHEHOOD |
| `--fern` / `--fern-tint` | `#3E7D3A` / `#E7F2E4` | FIELDNOTE, Recap |

- **Type:** headings `"Avenir Next", Avenir, "Segoe UI", system-ui, sans-serif` at 700; body the same stack at 400; code `ui-monospace, Menlo, Consolas, monospace`.
- **Scale:** base 34px at 1280×720. h2 1.32em, h3 1.05em, body lists 0.7em. Footer, page number, and cue at a fixed 14px. Nothing visible below 14px.
- **Contrast:** white text only on `--spruce`, `--spruce-deep`, `--sky`, `--signal`, `--slate`, `--fern`. Never white on `--sun`; use `--ink`.

## 3. Base elements
- **Title slide:** full-bleed `--spruce-deep` with a faint topographic contour pattern (inline SVG, lines in white at 8% opacity). Series name small in `--moss`; title in white; date line in white.
- **Top-level slide:** `--moss` background. The heading starts with a **trail marker**: the section number in white on `--spruce`, in a rounded rectangle with a small notch (like a painted trail blaze).
- **Vertical slide:** white background. The heading starts with a small number chip: `--spruce` text on `--moss`.
- **"More below" cue:** top-right, `--spruce`, a down chevron with "more on this trail".
- **Footer:** bottom-left. "As of" in `--spruce` bold, sources in `--caption` with dotted underlines.
- **Page number:** bottom-right, left of the navigation arrows, `--caption`, tabular figures.
- **`[TBD: …]` chip:** dashed `--signal` border, `--signal-tint` fill, text "TBD: description".
- **`[UNVERIFIED]` tag:** small `--slate-tint` pill, `--slate` text, "Unverified".
- **`[Try it yourself]`:** top-right badge on `--spruce` with a compass icon and white text "Try it yourself". Time on the line under the heading; steps as a numbered trail (circles joined by a line); the outcome in a `--fern-tint` panel labeled "You should see".
- **Tables:** header row text `--spruce`, 2px `--spruce` rule under the header, `--line` row rules.
- **Charts:** series order `--spruce`, `--sky`, `--sun`, `--signal`, `--slate`. Axis labels `--caption`; gridlines off or `--line`.
- **Mermaid:** emphasis classes `good`, `warn`, `key`. `theme: 'base'`; `primaryColor #FFFFFF`, `primaryBorderColor #1F5C4F`, `primaryTextColor #1E2B2E`, `lineColor #5C6B67`. Emphasis via `classDef good fill:#E7F2E4,stroke:#3E7D3A`, `classDef warn fill:#FBE6DD,stroke:#C8501F`, `classDef key fill:#1F5C4F,stroke:#1F5C4F,color:#FFFFFF`.

## 4. Callouts
Syntax: `> [!TYPE] optional title`. Rendering for all: a panel with a colored tab on the left holding the icon, the label (or title) in bold in the callout color, then the text. The tab is part of the panel's shape, not a decorative stripe.

| Type | Default label | Purpose | Proposal rule | Icon | Limit |
|---|---|---|---|---|---|
| `TIP` | Tip | A shortcut or better way to do something | A practical technique that saves time or effort and stands on its own | Lightbulb | 1 per slide |
| `REMEMBER` | Remember | The one thing to keep from this slide | A slide's single most important takeaway, when the slide has several points | Bookmark | 1 per slide; ≤ 2 per section |
| `WATCHOUT` | Watch out | A hazard, common mistake, or cost trap | A mistake attendees are likely to make, or a consequence that's easy to miss | Warning triangle | 1 per slide |
| `UNDERTHEHOOD` | Under the hood | Technical depth that non-technical attendees can skip | Mechanism or detail that explains why, aimed at technical attendees | Gear | 1 per slide |
| `FIELDNOTE` | Field note | A real example, story, or observed result | An anonymized internal example or a published case that grounds an abstract point | Notebook | 1 per slide; ≤ 3 per section |

## 5. Slide types

### `[Quick check]`
- **Purpose:** a fast, low-stakes question to the room; keeps attention and tests a key idea.
- **Proposal rule:** one after a section's key concept, when there's a common misconception or a surprising answer.
- **Required fields:** `Question:`, `Answer:`. Optional `Options:` followed by 2–4 bullets.
- **Rendering:** a "Quick check" label with a question-mark icon; the question large; options as cards; the answer in a `--sky-tint` panel that appears on the next click (Reveal fragment). Speaker notes get "Pause for answers before revealing."
- **Limit:** 1 per section.

### `[Myth vs fact]`
- **Purpose:** correct common misconceptions directly.
- **Proposal rule:** when research or seeds surface beliefs the audience likely holds that are wrong.
- **Required fields:** one or more `Myth:` / `Fact:` line pairs (at most 3).
- **Rendering:** two columns. Myths in `--signal-tint` cards marked with an ×; facts in `--fern-tint` cards marked with a ✓. Each fact appears on a click.
- **Limit:** 2 per deck.

### `[Recap]`
- **Purpose:** a two-minute recap closing a section.
- **Proposal rule:** the last vertical slide of a Core section with four or more subsections.
- **Required fields:** `Points:` followed by 3 bullets (at most 4).
- **Rendering:** label "Trail recap"; points as a checklist with `--fern` check icons; a footer line "Next trail: [next section title]" generated from the time plan.
- **Limit:** 1 per section.

### `[Try it yourself]` (base type)
Rendered as described in §3.

## 6. Frequency and balance
- At most one callout per slide; a slide-type slide carries no callouts.
- Across the deck, at least half the vertical slides have no callout.
- Don't put WATCHOUT on two consecutive slides; it stops reading as a warning.

## 7. Fallbacks for tags from other guides
| Tag | Render as |
|---|---|
| `[!NOTE]` | REMEMBER |
| `[!IMPORTANT]` | REMEMBER |
| `[!WARNING]`, `[!CAUTION]` | WATCHOUT |

## 8. Don'ts
- No stock photos or clip art; icons are simple line drawings in one stroke weight.
- No gradients and no drop shadows on panels.
- Don't color body text with callout colors; color identifies callout type only.
