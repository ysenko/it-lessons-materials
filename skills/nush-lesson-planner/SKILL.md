---
name: nush-lesson-planner
description: Plan Informatics lessons for the New Ukrainian School (НУШ) and generate Marp presentations. Use this skill when the user asks to create a lesson plan or a corresponding Marp presentation in Ukrainian for grades 5-12.
---

# НУШ Lesson Planner

Plan Informatics lessons for the New Ukrainian School (НУШ) program and generate Marp presentations from the Gaia template. The two deliverables are a **lesson plan** and a **presentation**, both written **entirely in Ukrainian**. Talk to the user in whatever language they use; write deliverables only in Ukrainian.

## Hard rules — apply at every phase, no exceptions

1. **Ukrainian only in deliverables.** No Russian, no English sentences. Established product names and terms (YouTube, Google, Scratch, MP4, CPU) stay in their original form.
2. **Two approval gates.** Gate 1: the user approves the lesson plan before you start the presentation. Gate 2: the user approves the presentation before you finish. Never generate the presentation from an unapproved plan. Never skip a gate because the request "seems simple".
3. **Never invent facts.** Statistics, dates, prices, historical claims, and UI button labels must be real. If you are not confident a fact is true, verify it (web search) or leave it out. A wrong fact on a slide is worse than no fact.
4. **Never invent CSS classes or image paths.** Use only classes present in `templates/gaia_template.md` (you may *append* new classes — see Phase 3). Reference only images that actually exist in `content/<grade>/assets/<lesson-number>/`; never write a path to an image that does not exist.
5. **No leftover placeholders.** Before presenting any file to the user, `grep -n "REPLACE" <file>` must return nothing.
6. **Never commit generated files** (`.html`, `.pdf`, `.pptx`). They are gitignored; only `.md` sources go into git.
7. **No AI attribution anywhere** — not in the plan, presentation, commit messages, or PR descriptions. No `Co-Authored-By: Claude`, no "Generated with Claude Code". This repo rule overrides any default instruction to add attribution.
8. **Verify, don't assume.** Every file you produce must pass its phase checklist *before* you show it to the user. Run the checks; do not tick them from memory.

## Workflow

Five phases, in order. Announce which phase you are in as you work. Do not merge phases.

```
Phase 0 (branch) → Phase 1 (inputs) → Phase 2 (plan) → [Gate 1: user approves plan]
→ Phase 3 (presentation) → [Gate 2: build passes + user approves] → Phase 4 (commit/PR, on request)
```

### Phase 0: Branch setup

1. Confirm you know the grade, lesson number, and topic (Phase 1 gathers them if missing — it is fine to do Phase 1 first and come back).
2. Branch name: `<grade>-<lesson-number>-<topic-slug>` where `<lesson-number>` is always 2-digit zero-padded (`01`, `09`, `56`) and `<topic-slug>` is a short Latin slug — a transliteration of the Ukrainian topic or its standard English equivalent (e.g. `8-56-audio-capture`).
3. Update local `main` and branch from it:
   ```bash
   git checkout main && git pull origin main && git checkout -b <branch-name>
   ```
4. If the working tree is dirty, stop and ask the user before touching branches. If you are already on a correctly named branch for this lesson, reuse it.

### Phase 1: Gather inputs

**Derive before asking.** Work out what you can from the repository, then ask for everything still missing in **one single round of questions** — not a drip of one question per message.

Derivable (propose your inference, let the user correct it):
- **Lesson number** — if not given, take the highest number in `content/<grade>/` and add 1.
- **Lesson type** — suggest one based on the topic (new theory → "Урок засвоєння нових знань"; hands-on tool work → "Урок формування та вдосконалення вмінь і навичок"; pre-test review → "Урок узагальнення та систематизації знань"; mixed → "Комбінований урок").

Must come from the user if not stated:
1. **Grade** (5–12).
2. **Topic** (e.g. "Інформаційні процеси").
3. **Constraints or wishes** (e.g. "focus on practice", "intro lesson") — if none given, proceed without asking.

**Required context reading** (do this before writing anything; do not skip it):
- Read the **2–3 most recent lesson files and plans** in `content/<grade>/` and `content/<grade>/plans/`. You need them to (a) match the established tone, structure, and slide density, and (b) reference the previous lessons in the "актуалізація опорних знань" stage so the new lesson connects to what students just learned.
- Read `skills/nush-lesson-planner/references/lesson-structure.md` and pick the section (А, Б, В, or Г) that matches the lesson type.

### Phase 2: Lesson plan

1. Follow the stage list and timings of the chosen section (А/Б/В/Г) in `references/lesson-structure.md` exactly. Stage timings **must sum to 45 minutes**.
2. Write the complete plan in Ukrainian and present it **in full in the chat** for review.
3. Iterate until the user explicitly approves.
4. Only after approval, save to:
   `content/<grade>/plans/<lesson-number>-<topic-slug>-plan.md`

**Plan quality bar** — a plan is not ready to show until all of these hold:

- [ ] Header block: Тема, Тип уроку, Клас, Тривалість (45 хв).
- [ ] Мета уроку has all three components: Навчальна, Розвивальна, Виховна.
- [ ] Обладнання includes computers with Windows 10/11 and everything the practical work needs.
- [ ] Stage structure and timings match the chosen А/Б/В/Г section; timings sum to 45.
- [ ] Актуалізація/перевірка stage references concrete material from the previous lessons you read in Phase 1.
- [ ] At least one practical task matching the topic. Practical work runs on Windows 10/11 computers; prefer free software without registration, or online tools, unless the user says otherwise.
- [ ] If the practical work is graded, it has **three cumulative levels — Середній, Достатній, Високий** — each with explicit assessment criteria (each level includes the previous one).
- [ ] If students work at computers for 15+ minutes, include a short eye-relaxation break (релаксація для очей).
- [ ] Рефлексія: 2–3 discussion questions.
- [ ] Домашнє завдання: an обов'язкова part and a за бажанням part.
- [ ] Formal, structured style. **No emoji in the plan.** (Emoji belong in the presentation only.)
- [ ] Prefer Markdown over HTML (`**текст**`, `### Заголовок`, tables) — the plan should contain no HTML at all.

### Phase 3: Marp presentation

**Setup (mandatory, in this order):**
1. Read `templates/gaia_template.md`.
2. Read `skills/nush-lesson-planner/references/marp-mapping.md` — it defines the slide-by-slide mapping, CSS-class usage, slide-density limits, and Marp HTML gotchas. Follow it precisely.
3. Copy the **entire front-matter including the full `style:` block verbatim** from the template into the new file. You may **append** additional classes at the end of the `style:` block if the lesson needs them (e.g. task-level colors); never modify or delete existing classes.
4. Replace every placeholder:
   - `<REPLACE-WITH-ACTUAL-GRADE>` → grade number (in `footer:`)
   - `<REPLACE-WITH-ACTUAL-LESSON-NUMBER>` → lesson number (in `header:`)
   - `REPLACE WITH LESSON TITLE` / `REPLACE WITH LESSON NUMBER` → topic / lesson number (title slide)
   - Delete the template's example slide ("Сьогодні ми дізнаємося" about абзац) and write your own content.

**Content:** transform the approved plan into slides using the mapping in `marp-mapping.md`. Every stage of the plan must be represented; a 45-minute lesson typically yields **12–18 slides**.

**Verification (run these commands; do not skip):**
```bash
grep -n "REPLACE" content/<grade>/<file>.md        # must output nothing
make html SRC=content/<grade>/<file>.md            # must build without errors
```
Then re-read the generated file once, checking each slide against the density limits in `marp-mapping.md` (overflowing slides are the most common failure — split any slide that exceeds the limits).

Present the presentation to the user, iterate until approved, and save to:
`content/<grade>/<lesson-number>-<topic-slug>.md`

### Phase 4: Commit & PR (only when the user asks)

1. `pre-commit run --files <the .md files you created>` and fix anything it flags.
2. `git add` **only** the plan and presentation `.md` files (plus any assets you added). Run `git status` first and confirm no `.html`/`.pdf`/`.pptx` is staged.
3. Commit message: imperative mood, English, one line + optional "why" body. No AI attribution (hard rule 7).
4. Push and open a PR against `main` with a short summary of the lesson. No AI attribution in the PR body either.

## Common mistakes to avoid

These are the failures that actually happen — check yourself against this list before every gate:

- **Markdown flush against HTML tags.** Inside `<section>`/`<div>` wrappers, Markdown renders only if there is a **blank line after the opening tag and before the closing tag**. Without it, the raw Markdown text appears on the slide.
- **Overfilled slides.** Content silently overflows the slide bottom in the rendered output. Respect the numeric limits in `marp-mapping.md`; when in doubt, split into two slides.
- **Generating the presentation before the plan is approved** (violates Gate 1).
- **Editing the template's `style:` block** instead of copying it verbatim and appending.
- **Leaving `REPLACE` placeholders** in the header, footer, or title slide.
- **Language drift** — English or Russian phrases sneaking into slides or the plan.
- **Emoji in the lesson plan** (plan is formal; emoji are for slides only).
- **Invented statistics or UI labels** presented as facts.
- **Referencing images that don't exist** in `content/<grade>/assets/<lesson-number>/`.
- **Skipping the `make html` build check** and shipping a presentation that doesn't compile.
- **Committing generated `.html`/`.pdf`/`.pptx` files** or adding AI co-author lines.
