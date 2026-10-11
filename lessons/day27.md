# Day 27: Python with MongoDB

> **Big idea:** MongoDB stores data as flexible, JSON-like **documents**, and Python reads and writes them using plain dictionaries.

```bash
pip install pymongo
```
You also need a running MongoDB server (local, or free in the cloud with MongoDB Atlas).

## How MongoDB Is Organised
- **Database** → holds **collections**
- **Collection** → holds **documents** (like a table holding rows)
- **Document** → a dictionary, e.g. `{"name": "Alice", "age": 25}`

No fixed columns: two documents in the same collection can have different fields.

## Connecting
```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]        # created automatically on first use
users = db["users"]              # a collection
```

## CRUD: Create, Read, Update, Delete
```python
# Create
users.insert_one({"name": "Alice", "age": 25})
users.insert_many([{"name": "Bob", "age": 30}, {"name": "Cy", "age": 17}])

# Read
print(users.find_one({"name": "Alice"}))    # one document (or None)
for user in users.find({"age": {"$gte": 18}}):   # all matching
    print(user)

# Update
users.update_one({"name": "Alice"}, {"$set": {"age": 26}})   # change a field
users.update_one({"name": "Alice"}, {"$inc": {"age": 1}})    # add 1

# Delete
users.delete_one({"name": "Bob"})
```
Pattern: `operation(filter, change)`. The **filter** says *which* documents; the **update** says *what to change*.

## Query Operators
- `$gt`, `$gte`, `$lt`, `$lte`: greater / less than (or equal)
- `$ne`: not equal · `$in`: value is in a list
- `$set`: set a field · `$inc`: increase a number · `$unset`: remove a field

## Sorting, Limiting, Counting
```python
for u in users.find().sort("age", -1).limit(3):   # oldest 3 (-1 = descending)
    print(u["name"])
print(users.count_documents({"age": {"$gte": 18}}))
```

## Aggregation (summaries)
```python
result = users.aggregate([
    {"$match": {"age": {"$gte": 18}}},                       # filter
    {"$group": {"_id": None, "average": {"$avg": "$age"}}},  # summarise
])
print(list(result))
```
A pipeline passes documents through stages, like an assembly line.

## Key terms
- **document**: one record, written as a dictionary.
- **collection**: a group of documents.
- **CRUD**: Create, Read, Update, Delete.
- **filter / query**: the dictionary that selects documents.
- **`_id`**: the unique ID MongoDB adds to every document.

## Watch out
- `update_one` **without** `$set` is an error: describe the change with an operator.
- `find()` returns a cursor, so loop over it or wrap it in `list()`.
- `find_one` returns `None` when nothing matches; check before using it.
- Never put your database password in code; use environment variables.
- **Remember:** queries are just dictionaries.

## Today's Task
Write the filter and update dictionaries that MongoDB expects.
