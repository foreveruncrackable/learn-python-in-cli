# Day 24: Statistics

> **Big idea:** statistics boil many numbers down to a few that describe them: the typical value and how spread out they are.

## The statistics Module
```python
import statistics

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(statistics.mean(data))      # 5.5
print(statistics.median(data))    # 5.5
print(statistics.mode([1, 2, 2, 3]))  # 2
print(statistics.stdev(data))     # 3.027...
print(statistics.variance(data))  # 9.166...
```

## What Each Measure Tells You
- **Mean**: the average. Add everything, divide by the count.
- **Median**: the middle value once sorted. (With an even count, the average of the two middle values.) It isn't thrown off by extreme values.
- **Mode**: the value that appears most often.
- **Range**: `max(data) - min(data)`, the full spread.
- **Variance**: the average squared distance from the mean.
- **Standard deviation**: the square root of the variance. In the same units as your data, so it's easier to read. **Small = values are close together; large = spread out.**

## Mean vs Median
```python
salaries = [30, 32, 35, 36, 400]
print(statistics.mean(salaries))    # 106.6   dragged up by the 400
print(statistics.median(salaries))  # 35      a better "typical" value
```
When data has outliers (extreme values), the median is more honest.

## Sample vs Population
`stdev` / `variance` are for a **sample** (part of the data). If your list is the **entire** population use `pstdev` / `pvariance`.

## Formatting the Output
```python
print(f"Mean: {statistics.mean(data):.2f}")   # 2 decimals
```

## Key terms
- **mean / median / mode**: three kinds of "typical".
- **variance / standard deviation**: how spread out the data is.
- **outlier**: an unusually large or small value.
- **sample / population**: part of the data / all of it.
- **dataset**: a collection of values you analyse.

## Watch out
- `median` and `stdev` need numbers; an empty list raises `StatisticsError`.
- `stdev` needs at least **two** values.
- Convert text input first: `[float(x) for x in text.split()]`.
- **Remember:** average ≠ typical when outliers exist; check both mean and median.

## Today's Task
Print the mean, median and standard deviation of a dataset.
