# Day 19: File Handling

> **Big idea:** variables vanish when your program ends. Files let data survive.

## Opening a File
```python
with open("data.txt", "r") as file:
    content = file.read()
```
- `open(path, mode)` connects to a file.
- `with ... as file:` **closes the file automatically** when the block ends, even if an error occurs. Always use it.

### Modes
- `"r"` read (default; error if the file doesn't exist)
- `"w"` write: **erases** existing content, creates the file if missing
- `"a"` append: adds to the end
- `"x"` create new; error if it already exists
- add `"b"` for binary files (images, PDFs): `"rb"`, `"wb"`

## Reading
```python
with open("data.txt", "r") as file:
    text = file.read()            # the whole file as ONE string

with open("data.txt", "r") as file:
    for line in file:             # one line at a time (best for big files)
        print(line.strip())       # strip() removes the trailing \n

with open("data.txt", "r") as file:
    lines = file.readlines()      # a list of lines
```

## Writing
```python
with open("output.txt", "w") as file:      # overwrites!
    file.write("Hello, World!\n")          # write() does NOT add a newline

with open("output.txt", "a") as file:      # adds to the end
    file.write("New line\n")
```
`write()` only accepts strings: `file.write(str(42))`.

## Paths
```python
from pathlib import Path

path = Path("notes") / "day1.txt"       # works on Windows, Mac and Linux
print(path.exists())                    # True / False
path.parent.mkdir(exist_ok=True)        # create the folder if needed
text = path.read_text(encoding="utf-8") # quick read
path.write_text("hi", encoding="utf-8") # quick write
```
A **relative** path (`data.txt`) starts from where the program runs; an **absolute** path starts from the drive root (`/home/me/data.txt`).

## JSON: saving structured data
JSON is a text format for dictionaries and lists, and every language understands it.
```python
import json

data = {"name": "Alice", "age": 25}
with open("data.json", "w") as f:
    json.dump(data, f)            # Python -> file

with open("data.json", "r") as f:
    loaded = json.load(f)         # file -> Python
print(loaded["name"])             # Alice
```
`json.dumps(obj)` / `json.loads(text)` do the same with strings.

## CSV: tables
```python
import csv
with open("people.csv", newline="") as f:
    for row in csv.DictReader(f):     # each row becomes a dict
        print(row["name"])
```

## Key terms
- **file mode**: how you open a file (read, write, append).
- **context manager**: the `with` statement that cleans up for you.
- **path**: the location of a file.
- **JSON / CSV**: common text formats for data / tables.
- **encoding**: how characters become bytes (use `utf-8`).

## Watch out
- `"w"` **deletes** what was there. Use `"a"` to keep it.
- `FileNotFoundError`: wrong folder or name. Print `Path.cwd()` to see where you are.
- Lines read from a file end with `\n`; use `.strip()`.
- After `file.read()` the "cursor" is at the end; reading again gives `""`.
- **Remember:** always `with open(...)`; never leave files open.

## Today's Task
Write a line of text to a file, then read it back.
