# Day 13: List Comprehension

> **Big idea:** a comprehension builds a new list in one readable line, instead of an empty list + loop + append.

## The Pattern
```python
# The long way
squares = []
for x in range(1, 6):
    squares.append(x ** 2)

# The comprehension way
squares = [x ** 2 for x in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]
```
Read it as: **"give me `x ** 2` for each `x` in `range(1, 6)`"**.
```
[  expression   for  item  in  iterable  ]
   what to keep      how to loop
```

## Adding a Condition (filter)
Put `if` at the end to keep only some items:
```python
evens = [x for x in range(20) if x % 2 == 0]
words = ["apple", "kiwi", "banana"]
long_words = [w for w in words if len(w) > 4]   # ['apple', 'banana']
```

## Changing Items While Filtering
```python
names = ["ann", "bob", "cy"]
shout = [n.upper() for n in names]                # ['ANN', 'BOB', 'CY']
labels = ["even" if x % 2 == 0 else "odd" for x in range(4)]
```
Careful with position: a filter `if` goes at the **end**; an `if/else` that *chooses a value* goes at the **front**.

## Nested Loops
The loops read in the same order you'd write them:
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Dictionary and Set Comprehensions
```python
squares_dict = {x: x ** 2 for x in range(5)}   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
unique_lengths = {len(w) for w in ["a", "bb", "cc"]}   # {1, 2}
```
Same idea, but with `{key: value ...}` or `{item ...}`.

## When NOT to use one
If it needs more than one condition and a long expression, a normal loop is easier to read. Clear beats clever.

## Key terms
- **comprehension**: a compact way to build a collection from another.
- **iterable**: anything you can loop over.
- **expression**: the part that produces each new item.
- **filter**: the `if` that decides which items to keep.

## Watch out
- Forgetting the square brackets gives a *generator*, not a list.
- `[x for x in data if x]` quietly drops `0` and empty values (they're falsy).
- Don't use a comprehension just for side effects like `print`; use a normal loop.
- **Remember:** a comprehension makes a **new** list; the original is unchanged.

## Today's Task
Build a list of squares with a list comprehension.
