"""Loading Screen Gold: a one-line loading-screen tip.

Writes exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure Python standard library only; no network, no other files read.
"""

import os

TIP = (
    "Tip: your AI agent just rewrote your 2 a.m. code. "
    "It's worse now, but far more confident. "
    "Review it like it owes you money."
)


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TIP + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
