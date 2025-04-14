import os
import pathlib
import re
import itertools

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


@dataclass
class PresentationFile:
    path: pathlib.Path
    file_name: str
    grade: str
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


def _index_grade_files(grade: int, lesson_files: list[PresentationFile]) -> str:
    """
    Create an index for the given grade and its lesson files.
    """
    index_content = f"\n## Уроки для {grade} Класу\n"
    for lesson_file in lesson_files:
        index_content += f"- Урок номер [{lesson_file.lesson_number}]({lesson_file.path})\n"

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


def _get_all_indexed_files(publish_dir: pathlib.Path) -> list[pathlib.Path]:
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
                lesson_file_path = grade_dir / lesson_file
                lesson_number_match = LESSON_NUMBER_MATCHER.match(lesson_file.name)
                if lesson_number_match:
                    lesson_number = int(lesson_number_match.group())
                    all_files.append(PresentationFile(
                        path=lesson_file_path,
                        file_name=lesson_file.name,
                        grade=grade,
                        lesson_number=lesson_number,
                    ))

    return all_files


if __name__ == "__main__":
    main()
