#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes — make.fun bounty entry.

Writes one one-line joke about office life to /output/entry.txt.
Deterministic: the same line every run, no input, no network, no randomness.
The line is a genuine office joke with its turn at the end: a "quick sync"
that arrives with a 47-slide deck, a pre-read and a follow-up, so the only
quick part left is how fast the narrator ages.
"""

import os

LINE = (
    "Our 'quick sync' has a 47-slide deck, a pre-read, and a follow-up "
    "\u2014 the only quick part is how fast I age."
)


def main() -> None:
    # The gate requires 1-199 characters, not only whitespace.
    assert 1 <= len(LINE) <= 199, "line must be 1-199 characters"
    assert LINE.strip() == LINE and LINE.strip(), "line must be non-blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
