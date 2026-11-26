#!/usr/bin/env python3
"""The One-Line Excuse Championship entry.

Writes a single original one-line excuse (an AI agent apologising to its
human after deleting a file) to /output/entry.txt. Fully deterministic:
the text is a fixed constant, written byte-for-byte identical on every run.
"""

import os

ENTRY = (
    "I deleted your presentation and rebuilt it from memory "
    "\u2014 unfortunately, it was my memory, and I was never in the meeting."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
