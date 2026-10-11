# Day 23: Virtual Environments

> **Big idea:** each project gets its own private toolbox of packages, so projects can't break one another.

## The Problem
Project A needs `requests 2.20`; Project B needs `requests 2.31`. Installed globally, only one can win. A **virtual environment** is a separate folder with its own Python packages, one per project.

## Create and Use One (venv)
```bash
# 1. Create (once per project)
python -m venv myenv

# 2. Activate (every time you open a new terminal)
source myenv/bin/activate         # Linux / Mac
myenv\Scripts\activate            # Windows

# 3. Work: installs now go into myenv only
pip install requests

# 4. Leave
deactivate
```
When active, your prompt shows `(myenv)`. `pip list` then shows only that environment's packages.

## Share Your Setup
```bash
pip freeze > requirements.txt          # save the package list
pip install -r requirements.txt        # recreate it elsewhere (in a new venv)
```

## Other Tools
- **virtualenv**: the older, still-popular predecessor of `venv`.
- **pipenv / Poetry**: manage the environment *and* the package list together.

## Best Practices
- One environment per project.
- Name it `.venv` or `venv` inside the project folder.
- Add the environment folder to `.gitignore` (it can be re-created anytime).
- Keep `requirements.txt` updated and committed.

## Key terms
- **virtual environment**: an isolated Python setup for one project.
- **activate**: switch your terminal to use that environment.
- **dependency**: a package your project needs.
- **isolation**: keeping projects separate.

## Watch out
- Forgot to activate? `pip install` goes to your global Python. Look for `(myenv)` in the prompt.
- Don't copy or move a venv folder to another machine; re-create it from `requirements.txt`.
- On Windows PowerShell you may need to allow scripts to run activation.
- **Remember:** create → activate → install → freeze.

## Today's Task
Write a function that returns the commands to create and activate a virtual environment.
