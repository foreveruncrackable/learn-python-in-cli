# Day 20: Package Management

> **Big idea:** you don't have to write everything yourself. **pip** downloads code other people shared.

## Packages and pip
- A **package** is a bundle of modules someone published (e.g. `requests`, `pandas`).
- **pip** is Python's installer. Packages come from **PyPI** (pypi.org), the public package store.

```bash
pip install requests            # install the latest version
pip install requests==2.28.0    # a specific version
pip install --upgrade requests  # update
pip uninstall requests          # remove
pip list                        # what's installed
pip show requests               # details about one package
```
If `pip` isn't found, use `python -m pip install requests`; it uses the same Python you run.

## Using what you installed
```python
import requests
response = requests.get("https://api.github.com")
print(response.status_code)   # 200
```

## requirements.txt: a shopping list
A text file listing the packages a project needs:
```text
requests==2.28.0
pandas>=1.5.0
```
```bash
pip freeze > requirements.txt     # save what's installed right now
pip install -r requirements.txt   # install everything listed
```
Anyone can then recreate your setup with one command.

## Why Versions Matter
Packages change. `==` pins an exact version (safe, reproducible); `>=` allows newer ones (flexible). Different projects may need *different* versions of the same package, which is why we use virtual environments (Day 23).

## Beyond pip
- **venv**: a private set of packages per project (Day 23).
- **Poetry / pipenv**: tools that handle packages *and* environments for you.

## Key terms
- **package**: shared, installable code.
- **PyPI**: the online package index.
- **dependency**: a package your project needs.
- **version pin**: fixing an exact version with `==`.
- **requirements.txt**: the list of dependencies.

## Watch out
- Install packages inside a virtual environment, not globally.
- The install name can differ from the import name: `pip install beautifulsoup4` → `import bs4`.
- `ModuleNotFoundError` after installing usually means pip and python are different installs. Use `python -m pip`.
- **Remember:** commit `requirements.txt`, not the `venv` folder.

## Today's Task
Write `is_installed(name)` to check whether a package can be imported.
