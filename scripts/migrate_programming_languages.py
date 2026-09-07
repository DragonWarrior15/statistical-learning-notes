"""Generate an MkDocs-compatible Programming Languages migration snapshot.

This historical migration utility copies ``_notes/programming_languages`` into
``docs/notes/programming_languages`` and rewrites the Jekyll constructs used by
that collection. The reviewed content under ``docs/`` is authoritative, so
running this script in the repository will overwrite files in that destination.
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "_notes" / "programming_languages"
DESTINATION = ROOT / "docs" / "notes" / "programming_languages"

FRONT_MATTER = re.compile(r"\A---\s*\n(?P<data>.*?)\n---\s*\n", re.DOTALL)
RAW_TAG = re.compile(r"{%\s*(?:raw|endraw)\s*%}\s*\n?")
LIST_ITEM = re.compile(r"(?:[-*+] |\d+[.] )")
INLINE_FENCE = re.compile(r"^(?P<indent>\s*)(?P<marker>\d+[.])\s+(?P<fence>```.*)$")
EMPTY_LIST_ITEM = re.compile(r"^(?P<indent>\s*)(?P<marker>\d+[.])\s*$")

INDEX_CONTENT = """# Programming Languages

Notes and exercises covering programming languages, databases, and foundational
data structures and algorithms.

<div class="grid cards" markdown>

-   ## SQL

    SQL syntax, queries, and practice exercises.

    [Explore SQL →](sql/sql.md)

-   ## C

    Core concepts and examples in the C programming language.

    [Explore C →](c/C.md)

-   ## C++

    C++ concepts together with a multi-part exercise collection.

    [Explore C++ →](cpp/cpp.md)

-   ## Data structures and algorithms

    Foundational data structures and algorithmic techniques.

    [Explore data structures →](dsa/ds.md)

</div>
"""


def normalize_block_spacing(content: str, *, exercise: bool) -> str:
    """Separate blocks where Kramdown accepts spacing Python-Markdown does not."""
    normalized: list[str] = []
    in_fence = False

    expanded: list[str] = []
    for line in content.splitlines():
        inline_fence = INLINE_FENCE.match(line)
        if inline_fence:
            indent = inline_fence.group("indent")
            expanded.append(f'{indent}{inline_fence.group("marker")} &nbsp;')
            expanded.append(f'{indent}    {inline_fence.group("fence")}')
        else:
            empty_item = EMPTY_LIST_ITEM.match(line)
            if empty_item:
                expanded.append(f'{empty_item.group("indent")}{empty_item.group("marker")} &nbsp;')
            else:
                expanded.append(line)

    just_closed_fence = False
    for line in expanded:
        stripped = line.lstrip()
        if exercise and not in_fence and line.startswith("        ") and LIST_ITEM.match(line[8:]):
            line = line[4:]
            stripped = line.lstrip()
        if just_closed_fence and line.strip() and normalized and normalized[-1].strip():
            normalized.append("")
        just_closed_fence = False
        if stripped.startswith("```"):
            if not in_fence and normalized and normalized[-1].strip():
                normalized.append("")
            if in_fence:
                in_fence = False
                just_closed_fence = True
            else:
                in_fence = True
        elif (
            not in_fence
            and LIST_ITEM.match(stripped)
            and normalized
            and normalized[-1].strip()
            and not LIST_ITEM.match(normalized[-1].lstrip())
        ):
            normalized.append("")
        normalized.append(line)

    return "\n".join(normalized).rstrip() + "\n"


def convert_markdown(source: Path, destination: Path) -> None:
    content = source.read_text(encoding="utf-8")
    title = source.stem.replace("_", " ").title()
    front_matter = FRONT_MATTER.match(content)
    if front_matter:
        metadata = yaml.safe_load(front_matter.group("data")) or {}
        title = metadata.get("title", title)
        content = content[front_matter.end() :]

    # MkDocs does not interpret Liquid, so only remove the Jekyll wrappers that
    # protected C++ brace initializers. Preserve their enclosed code verbatim.
    content = RAW_TAG.sub("", content)
    content = normalize_block_spacing(content, exercise="exercises" in source.stem)

    if not re.match(r"\s*#\s+", content):
        content = f"# {title}\n\n{content.lstrip()}"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(content, encoding="utf-8")


def main() -> None:
    if not SOURCE.is_dir():
        raise SystemExit(f"Programming Languages source directory not found: {SOURCE}")

    for source in SOURCE.rglob("*"):
        if source.is_dir():
            continue
        destination = DESTINATION / source.relative_to(SOURCE)
        if source.suffix == ".md":
            convert_markdown(source, destination)
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)

    (DESTINATION / "index.md").write_text(INDEX_CONTENT, encoding="utf-8")
    print(f"Generated {DESTINATION.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
