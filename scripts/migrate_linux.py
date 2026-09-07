"""Generate an MkDocs-compatible Linux migration snapshot.

This historical migration utility copies ``_notes/linux`` into
``docs/notes/linux`` and rewrites the Jekyll constructs used by that collection.
The reviewed content under ``docs/`` is authoritative, so running this script in
the repository will overwrite files in that destination.
"""

from __future__ import annotations

import os
import re
import shutil
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "_notes" / "linux"
DOCS = ROOT / "docs"
DESTINATION = DOCS / "notes" / "linux"

FRONT_MATTER = re.compile(r"\A---\s*\n(?P<data>.*?)\n---\s*\n", re.DOTALL)
IMAGE_INCLUDE = re.compile(r"{%\s*include\s+image\.html\s+(?P<args>.*?)%}", re.DOTALL)
JEKYLL_LINK = re.compile(
    r'{{\s*"(?P<path>/notes/linux/[^"#]+\.html)(?P<anchor>#[^"]*)?"\s*\|\s*relative_url\s*}}'
)
ATTR = re.compile(r'(\w+)=(?:"(?P<quoted>[^"]*)"|(?P<bare>[^\s]+))')

INDEX_CONTENT = """# Linux

Practical notes on Linux command-line tools, text processing, containers, and
container orchestration.

## Command-line tools

<div class="grid cards" markdown>

- [Regular expressions](regex.md)
- [`find`](find.md)
- [`grep`](grep.md)
- [`curl`](curl.md)
- [`sed`](sed.md)

</div>

## Containers and orchestration

<div class="grid cards" markdown>

- [Docker](docker.md)
- [Kubernetes](kubernetes.md)

</div>
"""


def attributes(args: str) -> dict[str, str]:
    return {
        match.group(1): match.group("quoted") or match.group("bare") or ""
        for match in ATTR.finditer(args)
    }


def relative_link(current: Path, jekyll_path: str, anchor: str = "") -> str:
    target = DOCS / jekyll_path.removeprefix("/").replace(".html", ".md")
    return Path(os.path.relpath(target, current.parent)).as_posix() + anchor


def image_markup(current: Path, args: str) -> str:
    attrs = attributes(args)
    url = attrs.get("url")
    if not url:
        raise ValueError(f"Image include has no URL in {current}")

    image = DOCS / url.lstrip("/")
    source = Path(os.path.relpath(image, current.parent)).as_posix()
    classes = attrs.get("img_classes", "notes-img")
    description = attrs.get("description", "")
    caption = f"\n  <figcaption>{description}</figcaption>" if description else ""
    return f'<figure class="{classes}">\n  <img src="{source}" alt="{description}">{caption}\n</figure>'


def convert_markdown(source: Path, destination: Path) -> None:
    content = source.read_text(encoding="utf-8")
    title = source.stem.replace("_", " ").title()
    front_matter = FRONT_MATTER.match(content)
    if front_matter:
        metadata = yaml.safe_load(front_matter.group("data")) or {}
        title = metadata.get("title", title)
        content = content[front_matter.end() :]

    content = IMAGE_INCLUDE.sub(lambda match: image_markup(destination, match.group("args")), content)
    content = JEKYLL_LINK.sub(
        lambda match: relative_link(destination, match.group("path"), match.group("anchor") or ""), content
    )

    if not re.match(r"\s*#\s+", content):
        content = f"# {title}\n\n{content.lstrip()}"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(content, encoding="utf-8")


def main() -> None:
    if not SOURCE.is_dir():
        raise SystemExit(f"Linux source directory not found: {SOURCE}")

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
