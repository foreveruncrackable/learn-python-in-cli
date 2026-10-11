# Day 10: Loops

> **Big idea:** a loop repeats code so you don't have to copy and paste it.

## for Loop: "for each item"
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:      # fruit takes each value in turn
    print(fruit)
```
Works on lists, strings, tuples, sets, dict keys and more. The loop variable (`fruit`) is a name you choose.

## range(): repeat N times
```python
for i in range(5):          # 0, 1, 2, 3, 4   (stops BEFORE 5)
    print(i)
for i in range(1, 6):       # 1 to 5
    print(i)
for i in range(0, 10, 2):   # 0, 2, 4, 6, 8   (step of 2)
    print(i)
```
`range(start, stop, step)`: `stop` is never included.

## while Loop: "as long as"
```python
count = 0
while count < 5:      # checked before every round
    print(count)
    count += 1        # without this the loop never ends!
```
Use `for` when you know what to loop over; use `while` when you loop until something changes.

## Accumulator Pattern
Build a result step by step:
```python
total = 0
for n in [4, 8, 15]:
    total += n         # add each item
print(total)           # 27
```

## break and continue
```python
for i in range(10):
    if i == 5:
        break          # leave the loop completely
    if i % 2 == 0:
        continue       # skip to the next round
    print(i)           # prints 1, 3
```

## Nested Loops
A loop inside a loop: the inner one finishes fully for every step of the outer one.
```python
for row in range(1, 4):
    for col in range(1, 4):
        print(row * col, end=" ")   # end=" " keeps output on one line
    print()                         # new line after each row
```

## enumerate and zip
```python
fruits = ["apple", "banana"]
for index, fruit in enumerate(fruits):   # index AND item
    print(index, fruit)                  # 0 apple / 1 banana

names = ["Alice", "Bob"]
ages = [25, 30]
for name, age in zip(names, ages):       # walk two lists together
    print(name, age)
```

## Key terms
- **iteration**: one round of a loop.
- **iterable**: anything you can loop over (list, string, range...).
- **loop variable**: the name holding the current item.
- **infinite loop**: a loop whose condition never becomes False (stop with Ctrl+C).
- **accumulator**: a variable that collects a running result.

## Watch out
- Forgetting to change the variable in a `while` loop → infinite loop.
- `range(5)` gives 0-4, not 1-5.
- Don't add/remove items from a list while looping over it; loop over a copy instead.
- Indentation decides what's inside the loop and what runs after it.
- **Remember:** `break` leaves the loop, `continue` skips one round.

## Today's Task
Print the multiplication table for a number.
