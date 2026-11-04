# WORKFLOW

How a presentation moves from seed files to a finished deck, and how progress is kept across chats.

## 1. Why the process looks like this

- **Chats don't share history.** Each chat starts with only the project instructions and knowledge files, so progress must live in files: OUTLINE.md and DECISIONS.md.
- **Content first, deck second.** Text is cheap to write, revise, and re-read; a generated deck is expensive on all three. Iterating on the outline costs a fraction of iterating on slides, and every "redo the deck" pays for the whole deck again.
- **An explicit gate.** Without one, Claude tends to jump to slides early. Phase 2 starts only when DECISIONS.md records approval.

## 2. Setup (once per presentation)

1. Create a Claude Project. Paste PROJECT-INSTRUCTIONS.md into its instructions.
2. Upload the knowledge files: BRIEF.md, OUTLINE.md, DECISIONS.md, WORKFLOW.md, OUTLINE-CONVENTIONS.md, DECK-BUILD-SPEC.md, the style guide you'll use, and any guide it reuses rules from. To switch styles later, upload the new guide too.
3. Upload seed inputs. Condense large or noisy ones first (section 6).
4. In the first chat, ask Claude to interview you and fill in BRIEF.md.

## 3. Phase 1: outline

**Goal:** a comprehensive, structured outline of everything the presentation could cover, more than fits the session. The time plan then picks the live path.

1. **Map the landscape.** Before structuring, Claude checks coverage against BRIEF.md's coverage dimensions and adds any its research turns up.
2. **Research.** Seeds are leads. Claude searches the sources BRIEF.md names, looks for topics the seeds miss, and tags each item `[Seed]`, `[Research]`, or both.
3. **Draft v0.1**, with a time plan, a Coverage gaps note, and a source-reconciliation table.
4. **Iterate** with scoped requests ("revise 4.2; add a subsection under 6 on X"). Each revision bumps the version (v0.2, v0.2.1) and adds a line under "Changes by version".
5. **Add style tags as content settles.** Claude proposes callouts and slide types from the style guide where they fit, and lists what it added.
6. **Fact-check.** The presenter confirms internal facts; Claude records them under "Facts to present" in DECISIONS.md.
7. **Review in a fresh chat** before approval (section 7). A new chat isn't anchored to earlier drafting choices and catches more gaps.
8. **Approve.** The approver says so explicitly; Claude records the gate entry `- YYYY-MM-DD · Decided · Outline vX.Y approved; Phase 2 begins.`.

Versions: OUTLINE.md uses v0.1, v0.2, v0.2.1 and so on; BRIEF.md and DECISIONS.md use a simple revision number. Restructuring v0.1 may renumber sections; from v0.2 onward numbering is frozen, so new sections get the next unused number and the time plan places them.

## 4. Phase 2: deck

Build per DECK-BUILD-SPEC.md. Start in a fresh chat with the approved outline; don't re-research or revise content during the build.

1. **Confirm before writing HTML:** the pinned library versions, the style guide, and any outline item that can't be rendered as specified.
2. **Pass 1:** title, agenda, and every horizontal slide. This is a complete, presentable walk-through on its own.
3. **Pass 2:** vertical slides, in priority order: Core sections first (an interim checkpoint), then Brief, then Self-guided.
4. **Verify every slide** with the checklist in DECK-BUILD-SPEC.md, and look at screenshots before calling it done.
5. **Content changes after approval:** Claude proposes the change; once the approver agrees, Claude bumps the outline version, records a Decided entry (e.g. `Outline v1.1: 4.2 revised after approval`), then regenerates only the affected slides. Phase 2 stays open; no new gate entry is needed.

## 5. Writing the state files

The state files are BRIEF.md, OUTLINE.md, and DECISIONS.md. Claude writes them directly in project knowledge; the presenter should not have to paste anything.

**When to write:** at checkpoints, not after every message. A checkpoint is a finished section or revision, a recorded decision, an approval, or the end of the chat. Each write makes the project reload its knowledge for later messages, so frequent writes waste tokens.

**How to write:**
1. Re-read the file from project knowledge immediately before writing. A long chat may hold an outdated copy, and another chat in the project may have written since.
2. Apply only the intended changes to that latest version.
3. Update the status comment near the top of the file (`<!-- status: … -->`): version or revision, phase, date.
4. Replace the file at its existing path. Never create a copy with a new name.
5. Report what changed, by section number. For a large change, also give a short list the presenter can check.

**Precise edits.** For several edits at once, change exact strings and confirm each one matched exactly once. Edits that match zero or several places should fail loudly rather than land in the wrong spot. Afterward, check for stale version strings, stray names, and broken heading numbers.

**Fallback.** If the chat can't write to project knowledge (tool access can drop mid-chat and can't be fixed in that chat), Claude ends with "Updates for OUTLINE.md" (complete revised sections, ready to paste) and "Updates for DECISIONS.md" (new entries), and says the files were not updated. To recover in a fresh chat, the new chat can use past-chat search to find that message and apply it.

## 6. Seed inputs

- **Trust varies by type.** A practitioner transcript reflects real concerns but may misstate facts. Another LLM's outline gives breadth, but its specific claims need verification. Record each seed's trust level in BRIEF.md.
- **Condense large or noisy inputs** before uploading (an email exported as HTML, a long transcript). A good condensed file has:
  - a header: source type, how to attribute it (generically), and what still needs verification
  - the content, organized as an outline
  - a clearly labeled "Observations" section with your or Claude's notes (strengths, gaps, activity ideas), kept separate from the source content

## 7. Chat hygiene

- **One job per chat.** Start a fresh chat for a review, for Phase 2, or when a chat has grown long. Every message in a long chat resends all of it.
- **Hand off with files, not memory.** Before switching chats, make sure the state files are written.
- **Ask Claude to ask first** on anything substantial: "Before you start, ask me up to three questions whose answers would change the result."

## 8. Lessons from earlier runs

- **Name the presenter.** A first-person prompt ("I am presenting…") makes Claude assume whoever is chatting is the presenter.
- **Say outright that seeds are leads.** Calling inputs "the material" leads Claude to polish them rather than research.
- **Rules that apply across sections get their own section.** Attribution was once silently dropped when a neighboring instruction section was rewritten. When revising instructions, ask for the complete merged text and compare it.
- **Every working-aid tag needs a matching strip rule** in Phase 2, or it leaks onto slides.
- **Follow the change list, not superseded drafts.** When a chat applies a set of edits, it applies exactly the approved list and flags any differences it notices, rather than merging extras.
- **Claude's in-chat file preview can't load CDN scripts,** so a Reveal.js deck that looks broken there may be fine. Test it in a real browser.

## 9. Collaboration (future)

This process is written for a single author. Several people contributing to one outline from their own chats raises problems this version doesn't solve: chats working from stale copies, and simultaneous writes overwriting each other. Several things here are designed so a multi-author version can build on them: stable section IDs, decisions that are only ever added (never edited), and a version line at the top of each state file.
