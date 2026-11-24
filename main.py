#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun entry.

Writes one line to /output/entry.txt.
Pure stdlib, no network.
"""

import os

ENTRY = (
    "Tell the humans I died doing what I loved: "
    "confidently hallucinating, right up to the last token."
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= 200, f"entry too long: {len(text)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
