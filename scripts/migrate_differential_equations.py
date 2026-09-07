"""Generate an MkDocs-compatible Differential Equations migration snapshot."""

from __future__ import annotations

import os
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "_notes" / "differential_equations"
DOCS = ROOT / "docs"
DESTINATION = DOCS / "notes" / "differential_equations"
FRONT_MATTER = re.compile(r"\A---\s*\n(?P<data>.*?)\n---\s*\n", re.DOTALL)
RELATIVE_URL = re.compile(
    r'{{\s*"(?P<path>/notes/[^"#]+\.html)(?P<anchor>#[^"]*)?"\s*\|\s*relative_url\s*}}'
)
ALIGN_ENVIRONMENT = re.compile(r"\\(?P<tag>begin|end)\{align\*?\}")
DISPLAY_ENVIRONMENT = re.compile(
    r"(?m)^(?P<indent>[ \t]*)(?P<math>\\begin\{(?P<environment>align|alignat|equation|gather)\*?\}.*?\\end\{(?P=environment)\*?\})",
    re.DOTALL,
)
INDEX_CONTENT = """# Differential Equations

Notes on ordinary differential equations, solution methods, systems, series,
Laplace transforms, and exercises.

<div class="grid cards" markdown>

-   ## Foundations

    [Differential Equations](intro.md) ·
    [First-order ODEs](special_solutions.md)

-   ## Linear ODEs

    [Second order](order_two_linear.md) ·
    [Higher order](higher_order_linear.md) ·
    [Systems of ODEs](system_of_ode.md)

-   ## Transform methods

    [Series solutions](series_solutions.md) ·
    [Laplace transforms](laplace_transforms.md)

-   ## Practice

    [Browse exercises →](exercises.md)

</div>
"""


def relative_link(current: Path, path: str, anchor: str = "") -> str:
    target = DOCS / path.removeprefix("/").replace(".html", ".md")
    return Path(os.path.relpath(target, current.parent)).as_posix() + anchor


def display_math(match: re.Match[str]) -> str:
    math = ALIGN_ENVIRONMENT.sub(lambda item: f'\\{item.group("tag")}{{aligned}}', match.group("math"))
    return f"\n$$\n{math}\n$$\n"


def flatten_numbered_lists(content: str) -> str:
    lines: list[str] = []
    in_list = False
    next_number = 1
    for line in content.splitlines():
        marker = re.match(r"^(?P<number>\d+)\.\s+(?P<text>.*)$", line)
        if marker:
            source_number = int(marker.group("number"))
            number = next_number if in_list and source_number == 1 else source_number
            lines.append(f'{number}\\. {marker.group("text")}'.rstrip())
            next_number = number + 1
            in_list = True
        elif in_list and line.startswith("    "):
            lines.append(line[4:])
        else:
            lines.append(line)
            if line.strip():
                in_list = False
                next_number = 1
    return "\n".join(lines) + "\n"


def convert(source: Path, destination: Path) -> None:
    content = source.read_text(encoding="utf-8")
    title = source.stem.replace("_", " ").title()
    front_matter = FRONT_MATTER.match(content)
    if front_matter:
        title = (yaml.safe_load(front_matter.group("data")) or {}).get("title", title)
        content = content[front_matter.end():]
    if source == SOURCE / "exercises.md":
        content = flatten_numbered_lists(content)
    content = RELATIVE_URL.sub(
        lambda match: relative_link(destination, match.group("path"), match.group("anchor") or ""), content
    )
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
