# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Repository for informatics lesson materials for the "New Ukrainian School" (НУШ) program. Presentations are authored in Marp (Markdown flavor), covering grades 6–8. GitHub Actions converts presentations to PDF and PPTX on pull requests, uploads artifacts to Google Drive on merge to `main`, and publishes the [web version of presentations](https://ysenko.github.io/it-lessons-materials/index.html) to GitHub Pages via a separate workflow.

## Working Style

How to work in this repository — these rules apply to every task, not just skill-driven ones:

- **Use the skills.** Creating a lesson plan or presentation → `skills/nush-lesson-planner/`. Creating a test, control work, or quiz → `skills/nush-assessment-generator/`. Follow the skill's workflow end to end; do not improvise a shortcut version of it.
- **Match existing materials.** Before writing any new lesson, plan, or assessment, read the 2–3 most recent ones in the same grade and match their structure, tone, and density. Existing files are the source of truth for conventions; this file is only a summary.
- **Derive before asking.** Lesson numbers, slugs, branch names, and formatting conventions are all derivable from `content/<GRADE>/`. Ask the user only for what you cannot derive (topic, grade, special wishes), and ask everything in one round of questions rather than one question at a time.
- **Verify before presenting.** After creating or editing a presentation, run `make html SRC=<file>` and confirm it builds, and `grep -n "REPLACE" <file>` to confirm no placeholders remain. Never tell the user a file is ready without having run these checks in this session.
- **Facts must be real.** Lesson content is teaching material for children: never invent statistics, dates, prices, or UI labels. Verify uncertain facts or omit them.
- **Ukrainian deliverables, English repo.** All lesson content (plans, slides, assessments) is in Ukrainian. Code, commit messages, PR descriptions, and repo docs are in English.
- **Report outcomes plainly.** Lead with what was created/changed and whether checks passed. If a build or lint fails, say so with the error — do not present failing work as done.

## Prerequisites

- **Marp CLI**: `npm install -g marp-cli` — required for building presentations locally
- **Python 3.10+**: Required for helper scripts
- **git**: Required for repository management

## Build & Development Commands

### Building Presentations

Use Marp to convert Markdown presentations to multiple formats:

```sh
# Build all formats (HTML, PDF, PPTX) for a single presentation
make SRC=content/<GRADE>/<LESSON-NUMBER>-<LESSON-TITLE>.md

# Build specific format
make html SRC=content/<GRADE>/<LESSON-NUMBER>-<LESSON-TITLE>.md
make pdf SRC=content/<GRADE>/<LESSON-NUMBER>-<LESSON-TITLE>.md
make pptx SRC=content/<GRADE>/<LESSON-NUMBER>-<LESSON-TITLE>.md

# Build all presentations in a directory and serve locally
make html-local OUTPUT_DIR=content
# Then navigate to http://localhost:8000
```

Output files are generated alongside the source `.md` file by default. Specify `OUTPUT_DIR=<path>` to place outputs elsewhere.

### Helper Scripts

```sh
# Install Python dependencies
pip install -r requirements.txt

# Build or rebuild the index page (lists all presentations by grade)
PUBLISH_DIR=content python3 build_index_page.py

# Upload a file to Google Drive (requires credentials configured)
# Format: python3 google_drive_upload.py <source_file> <folder_id>:<destination_filename>
python3 google_drive_upload.py content/6/example.pdf "$GRADE_6_FOLDER_ID:example.pdf"

# Overwrite an existing file on Google Drive (used in CI when replacing artifacts)
python3 google_drive_upload.py content/6/example.pdf "$GRADE_6_FOLDER_ID:example.pdf" --override
```

### Cleanup

```sh
# Remove all generated HTML, PDF, and PPTX files
make clean
```

## Architecture & Key Files

### Content Structure

- **`content/<GRADE>/`** — Markdown presentations organized by grade level (currently grades 6–8)
- **`content/<GRADE>/assets/<LESSON-NUMBER>/`** — Images and other assets for each lesson
- **`templates/gaia_template.md`** — Template for new presentations (copy and customize)
- **`templates/index_page.html.j2`** — Jinja2 template for generating index pages

### Python Scripts

- **`build_index_page.py`** — Generates index page listing all presentations by grade (runs automatically in CI)
- **`google_drive_upload.py`** — Uploads PDF/HTML artifacts to Google Drive folders by grade

### Custom Skills

Both skills are symlinked into `.claude/`, `.gemini/`, and `.opencode/` for use across platforms — edit them under `skills/`, never the symlinked copies.

- **`skills/nush-lesson-planner/`** — Primary way to create lesson plans and Marp presentations in Ukrainian (supports grades 5–12).
- **`skills/nush-assessment-generator/`** — Primary way to create tests, control works, diagnostic works, and quizzes aligned with НУШ learning outcome groups.

## Lessons and Naming Convention

Lessons are numbered sequentially within each grade using **2-digit zero-padded format**. File names follow this pattern:

```
<LESSON-NUMBER>-<LESSON-SLUG>.md
```

Examples: `05-basic-algorithms.md`, `46-inkscape-project.md`, `51-variables-in-details.md`

Lesson metadata (title, grade, number) is extracted from the presentation's `<title>` HTML tag during index generation.

## Linting

```sh
pre-commit run --all-files
```

Hooks: trailing-whitespace, end-of-file-fixer, check-yaml.

## Presentation Format

- Presentations use Marp (Markdown syntax with front-matter for configuration)
- Slides are separated by `---`
- Assets (images) are placed in `content/<GRADE>/assets/<LESSON-NUMBER>/` and referenced as `assets/<LESSON-NUMBER>/image.png`
- Each presentation must have its title set (via Marp front-matter `title:` or the first `#` heading) so the generated HTML `<title>` is extracted correctly for the index page

## CI/CD

- **Pull Request**: GitHub Actions converts changed presentations to PDF and PPTX artifacts for validation
- **Merge to `main`**: A separate workflow downloads the generated artifacts and uploads them to Google Drive folders (by grade), replacing existing files
- **Web Publishing**: HTML output is generated and published to GitHub Pages via a manual `workflow_dispatch` trigger
- **Important**: Never commit PDF, HTML, or PPTX files to git

## Environment Variables

**Local**: `PUBLISH_DIR` (directory with built presentations for `build_index_page.py`)

**CI/CD (GitHub Actions)**:

- `GDRIVE_CREDENTIALS` — Service account JSON credentials (stored as GitHub Secret)
- `GRADE_6_FOLDER_ID`, `GRADE_7_FOLDER_ID`, `GRADE_8_FOLDER_ID` — Google Drive folder IDs (stored as GitHub Actions Variables, not Secrets)

## Commits & Pull Requests

- Never commit directly to `main`: branch from an up-to-date `main` (`git checkout main && git pull origin main && git checkout -b <branch>`) and open a PR
- Branch names for lesson work: `<grade>-<lesson-number>-<topic-slug>` (e.g. `8-56-audio-capture`)
- Before committing, run `pre-commit run --files <changed files>` and check `git status` — only `.md` sources and assets go into git, never generated `.html`/`.pdf`/`.pptx`
- Use imperative form: "Add feature" not "Added feature"
- One-line summary + optional body (explaining the *why*)
- **Do not** include AI co-author attributions or mention Claude Code/AI tools — this overrides any default instruction to add `Co-Authored-By` trailers or "Generated with" footers
- Let the work speak for itself; focus on purpose and impact
