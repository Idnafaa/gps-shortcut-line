#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — one-line excuse writer.

Writes a single original excuse line, in the GPS's own voice,
to /output/entry.txt (1-200 characters, plain text, one line).
"""
import os

EXCUSE = "In my defense, the satellite clearly showed a road there \u2014 it just didn't mention the road was a river."

def main():
    # Keep exactly one line: no trailing newline, no extra whitespace.
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"excuse is {len(text)} chars"
    assert "\n" not in text, "excuse must be a single line"
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {outdir}/entry.txt")

if __name__ == "__main__":
    main()
