#!/usr/bin/env python3
"""Fast sanity checks for Marp presentations.

Marp CLI converts almost anything without complaint, so this script catches
problems it silently accepts: broken front matter, missing images, unbalanced
HTML wrappers, misspelled directives.

Usage: python tools/check_marp.py <deck.md> [<deck.md> ...]
Prints ``path:line: message`` per problem; exits 1 if any were found.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import NamedTuple
from urllib.parse import unquote

import yaml

DEFAULT_TEMPLATE = Path(__file__).resolve().parent.parent / "templates" / "gaia_template.md"

KNOWN_DIRECTIVES = {
    "class", "paginate", "header", "footer", "backgroundColor",
    "backgroundImage", "backgroundPosition", "backgroundRepeat",
    "backgroundSize", "color", "theme", "style", "headingDivider", "size",
    "math", "title", "description", "author", "image", "keywords", "url",
    "marp", "lang",
}

FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
INLINE_CODE_RE = re.compile(r"(`+)(.+?)\1")
COMMENT_RE = re.compile(r"<!--(.*?)-->", re.DOTALL)
DIRECTIVE_LINE_RE = re.compile(r"^\s*_?([A-Za-z][A-Za-z0-9]*)\s*:")
OPEN_TAG_RE = re.compile(r"<(div|section)\b[^>]*?(?<!/)>", re.IGNORECASE)
CLOSE_TAG_RE = re.compile(r"</(div|section)\s*>", re.IGNORECASE)
H1_RE = re.compile(r"^#\s+\S")
IMAGE_RES = (
    re.compile(r"!\[[^\]]*\]\(\s*<?([^)\s>]+)"),
    re.compile(r"<img\b[^>]*?\bsrc\s*=\s*[\"']([^\"']+)[\"']", re.IGNORECASE),
    re.compile(r"url\(\s*[\"']?([^\"')]+?)[\"']?\s*\)"),
)
SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:|^//|^#")


class Problem(NamedTuple):
    line: int
    message: str


class Slide(NamedTuple):
    start_line: int
    lines: list[str]  # code-masked: fenced code blanked, inline code -> spaces


class Deck(NamedTuple):
    path: Path
    front_matter: dict | None
    front_matter_error: str | None
    fm_end_line: int  # 1-based line of the closing ``---``; 0 if none
    slides: list[Slide]
    raw_lines: list[str]


def _mask_code(lines: list[str]) -> list[str]:
    masked: list[str] = []
    fence: str | None = None
    for line in lines:
        m = FENCE_RE.match(line)
        if fence is None and m:
            fence = m.group(1)
            masked.append("")
        elif fence is not None:
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                fence = None
            masked.append("")
        else:
            masked.append(INLINE_CODE_RE.sub(lambda c: " " * len(c.group(0)), line))
    return masked


def parse_deck(path: Path) -> Deck:
    path = Path(path)
    text = path.read_text(encoding="utf-8")  # universal newlines: CRLF -> LF
    raw_lines = text.split("\n")
    if raw_lines and raw_lines[-1] == "":
        raw_lines.pop()

    front_matter: dict | None = None
    error: str | None = None
    fm_end = 0
    if raw_lines and raw_lines[0].rstrip() == "---":
        for i in range(1, len(raw_lines)):
            if raw_lines[i].rstrip() == "---":
                fm_end = i + 1
                break
        if fm_end == 0:
            error = "front matter is not closed with ---"
        else:
            try:
                data = yaml.safe_load("\n".join(raw_lines[1 : fm_end - 1]))
            except yaml.YAMLError as exc:
                error = f"front matter is not valid YAML: {' '.join(str(exc).split())}"
            else:
                if isinstance(data, dict):
                    front_matter = data
                else:
                    error = "front matter is not a YAML mapping"
    else:
        error = "missing front matter (the file must start with ---)"

    masked = _mask_code(raw_lines[fm_end:])
    slides: list[Slide] = []
    current: list[str] = []
    start = fm_end + 1
    for offset, line in enumerate(masked):
        if line.rstrip() == "---":
            slides.append(Slide(start, current))
            current = []
            start = fm_end + offset + 2
        else:
            current.append(line)
    slides.append(Slide(start, current))
    return Deck(path, front_matter, error, fm_end, slides, raw_lines)


def _check_front_matter(deck: Deck) -> list[Problem]:
    if deck.front_matter_error:
        return [Problem(1, deck.front_matter_error)]
    if deck.front_matter.get("marp") is not True:
        return [Problem(1, "front matter must contain marp: true")]
    return []


def _check_title(deck: Deck) -> list[Problem]:
    if deck.front_matter and deck.front_matter.get("title"):
        return []
    for slide in deck.slides:
        if any(H1_RE.match(line) for line in slide.lines):
            return []
    return [Problem(1, "no title: add title: to the front matter or a # heading")]


def _content_lines(deck: Deck):
    """Yield (line_number, masked_line) for every line after the front matter."""
    for slide in deck.slides:
        for i, line in enumerate(slide.lines):
            yield slide.start_line + i, line


def _check_images(deck: Deck) -> list[Problem]:
    problems = []
    fm_lines = ((i + 1, l) for i, l in enumerate(deck.raw_lines[: deck.fm_end_line]))
    for number, line in [*fm_lines, *_content_lines(deck)]:
        for regex in IMAGE_RES:
            for src in regex.findall(line):
                src = src.strip()
                if not src or SCHEME_RE.match(src):
                    continue
                rel = unquote(re.split(r"[?#]", src, maxsplit=1)[0])
                if not (deck.path.parent / rel).exists():
                    problems.append(Problem(number, f"image not found: {src}"))
    return problems


def _strip_comments(lines: list[str]) -> list[str]:
    text = "\n".join(lines)
    text = COMMENT_RE.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    return text.split("\n")


def _check_tags(deck: Deck) -> list[Problem]:
    problems = []
    last = len(deck.slides) - 1
    for index, slide in enumerate(deck.slides):
        stack: list[tuple[str, int]] = []
        for i, line in enumerate(_strip_comments(slide.lines)):
            number = slide.start_line + i
            events = [(m.start(), "open", m.group(1).lower()) for m in OPEN_TAG_RE.finditer(line)]
            events += [(m.start(), "close", m.group(1).lower()) for m in CLOSE_TAG_RE.finditer(line)]
            for _, kind, tag in sorted(events):
                if kind == "open":
                    stack.append((tag, number))
                elif stack and stack[-1][0] == tag:
                    stack.pop()
                else:
                    problems.append(Problem(number, f"</{tag}> has no matching <{tag}> on this slide"))
        for tag, number in stack:
            if index < last:
                brk = deck.slides[index + 1].start_line - 1
                problems.append(Problem(
                    number, f"<{tag}> is not closed before the --- slide break on line {brk}"
                ))
            else:
                problems.append(Problem(number, f"<{tag}> is not closed"))
    return problems


def _check_directives(deck: Deck) -> list[Problem]:
    problems = []
    for slide in deck.slides:
        text = "\n".join(slide.lines)
        for m in COMMENT_RE.finditer(text):
            body_lines = m.group(1).split("\n")
            keyed = [l for l in body_lines if l.strip()]
            if not keyed or not all(DIRECTIVE_LINE_RE.match(l) for l in keyed):
                continue
            first_line = slide.start_line + text.count("\n", 0, m.start())
            for offset, body_line in enumerate(body_lines):
                dm = DIRECTIVE_LINE_RE.match(body_line)
                if dm and dm.group(1) not in KNOWN_DIRECTIVES:
                    name = body_line.strip().split(":", 1)[0].strip()
                    problems.append(Problem(first_line + offset, f"unknown Marp directive: {name}"))
    return problems


def check_deck(deck: Deck, template_path: Path, skip_slide_limit: bool) -> list[Problem]:
    problems = _check_front_matter(deck)
    problems += _check_title(deck)
    problems += _check_images(deck)
    problems += _check_tags(deck)
    problems += _check_directives(deck)
    return sorted(problems, key=lambda p: p.line)


def main(argv: list[str] | None = None) -> int:
    paths = sys.argv[1:] if argv is None else argv
    failed = False
    for name in paths:
        deck = parse_deck(Path(name))
        for problem in check_deck(deck, DEFAULT_TEMPLATE, skip_slide_limit=False):
            print(f"{name}:{problem.line}: {problem.message}")
            failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
