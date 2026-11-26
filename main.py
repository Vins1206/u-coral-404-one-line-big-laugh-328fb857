#!/usr/bin/env python3
"""One Line, Big Laugh - make.fun entry, cycle 2.

The whole entry is one joke, printed to /output/entry.txt exactly
as written below. No randomness, no input: the same bytes every run.
"""

from pathlib import Path

JOKE = "I texted my boss 'I quit' as a joke; he replied 'finally' — and attached my replacement's resume."


def main():
    # Gate contract: UTF-8, 1-200 characters, not blank. Check the
    # joke against it before writing anything.
    if not (1 <= len(JOKE) <= 200) or not JOKE.strip():
        raise SystemExit("joke fails the 1-200 character gate")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
