import os
import pathlib
import re
import itertools
import logging

from dataclasses import dataclass

import markdown

PUBLISH_DIR = os.environ.get("PUBLISH_DIR", "publish")
INDEX_EXT = ".html"

LESSON_NUMBER_MATCHER = re.compile(r"^\d+")

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Презентації для уроків інформатики НУШ</title>
</head>
<body>
{html_content}
</body>
</html>
"""

LESSON_TITLE_MATCHER = re.compile(r"<title>(?P<lesson_title>.+)</title>")


@dataclass
class PresentationFile:
    lesson_dir: pathlib.Path
    path: pathlib.Path
    file_name: str
    grade: int
    lesson_number: int


def main():
    markdown_text = """\
# Список уроків з інформатики НУШ

"""

    lessons_dir = pathlib.Path(PUBLISH_DIR)

    indexable_files = _get_all_indexed_files(lessons_dir)

    indexable_files.sort(key=lambda f: (f.grade, f.lesson_number))

    for f in itertools.groupby(indexable_files, key=lambda f: f.grade):
        grade_number, grade_files = f
        markdown_text += _index_grade_files(grade_number, list(grade_files))

    print(markdown_text)

    _create_index_file(markdown_text, lessons_dir)


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


def _build_index_lesson_name(
    lesson_number: int,
    lesson_human_readable_name: str | None,
    lesson_file_path: pathlib.Path,
) -> str:
    """Build lesson name for the index file.

    Args:
        lesson_number (int) lesson number
        lesson_human_readable_name (str): lesson name extracted from file or None.
        lesson_file_path (pathlib.Path): path to the lesson file1

    Args:
        str, Lesson name for the index file list.
    """
    lesson_name = str(lesson_number)
    if lesson_human_readable_name:
        lesson_name += f": {lesson_human_readable_name}"

    return f"- Урок [{lesson_name}]({lesson_file_path})\n"


def _index_grade_files(grade: int, lesson_files: list[PresentationFile]) -> str:
    """
    Create an index for the given grade and its lesson files.
    """
    index_content = f"\n## Уроки для {grade} Класу\n"
    for lesson_file in lesson_files:
        lesson_name = _get_lesson_human_readable_name(lesson_file)
        index_content += _build_index_lesson_name(
            lesson_file.lesson_number, lesson_name, lesson_file.path
        )

    return index_content


def _create_index_file(markdown_text: str, publish_dir: pathlib.Path) -> None:
    """
    Create an index file in the given directory.
    """
    index_file_path = publish_dir / "index.html"
    with open(index_file_path, "w", encoding="utf-8") as f:
        full_html = HTML_TEMPLATE.format(
            html_content=markdown.markdown(markdown_text, output_format="html")
        )
        f.write(full_html)


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
