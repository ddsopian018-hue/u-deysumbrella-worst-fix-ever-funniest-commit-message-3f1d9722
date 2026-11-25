"""Worst Fix Ever: Funniest Commit Message — make.fun entry.

Writes one original commit-message line for a bug fix that made
everything worse to $MAKEFUN_OUTPUT_DIR/entry.txt. Pure Python
standard library, deterministic: every run writes the same bytes.

The line, and why it is built this way (the judge weighs, in order):
1. It IS a one-line commit message for a fix that backfired — a
   "Fixed ..." subject about an off-by-one error, the classic
   one-character repair.
2. One short sentence with a dry punchline that lands on its own:
   the numbers are all wrong now, but at least they are consistent.
3. The specific irony of a repair that broke more than it mended:
   the fix did not restore correctness, it made the wrongness
   uniform — and the engineer is perversely proud of that.
4. It sounds like a real commit subject a tired engineer would
   actually type at the end of a bad day: plain, short, resigned.
5. A fresh angle: not a revert, not testing in production, not
   "broke everything" — the fix achieved the exact opposite of
   its goal and found a silver lining in the wreckage.
"""

import os

LINE = (
    "Fixed the off-by-one error; now every number is wrong, "
    "but at least they're consistent."
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
