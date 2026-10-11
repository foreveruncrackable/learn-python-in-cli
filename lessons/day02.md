# Day 2: Variables & Data Types

> **Big idea:** a variable is a *name* attached to a value so you can use it again later.

## Variables
```python
name = "Alice"
age = 25
height = 5.6
is_student = True
```
- `=` means **assign**: "store the value on the right under the name on the left". It is *not* a math equals sign.
- You can change what a name points to at any time: `age = 26`.
- Python figures out the type from the value. You don't declare it.

### Naming rules
- Start with a letter or `_`, never a number: `age1` ✓  `1age` ✗
- Only letters, digits and `_`: no spaces or `-`
- Case-sensitive: `age` and `Age` are different names
- Can't be a reserved word such as `if`, `for`, `class`
- Style: use **snake_case** and descriptive names: `first_name`, not `fn`

## Data Types
Every value has a **type** that decides what you can do with it.
- **int**: whole numbers → `42`, `-7`
- **float**: numbers with a decimal point → `3.14`
- **str**: text → `"Hello"`
- **bool**: `True` or `False` (capital first letter!)
- **list, tuple, set, dict**: collections of values (Days 5-8)

```python
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("hi"))      # <class 'str'>
print(type(True))      # <class 'bool'>
```
`type()` tells you what something is. Use it whenever you're confused.

## Type Casting (converting)
```python
x = int("42")       # "42" (text)  -> 42 (number)
y = str(42)         # 42 (number)  -> "42" (text)
z = float("3.14")   # "3.14"       -> 3.14
n = int(7.9)        # 7  (cuts off the decimals, does not round)
```
`"5" + 5` fails because Python won't guess whether you want text or math. Convert first.

## Getting Input
```python
name = input("What is your name? ")
print("Hello,", name)

age = int(input("Age: "))   # input() ALWAYS gives text, so convert it
```

## Handy Built-in Functions
- `print(a, b)`: show values (separated by a space)
- `len(x)`: length of text or a collection
- `type(x)`: the type of `x`
- `input(prompt)`: ask the user for text
- `int()`, `float()`, `str()`: convert

## Multiple Assignment
```python
a, b, c = 1, 2, 3     # three variables at once
x = y = 0             # same value for both
a, b = b, a           # swap two variables (needs no temp variable!)
```

## Key terms
- **variable**: a name that refers to a value.
- **assignment**: giving a name a value with `=`.
- **type**: the kind of value (int, str, ...).
- **casting**: converting from one type to another.
- **argument**: the value you pass into a function, e.g. `"hi"` in `print("hi")`.

## Watch out
- `input()` always returns a **string**: `input("5") + 1` is an error. Wrap it: `int(input(...))`.
- `int("3.5")` fails: go through float first: `int(float("3.5"))`.
- Don't name a variable `list`, `str`, `type`, `input`... you'd hide the built-in function.
- **Remember:** a variable is a label, not a box. Two names can point to the same value.

## Today's Task
Swap two variables without a temporary variable.
