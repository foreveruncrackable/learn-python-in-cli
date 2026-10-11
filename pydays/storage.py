"""Load / save learner progress.

The progress file is plain JSON.  Loading is forgiving: old files (v1) are
migrated, missing keys get defaults, and a corrupt file is moved aside to
``progress.json.bak`` instead of crashing the app.
"""

from __future__ import annotations

import json
import os
import re
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Optional

from . import config
from .curriculum import TOTAL_DAYS

SCHEMA_VERSION = 2


def default_progress() -> dict:
    now = datetime.now().isoformat(timespec="seconds")
    return {
        "version": SCHEMA_VERSION,
        "started_at": now,
        "last_active": now,
        "current_day": 1,
        "completed_days": [],
        # "<day>:<task_id>" -> {"passed": bool, "attempts": int}
        "tasks": {},
        # "<day>" -> {"best": int, "total": int, "attempts": int}
        "quiz_scores": {},
        "total_time_seconds": 0,
        "activity_dates": [],
    }


def _path(path: Optional[Path]) -> Path:
    return Path(path) if path else config.PROGRESS_FILE


def task_key(day: int, task_id: str) -> str:
    return f"{day}:{task_id}"


def _migrate(data: dict) -> dict:
    """Bring any older / partial progress dict up to the current schema."""
    progress = default_progress()
    if not isinstance(data, dict):
        return progress

    for key in ("started_at", "last_active"):
        if isinstance(data.get(key), str):
            progress[key] = data[key]

    days = data.get("completed_days", [])
    progress["completed_days"] = sorted(
        {d for d in days if isinstance(d, int) and 1 <= d <= TOTAL_DAYS}
    )

    current = data.get("current_day", 1)
    progress["current_day"] = current if isinstance(current, int) and 1 <= current <= TOTAL_DAYS else 1

    if isinstance(data.get("tasks"), dict):
        progress["tasks"] = data["tasks"]

    # v1 stored finished tasks as ["day10_multiplication_table", ...]
    for legacy in data.get("code_tasks_completed", []) or []:
        match = re.fullmatch(r"day(\d+)_(.+)", str(legacy))
        if match:
            progress["tasks"].setdefault(
                task_key(int(match.group(1)), match.group(2)), {"passed": True, "attempts": 1}
            )

    if isinstance(data.get("quiz_scores"), dict):
        for day, value in data["quiz_scores"].items():
            if isinstance(value, dict):
                progress["quiz_scores"][str(day)] = value

    seconds = data.get("total_time_seconds")
    if seconds is None and isinstance(data.get("total_time_minutes"), (int, float)):
        seconds = data["total_time_minutes"] * 60
    progress["total_time_seconds"] = int(seconds) if isinstance(seconds, (int, float)) else 0

    dates = data.get("activity_dates", [])
    progress["activity_dates"] = [d for d in dates if isinstance(d, str)][-365:]
    return progress


def load_progress(path: Optional[Path] = None) -> dict:
    target = _path(path)
    if not target.exists():
        return default_progress()
    try:
        with open(target, "r", encoding="utf-8") as fh:
            return _migrate(json.load(fh))
    except (json.JSONDecodeError, UnicodeDecodeError, OSError):
        try:
            os.replace(target, target.with_suffix(target.suffix + ".bak"))
        except OSError:
            pass
        return default_progress()


def save_progress(progress: dict, path: Optional[Path] = None) -> None:
    """Write atomically so a crash mid-save can't wipe the file."""
    target = _path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    progress["last_active"] = datetime.now().isoformat(timespec="seconds")
    tmp = target.with_suffix(target.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(progress, fh, indent=2)
    os.replace(tmp, target)


def reset_progress(path: Optional[Path] = None) -> None:
    target = _path(path)
    if target.exists():
        target.unlink()


# ---------------------------------------------------------------- tasks / days

def record_attempt(progress: dict, day: int, task_id: str, passed: bool) -> None:
    entry = progress["tasks"].setdefault(task_key(day, task_id), {"passed": False, "attempts": 0})
    entry["attempts"] = entry.get("attempts", 0) + 1
    entry["passed"] = bool(entry.get("passed")) or passed


def task_passed(progress: dict, day: int, task_id: str) -> bool:
    return bool(progress["tasks"].get(task_key(day, task_id), {}).get("passed"))


def task_attempts(progress: dict, day: int, task_id: str) -> int:
    return int(progress["tasks"].get(task_key(day, task_id), {}).get("attempts", 0))


def complete_day(progress: dict, day: int) -> None:
    if day not in progress["completed_days"]:
        progress["completed_days"].append(day)
        progress["completed_days"].sort()
    progress["current_day"] = min(day + 1, TOTAL_DAYS)


def suggest_day(progress: dict) -> Optional[int]:
    """Next unfinished day at/after the current one (wrapping); None if all done."""
    done = set(progress["completed_days"])
    start = progress.get("current_day", 1)
    order = list(range(start, TOTAL_DAYS + 1)) + list(range(1, start))
    return next((d for d in order if d not in done), None)


def record_quiz(progress: dict, day: int, correct: int, total: int) -> None:
    entry = progress["quiz_scores"].setdefault(str(day), {"best": 0, "total": total, "attempts": 0})
    entry["best"] = max(entry.get("best", 0), correct)
    entry["total"] = total
    entry["attempts"] = entry.get("attempts", 0) + 1


# ---------------------------------------------------------------- time / streak

def add_time(progress: dict, seconds: float) -> None:
    progress["total_time_seconds"] = int(progress.get("total_time_seconds", 0) + max(0, seconds))


def touch_activity(progress: dict, today: Optional[date] = None) -> None:
    today = today or date.today()
    iso = today.isoformat()
    if iso not in progress["activity_dates"]:
        progress["activity_dates"].append(iso)
        progress["activity_dates"] = progress["activity_dates"][-365:]


def current_streak(progress: dict, today: Optional[date] = None) -> int:
    """Consecutive active days ending today (or yesterday, so the streak isn't
    lost before you've had a chance to study today)."""
    today = today or date.today()
    days = set()
    for iso in progress.get("activity_dates", []):
        try:
            days.add(date.fromisoformat(iso))
        except ValueError:
            continue
    cursor = today if today in days else today - timedelta(days=1)
    streak = 0
    while cursor in days:
        streak += 1
        cursor -= timedelta(days=1)
    return streak


def format_duration(seconds: int) -> str:
    minutes, _ = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    if hours:
        return f"{hours}h {minutes}m"
    return f"{minutes}m" if minutes else "<1m"
