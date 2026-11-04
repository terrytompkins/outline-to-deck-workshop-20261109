# STYLE GUIDE: [Name]

Copy this file to `STYLE-<NAME>.md`, fill every section, and name it in BRIEF.md. A style guide does two jobs:
1. **Phase 1:** it tells Claude which callout and slide-type tags exist and when to propose each one.
2. **Phase 2:** it tells Claude exactly how to render every base element and every tag.

Anything this file doesn't specify falls back to DECK-BUILD-SPEC.md and OUTLINE-CONVENTIONS.md.

## 1. Identity
- **Concept:** [one sentence: what the deck should feel like and why]
- **Use for:** [kinds of talks this suits]
- **Avoid for:** [kinds it doesn't]

## 2. Tokens
Define as CSS custom properties on `:root`.

| Token | Value | Use |
|---|---|---|
| `--ink` | | Body text |
| `--primary` | | Headings, number chips, links |
| `--primary-tint` | | Panels on white |
| `--surface` | | Content slide background |
| `--surface-alt` | | Top-level slide background (optional) |
| `--line` | | Rules, table borders |
| `--caption` | | Footer, captions (must still pass 4.5:1 on `--surface`) |

- **Type:** heading stack, body stack, monospace stack. System fonts unless a web font is essential.
- **Scale:** base size at 1280×720 (34px is a good default), heading sizes, minimum size (no visible text below 14px).
- **Contrast rule:** body text ≥ 4.5:1; large headings ≥ 3:1. State which text colors are allowed on which fills.

## 3. Base elements
Describe each one: placement, size, color.
- **Title slide:**
- **Top-level (horizontal) slide:** background, heading treatment, number chip
- **Vertical slide:**
- **"More below" cue:**
- **Footer:** "As of" label, source links
- **Page number:**
- **Logo** (if any): file, size, which slides
- **`[TBD: …]` placeholder chip:**
- **`[UNVERIFIED]` tag:**
- **`[Try it yourself]`:** badge, steps, time, outcome panel
- **Tables:**
- **Charts:** series colors in order; axis and gridline treatment
- **Mermaid:** `themeVariables`, plus `classDef` styles for emphasized nodes

## 4. Callouts
Syntax in the outline: `> [!TYPE] optional title`.

| Type | Default label | Purpose | Proposal rule (when Claude adds it in Phase 1) | Rendering | Limit |
|---|---|---|---|---|---|
| `TYPE` | | | | | |

## 5. Slide types
Syntax in the outline: `### N.M [Type name] Title`.

For each slide type:
- **Purpose:**
- **Proposal rule:**
- **Required fields:** (lines in the outline, e.g., `Question:`)
- **Rendering:** (layout; any click-to-reveal fragments)
- **Limit:**

## 6. Frequency and balance
- [e.g., at most one callout per slide; at most N of type X per section]

## 7. Fallbacks for tags from other style guides
| Other guide's tag | Render here as |
|---|---|
| `[!NOTE]` | |

## 8. Don'ts
- [the visual habits that would break this style]
