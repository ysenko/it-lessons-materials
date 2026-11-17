import contextlib
import io
import re
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "tools"))

from check_marp import DEFAULT_TEMPLATE, check_deck, main, parse_deck  # noqa: E402


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


if __name__ == "__main__":
    unittest.main()
