# Day 28: APIs

> **Big idea:** an API is a menu a program offers to other programs: you send a request, it sends back data.

## What Is an API?
An **API** (Application Programming Interface) lets two programs talk. Most web APIs follow **REST**: you use a URL plus an HTTP **method** to say what to do.

- **GET**: read data
- **POST**: create data
- **PUT / PATCH**: update data
- **DELETE**: remove data

Servers answer with a **status code**:
- `200` OK · `201` created
- `400` bad request · `401` not logged in · `404` not found
- `500` server error

## GET Requests
```python
import requests

response = requests.get("https://api.github.com/users/octocat")
print(response.status_code)     # 200
data = response.json()          # JSON text -> Python dictionary
print(data["name"])
```

## Parameters
```python
response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "python", "sort": "stars"},    # becomes ?q=python&sort=stars
)
print(response.url)
```
Let `requests` build the query string; it handles spaces and special characters for you.

## POST Requests
```python
response = requests.post(
    "https://httpbin.org/post",
    json={"name": "Alice", "age": 25},    # sent as JSON
)
print(response.status_code)
```

## JSON
JSON is the standard data format of APIs. It maps neatly onto Python:
- object `{ }` → dict · array `[ ]` → list · string/number → str/int/float
- `true/false/null` → `True/False/None`

## Authentication
Many APIs need to know who you are. Usually you send a secret **API key** or token in a header:
```python
headers = {"Authorization": "Bearer YOUR_TOKEN"}
response = requests.get(url, headers=headers)
```
Keep keys out of your code: read them from environment variables (`os.environ["API_KEY"]`).

## Handling Problems
```python
try:
    response = requests.get(url, timeout=5)    # always set a timeout
    response.raise_for_status()                # raises an error for 4xx/5xx
    data = response.json()
except requests.RequestException as e:
    print("Request failed:", e)
```

## Key terms
- **API**: a way for programs to talk to each other.
- **endpoint**: one URL of an API.
- **request / response**: what you send / what you get back.
- **HTTP method**: GET, POST, PUT, DELETE.
- **status code**: the result number.
- **JSON**: the data format.

## Watch out
- Check `status_code` (or `raise_for_status()`) before using `.json()`.
- Respect rate limits: too many requests get you blocked.
- Never publish API keys on GitHub.
- **Remember:** an API is just a URL that returns data instead of a web page.

## Today's Task
Build an API request URL and read a JSON response.
