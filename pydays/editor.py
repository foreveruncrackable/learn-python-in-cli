"""Open a file for editing in vim.

vim is the built-in editor. It's started with Python-friendly settings
(line numbers, 4-space indents, tabs turned into spaces).

Fallbacks:
  * ``vi`` if ``vim`` isn't installed
  * a built-in "paste mode" if neither exists

To use a different editor, set ``PYDAYS_EDITOR`` (GUI editors need a wait
flag, e.g. ``PYDAYS_EDITOR="code --wait"``).
"""

from __future__ import annotations

import os
import shlex
import shutil
import subprocess
from pathlib import Path
from typing import List, Optional

PASTE_TERMINATOR = "END"

VIM_SETTINGS = "set number autoindent expandtab tabstop=4 shiftwidth=4 softtabstop=4"

VIM_CHEATSHEET = (
    "vim quick guide:  [bold]i[/bold] = start typing · [bold]Esc[/bold] = stop typing · "
    "[bold]:wq[/bold] + Enter = save & run · [bold]:q![/bold] + Enter = quit without saving"
)


def find_editor() -> Optional[List[str]]:
    custom = os.environ.get("PYDAYS_EDITOR", "").strip()
    if custom:
        return shlex.split(custom, posix=(os.name != "nt"))
    if shutil.which("vim"):
        return ["vim", "-c", VIM_SETTINGS]
    if shutil.which("vi"):
        return ["vi"]
    return None


def uses_vim() -> bool:
    command = find_editor()
    return bool(command) and os.path.basename(command[0]) in ("vim", "vi")


def edit_file(path: Path) -> bool:
    """Open ``path`` in the editor.  Returns False if no editor could be launched."""
    command = find_editor()
    if not command:
        return False
    try:
        subprocess.call(command + [str(path)])
        return True
    except (OSError, KeyboardInterrupt):
        return False


def paste_code(read_line=input) -> str:
    """Collect code typed/pasted line by line until a line that is just END."""
    lines = []
    while True:
        try:
            line = read_line()
        except EOFError:
            break
        if line.strip() == PASTE_TERMINATOR:
            break
        lines.append(line)
    return "\n".join(lines) + ("\n" if lines else "")
