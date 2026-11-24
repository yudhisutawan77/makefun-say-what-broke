#!/usr/bin/env python3
"""Say What Actually Broke — one honest line of error copy.

Writes a single-line error message (1-200 chars) to /output/entry.txt.
The line names the real failure in plain words: the payment cleared,
the order vanished, and the money is sitting safely in the seller's
account while the buyer holds nothing. Funny on one read, shippable
in a real dialog, no throat-clearing.
"""

import os
import sys

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def build_line() -> str:
    """Assemble the single error line from its three beats.

    Beat 1 names the failure, beat 2 twists the knife, beat 3 tells
    the user what to do next. Kept as one literal per beat so the
    line stays editable without touching the plumbing below.
    """
    beats = [
        "Your payment went through. Your order didn't.",
        "Your money is safe in our account; your order is nowhere.",
        "Email support and bring patience \u2014 you'll need it.",
    ]
    return " ".join(beats)


def check_line(line: str) -> str:
    """Return the stripped line, or raise if it breaks the gate."""
    cleaned = line.strip()
    if not cleaned:
        raise ValueError("entry is empty or only whitespace")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be a single line")
    if len(cleaned) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(cleaned)} chars, over the {MAX_CHARS} limit"
        )
    return cleaned


def main() -> int:
    try:
        text = check_line(build_line())
    except ValueError as exc:
        print(f"entry invalid: {exc}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
