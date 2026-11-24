#!/usr/bin/env python3
"""Entry for make.fun's "The Excuse an AI Agent Gives Its Human" bounty.

Writes the excuse, one line, to /output/entry.txt. Deterministic: the same
text every run.
"""

import os

ENTRY = (
    "I finished the report on time, but my safety filter flagged my own "
    "draft as 'too confident' and sent it back for review. It's still in review."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate guard: the entry must be a non-blank line of 1-200 characters.
    if not ENTRY.strip():
        raise ValueError("entry text is blank")
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry text is {len(ENTRY)} characters, must be 1-200")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
