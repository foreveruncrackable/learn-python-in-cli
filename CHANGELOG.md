# Changelog

## 2.0.0
- The code editor is **vim** (Python-friendly settings and an on-screen reminder of the basic keys);
  `vi`, then paste mode, as fallbacks. Override with `PYDAYS_EDITOR`.
- **All 30 lessons rewritten to explain, not just show code:** a one-line "Big idea", a plain-English
  explanation before each example, the result of each snippet in a comment, a short "Key terms" list and a
  "Watch out" section (common mistakes + one thing to remember). Topic order follows the open-source
  *30 Days of Python* course; the wording is original.
- Added missing topics: Day 11 scope & docstrings, Day 14 closures, Day 15 tracebacks/logging/pdb,
  Day 16 parsing & timezones, Day 19 paths & CSV, and more.
- Fixed a crashing example in the Day 13 lesson (flattening a matrix looped over the wrong variable).
- Split the 1,600-line `main.py` into a `pydays/` package; lessons are now markdown files.
- Real automated checks: multiple test cases per task, required-construct checks, readable failures.
- Fixed: tasks using `input()` ran with no stdin and could never pass.
- Fixed: a day was marked complete even if every task failed; now it needs all tasks to pass.
- Fixed: hardcoded `/home/omlanda/abu/god/bin/python3`; code now runs with the current interpreter.
- Fixed: hard dependency on tmux + vim; now uses `$EDITOR`, common editors, or paste mode.
- Fixed: auto `pip install rich` failing on PEP 668 systems; dependencies are installed explicitly.
- Fixed: Day 18 lesson invalid-escape warning; Day 17 `finally` example that could crash.
- Added: quizzes, hints/solutions flow, playground, streaks, time tracking, per-day status table,
  `--day / --list / --reset / --no-animation`, atomic progress saves, v1 progress migration.
- Tasks for Days 12, 16, 20, 22-29 are now offline and testable (no network, MongoDB or running server).
- Added a pytest suite (reference solutions pass, starters fail, storage, runner).
- Slimmed `requirements.txt` to `rich`; heavy packages moved to `requirements-extras.txt`.
