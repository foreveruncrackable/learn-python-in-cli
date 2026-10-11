"""Run a learner's code against a task's test cases.

Each case executes in a fresh subprocess using the *same* interpreter that is
running the app (no hardcoded paths), inside a throw-away temp directory, with
a timeout.  ``input()`` prompts are silenced so they don't pollute the output
that gets compared with the expected result.
"""

from __future__ import annotations

import ast
import importlib.util
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional

SCRIPT_NAME = "your_code.py"
DEFAULT_TIMEOUT = 10

# Launcher: silences input() prompts, optionally neuters Flask's app.run(),
# then runs the learner's file as ``__main__``.
_STUB = r'''
import builtins, os, runpy, sys
_real_input = builtins.input
builtins.input = lambda prompt="": _real_input()
if os.environ.get("PYDAYS_PATCH_FLASK"):
    try:
        import flask
        flask.Flask.run = lambda *a, **k: None
    except Exception:
        pass
path = sys.argv[1]
sys.argv = [path]
sys.path.insert(0, os.path.dirname(path))
runpy.run_path(path, run_name="__main__")
'''

_HARNESS_PRELUDE = '\n\n# ---- test harness ----\ndef show(*args):\n    print("@@" + " ".join(str(a) for a in args))\n'


@dataclass
class Case:
    """One test: feed ``stdin`` (and/or append ``harness`` code) and compare output.

    mode: exact | contains | numeric | nonempty
    harness: code appended after the learner's code; use ``show(...)`` to emit
             values.  Only ``show`` output is compared in that case.
    """

    expected: str = ""
    stdin: str = ""
    mode: str = "exact"
    harness: str = ""
    label: str = ""

    def describe(self) -> str:
        if self.label:
            return self.label
        if self.stdin:
            return "input: " + " ⏎ ".join(self.stdin.strip().splitlines())[:60]
        if self.harness:
            return self.harness.strip().splitlines()[0][:60]
        return "run the program"


@dataclass
class CaseResult:
    case: Case
    passed: bool
    actual: str = ""
    error: str = ""
    timed_out: bool = False


@dataclass
class RunResult:
    passed: bool = False
    syntax_error: Optional[str] = None
    missing_constructs: List[str] = field(default_factory=list)
    cases: List[CaseResult] = field(default_factory=list)

    @property
    def passed_count(self) -> int:
        return sum(1 for c in self.cases if c.passed)


# ------------------------------------------------------------------ comparing

def _normalise(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.strip().splitlines())


def matches(mode: str, expected: str, actual: str) -> bool:
    if mode == "exact":
        return _normalise(actual) == _normalise(expected)
    if mode == "contains":
        return expected.lower() in actual.lower()
    if mode == "numeric":
        numbers = re.findall(r"-?\d+(?:\.\d+)?", actual)
        return bool(numbers) and abs(float(numbers[-1]) - float(expected)) < 1e-6
    if mode == "nonempty":
        return bool(actual.strip())
    raise ValueError(f"unknown match mode: {mode}")


# ------------------------------------------------------------------ AST checks

_CONSTRUCT_LABELS = {
    "loop": "a loop (for/while)",
    "unpack": "tuple unpacking (a, b = ...)",
}


def _has_construct(tree: ast.AST, spec: str) -> bool:
    nodes = list(ast.walk(tree))
    if spec == "loop":
        return any(isinstance(n, (ast.For, ast.While)) for n in nodes)
    if spec == "unpack":
        return any(
            isinstance(n, ast.Assign) and any(isinstance(t, (ast.Tuple, ast.List)) for t in n.targets)
            for n in nodes
        )
    if spec.startswith("call:"):
        name = spec[5:]
        return any(
            isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == name for n in nodes
        )
    if spec.startswith("import:"):
        module = spec[7:]
        for n in nodes:
            if isinstance(n, ast.Import) and any(a.name.split(".")[0] == module for a in n.names):
                return True
            if isinstance(n, ast.ImportFrom) and n.module and n.module.split(".")[0] == module:
                return True
        return False
    node_type = getattr(ast, spec, None)
    return bool(node_type) and any(isinstance(n, node_type) for n in nodes)


def describe_construct(spec: str) -> str:
    if spec in _CONSTRUCT_LABELS:
        return _CONSTRUCT_LABELS[spec]
    if spec.startswith("call:"):
        return f"a call to {spec[5:]}()"
    if spec.startswith("import:"):
        return f"`import {spec[7:]}`"
    pretty = {
        "ListComp": "a list comprehension",
        "For": "a for loop",
        "If": "an if statement",
        "Try": "try/except",
        "ClassDef": "a class",
        "FunctionDef": "a function (def)",
        "Lambda": "a lambda",
        "With": "a `with` block",
    }
    return pretty.get(spec, spec)


def missing_requirements(requires) -> List[str]:
    """Names from ``requires`` that can't be imported by this interpreter."""
    return [m for m in requires if importlib.util.find_spec(m) is None]


# ------------------------------------------------------------------ execution

def _clean_traceback(stderr: str, harness_failure: bool) -> str:
    lines = stderr.strip().splitlines()
    if not lines:
        return ""
    if harness_failure:
        return lines[-1]  # e.g. "NameError: name 'fibonacci' is not defined"
    start = next(
        (i for i, line in enumerate(lines) if SCRIPT_NAME in line and line.lstrip().startswith("File")),
        None,
    )
    if start is None:
        return lines[-1]
    cleaned = ["Traceback (most recent call last):"] + lines[start:]
    text = "\n".join(cleaned)
    return re.sub(r'File "[^"]*' + re.escape(SCRIPT_NAME) + '"', f'File "{SCRIPT_NAME}"', text)


def run_case(code: str, case: Case, files=None, requires=(), timeout: int = DEFAULT_TIMEOUT) -> CaseResult:
    source = code + (_HARNESS_PRELUDE + case.harness + "\n" if case.harness else "")
    with tempfile.TemporaryDirectory(prefix="pydays_") as tmp:
        tmp_path = Path(tmp)
        script = tmp_path / SCRIPT_NAME
        script.write_text(source, encoding="utf-8")
        for name, content in (files or {}).items():
            (tmp_path / name).write_text(content, encoding="utf-8")

        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONIOENCODING="utf-8")
        if "flask" in requires:
            env["PYDAYS_PATCH_FLASK"] = "1"
        try:
            proc = subprocess.run(
                [sys.executable, "-X", "utf8", "-c", _STUB, str(script)],
                input=case.stdin,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=timeout,
                cwd=tmp,
                env=env,
            )
        except subprocess.TimeoutExpired:
            return CaseResult(case, False, timed_out=True)

    stdout = proc.stdout
    if case.harness:
        stdout = "\n".join(l[2:] for l in stdout.splitlines() if l.startswith("@@"))

    if proc.returncode != 0:
        error = _clean_traceback(proc.stderr, harness_failure=bool(case.harness))
        return CaseResult(case, False, actual=stdout, error=error)

    return CaseResult(case, matches(case.mode, case.expected, stdout), actual=stdout)


def check_task(task, code: str) -> RunResult:
    """Run every case of ``task`` against ``code``."""
    result = RunResult()
    try:
        tree = ast.parse(code)
    except SyntaxError as exc:
        text = (exc.text or "").rstrip()
        result.syntax_error = f"line {exc.lineno}: {exc.msg}" + (f"\n    {text}" if text else "")
        return result

    result.missing_constructs = [s for s in task.must_use if not _has_construct(tree, s)]
    for case in task.cases:
        result.cases.append(run_case(code, case, task.files, task.requires))
    result.passed = not result.missing_constructs and all(c.passed for c in result.cases)
    return result


def run_interactive(path: Path) -> int:
    """Run a file attached to the real terminal (used by the playground)."""
    try:
        return subprocess.call([sys.executable, str(path)], cwd=str(path.parent))
    except KeyboardInterrupt:
        return 130
