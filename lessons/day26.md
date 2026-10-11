# Day 26: Python Web (Flask)

> **Big idea:** a web app listens for URLs. Each URL (a **route**) is connected to a Python function that builds the reply.

```bash
pip install flask
```

## A Minimal App
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")                  # when someone visits "/", run home()
def home():
    return "Hello, World!"       # what the browser receives

@app.route("/about")
def about():
    return "About Page"

if __name__ == "__main__":
    app.run(debug=True)          # start the dev server
```
Run it (`python app.py`) and open http://127.0.0.1:5000.
- `@app.route(...)` is a **decorator**: it attaches the function below it to a URL.
- `debug=True` reloads on every change and shows detailed errors (development only!).

## URL Parameters
```python
@app.route("/user/<username>")
def show_user(username):
    return f"User: {username}"

@app.route("/post/<int:post_id>")     # <int:...> converts to a number
def show_post(post_id):
    return f"Post number {post_id}"
```
Visiting `/user/ada` returns `User: ada`.

## Templates: HTML with blanks
Put HTML files in a folder named `templates/`.
```python
from flask import render_template

@app.route("/")
def home():
    return render_template("index.html", name="Alice")
```
```html
<!-- templates/index.html -->
<h1>Hello, {{ name }}!</h1>
{% for fruit in fruits %}
  <li>{{ fruit }}</li>
{% endfor %}
```
`{{ ... }}` shows a value; `{% ... %}` runs logic (loops, ifs).

## Forms (GET vs POST)
```python
from flask import request

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]      # the submitted field
        return f"Welcome, {name}"
    return render_template("login.html") # GET shows the form
```
**GET** asks for a page; **POST** sends data to the server.

## Deployment (the idea)
`app.run()` is only for development. For real users you host the app on a server or a platform (Render, Railway, PythonAnywhere...) behind a production server such as **gunicorn**, with `debug` off.

## Key terms
- **route**: a URL path connected to a function.
- **decorator**: `@something` above a function that changes its behaviour.
- **template**: an HTML file with placeholders.
- **request / response**: what the browser sends / what the server returns.
- **GET / POST**: read vs. send data.

## Watch out
- `404 Not Found` → the URL doesn't match any route.
- `TemplateNotFound` → the file isn't inside a `templates/` folder.
- Every route function must **return** something.
- Never run `debug=True` on a public server.
- **Remember:** URL → route → function → response.

## Today's Task
Add routes to a Flask app (one with a URL parameter).
