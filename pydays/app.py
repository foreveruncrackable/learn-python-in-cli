"""Menus and learning flow."""

from __future__ import annotations

import argparse
import random
import shutil
import sys
import time
from typing import Optional

from rich.prompt import Confirm, IntPrompt, Prompt

from . import __version__, config, editor, runner, storage, ui
from .curriculum import CURRICULUM, TOTAL_DAYS
from .lessons import load_lesson, split_sections
from .quizzes import QUIZZES
from .tasks import get_day_tasks

console = ui.console

SOLUTION_AFTER_ATTEMPTS = 2


# ------------------------------------------------------------------ lessons

def show_lesson(day: int) -> str:
    """Page through a lesson. Returns 'tasks' to continue or 'menu' to leave."""
    sections = split_sections(load_lesson(day))
    i = 0
    while i < len(sections):
        ui.clear()
        ui.show_day_banner(day)
        ui.show_markdown(sections[i])
        console.print()
        last = i == len(sections) - 1
        ui.info(f"Section {i + 1}/{len(sections)}   "
                f"\\[Enter] {'finish lesson' if last else 'next'} · \\[b] back · \\[t] jump to tasks · \\[q] menu")
        choice = Prompt.ask("", default="", show_default=False).strip().lower()
        if choice == "q":
            return "menu"
        if choice == "t":
            return "tasks"
        if choice == "b":
            i = max(0, i - 1)
        else:
            i += 1
    return "tasks"


# ------------------------------------------------------------------ quizzes

def run_quiz(day: int, progress: dict) -> None:
    questions = QUIZZES.get(day)
    if not questions:
        return
    console.print("\n[bold magenta]🧠 Quick quiz[/bold magenta]\n")
    correct = 0
    letters = "abcd"
    for n, (question, options, answer, explanation) in enumerate(questions, 1):
        order = list(range(len(options)))
        random.shuffle(order)
        console.print(f"[bold]{n}. {question}[/bold]")
        for letter, idx in zip(letters, order):
            console.print(f"   [cyan]{letter})[/cyan] {options[idx]}")
        pick = Prompt.ask("Your answer", choices=list(letters[: len(options)]), show_choices=False)
        chosen = order[letters.index(pick)]
        if chosen == answer:
            correct += 1
            ui.success("✓ Correct!")
        else:
            ui.error(f"✗ Not quite — the answer is “{options[answer]}”.")
        ui.info(explanation + "\n")
    storage.record_quiz(progress, day, correct, len(questions))
    storage.save_progress(progress)
    ui.success(f"Quiz score: {correct}/{len(questions)}\n")


# ------------------------------------------------------------------ tasks

def _write_starter(path, task) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(task.starter, encoding="utf-8")


def _open_for_editing(path) -> bool:
    """Let the learner edit ``path``; falls back to paste mode. False = no change made."""
    if editor.uses_vim():
        ui.console.print(editor.VIM_CHEATSHEET)
        input("Press Enter to open vim...")
    if editor.edit_file(path):
        return True
    ui.warn("vim isn't installed (try: sudo apt install vim). Using paste mode instead.")
    ui.info(f"Type or paste your full solution, then put a line containing just {editor.PASTE_TERMINATOR} to finish.")
    code = editor.paste_code(lambda: input())
    if not code.strip():
        return False
    path.write_text(code, encoding="utf-8")
    return True


def attempt_task(day: int, task, progress: dict) -> Optional[bool]:
    """Returns True if passed, False if not, None if the task is unavailable."""
    missing = runner.missing_requirements(task.requires)
    path = config.USER_CODE_DIR / f"day{day}_{task.id}.py"
    ui.show_task(task, storage.task_attempts(progress, day, task.id),
                 storage.task_passed(progress, day, task.id), missing)
    if missing:
        return None

    if not path.exists():
        _write_starter(path, task)
    ui.show_code(path.read_text(encoding="utf-8"), title="Your current code")

    while True:
        attempts = storage.task_attempts(progress, day, task.id)
        ui.info("\\[e] edit & run · \\[h] hint · \\[s] solution · \\[r] reset to starter · \\[k] skip")
        choice = Prompt.ask("What next?", choices=["e", "h", "s", "r", "k"], default="e", show_choices=False)

        if choice == "k":
            ui.info("Task skipped.")
            return storage.task_passed(progress, day, task.id)
        if choice == "h":
            ui.console.print("[bold yellow]💡 Hint:[/bold yellow] " + task.hint)
        elif choice == "r":
            _write_starter(path, task)
            ui.info("Reset to the starter code.")
        elif choice == "s":
            if attempts < SOLUTION_AFTER_ATTEMPTS and not storage.task_passed(progress, day, task.id):
                left = SOLUTION_AFTER_ATTEMPTS - attempts
                ui.warn(f"Give it {left} more honest attempt(s) first — struggling is how it sticks! "
                        "Try the hint option (h).")
            else:
                ui.show_code(task.solution, title="Reference solution")
        else:  # edit & run
            before = path.read_text(encoding="utf-8")
            if not _open_for_editing(path):
                ui.info("No changes made.")
                continue
            code = path.read_text(encoding="utf-8")
            unchanged = code == before and (code == task.starter or attempts > 0)
            if not code.strip() or unchanged:
                ui.info("Your code is unchanged, so there's nothing new to run.")
                continue
            ui.show_code(code, title="Your code")
            result = runner.check_task(task, code)
            ui.show_result(result)
            storage.record_attempt(progress, day, task.id, result.passed)
            storage.touch_activity(progress)
            storage.save_progress(progress)
            if result.passed:
                return True


# ------------------------------------------------------------------ a day

def study_day(day: int, progress: dict) -> str:
    """Run one full day. Returns 'next', 'menu'."""
    started = time.monotonic()
    storage_day_done = False
    try:
        if show_lesson(day) == "menu":
            return "menu"

        ui.clear()
        ui.show_day_banner(day)
        if QUIZZES.get(day) and Confirm.ask("Take the quick quiz?", default=True):
            run_quiz(day, progress)

        tasks = get_day_tasks(day)
        available = [t for t in tasks if not runner.missing_requirements(t.requires)]
        for task in tasks:
            attempt_task(day, task, progress)

        passed = sum(1 for t in available if storage.task_passed(progress, day, t.id))
        console.print()
        if available and passed == len(available):
            storage.complete_day(progress, day)
            storage_day_done = True
            ui.success(f"🎉 Day {day} completed!  ({passed}/{len(tasks)} tasks passed)")
        elif not available:
            ui.warn("None of today's tasks can run until you install the packages mentioned above.")
        elif day in progress["completed_days"]:
            ui.warn(f"Day {day} stays marked complete from before, but only {passed}/{len(available)} "
                    "task(s) pass the checks. Come back any time to finish them; your code is saved.")
        else:
            ui.warn(f"Day {day} isn't finished yet — {passed}/{len(available)} tasks passed. "
                    "Come back any time; your code is saved.")
        skipped = len(tasks) - len(available)
        if skipped:
            ui.info(f"({skipped} task(s) need extra packages and don't count toward completion.)")
    finally:
        storage.add_time(progress, time.monotonic() - started)
        storage.touch_activity(progress)
        storage.save_progress(progress)

    if storage_day_done and day < TOTAL_DAYS:
        return "next" if Confirm.ask("Continue to the next day?", default=True) else "menu"
    if storage_day_done and day == TOTAL_DAYS:
        ui.success("🏆 Congratulations! You've completed all 30 days!")
        Prompt.ask("Press Enter to return to the menu", default="", show_default=False)
        return "menu"
    Prompt.ask("Press Enter to return to the menu", default="", show_default=False)
    return "menu"


def run_from_day(day: int, progress: dict) -> None:
    while True:
        outcome = study_day(day, progress)
        if outcome != "next":
            return
        day += 1


# ------------------------------------------------------------------ playground

def playground() -> None:
    path = config.USER_CODE_DIR / "playground.py"
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text('# Playground: write any Python you like!\nprint("Hello from the playground")\n',
                        encoding="utf-8")
    while True:
        if not _open_for_editing(path):
            return
        console.print("\n[bold green]▶ Running…[/bold green]\n")
        runner.run_interactive(path)
        console.print()
        if not Confirm.ask("Edit and run again?", default=True):
            return


# ------------------------------------------------------------------ menu

def pick_day(progress: dict) -> Optional[int]:
    ui.clear()
    ui.days_table(progress)
    suggested = storage.suggest_day(progress) or progress["current_day"]
    value = Prompt.ask(f"Day number (1-{TOTAL_DAYS}, or q to go back)", default=str(suggested))
    if value.strip().lower() == "q":
        return None
    try:
        day = int(value)
    except ValueError:
        ui.error("Please enter a number.")
        return pick_day(progress) if Confirm.ask("Try again?", default=True) else None
    if 1 <= day <= TOTAL_DAYS:
        return day
    ui.error(f"Day must be between 1 and {TOTAL_DAYS}.")
    return None


def view_progress(progress: dict) -> None:
    ui.clear()
    ui.stats_panel(progress)
    console.print()
    ui.days_table(progress)
    Prompt.ask("\nPress Enter to return to the menu", default="", show_default=False)


def reset_everything() -> None:
    if not Confirm.ask("Reset ALL progress?", default=False):
        return
    storage.reset_progress()
    if config.USER_CODE_DIR.exists() and Confirm.ask("Also delete your saved code in user_code/?", default=False):
        shutil.rmtree(config.USER_CODE_DIR, ignore_errors=True)
    ui.success("Progress reset!")


def main_menu() -> None:
    while True:
        progress = storage.load_progress()
        ui.clear()
        ui.show_banner()
        ui.progress_bar(progress)

        nxt = storage.suggest_day(progress)
        label = f"Continue learning (Day {nxt}: {CURRICULUM[nxt - 1]['title']})" if nxt else "Review a day (all 30 done! 🏆)"
        console.print("[bold cyan]📚 Main Menu[/bold cyan]\n")
        for key, text in [("1", label), ("2", "Select a day"), ("3", "Playground (free coding)"),
                          ("4", "View progress"), ("5", "Reset progress"), ("6", "Exit")]:
            console.print(f"  [bold green]{key}.[/bold green] {text}")
        console.print()

        choice = Prompt.ask("Choose an option", choices=[str(i) for i in range(1, 7)], default="1", show_choices=False)
        if choice == "1":
            day = nxt if nxt else pick_day(progress)
            if day:
                run_from_day(day, progress)
        elif choice == "2":
            day = pick_day(progress)
            if day:
                run_from_day(day, progress)
        elif choice == "3":
            playground()
        elif choice == "4":
            view_progress(progress)
        elif choice == "5":
            reset_everything()
        else:
            console.print("\n[bold yellow]Happy Coding! 🐍[/bold yellow]\n")
            return


# ------------------------------------------------------------------ entry point

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="30-days-of-python", description="Learn Python in 30 days, in your terminal.")
    parser.add_argument("--day", type=int, metavar="N", help=f"jump straight to day N (1-{TOTAL_DAYS})")
    parser.add_argument("--list", action="store_true", help="show all days and your progress, then exit")
    parser.add_argument("--reset", action="store_true", help="reset progress (asks first), then exit")
    parser.add_argument("--no-animation", action="store_true", help="turn off the typing/banner animation")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    ui.set_animation(not args.no_animation)

    try:
        if args.list:
            ui.days_table(storage.load_progress())
            return 0
        if args.reset:
            reset_everything()
            return 0
        if args.day is not None:
            if not 1 <= args.day <= TOTAL_DAYS:
                console.print(f"[red]--day must be between 1 and {TOTAL_DAYS}[/red]")
                return 2
            run_from_day(args.day, storage.load_progress())
            return 0
        main_menu()
    except (KeyboardInterrupt, EOFError):
        console.print("\n\n[bold yellow]Progress saved. Happy Coding! 🐍[/bold yellow]\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
