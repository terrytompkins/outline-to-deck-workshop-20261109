# DECISIONS

<!-- status: revision 5 | phase 2 (test) | last written 2026-11-08 -->

A dated log of decisions about scope, audience, content, and design. Respect every *Decided* entry; if a request conflicts with one, say so before proceeding.

**Entry format:** `- YYYY-MM-DD · Decided · text` or `- YYYY-MM-DD · Proposed · text`

**Rules**
- **Proposed** entries are Claude's suggestions. They become **Decided** only when the approver named in BRIEF.md says so; Claude then adds a new Decided line rather than editing the Proposed one.
- Claude records a decision as **Decided** only when the approver states it explicitly in a chat.
- Only the approver opens Phase 2. The gate entry reads exactly (with the real date and version):
  `- YYYY-MM-DD · Decided · Outline vX.Y approved; Phase 2 begins.`
- Content changes after approval are recorded as new Decided entries before the affected slides are rebuilt, e.g. `- YYYY-MM-DD · Decided · Outline v1.1: 4.2 revised after approval.`
- Never edit or delete an old entry. To change a decision, add a new entry that names what it replaces: `(supersedes YYYY-MM-DD: short quote)`.
- Keep entries to one line. Put reasoning in the outline's speaker notes or source-reconciliation table, not here.

## Status
- 2026-11-05 · Decided · Phase 1 in progress; outline not yet approved.
- 2026-11-05 · Decided · Test run: Suzanne Edwards approves v0.1 only to test Phase 2, on branch test/phase2-v0.1. This is not the real approval.
- 2026-11-05 · Decided · Outline v0.1 approved; Phase 2 begins.

## Scope and audience
- 2026-11-05 · Proposed · Live path is sections 1–7 in 30 minutes, plus 5 minutes of Q&A; sections 5 and 6 get 2 minutes each.
- 2026-11-05 · Proposed · Both Try it yourself activities (4.4, 7.1) are self-guided, not done live.

## Content
- 2026-11-05 · Proposed · Teach outline-first as independent of the output tool; Phase 2 stays Reveal.js, with Claude Slides named as an alternative.
- 2026-11-05 · Proposed · Why now: Claude can now build a deck in any conversation (release notes, September 16, 2026); this method makes it the deck you want.
- 2026-11-05 · Proposed · Use the earlier internal token-spend talk as the worked example, described generically.
- 2026-11-05 · Decided · Outline v0.2: 4.3 shows the demo deck in a live frame, with a text fallback (test branch only).

## Style and design
- 2026-11-08 · Decided · Style: Toons (STYLE-TOONS.md), an original cartoon look with no studio characters or logos; built as outline-first-toons.html on branch test/style-toons (test branch only).

## Facts to present
Confirmed facts the presenter supplied (internal settings, dates, numbers), so later chats don't ask again.

## Internal only (never on slides)
Context Claude needs but must not put in the outline or deck.
- The template repository is private to the presenters; don't link it on slides until a share location is decided.
