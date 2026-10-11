# Day 5: Lists

> **Big idea:** a list holds many values in order, and you can change it whenever you like.

## Four Collection Types (preview)
- **List** `[ ]`: ordered, changeable, allows duplicates ← today
- **Tuple** `( )`: ordered, *not* changeable (Day 6)
- **Set** `{ }`: unordered, unique items (Day 7)
- **Dictionary** `{k: v}`: key → value pairs (Day 8)

## Creating Lists
```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]   # types can be mixed
empty = []
print(len(fruits))                 # 3
```

## Accessing & Slicing
Same idea as strings: index from 0, negatives from the end, slice stop excluded.
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])     # apple
print(fruits[-1])    # cherry
print(fruits[0:2])   # ['apple', 'banana']   (a new list)
print(fruits[::-1])  # ['cherry', 'banana', 'apple']
```
Unpacking assigns each item to a variable: `a, b, c = fruits`.

## Changing a List
```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"      # replace by index
fruits.append("date")        # add to the END
fruits.insert(1, "orange")   # add at position 1
fruits.extend(["fig", "kiwi"])  # add several items
```
`append([1, 2])` adds the list as *one* item; `extend([1, 2])` adds *each* item.

## Removing Items
```python
fruits = ["apple", "banana", "cherry", "date"]
fruits.remove("banana")   # remove by VALUE
last = fruits.pop()       # remove and return the LAST item
fruits.pop(0)             # remove by INDEX
del fruits[0]             # also by index
fruits.clear()            # remove everything
```

## Searching, Counting, Sorting
```python
nums = [3, 1, 2, 3]
print(3 in nums)          # True
print(nums.index(2))      # 2   position of first match
print(nums.count(3))      # 2
nums.sort()               # sorts IN PLACE -> [1, 2, 3, 3]
nums.reverse()            # reverses IN PLACE
print(sorted(nums))       # returns a NEW sorted list, original untouched
print(sum(nums), min(nums), max(nums))
```

## Copying and Joining
```python
a = [1, 2, 3]
b = a            # NOT a copy: both names point to the SAME list!
b.append(4)
print(a)         # [1, 2, 3, 4]

c = a.copy()     # a real copy (or a[:] or list(a))
print(a + [5, 6])  # [1, 2, 3, 4, 5, 6]  joining makes a new list
```

## Key terms
- **list**: an ordered, changeable collection.
- **item / element**: one value in a list.
- **index**: an item's position (starts at 0).
- **mutable**: can be changed after creation.
- **in place**: changes the original instead of returning a new one.

## Watch out
- `IndexError: list index out of range`: the list is shorter than you think. Last valid index is `len(x) - 1`.
- `.sort()` and `.append()` **return `None`**. `x = x.sort()` wipes your list! Just call `x.sort()`.
- `b = a` doesn't copy. Use `a.copy()`.
- `.remove(x)` raises an error if `x` isn't there: check with `in` first.
- **Remember:** to total a list in your head, loop with an accumulator: `total += n`.

## Today's Task
Add up a list of numbers with a `for` loop.
