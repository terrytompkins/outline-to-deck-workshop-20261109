# Prompts for each stage

Copy-paste prompts for running a presentation through the template. Start each one in a **fresh chat** in the project unless it says otherwise. The project files carry the state between chats.

## 1. Kickoff: fill in the brief
> Read BRIEF.md. Interview me to fill in every `[TBD: …]` field, a few questions at a time. When we're done, write BRIEF.md to the project and summarize it in five lines.

## 2. First outline
> Following the project instructions, research the topic in BRIEF.md and write outline v0.1. Map the coverage dimensions before choosing a structure. Include the time plan, origin tags, Coverage gaps, and source reconciliation. Add callout and slide-type tags from the active style guide where they genuinely fit, and list which ones you added. Write OUTLINE.md and DECISIONS.md to the project when done.

## 3. Revise (same chat is fine for small changes)
> Revise sections [N, N.M]: [what to change]. Don't renumber anything. Bump the version, record the change under "Changes by version", and write the files at the end.

## 4. Independent review before approval
> Review OUTLINE.md against BRIEF.md, DECISIONS.md, and the project instructions. Don't restructure or renumber. Give me a gap list ranked by value to attendees, check that style tags follow the style guide's proposal rules and limits, and flag any claim that needs an "As of" date or an [UNVERIFIED] tag. Propose changes; don't write the files until I approve them.

## 5. Approve
> I approve outline v[X.Y]. Record the gate entry "- [today's date] · Decided · Outline v[X.Y] approved; Phase 2 begins." in DECISIONS.md, update OUTLINE.md's status, and write both files.

## 6. Start Phase 2 (fresh chat)
> Start Phase 2. DECISIONS.md records approval of outline v[X.Y]; build from it as written, without re-researching or revising content. Follow DECK-BUILD-SPEC.md and the style guide in BRIEF.md. Before writing HTML, confirm the pinned library versions and list any outline item or tag you can't render as specified. Pass 1: title, agenda, and every horizontal slide. Then stop and send me the file.

## 7. Phase 2, pass 2
> Continue with pass 2: vertical slides in priority order, Core sections first. Send an interim file after the Core sections, then finish Brief and Self-guided. Run the full verification checklist and report the results as numbers.

## 8. Change content after the build
> Change [section N.M]: [what]. Update OUTLINE.md first (bump the version and record a Decided entry for the change), then regenerate only the affected slides, re-run the checks on them, and send the updated deck.

## 9. Switch style guides
> I've uploaded [STYLE-X.md]. Make it the active style guide in BRIEF.md. List the tags in OUTLINE.md that the new guide neither defines nor maps in its fallback table, and propose a mapping. After I approve, rebuild the deck.

## Recovery: a chat lost its file tools
> A previous chat in this project produced changes it couldn't write to the files. Use past-chat search to find the message containing "Updates for OUTLINE.md" from [approximate date]. Read it in full, apply exactly those changes to the current files, write them, and list by section number what you applied and anything you couldn't.
