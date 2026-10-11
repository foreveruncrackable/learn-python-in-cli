# Day 3: Operators

> **Big idea:** operators are the symbols that *do something* with values: add them, compare them, combine conditions.

## Arithmetic Operators
```python
a = 10
b = 3
print(a + b)   # 13   addition
print(a - b)   # 7    subtraction
print(a * b)   # 30   multiplication
print(a / b)   # 3.333...  division (always gives a float)
print(a // b)  # 3    floor division: divide, then drop the decimals
print(a % b)   # 1    modulus: the remainder after dividing
print(a ** b)  # 1000 exponent: 10 to the power 3
```
Useful tricks:
- `n % 2 == 0` → `n` is even.
- `n % 10` → the last digit of `n`.
- Python does `**` first, then `* / // %`, then `+ -`. Use parentheses to be clear: `(a + b) * 2`.

## Assignment Operators (shortcuts)
```python
x = 5
x += 2    # same as x = x + 2  -> 7
x -= 1    # 6
x *= 3    # 18
x //= 4   # 4
```

## Boolean Values
A **boolean** is either `True` or `False`. Comparisons produce booleans.

## Comparison Operators
```python
print(5 == 5)   # True   equal to
print(5 != 3)   # True   not equal to
print(5 > 3)    # True   greater than
print(5 < 3)    # False  less than
print(5 >= 5)   # True   greater than or equal
print(5 <= 4)   # False  less than or equal
```
**`=` stores a value. `==` asks "are these equal?"** Mixing them up is the #1 beginner bug.

## Logical Operators
Combine booleans with words, not symbols:
```python
age = 20
print(age > 18 and age < 30)   # True  -> BOTH must be true
print(age < 18 or age > 60)    # False -> AT LEAST ONE must be true
print(not age > 18)            # False -> flips True/False
```

## Identity & Membership
```python
print(3 in [1, 2, 3])        # True   is it inside?
print("a" not in "cat")      # False
x = [1]; y = [1]
print(x == y)                # True   same value
print(x is y)                # False  not the same object in memory
```
Use `==` to compare values. Use `is` mainly for `None`: `if x is None:`.

## Key terms
- **operator**: a symbol (`+`, `==`, `and`) that acts on values.
- **operand**: a value an operator works on (in `3 + 4`, the 3 and 4).
- **boolean**: `True` / `False`.
- **modulus**: the remainder of a division.
- **expression**: code that produces a value, like `3 + 4 * 2`.

## Watch out
- `10 / 2` is `5.0` (float), not `5`. Use `//` for a whole number.
- `1 < x < 10` is valid and means "between"; no need for `and`.
- Comparing text to a number (`"5" == 5`) is `False`, not an error: convert first.
- **Remember:** `and`/`or`/`not` are English words in Python; there's no `&&` or `||`.

## Today's Task
Build a calculator that reads two numbers and an operator (and handles dividing by zero).
