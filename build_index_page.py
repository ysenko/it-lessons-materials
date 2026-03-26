import os
import pathlib
import re
import logging

from dataclasses import dataclass

from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import select_autoescape

PUBLISH_DIR = os.environ.get("PUBLISH_DIR", "publish")
INDEX_EXT = ".html"
INDEX_TEMPLATE = "index_page.html.j2"
TEMPLATES_DIR = pathlib.Path(__file__).parent / "templates"

LESSON_NUMBER_MATCHER = re.compile(r"^\d+")

LESSON_TITLE_MATCHER = re.compile(r"<title>(?P<lesson_title>.+)</title>")


@dataclass
class PresentationFile:
    lesson_dir: pathlib.Path
    path: pathlib.Path
    file_name: str
    grade: int
    lesson_number: int


def main():
    lessons_dir = pathlib.Path(PUBLISH_DIR)

    indexable_files = _get_all_indexed_files(lessons_dir)

    indexable_files.sort(key=lambda f: (f.grade, f.lesson_number))

    grouped_lessons = _group_lessons_by_grade(indexable_files)

    _create_index_file(grouped_lessons, lessons_dir)


def _get_lesson_human_readable_name(lesson_file: PresentationFile) -> str | None:
    """Read lesson name from the presentation file using regex.

    Params:
        lesson_file (PresentationFile): object representing the presentation file

    Returns:
        str with lesson name or None, it the function was unable to read lesson name.
    """
    try:
        with open(lesson_file.lesson_dir / lesson_file.path) as fin:
            matched_title_obj = LESSON_TITLE_MATCHER.search(fin.read())
    except Exception:
        logging.exception("Cannot extract lesson name from file.")
        return None

    if matched_title_obj is not None:
        return matched_title_obj.group("lesson_title")


def _group_lessons_by_grade(indexable_files: list[PresentationFile]) -> list[dict]:
    """Group lessons by grade and build a render-friendly structure."""
    grouped: dict[int, list[dict]] = {}

    for lesson_file in indexable_files:
        lesson_title = _get_lesson_human_readable_name(lesson_file)
        lesson_display_name = str(lesson_file.lesson_number)
        if lesson_title:
            lesson_display_name += f": {lesson_title}"

        grouped.setdefault(lesson_file.grade, []).append(
            {
                "display_name": lesson_display_name,
                "path": lesson_file.path.as_posix(),
                "lesson_number": lesson_file.lesson_number,
            }
        )

    return [
        {
            "grade": grade,
            "lessons": sorted(
                lessons,
                key=lambda lesson: lesson["lesson_number"],
            ),
        }
        for grade, lessons in sorted(grouped.items(), key=lambda item: item[0])
    ]


def _create_index_file(grouped_lessons: list[dict], publish_dir: pathlib.Path) -> None:
    """
    Create an index file in the given directory.
    """
    index_file_path = publish_dir / "index.html"
    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=select_autoescape(("html", "j2")),
    )
    template = env.get_template(INDEX_TEMPLATE)

    with open(index_file_path, "w", encoding="utf-8") as f:
        f.write(template.render(grouped_lessons=grouped_lessons))


def _get_all_indexed_files(publish_dir: pathlib.Path) -> list[PresentationFile]:
    """
    Get all indexable files in the given directory and its subdirectories.
    """
    all_files = []
    for grade_dir in publish_dir.iterdir():
        if not grade_dir.is_dir() or not grade_dir.name.isdigit():
            continue

        grade = int(grade_dir.name)

        for lesson_file in grade_dir.iterdir():
            if lesson_file.is_file() and lesson_file.name.endswith(INDEX_EXT):
                lesson_number_match = LESSON_NUMBER_MATCHER.match(lesson_file.name)
                if lesson_number_match:
                    lesson_number = int(lesson_number_match.group())
                    all_files.append(
                        PresentationFile(
                            lesson_dir=publish_dir,
                            path=lesson_file.relative_to(publish_dir),
                            file_name=lesson_file.name,
                            grade=grade,
                            lesson_number=lesson_number,
                        )
                    )

    return all_files


if __name__ == "__main__":
    main()
