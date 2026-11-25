#!/usr/bin/env python3
"""One Line, Big Laugh - make.fun entry.

Writes a single funny line (at most 200 characters) to /output/entry.txt.
Pure stdlib, deterministic: the same line on every run.
"""

import os

LINE = "I asked my grandmother for her secret recipe; she whispered: 'store-bought — add butter and lie.'"


def main():
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 200
    # characters, not only white space. Enforce it here so a bad line
    # can never ship silently.
    assert 1 <= len(LINE) <= 200, len(LINE)
    assert LINE.strip(), "line must not be whitespace-only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
