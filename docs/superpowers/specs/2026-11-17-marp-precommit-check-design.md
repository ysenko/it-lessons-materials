# Marp pre-commit check — design

## Intent

Give Claude Code a sub-second way to verify a Marp deck before pushing to GitHub,
instead of relying on the PR build (which never fails: Marp CLI exits 0 on broken
front matter, missing images, unclosed HTML and misspelled directives) or on manual
self-checks described in `skills/nush-lesson-planner/SKILL.md`.

## Goals

- Catch technical Marp breakage and violations of the lesson-planner skill's rules.
- Run automatically on `git commit` (the pre-commit hook is already installed) and
  on demand via `pre-commit run marp-check --files <deck>`.
- Report each problem as `path:line: message` so it can be fixed directly.

## Non-goals

- Rendering slides or checking visual layout/overflow (the user checks layout).
- Checking lesson plans (`plans/`) or assessments (`assessments/`).
- Distinguishing lesson types (A vs others) for the slide limit.

## Anti-goals

- Noticeably slowing commits or needing Node/npm in the repo.
- Blocking commits that don't touch decks.

## Approaches

- **A. Python script as a local pre-commit hook — chosen.** Fast, matches the repo's
  Python tooling, isolated deps via pre-commit.
- B. markdownlint-cli2 with custom JS rules — adds Node, built-in rules fight Marp's
  inline HTML.
- C. Node script using `@marp-team/marp-core` to render and inspect — exact slide
  parsing, but Node setup, slower, more code.

## Design

**Files**

- `tools/check_marp.py` — the checker; takes file paths, exits non-zero on any error.
- `.pre-commit-config.yaml` — new `repo: local` hook `marp-check`,
  `language: python`, `additional_dependencies: [pyyaml]`,
  `files: ^content/[0-9]+/[^/]+\.md$` (top-level decks only, so `plans/` and
  `assessments/` are excluded).
- `skills/nush-lesson-planner/SKILL.md` — replace the manual "no `](http`" self-check
  with "run `pre-commit run marp-check --files <deck>` and fix all errors before
  presenting the deck"; mention it in the CLAUDE.md Linting section.

**Checks**

Technical:
1. File starts with a `---` front-matter block that parses as YAML (a mapping).
2. Front matter has `marp: true`.
3. Title present: front-matter `title:` or a `# ` heading.
4. Every local image path (`![](…)`, `<img src>`, `url(…)` that isn't `http(s):`/`data:`)
   exists relative to the deck.
5. `<div>` and `<section>` open/close tags balance per slide; no `---` slide break
   while a `<section>`/`<div>` is open.
6. HTML-comment directives (`<!-- key: … -->`, `<!-- _key: … -->`) use known Marp
   directive names (class, paginate, header, footer, backgroundColor,
   backgroundImage, backgroundPosition, backgroundRepeat, backgroundSize, color,
   theme, style, headingDivider, size, math, title, description, author, image,
   keywords, url, marp, lang); other comments (notes) are ignored.

Skill rules:
7. No Markdown links to URLs (`[text](http…)`), autolinks (`<http…>`), or bare
   URLs outside an `href`/`src` attribute — links must be
   `<a href=… target="_blank" rel="noopener noreferrer">`.
8. Every `<a href="http…">` has `target="_blank"`.
9. No leftover placeholders: `REPLACE`, `ABC–XYZ` / `ABC-XYZ`.
10. Slide 2 is the "🛡️ Пригадуємо: техніка безпеки" slide.
11. A `## 🏠 Домашнє завдання` slide exists.
12. At most 14 slides, not counting the homework slide. Skipped when the env
    variable `MARP_CHECK_SKIP_SLIDE_LIMIT` is set to a non-empty value other than
    `0` (e.g. `MARP_CHECK_SKIP_SLIDE_LIMIT=1 git commit …`); all other checks still run.
13. All CSS class selectors from `templates/gaia_template.md`'s `style:` block are
    present in the deck's `style:` block (read from the template at runtime, not
    hard-coded).

Slides are split on lines that are exactly `---` outside the front matter and
outside fenced code blocks.

**Older decks:** of 163 existing decks, 56 have the safety slide and 80 use
Markdown links, so editing an old deck will fail the hook until it's brought up to
the current conventions. That's intended (a reused deck should meet the rules);
a one-off bypass is `SKIP=marp-check git commit …`.

## Left to the builder

- Exact regexes and message wording.
- Small pytest file for the checker (fixtures of good/bad decks) under `tests/`.
- Running the checker over the current lesson-22 grade-7 deck to confirm it passes.
