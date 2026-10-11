# Day 7: Sets

> **Big idea:** a set is a bag of *unique* items. Add the same thing twice and it's still there only once.

## Creating Sets
```python
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)      # {1, 2, 3}   duplicates vanish
empty = set()       # {} would create an empty DICTIONARY, not a set
print(len(fruits))  # 3
```
Sets have **no order and no index**: `fruits[0]` is an error. You loop over them or test membership.

## Why use a set?
```python
names = ["Ann", "Bob", "Ann", "Cy"]
unique = list(set(names))        # remove duplicates (order not kept)
print("Bob" in set(names))       # True: very fast membership test
```

## Adding & Removing
```python
s = {1, 2, 3}
s.add(4)              # add one item
s.update([5, 6])      # add many items
s.remove(2)           # error if 2 is missing
s.discard(99)         # no error if missing
x = s.pop()           # removes an ARBITRARY item
s.clear()             # empty it
```

## Set Math
The big reason sets exist:
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)   # {1, 2, 3, 4, 5, 6}  union: everything in either
print(a & b)   # {3, 4}              intersection: in both
print(a - b)   # {1, 2}              difference: in a but not b
print(a ^ b)   # {1, 2, 5, 6}        symmetric difference: in one, not both
print({1, 2} <= a)   # True   subset
```
Named versions: `a.union(b)`, `a.intersection(b)`, `a.difference(b)`, `a.issubset(b)`.

## Key terms
- **set**: an unordered collection of unique items.
- **union / intersection / difference**: combine, overlap, subtract.
- **hashable**: an item type a set can hold (numbers, strings, tuples).
- **membership test**: `x in s`.

## Watch out
- `{}` is an empty **dict**. Use `set()`.
- Sets can't hold lists or other sets (they're changeable): `{[1, 2]}` is a `TypeError`.
- The printed order of a set may differ from what you typed. Use `sorted(s)` if you need order.
- **Remember:** use a set when you care about *what's there*, not *where* it is.

## Today's Task
Print the union, intersection and difference of two sets.
