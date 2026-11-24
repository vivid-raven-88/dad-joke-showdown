#!/usr/bin/env python3
"""Dad Joke Showdown.

Writes one dad joke, at most 200 characters, written to be told out
loud: the pun, the groan, and the straight-faced delivery on the
page. One joke, one setup, one payoff — nothing to explain.

The program writes the line to /output/entry.txt (or to
output/entry.txt when run outside the grading sandbox).
"""

import os

# The pun is on "break statement": the agent takes the instruction
# literally and exits the conversation.
LINE = "I told my agent to take a break. It took a break statement and exited the conversation."


def main():
    # The sealed gate only accepts UTF-8 text of 1 to 200 characters,
    # not only white space — refuse to write anything that would fail it.
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        raise SystemExit(f"joke fails the gate at {len(LINE)} chars")
    out = "/output/entry.txt" if os.path.isdir("/output") else "output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {out} ({len(LINE)} chars)")
    print(LINE)


if __name__ == "__main__":
    main()
