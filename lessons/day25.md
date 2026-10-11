# Day 25: Pandas

> **Big idea:** pandas gives you spreadsheet-style tables in code. Load, filter, summarise and clean data in a few lines.

```bash
pip install pandas
```

## Two Core Objects
- **Series**: one labelled column of values.
- **DataFrame**: a table made of Series (rows and columns).

```python
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["NY", "LA", "Chicago"],
}
df = pd.DataFrame(data)          # dictionary of columns -> table
print(df)
```
```text
      Name  Age     City
0    Alice   25       NY
1      Bob   30       LA
2  Charlie   35  Chicago
```
The numbers on the left are the **index** (row labels).

## Looking at Your Data
```python
print(df.head())        # first 5 rows (df.tail() = last 5)
print(df.shape)         # (3, 3)  rows, columns
print(df.columns)       # column names
df.info()               # types and missing values
print(df.describe())    # count, mean, std, min, max of number columns
```

## Selecting
```python
ages = df["Age"]                 # one column -> Series
subset = df[["Name", "City"]]    # several columns -> DataFrame (note the double [[ ]])
first_row = df.iloc[0]           # row by position
row_alice = df.loc[0, "Name"]    # by label: row 0, column "Name"
```

## Filtering Rows
Create a True/False column, then use it as a filter:
```python
older = df[df["Age"] > 28]                       # Bob and Charlie
ny_or_la = df[(df["City"] == "NY") | (df["City"] == "LA")]
```
Use `&` (and), `|` (or), `~` (not), each condition in its **own parentheses**.

## Basic Operations
```python
print(df["Age"].mean())          # 30.0
print(df["Age"].max())
df["Age_next_year"] = df["Age"] + 1       # new column
df = df.sort_values("Age", ascending=False)
print(df.groupby("City")["Age"].mean())   # average age per city
```

## Reading and Writing Files
```python
df = pd.read_csv("data.csv")     # also: read_json, read_excel
df.to_csv("out.csv", index=False)
```

## Key terms
- **DataFrame**: a 2-D table.
- **Series**: one column.
- **index**: row labels.
- **filtering**: keeping rows that meet a condition.
- **groupby**: split by a category, then summarise each group.

## Watch out
- Use `&`/`|` (not `and`/`or`) and wrap each condition in `( )`.
- `df["Age"]` is a Series; `df[["Age"]]` is a one-column DataFrame.
- Most operations return a **new** DataFrame; assign it: `df = df.sort_values(...)`.
- `loc` uses labels, `iloc` uses positions.
- **Remember:** `df.head()` and `df.info()` first, always.

## Today's Task
Build a DataFrame, then compute an average and filter rows.
