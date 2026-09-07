"""Generate an MkDocs-compatible Machine Learning migration snapshot."""

from __future__ import annotations

import os
import re
import shutil
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "_notes" / "machine_learning"
DOCS = ROOT / "docs"
DESTINATION = DOCS / "notes" / "machine_learning"
FRONT_MATTER = re.compile(r"\A---\s*\n(?P<data>.*?)\n---\s*\n", re.DOTALL)
ATTR = re.compile(r'(\w+)=(?:"(?P<quoted>[^"]*)"|(?P<bare>[^\s]+))')
RELATIVE_URL = re.compile(
    r'{{\s*"(?P<path>/?notes/[^"#]+\.html)(?P<anchor>#[^"]*)?"\s*\|\s*relative_url\s*}}'
)
IMAGE_INCLUDE = re.compile(r"(?m)^[ \t]*{%\s*include\s+image\.html\s+(?P<args>.*?)%}")
CODE_INCLUDE = re.compile(
    r"{%\s*highlight\s+(?P<language>\w+).*?%}\s*"
    r"{%\s*include_relative\s+(?P<filename>[^\s%]+)\s*%}\s*"
    r"{%\s*endhighlight\s*%}",
    re.DOTALL,
)
CAPTURED_IMAGE = re.compile(
    r'{%\s*capture\s+img_url\s*%}\s*{{\s*"(?P<link>notes/[^"#]+\.html)"\s*\|\s*relative_url\s*}}\s*{%\s*endcapture\s*%}\s*'
    r'{%\s*capture\s+img_desc\s*%}\s*{{\s*"(?P<description>.*?)"\s*}}\s*{%\s*endcapture\s*%}\s*'
    r'{%\s*include\s+image\.html\s+(?P<args>.*?)%}',
    re.DOTALL,
)
ALIGN_ENVIRONMENT = re.compile(r"\\(?P<tag>begin|end)\{align\*?\}")
DISPLAY_ENVIRONMENT = re.compile(
    r"(?m)^(?P<indent>[ \t]*)(?P<math>\\begin\{(?P<environment>align|alignat|aligned|equation|gather)\*?\}.*?\\end\{(?P=environment)\*?\})",
    re.DOTALL,
)
EXISTING_DISPLAY = re.compile(
    r"(?ms)^[ \t]*\$\$[ \t]*\n(?P<math>.*?)\n[ \t]*\$\$[ \t]*$"
)
INDEX_CONTENT = """# Machine Learning

Notes on regression, classification, model selection, non-linear methods,
trees, support vector machines, Bayesian methods, and clustering.

<div class="grid cards" markdown>

-   ## Supervised learning

    [Linear regression](chapters/regression/intro.md) ·
    [Classification](chapters/classification/intro.md) ·
    [Model selection](chapters/linear_model_selection_regularization/intro.md)

-   ## Non-linear models

    [Moving beyond linearity](chapters/moving_beyond_linearity/intro.md) ·
    [Tree-based models](chapters/tree_models/intro.md) ·
    [Support vector machines](chapters/svm/svm_intro.md)

-   ## Statistical methods

    [Resampling](chapters/resampling_methods/resampling_methods.md) ·
    [Bayesian methods](chapters/bayesian_methods/bayesian_methods.md) ·
    [Clustering](chapters/clustering/intro.md)

-   ## Supporting material

    [Appendix](chapters/appendix/bias_variance.md) ·
    [Code](codes/gaussian_process_prediction.md)

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
    caption_description = re.sub(r"\$(.+?)\$", r"\\(\1\\)", description)
    caption = f"\n  <figcaption>{caption_description}</figcaption>" if description else ""
    alt = re.sub(r"<.*?>", "", description).replace("$", "")
    return f'<figure class="{classes}">\n  <img src="{source}" alt="{alt}">{caption}\n</figure>'


def captured_figure(current: Path, match: re.Match[str]) -> str:
    link = relative_link(current, match.group("link"))
    description = match.group("description").replace(
        "<a href='\" | append: img_url | append: \"'>", f'<a href="{link}">'
    )
    return figure(current, match.group("args"), description)


def included_code(source: Path, match: re.Match[str]) -> str:
    code = (source.parent / match.group("filename")).read_text(encoding="utf-8").rstrip()
    return f'```{match.group("language")}\n{code}\n```'


def display_math(match: re.Match[str]) -> str:
    indent = match.group("indent")
    math = ALIGN_ENVIRONMENT.sub(lambda item: f'\\{item.group("tag")}{{aligned}}', match.group("math"))
    math = re.sub(r"\n[ \t]*\n", "\n", math)
    math = "\n".join(f"{indent}{line}" for line in math.splitlines())
    return f"\n{indent}$$\n{math}\n{indent}$$\n"


def protect_existing_displays(content: str) -> tuple[str, list[str]]:
    displays: list[str] = []

    def protect(match: re.Match[str]) -> str:
        math = ALIGN_ENVIRONMENT.sub(
            lambda item: f'\\{item.group("tag")}{{aligned}}', match.group("math")
        )
        math = re.sub(r"\n[ \t]*\n", "\n", math)
        token = f"MKDOCS_MACHINE_LEARNING_DISPLAY_{len(displays)}_END"
        displays.append(f"$$\n{math}\n$$")
        return f"\n\n{token}\n\n"

    return EXISTING_DISPLAY.sub(protect, content), displays


def convert(source: Path, destination: Path) -> None:
    content = source.read_text(encoding="utf-8")
    title = source.stem.replace("_", " ").title()
    front_matter = FRONT_MATTER.match(content)
    if front_matter:
        title = (yaml.safe_load(front_matter.group("data")) or {}).get("title", title)
        content = content[front_matter.end():]
    content, protected_displays = protect_existing_displays(content)
    content = CODE_INCLUDE.sub(lambda match: included_code(source, match), content)
    content = CAPTURED_IMAGE.sub(lambda match: captured_figure(destination, match), content)
    content = IMAGE_INCLUDE.sub(lambda match: figure(destination, match.group("args")), content)
    content = RELATIVE_URL.sub(
        lambda match: relative_link(destination, match.group("path"), match.group("anchor") or ""), content
    )
    content = DISPLAY_ENVIRONMENT.sub(display_math, content)
    for index, math in enumerate(protected_displays):
        content = content.replace(f"MKDOCS_MACHINE_LEARNING_DISPLAY_{index}_END", math)
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
