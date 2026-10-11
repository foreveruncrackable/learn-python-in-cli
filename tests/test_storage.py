import json
from datetime import date, timedelta

from pydays import storage


def test_missing_file_gives_defaults(tmp_path):
    p = storage.load_progress(tmp_path / "nope.json")
    assert p["completed_days"] == [] and p["version"] == storage.SCHEMA_VERSION


def test_roundtrip(tmp_path):
    f = tmp_path / "p.json"
    p = storage.default_progress()
    storage.record_attempt(p, 3, "calculator", True)
    storage.complete_day(p, 3)
    storage.save_progress(p, f)
    q = storage.load_progress(f)
    assert q["completed_days"] == [3] and q["current_day"] == 4
    assert storage.task_passed(q, 3, "calculator")


def test_migrates_v1_file(tmp_path):
    f = tmp_path / "p.json"
    f.write_text(json.dumps({
        "started_at": "2026-10-02T06:45:19", "last_day": 1, "completed_days": [10],
        "current_day": 11, "current_section": 0, "quiz_scores": {},
        "code_tasks_completed": ["day10_multiplication_table"], "total_time_minutes": 5,
    }))
    p = storage.load_progress(f)
    assert p["completed_days"] == [10] and p["current_day"] == 11
    assert storage.task_passed(p, 10, "multiplication_table")
    assert p["total_time_seconds"] == 300


def test_corrupt_file_is_backed_up(tmp_path):
    f = tmp_path / "p.json"
    f.write_text("{not json")
    p = storage.load_progress(f)
    assert p["completed_days"] == []
    assert (tmp_path / "p.json.bak").exists()


def test_bad_values_are_sanitised(tmp_path):
    f = tmp_path / "p.json"
    f.write_text(json.dumps({"completed_days": [1, 1, 99, "x", 2], "current_day": 500}))
    p = storage.load_progress(f)
    assert p["completed_days"] == [1, 2] and p["current_day"] == 1


def test_attempts_count_and_passed_sticks():
    p = storage.default_progress()
    storage.record_attempt(p, 1, "t", False)
    storage.record_attempt(p, 1, "t", True)
    storage.record_attempt(p, 1, "t", False)
    assert storage.task_attempts(p, 1, "t") == 3 and storage.task_passed(p, 1, "t")


def test_suggest_day_wraps_and_finishes():
    p = storage.default_progress()
    p["current_day"], p["completed_days"] = 29, [29, 30]
    assert storage.suggest_day(p) == 1
    p["completed_days"] = list(range(1, 31))
    assert storage.suggest_day(p) is None


def test_streak():
    today = date(2026, 10, 2)
    p = storage.default_progress()
    for back in (0, 1, 2, 4):
        storage.touch_activity(p, today - timedelta(days=back))
    assert storage.current_streak(p, today) == 3
    p["activity_dates"] = [(today - timedelta(days=1)).isoformat()]
    assert storage.current_streak(p, today) == 1   # yesterday still counts
    p["activity_dates"] = [(today - timedelta(days=3)).isoformat()]
    assert storage.current_streak(p, today) == 0


def test_quiz_keeps_best_score():
    p = storage.default_progress()
    storage.record_quiz(p, 2, 1, 2)
    storage.record_quiz(p, 2, 2, 2)
    storage.record_quiz(p, 2, 0, 2)
    assert p["quiz_scores"]["2"] == {"best": 2, "total": 2, "attempts": 3}
