"""Generate an MkDocs-compatible Probability proof of concept.

The Jekyll source remains the authority during the migration. This script copies
only ``_notes/probability`` into ``docs/probability`` and rewrites the small
set of Jekyll constructs found in that subject.
"""

from __future__ import annotations

import re
import shutil
import os
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "_notes" / "probability"
DOCS = ROOT / "docs"
DESTINATION = DOCS / "probability"
NAVIGATION = ROOT / "_data" / "navigation.yml"
CONFIG = ROOT / "mkdocs.probability.yml"

FRONT_MATTER = re.compile(r"\A---\s*\n(?P<data>.*?)\n---\s*\n", re.DOTALL)
IMAGE_INCLUDE = re.compile(r"{%\s*include\s+image\.html\s+(?P<args>.*?)%}", re.DOTALL)
JEKYLL_LINK = re.compile(
    r'{{\s*"(?P<path>/notes/probability/[^"#]+\.html)(?P<anchor>#[^"]*)?"\s*\|\s*relative_url\s*}}'
)
BARE_LINK = re.compile(r"(?P<path>/notes/probability/[^\s)\"']+\.html)(?P<anchor>#[^\s)\"']+)?")
ATTR = re.compile(r'(\w+)=(?:"(?P<quoted>[^"]*)"|(?P<bare>[^\s]+))')
ALIGN_ENVIRONMENT = re.compile(r"\\(?P<tag>begin|end)\{align\*?\}")
DISPLAY_ENVIRONMENT = re.compile(
    r"(?m)^(?P<indent>[ \t]*)(?P<math>\\begin\{(?P<environment>align|alignat|equation|gather)\*?\}.*?\\end\{(?P=environment)\*?\})",
    re.DOTALL,
)


def attributes(args: str) -> dict[str, str]:
    return {
        match.group(1): match.group("quoted") or match.group("bare") or ""
        for match in ATTR.finditer(args)
    }


def relative_link(current: Path, jekyll_path: str, anchor: str = "") -> str:
    """Turn a Jekyll collection URL into a relative MkDocs source link."""
    target = DOCS / jekyll_path.removeprefix("/notes/").replace(".html", ".md")
    return Path(os.path.relpath(target, current.parent)).as_posix() + anchor


def image_markup(current: Path, args: str) -> str:
    attrs = attributes(args)
    url = attrs.get("url")
    if not url:
        raise ValueError(f"Image include has no URL in {current}")

    image = DOCS / url.removeprefix("notes/")
    source = Path(os.path.relpath(image, current.parent)).as_posix()
    classes = attrs.get("img_classes", "notes-img")
    description = attrs.get("description", "")
    caption = f"\n  <figcaption>{description}</figcaption>" if description else ""
    return f'<figure class="{classes}">\n  <img src="{source}" alt="{description}">{caption}\n</figure>'


def display_math_markup(match: re.Match[str]) -> str:
    """Render an unnumbered display-math block."""
    # ``align`` numbers every row. ``aligned`` preserves the alignment inside
    # one display-math block without introducing equation numbers.
    math = ALIGN_ENVIRONMENT.sub(lambda item: f"\\{item.group('tag')}{{aligned}}", match.group("math"))
    return f"\n$$\n{math}\n$$\n"


def flatten_exercise_lists(content: str) -> str:
    """Turn exercise lists into portable numbered labels.

    Python-Markdown treats indented display math inside ordered lists as code.
    The source commonly uses ``1.`` for automatic numbering, so calculate the
    visible number here and dedent each item's body before math conversion.
    """
    flattened: list[str] = []
    in_list = False
    next_number = 1
    marker = re.compile(r"^(?P<number>\d+)\.\s*(?P<text>.*)$")

    for line in content.splitlines():
        match = marker.match(line)
        if match:
            source_number = int(match.group("number"))
            number = next_number if in_list and source_number == 1 else source_number
            flattened.append(f"{number}\\. {match.group('text')}".rstrip())
            next_number = number + 1
            in_list = True
        elif in_list and line.startswith("    "):
            flattened.append(line[4:])
        else:
            flattened.append(line)
            if line.strip():
                in_list = False
                next_number = 1

    return "\n".join(flattened) + "\n"


def convert_markdown(source: Path, destination: Path) -> None:
    content = source.read_text(encoding="utf-8")
    title = source.stem.replace("_", " ").title()
    front_matter = FRONT_MATTER.match(content)
    if front_matter:
        metadata = yaml.safe_load(front_matter.group("data")) or {}
        title = metadata.get("title", title)
        content = content[front_matter.end() :]

    if "chapters/exercises" in source.as_posix():
        content = flatten_exercise_lists(content)

    content = IMAGE_INCLUDE.sub(lambda match: image_markup(destination, match.group("args")), content)
    content = JEKYLL_LINK.sub(
        lambda match: relative_link(destination, match.group("path"), match.group("anchor") or ""), content
    )
    content = BARE_LINK.sub(
        lambda match: relative_link(destination, match.group("path"), match.group("anchor") or ""), content
    )
    content = content.replace("{{ site.url }}", "https://dragonwarrior15.github.io/statistical-learning-notes/")
    content = content.replace("{{ site.baseurl }}", "")
    # Jekyll's MathJax setup processes bare TeX environments. Arithmatex only
    # passes display math through to MathJax when it is delimited explicitly.
    content = DISPLAY_ENVIRONMENT.sub(display_math_markup, content)

    if not re.match(r"\s*#\s+", content):
        content = f"# {title}\n\n{content.lstrip()}"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(content, encoding="utf-8")


def nav_entry(item: dict) -> dict[str, object]:
    children = [nav_entry(child) for child in item.get("subnav", [])]
    link = item.get("link")
    if link and children:
        return {item["name"]: [link.removeprefix("/notes/").replace(".html", ".md"), *children]}
    if link:
        return {item["name"]: link.removeprefix("/notes/").replace(".html", ".md")}
    return {item["name"]: children}


def write_config() -> None:
    navigation = yaml.safe_load(NAVIGATION.read_text(encoding="utf-8"))
    config = {
        "site_name": "Learning Notes — Probability",
        "docs_dir": "docs",
        "site_dir": "site/probability",
        "use_directory_urls": False,
        "theme": {
            "name": "material",
            "features": [
                "navigation.footer",
                "navigation.indexes",
                "navigation.sections",
                "navigation.top",
                "search.highlight",
                "search.suggest",
                "toc.follow",
            ],
        },
        "plugins": ["search"],
        # Answers and references are linked from the exercises, but deliberately
        # excluded from the global reading order used by the original site.
        "not_in_nav": "probability/chapters/references.md\nprobability/chapters/exercises/a_*.md\n",
        "extra_css": ["stylesheets/extra.css"],
        "extra_javascript": [
            "javascripts/mathjax.js",
            "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js",
        ],
        "markdown_extensions": [
            "admonition",
            "attr_list",
            "tables",
            {"toc": {"permalink": True}},
            {"pymdownx.arithmatex": {"generic": True}},
            {"pymdownx.highlight": {"anchor_linenums": True, "pygments_lang_class": True}},
            "pymdownx.inlinehilite",
            "pymdownx.superfences",
        ],
        "nav": [{"Home": "index.md"}, {"Probability": [nav_entry(item) for item in navigation["probability"]]}],
    }
    CONFIG.write_text(yaml.safe_dump(config, sort_keys=False, allow_unicode=True), encoding="utf-8")


def main() -> None:
    if not SOURCE.is_dir():
        raise SystemExit(f"Probability source directory not found: {SOURCE}")

    for source in SOURCE.rglob("*"):
        if source.is_dir():
            continue
        destination = DESTINATION / source.relative_to(SOURCE)
        if source.suffix == ".md":
            convert_markdown(source, destination)
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)

    DOCS.mkdir(exist_ok=True)
    (DOCS / "index.md").write_text(
        "# Learning Notes\n\nThis MkDocs proof of concept currently contains the Probability notes.\n\n"
        "[Start reading Probability](probability/chapters/theorems/probability_theorems.md)\n",
        encoding="utf-8",
    )
    write_config()
    print(f"Generated {DESTINATION.relative_to(ROOT)} and {CONFIG.name}")


if __name__ == "__main__":
    main()
