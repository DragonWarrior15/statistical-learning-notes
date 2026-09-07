"""Generate an MkDocs-compatible Linear Algebra migration snapshot."""

from __future__ import annotations

import os
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "_notes" / "linalg"
DOCS = ROOT / "docs"
DESTINATION = DOCS / "notes" / "linalg"
FRONT_MATTER = re.compile(r"\A---\s*\n(?P<data>.*?)\n---\s*\n", re.DOTALL)
RELATIVE_URL = re.compile(
    r'{{\s*"(?P<path>/notes/[^"#]+\.html)(?P<anchor>#[^"]*)?"\s*\|\s*relative_url\s*}}'
)
BARE_LINK = re.compile(r"(?P<path>/notes/[^\s)\"']+\.html)(?P<anchor>#[^\s)\"']+)?")
ALIGN_ENVIRONMENT = re.compile(r"\\(?P<tag>begin|end)\{align\*?\}")
DISPLAY_ENVIRONMENT = re.compile(
    r"(?m)^(?P<indent>[ \t]*)(?P<math>\\begin\{(?P<environment>align|alignat|equation|gather)\*?\}.*?\\end\{(?P=environment)\*?\})",
    re.DOTALL,
)
INDEX_CONTENT = """# Linear Algebra

Notes on vector spaces, linear maps, matrices, linear equations, and
eigenvalues.

<div class="grid cards" markdown>

-   ## Vector spaces

    [Start with complex fields →](vector_spaces/complex.md)

-   ## Linear maps

    [Explore linear maps and matrices →](linear_maps/linear_maps.md)

-   ## Linear equations

    [Study elimination and eigenvalues →](linear_eq/elimination.md)

-   ## Exercises

    [Work through exercises →](exercises/problems.md)

</div>
"""


def relative_link(current: Path, path: str, anchor: str = "") -> str:
    target = DOCS / path.removeprefix("/").replace(".html", ".md")
    return Path(os.path.relpath(target, current.parent)).as_posix() + anchor


def display_math(match: re.Match[str]) -> str:
    math = ALIGN_ENVIRONMENT.sub(lambda item: f'\\{item.group("tag")}{{aligned}}', match.group("math"))
    return f"\n$$\n{math}\n$$\n"


def flatten_exercise(content: str) -> str:
    lines: list[str] = []
    in_item = False
    for line in content.splitlines():
        marker = re.match(r"^(?P<number>\d+)\.\s+(?P<text>.*)$", line)
        if marker:
            lines.append(f'{marker.group("number")}\\. {marker.group("text")}'.rstrip())
            in_item = True
        elif in_item and line.startswith("    "):
            lines.append(line[4:])
        else:
            lines.append(line)
            if line.strip():
                in_item = False
    return "\n".join(lines) + "\n"


def convert(source: Path, destination: Path) -> None:
    content = source.read_text(encoding="utf-8")
    title = source.stem.replace("_", " ").title()
    front_matter = FRONT_MATTER.match(content)
    if front_matter:
        title = (yaml.safe_load(front_matter.group("data")) or {}).get("title", title)
        content = content[front_matter.end():]
    if source == SOURCE / "exercises" / "problems.md":
        content = flatten_exercise(content)
    content = RELATIVE_URL.sub(
        lambda match: relative_link(destination, match.group("path"), match.group("anchor") or ""), content
    )
    content = content.replace("{{ site.baseurl }}", "")
    content = BARE_LINK.sub(
        lambda match: relative_link(destination, match.group("path"), match.group("anchor") or ""), content
    )
    content = content.replace("{{ site.url }}", "https://dragonwarrior15.github.io/statistical-learning-notes/")
    content = DISPLAY_ENVIRONMENT.sub(display_math, content)
    if not re.match(r"\s*#\s+", content):
        content = f"# {title}\n\n{content.lstrip()}"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(content.rstrip() + "\n", encoding="utf-8")


def main() -> None:
    for source in SOURCE.rglob("*.md"):
        convert(source, DESTINATION / source.relative_to(SOURCE))
    DESTINATION.mkdir(parents=True, exist_ok=True)
    (DESTINATION / "index.md").write_text(INDEX_CONTENT, encoding="utf-8")
    print(f"Generated {DESTINATION.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
