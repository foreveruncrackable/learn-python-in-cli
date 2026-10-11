"""Two quick multiple-choice questions per day.

Each entry: (question, [options], index_of_correct_option, explanation)
"""

QUIZZES = {
    1: [
        ("Which function displays text on the screen?", ["echo()", "print()", "console.log()", "write()"], 1,
         "print() writes its arguments to the terminal."),
        ("How does Python mark a block of code?", ["Curly braces", "Indentation", "begin/end", "Semicolons"], 1,
         "Indentation is part of Python's syntax."),
    ],
    2: [
        ("What is the type of 3.0?", ["int", "float", "str", "decimal"], 1, "Numbers with a decimal point are floats."),
        ("What does int(\"42\") return?", ["The string \"42\"", "The integer 42", "42.0", "An error"], 1,
         "int() converts a numeric string into an integer."),
    ],
    3: [
        ("What is 7 // 2?", ["3.5", "3", "4", "1"], 1, "// is floor division: it rounds down."),
        ("What is 7 % 2?", ["0", "1", "3", "3.5"], 1, "% gives the remainder of the division."),
    ],
    4: [
        ("What does \"Python\"[::-1] produce?", ["Python", "nohtyP", "P", "Error"], 1,
         "A step of -1 walks the string backwards."),
        ("What does \"a,b,c\".split(\",\") return?", ["\"abc\"", "['a', 'b', 'c']", "('a','b','c')", "3"], 1,
         "split() returns a list of the pieces."),
    ],
    5: [
        ("What is [1, 2, 3][-1]?", ["1", "2", "3", "Error"], 2, "Negative indexes count from the end."),
        ("Which method adds one item to the end of a list?", ["add()", "append()", "push()", "insert_end()"], 1,
         "list.append(x) adds x at the end."),
    ],
    6: [
        ("Tuples are...", ["Mutable", "Immutable", "Unordered", "Key-value pairs"], 1,
         "Once created, a tuple can't be changed."),
        ("How do you write a one-item tuple?", ["(5)", "(5,)", "[5]", "{5}"], 1,
         "The trailing comma is what makes it a tuple."),
    ],
    7: [
        ("What do sets guarantee?", ["Order", "Unique items", "Sorted items", "Indexes"], 1,
         "Duplicates are discarded automatically."),
        ("What is {1, 2} & {2, 3}?", ["{1, 2, 3}", "{2}", "{1, 3}", "{}"], 1, "& is intersection: items in both."),
    ],
    8: [
        ("How do you read a key without risking KeyError?", ["d[\"k\"]", "d.get(\"k\")", "d.find(\"k\")", "d.k"], 1,
         "get() returns None (or a default) for a missing key."),
        ("Which method gives keys and values together?", ["d.keys()", "d.values()", "d.items()", "d.pairs()"], 2,
         "items() yields (key, value) pairs."),
    ],
    9: [
        ("Which keyword means \"else if\"?", ["elseif", "elif", "else if", "otherwise"], 1, "Python spells it elif."),
        ("What is `x if cond else y` called?", ["A ternary expression", "A loop", "A decorator", "A lambda"], 0,
         "It's a one-line conditional expression."),
    ],
    10: [
        ("What does `break` do?", ["Skips one iteration", "Exits the loop", "Stops the program", "Restarts the loop"], 1,
         "break leaves the nearest enclosing loop."),
        ("What does range(3) produce?", ["1, 2, 3", "0, 1, 2", "0, 1, 2, 3", "3"], 1, "range stops *before* its argument."),
    ],
    11: [
        ("What does a function return if it has no return statement?", ["0", "\"\"", "None", "Error"], 2,
         "Functions return None by default."),
        ("What does *args collect?", ["Keyword arguments", "Extra positional arguments", "A list only", "Nothing"], 1,
         "*args packs extra positional arguments into a tuple."),
    ],
    12: [
        ("How do you import only sqrt from math?", ["import sqrt from math", "from math import sqrt", "using math.sqrt", "include math"], 1,
         "from module import name."),
        ("What makes a file a module?", ["A special header", "It's just a .py file", "A __module__ line", "Compiling it"], 1,
         "Any .py file can be imported."),
    ],
    13: [
        ("What is [x * 2 for x in range(3)]?", ["[0, 1, 2]", "[0, 2, 4]", "[2, 4, 6]", "[0, 2]"], 1,
         "x runs over 0, 1, 2 and each is doubled."),
        ("Which is dictionary-comprehension syntax?", ["[k: v for ...]", "{k: v for ...}", "(k: v for ...)", "{k, v for ...}"], 1,
         "Dict comprehensions use curly braces with key: value."),
    ],
    14: [
        ("filter(f, items) keeps items where f(item) is...", ["False", "True", "None", "An int"], 1,
         "Only items for which the function is truthy survive."),
        ("What does map() return in Python 3?", ["A list", "A lazy iterator", "A tuple", "A set"], 1,
         "Wrap it in list() to see the values."),
    ],
    15: [
        ("What error does \"5\" + 5 raise?", ["ValueError", "TypeError", "NameError", "SyntaxError"], 1,
         "You can't add a str and an int."),
        ("Which standard module helps you log messages?", ["print", "logging", "debug", "trace"], 1,
         "logging is the built-in logging framework."),
    ],
    16: [
        ("Subtracting two datetimes gives a...", ["int", "float", "timedelta", "date"], 2, "A timedelta with .days, .seconds..."),
        ("What does strftime do?", ["Parses a string", "Formats a date as text", "Sleeps", "Adds days"], 1,
         "strftime = string-format-time; strptime parses."),
    ],
    17: [
        ("Which block runs whether or not an error occurred?", ["else", "finally", "except", "try"], 1,
         "finally always runs."),
        ("Which exception does 1 / 0 raise?", ["ValueError", "ArithmeticError only", "ZeroDivisionError", "OverflowError"], 2,
         "ZeroDivisionError (a subclass of ArithmeticError)."),
    ],
    18: [
        ("What does \\d match in a regex?", ["Any letter", "A digit", "A dot", "Whitespace"], 1, "\\d is a digit; \\w word char; \\s whitespace."),
        ("What does re.findall return?", ["First match only", "A list of all matches", "True/False", "A count"], 1,
         "findall collects every match into a list."),
    ],
    19: [
        ("Why use `with open(...)`?", ["It's faster", "It closes the file automatically", "It encrypts data", "It's required"], 1,
         "The file is closed even if an error occurs."),
        ("Which mode appends to an existing file?", ["\"r\"", "\"w\"", "\"a\"", "\"x\""], 2, "\"w\" would overwrite it."),
    ],
    20: [
        ("Which file conventionally lists a project's dependencies?", ["setup.txt", "requirements.txt", "deps.py", "packages.json"], 1,
         "requirements.txt is the pip convention."),
        ("What does `pip install -r requirements.txt` do?", ["Removes packages", "Installs everything listed", "Upgrades Python", "Lists packages"], 1,
         "-r reads package names from a file."),
    ],
    21: [
        ("What is `self` in a method?", ["The class", "The instance the method is called on", "A keyword for private data", "The parent class"], 1,
         "self refers to the current object."),
        ("Which line makes Cat inherit from Animal?", ["class Cat: Animal", "class Cat(Animal):", "class Cat extends Animal:", "Cat = Animal()"], 1,
         "Parent classes go in parentheses."),
    ],
    22: [
        ("Which library parses HTML in this course?", ["BeautifulSoup", "NumPy", "Flask", "pytest"], 0, "bs4 (BeautifulSoup)."),
        ("What does robots.txt tell scrapers?", ["Passwords", "Which paths may be crawled", "Page titles", "Nothing"], 1,
         "Respect it — scraping ethically matters."),
    ],
    23: [
        ("Why use a virtual environment?", ["To speed up Python", "To isolate project dependencies", "To hide code", "To compile code"], 1,
         "Each project gets its own packages."),
        ("Which command creates one?", ["python -m venv env", "pip venv env", "python create env", "venv --new env"], 0,
         "python -m venv <folder>."),
    ],
    24: [
        ("Which statistic measures how spread out data is?", ["Mean", "Median", "Standard deviation", "Mode"], 2,
         "Standard deviation measures spread around the mean."),
        ("What is the median of [1, 3, 2]?", ["1", "2", "3", "2.5"], 1, "Sort it: 1, 2, 3 — the middle is 2."),
    ],
    25: [
        ("What is a single labelled column in pandas?", ["DataFrame", "Series", "Array", "Index"], 1,
         "A DataFrame is made of Series."),
        ("What does df.head() show?", ["The last row", "The first 5 rows", "Column names only", "Statistics"], 1,
         "head() previews the top rows."),
    ],
    26: [
        ("Which decorator maps a URL to a function in Flask?", ["@app.url", "@app.route", "@flask.path", "@route.app"], 1,
         "@app.route(\"/path\")."),
        ("What does render_template do?", ["Sends JSON", "Fills in an HTML template", "Connects to a DB", "Restarts the server"], 1,
         "It renders a Jinja2 template."),
    ],
    27: [
        ("MongoDB stores data as...", ["Rows in tables", "JSON-like documents", "CSV files", "Key only"], 1, "Documents (BSON) in collections."),
        ("What does the $set operator do?", ["Deletes a field", "Sets a field's value", "Sorts results", "Counts documents"], 1,
         "$set assigns new values in an update."),
    ],
    28: [
        ("Which HTTP method normally creates a resource?", ["GET", "POST", "DELETE", "HEAD"], 1, "POST creates; GET reads."),
        ("What does status code 404 mean?", ["Server error", "Not found", "Created", "Unauthorized"], 1,
         "The requested resource doesn't exist."),
    ],
    29: [
        ("What does status 201 mean?", ["OK", "Created", "No content", "Bad request"], 1, "201 = a new resource was created."),
        ("What does jsonify do?", ["Parses JSON", "Turns data into a JSON response", "Validates input", "Opens a file"], 1,
         "It builds a Response with JSON content."),
    ],
    30: [
        ("What's the best way to keep improving?", ["Stop practising", "Build real projects", "Memorise the docs", "Avoid errors"], 1,
         "Projects turn knowledge into skill."),
        ("Which structure bundles data and behaviour together?", ["List", "Class", "Tuple", "Set"], 1, "That's what classes are for."),
    ],
}
