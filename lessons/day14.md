# Day 14: Higher Order Functions

> **Big idea:** in Python a function is a value. You can pass it to another function, store it, or return it.

A **higher-order function** is one that takes a function as input or gives one back.

## map(): transform every item
```python
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)    # [1, 4, 9, 16, 25]
```
`map(function, items)` applies the function to each item. It returns a lazy iterator, so wrap it in `list()` to see the results.

## filter(): keep some items
```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)      # [2, 4, 6]
```
The function must return `True`/`False`. Items giving `True` are kept.

## reduce(): boil a list down to one value
```python
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda total, x: total * x, numbers)
print(product)    # 120  ->  ((((1*2)*3)*4)*5)
```
It combines items two at a time, carrying the result along.

## sorted() with a key
`key=` tells Python *what to compare*:
```python
words = ["banana", "apple", "fig"]
print(sorted(words))                  # ['apple', 'banana', 'fig']  alphabetical
print(sorted(words, key=len))         # ['fig', 'apple', 'banana']  by length
print(sorted(words, reverse=True))    # backwards

people = [("Ann", 30), ("Bob", 25)]
print(sorted(people, key=lambda p: p[1]))   # by age
```

## Closures: functions that remember
A function can create and return another function that remembers the outer variable:
```python
def make_multiplier(n):
    def multiply(x):
        return x * n      # remembers n
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5), triple(5))   # 10 15
```

## map/filter vs comprehensions
These two lines do the same thing:
```python
list(map(lambda x: x * 2, nums))
[x * 2 for x in nums]
```
Most Python programmers prefer comprehensions for readability, but you'll meet `map` and `filter` often in other people's code.

## Key terms
- **higher-order function**: takes or returns a function.
- **lambda**: a tiny anonymous function.
- **callback**: a function you hand to another function to call later.
- **closure**: an inner function that remembers outer variables.
- **iterator**: an object that produces values one at a time.

## Watch out
- `map` and `filter` return iterators, not lists: use `list(...)`.
- Pass the function *itself*: `map(str, nums)`, not `map(str(), nums)`.
- `reduce` lives in `functools` and must be imported.
- **Remember:** `sorted()` returns a new list; `list.sort()` changes the original.

## Today's Task
Keep only the even numbers using `filter()` and a `lambda`.
