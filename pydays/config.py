"""Filesystem locations used by the app.

Set ``PYDAYS_HOME`` to keep progress and your code somewhere other than the
project folder (handy if the project lives in a read-only location).
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = Path(os.environ.get("PYDAYS_HOME", BASE_DIR)).expanduser()

PROGRESS_FILE = DATA_DIR / "progress.json"
USER_CODE_DIR = DATA_DIR / "user_code"
LESSONS_DIR = BASE_DIR / "lessons"
