# Day 4: Strings

> **Big idea:** a string is a *sequence of characters*. Once you can pick characters by position, you can do almost anything with text.

## Creating Strings
```python
s1 = "Hello"
s2 = 'World'                 # single or double quotes: same thing
s3 = """This string
spans many lines"""          # triple quotes allow line breaks
```
Use the other kind of quote to put a quote inside: `"It's fine"`.

## Joining & Repeating
```python
print("Hello" + " " + "World")   # Hello World   (concatenation)
print("ha" * 3)                  # hahaha
print(len("Python"))             # 6   number of characters
```

## Escape Sequences
A backslash `\` followed by a letter makes a special character:
- `\n` new line · `\t` tab · `\\` a real backslash · `\"` a quote inside quotes
```python
print("Line 1\nLine 2")
```

## Indexing: one character
Counting starts at **0**. Negative numbers count from the end.
```python
s = "Python"
#    P  y  t  h  o  n
#    0  1  2  3  4  5      positive index
#   -6 -5 -4 -3 -2 -1      negative index
print(s[0])     # P
print(s[-1])    # n
```

## Slicing: several characters
`s[start:stop:step]` takes from `start` up to **but not including** `stop`.
```python
s = "Python"
print(s[0:4])    # Pyth     (positions 0,1,2,3)
print(s[2:])     # thon     (from 2 to the end)
print(s[:3])     # Pyt      (from the start up to 3)
print(s[::2])    # Pto      (every 2nd character)
print(s[::-1])   # nohtyP   (step -1 = backwards)
```

## String Methods
A method is a function that belongs to a value, called with a dot.
```python
s = "Hello World"
print(s.upper())                    # HELLO WORLD
print(s.lower())                    # hello world
print(s.replace("World", "Python")) # Hello Python
print(s.split())                    # ['Hello', 'World']
print("  hi  ".strip())             # hi    (removes spaces at both ends)
print(s.startswith("Hell"))         # True
print(s.find("World"))              # 6     (index, or -1 if missing)
print(s.count("l"))                 # 3
print("-".join(["a", "b", "c"]))    # a-b-c
```
Handy checks: `.isdigit()`, `.isalpha()`, `.isupper()`, and `"ell" in s` → `True`.

## Formatting with f-strings
Put `f` before the quotes and variables inside `{ }`:
```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old")
print(f"Pi is about {3.14159:.2f}")   # 3.14  (2 decimals)
print(f"{age + 1} next year")         # any expression works
```

## Key terms
- **sequence**: an ordered collection you can index (strings, lists, tuples).
- **index**: a character's position, starting at 0.
- **slice**: a piece of a sequence.
- **concatenation**: joining strings with `+`.
- **method**: a function attached to a value (`s.upper()`).
- **immutable**: can't be changed after creation.

## Watch out
- **Strings are immutable.** `s[0] = "J"` is an error. Build a new string instead.
- Methods **return a new string**; they don't change the old one. `s.upper()` alone does nothing useful: write `s = s.upper()`.
- The slice stop is *excluded*, so `s[0:4]` has 4 characters, not 5.
- `"Age: " + 25` fails. Use `f"Age: {25}"` or `str(25)`.
- **Remember:** `s[::-1]` reverses any sequence.

## Today's Task
Read a string and print it reversed.
