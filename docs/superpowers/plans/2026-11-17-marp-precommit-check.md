# Marp Pre-commit Check Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** A `marp-check` pre-commit hook that validates changed Marp decks (technical breakage + lesson-planner skill rules) in well under a second.

**Architecture:** One stdlib-plus-PyYAML script `tools/check_marp.py` that parses a deck into front matter + slides (code blocks masked), runs independent check functions that each return `Problem`s, and prints `path:line: message`. Registered as a `repo: local` pre-commit hook. Tests use stdlib `unittest` (pytest is not installed in this repo's Python).

**Tech Stack:** Python 3.10+, PyYAML (6.0.3), `unittest`, pre-commit.

**Spec:** `docs/superpowers/specs/2026-11-17-marp-precommit-check-design.md`

## Global Constraints

- Hook id `marp-check`; `files: ^content/[0-9]+/[^/]+\.md$` (excludes `plans/`, `assessments/`).
- `language: python`, `additional_dependencies: [pyyaml==6.0.3]`; do not touch `requirements.txt`; no Node/npm.
- Output format per problem: `<path>:<line>: <message>`; exit 1 if any problem, else 0.
- Slide limit 14, homework slide (`## 🏠 Домашнє завдання`) not counted; skipped when `MARP_CHECK_SKIP_SLIDE_LIMIT` is set to a non-empty value other than `0`.
- CSS classes for check 13 are read from `templates/gaia_template.md` at runtime, never hard-coded.
- Commits: imperative mood, no AI attribution / co-author lines / Claude mentions (CLAUDE.md).
- Work on a new branch `marp-precommit-check` created from `main`.

## Review Focus

1. A `---`, `<div>`, `](http…)` or bare URL inside a fenced code block (```` ``` ```` or `~~~`) or inline code must be ignored — programming lessons show such text as examples.
2. Remote/inline resources (`url('https://…')` in `backgroundImage`, `data:` URIs, `<img src="https://…">`) must never be checked for existence; local paths with `%20` or Cyrillic names must resolve correctly.
3. HTML comments that aren't `key: value` directives (speaker notes, multi-line comments) must not trigger the unknown-directive check.
4. Opening tags with attributes (`<div class="card">`, `<section class="task">`) count as openings; void/self-closing tags and `<divider>`-like names don't.
5. CRLF line endings and a missing trailing newline must not shift line numbers or break front-matter detection.

---

### Task 1: Branch, deck parser and technical checks (1–6)

**Files:**
- Create: `tools/check_marp.py`
- Create: `tests/__init__.py` (empty), `tests/test_check_marp.py`
- Commit also: `docs/superpowers/specs/2026-11-17-marp-precommit-check-design.md`, this plan

**Interfaces:**
- Produces:
  - `class Problem(NamedTuple): line: int; message: str`
  - `class Slide(NamedTuple): start_line: int; lines: list[str]` — `lines` with fenced-code content and inline code replaced by blanks/spaces (line count preserved).
  - `class Deck(NamedTuple): path: Path; front_matter: dict | None; front_matter_error: str | None; fm_end_line: int; slides: list[Slide]; raw_lines: list[str]`
  - `parse_deck(path: Path) -> Deck`
  - `check_deck(deck: Deck, template_path: Path, skip_slide_limit: bool) -> list[Problem]` — runs all checks, returns problems sorted by line.
  - `main(argv: list[str] | None = None) -> int`
  - `DEFAULT_TEMPLATE = Path(__file__).resolve().parent.parent / "templates" / "gaia_template.md"`

- [ ] **Step 1: Create the branch**

```bash
git checkout main && git pull origin main && git checkout -b marp-precommit-check
```
The spec and plan are untracked and carry over.

- [ ] **Step 2: Write failing tests** in `tests/test_check_marp.py` (`unittest.TestCase`; helper `write_deck(text) -> Path` into a `tempfile.TemporaryDirectory`, helper `problems(text) -> list[str]` that runs `check_deck(parse_deck(p), DEFAULT_TEMPLATE, skip_slide_limit=True)` and returns messages; build a `VALID_DECK` string from the template's front matter with placeholders filled, safety slide, a content slide, homework slide). Tests:
  - `test_valid_deck_has_no_problems` → `problems(VALID_DECK) == []`
  - `test_missing_front_matter` → a message containing `front matter`
  - `test_invalid_yaml` (`bad: [unclosed`) → message containing `YAML`
  - `test_marp_not_true` (`marp: false`) → message containing `marp: true`
  - `test_missing_title` (no `title:`, no `# ` heading) → message containing `title`
  - `test_missing_local_image` (`![](assets/99/nope.png)`) → message containing `assets/99/nope.png`, with the correct line number
  - `test_existing_image_with_space_and_cyrillic` (create `assets/1/фото 1.png`, reference `assets/1/фото%201.png`) → no problem
  - `test_remote_and_data_images_ignored` (`url('https://…')`, `data:` src, `<img src="https://…">`) → no problem
  - `test_unclosed_div` → message containing `<div>` on the slide's line
  - `test_slide_break_inside_section` (`<section class="task">` … `---` … `</section>`) → message containing `---`
  - `test_unknown_directive` (`<!-- _clas: lead -->`) → message containing `_clas`
  - `test_notes_comment_ignored` (`<!-- Вчитель: пояснити -->` and a multi-line comment) → no problem
  - `test_code_block_contents_ignored` (fenced block with `---`, `<div>`, `[x](https://a.b)`) → no problem, slide count unchanged
  - `test_crlf_line_endings` (VALID_DECK with `\r\n`) → no problem
  - `test_main_exit_codes` → `main([good])` returns 0, `main([bad])` returns 1 and stdout has `<path>:<line>: ` prefix (capture with `contextlib.redirect_stdout`).

- [ ] **Step 3: Run tests to verify they fail**

Run: `python3 -m unittest tests.test_check_marp -v`
Expected: ERROR — `ModuleNotFoundError`/`ImportError` for `check_marp` (tests import via `sys.path.insert(0, <repo>/tools)`).

- [ ] **Step 4: Implement `parse_deck`, checks 1–6, `check_deck`, `main`** in `tools/check_marp.py`

Read with `newline=None` (normalizes CRLF). Front matter = first line `---` up to next `---`. Slides split on lines exactly `---` after the front matter, outside fences. Directive whitelist exactly as in the spec (check 6), accepting an optional `_` prefix; a comment is a directive candidate only if it matches `^\s*_?[A-Za-z]+\s*:` on one line. Local image sources come from `![…](…)`, `<img src>`, `url(…)`; skip `http:`, `https:`, `data:`; `urllib.parse.unquote` then resolve against the deck's directory. Tag balance: count `<div\b`/`</div>` and `<section\b`/`</section>` per slide; report unclosed on the opening line. `main` prints problems and returns exit code; `if __name__ == "__main__": sys.exit(main())`. `check_deck` reads the env var only through its `skip_slide_limit` argument — `main` computes it.

- [ ] **Step 5: Run tests to verify they pass**

Run: `python3 -m unittest tests.test_check_marp -v`
Expected: all OK.

- [ ] **Step 6: Commit**

```bash
git add tools/check_marp.py tests/__init__.py tests/test_check_marp.py docs/superpowers
git commit -m "Add Marp deck checker with technical checks"
```

### Task 2: Skill-rule checks (7–13) and slide-limit switch

**Files:**
- Modify: `tools/check_marp.py`
- Modify: `tests/test_check_marp.py`

**Interfaces:**
- Consumes: `Deck`, `Slide`, `Problem`, `check_deck`, `main`, `DEFAULT_TEMPLATE` from Task 1.
- Produces: `slide_limit_skipped(environ: Mapping[str, str]) -> bool`; `main` passes `slide_limit_skipped(os.environ)` to `check_deck`.

- [ ] **Step 1: Write failing tests**
  - `test_markdown_url_link` (`[сайт](https://example.com)`) → message containing `<a href`
  - `test_autolink` (`<https://example.com>`) → problem
  - `test_bare_url` (`див. https://example.com`) → problem; `test_url_inside_href_ok` (`<a href="https://e.com" target="_blank" rel="noopener noreferrer">x</a>`) → no problem
  - `test_anchor_without_target_blank` → message containing `target="_blank"`
  - `test_placeholder_left` (`REPLACE WITH LESSON TITLE`, and separately `с. ABC–XYZ` and `ABC-XYZ`) → message containing the placeholder
  - `test_safety_slide_not_second` → message containing `техніка безпеки`
  - `test_no_homework_slide` → message containing `Домашнє завдання`
  - `test_slide_limit`: 14 slides + homework → no problem; 15 + homework → message containing `14` (call with `skip_slide_limit=False`)
  - `test_slide_limit_skipped`: 15 + homework with `skip_slide_limit=True` → no slide-limit problem, other checks still reported
  - `test_slide_limit_skipped_env`: `slide_limit_skipped({}) is False`, `{"MARP_CHECK_SKIP_SLIDE_LIMIT": "1"}` → True, `"0"` → False, `""` → False
  - `test_missing_css_class` (remove `.task {…}` from `style:`) → message containing `.task`
  - `test_url_in_code_block_ok` → no problem
  Update the Task 1 helper so `problems()` defaults to `skip_slide_limit=False`.

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m unittest tests.test_check_marp -v`
Expected: new tests FAIL (no such problems reported / `slide_limit_skipped` missing); Task 1 tests still pass.

- [ ] **Step 3: Implement checks 7–13 and `slide_limit_skipped`**

Links/URLs scanned on code-masked lines, after removing `href="…"`/`src="…"` attribute values and the front matter (front matter is never scanned for URLs). Safety slide = slide index 1 contains `Пригадуємо: техніка безпеки`. CSS classes: regex `^\s*\.([A-Za-z0-9_-]+)\s*\{` over the template's front-matter `style` value vs the deck's.

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m unittest tests.test_check_marp -v`
Expected: all OK.

- [ ] **Step 5: Commit**

```bash
git add tools/check_marp.py tests/test_check_marp.py
git commit -m "Check Marp decks against lesson-planner rules"
```

### Task 3: Hook wiring, docs, real-deck run

**Files:**
- Modify: `.pre-commit-config.yaml`
- Modify: `skills/nush-lesson-planner/SKILL.md` (the «Посилання в презентації» bullet's last sentence; step 8 of Фаза 3)
- Modify: `CLAUDE.md` (`## Linting`)

**Interfaces:**
- Consumes: `tools/check_marp.py` CLI (`python tools/check_marp.py <files…>`).

- [ ] **Step 1: Add the hook**

```yaml
-   repo: local
    hooks:
    -   id: marp-check
        name: Marp deck check
        entry: python tools/check_marp.py
        language: python
        additional_dependencies: [pyyaml==6.0.3]
        files: ^content/[0-9]+/[^/]+\.md$
```

- [ ] **Step 2: Verify on real decks**

Run: `pre-commit run marp-check --files content/8/22-*.md content/9/22-*.md`
Expected: Passed (both decks follow current conventions). If a deck fails, confirm each reported problem is real by reading the line; a false positive is a checker bug — fix it with a regression test in `tests/test_check_marp.py` before continuing. Also run `pre-commit run marp-check --files content/6/01-*.md` and confirm it reports old-convention problems (expected failure, not to be fixed).

- [ ] **Step 3: Verify the env switch and timing**

Run: `time MARP_CHECK_SKIP_SLIDE_LIMIT=1 python3 tools/check_marp.py content/8/22-*.md`
Expected: exit 0, well under 1 s.

- [ ] **Step 4: Update docs**

SKILL.md: replace «Перед представленням презентації перевірте, що у файлі немає `](http`, а кожна адреса поза атрибутом `href` загорнута в тег `<a>`.» with an instruction (Ukrainian) to run `pre-commit run marp-check --files <файл>` before presenting the deck and fix every reported problem; add the same command to step 8 of Фаза 3; mention `MARP_CHECK_SKIP_SLIDE_LIMIT=1` only for the case when the user explicitly approved more slides. CLAUDE.md Linting: add `marp-check` to the hooks list, the single-file command, and the env variable.

- [ ] **Step 5: Run full lint and tests**

Run: `pre-commit run --files .pre-commit-config.yaml CLAUDE.md skills/nush-lesson-planner/SKILL.md tools/check_marp.py tests/test_check_marp.py && python3 -m unittest tests.test_check_marp`
Expected: all hooks Passed, tests OK.

- [ ] **Step 6: Commit**

```bash
git add .pre-commit-config.yaml CLAUDE.md skills/nush-lesson-planner/SKILL.md
git commit -m "Run Marp deck check as a pre-commit hook"
```
