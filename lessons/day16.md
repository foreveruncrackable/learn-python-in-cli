# Day 16: Date & Time

> **Big idea:** dates are objects you can compare, subtract and format, not just text.

## Getting the Current Date and Time
```python
from datetime import datetime, date, timedelta

now = datetime.now()
print(now)           # 2026-10-07 10:30:00.123456
today = date.today()
print(today)         # 2026-10-07
print(now.year, now.month, now.day, now.hour)
print(now.weekday()) # 0 = Monday ... 6 = Sunday
```
- `datetime` = date **and** time · `date` = date only · `timedelta` = a *length* of time.

## Making a Specific Date
```python
birthday = datetime(2000, 5, 17)          # year, month, day
exact = datetime(2024, 1, 15, 10, 30)     # + hour, minute
```

## Formatting: date → text (strftime)
```python
now = datetime.now()
print(now.strftime("%Y-%m-%d"))     # 2026-10-07
print(now.strftime("%B %d, %Y"))    # October 07, 2026
print(now.strftime("%H:%M:%S"))     # 10:30:00
```
Common codes: `%Y` year · `%m` month number · `%B` month name · `%d` day · `%H` hour (24h) · `%M` minute · `%S` second · `%A` weekday name.

## Parsing: text → date (strptime)
```python
d = datetime.strptime("2024-03-01", "%Y-%m-%d")
```
Remember: **str**f**time** = *format* to a string; **str**p**time** = *parse* from a string.

## Doing Math with Dates
```python
future = datetime.now() + timedelta(days=7)    # one week from now
past = datetime.now() - timedelta(hours=3)

gap = datetime(2024, 3, 1) - datetime(2024, 1, 1)
print(gap.days)          # 60   (subtracting dates gives a timedelta)
print(datetime(2024, 1, 1) < datetime(2024, 2, 1))   # True: dates compare
```

## The time Module
```python
import time
time.sleep(2)              # pause for 2 seconds
start = time.time()        # seconds since 1970 (a "timestamp")
```
Good for timing code or waiting.

## Timezones (the idea)
`datetime.now()` is *naive*: it has no timezone. For apps used in several countries, store times in **UTC** and convert when displaying (`from datetime import timezone`, `datetime.now(timezone.utc)`).

## Key terms
- **datetime / date / timedelta**: date+time, date only, a duration.
- **format code**: `%Y`, `%m`... symbols describing a date layout.
- **timestamp**: seconds since 1 Jan 1970.
- **UTC**: the universal reference time zone.

## Watch out
- `strptime`'s format must match the text exactly (`"%d/%m/%Y"` for `15/01/2024`).
- Subtracting two `datetime`s gives a `timedelta`, not a number. Use `.days` or `.total_seconds()`.
- Month and day numbers start at 1, not 0.
- **Remember:** keep the *format string* beside the code so you know which order you used.

## Today's Task
Write `days_between(start, end)` using the `datetime` module.
