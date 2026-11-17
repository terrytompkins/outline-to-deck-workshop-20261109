# Transcript: planning guided mode, the prompt script, and skills vs. projects

Chat of November 15, 2026, working in the `outline-to-deck-workshop-20261109` folder ahead of the Promptly-at-9 follow-up session.

**Conventions:** user messages and Claude's replies are in full. Tool calls appear as one-line summaries; tool results are omitted. Hidden reasoning and system context are omitted. Quotations from web sources are marked with their source link.

## Summary

**Decisions**
- Build the guided-mode orchestration first, SmartArt-style layouts second (design in `docs/SmartArt-style-layouts-for-outline-to-deck-design.md`).
- Keep the current project structure (instructions + knowledge files). Moving to an installable plugin and/or skills is a later discussion.
- Two working modes, **guided** and **manual**. "Continue my deck" works in both and never crosses the approval gate.

**Files created or changed in this chat**
- New: `knowledge/GUIDED-WORKFLOW.md`, `examples/outlook-to-todo/PROMPT-SCRIPT.md`, this transcript.
- Changed: `PROJECT-INSTRUCTIONS.md`, `PROMPTS.md`, `README.md`, `knowledge/WORKFLOW.md`, `knowledge/BRIEF.md`, `knowledge/OUTLINE.md`.
- Not committed to git.

**Open follow-ups**
- Terry tests the full guided and manual runs on November 16, in separate projects, and reports issues.
- Promptly-at-9 (November 17): do the brief, first outline and approval-gate check live; leave the deck build as homework or a demo.
- Optionally export the original test project's final BRIEF.md and OUTLINE.md into `examples/outlook-to-todo/`.
- Later: restructure into skill(s) + project template (see the last two exchanges), then the SmartArt layouts.

---

## User message 1

We will be working with the project directory i have shared here called outline-to-deck-workshop-20261109".  I conducted the workshop last week and I will be hosting a follow up session in my regular "Promptly-at-9" class this coming tuesday.  I had about 40 people out of the 600 who attended my workshop who requested some follow up help trying to run the prompts I gave them after we setup the Claude project for creating a deck from an outline.  The file from the workspace they used was PROMPTS.md.  After running the series of prompts to create a few decks myself, I noticed a couple of opportunities for improvement.  First, sometimes Claude would run with the first ("1. Kickoff: fill in the brief") prompt and start working on interviewing the user for developing the outline before I (or the users) got a chance to issue the second prompt ("2. First outline").  It was also easy to miss the new-chat transition step from phase 1 to phase 2.  I did this myself accidentally, which put everything in one long chat.  It worked fine, but that miss confused the users.  

I would like to move from the series of individual prompts in PROMPTS.md to a Claude-managed interview workflow.  This will help us productionalize this process to move it from just a learning exercise to a useful tool.  Normally, we would use a skill for something like this, but since we have a project with an instruction prompt and a whole series of knowledge files which help guide the whole process, I'm fine with just adding a single prompt (or skill within the Project structure if that's possible) to orchestrate all of the individual steps in the PROMPTS.md file.  In fact, I'd like to keep the PROMPTS.md file as a document in the project so that I can teach people the individual steps, but when not teaching, I'd like the entire process to be a smooth series of interview questions and instructions from Claude that takes the user from idea to outline to completed, styled Reveal.js deck.

In addition to this enhancement, I have a new feature that I would like to add that will help recreate the capability of displaying data that PowerPoint has called "SmartArt".  I previously worked with Claude to start designing this and you can review that design content in docs/SmartArt-style-layouts-for-outline-to-deck-design.md.

One question is: should we first work on turning the individual prompts into a skill or other mechanism for an orchestrated workflow as described above, or should we work on adding the SmartArt capability first and then the process orchestration?

### Claude

I'll look through the project folder, PROMPTS.md and the SmartArt design doc before answering.

> 🔧 **device_list_dir**: project folder (recursive)
> 🔧 **device_stage_files**: PROMPTS.md, PROJECT-INSTRUCTIONS.md, README.md, the SmartArt design doc, and the knowledge files
> 🔧 **Bash**: print the key project files
> 🔧 **WebSearch**: Claude Projects skills project-level skill support

I'd do the orchestration first and add SmartArt after it. The two barely touch each other, so the order mostly comes down to timing and risk.

**Why orchestration first**

- **It's what Tuesday's group needs.** The 40 people asking for help got stuck on the process: Claude running ahead after the Kickoff prompt, and the missed new-chat step. Neither is a SmartArt issue. Fixing the workflow lets you demo the fix to the people who hit the problems. SmartArt still has four open questions in your design doc (fenced block or heading tag, frequency limits, animation default, naming), and two days isn't enough to settle them and test.
- **SmartArt can plug in later without reworking the orchestrator.** In your design, SmartArt is a new knowledge file (`LAYOUTS.md`) plus additions to the conventions, the build spec, the style guides and `check-deck.py`. If the orchestrator says "propose tags as the knowledge files define them" instead of listing tag families, layouts slot in with at most one new checkpoint ("here are the layouts I suggested").
- **It makes SmartArt cheaper to test.** Step 6 of your design doc means running Phase 1 → Phase 2 over and over to see if Claude suggests the right layouts. A smooth guided run makes each test faster, and every test also exercises the orchestrator.

The case for SmartArt first is that the orchestrator would know about every step from day one. Since the orchestrator hands the details to the knowledge files, that gain is small.

**Things to settle for the orchestrator**

- **Where it lives.** Skills in claude.ai belong to your account, not to a Project. "Create a Skill once, and it's available in any conversation—regular chats, inside Projects, across all your work with Claude." ([What are skills?](https://support.claude.com/en/articles/12580051)) A skill wouldn't come along with the project, so each attendee would have to install it separately. A knowledge file (say `GUIDED-WORKFLOW.md`) plus a short section in the project instructions keeps everything in the project, and `PROMPTS.md` stays as the teaching document.
- **The new-chat step.** Claude can't open a new chat itself, so the orchestrator can't do the switch for the user. It can make the switch hard to miss and safe to skip:
  - At the gate, Claude stops with a clear "start a new chat" message.
  - In any new chat, Claude works out where things stand from the state files: BRIEF.md still has blanks, the outline is a draft, the approval entry exists, the deck is partly built. Then it picks up from there.
  - Users can type the same thing in every chat ("continue my deck"). Someone who skips the switch, as you did, can still carry on.
- **Guided and manual modes.** In guided mode, moving from the brief straight to the outline interview is what you want, as long as it pauses at each checkpoint. For teaching with the separate prompts, add "stop after writing BRIEF.md" to prompt 1. Also add a line to the instructions: when a request names one step, do only that step. That's a quick fix you could hand the class on Tuesday even before the full orchestrator is ready.

If you'd like, I can draft the guided-workflow file, the changes to the project instructions and the prompt-1 fix in your folder, then walk through a sample run to check the checkpoints and the restart in a new chat.

## User message 2

My thoughts on your comments:

1. I agree that separating the SmartArt and orchestration work, and doing the orchestration work first is the way to go.
2. for "where it lives", we can stick with the current project structure.  At a future time, i would like to discuss with you the possibility of moving all of this behavior into some kind of an installable Claude plugin.  I don't want to complicate our work here with going down that path yet.
3. your second bullet under "The new-chat step" raises a question: the project instructions prevent work on the deck from starting before the user completes the outline and approves the completion of phase 1 (prompt 5 records the approval in DECISIONS.md and OUTLINE.md.
4. I love the idea in the third bullet of "The new-chat step" section - with or without the orchestrator or a new chat window, if the user says something like "continue my deck" the process should continue.  However, it should still enforce not working on the deck itself until the user has approved the outline.  If the user tells Claude to start work on the deck, Claude should respond with something like, "the outline has not been approved yet - if you would like to do that now, we can record the decision and proceed".  
5. Your way of describing the current behavior ("manual mode", with the individual prompts for each step), and "guided" mode to orchestrate the entire flow makes sense.  We may even want a convention which would instruct Claude on the desired mode (guided or manual).  for example, if the user's first prompt in a chat in the project includes something like, "please use guided mode" then Claude would know it should prompt the user until each requirement is fulfilled before moving the next step.  If the user doesn't indicate in the first prompt, perhaps Claude could be instructed to ask the user which mode he/she would like.  I'd like your thoughts on this.
6. If I haven't left you with additional questions in my commentary above, then yes - draft the guided-workflow file and make any other needed tweaks to the current markdown files to accommodate.  you can operate directly on the files in the shared folder.

### Claude

I'll read the rest of the knowledge files, then draft the guided-workflow file and the edits in your folder.

> 🔧 **Bash**: print BRIEF.md, DECISIONS.md, OUTLINE.md, OUTLINE-CONVENTIONS.md, DECK-BUILD-SPEC.md
> 🔧 **TaskCreate** ×3: draft GUIDED-WORKFLOW.md; update existing files; check consistency and write back
> 🔧 **Write**: knowledge/GUIDED-WORKFLOW.md
> 🔧 **Edit** ×3: PROJECT-INSTRUCTIONS.md (knowledge list, "Working modes" and "Continuing" sections, gate response)
> 🔧 **Edit/Bash**: PROMPTS.md (guided-mode section, "Manual mode" heading, prompt 1 stop, prompt 4 marks reviewed)
> 🔧 **Edit**: BRIEF.md (Working mode field); OUTLINE.md (status fields)
> 🔧 **Bash**: WORKFLOW.md and README.md edits
> 🔧 **device_commit_files**: wrote 7 files back to the folder

I've added a new `knowledge/GUIDED-WORKFLOW.md` and edited six existing files in your folder. None of it is tested yet, and nothing is committed to git.

**Your point 3.** Picking up from the files never gets around the approval. When Claude works out where things stand, it checks DECISIONS.md for the approval entry, so "continue my deck" can take a user up to the approval question but not past it. If someone asks for the deck before approving, Claude says the outline hasn't been approved yet, names the current version, and offers to record the approval now, as you described. If the independent review hasn't happened either, it mentions that in one line and leaves the choice to the user.

**Your point 5.** I went with your idea, plus two changes so the question doesn't become a nuisance:
- **Ask only when the first message is open-ended**, like "continue my deck" or "hi". If the message names a mode, Claude uses it. If it's a prompt from PROMPTS.md, or another request for a single step like "revise 4.2", Claude runs that one step in manual mode without asking. That way your class can paste prompts as before, and step 1 can no longer run on into the outline.
- **Remember the choice.** BRIEF.md has a new **Working mode** field. Later chats use it and say so in one line ("Continuing in guided mode. Say 'manual mode' to switch."), instead of asking every time. Users can switch modes at any point.

**What's in the folder now**
- **`knowledge/GUIDED-WORKFLOW.md` (new):** the two modes and how Claude picks one, how it tells where a presentation stands, the approval rule, and the guided steps (brief → outline → revise → review → approve → pass 1 → pass 2 → changes after the build). Each step is tied to its prompt in PROMPTS.md. It also has a standard "start a new chat" message that's hard to miss. If a user ignores it, Claude carries on and doesn't repeat the advice.
- **New status fields.** OUTLINE.md's status line now records `reviewed:` and `deck:` (none / pass 1 / core / complete) as well as `approved:`, so any new chat can tell what comes next. Outlines made before this change don't have these fields; Claude works the stage out from DECISIONS.md and asks if it can't tell.
- **`PROJECT-INSTRUCTIONS.md`:** the "First chat" section is replaced by short "Working modes" and "Continuing" sections, and the approval response is added to the Phase 2 rule. I kept these core rules in the instructions themselves rather than only in the new file, because Claude always sees the instructions but may not open a knowledge file.
- **`PROMPTS.md`:** now opens with a guided-mode section that has two prompts, "Use guided mode…" and "Continue my deck." The numbered prompts sit under a "Manual mode" heading. Prompt 1 now ends with "Then stop; don't start the outline", and prompt 4 now marks the outline as reviewed.
- **`WORKFLOW.md`, `README.md`, `BRIEF.md`, `OUTLINE.md`:** updated to match, with the quick start showing both paths.

For Tuesday, attendees who already have a project only need to do two things: paste the new project instructions, and upload `GUIDED-WORKFLOW.md`. Their BRIEF.md and OUTLINE.md files can stay as they are.

The next step is a test run in a fresh project. I'd do one guided run, deliberately skipping a new-chat handoff, and one run where you ask for the deck before approving, to check that the approval rule holds.

## User message 3

your work looks great.  Towards your suggestion of running a test in a fresh project, here's what I would like to do:  I would like to reverse engineer the content in examples/outlook-to-todo into a prompt script for the user (if that's feasible).  That folder contains a finished example presentation as well as a transcript from my chat when that deck was built.  if that is feasible, then it would give me prompts not only for my test, but also for the promptly-at-9 session as an exercise.  let me know if you think there are issues with that approach.

### Claude

I'll read the transcript and the finished deck first to see whether a prompt script can be pulled out of them cleanly.

> 🔧 **device_stage_files**: transcript-inbox-to-todo-deck.md, inbox-to-todo-workshop.html, interim-core.html
> 🔧 **Bash** ×4: inspect transcript structure; read the interview (messages 1–8); extract user messages 9–16; read the outline summary, revisions and review
> 🔧 **Bash** ×2: find build results; count slides in the finished deck (41)

Feasible, and it fits as both a test and a class exercise. The transcript has 16 user messages, which reduce to a set of interview answers plus the PROMPTS.md sequence. A straight replay won't work, though, so I'm drafting the script in a form that holds up when Claude's questions and section numbers come out differently.

> 🔧 **Write**: examples/outlook-to-todo/PROMPT-SCRIPT.md
> 🔧 **Bash**: fix slide count and timing wording
> 🔧 **device_commit_files**: wrote PROMPT-SCRIPT.md to the folder

Reverse-engineering the example worked. I saved the script as `examples/outlook-to-todo/PROMPT-SCRIPT.md`. It has three parts:

- **An answer sheet** with everything you told Claude in the original interview, sorted by BRIEF.md section.
- **A guided run** for your test, with four deliberate checks added: Claude asks for the mode on an open-ended first message, refuses to build the deck before approval, carries on if you ignore the "start a new chat" advice, and resumes in a new chat without asking for the mode again.
- **A manual run** that repeats your original prompts in order, for the class exercise.

Replaying the transcript word for word wouldn't have worked, for these reasons:

- **Claude's questions come in a different order each run.** In your original run, several answers were "your draft looks good". That only works if Claude makes the same draft, and it won't. So the answer sheet spells out what was actually agreed, such as the four outcomes and the eight coverage angles, instead of just saying "accept".
- **Section numbers will be different.** Two of your prompts were reactions to that particular outline ("Revise section 7…", "fix the 2.2 cross-reference"). I turned them into templates, like "remove any claim Claude marked [UNVERIFIED]", since the same sections won't exist in a new run.
- **The new outline won't match the example.** Claude's research is live, so the comparison section asks people to judge the overall shape of the result rather than look for an identical deck.
- **The original gate prompt had a date format problem.** You typed 11/09/2026 and Claude converted it to the required YYYY-MM-DD format. The script asks for YYYY-MM-DD directly.

Some issues the script can't fully fix:

- **The full run is long.** Yours spread over two days, and the chat got long enough that Claude had to compact it. For Promptly-at-9, I'd do the interview, the first outline and the approval check live, and leave the deck build as homework or a demo. How long is the session?
- **Your test won't behave like an attendee's.** Claude used your memory to fill in your name and the series before you answered. Your test will look smoother than an attendee's first run unless you test with memory turned off.
- **The example folder has the deck but not the final BRIEF.md and OUTLINE.md.** If the original test project is still there, exporting those two files would give attendees an outline to compare against, not just slides.
- **The answer sheet uses IDEXX and Artifaxx details.** Your design doc says this repo is public, but the transcript already has these details. The script tells attendees to use their own name as presenter. I left the rest as is.

## User message 4

Issues noted.  I will likely follow your advice to address the full run being long - that should work.  Tomorrow (a day before the class) I will run through the full manual and guided process with either what you have prepared or a simple example.

### Claude

Sounds like a good plan. Two tips for tomorrow:

- **Use a separate project for each run.** Once the guided run saves its working mode to BRIEF.md, a manual run in that same project would pick up guided mode whenever you type something open-ended. In the manual project, Claude may also ask you to fill in the Working mode field during the kickoff interview. That's harmless: just answer "manual."
- **Note where the instructions are unclear, not just where they fail.** The guided run is the first real test of GUIDED-WORKFLOW.md. Note the moments where Claude hesitated, asked an odd question, or skipped a pause, even if it got there in the end. Those are usually one-line fixes in the instructions.

If anything goes wrong, send me the step and what Claude said, and I can tighten the files before Tuesday.

## User message 5

I will follow up with you after tomorrow's testing.  In the meantime, I'd like to revisit an earlier topic (for educational purposes, no changes needed for this).  I'm curious about the differences in how memory would be managed if this project were created as a skill - prompt(s), templates, scripts, etc. vs how we have it now with an instruction prompt and multiple knowledge files.  the world is excited about skills, but it feels like the structure we have now might be more effective for keeping the correct pieces in context as the process unfolds with the user.  what is your position on this?

### Claude

I don't think it's skills versus projects. The two hold different kinds of information: a skill is good for the **how** of a process, and a project is good for the **state** of one particular piece of work. Your instinct is right about the state, and only partly right about keeping the right pieces in context.

**How each one loads into context**

- **Project:** the instructions are in context for every message of every chat. In a small project the knowledge files are too, which is why the current setup feels dependable. Everything is always there. That has two costs:
  - Every message pays for all of it, including the Phase 2 build rules while you're still doing the brief interview.
  - It doesn't hold up as the project grows. "When your project knowledge approaches context limits, Claude seamlessly enables Retrieval Augmented Generation (RAG) mode to expand capacity by up to 10x." ([Skills explained](https://claude.com/it/resources/articles/skills-explained)) Past that point, Claude retrieves pieces of the knowledge files based on the question, so a rule like the gate may or may not come back with a given message. Upload the 108 KB transcript and the example decks as reference, and you'd get there quickly.
- **Skill:** only a short description is always loaded. The main instructions load when the skill is triggered, and reference files load when those instructions say to read them. Scripts run without being read into context at all. So the build spec loads at the start of Phase 2, deliberately, rather than sitting in context from the first message or turning up in fragments through retrieval. For a process with clear phases, that's arguably more dependable than what a large project does.

**Where a skill falls short for this process**

- **It doesn't keep state.** A skill is the same for every user and every presentation. BRIEF.md, OUTLINE.md and DECISIONS.md still need a home that lasts across chats, belongs to one presentation, and can be written to. A project gives you that for free, and the user can see the files, which matters for teaching.
- **It has to be triggered.** A skill loads when Claude decides the request matches it, or when the user names it. The gate and the attribution rules have to apply even when someone types "just make the slides" in a chat where the skill never loaded. Rules like that belong in instructions that are always loaded.

**Where a skill clearly wins**

- **Scripts that run the same way every time.** Today Claude rebuilds the deck-assembly script in each build, and runs its own version of the checks because `tools/check-deck.py` isn't uploaded to the project. A skill would bundle both, so they run identically each time.
- **Setup and updates.** Today's changes mean all 40 attendees have to paste new instructions and upload a file. With a skill or plugin, you update it once. Setup was where a lot of your follow-up requests came from.
- **Loading only the current phase's rules.** This matches the outline → deck structure well.

**My position**

Your current structure is the right one for teaching, and a good one while the project stays small. For production, I'd split it:

- **Skill or plugin:** the process, conventions, build spec, style guides, templates and scripts.
- **Project (or a working folder):** only the state files.
- **Project instructions:** a few lines that say to use the skill, where the state files live, and the rules that must always hold (the gate and attribution).

That fits the plugin conversation you want to have later.

One more thing: Claude's personal memory doesn't belong in this design at all. It's tied to the user rather than to the presentation, and you saw it fill in answers during the interview. Project state should stay in files you can see.

## User message 6

ok - I will definitely want to follow up at a later time on how to eventually restructure all of this into an optimized combination of skill(s) and a project template or some other design.  I'm going to want to refer to our work here today in another Claude account tomorrow.  Please create a complete transcript and store as a document under the docs folder.

### Claude

I'll write the transcript to `docs/`, using the same conventions as your existing transcript in `examples/`.

> 🔧 **Write**: docs/transcript-guided-workflow-session-20261115.md
> 🔧 **device_commit_files**: wrote the transcript to the folder

*(This file is that transcript.)*
