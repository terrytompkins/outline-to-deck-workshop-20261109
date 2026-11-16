# GUIDED WORKFLOW

How Claude picks a working mode, works out where a presentation stands, and, in guided mode, leads the presenter from idea to finished deck. The rules in WORKFLOW.md, OUTLINE-CONVENTIONS.md and DECK-BUILD-SPEC.md still apply at every step; this file decides the order, when to pause, and when to recommend a fresh chat.

## 1. Two modes

- **Guided.** Claude leads. It works through the steps in section 4 in order, asks the presenter what it needs at each step, pauses at every checkpoint, and says plainly when to start a new chat. The presenter only answers questions, makes decisions and reviews files.
- **Manual.** The presenter leads, using the prompts in PROMPTS.md or their own requests. Claude does exactly the step asked for, writes the state files at its checkpoints, then stops. It may name the next step in one line ("Next: the First outline prompt"), but it never starts that step on its own.

Both modes follow the same rules, write the same files, and respect the same gate (section 3). Only who decides what happens next differs.

### 1.1 Picking the mode at the start of a chat

Decide from the presenter's first message in each chat, checking in this order:

1. **The message names a mode** ("use guided mode", "manual mode, please"): use it.
2. **The message asks for one specific step**, such as any prompt from PROMPTS.md or a scoped request like "revise 4.2": do that step in manual mode, without asking about modes. If BRIEF.md says the working mode is guided, end by offering in one line to carry on in guided mode.
3. **The message is open-ended** ("continue my deck", "let's get started", "hi"): use the working mode in BRIEF.md if it is set, and say so in one line ("Continuing in guided mode. Say 'manual mode' to switch."). If it isn't set, ask once, and do nothing else in that message:

   > Which way would you like to work?
   > - **Guided** (recommended): I'll walk you through each step with questions, pause for your decisions, and tell you when to start a new chat.
   > - **Manual**: you run each step yourself with the prompts in PROMPTS.md.

The presenter can switch modes at any time by saying so. Record the choice in BRIEF.md's **Working mode** field the next time BRIEF.md is written. If BRIEF.md is otherwise complete and won't be written again soon, write it now so later chats don't ask again.

## 2. Where things stand

Before acting on an open-ended request, and at the start of every guided step, read the state files and work out the stage:

| Check, in order | Stage | Next step |
|---|---|---|
| BRIEF.md still has `[TBD: …]` fields | A. Brief | Interview to fill them |
| OUTLINE.md is still the v0.0 starter | B. First outline | Research and write v0.1 |
| Outline v0.1 or later; status says `reviewed: no` | C. Refine | Revise until the presenter is ready for review, then D |
| Outline reviewed; DECISIONS.md has no gate entry | E. Approve | Ask for approval |
| Gate entry present; status says `deck: none` | F. Deck, pass 1 | Build the horizontal slides |
| `deck: pass 1` or `deck: core` | G. Deck, pass 2 | Build or finish the vertical slides |
| `deck: complete` | H. After the build | Changes, style switch, or wrap-up |

The status fields are described in section 6. If the files disagree with each other, or a field is missing (an outline started before these fields existed), work it out from DECISIONS.md and the outline's "Changes by version", and ask if it is still unclear.

Then tell the presenter where things stand in one or two lines before doing anything else, for example: "Where we are: outline v0.3, not yet reviewed. Next: an independent review, which works best in a fresh chat."

"Continue my deck" (or any wording that means the same) works in both modes. In guided mode Claude carries on with the flow; in manual mode it names the next step, does that step only, and stops.

## 3. The gate

No Phase 2 work (slides, HTML, slide-level design, the deck file) happens until DECISIONS.md contains the gate entry `- YYYY-MM-DD · Decided · Outline vX.Y approved; Phase 2 begins.` This holds in both modes and however the request is worded: "continue", "build the deck", "just make a few slides to see how it looks".

If the presenter asks for deck work before the gate entry exists, don't start it. Reply along these lines:

> The outline hasn't been approved yet (current version: v0.4). If you'd like to approve it now, I'll record the decision and we can start on the deck.

If the outline hasn't had its independent review (`reviewed: no`), add one line saying so and offer the review, but leave the choice to the presenter.

**What counts as approval.** The approver named in BRIEF.md says explicitly that they approve a specific version: "Yes, approve v0.4" counts; "looks good" in reply to an unrelated question doesn't. In guided mode Claude asks the question directly ("Do you approve outline v0.4 for the deck?"), so the answer is unambiguous.

**On approval:** add the gate entry to DECISIONS.md, set OUTLINE.md's status to `approved: vX.Y` and phase 2, write both files, confirm the writes by name, then hand off to a fresh chat (section 5).

## 4. Guided steps

Each step lists what Claude does, where it pauses, and what is written. The matching PROMPTS.md prompt is named so the two modes stay in step; that prompt's wording is the definition of the step's work.

### A. Brief (PROMPTS.md 1, Kickoff)
- Interview the presenter to fill every `[TBD: …]` in BRIEF.md, two to four questions at a time, one BRIEF.md section per round. Offer a sensible default where there is one ("Approver: you, unless someone else signs off?").
- For seed inputs, list the files in the project that aren't template files and ask what each one is and how far to trust it. "None" is a fine answer.
- Fill **Working mode** with the mode in use; don't ask about it again.
- **Done when** no `[TBD: …]` fields remain, or the presenter says to leave one open (write "to be decided" in it).
- **Write** BRIEF.md and summarize it in five lines.
- **Pause:** "Next: I'll research the topic and draft outline v0.1. Ready?" The same chat is fine for the next step.

### B. First outline (PROMPTS.md 2)
- If anything in the brief would change the structure and is unclear, ask up to three questions first. Otherwise start.
- Do the work of prompt 2: coverage dimensions, research, v0.1 with time plan, origin tags, Coverage gaps, source reconciliation, and style tags where they fit.
- **Write** OUTLINE.md (v0.1, `reviewed: no`) and DECISIONS.md.
- **Report** the section list with live minutes, the style tags added, the main coverage gaps, and any `[TBD: …]` facts only the presenter can supply.
- **Pause:** ask what to change, and offer to go straight to review if the presenter is happy.

### C. Refine (PROMPTS.md 3)
- Loop: the presenter asks for changes (by section number where possible); Claude applies them, bumps the version, and records each under "Changes by version".
- Along the way, offer the presenter the open `[TBD: …]` facts to confirm, and record confirmed ones under "Facts to present" in DECISIONS.md.
- **Write** at checkpoints: when a round of changes is finished, not after every message.
- **Exit** when the presenter says the outline is ready for review. If the chat has grown long, recommend a fresh chat for the next round.

### D. Independent review (PROMPTS.md 4), fresh chat recommended
- Hand off first (section 5): a fresh chat isn't anchored to the drafting choices and catches more gaps. If the presenter prefers to stay in this chat, do the review here and say once that it may miss more.
- In the review chat, do the work of prompt 4 and propose a ranked change list. **Don't write anything until the presenter approves the list.**
- Apply exactly the approved changes, bump the version, set `reviewed:` to the new version, and **write** the files.
- **Pause:** move to E.

### E. Approve (PROMPTS.md 5)
- Before asking, show in a few lines what approval locks in: the version, the `[TBD: …]` items that will appear as placeholder chips, the number of `[UNVERIFIED]` claims, and any small edits made since the review.
- Ask: "Do you approve outline vX.Y for the deck?" Then follow "On approval" in section 3.
- If the presenter wants more changes instead, go back to C. Small edits after the review don't need a second review; offer one if the structure changed.

### F. Deck, pass 1 (PROMPTS.md 6), fresh chat recommended
- Do the work of prompt 6: confirm the pinned library versions and the style guide, and list any outline item or tag that can't be rendered as specified. Pause only if something needs the presenter's decision.
- Build pass 1 (title, agenda, every horizontal slide), send the file, set `deck: pass 1`, and **write** OUTLINE.md (status fields only; no content changes).
- **Pause:** "Open it in a browser; the in-chat preview can't load the slide library. Tell me what to adjust, or say 'go' for pass 2." Visual adjustments can be made directly. Content changes go through H.

### G. Deck, pass 2 (PROMPTS.md 7), same chat
- Build the vertical slides for the Core sections, send the interim file, and set `deck: core`. Carry on with Brief and Self-guided sections unless the presenter asks to stop there.
- Run the full verification checklist in DECK-BUILD-SPEC.md, report the results as numbers, set `deck: complete`, and **write** OUTLINE.md.
- **Pause:** offer H.

### H. After the build (PROMPTS.md 8 and 9)
- **Content change:** propose it; once the approver agrees, update OUTLINE.md first (bump the version, add a Decided entry), then regenerate only the affected slides, re-run the checks on them, and send the deck.
- **Style switch:** follow prompt 9.
- **Wrap-up:** when the presenter is done, summarize the deck file name, the outline version it was built from, any placeholder chips still showing, and where BRIEF.md says the deck will be hosted.

**The deck file across chats.** The deck is a file in a chat, not a state file. If a Phase 2 step runs in a chat that doesn't have the latest deck file, ask the presenter to attach it. Don't rebuild from scratch unless they ask.

## 5. Pauses and handoffs

- **One thing at a time.** When Claude asks for a decision or information, the message ends there. It doesn't ask and carry on in the same message.
- **Every pause ends with a "Next:" line** saying what Claude will do when the presenter replies.
- **Write before handing off.** The state files must be written (WORKFLOW.md §5) before any handoff. If the writes failed, use the fallback in WORKFLOW.md §5 and say that the next chat will need the Recovery prompt.
- **Handoff message.** Recommend a fresh chat before the review (D) and before Phase 2 (F), and when a chat has grown long. Use this block so it's hard to miss:

  > **Next step: start a new chat.** Everything is saved in the project files.
  > In a new chat in this project, type: **continue my deck**

- **If the presenter stays in the same chat anyway**, carry on. Mention the fresh-chat advice at most once per chat; skipping it costs tokens and some review quality, but nothing breaks.

## 6. Status fields

The status comment at the top of OUTLINE.md carries the stage, so any chat can tell where things stand:

`<!-- status: version 0.3 | phase 1 | last written 2026-11-15 | approved: no | reviewed: no | deck: none -->`

| Field | Values | Set when |
|---|---|---|
| `approved` | `no`, or the approved version (`v0.4`) | The gate entry is recorded |
| `reviewed` | `no`, or the version the review's approved changes produced | Step D's changes are written |
| `deck` | `none`, `pass 1`, `core`, `complete` | Steps F and G finish |

Keep the plain-language `**Status:**` line under the title in step with these fields. Both are outline-only and stripped from the deck.
