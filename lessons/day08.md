# Day 8: Dictionaries

> **Big idea:** a dictionary looks things up by a **key**, like a real dictionary looks up a word to find its meaning.

## Creating Dictionaries
```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
}
print(len(person))   # 3 key-value pairs
```
- Each entry is `key: value`. Keys are usually strings or numbers and must be **unique** and **unchangeable** (no lists as keys).
- Values can be anything, even other lists or dictionaries.

## Reading Values
```python
print(person["name"])            # Alice
print(person.get("age"))         # 25
print(person.get("email"))       # None   (no error)
print(person.get("email", "n/a"))# n/a    (your own default)
print(person["email"])           # KeyError: the key doesn't exist
print("name" in person)          # True   (checks KEYS)
```
Use `[ ]` when the key must exist; use `.get()` when it might not.

## Adding, Changing, Removing
```python
person["email"] = "alice@example.com"   # new key -> adds
person["age"] = 26                      # existing key -> updates
del person["city"]                      # remove a key
removed = person.pop("email")           # remove and return the value
person.update({"age": 27, "job": "dev"})  # merge another dict in
```

## Looping
```python
person = {"name": "Alice", "age": 25}
for key in person:                 # keys by default
    print(key)
for value in person.values():
    print(value)
for key, value in person.items():  # both at once, the most useful form
    print(f"{key} = {value}")
```
`.keys()`, `.values()` and `.items()` give you views of the dictionary.

## Counting Pattern
Dictionaries are perfect for counting things:
```python
counts = {}
for word in "a b a c a".split():
    counts[word] = counts.get(word, 0) + 1   # start at 0 if new
print(counts)   # {'a': 3, 'b': 1, 'c': 1}
```
Read it as: "the count for this word = (old count, or 0 if none) + 1".

## Nested Dictionaries
```python
users = {
    "ann": {"age": 30, "langs": ["python", "sql"]},
    "bob": {"age": 25, "langs": ["js"]},
}
print(users["ann"]["langs"][0])   # python
```
Chain `[ ]` to go one level deeper each time.

## Key terms
- **dictionary (dict)**: a collection of key → value pairs.
- **key**: the label you look up by.
- **value**: the data stored under a key.
- **item**: one key-value pair.
- **nested**: a structure inside another structure.

## Watch out
- `KeyError` means that key isn't there. Check with `in` or use `.get()`.
- Assigning to a new key *adds* it. A typo in the key silently creates a new entry.
- `for x in d` gives **keys**, not values.
- Keys are case-sensitive: `"Name"` ≠ `"name"`.
- **Remember:** dict = fast lookup by name; list = fast lookup by position.

## Today's Task
Count how often each word appears in a sentence.
