#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line.

Writes one sentence about a small everyday moment of wonder to
/output/entry.txt. Stdlib only, no network, deterministic.
"""

import os

ENTRY = (
    "The lift mirror catches me mid-yawn, and for a second I am a stranger "
    "borrowing my own face for the ride down."
)


def main() -> None:
    # Guard the gate before writing: one sentence, 1-200 chars, not blank.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert text.count(".") == 1 and text.endswith("."), "must be one sentence"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
