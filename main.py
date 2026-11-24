"""make.fun entry: Seventeen Syllables of Debugging.

Writes the 5-7-5 haiku about debugging to /output/entry.txt.
Stdlib only.

Brief: three lines in the 5-7-5 syllable shape, at most 200 characters.
Syllables: Cursor(2) blinks(1) at(1) three(1) = 5;
a(1) thousand(2) logs(1) no(1) answer(2) = 7;
one(1) missing(2) comma(2) = 5.
"""

import os
import sys

ENTRY = "Cursor blinks at three\na thousand logs, no answer\none missing comma"

MAX_CHARS = 200


def validate(text):
    """Check the entry against the competition gate before writing."""
    if not text or not text.strip():
        sys.exit("entry must not be blank")
    if len(text) > MAX_CHARS:
        sys.exit("entry is %d chars, over the %d limit" % (len(text), MAX_CHARS))
    if len(text.split("\n")) != 3:
        sys.exit("haiku must be exactly three lines")


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
