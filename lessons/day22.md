# Day 22: Web Scraping

> **Big idea:** a web page is just text (HTML). A scraper downloads it and picks out the parts you want.

## The Steps
1. **Download** the page with `requests`.
2. **Parse** the HTML with BeautifulSoup so you can search it.
3. **Extract** the data.

```bash
pip install requests beautifulsoup4
```

## HTML in 30 Seconds
```html
<html>
  <head><title>My Page</title></head>
  <body>
    <h1 class="main">Welcome</h1>
    <a href="/about">About</a>
  </body>
</html>
```
- A **tag** is `<name> ... </name>`.
- **Attributes** sit inside the opening tag: `href="/about"`, `class="main"`.

## Download and Parse
```python
import requests
from bs4 import BeautifulSoup

response = requests.get("https://example.com")
print(response.status_code)               # 200 = OK
soup = BeautifulSoup(response.text, "html.parser")
```

## Find Things
```python
print(soup.title.text)                       # the page title
first_link = soup.find("a")                  # first <a> tag
all_links = soup.find_all("a")               # every <a> tag (a list)

for link in all_links:
    print(link.get("href"), link.text)       # attribute and visible text

heading = soup.find("h1", class_="main")     # filter by class
items = soup.select("div.card > p")          # CSS selectors
```
`.get("href")` reads an attribute; `.text` gives the text inside the tag.

## Be a Good Scraper
- Check the site's `robots.txt` and terms of service first.
- Don't send many requests quickly: add `time.sleep(1)` between them.
- Prefer an official **API** (Day 28) when one exists.
- Don't scrape personal data or paywalled content.

## Key terms
- **HTML**: the markup language of web pages.
- **tag / attribute**: an element / its extra info.
- **parse**: turn raw text into a searchable structure.
- **scraping**: extracting data from web pages.
- **status code**: the server's answer (`200` OK, `404` not found).

## Watch out
- `find()` returns `None` if nothing matches, so check before using `.text`.
- Page layouts change; your scraper may break.
- Some content is added by JavaScript and isn't in the downloaded HTML.
- **Remember:** always check `response.status_code` before parsing.

## Today's Task
Parse an HTML page and print its title and links.
