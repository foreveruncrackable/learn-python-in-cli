"""All terminal rendering lives here (rich)."""

from __future__ import annotations

import sys
import time

from rich import box
from rich.console import Console
from rich.markdown import Markdown
from rich.markup import escape
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table
from rich.text import Text

from . import storage
from .curriculum import CURRICULUM, TOTAL_DAYS
from .runner import RunResult, describe_construct

console = Console()

_animate = sys.stdout.isatty()


def set_animation(enabled: bool) -> None:
    global _animate
    _animate = enabled and sys.stdout.isatty()


def clear() -> None:
    console.clear()


BANNER = r"""
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║           🐍  30 DAYS OF PYTHON  🐍                          ║
    ║                                                              ║
    ║         Interactive CLI Learning Experience                  ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
"""


def show_banner() -> None:
    for line in BANNER.splitlines():
        console.print(line, style="bold yellow")
        if _animate:
            time.sleep(0.04)


def show_day_banner(day: int) -> None:
    entry = CURRICULUM[day - 1]
    console.print(Panel(
        f"[bold cyan]Day {day}[/bold cyan] — [bold green]{entry['title']}[/bold green]\n\n"
        f"Topics: {', '.join(entry['topics'])}",
        border_style="bright_blue", box=box.DOUBLE, padding=(1, 2),
    ))
    console.print()


def progress_bar(progress: dict) -> None:
    completed = len(progress["completed_days"])
    width = 30
    filled = int(width * completed / TOTAL_DAYS)
    bar = "█" * filled + "░" * (width - filled)
    streak = storage.current_streak(progress)
    extra = f"   🔥 {streak}-day streak" if streak > 1 else ""
    console.print(
        f"  [cyan]{completed / TOTAL_DAYS:>4.0%}[/cyan]  [green]{bar}[/green]  "
        f"[yellow]{completed}/{TOTAL_DAYS} days[/yellow]{extra}\n"
    )


def info(message: str) -> None:
    console.print(f"[dim]{message}[/dim]")


def success(message: str) -> None:
    console.print(f"[bold green]{message}[/bold green]")


def warn(message: str) -> None:
    console.print(f"[bold yellow]{message}[/bold yellow]")


def error(message: str) -> None:
    console.print(f"[bold red]{message}[/bold red]")


def show_markdown(text: str) -> None:
    console.print(Markdown(text))


def show_code(code: str, title: str = "") -> None:
    syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
    console.print(Panel(syntax, title=title, border_style="cyan", box=box.ROUNDED) if title else syntax)


# --------------------------------------------------------------- task display

def show_task(task, attempts: int, passed_before: bool, unavailable: list) -> None:
    status = "  [green]✓ done[/green]" if passed_before else (f"  [dim]attempts: {attempts}[/dim]" if attempts else "")
    console.print(f"\n[bold yellow]📝 Task: {task.title}[/bold yellow]{status}")
    show_markdown(task.instructions)
    if task.must_use:
        console.print("[dim]Your solution must use: " + ", ".join(describe_construct(s) for s in task.must_use) + "[/dim]")
    console.print(f"[dim]It will be checked with {len(task.cases)} test case(s).[/dim]\n")
    if unavailable:
        warn("This task needs: " + ", ".join(unavailable) + "  →  pip install " + " ".join(
            {"bs4": "beautifulsoup4"}.get(m, m) for m in unavailable))


def show_result(result: RunResult) -> None:
    if result.syntax_error:
        console.print(Panel(Text(result.syntax_error), title="Syntax error", border_style="red", box=box.ROUNDED))
        error("❌ Python couldn't read your code — fix the syntax and try again.")
        return

    table = Table(box=box.SIMPLE_HEAVY, show_edge=False, pad_edge=False)
    table.add_column("", width=2)
    table.add_column("Test", style="cyan", overflow="fold")
    table.add_column("Result", overflow="fold")
    failures = []
    for i, cr in enumerate(result.cases, 1):
        mark = "[green]✓[/green]" if cr.passed else "[red]✗[/red]"
        if cr.passed:
            note = "[green]passed[/green]"
        elif cr.timed_out:
            note = "[red]timed out (infinite loop?)[/red]"
        elif cr.error:
            note = "[red]error[/red]"
        else:
            note = "[red]wrong output[/red]"
        table.add_row(mark, escape(f"{i}. {cr.case.describe()}"), note)
        if not cr.passed:
            failures.append((i, cr))
    console.print(table)

    for i, cr in failures[:2]:
        body = ""
        if cr.error:
            body = cr.error
        elif not cr.timed_out:
            shown = cr.actual.strip() or "(no output)"
            expected = cr.case.expected if cr.case.mode != "nonempty" else "(any output)"
            if cr.case.mode == "contains":
                expected = f"output containing “{expected}”"
            body = f"expected:\n{expected}\n\nyou printed:\n{shown}"
        if body:
            console.print(Panel(Text(body), title=f"Test {i}", border_style="red", box=box.ROUNDED))
    if len(failures) > 2:
        info(f"…and {len(failures) - 2} more failing test(s).")

    for spec in result.missing_constructs:
        warn(f"⚠ This task needs {describe_construct(spec)} in your solution.")

    if result.passed:
        success(f"🎉 All {len(result.cases)} test(s) passed!")
    else:
        error(f"❌ {result.passed_count}/{len(result.cases)} tests passed — you've got this, try again!")


# --------------------------------------------------------------- tables

def days_table(progress: dict) -> None:
    from .tasks import get_day_tasks

    table = Table(box=box.ROUNDED, title="Your 30 days")
    table.add_column("Day", justify="right", style="cyan")
    table.add_column("Topic")
    table.add_column("Tasks", justify="center")
    table.add_column("Quiz", justify="center")
    table.add_column("", width=2)
    for entry in CURRICULUM:
        day = entry["day"]
        tasks = get_day_tasks(day)
        done = sum(1 for t in tasks if storage.task_passed(progress, day, t.id))
        quiz = progress["quiz_scores"].get(str(day))
        quiz_cell = f"{quiz['best']}/{quiz['total']}" if quiz else "[dim]–[/dim]"
        finished = day in progress["completed_days"]
        table.add_row(str(day), entry["title"], f"{done}/{len(tasks)}", quiz_cell,
                      "[green]✓[/green]" if finished else "")
    console.print(table)


def stats_panel(progress: dict) -> None:
    table = Table(box=box.ROUNDED, show_header=False)
    table.add_column(style="cyan")
    table.add_column(style="green")
    table.add_row("Started", progress.get("started_at", "N/A")[:10])
    table.add_row("Days completed", f"{len(progress['completed_days'])}/{TOTAL_DAYS}")
    table.add_row("Tasks passed", str(sum(1 for t in progress["tasks"].values() if t.get("passed"))))
    scores = progress["quiz_scores"].values()
    if scores:
        table.add_row("Quiz average", f"{sum(s['best'] for s in scores) / sum(s['total'] for s in scores):.0%}")
    table.add_row("Current streak", f"{storage.current_streak(progress)} day(s)")
    table.add_row("Time studied", storage.format_duration(progress.get("total_time_seconds", 0)))
    console.print(Panel("[bold cyan]📊 Your Progress[/bold cyan]", border_style="blue"))
    console.print(table)
