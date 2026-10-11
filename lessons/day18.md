# Day 18: Regular Expressions

> **Big idea:** a regular expression (regex) is a tiny language for describing *patterns* in text, like "three digits, a dash, four digits".

## Using the re Module
```python
import re

text = "My email is test@example.com"
match = re.search(r"[\w.-]+@[\w.-]+\.\w+", text)
if match:                       # search returns None when nothing matches
    print(match.group())        # test@example.com
```
Write patterns as **raw strings** `r"..."` so backslashes aren't treated as escapes.

## Pattern Building Blocks
- `.` any one character (except newline)
- `\d` a digit · `\w` a letter/digit/underscore · `\s` whitespace
- `\D`, `\W`, `\S` the opposites
- `[abc]` one of a, b or c · `[a-z]` any lowercase letter · `[^0-9]` anything *except* digits
- `^` start of text · `$` end of text
- `*` zero or more · `+` one or more · `?` zero or one · `{3}` exactly three · `{2,4}` two to four
- `( )` a group · `|` or
- `\.` a literal dot (escape special characters with `\`)

Examples: `\d{3}-\d{4}` matches `555-1234` · `colou?r` matches both `color` and `colour`.

## The Main Functions
```python
re.search(r"\d+", "abc 123 def")        # first match anywhere in the text
re.match(r"\d+", "123 abc")             # must match at the START
re.fullmatch(r"\d+", "123")             # the WHOLE string must match
re.findall(r"\d+", "a1 b22 c333")       # ['1', '22', '333']  all matches
re.sub(r"\s+", " ", "too    many   spaces")   # 'too many spaces'  substitute
re.split(r"[,;]", "a,b;c")              # ['a', 'b', 'c']
```
`search`, `match` and `fullmatch` return a match object (or `None`); call `.group()` to get the text.

## Groups: pull out parts
```python
m = re.search(r"(\d{4})-(\d{2})-(\d{2})", "Date: 2024-03-15")
print(m.group(1), m.group(2), m.group(3))   # 2024 03 15
```

## Validating Input
```python
email = "alice@example.com"
if re.fullmatch(r"[\w.+-]+@[\w-]+(\.[\w-]+)+", email):
    print("Valid")
```
Use `fullmatch` for validation; otherwise `"bad@x.com!!!"` could match partially.

## Key terms
- **regex / pattern**: a description of text to find.
- **match**: a piece of text that fits the pattern.
- **raw string**: `r"..."`, backslashes kept as-is.
- **group**: a part of the pattern in parentheses.
- **quantifier**: `* + ? {n}`: how many times.

## Watch out
- Forget the `r` prefix and `\d` may break. Always use raw strings.
- `.` matches *any* character; to match a real dot, write `\.`.
- Patterns are greedy: `.*` grabs as much as it can. Use `.*?` for the shortest match.
- Regexes get unreadable fast. Build them step by step and test each piece.
- **Remember:** `search` finds anywhere; `fullmatch` checks the whole string.

## Today's Task
Validate email addresses with a regular expression.
