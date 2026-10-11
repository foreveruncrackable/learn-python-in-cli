#!/usr/bin/env python3
"""30 Days of Python - interactive CLI learning app.

Run:  python main.py            (menu)
      python main.py --day 5    (jump to a day)
      python main.py --list     (see your progress)
"""

import sys

from pydays.app import main

if __name__ == "__main__":
    sys.exit(main())
