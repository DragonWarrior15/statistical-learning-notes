"""Generate an MkDocs-compatible Maths Miscellaneous migration snapshot."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "_notes" / "maths_misc"
DESTINATION = ROOT / "docs" / "notes" / "maths_misc"
FRONT_MATTER = re.compile(r"\A---\s*\n(?P<data>.*?)\n---\s*\n", re.DOTALL)
ALIGN_ENVIRONMENT = re.compile(r"\\(?P<tag>begin|end)\{align\*?\}")
DISPLAY_ENVIRONMENT = re.compile(
    r"(?m)^(?P<indent>[ \t]*)(?P<math>\\begin\{(?P<environment>align|alignat|equation|gather)\*?\}.*?\\end\{(?P=environment)\*?\})",
    re.DOTALL,
)
INDEX_CONTENT = """# Maths Miscellaneous

Short mathematical questions, puzzles, and worked solutions.

<div class="grid cards" markdown>

- [Exponent and base reversed](exp_base_reversed.md)
- [Definite integral](definite_integral.md)
- [First to call 50](first_to_50.md)
- [Incremental remainders](incremental_remainders.md)

</div>
"""


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
