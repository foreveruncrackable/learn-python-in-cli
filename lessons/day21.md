# Day 21: Classes & OOP

> **Big idea:** a **class** is a blueprint; an **object** is a thing built from it. Objects bundle *data* and the *actions* that use it.

## A First Class
```python
class Dog:
    def __init__(self, name, age):   # runs automatically when you create a Dog
        self.name = name             # store data on the object
        self.age = age

    def bark(self):                  # a method: a function inside a class
        return f"{self.name} says Woof!"

dog = Dog("Buddy", 3)                # create an object (an "instance")
print(dog.name)                      # Buddy
print(dog.bark())                    # Buddy says Woof!
```
- `__init__` is the **constructor**: it sets up a new object.
- `self` means "this particular object". It's always the first parameter of a method, and Python fills it in for you.
- **Attributes** (`self.name`) are the object's data. **Methods** (`bark`) are its actions.
- You can make many objects from one class: `Dog("Rex", 5)`.

## Inheritance: reuse and specialise
```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."

class Cat(Animal):                    # Cat gets everything Animal has
    def speak(self):                  # ...and overrides speak
        return f"{self.name} says Meow!"

print(Cat("Tom").speak())             # Tom says Meow!
```
`Cat` **is an** `Animal`. Use `super().__init__(...)` to run the parent's setup when you add your own `__init__`.

## Polymorphism: same call, different behaviour
```python
for animal in [Animal("x"), Cat("Tom")]:
    print(animal.speak())      # each class answers in its own way
```

## Encapsulation: protect the data
```python
class BankAccount:
    def __init__(self):
        self.__balance = 0         # double underscore = "private"

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance
```
Other code should use `deposit()` and `get_balance()` rather than touching `__balance` directly, so the rules (no negative deposits) can't be bypassed.

## Nice to Know: __str__
```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):             # what print(obj) shows
        return f"({self.x}, {self.y})"
print(Point(1, 2))                 # (1, 2)
```

## Key terms
- **class**: the blueprint.
- **object / instance**: one thing built from a class.
- **attribute**: data stored on an object.
- **method**: a function defined in a class.
- **inheritance**: a class building on another.
- **self**: the current object.

## Watch out
- Forgetting `self` in `def bark():` → `TypeError`. Methods need `self` first.
- Inside a method, use `self.name`, not just `name`.
- `Dog` is the class; `Dog("Buddy", 3)` (with parentheses) creates an object.
- **Remember:** `__init__` has **two** underscores on each side.

## Today's Task
Finish the `Dog` class with attributes and a method.
