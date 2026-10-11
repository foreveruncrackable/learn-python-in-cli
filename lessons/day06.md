# Day 6: Tuples

> **Big idea:** a tuple is a list you promise never to change.

## Creating Tuples
```python
coordinates = (10, 20)
colors = ("red", "green", "blue")
single = (1,)        # the COMMA makes it a tuple; (1) is just the number 1
empty = ()
print(len(colors))   # 3
```

## Accessing & Slicing
Works exactly like lists and strings:
```python
colors = ("red", "green", "blue")
print(colors[0])      # red
print(colors[-1])     # blue
print(colors[0:2])    # ('red', 'green')
print(colors.count("red"))   # 1
print(colors.index("blue"))  # 2
```
Those two methods, `count()` and `index()`, are all a tuple has, because it can't be changed.

## Immutable
```python
colors[0] = "pink"   # TypeError: 'tuple' object does not support item assignment
```
To "change" a tuple, build a new one: `colors = ("pink",) + colors[1:]`, or convert: `list(colors)`, edit, then `tuple(...)`.

## Unpacking
This is the most useful tuple trick: split a tuple into variables in one line.
```python
point = (10, 20)
x, y = point
print(x, y)          # 10 20

first, *rest = (1, 2, 3, 4)   # * collects the leftovers
print(first, rest)   # 1 [2, 3, 4]
```
The number of variables must match the number of items (unless you use `*`).

## Returning Several Values
A function can return a tuple, and you unpack it:
```python
def min_max(numbers):
    return min(numbers), max(numbers)   # a tuple

low, high = min_max([4, 1, 9])
```

## When to Use Tuples
- Data that shouldn't change: coordinates, RGB colours, dates.
- Dictionary keys (lists can't be keys, tuples can).
- Slightly faster and safer than lists for fixed data.

## Key terms
- **tuple**: an ordered, unchangeable collection.
- **immutable**: can't be modified after creation.
- **unpacking**: assigning items to separate variables.
- **packing**: grouping values into a tuple (`t = 1, 2, 3`).

## Watch out
- `("a")` is a string; `("a",)` is a tuple.
- You can't append, remove or assign to a tuple, but a *list inside* a tuple can still change.
- **Remember:** parentheses aren't what make a tuple, the commas are.

## Today's Task
Unpack a tuple into two variables.
