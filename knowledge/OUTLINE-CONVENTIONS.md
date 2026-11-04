# OUTLINE CONVENTIONS

How OUTLINE.md is structured and tagged, and exactly what Phase 2 does with each tag. The outline is written to map directly onto the deck, so every rule here has a matching rule in Phase 2: a tag is either **rendered** or **stripped**, never left to judgment.

## 1. Structure

- **Stable hierarchical numbering** (1, 1.1, 1.1.1). Numbers are IDs, not slide order. Restructuring v0.1 may renumber; **from v0.2 onward numbering is frozen**: new sections get the next unused number and the time plan places them. Reference sections by number across chats ("change 4.2").
- **Top-level section (`## 3. Title`)** = one topic = one **horizontal** slide. Its "Main points" state the topic's essentials, so walking only the top-level slides gives a complete introduction.
- **Subsection (`### 3.1 Title`)** = one **vertical** slide beneath its topic: examples, detail, exercises.
- **Sub-subsection (`#### 3.1.1 Title`)** = another vertical slide, placed right after its parent. Reveal.js has only two dimensions.
- **Time plan table** gives live order, minutes (Full = everything in the section; Live = time in the session), and priority. It drives the agenda order and the Phase 2 build order.
- **Front matter** section: title, series name, framing line, agenda.
- **Header lines** at the top of the outline (title line, status comment, `**Status:**`, `**Session:**`, `**Facts verified:**`) and the **Central message** section are outline-only and stripped. The central message may be reused in the title slide's speaker notes.
- **`Main points:`** is a label for the horizontal slide's body; the label is stripped and its bullets become the slide.

## 2. Tag families at a glance

| Family | Examples | Where it goes | Phase 2 |
|---|---|---|---|
| Working aids | `[Seed]`, `[Research]`, `[All]`, `[Core]`, Coverage gaps | End of a heading or bullet; whole outline-only sections | **Stripped** |
| Content markers | `Speaker notes:`, `As of …`, `[UNVERIFIED]`, `[TBD: …]`, source links | Inside bullets | **Rendered** by every style guide |
| Base slide type | `[Try it yourself]` | In a heading | **Rendered** by every style guide |
| Visual directives | `Suggested visual:`, fenced `mermaid` block | Own bullet or block | **Rendered** as a designed visual |
| Style callouts | `> [!TIP]`, `> [!WATCHOUT]` | Block quote inside a slide | **Rendered** per the active style guide |
| Style slide types | `[Quick check]`, `[Recap]` | In a heading | **Rendered** per the active style guide |

Square brackets are a closed vocabulary: only the tags in this file, the active style guide, and `[TBD: …]` placeholders. Markdown links (`[text](url)`) are fine. Anything else in square brackets is a mistake to fix.

## 3. Working aids (outline only; always stripped)

- **Origin:** `[Seed]` (from seed inputs or the presenter's direct input), `[Research]` (from Claude's research), or both. If a revision comes back mostly `[Seed]`, research is too thin.
- **Audience:** the tags listed in BRIEF.md, e.g., `[All]`, `[Technical]`, `[Leadership/Business]`.
- **Priority:** `[Core]`, `[Brief]`, `[Self-guided]`, normally recorded in the time plan. In Phase 2, Self-guided sections get a small "self-guided" label in the agenda; the tag itself is stripped.
- **Outline-only sections**, marked "(outline-only working aid)" in the heading: Changes by version, Time plan, Source reconciliation, Coverage gaps. None of these appear in the deck. A heading carrying that marker is always stripped, whatever its name.
- **Every revision includes a Coverage gaps note**: what is missing or thin, and the research that would fill it.

## 4. Content markers (rendered by every style guide)

| Marker | Phase 2 rendering |
|---|---|
| `Speaker notes: text` (as a paragraph or a bullet) | `<aside class="notes">`; never visible on the slide |
| `As of October 18, 2026` | Footer "As of" label on that slide |
| `([Source title](url))` | Footer source link on that slide |
| `[UNVERIFIED]` or `[UNVERIFIED: reason]` | Small visible tag beside the claim; the reason goes to speaker notes |
| `[TBD: description]` | Visible placeholder chip showing the description. Never replaced with invented data. |

## 5. Base slide type: `[Try it yourself]`

`### 4.5 [Try it yourself] Rewrite a vague request`

Required fields, so the slide works self-guided on a hosted deck:
- `Time:` minutes needed
- `Steps:` numbered, each a single action
- `Expected outcome:` what the attendee should see or learn

Phase 2: a consistent badge (top-right by default; the style guide may restyle it), numbered steps, and an outcome panel. A missing field is reported, not invented.

## 6. Visual directives

- `Suggested visual: description` tells Phase 2 to design an inline SVG chart, diagram, or icon set from the description. Charts must use real numbers from the outline; conceptual shapes are captioned "Illustrative, not measured data."
- A fenced `mermaid` block is passed through as a diagram:

  ````
  ```mermaid
  flowchart LR
    A[Draft outline] --> B{Approved?}
    B -->|No| A
    B -->|Yes| C[Build deck]
  ```
  ````

  Keep diagrams to about seven nodes; anything bigger belongs on its own slide. To emphasize nodes, use a class name the style guide defines (`class B key`); the build adds that guide's `classDef` lines.

## 7. Style tags (defined by the active style guide)

The style guide named in BRIEF.md declares its own tags in two kinds. Each declaration includes a rendering rule, required fields, a frequency limit, and a **proposal rule** that tells Claude when to add the tag during Phase 1.

### 7.1 Callouts (inside a slide)

Use GitHub alert syntax, a block quote whose first line is the type:

```markdown
> [!TIP]
> Ask for the length you need: "bullet summary, under 200 words."

> [!WATCHOUT] Don't skip the gate
> Phase 2 starts only after the approval is recorded.
```

- The type is uppercase with no spaces (`TIP`, `UNDERTHEHOOD`).
- Text after the type on the first line is an optional title. Otherwise the style guide's default label is used.
- GitHub itself renders five types (NOTE, TIP, IMPORTANT, WARNING, CAUTION) as of November 2, 2026; other types appear on GitHub as a plain quote, which is fine. The deck is what matters.

### 7.2 Slide types (whole slide)

Put the tag in the heading, before the title, like `[Try it yourself]`:

```markdown
### 2.4 [Quick check] Which costs more?
```

At most one slide-type tag per heading. The style guide lists each type's required fields (for example, a quick check needs `Question:` and `Answer:`).

### 7.3 Rules that apply to every style guide
- A style tag is **known** if the active style guide declares it or lists it in its fallback table; fallback-mapped tags render as the table says. Any other tag is **unknown**. If the presenter switches style guides, Claude lists the outline's unknown tags under the new guide and proposes a mapping before Phase 2.
- Respect the guide's frequency limits (for example, one callout per slide). Callouts lose their effect when every slide has one. A limit "per section" means per top-level section, including its vertical slides.
- When Claude adds a style tag in Phase 1, it says so in its summary of changes, so the presenter can accept or remove it.
- In Phase 2, an unknown tag or a missing required field stops the build for that slide and is reported. Nothing is guessed.

## 8. Example

```markdown
## 3. Why code reviews stall [All] [Core]

Main points:
- Large pull requests wait longest for a first review. [Seed] [Research]
- Review guidance recommends small, focused changes. ([Example guide](https://example.com/review-guide)) As of November 2, 2026
- Our median wait for a first review: [TBD: median hours to first review]
- Suggested visual: bar chart of wait time by pull-request size, using the numbers above.

> [!REMEMBER]
> One change per pull request.

Speaker notes: Ask the room how long their oldest open pull request has waited.

### 3.1 [Quick check] Which gets reviewed first?
Question: One 1,200-line pull request, or four 300-line ones?
Answer: Usually the small ones: each is quick to read, so reviewers start sooner.
```

In the deck, the tags `[All]`, `[Core]`, `[Seed]`, and `[Research]` disappear; the source and "As of" move to the footer; the `[TBD]` shows as a placeholder chip; the visual is drawn; the callout becomes a styled Remember box; the speaker note goes to the notes view; and 3.1 becomes a quiz slide whose answer appears on the next click.
