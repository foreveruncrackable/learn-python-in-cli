# 30 Days of Python — Interactive CLI

Learn Python in your terminal: read a short lesson, take a quick quiz, then write real code that is
**automatically tested**. Progress, streaks and time studied are saved between sessions.

## Quick start

```bash
cd 30-days-of-python-cli
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt                      # just `rich`
python main.py
```

Optional: `pip install -r requirements-extras.txt` for the tasks on Days 22, 25, 26, 28 and 29
(BeautifulSoup, pandas, Flask, requests). Without them those tasks are marked *unavailable* and
don't block you from finishing the day. Nothing needs the internet or a database.

## Using it

```bash
python main.py              # menu
python main.py --day 5      # jump straight to Day 5
python main.py --list       # see all days and your progress
python main.py --reset      # start over (asks first)
python main.py --no-animation
```

Every lesson explains each idea in plain words (a "Big idea", examples with their results, "Key terms" and "Watch out" pages),
not just code. Topic order follows the open-source [30 Days of Python](https://github.com/Asabeneh/30-Days-Of-Python) course.

Each day is: **lesson** (paged — `Enter` next, `b` back, `t` jump to tasks, `q` menu) →
**quiz** (2 questions) → **coding task(s)**.

For a task you can edit & run (`e`), ask for a hint (`h`), see the reference solution (`s`, unlocked
after two attempts), reset to the starter code (`r`) or skip (`k`). A day is complete when all of its
tasks pass. Your code lives in `user_code/` so you can reopen it any time.

There's also a **Playground** in the menu for free-form coding.

### The editor is vim

Tasks and the Playground open in **vim**, set up for Python (line numbers, 4-space indents).
New to vim? A reminder is shown each time:

- `i`: start typing · `Esc`: stop typing
- `:wq` + Enter: save and run your code · `:q!` + Enter: quit without saving

If `vim` isn't installed the app tries `vi`, and then falls back to a **paste mode**
(paste code, finish with a line containing `END`). To use another editor, set
`PYDAYS_EDITOR`, e.g. `export PYDAYS_EDITOR="code --wait"`. No tmux required.

### Where is my data?

`progress.json` and `user_code/` sit in the project folder. Set `PYDAYS_HOME=/some/dir` to store
them elsewhere. Old (v1) progress files are migrated automatically.

## How tasks are checked

Your code runs in a throw-away temp folder using the same Python that runs the app, with a timeout.
Each task has several test cases (so printing the one expected answer won't pass), and some require a
specific construct, e.g. a list comprehension on Day 13 or `filter()` on Day 14. Failed tests show
what was expected vs. what your code printed, plus a cleaned-up traceback.

## Project layout

```
main.py              entry point
pydays/
  app.py             menus & learning flow
  ui.py              all rich rendering
  storage.py         progress file (migration, atomic save, streaks)
  runner.py          sandboxed test runner + AST checks
  editor.py          editor launcher / paste mode
  tasks.py           the 30 tasks (starter, hint, solution, tests)
  quizzes.py         quiz questions
  lessons.py         loads lessons/dayNN.md
  curriculum.py      titles & topics
lessons/dayNN.md     lesson content (plain markdown — easy to edit!)
tests/               pytest suite
```

## Contributing / editing content

- **Lessons** are markdown files in `lessons/`. Use `##` headings; each becomes a page.
- **Tasks** are entries in `pydays/tasks.py`. Give every task a reference `solution` and run
  `pytest` — it checks that each solution passes and each starter fails.

```bash
pip install -r requirements-dev.txt
pytest
```
