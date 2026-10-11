"""Coding tasks for each day.

Every task has real test cases (several inputs, so hard-coding the answer
doesn't work), an optional list of constructs the solution must use, a hint
and a reference solution.  Tasks that need a third-party package declare it in
``requires``; if it isn't installed the task is shown as unavailable and does
not block finishing the day.  Nothing here needs the network or a database.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Tuple

from .runner import Case


@dataclass
class Task:
    id: str
    title: str
    instructions: str
    starter: str
    hint: str
    solution: str
    cases: List[Case]
    must_use: Tuple[str, ...] = ()
    requires: Tuple[str, ...] = ()
    files: Dict[str, str] = field(default_factory=dict)


def _stdin_cases(pairs, mode="exact"):
    return [Case(stdin=s, expected=e, mode=mode) for s, e in pairs]


TASKS: Dict[int, List[Task]] = {}


def _add(day: int, task: Task) -> None:
    TASKS.setdefault(day, []).append(task)


# ----------------------------------------------------------------- Day 1
_add(1, Task(
    id="hello_world",
    title="Hello, World!",
    instructions="Print exactly `Hello, World!`",
    starter="# Print Hello, World! below\n",
    hint="Use the print() function with a string: print(\"...\")",
    solution='print("Hello, World!")\n',
    cases=[Case(expected="Hello, World!")],
    must_use=("call:print",),
))

# ----------------------------------------------------------------- Day 2
_add(2, Task(
    id="variable_swap",
    title="Swap two variables",
    instructions="Swap the values of `a` and `b` so the program prints `a = 10, b = 5`.",
    starter='a = 5\nb = 10\n# Swap a and b here\n\nprint(f"a = {a}, b = {b}")\n',
    hint="Python can swap without a temp variable: a, b = b, a",
    solution='a = 5\nb = 10\na, b = b, a\nprint(f"a = {a}, b = {b}")\n',
    cases=[Case(expected="a = 10, b = 5")],
))

# ----------------------------------------------------------------- Day 3
_add(3, Task(
    id="calculator",
    title="Simple calculator",
    instructions=(
        "Read two numbers and an operator (`+ - * /`) and print the result.\n"
        "If the user divides by zero, print `Cannot divide by zero`."
    ),
    starter=(
        'num1 = float(input("First number: "))\n'
        'operator = input("Operator (+, -, *, /): ")\n'
        'num2 = float(input("Second number: "))\n'
        "# Calculate and print the result\n"
    ),
    hint="Use if/elif/else on `operator`. For division, check `num2 == 0` first.",
    solution=(
        'num1 = float(input("First number: "))\n'
        'operator = input("Operator (+, -, *, /): ")\n'
        'num2 = float(input("Second number: "))\n'
        'if operator == "+":\n    print(num1 + num2)\n'
        'elif operator == "-":\n    print(num1 - num2)\n'
        'elif operator == "*":\n    print(num1 * num2)\n'
        'elif operator == "/":\n'
        '    if num2 == 0:\n        print("Cannot divide by zero")\n'
        "    else:\n        print(num1 / num2)\n"
    ),
    cases=_stdin_cases(
        [("10\n+\n5\n", "15"), ("10\n-\n4\n", "6"), ("6\n*\n7\n", "42"), ("9\n/\n2\n", "4.5")],
        mode="numeric",
    ) + [Case(stdin="5\n/\n0\n", expected="zero", mode="contains")],
    must_use=("If",),
))

# ----------------------------------------------------------------- Day 4
_add(4, Task(
    id="string_reversal",
    title="Reverse a string",
    instructions="Read a string and print it reversed.",
    starter='s = input("Enter a string: ")\n# Reverse the string and print it\n',
    hint="Slicing with a negative step reverses a sequence: s[::-1]",
    solution='s = input("Enter a string: ")\nprint(s[::-1])\n',
    cases=_stdin_cases([("Python\n", "nohtyP"), ("racecar\n", "racecar"), ("a b c\n", "c b a")]),
))

# ----------------------------------------------------------------- Day 5
_add(5, Task(
    id="list_sum",
    title="Sum a list",
    instructions=(
        "Read space-separated integers, then use a `for` loop to add them up and print the total.\n"
        "(No `sum()` shortcut this time — practise the loop!)"
    ),
    starter='numbers = [int(x) for x in input("Numbers: ").split()]\n# Use a for loop to calculate and print the sum\n',
    hint="Start with total = 0, then inside the loop do total += n.",
    solution=(
        'numbers = [int(x) for x in input("Numbers: ").split()]\n'
        "total = 0\nfor n in numbers:\n    total += n\nprint(total)\n"
    ),
    cases=_stdin_cases([("1 2 3 4 5\n", "15"), ("10 20\n", "30"), ("-1 1\n", "0"), ("7\n", "7")]),
    must_use=("For",),
))

# ----------------------------------------------------------------- Day 6
_add(6, Task(
    id="tuple_unpacking",
    title="Unpack a tuple",
    instructions="Unpack `point` into `x` and `y` so the program prints `x = 10, y = 20`.",
    starter='point = (10, 20)\n# Unpack the tuple into x and y\nprint(f"x = {x}, y = {y}")\n',
    hint="Assign a tuple to several names at once: x, y = point",
    solution='point = (10, 20)\nx, y = point\nprint(f"x = {x}, y = {y}")\n',
    cases=[Case(expected="x = 10, y = 20")],
    must_use=("unpack",),
))

# ----------------------------------------------------------------- Day 7
_add(7, Task(
    id="set_operations",
    title="Set operations",
    instructions=(
        "Print three lines for `a` and `b`: the union, the intersection, and `a - b`.\n"
        "Print each as a sorted list, e.g. `[1, 2]`."
    ),
    starter="a = {1, 2, 3, 4}\nb = {3, 4, 5, 6}\n# Print union, intersection and difference (a - b) as sorted lists\n",
    hint="| is union, & is intersection, - is difference. Wrap results in sorted().",
    solution=(
        "a = {1, 2, 3, 4}\nb = {3, 4, 5, 6}\n"
        "print(sorted(a | b))\nprint(sorted(a & b))\nprint(sorted(a - b))\n"
    ),
    cases=[Case(expected="[1, 2, 3, 4, 5, 6]\n[3, 4]\n[1, 2]")],
))

# ----------------------------------------------------------------- Day 8
_add(8, Task(
    id="word_count",
    title="Count words",
    instructions="Read a line of text and print a dictionary of how many times each word appears.",
    starter='text = input("Text: ")\n# Count word occurrences and print the dict\n',
    hint="Loop over text.split(); use counts[word] = counts.get(word, 0) + 1",
    solution=(
        'text = input("Text: ")\ncounts = {}\n'
        "for word in text.split():\n    counts[word] = counts.get(word, 0) + 1\nprint(counts)\n"
    ),
    cases=_stdin_cases([
        ("hello world hello python world\n", "{'hello': 2, 'world': 2, 'python': 1}"),
        ("a b a\n", "{'a': 2, 'b': 1}"),
        ("one\n", "{'one': 1}"),
    ]),
))

# ----------------------------------------------------------------- Day 9
_add(9, Task(
    id="grade_classifier",
    title="Grade classifier",
    instructions="Read a score (0-100) and print its grade: A (90+), B (80+), C (70+), D (60+), otherwise F.",
    starter='score = int(input("Enter score (0-100): "))\n# Print the grade\n',
    hint="Check from the highest range down with if / elif / else.",
    solution=(
        'score = int(input("Enter score (0-100): "))\n'
        'if score >= 90:\n    print("A")\nelif score >= 80:\n    print("B")\n'
        'elif score >= 70:\n    print("C")\nelif score >= 60:\n    print("D")\nelse:\n    print("F")\n'
    ),
    cases=_stdin_cases([
        ("95\n", "A"), ("100\n", "A"), ("85\n", "B"), ("72\n", "C"),
        ("60\n", "D"), ("59\n", "F"), ("0\n", "F"),
    ]),
    must_use=("If",),
))

# ----------------------------------------------------------------- Day 10
_add(10, Task(
    id="multiplication_table",
    title="Multiplication table",
    instructions="Read `n` and print its table from 1 to 10, one line each, like `7 x 3 = 21`.",
    starter='n = int(input("Enter a number: "))\n# Print the multiplication table up to 10\n',
    hint="for i in range(1, 11): then print(f\"{n} x {i} = {n * i}\")",
    solution=(
        'n = int(input("Enter a number: "))\n'
        "for i in range(1, 11):\n    print(f\"{n} x {i} = {n * i}\")\n"
    ),
    cases=[
        Case(stdin="7\n", expected="\n".join(f"7 x {i} = {7 * i}" for i in range(1, 11))),
        Case(stdin="3\n", expected="\n".join(f"3 x {i} = {3 * i}" for i in range(1, 11))),
    ],
    must_use=("loop",),
))

# ----------------------------------------------------------------- Day 11
_add(11, Task(
    id="fibonacci",
    title="Fibonacci function",
    instructions=(
        "Write `fibonacci(n)` that **returns** a list of the first `n` Fibonacci numbers "
        "(starting 0, 1, 1, 2, ...). `fibonacci(0)` returns an empty list."
    ),
    starter='def fibonacci(n):\n    """Return a list with the first n Fibonacci numbers."""\n    pass\n',
    hint="Keep two variables a, b = 0, 1. Append a, then do a, b = b, a + b, n times.",
    solution=(
        "def fibonacci(n):\n    result = []\n    a, b = 0, 1\n"
        "    for _ in range(n):\n        result.append(a)\n        a, b = b, a + b\n    return result\n"
    ),
    cases=[
        Case(harness="show(fibonacci(7))", expected="[0, 1, 1, 2, 3, 5, 8]"),
        Case(harness="show(fibonacci(1))", expected="[0]"),
        Case(harness="show(fibonacci(0))", expected="[]"),
        Case(harness="show(fibonacci(12)[-1])", expected="89"),
    ],
    must_use=("FunctionDef",),
))

# ----------------------------------------------------------------- Day 12
_HELPERS = (
    '"""helpers.py - a tiny module we give you."""\n\n'
    "def shout(text):\n    return text.upper() + \"!\"\n\n"
    "def add(a, b):\n    return a + b\n"
)
_add(12, Task(
    id="use_a_module",
    title="Import a module",
    instructions=(
        "A module called `helpers` sits next to your code. It has `shout(text)` and `add(a, b)`.\n"
        "Read a word and print `helpers.shout(word)`. (Peek at the module below.)\n\n"
        "```python\n" + _HELPERS + "```"
    ),
    starter='# import the helpers module, then use it\nword = input("Word: ")\n',
    hint="`import helpers` then call `helpers.shout(word)`.",
    solution='import helpers\n\nword = input("Word: ")\nprint(helpers.shout(word))\n',
    cases=_stdin_cases([("hello\n", "HELLO!"), ("python\n", "PYTHON!")]),
    must_use=("import:helpers",),
    files={"helpers.py": _HELPERS},
))

# ----------------------------------------------------------------- Day 13
_add(13, Task(
    id="squares_comprehension",
    title="Squares with a comprehension",
    instructions="Read `n` and print a list of the squares of 1..n using a **list comprehension**.",
    starter='n = int(input("N: "))\nsquares = []\nprint(squares)\n',
    hint="[x ** 2 for x in range(1, n + 1)]",
    solution='n = int(input("N: "))\nsquares = [x ** 2 for x in range(1, n + 1)]\nprint(squares)\n',
    cases=_stdin_cases([
        ("10\n", "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"), ("3\n", "[1, 4, 9]"), ("0\n", "[]"),
    ]),
    must_use=("ListComp",),
))

# ----------------------------------------------------------------- Day 14
_add(14, Task(
    id="filter_evens",
    title="Filter even numbers",
    instructions="Read space-separated integers and print the even ones as a list, using `filter()` and a `lambda`.",
    starter='numbers = [int(x) for x in input("Numbers: ").split()]\nevens = []\nprint(evens)\n',
    hint="evens = list(filter(lambda x: x % 2 == 0, numbers))",
    solution=(
        'numbers = [int(x) for x in input("Numbers: ").split()]\n'
        "evens = list(filter(lambda x: x % 2 == 0, numbers))\nprint(evens)\n"
    ),
    cases=_stdin_cases([
        ("1 2 3 4 5 6 7 8 9 10\n", "[2, 4, 6, 8, 10]"), ("7 9 11\n", "[]"), ("-2 0 5\n", "[-2, 0]"),
    ]),
    must_use=("call:filter", "Lambda"),
))

# ----------------------------------------------------------------- Day 15
_add(15, Task(
    id="debug_practice",
    title="Squash the bugs",
    instructions=(
        "This program should print `Average: 25.0`, but it has several bugs "
        "(syntax errors **and** a logic error). Fix them all!"
    ),
    starter=(
        "numbers = [10, 20, 30, 40\n"
        "total = 0\n"
        "for n in numbers\n"
        "total = n\n"
        'print("Average:", total / len(numbers)\n'
    ),
    hint="Read the error message top to bottom. Check brackets, colons and indentation, then ask: should `total` be replaced or added to?",
    solution=(
        "numbers = [10, 20, 30, 40]\ntotal = 0\nfor n in numbers:\n    total += n\n"
        'print("Average:", total / len(numbers))\n'
    ),
    cases=[Case(expected="Average: 25.0")],
))

# ----------------------------------------------------------------- Day 16
_add(16, Task(
    id="days_between",
    title="Days between two dates",
    instructions=(
        "Write `days_between(start, end)` taking two `\"YYYY-MM-DD\"` strings and returning the number of days "
        "from `start` to `end` as an int."
    ),
    starter="from datetime import datetime\n\ndef days_between(start, end):\n    pass\n",
    hint="datetime.strptime(text, \"%Y-%m-%d\") parses a string; subtracting two datetimes gives a timedelta with .days",
    solution=(
        "from datetime import datetime\n\ndef days_between(start, end):\n"
        '    fmt = "%Y-%m-%d"\n'
        "    return (datetime.strptime(end, fmt) - datetime.strptime(start, fmt)).days\n"
    ),
    cases=[
        Case(harness='show(days_between("2024-01-01", "2024-03-01"))', expected="60"),
        Case(harness='show(days_between("2023-12-25", "2024-01-01"))', expected="7"),
        Case(harness='show(days_between("2024-05-10", "2024-05-10"))', expected="0"),
    ],
    must_use=("import:datetime",),
))

# ----------------------------------------------------------------- Day 17
_add(17, Task(
    id="safe_divide",
    title="Safe divide",
    instructions=(
        "Write `safe_divide(a, b)` that returns `a / b`, but returns `None` instead of crashing "
        "when `b` is zero or the values aren't numbers."
    ),
    starter="def safe_divide(a, b):\n    # Add error handling here\n    pass\n",
    hint="Wrap the division in try/except and catch ZeroDivisionError and TypeError.",
    solution=(
        "def safe_divide(a, b):\n    try:\n        return a / b\n"
        "    except (ZeroDivisionError, TypeError):\n        return None\n"
    ),
    cases=[
        Case(harness="show(safe_divide(10, 2))", expected="5.0"),
        Case(harness="show(safe_divide(10, 0))", expected="None"),
        Case(harness='show(safe_divide("a", 2))', expected="None"),
    ],
    must_use=("Try",),
))

# ----------------------------------------------------------------- Day 18
_add(18, Task(
    id="email_validator",
    title="Email validator",
    instructions="Read an email address and print `Valid` or `Invalid` using the `re` module.",
    starter='import re\n\nemail = input("Enter email: ")\n# Validate with a regex, then print "Valid" or "Invalid"\n',
    hint=r"Try re.fullmatch(r'[\w.+-]+@[\w-]+(\.[\w-]+)+', email)",
    solution=(
        "import re\n\n"
        'email = input("Enter email: ")\n'
        "if re.fullmatch(r\"[\\w.+-]+@[\\w-]+(\\.[\\w-]+)+\", email):\n"
        '    print("Valid")\nelse:\n    print("Invalid")\n'
    ),
    cases=_stdin_cases([
        ("alice@example.com\n", "Valid"), ("bob.smith@mail.co.uk\n", "Valid"),
        ("no-at-sign.com\n", "Invalid"), ("a@b\n", "Invalid"),
        ("@x.com\n", "Invalid"), ("user@@x.com\n", "Invalid"),
    ]),
    must_use=("import:re",),
))

# ----------------------------------------------------------------- Day 19
_add(19, Task(
    id="file_writer",
    title="Write and read a file",
    instructions=(
        "Read a line of text, write it to `output.txt` (using `with`), read the file back and print its contents."
    ),
    starter='text = input("Text: ")\n# Write text to output.txt, then read it back and print it\n',
    hint="with open(\"output.txt\", \"w\") as f: f.write(text) — then open it again with \"r\".",
    solution=(
        'text = input("Text: ")\n'
        'with open("output.txt", "w") as f:\n    f.write(text)\n'
        'with open("output.txt") as f:\n    print(f.read())\n'
    ),
    cases=[
        Case(stdin="Hello, File!\n", expected="Hello, File!"),
        Case(stdin="second run\n", expected="second run"),
        Case(stdin="saved?\n", harness='show(open("output.txt").read().strip())', expected="saved?",
             label="output.txt contains your text"),
    ],
    must_use=("With",),
))

# ----------------------------------------------------------------- Day 20
_add(20, Task(
    id="package_explorer",
    title="Is it installed?",
    instructions="Write `is_installed(name)` returning True if a package/module can be imported, else False.",
    starter="import importlib.util\n\ndef is_installed(name):\n    pass\n",
    hint="importlib.util.find_spec(name) returns None when the module isn't available.",
    solution=(
        "import importlib.util\n\ndef is_installed(name):\n"
        "    return importlib.util.find_spec(name) is not None\n"
    ),
    cases=[
        Case(harness='show(is_installed("json"))', expected="True"),
        Case(harness='show(is_installed("os"))', expected="True"),
        Case(harness='show(is_installed("definitely_not_a_real_package_xyz"))', expected="False"),
    ],
))

# ----------------------------------------------------------------- Day 21
_add(21, Task(
    id="class_creator",
    title="Build a Dog class",
    instructions="Finish the `Dog` class: store `name` and `age`, and make `bark()` return `\"<name> says Woof!\"`.",
    starter=(
        "class Dog:\n    def __init__(self, name, age):\n        # Store the attributes\n        pass\n\n"
        "    def bark(self):\n        # Return the bark message\n        pass\n"
    ),
    hint="Inside __init__: self.name = name. In bark: return f\"{self.name} says Woof!\"",
    solution=(
        "class Dog:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n\n"
        '    def bark(self):\n        return f"{self.name} says Woof!"\n'
    ),
    cases=[
        Case(harness='show(Dog("Buddy", 3).bark())', expected="Buddy says Woof!"),
        Case(harness='d = Dog("Rex", 5)\nshow(d.name, d.age)', expected="Rex 5"),
    ],
    must_use=("ClassDef",),
))

# ----------------------------------------------------------------- Day 22
_PAGE_1 = '<html><head><title>My Page</title></head><body><a href="/about">About</a> <a href="https://example.org">Ex</a></body></html>'
_PAGE_2 = "<html><head><title>Empty</title></head><body><p>No links here</p></body></html>"
_add(22, Task(
    id="web_scraper",
    title="Parse a web page",
    instructions=(
        "The HTML of a page arrives on standard input. Print the `<title>` text, then every link's `href`, one per line.\n"
        "(We use a local HTML string so this works offline — the parsing skills are identical.)"
    ),
    starter=(
        "import sys\nfrom bs4 import BeautifulSoup\n\n"
        'html = sys.stdin.read()\nsoup = BeautifulSoup(html, "html.parser")\n'
        "# Print the title, then each link's href\n"
    ),
    hint="soup.title.text gives the title; for a in soup.find_all(\"a\"): print(a.get(\"href\"))",
    solution=(
        "import sys\nfrom bs4 import BeautifulSoup\n\n"
        'html = sys.stdin.read()\nsoup = BeautifulSoup(html, "html.parser")\n'
        "print(soup.title.text)\nfor a in soup.find_all(\"a\"):\n    print(a.get(\"href\"))\n"
    ),
    cases=[
        Case(stdin=_PAGE_1, expected="My Page\n/about\nhttps://example.org", label="page with two links"),
        Case(stdin=_PAGE_2, expected="Empty", label="page with no links"),
    ],
    must_use=("import:bs4",),
    requires=("bs4",),
))

# ----------------------------------------------------------------- Day 23
_add(23, Task(
    id="venv_creator",
    title="Virtual environment commands",
    instructions=(
        "Write `venv_commands(name, windows=False)` returning a list of two strings: the command to create "
        "the environment and the command to activate it.\n\n"
        "- create: `python -m venv <name>`\n"
        "- activate (Linux/Mac): `source <name>/bin/activate`\n"
        "- activate (Windows): `<name>\\Scripts\\activate`"
    ),
    starter="def venv_commands(name, windows=False):\n    pass\n",
    hint="Build two f-strings and pick the activate one with an if on `windows`.",
    solution=(
        "def venv_commands(name, windows=False):\n"
        '    create = f"python -m venv {name}"\n'
        "    if windows:\n"
        '        activate = f"{name}\\\\Scripts\\\\activate"\n'
        "    else:\n"
        '        activate = f"source {name}/bin/activate"\n'
        "    return [create, activate]\n"
    ),
    cases=[
        Case(harness='show("|".join(venv_commands("env")))', expected="python -m venv env|source env/bin/activate"),
        Case(harness='show("|".join(venv_commands("proj", windows=True)))',
             expected="python -m venv proj|proj\\Scripts\\activate"),
    ],
    must_use=("FunctionDef",),
))

# ----------------------------------------------------------------- Day 24
_add(24, Task(
    id="stats_calculator",
    title="Statistics calculator",
    instructions=(
        "Read space-separated numbers and print three lines: `Mean: x`, `Median: x`, `Stdev: x` "
        "with two decimals (use `statistics`)."
    ),
    starter=(
        "import statistics\n\n"
        'data = [float(x) for x in input("Numbers: ").split()]\n'
        "# Print mean, median and (sample) standard deviation, 2 decimals each\n"
    ),
    hint='Format with f"{value:.2f}". statistics.stdev() is the sample standard deviation.',
    solution=(
        "import statistics\n\n"
        'data = [float(x) for x in input("Numbers: ").split()]\n'
        'print(f"Mean: {statistics.mean(data):.2f}")\n'
        'print(f"Median: {statistics.median(data):.2f}")\n'
        'print(f"Stdev: {statistics.stdev(data):.2f}")\n'
    ),
    cases=_stdin_cases([
        ("1 2 3 4 5 6 7 8 9 10\n", "Mean: 5.50\nMedian: 5.50\nStdev: 3.03"),
        ("2 4 4 4 5 5 7 9\n", "Mean: 5.00\nMedian: 4.50\nStdev: 2.14"),
    ]),
    must_use=("import:statistics",),
))

# ----------------------------------------------------------------- Day 25
_add(25, Task(
    id="pandas_intro",
    title="First DataFrame",
    instructions=(
        "Using the DataFrame `df`, print the average age (one number), then the names of everyone "
        "**older than 28**, one per line."
    ),
    starter=(
        "import pandas as pd\n\n"
        'data = {"Name": ["Alice", "Bob", "Charlie", "Diana"], "Age": [25, 30, 35, 28]}\n'
        "df = pd.DataFrame(data)\n"
        "# 1. Print the average age\n# 2. Print names of people older than 28, one per line\n"
    ),
    hint='df["Age"].mean() for the average; df[df["Age"] > 28]["Name"] filters rows.',
    solution=(
        "import pandas as pd\n\n"
        'data = {"Name": ["Alice", "Bob", "Charlie", "Diana"], "Age": [25, 30, 35, 28]}\n'
        "df = pd.DataFrame(data)\n"
        'print(df["Age"].mean())\n'
        'for name in df[df["Age"] > 28]["Name"]:\n    print(name)\n'
    ),
    cases=[Case(expected="29.5\nBob\nCharlie")],
    must_use=("import:pandas",),
    requires=("pandas",),
))

# ----------------------------------------------------------------- Day 26
_add(26, Task(
    id="flask_hello",
    title="Your first Flask routes",
    instructions=(
        "Make `/` return `Hello, Flask!` and add `/hello/<name>` returning `Hello, <name>!`.\n"
        "We test with Flask's built-in test client, so there's no need to start a server."
    ),
    starter=(
        "from flask import Flask\n\napp = Flask(__name__)\n\n"
        '@app.route("/")\ndef home():\n    return "TODO"\n\n'
        '# Add a route /hello/<name> that returns "Hello, <name>!"\n'
    ),
    hint='@app.route("/hello/<name>") — the function receives `name` as an argument.',
    solution=(
        "from flask import Flask\n\napp = Flask(__name__)\n\n"
        '@app.route("/")\ndef home():\n    return "Hello, Flask!"\n\n'
        '@app.route("/hello/<name>")\ndef hello(name):\n    return f"Hello, {name}!"\n'
    ),
    cases=[Case(
        harness='_c = app.test_client()\nshow(_c.get("/").get_data(as_text=True))\n'
                'show(_c.get("/hello/Ada").get_data(as_text=True))',
        expected="Hello, Flask!\nHello, Ada!",
        label="GET / and GET /hello/Ada",
    )],
    must_use=("import:flask",),
    requires=("flask",),
))

# ----------------------------------------------------------------- Day 27
_add(27, Task(
    id="mongo_queries",
    title="Speak MongoDB",
    instructions=(
        "MongoDB queries and updates are just dictionaries. Write three functions (no database needed):\n\n"
        "- `adults_filter(min_age)` → a filter matching `age >= min_age` (`$gte`)\n"
        "- `birthday_update()` → an update that adds 1 to `age` (`$inc`)\n"
        "- `rename_update(new_name)` → an update that sets `name` (`$set`)"
    ),
    starter=(
        "def adults_filter(min_age):\n    pass\n\n"
        "def birthday_update():\n    pass\n\n"
        "def rename_update(new_name):\n    pass\n"
    ),
    hint='Example shape: {"age": {"$gte": 18}} and {"$set": {"name": "Zed"}}',
    solution=(
        'def adults_filter(min_age):\n    return {"age": {"$gte": min_age}}\n\n'
        'def birthday_update():\n    return {"$inc": {"age": 1}}\n\n'
        'def rename_update(new_name):\n    return {"$set": {"name": new_name}}\n'
    ),
    cases=[
        Case(harness="show(adults_filter(18))", expected="{'age': {'$gte': 18}}"),
        Case(harness="show(birthday_update())", expected="{'$inc': {'age': 1}}"),
        Case(harness='show(rename_update("Zed"))', expected="{'$set': {'name': 'Zed'}}"),
    ],
))

# ----------------------------------------------------------------- Day 28
_add(28, Task(
    id="api_fetcher",
    title="Build requests, read responses",
    instructions=(
        "Two helpers for talking to an API (offline-friendly):\n\n"
        "- `search_url(query, sort)` → the full URL "
        "`https://api.github.com/search/repositories?q=<query>&sort=<sort>` "
        "(let `requests` build the query string)\n"
        "- `top_name(raw_json)` → the `name` of the first item in the JSON's `\"items\"` list"
    ),
    starter=(
        "import json\nimport requests\n\n"
        "def search_url(query, sort):\n    pass\n\n"
        "def top_name(raw_json):\n    pass\n"
    ),
    hint="requests.Request(\"GET\", url, params={...}).prepare().url builds the URL; json.loads parses text.",
    solution=(
        "import json\nimport requests\n\n"
        "def search_url(query, sort):\n"
        '    base = "https://api.github.com/search/repositories"\n'
        '    return requests.Request("GET", base, params={"q": query, "sort": sort}).prepare().url\n\n'
        "def top_name(raw_json):\n    return json.loads(raw_json)[\"items\"][0][\"name\"]\n"
    ),
    cases=[
        Case(harness='show(search_url("python", "stars"))',
             expected="https://api.github.com/search/repositories?q=python&sort=stars"),
        Case(harness='show(search_url("web scraping", "forks"))',
             expected="https://api.github.com/search/repositories?q=web+scraping&sort=forks"),
        Case(harness="""show(top_name('{"items": [{"name": "flask"}, {"name": "django"}]}'))""", expected="flask"),
    ],
    requires=("requests",),
))

# ----------------------------------------------------------------- Day 29
_add(29, Task(
    id="build_api",
    title="A tiny REST API",
    instructions=(
        "Finish the API:\n\n"
        "- `POST /api/users` stores the JSON body and returns it with status **201**\n"
        "- `GET /api/users/<id>` returns the user at that index, or status **404** if it doesn't exist\n\n"
        "(`GET /api/users` is already done. Tested with Flask's test client.)"
    ),
    starter=(
        "from flask import Flask, jsonify, request\n\napp = Flask(__name__)\nusers = []\n\n"
        '@app.route("/api/users", methods=["GET"])\ndef get_users():\n    return jsonify(users)\n\n'
        "# Implement POST /api/users\n# Implement GET /api/users/<int:user_id>\n"
    ),
    hint="Use request.get_json(), users.append(...), and return jsonify(user), 201. For a missing id, return jsonify(...), 404.",
    solution=(
        "from flask import Flask, jsonify, request\n\napp = Flask(__name__)\nusers = []\n\n"
        '@app.route("/api/users", methods=["GET"])\ndef get_users():\n    return jsonify(users)\n\n'
        '@app.route("/api/users", methods=["POST"])\ndef create_user():\n'
        "    user = request.get_json()\n    users.append(user)\n    return jsonify(user), 201\n\n"
        '@app.route("/api/users/<int:user_id>")\ndef get_user(user_id):\n'
        "    if 0 <= user_id < len(users):\n        return jsonify(users[user_id])\n"
        '    return jsonify({"error": "not found"}), 404\n'
    ),
    cases=[Case(
        harness=(
            '_c = app.test_client()\n'
            'r = _c.post("/api/users", json={"name": "Ada"}); show(r.status_code, r.get_json())\n'
            'r = _c.get("/api/users"); show(r.status_code, r.get_json())\n'
            'r = _c.get("/api/users/0"); show(r.status_code, r.get_json())\n'
            'r = _c.get("/api/users/9"); show(r.status_code)'
        ),
        expected="201 {'name': 'Ada'}\n200 [{'name': 'Ada'}]\n200 {'name': 'Ada'}\n404",
        label="POST, list, get one, get missing",
    )],
    requires=("flask",),
))

# ----------------------------------------------------------------- Day 30
_add(30, Task(
    id="final_project",
    title="Capstone mini-project",
    instructions=(
        "Build any small program you like (a to-do list, quiz, expense tracker...). To pass it must run without "
        "errors, print something, and use **a class**, **a function** and **a `with` block** (file handling)."
    ),
    starter=(
        "# Combine what you've learned: a class, a function and file handling.\n"
        "# Idea: a tiny to-do list that saves tasks to a file.\n\n"
        'print("Project complete!")\n'
    ),
    hint="Make a class to hold your data, a function to do one job, and use `with open(...)` to save or load something.",
    solution=(
        "class Todo:\n    def __init__(self):\n        self.items = []\n\n"
        "    def add(self, item):\n        self.items.append(item)\n\n"
        "def save(todo, path):\n    with open(path, \"w\") as f:\n        f.write(\"\\n\".join(todo.items))\n\n"
        't = Todo()\nt.add("learn python")\nsave(t, "todo.txt")\nprint("Project complete!")\n'
    ),
    cases=[Case(mode="nonempty", label="runs and prints something")],
    must_use=("ClassDef", "FunctionDef", "With"),
))


def get_day_tasks(day: int) -> List[Task]:
    return TASKS.get(day, [])
