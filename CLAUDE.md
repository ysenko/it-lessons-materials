# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Repository for informatics lesson materials for the "New Ukrainian School" (НУШ) program. Presentations are authored in Marp (Markdown flavor), covering grades 5–12. A CI/CD pipeline builds PDF and HTML versions and uploads them to Google Drive. The [web version of presentations](https://ysenko.github.io/it-lessons-materials/index.html) is published to GitHub Pages.

## Prerequisites

- **Marp CLI**: `npm install -g marp-cli` — required for building presentations locally
- **Python 3.10+**: Required for helper scripts
- **git** and **gh** (GitHub CLI): Required for managing and uploading content

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

# Upload PDFs to Google Drive (requires credentials configured)
python google_drive_upload.py
```

### Cleanup

```sh
# Remove all generated HTML, PDF, and PPTX files
make clean
```

## Architecture & Key Files

### Content Structure

- **`content/<GRADE>/`** — Markdown presentations organized by grade level (5–12)
- **`content/<GRADE>/assets/<LESSON-NUMBER>/`** — Images and other assets for each lesson
- **`templates/gaia_template.md`** — Template for new presentations (copy and customize)
- **`templates/index_page.html.j2`** — Jinja2 template for generating index pages

### Python Scripts

- **`build_index_page.py`** — Scans published presentations, extracts lesson metadata (title, grade, lesson number), and generates an `index.html` file. Runs automatically in CI after new presentations are built.
- **`google_drive_upload.py`** — Uploads PDF/HTML artifacts to Google Drive folders by grade. Authenticates via service account credentials (set via `GDRIVE_CREDENTIALS_FILE` env var or `creds.json`).

### Custom Skill

- **`skills/nush-lesson-planner/`** — Claude Code skill for planning and generating Marp presentations in Ukrainian. Supports the full range of grades (5–12). The skill is also linked from `.claude/`, `.gemini/`, and `.opencode/` directories for use across multiple AI platforms.

## Lessons and Naming Convention

Lessons are numbered sequentially within each grade using **2-digit zero-padded format**. File names follow this pattern:

```
<LESSON-NUMBER>-<LESSON-TITLE>.md
```

Examples: `05-basic-algorithms.md`, `46-inkscape-project.md`, `51-variables-in-details.md`

Lesson metadata (title, grade, number) is extracted from the presentation's `<title>` HTML tag during index generation.

## Linting

The repository uses `pre-commit` for basic checks:

```sh
pre-commit run --all-files
```

Current hooks: trailing-whitespace, end-of-file-fixer, check-yaml.

No Python or Markdown linters are currently configured.

## Presentation Format

- Presentations use Marp (Markdown syntax with front-matter for configuration)
- Slides are separated by `---`
- Assets (images) are placed in `content/<GRADE>/assets/<LESSON-NUMBER>/` and referenced as `assets/<LESSON-NUMBER>/image.png`
- Each presentation must include a `<title>` tag for the index page to extract the lesson name

## CI/CD

- **Trigger**: GitHub Actions workflow runs automatically on merge to `main`
- **Build Process**: All changed presentations are built into HTML, PDF, and PPTX formats
- **Upload**: Built artifacts are uploaded to Google Drive folders organized by grade
- **Cleanup**: Existing files with the same name are deleted and replaced on Google Drive
- **Artifacts**: PDF, HTML, and PPTX files should never be committed to git

## Important Env Vars

**Local Development** (Google Drive uploads):

- `GDRIVE_CREDENTIALS_FILE` — Path to service account JSON credentials (defaults to `creds.json`)
- `PUBLISH_DIR` — Directory containing built presentations (used by `build_index_page.py`)

**CI/CD** (GitHub Actions):

- `GDRIVE_CREDENTIALS` — Service account JSON credentials (stored in GitHub Secrets)
- `GRADE_*_FOLDER_ID` — Google Drive folder IDs for each grade (stored in GitHub Secrets)

## Notes

- See `AGENTS.md` for a runbook of build and helper script commands (intended for automated agents)
- The `nush-lesson-planner` skill is the primary way to create new lesson plans and Marp presentations
- Google Drive service account must be configured with Editor access to grade folders for uploads to work
