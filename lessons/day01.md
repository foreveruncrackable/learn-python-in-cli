# Day 1: Introduction & Setup

> **Big idea:** a program is a list of instructions. Python reads them top to bottom and does what they say.

## What is Python?
Python is a programming language designed to be easy to read. Three words you'll hear:
- **High-level**: it reads close to English; you don't manage computer memory yourself.
- **Interpreted**: Python runs your code line by line. There is no separate "build" step.
- **General-purpose**: websites, data analysis, AI, automation, games... one language, many jobs.

It was created by Guido van Rossum and released in 1991.

## Two ways to run Python
1. **Interactive shell**: type `python` (or `python3`) in a terminal, then type one line at a time and see the result instantly. Great for experiments. Leave with `exit()`.
2. **Script**: save code in a file like `hello.py`, then run `python hello.py`. Use this for real programs.

## Your First Program
```python
print("Hello, World!")
```
- `print` is a **function**: a named action. The parentheses `( )` hold what you give it.
- `"Hello, World!"` is a **string**: text inside quotes.
- Result on screen: `Hello, World!`

## The Basic Rules
```python
# This is a comment: Python ignores it. It's a note for humans.
name = "Ada"        # a comment can follow code
if name == "Ada":
    print("Hi Ada")  # 4 spaces of indentation = "inside the if"
```
- **Indentation matters.** The spaces at the start of a line show which lines belong together.
- **Case matters.** `print` works, `Print` does not.
- **Quotes must match.** `"hi"` or `'hi'`, never `"hi'`.
- **No semicolons** needed at the end of a line.

## Key terms
- **program / script**: a file of instructions.
- **interpreter**: the tool (`python`) that reads and runs your code.
- **statement**: one instruction, usually one line.
- **function**: a named, reusable action, e.g. `print()`.
- **string**: text in quotes.
- **comment**: a note starting with `#`, ignored by Python.
- **syntax error**: Python can't understand your code's grammar (a typo, missing quote or bracket).

## Watch out
- `SyntaxError` almost always means a missing quote, bracket or colon. Read the line the error points to, and the line above it.
- `IndentationError`: don't mix tabs and spaces. Use 4 spaces.
- If `python` isn't found, try `python3`.
- **Remember:** errors are normal. Read the *last line* of the message first; it says what went wrong.

## Today's Task
Write your first Python program: print `Hello, World!`
