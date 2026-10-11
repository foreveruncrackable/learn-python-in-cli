# Day 29: Building APIs

> **Big idea:** yesterday you *used* an API; today you *build* one with Flask. Each endpoint is a route that returns JSON.

## A Tiny CRUD API
```python
from flask import Flask, jsonify, request

app = Flask(__name__)
users = []                                   # our "database" (just a list)

@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify(users)                    # list -> JSON response

@app.route("/api/users", methods=["POST"])
def create_user():
    user = request.get_json()                # read the JSON body
    users.append(user)
    return jsonify(user), 201                # 201 = created

@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    if 0 <= user_id < len(users):
        return jsonify(users[user_id])
    return jsonify({"error": "not found"}), 404
```
- `jsonify(data)` turns Python data into a JSON response.
- `return jsonify(...), 201` sends the **data and a status code**.
- `request.get_json()` reads the data the client sent.

## Endpoint Design
Name by the *thing*, and let the method give the verb:
- `GET /api/users` → list users
- `POST /api/users` → create one
- `GET /api/users/3` → get user 3
- `PUT /api/users/3` → update user 3
- `DELETE /api/users/3` → delete user 3

## Return Proper Status Codes
- `200` OK · `201` created · `204` deleted (no content)
- `400` the client sent bad data · `404` not found

## Validate Input
```python
@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json(silent=True) or {}
    if "name" not in data:
        return jsonify({"error": "name is required"}), 400
    users.append(data)
    return jsonify(data), 201
```
Never trust incoming data. Check it first.

## Testing Without a Browser
```python
client = app.test_client()
response = client.post("/api/users", json={"name": "Ada"})
print(response.status_code, response.get_json())   # 201 {'name': 'Ada'}
```
Or use `curl`: `curl -X POST -H "Content-Type: application/json" -d '{"name":"Ada"}' http://127.0.0.1:5000/api/users`.

## Documentation
An API is only useful if people know how to call it. Document each endpoint: method, URL, what to send, what comes back. Tools like Swagger/OpenAPI can generate this for you.

## Key terms
- **endpoint**: a URL + method the API offers.
- **CRUD**: Create, Read, Update, Delete.
- **JSON body**: data sent inside the request.
- **validation**: checking input before using it.
- **status code**: tells the client how it went.

## Watch out
- Methods must be listed: `methods=["POST"]`, or you get `405 Method Not Allowed`.
- Our list resets when the server restarts. Real apps use a database (Day 27).
- `request.get_json()` fails if the client forgot the JSON header.
- **Remember:** return the right status code, not always 200.

## Today's Task
Finish a tiny REST API (a POST endpoint and a GET-one endpoint).
