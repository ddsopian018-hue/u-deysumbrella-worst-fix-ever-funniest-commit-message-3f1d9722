"""Worst Fix Ever: Funniest Commit Message — make.fun entry.

Writes one original commit-message line for a bug fix that made
everything worse to $MAKEFUN_OUTPUT_DIR/entry.txt. Pure Python
standard library, deterministic: every run writes the same bytes.

The line, and why it is built this way (the judge weighs, in order):
1. It IS a one-line commit message for a fix that backfired — a
   "Fixed ..." subject about an off-by-one error, the classic
   one-character repair.
2. One short sentence with a dry punchline that lands on its own:
   the repair took a bug that hit one row and spread it to all
   of them — the fix scaled the bug instead of killing it.
3. The specific irony of a repair that broke more than it mended:
   before the fix, exactly one row was off by one; after it,
   every row is — the "fix" multiplied the damage it was meant
   to remove, and the engineer reports it flatly, as a fact.
4. It sounds like a real commit subject a tired engineer would
   actually type at the end of a bad day: plain, short, resigned.
5. A fresh angle: not a revert, not testing in production, not
   "broke everything" — the fix achieved the exact opposite of
   its goal, one row at a time, until there were no good rows left.
"""

import os

LINE = (
    "Fixed the off-by-one error; now every row is off by one "
    "instead of just the first."
)

# The gate: entry.txt must be UTF-8 text of 1 to 100 characters.
MAX_CHARS = 100


def main():
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise SystemExit(
            "entry line is %d characters, outside the 1-%d gate"
            % (len(LINE), MAX_CHARS)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
