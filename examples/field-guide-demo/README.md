# Field Guide demo

A 17-slide deck generated from [`OUTLINE.md`](OUTLINE.md) using [`STYLE-FIELD-GUIDE.md`](../../knowledge/styles/STYLE-FIELD-GUIDE.md). Every Field Guide callout and slide type, and every base content marker, appears at least once, so you can see exactly what each piece of outline metadata turns into. The demo assumes BRIEF.md audience tags `[All]` and `[Technical]`; it has no Self-guided sections.

Open [`deck.html`](deck.html) in a browser (it loads Reveal.js and Mermaid from cdnjs). Use the arrow keys: left and right move between topics, down opens a topic's detail slides. Press **S** for the speaker view, which shows the speaker notes.

## Where each tag lands

| Outline | Kind | Deck page | What you see |
|---|---|---|---|
| Front matter | Structure | 1–2 | Contour-pattern cover; agenda with trail markers linking to each topic |
| `## 1. Why outline first` | Structure | 3 | Horizontal slide on the moss background, trail-marker number, "more on this trail" cue |
| `### 1.1 …` | Structure | 4 | Vertical slide with a number chip |
| `[All]`, `[Core]`, `[Seed]`, `[Research]` | Working aid | — | Stripped everywhere |
| Time plan, Coverage gaps, Source reconciliation | Working aid | — | Not in the deck; the time plan sets agenda order |
| `Speaker notes:` | Content marker | 1, 3, 6, 10 | Speaker view only (press S) |
| `([Title](url))` | Content marker | 3, 7, 13, 16 | Footer source link |
| `As of November 2, 2026` | Content marker | 16 | Footer "As of" label |
| `[TBD: …]` | Content marker | 3 | Dashed placeholder chip |
| `[UNVERIFIED: …]` | Content marker | 4 | "Unverified" pill; the reason is in the speaker notes |
| `Suggested visual:` | Visual directive | 4, 15 | Illustrative line chart with caption; tag-to-slide table |
| ` ```mermaid ` | Visual directive | 8 | Rendered diagram, styled from the theme |
| `> [!REMEMBER]` | Callout | 3 | Blue bookmark callout |
| `> [!FIELDNOTE]` | Callout | 6 | Green notebook callout |
| `> [!TIP]` | Callout | 8 | Yellow lightbulb callout |
| `> [!WATCHOUT]` | Callout | 9, 17 | Orange warning callout |
| `> [!UNDERTHEHOOD]` | Callout | 14 | Slate gear callout |
| `[Myth vs fact]` | Slide type | 5 | Myth cards; each fact appears on a click |
| `[Quick check]` | Slide type | 10 | Question and options; answer appears on a click |
| `[Try it yourself]` | Base slide type | 11 | Compass badge, time, numbered trail of steps, "You should see" panel |
| `[Recap]` | Slide type | 12 | Trail recap checklist with "Next trail" pointer |

## Try a different theme

Point BRIEF.md at `STYLE-NEUTRAL.md` and ask Claude to rebuild the deck. The outline doesn't change. The Neutral guide's fallback table maps the Field Guide callouts to its three standard types and turns quizzes and recaps into plain slides, so you can see how the same metadata degrades gracefully.
