"""Generate an MkDocs-compatible Large Language Models migration snapshot."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "_notes" / "large_language_models"
DESTINATION = ROOT / "docs" / "notes" / "large_language_models"
FRONT_MATTER = re.compile(r"\A---\s*\n(?P<data>.*?)\n---\s*\n", re.DOTALL)
INDEX_CONTENT = """# Large Language Models

Notes on adapting large language models and engineering efficient inference
systems for language, image, and video generation.

<div class="grid cards" markdown>

-   ## Finetuning

    Adapt pretrained language models to specialized tasks and instructions.

    [Explore finetuning →](finetuning.md)

-   ## Inference engineering

    Model mechanics, bottlenecks, quantization, speculative decoding, caching,
    parallelism, and disaggregated serving.

    [Start with motivation →](inference_engineering/chapters/01_motivation.md)

</div>
"""


def normalize_lists(content: str) -> str:
    output: list[str] = []
    in_fence = False
    for line in content.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```"):
            in_fence = not in_fence
        if (
            not in_fence
            and line == stripped
            and re.match(r"[-*+] ", line)
            and output
            and output[-1].strip()
            and not re.match(r"[-*+] ", output[-1])
        ):
            output.append("")
        output.append(line)
    return "\n".join(output).rstrip() + "\n"


def convert(source: Path, destination: Path) -> None:
    content = source.read_text(encoding="utf-8")
    title = source.stem.replace("_", " ").title()
    front_matter = FRONT_MATTER.match(content)
    if front_matter:
        title = (yaml.safe_load(front_matter.group("data")) or {}).get("title", title)
        content = content[front_matter.end():]
    content = normalize_lists(content)
    heading = re.match(r"\s*##\s+(?P<title>[^\n]+)\n", content)
    if heading:
        content = f'# {heading.group("title")}\n' + content[heading.end():]
    elif not re.match(r"\s*#\s+", content):
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
