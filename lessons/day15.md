# Day 15: Type Errors & Debugging

> **Big idea:** bugs are normal. Reading the error message is the skill that makes you fast.

## Reading a Traceback
Read from the **bottom up**: the last line says *what* went wrong, the lines above say *where*.
```text
Traceback (most recent call last):
  File "app.py", line 3, in <module>
    print(total / count)
ZeroDivisionError: division by zero
```
- `ZeroDivisionError: division by zero` → the problem
- `line 3` → where to look first

## Common Errors
```python
print(undefined_var)      # NameError: the name doesn't exist (typo? not defined yet?)
"hello" + 5               # TypeError: wrong type for that operation
lst = [1, 2, 3]
print(lst[5])             # IndexError: position doesn't exist
d = {"a": 1}
print(d["b"])             # KeyError: key doesn't exist
int("abc")                # ValueError: right type, impossible value
10 / 0                    # ZeroDivisionError
```
Also: `SyntaxError` (grammar is wrong, Python can't even start), `IndentationError`, `AttributeError` (that object has no such method), `ModuleNotFoundError`.

## Two Kinds of Bugs
- **Crash (error)**: Python stops and tells you. Easy to find.
- **Logic bug**: no error, but the answer is wrong. You must investigate.

## Debugging Steps
1. **Read** the error message and the line number.
2. **Reproduce** it with the smallest possible input.
3. **Print** variables to see what they really hold: `print("x =", x, type(x))`.
4. **Test small pieces** separately instead of the whole program.
5. **Change one thing at a time**, then run again.

## The Debugger (pdb)
Pause your program and look around:
```python
breakpoint()      # (same as: import pdb; pdb.set_trace())
```
In the `(Pdb)` prompt: `n` next line · `s` step into · `c` continue · `p x` print x · `q` quit.

## Logging instead of print
```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Starting")        # INFO:root:Starting
logging.warning("Careful")
```
Logs have levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`) and can be switched off without deleting lines.

## Key terms
- **bug**: a mistake in a program.
- **traceback**: the report of where an error happened.
- **exception**: an error raised while running.
- **debugging**: finding and fixing bugs.
- **breakpoint**: a place where the program pauses.

## Watch out
- Fix the **first** error in the list; later ones are often side-effects.
- If the line looks fine, the mistake is often on the line *above* it (a missing bracket).
- Don't guess randomly. Print, look, then change.
- **Remember:** explaining your code line by line out loud ("rubber duck debugging") finds many bugs.

## Today's Task
Fix a broken program that has syntax errors *and* a logic bug.
