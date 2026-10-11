from pydays.runner import Case, check_task, matches
from pydays.tasks import Task


def make(cases, must_use=(), files=None):
    return Task("t", "T", "", "", "", "", cases, must_use=must_use, files=files or {})


def test_input_prompts_do_not_pollute_output():
    t = make([Case(stdin="hi\n", expected="hi")])
    assert check_task(t, 'print(input("Prompt: "))').passed


def test_wrong_output_reports_actual():
    r = check_task(make([Case(expected="1")]), "print(2)")
    assert not r.passed and r.cases[0].actual.strip() == "2"


def test_runtime_error_is_cleaned():
    r = check_task(make([Case(expected="x")]), "x = 1\nprint(1/0)\n")
    err = r.cases[0].error
    assert "ZeroDivisionError" in err and "runpy" not in err and "your_code.py" in err


def test_syntax_error_reported_without_running():
    r = check_task(make([Case(expected="x")]), "print(\n")
    assert r.syntax_error and "line" in r.syntax_error and not r.cases


def test_timeout():
    import pydays.runner as runner
    c = runner.run_case("while True: pass", Case(expected="x"), timeout=1)
    assert c.timed_out and not c.passed


def test_missing_construct_blocks_pass():
    t = make([Case(expected="3")], must_use=("loop",))
    r = check_task(t, "print(3)")
    assert not r.passed and r.missing_constructs == ["loop"]


def test_harness_filters_to_show_lines():
    t = make([Case(harness="show(f(2))", expected="4")])
    assert check_task(t, 'def f(x):\n    print("noise")\n    return x * x\n').passed


def test_harness_name_error_is_short():
    r = check_task(make([Case(harness="show(f(2))", expected="4")]), "pass")
    assert r.cases[0].error.startswith("NameError")


def test_extra_files_available():
    t = make([Case(expected="HI")], files={"mod.py": "X = 'HI'"})
    assert check_task(t, "import mod\nprint(mod.X)").passed


def test_code_runs_in_temp_dir_not_cwd(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    check_task(make([Case(expected="")], ), 'open("leak.txt", "w").write("x")')
    assert not (tmp_path / "leak.txt").exists()


def test_match_modes():
    assert matches("numeric", "4.5", "result: 4.50")
    assert not matches("numeric", "4.5", "nothing")
    assert matches("contains", "zero", "Cannot divide by ZERO")
    assert matches("exact", "a\nb", "a  \nb\n\n")
    assert matches("nonempty", "", "x") and not matches("nonempty", "", "  ")
