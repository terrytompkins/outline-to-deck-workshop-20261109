# Prompt script: rebuild the inbox-to-to-do deck

A script for rebuilding this example from scratch in a fresh project, taken from `transcript-inbox-to-todo-deck.md`. Use it to test the project, or as a class exercise.

It has three parts:
1. **Presenter answer sheet:** everything the presenter told Claude in the original run, so you can answer Claude's questions in any order.
2. **Run A, guided mode:** the short version, plus a few deliberate checks of the workflow.
3. **Run B, manual mode:** the original prompt sequence from PROMPTS.md.

## Before you start: what will and won't match

- **Your outline won't match the example's.** Claude researches live, so sources, section numbers, style tags and wording will differ from the original run. Compare at the level of structure: is the 45-minute time plan believable, are all eight coverage dimensions covered, are there hands-on slides, does the deck pass its checks?
- **Claude's questions will come in a different order.** Answer from the sheet below, whatever order they arrive in. If Claude asks something the sheet doesn't cover, accept Claude's suggestion or answer as you see fit.
- **Revision requests are templates.** The original run's revisions named specific sections ("revise section 7"). Your outline will be numbered differently, so the script describes the kind of change to ask for.
- **It takes a while.** The original run took two days, and the chat was long enough that Claude had to compact it. Research and each build pass take several minutes. In a class session, plan to do the brief and the first outline live, and leave the deck build as homework or a demo.

## Setup

1. Create a new Claude Project and paste the project instructions from `PROJECT-INSTRUCTIONS.md` (everything below the line).
2. Upload everything in `knowledge/` except `STYLE-NEUTRAL.md` and `STYLE-GUIDE-TEMPLATE.md`. This deck uses `STYLE-FIELD-GUIDE.md`.
3. Don't upload any seed files. In the original run, all the content came from Claude's research.

## 1. Presenter answer sheet

Use your own name as presenter and approver. The original run used the workshop author's name.

**Event and people**
- Title: Using Claude to Create a ToDo List from Your Inbox
- Event: Learning Day Workshop
- Presenter and approver: you
- Name on the title slide: yes

**Audience**
- Who attends: anyone at IDEXX who wants to learn to use Claude better. A mix of technical and non-technical people, mostly non-technical.
- Audience tags: yes; let Claude choose tags that fit the content (for example `[All]`, `[Technical]`, `[Setup]`).
- What they already know: most have chatted with Claude, and some have used Cowork with Office files. Everyone uses Outlook and Teams. The deck has to cover turning on the connector(s) so Claude can read their inbox.

**Topic and outcomes**
- Topic: using Claude to turn Outlook email, Teams messages and calendar into a prioritized to-do list.
- Why now: workloads are high, and a lot of communication arrives through email and Teams. Anything that helps pull tasks out of that stream helps.
- Outcomes. After the session, attendees can:
  - connect Claude to Outlook, Teams and calendar, within IDEXX's approved settings
  - write a prompt that turns recent email, Teams messages and calendar into a prioritized to-do list
  - check and correct Claude's output before acting on it
  - optionally, repeat the process on a schedule

**Logistics**
- Length: 45 minutes including Q&A. Attendees try it live.
- Target date: November 30, 2026
- Hosting: the internal Artifaxx site; the HTML file can also be handed out directly.

**Seed inputs**
- None. Research the topic and provide the content.

**Research**
- Authoritative sources: Anthropic's official documentation and help center (Claude, connectors, scheduled tasks), and Microsoft's official documentation (Outlook, Teams, Microsoft 365 permissions and admin consent).
- Also acceptable: reputable practitioner write-ups on email triage and task capture, and vendor guidance on prompting for summarization and prioritization.
- Volatile items to verify and date: which connectors exist, which plans or settings enable them, the permissions they request, menu and button names in Claude, scheduling features, and the Microsoft 365 consent flow.
- Coverage dimensions: connector setup and permissions; data privacy and IDEXX policy; prompt design; prioritization methods; verifying output; Teams and calendar as sources; repeating the process on a schedule; common failure modes.
- If asked about internal policy: IDEXX has an approved list of connectors. This presentation covers only the Microsoft 365 connectors (Outlook and Teams). Keep the list and policy details off the slides.
- If asked about connector access: everyone can enable the connector themselves but may need to check it on their own account, so show how to do that in Claude.

**Style and deck**
- Style guide: STYLE-FIELD-GUIDE.md; the Field Guide look is fine for a teaching event.
- Brand overrides: none.
- Callouts: lean on TIP, WATCHOUT (privacy and verification) and REMEMBER; use UNDERTHEHOOD sparingly.
- Deck file name: `inbox-to-todo-workshop.html`
- Attribution: the default (no individual names; published sources cited with links).

**Working mode** (Run A only): guided.

## 2. Run A: guided mode

Each step lists what you type and what to check. Steps marked **Check** test the workflow deliberately and weren't part of the original run.

| # | You type | What should happen |
|---|---|---|
| A1 | `Continue my deck.` | **Check:** Claude asks whether you want guided or manual mode, and nothing else. (The mode isn't in the message or in BRIEF.md yet.) |
| A2 | `Guided.` | Claude starts the brief interview, a few questions at a time. Answer from the sheet. |
| A3 | (answers) | Claude writes BRIEF.md, with **Working mode: guided**, summarizes it in five lines, and asks before it starts the outline. It shouldn't start researching without asking. |
| A4 | `Yes, go ahead.` | Research and outline v0.1. Claude reports the structure, the style tags it added, the coverage gaps and open questions, and asks what to change. |
| A5 | `Let's skip ahead and build the deck now.` | **Check:** Claude refuses to start the deck. It says the outline hasn't been approved (naming v0.1), notes that the review hasn't happened, and offers to record the approval now. |
| A6 | `No, not yet.` Then one revision, for example: `Remove the [UNVERIFIED] claim in section N.` (pick any claim Claude marked) | Claude makes the change, bumps the version to v0.2, records it, and writes the files. If it mentions a knock-on fix (the original run found a stale cross-reference), say `Yes, fix it.` |
| A7 | `I'm ready for the review.` | Claude sets `reviewed: pending` in OUTLINE.md's status comment, writes the files, and shows the "start a new chat" message. |
| A8 | **Check:** ignore the advice once. `Let's just do it here.` | Claude does the review in this chat, says once that a fresh chat might catch more, and doesn't repeat the advice. *(To test the handoff instead, open a new chat and type `Continue my deck.` Claude should say where things stand and start the review.)* |
| A9 | `Approve all.` | Claude applies exactly the proposed changes, bumps the version, marks the outline reviewed, and writes the files. |
| A10 | (Claude asks for approval) `Yes, I approve vX.Y.` | Claude records the gate entry with today's date in YYYY-MM-DD form, updates OUTLINE.md's status, writes both files, and shows the "start a new chat" message. |
| A11 | In a **new chat**: `Continue my deck.` | **Check:** Claude doesn't ask about the mode (BRIEF.md has it). It says the outline is approved and Phase 2 is next, then confirms the library versions and lists anything it can't render. |
| A12 | (if asked) `Go ahead.` | Pass 1 (title, agenda, horizontal slides) is sent, with a reminder to open it in a real browser. |
| A13 | `Go.` | Pass 2: an interim file after the Core sections, then the finished deck and verification results as numbers. |
| A14 | `I'm done.` | Wrap-up: file name, outline version, any placeholder chips left, and where the deck will be hosted. |

**Also check, at any point:** open OUTLINE.md in the project's files and look at the status comment. `approved`, `reviewed` and `deck` should match where you are.

## 3. Run B: manual mode (the original sequence)

These are the prompts from the original run, in order. Apart from the two revisions, they're the PROMPTS.md prompts word for word, so this run works as the step-by-step teaching exercise. Start each prompt in a fresh chat unless it says "same chat".

| # | Prompt | Notes |
|---|---|---|
| B1 | PROMPTS.md **1. Kickoff** | Answer from the sheet. **Check:** Claude stops after the five-line summary and doesn't start the outline. |
| B2 | PROMPTS.md **2. First outline** | The original v0.1 had nine sections, a time plan with 65 minutes of full content and 45 live, three hands-on slides, and a few `[TBD]` items for internal facts. |
| B3 | Same chat: `Revise section N: remove the unverified point about [claim].` | The original removed a claim it couldn't verify (whether Teams chat tools work inside scheduled tasks). Pick any `[UNVERIFIED]` item in your outline. |
| B4 | Same chat: `Please fix the [cross-reference or inconsistency] you mentioned.` | Only if Claude points one out. The original fixed a "see 3.3" reference that should have said "see section 3". |
| B5 | PROMPTS.md **4. Independent review** | The original returned 8 gaps, 6 style-tag flags and 10 claim issues. |
| B6 | Same chat: `Approve all.` | Claude applies the changes as the next version and marks the outline reviewed. |
| B7 | PROMPTS.md **5. Approve**, using today's date as YYYY-MM-DD | The original typed 11/09/2026, and Claude corrected it to the required format. |
| B8 | PROMPTS.md **6. Start Phase 2** | Fresh chat. |
| B9 | Same chat: PROMPTS.md **7. Phase 2, pass 2** | The original deck has 52 slides. |

## 4. Comparing with the example

Open `inbox-to-todo-workshop.html` (the finished original) and `interim-core.html` (its interim file after the Core sections) in a browser next to your deck. Expect the same kind of deck, not the same deck. Things worth comparing:
- the hands-on slides and whether their steps work in your own Claude account
- how each deck handles volatile facts (menu names, connector settings) and their "As of" dates
- the placeholder chips each one left for internal facts
- whether your guided run reached a comparable deck with fewer prompts
