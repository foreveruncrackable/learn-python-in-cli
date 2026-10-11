# Day 17: Exception Handling

> **Big idea:** errors will happen (bad input, missing file). `try/except` lets your program react instead of crashing.

An **exception** is an error raised while the program runs. If nothing handles it, the program stops.

## try / except
```python
try:
    result = 10 / 0          # code that might fail
except ZeroDivisionError:    # what to do if THAT error happens
    print("Cannot divide by zero!")
print("Program keeps going")
```
Python runs the `try` block. If an error occurs, it jumps to the matching `except`. If not, `except` is skipped.

## Handling Different Errors
```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("That wasn't a number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except (TypeError, KeyError):         # several at once
    print("Wrong type or missing key")
```
Catch **specific** errors. A bare `except:` hides every bug, even typos.

## Getting the Error Message
```python
try:
    int("abc")
except ValueError as e:
    print("Problem:", e)    # invalid literal for int() with base 10: 'abc'
```

## else and finally
```python
try:
    number = int("42")
except ValueError:
    print("Bad number")
else:
    print("Worked!", number)      # runs only if NO error happened
finally:
    print("Always runs")          # runs no matter what: cleanup
```

## Raising Your Own Errors
```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return age
```
`raise` stops the function and signals a problem to the caller.

## Custom Exceptions
```python
class AgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise AgeError("Age cannot be negative!")
```
A custom name makes errors easier to catch and understand in bigger programs.

## Best Practices
- Keep the `try` block **small**: only the line that can fail.
- Catch specific exceptions.
- Don't silence errors with `except: pass`.
- Prefer checking first when it's simple (`if b != 0`), and use `try` for things you can't predict (files, network, user input).

## Key terms
- **exception**: an error at run time.
- **raise**: trigger an exception yourself.
- **handle / catch**: respond to an exception with `except`.
- **finally**: cleanup code that always runs.

## Watch out
- `except Exception` is better than a bare `except`, but specific is best.
- Order matters: put specific exceptions before general ones.
- A `try` without a matching `except` or `finally` is a `SyntaxError`.
- **Remember:** read an exception name like a sentence: `ZeroDivisionError` = "you divided by zero".

## Today's Task
Write a `safe_divide(a, b)` function that never crashes.
