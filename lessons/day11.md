# Day 11: Functions

> **Big idea:** a function is a named, reusable recipe. Write it once, use it anywhere.

## Defining and Calling
```python
def greet(name):               # def + name + (parameters) + colon
    return f"Hello, {name}!"   # the indented body

message = greet("Alice")       # call it with an argument
print(message)                 # Hello, Alice!
```
- **Define** with `def`: this only saves the recipe.
- **Call** with `name(...)`: this actually runs it.
- **Parameter** = the name in the definition (`name`). **Argument** = the value you pass in (`"Alice"`).

## return vs print
```python
def add(a, b):
    return a + b        # hands the value BACK to the caller

total = add(2, 3)       # total is 5 and you can use it
```
`print` only *shows* something on screen. `return` *gives the value back* so other code can use it. A function with no `return` gives back `None`.

## Default and Keyword Arguments
```python
def add(a, b=10):         # b is optional; defaults to 10
    return a + b

print(add(5))             # 15
print(add(5, 20))         # 25
print(add(b=1, a=2))      # 3   keyword arguments: order doesn't matter
```
Parameters with defaults must come **after** those without.

## *args and **kwargs
```python
def show(*args, **kwargs):
    print(args)      # (1, 2)            extra positional arguments, as a tuple
    print(kwargs)    # {'x': 3, 'y': 4}  extra keyword arguments, as a dict

show(1, 2, x=3, y=4)
```
Use them when you don't know how many arguments will arrive.

## Scope: where a name lives
```python
x = "global"
def demo():
    x = "local"      # a NEW variable, only inside demo
    print(x)         # local
demo()
print(x)             # global  (unchanged)
```
Variables created inside a function are **local**: they disappear when it ends. A function can *read* outer variables, but to be safe pass what you need as parameters and `return` the result.

## Lambda: tiny one-line functions
```python
square = lambda x: x ** 2
print(square(5))            # 25
print((lambda a, b: a + b)(2, 3))   # 5
```
`lambda parameters: expression`. It returns the expression automatically. Great for short throwaway functions (Day 14).

## Docstrings
```python
def area(w, h):
    """Return the area of a rectangle."""   # explains what the function does
    return w * h
```

## Key terms
- **function**: a named block of reusable code.
- **parameter / argument**: the placeholder / the real value.
- **return value**: what a function hands back.
- **scope**: the part of the program where a name exists.
- **recursion**: a function that calls itself.

## Watch out
- Forgetting the parentheses: `greet` is the function; `greet()` runs it.
- `print()` inside a function is not the same as `return`.
- Code after a `return` never runs.
- Don't use a mutable default like `def f(x=[])`; it's shared between calls.
- **Remember:** one function, one job; give it a name that says what it does.

## Today's Task
Write a `fibonacci(n)` function that returns a list.
