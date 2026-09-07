"""Generate an MkDocs-compatible Time Series migration snapshot."""

from __future__ import annotations

import os
import re
import shutil
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "_notes" / "time_series"
DOCS = ROOT / "docs"
DESTINATION = DOCS / "notes" / "time_series"
FRONT_MATTER = re.compile(r"\A---\s*\n(?P<data>.*?)\n---\s*\n", re.DOTALL)
ATTR = re.compile(r'(\w+)=(?:"(?P<quoted>[^"]*)"|(?P<bare>[^\s]+))')
JEKYLL_LINK = re.compile(
    r'{{\s*"(?P<path>/?notes/time_series/[^"#]+\.html)(?P<anchor>#[^"]*)?"\s*\|\s*relative_url\s*}}'
)
IMAGE_INCLUDE = re.compile(r"(?m)^[ \t]*{%\s*include\s+image\.html\s+(?P<args>.*?)%}")
CODE_INCLUDE = re.compile(
    r"{%\s*highlight\s+(?P<language>\w+).*?%}\s*"
    r"{%\s*include_relative\s+(?P<filename>[^\s%]+)\s*%}\s*"
    r"{%\s*endhighlight\s*%}",
    re.DOTALL,
)
CAPTURED_IMAGE = re.compile(
    r'{%\s*capture\s+img_url\s*%}\s*{{\s*"(?P<link>notes/time_series/[^"#]+\.html)"\s*\|\s*relative_url\s*}}\s*{%\s*endcapture\s*%}\s*'
    r'{%\s*capture\s+img_desc\s*%}\s*{{\s*"(?P<description>.*?)"\s*}}\s*{%\s*endcapture\s*%}\s*'
    r'{%\s*include\s+image\.html\s+(?P<args>.*?)%}',
    re.DOTALL,
)
ALIGN_ENVIRONMENT = re.compile(r"\\(?P<tag>begin|end)\{align\*?\}")
DISPLAY_ENVIRONMENT = re.compile(
    r"(?m)^(?P<indent>[ \t]*)(?P<math>\\begin\{(?P<environment>align|alignat|equation|gather)\*?\}.*?\\end\{(?P=environment)\*?\})",
    re.DOTALL,
)
LOCAL_ANCHOR = re.compile(r"(?P<prefix>\]\(#)(?P<anchor>[^)]+)(?P<suffix>\))")
INDEX_CONTENT = """# Time Series

Notes on time-series structure, dependence, ARIMA models, exponential
smoothing, and practical simulations.

<div class="grid cards" markdown>

-   ## Characteristics

    Formulations, measures of dependence, and exercises.

    [Explore characteristics →](chapters/characteristics/characteristics.md)

-   ## ARIMA

    Backward shifts, smoothing, AR, MA, ARMA, ARIMA, and a walkthrough.

    [Explore ARIMA →](chapters/arima/backward_shift.md)

-   ## Exponential smoothing

    Simple, trend-aware, and seasonal exponential smoothing.

    [Explore smoothing →](chapters/ses/ses.md)

-   ## Code and simulations

    Python implementations for ACF, PACF, ARIMA, SARMA, and smoothing.

    [Browse simulations →](codes/time_series_python.md)

</div>
"""


def attributes(args: str) -> dict[str, str]:
    return {
        match.group(1): match.group("quoted") or match.group("bare") or ""
        for match in ATTR.finditer(args)
    }


def relative_link(current: Path, path: str, anchor: str = "") -> str:
    target = DOCS / path.lstrip("/").replace(".html", ".md")
    return Path(os.path.relpath(target, current.parent)).as_posix() + anchor


def figure(current: Path, args: str, description: str | None = None) -> str:
    attrs = attributes(args)
    url = attrs.get("url")
    if not url:
        raise ValueError(f"Image include has no URL in {current}")
    source = Path(os.path.relpath(DOCS / url.lstrip("/"), current.parent)).as_posix()
    description = attrs.get("description", "") if description is None else description
    classes = attrs.get("img_classes", "notes-img")
    caption = f"\n  <figcaption>{description}</figcaption>" if description else ""
    return f'<figure class="{classes}">\n  <img src="{source}" alt="{re.sub(r"<.*?>", "", description)}">{caption}\n</figure>'


def captured_figure(current: Path, match: re.Match[str]) -> str:
    link = relative_link(current, match.group("link"))
    description = match.group("description").replace(
        "<a href='\" | append: img_url | append: \"'>", f'<a href="{link}">'
    )
    return figure(current, match.group("args"), description)


def included_code(source: Path, match: re.Match[str]) -> str:
    included = source.parent / match.group("filename")
    code = included.read_text(encoding="utf-8").rstrip()
    return f'```{match.group("language")}\n{code}\n```'


def display_math(match: re.Match[str]) -> str:
    math = ALIGN_ENVIRONMENT.sub(lambda item: f'\\{item.group("tag")}{{aligned}}', match.group("math"))
    return f"\n$$\n{math}\n$$\n"


def convert(source: Path, destination: Path) -> None:
    content = source.read_text(encoding="utf-8")
    title = source.stem.replace("_", " ").title()
    front_matter = FRONT_MATTER.match(content)
    if front_matter:
        title = (yaml.safe_load(front_matter.group("data")) or {}).get("title", title)
        content = content[front_matter.end():]
    content = CODE_INCLUDE.sub(lambda match: included_code(source, match), content)
    content = CAPTURED_IMAGE.sub(lambda match: captured_figure(destination, match), content)
    content = IMAGE_INCLUDE.sub(lambda match: figure(destination, match.group("args")), content)
    content = JEKYLL_LINK.sub(
        lambda match: relative_link(destination, match.group("path"), match.group("anchor") or ""), content
    )
    content = LOCAL_ANCHOR.sub(
        lambda match: match.group("prefix") + match.group("anchor").lower() + match.group("suffix"),
        content,
    )
    content = DISPLAY_ENVIRONMENT.sub(display_math, content)
    if not re.match(r"\s*#\s+", content):
        content = f"# {title}\n\n{content.lstrip()}"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(content.rstrip() + "\n", encoding="utf-8")


def main() -> None:
    for source in SOURCE.rglob("*"):
        if source.is_dir():
            continue
        destination = DESTINATION / source.relative_to(SOURCE)
        if source.suffix == ".md":
            convert(source, destination)
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
    (DESTINATION / "index.md").write_text(INDEX_CONTENT, encoding="utf-8")
    print(f"Generated {DESTINATION.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
