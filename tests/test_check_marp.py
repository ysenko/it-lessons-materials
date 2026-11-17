import contextlib
import io
import os
import re
import sys
import tempfile
import unittest
import unittest.mock
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "tools"))

from check_marp import (  # noqa: E402
    DEFAULT_TEMPLATE,
    check_deck,
    main,
    parse_deck,
    slide_limit_skipped,
)


def _valid_deck() -> str:
    text = DEFAULT_TEMPLATE.read_text(encoding="utf-8")
    text = (
        text.replace("<REPLACE-WITH-ACTUAL-GRADE>", "7")
        .replace("<REPLACE-WITH-ACTUAL-LESSON-NUMBER>", "22")
        .replace("REPLACE WITH LESSON TITLE", "Типи даних")
        .replace("REPLACE WITH LESSON NUMBER", "22")
    )
    return text.rstrip("\n") + (
        "\n\n---\n\n## 🏠 Домашнє завдання\n\n"
        "1. 📖 Опрацювати конспект уроку.\n"
        "2. 📚 Опрацювати матеріали підручника **с. 82–86**.\n"
    )


VALID_DECK = _valid_deck()
# Line number of the first line after the front matter, i.e. where test
# snippets inserted by `with_slide` start.
CONTENT_MARKER = "## 🎯 Сьогодні ми дізнаємося"


def with_slide(body: str) -> str:
    """Insert an extra slide right before the goals slide."""
    return VALID_DECK.replace(CONTENT_MARKER, body + "\n\n---\n\n" + CONTENT_MARKER, 1)


def line_of(text: str, needle: str) -> int:
    for i, line in enumerate(text.splitlines(), start=1):
        if needle in line:
            return i
    raise AssertionError(f"{needle!r} not in text")


class Base(unittest.TestCase):
    skip_slide_limit = False

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def write_deck(self, text: str, newline: str = "\n") -> Path:
        path = self.dir / "22-deck.md"
        with open(path, "w", encoding="utf-8", newline=newline) as f:
            f.write(text)
        return path

    def check(self, text: str, newline: str = "\n", skip_slide_limit=None):
        if skip_slide_limit is None:
            skip_slide_limit = self.skip_slide_limit
        deck = parse_deck(self.write_deck(text, newline))
        return check_deck(deck, DEFAULT_TEMPLATE, skip_slide_limit=skip_slide_limit)

    def problems(self, text: str, **kw) -> list[str]:
        return [p.message for p in self.check(text, **kw)]

    def assertProblem(self, text: str, fragment: str, **kw):
        msgs = self.problems(text, **kw)
        self.assertTrue(
            any(fragment in m for m in msgs), f"{fragment!r} not in {msgs}"
        )


class TechnicalChecks(Base):
    def test_valid_deck_has_no_problems(self):
        self.assertEqual(self.problems(VALID_DECK), [])

    def test_missing_front_matter(self):
        self.assertProblem("# Заголовок\n\nТекст\n", "front matter")

    def test_invalid_yaml(self):
        text = VALID_DECK.replace("paginate: true", "paginate: true\nbad: [unclosed", 1)
        self.assertProblem(text, "YAML")

    def test_marp_not_true(self):
        self.assertProblem(VALID_DECK.replace("marp: true", "marp: false", 1), "marp: true")

    def test_missing_title(self):
        text = VALID_DECK.replace("# Типи даних", "Типи даних", 1)
        self.assertProblem(text, "title")

    def test_missing_local_image(self):
        text = with_slide("## Картинка\n\n![](assets/99/nope.png)")
        found = [p for p in self.check(text) if "assets/99/nope.png" in p.message]
        self.assertEqual(len(found), 1, self.problems(text))
        self.assertEqual(found[0].line, line_of(text, "assets/99/nope.png"))

    def test_existing_image_with_space_and_cyrillic(self):
        (self.dir / "assets" / "1").mkdir(parents=True)
        (self.dir / "assets" / "1" / "фото 1.png").write_bytes(b"png")
        text = with_slide(
            '## Фото\n\n![w:300](assets/1/фото%201.png)\n\n<img src="assets/1/фото 1.png">'
        )
        self.assertEqual(self.problems(text), [])

    def test_remote_and_data_images_ignored(self):
        text = with_slide(
            "<!-- _backgroundImage: url('https://example.com/bg.svg') -->\n"
            "## Фото\n\n"
            '<img src="https://example.com/a.png">\n\n'
            '<img src="data:image/png;base64,AAAA">\n\n'
            "![](https://example.com/b.png)"
        )
        self.assertEqual(self.problems(text), [])

    def test_unclosed_div(self):
        text = with_slide('## Картка\n\n<div class="card">\n\nТекст')
        found = [p for p in self.check(text) if "<div>" in p.message]
        self.assertEqual(len(found), 1, self.problems(text))
        self.assertEqual(found[0].line, line_of(text, '<div class="card">'))

    def test_slide_break_inside_section(self):
        text = with_slide(
            '<section class="task">\n\n## Завдання\n\n---\n\nТекст\n\n</section>'
        )
        self.assertProblem(text, "---")

    def test_unknown_directive(self):
        self.assertProblem(with_slide("<!-- _clas: lead -->\n# Розділ"), "_clas")

    def test_notes_comment_ignored(self):
        text = with_slide(
            "## Слайд\n\n<!-- Вчитель: пояснити приклад -->\n\n"
            "<!--\nДовга нотатка\nна кілька рядків\n-->"
        )
        self.assertEqual(self.problems(text), [])

    def slide_count(self, text: str) -> int:
        return len(parse_deck(self.write_deck(text)).slides)

    def test_dash_break_inside_comment_ignored(self):
        text = with_slide("## Слайд\n\n<!--\n\n---\n\n<div>\n-->")
        self.assertEqual(self.problems(text), [])
        self.assertEqual(self.slide_count(text), self.slide_count(VALID_DECK) + 1)

    def test_setext_heading_not_a_break(self):
        text = with_slide("## Слайд\n\nПідзаголовок\n---\n\nТекст")
        self.assertEqual(self.slide_count(text), self.slide_count(VALID_DECK) + 1)

    def test_dash_after_html_block_not_a_break(self):
        text = with_slide('<div class="card">\nТекст\n</div>\n---\n\n## Далі')
        self.assertEqual(self.slide_count(text), self.slide_count(VALID_DECK) + 1)

    def test_asterisk_rule_is_a_break(self):
        text = with_slide("## A\n\n***\n\n## B\n\n___\n\n## C")
        self.assertEqual(self.slide_count(text), self.slide_count(VALID_DECK) + 3)

    def test_bold_inline_code_not_a_break(self):
        text = with_slide("## Код\n\nДодати блок:\n**`встановити колір`**\n\nТекст")
        self.assertEqual(self.slide_count(text), self.slide_count(VALID_DECK) + 1)

    def test_dash_after_comment_is_a_break(self):
        text = with_slide("## A\n<!-- нотатка -->\n---\n\n## B")
        self.assertEqual(self.slide_count(text), self.slide_count(VALID_DECK) + 2)

    def test_indented_fence_in_list_masked(self):
        text = with_slide("## Код\n\n1. Крок\n    ```\n    ---\n    <section>\n    ```")
        self.assertEqual(self.problems(text), [])
        self.assertEqual(self.slide_count(text), self.slide_count(VALID_DECK) + 1)

    def test_capitalized_note_comment_ignored(self):
        text = with_slide("## Слайд\n\n<!-- TODO: замінити знімок -->\n<!-- Note: check -->")
        self.assertEqual(self.problems(text), [])

    def test_code_block_contents_ignored(self):
        code = (
            "## Код\n\n```python\nprint('---')\n---\n"
            "html = '<div>'\n# [x](https://a.b)\n```\n\n"
            "~~~\n---\n<section>\n~~~\n\n`<div>` і `https://a.b`"
        )
        text = with_slide(code)
        self.assertEqual(self.problems(text), [])
        base_slides = len(parse_deck(self.write_deck(VALID_DECK)).slides)
        self.assertEqual(len(parse_deck(self.write_deck(text)).slides), base_slides + 1)

    def test_crlf_line_endings(self):
        self.assertEqual(self.problems(VALID_DECK, newline="\r\n"), [])

    def test_crlf_line_numbers(self):
        text = with_slide("## Картинка\n\n![](assets/99/nope.png)")
        found = [p for p in self.check(text, newline="\r\n") if "nope" in p.message]
        self.assertEqual(found[0].line, line_of(text, "assets/99/nope.png"))

    def test_missing_trailing_newline(self):
        self.assertEqual(self.problems(VALID_DECK.rstrip("\n")), [])

    def test_main_exit_codes(self):
        good = self.write_deck(VALID_DECK)
        bad = self.dir / "bad.md"
        bad.write_text(with_slide("<!-- _clas: lead -->"), encoding="utf-8")
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(main([str(good)]), 0)
            self.assertEqual(main([str(bad)]), 1)
        self.assertRegex(out.getvalue(), rf"^{re.escape(str(bad))}:\d+: .*_clas")


def deck_with_counted_slides(n: int) -> str:
    """VALID_DECK padded to n slides, not counting the homework slide."""
    base = len(VALID_DECK.split("\n---\n")) - 2  # minus front matter, homework
    extra = "\n\n---\n\n".join(f"## Слайд {i}" for i in range(n - base))
    return with_slide(extra) if n > base else VALID_DECK


class SkillRules(Base):
    def test_markdown_url_link(self):
        self.assertProblem(with_slide("[сайт](https://example.com)"), "<a href")

    def test_autolink(self):
        self.assertProblem(with_slide("Див. <https://example.com>"), "<a href")

    def test_bare_url(self):
        self.assertProblem(with_slide("див. https://example.com"), "<a href")

    def test_bare_domain(self):
        self.assertProblem(with_slide("Відкрийте padlet.com"), "<a href")

    def test_url_inside_href_ok(self):
        text = with_slide(
            '<a href="https://e.com/x?a=1" target="_blank" rel="noopener noreferrer">сайт</a>'
        )
        self.assertEqual(self.problems(text), [])

    def test_url_in_code_block_ok(self):
        text = with_slide("```\ncurl https://example.com\n[x](https://a.b)\n```")
        self.assertEqual(self.problems(text), [])

    def test_anchor_without_target_blank(self):
        text = with_slide('<a href="https://e.com">сайт</a>')
        self.assertProblem(text, 'target="_blank"')

    def test_placeholder_replace(self):
        self.assertProblem(with_slide("REPLACE WITH LESSON TITLE"), "REPLACE")

    def test_placeholder_pages_en_dash(self):
        self.assertProblem(with_slide("Підручник с. ABC–XYZ"), "ABC–XYZ")

    def test_placeholder_pages_hyphen(self):
        self.assertProblem(with_slide("Підручник с. ABC-XYZ"), "ABC-XYZ")

    def test_safety_slide_not_second(self):
        text = VALID_DECK.replace(
            "## 🛡️ Пригадуємо: техніка безпеки", "## 📌 Інший слайд", 1
        )
        self.assertProblem(text, "техніка безпеки")

    def test_no_homework_slide(self):
        text = VALID_DECK.replace("## 🏠 Домашнє завдання", "## Підсумки", 1)
        self.assertProblem(text, "Домашнє завдання")

    def test_slide_limit_ok_at_14(self):
        self.assertEqual(self.problems(deck_with_counted_slides(14)), [])

    def test_slide_limit_exceeded_at_15(self):
        self.assertProblem(deck_with_counted_slides(15), "14")

    def test_slide_limit_skipped(self):
        text = deck_with_counted_slides(15).replace("marp: true", "marp: false", 1)
        msgs = self.problems(text, skip_slide_limit=True)
        self.assertFalse(any("14" in m for m in msgs), msgs)
        self.assertTrue(any("marp: true" in m for m in msgs), msgs)

    def test_slide_limit_skipped_env(self):
        self.assertIs(slide_limit_skipped({}), False)
        self.assertIs(slide_limit_skipped({"MARP_CHECK_SKIP_SLIDE_LIMIT": "1"}), True)
        self.assertIs(slide_limit_skipped({"MARP_CHECK_SKIP_SLIDE_LIMIT": "0"}), False)
        self.assertIs(slide_limit_skipped({"MARP_CHECK_SKIP_SLIDE_LIMIT": ""}), False)

    def test_main_reads_env_switch(self):
        path = self.write_deck(deck_with_counted_slides(15))
        out = io.StringIO()
        with contextlib.redirect_stdout(out), unittest.mock.patch.dict(
            os.environ, {"MARP_CHECK_SKIP_SLIDE_LIMIT": "1"}
        ):
            self.assertEqual(main([str(path)]), 0)

    def test_missing_css_class(self):
        text = VALID_DECK.replace("  .task {", "  .task-renamed {", 1)
        self.assertProblem(text, ".task")


if __name__ == "__main__":
    unittest.main()
