# Day 12: Modules

> **Big idea:** a module is a file of ready-made code. `import` lets you borrow it instead of rewriting it.

## Importing
```python
import math
print(math.pi)          # 3.14159...
print(math.sqrt(16))    # 4.0

from math import sqrt   # take just one name
print(sqrt(25))         # 5.0

import random as rnd    # give it a shorter nickname
print(rnd.randint(1, 10))
```
- `import x` → use as `x.name`.
- `from x import name` → use `name` directly.
- `import x as y` → use as `y.name`.

## The Standard Library
Python comes with hundreds of modules, no installation needed:
- `math`: `sqrt`, `ceil`, `floor`, `pi`
- `random`: `randint`, `choice`, `shuffle`
- `datetime`: dates and times (Day 16)
- `os`: files, folders, environment
- `sys`: Python itself, command-line arguments
- `json`: read and write JSON
- `re`: regular expressions (Day 18)

Explore any module in the shell:
```python
import math
print(dir(math))      # list everything inside it
help(math.sqrt)       # read its documentation
```

## Creating Your Own Module
Any `.py` file is a module. Put two files in the same folder:
```python
# mymodule.py
def greet(name):
    return f"Hello, {name}!"
```
```python
# main.py
import mymodule                    # the file name, without .py
print(mymodule.greet("Alice"))
```

## Running vs Importing
```python
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":     # True only when you run THIS file directly
    print(greet("test"))       # not run when another file imports it
```

## Third-party Modules
Others publish modules you can install with `pip install package_name` (Day 20), ideally inside a virtual environment (Day 23).

## Key terms
- **module**: a Python file you can import.
- **package**: a folder of modules.
- **standard library**: the modules that ship with Python.
- **namespace**: the `module.` prefix that keeps names apart.
- **alias**: a nickname given with `as`.

## Watch out
- `ModuleNotFoundError`: the module isn't installed, or your file isn't in the same folder.
- Never name your own file like a real module (`random.py`, `math.py`); it hides the real one.
- Avoid `from x import *`; you can't tell where names come from.
- **Remember:** `dir(module)` and `help(thing)` are your built-in cheat sheet.

## Today's Task
Import the provided `helpers` module and use its functions.
