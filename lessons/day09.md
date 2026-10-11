# Day 9: Conditionals

> **Big idea:** conditionals let your program *decide*. Different situation, different action.

Normally Python runs lines top to bottom. `if` lets it skip some lines depending on a condition (something that's `True` or `False`).

## if
```python
age = 18
if age >= 18:                 # the colon is required
    print("You are an adult") # indented = runs only if the condition is True
print("This always runs")     # not indented = outside the if
```

## if / else
```python
age = 16
if age >= 18:
    print("You are an adult")
else:                         # runs when the condition is False
    print("You are a minor")
```

## if / elif / else
For more than two outcomes. Python checks top to bottom and runs the **first** block that's true, then skips the rest.
```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:     # only reached if score < 90
    grade = "B"
elif score >= 70:
    grade = "C"
else:                 # nothing above was true
    grade = "F"
print(grade)          # B
```
Order matters: put the strictest condition first.

## Combining Conditions
```python
age = 25
has_id = True
if age >= 18 and has_id:
    print("Entry allowed")
if age < 13 or age > 65:
    print("Discount")
```
Nested ifs can usually be flattened with `and`:
```python
if age >= 18:
    if has_id:        # same as: if age >= 18 and has_id
        print("Entry allowed")
```

## Ternary (one-line if/else)
```python
status = "adult" if age >= 18 else "minor"
```
Read: "value-if-true `if` condition `else` value-if-false". Keep it for short, simple cases.

## Truthy and Falsy
Python treats some values as `False` in a condition: `0`, `0.0`, `""`, `[]`, `{}`, `()`, `set()` and `None`. Everything else is `True`.
```python
items = []
if items:                     # False because the list is empty
    print("has items")
else:
    print("nothing here")
```

## Key terms
- **condition**: an expression that's `True` or `False`.
- **block**: the indented lines under an `if`/`else`.
- **branch**: one possible path through the code.
- **truthy / falsy**: counts as True / False in a condition.

## Watch out
- `if x = 5:` is an error; you want `==`.
- Forgetting the colon `:` or the indent is a `SyntaxError` / `IndentationError`.
- With `elif`, only one branch runs. With separate `if`s, several can run.
- `if x == True:` is clumsy: write `if x:`.
- **Remember:** test boundaries! `>= 90` includes 90; `> 90` doesn't.

## Today's Task
Turn a numeric score into a letter grade.
