"""Load lesson markdown files and split them into bite-sized sections."""

from __future__ import annotations

from typing import List

from . import config


def load_lesson(day: int) -> str:
    path = config.LESSONS_DIR / f"day{day:02d}.md"
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return f"# Day {day}\n\nLesson content coming soon!"


def split_sections(markdown: str) -> List[str]:
    """Split on level-2 headings (``## ...``), ignoring ``##`` inside code fences."""
    sections: List[str] = []
    current: List[str] = []
    in_fence = False
    for line in markdown.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        if not in_fence and line.startswith("## ") and current:
            sections.append("\n".join(current).strip())
            current = []
        current.append(line)
    if current:
        sections.append("\n".join(current).strip())
    return [s for s in sections if s]
