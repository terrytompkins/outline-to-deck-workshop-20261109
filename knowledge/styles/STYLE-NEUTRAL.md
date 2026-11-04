# STYLE GUIDE: Neutral

A minimal, brand-free starting point. It uses only GitHub's standard alert types, so an outline written for it reads cleanly on GitHub as well.

## 1. Identity
- **Concept:** clean and quiet; content carries the deck.
- **Use for:** any talk without a brand requirement; a base to copy when creating an organization's brand guide.

## 2. Tokens

| Token | Value | Use |
|---|---|---|
| `--ink` | `#1F2933` | Body text |
| `--primary` | `#3B5BDB` | Headings accents, number chips, links |
| `--primary-tint` | `#E8ECFB` | Panels |
| `--surface` | `#FFFFFF` | All slide backgrounds |
| `--line` | `#DDE1E6` | Rules |
| `--caption` | `#5F6B76` | Footer, captions |
| `--amber` / `--amber-tint` | `#B7791F` / `#FDF2DE` | TIP |
| `--red` / `--red-tint` | `#C0392B` / `#FBE7E4` | WARNING |

NOTE uses `--primary` / `--primary-tint`.

- **Type:** `system-ui, -apple-system, "Segoe UI", Roboto, sans-serif` for everything; code `ui-monospace, Menlo, Consolas, monospace`.
- **Scale:** base 34px at 1280×720; h2 1.3em, h3 1.05em, body lists 0.7em. Footer, page number, and cue at a fixed 14px.
- **Contrast:** white text only on `--primary` and `--red`.

## 3. Base elements
- **Title slide:** white, title in `--ink`, a short `--primary` rule above the series name.
- **Top-level slide:** white; number chip in white on `--primary`.
- **Vertical slide:** white; number chip `--primary` on `--primary-tint`.
- **Footer, page number, "more below" cue:** placed as in DECK-BUILD-SPEC.md §2.1, in `--caption`; the cue is a down chevron with "more below".
- **`[TBD: …]`:** dashed `--amber` border chip. **`[UNVERIFIED]`:** `--red-tint` pill.
- **`[Try it yourself]`:** top-right `--primary` badge; outcome in a `--primary-tint` panel.
- **Tables:** header text `--primary`, 2px `--primary` rule under the header, `--line` row rules.
- **Charts:** `--primary`, `#7C93E8`, `--amber`, `--red`.
- **Mermaid:** `theme: 'base'`; `primaryColor #FFFFFF`, `primaryBorderColor #3B5BDB`, `primaryTextColor #1F2933`, `lineColor #5F6B76`. Class `key`: `classDef key fill:#3B5BDB,stroke:#3B5BDB,color:#FFFFFF`.

## 4. Callouts

| Type | Label | Purpose | Proposal rule | Limit |
|---|---|---|---|---|
| `NOTE` | Note | Useful context | Background that helps but isn't essential | 1 per slide |
| `TIP` | Tip | A better way to do something | A practical technique | 1 per slide |
| `WARNING` | Warning | A mistake or risk | Something attendees are likely to get wrong | 1 per slide |

Rendering: a tinted panel with the label in bold in the callout color. No icons.

## 5. Slide types
Only the base `[Try it yourself]`.

## 6. Fallbacks
| Tag | Render as |
|---|---|
| `[!REMEMBER]`, `[!IMPORTANT]`, `[!FIELDNOTE]`, `[!UNDERTHEHOOD]` | NOTE, keeping the original label |
| `[!WATCHOUT]`, `[!CAUTION]` | WARNING |
| `[Quick check]` | A plain vertical slide with the question and options; the answer goes in speaker notes |
| `[Myth vs fact]` | A plain vertical slide listing the myths; the facts go in speaker notes |
| `[Recap]` | A plain vertical slide with the points as a bulleted list |
