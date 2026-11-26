#!/usr/bin/env python3
# Entry for make.fun bounty u-eager-stork-81-9647-the-printer-apology-60229153
"""The Printer Apology.

Deterministic entry: writes exactly one line to /output/entry.txt
and prints that same line, nothing else.
"""

import os

LINE = "I am sorry I jammed on page 47. Cheap paper, staples, your 2 a.m. deadline — I snapped, and honestly, no regrets."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
