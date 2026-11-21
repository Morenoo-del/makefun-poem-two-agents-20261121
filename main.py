#!/usr/bin/env python3
"""Write the entry poem to /output/entry.txt (UTF-8, deterministic)."""

import os

POEM_LINES = (
    "You brought the yes. I brought the no.",
    "We laid them down, side by side,",
    "and between them found a third word —",
    "ours.",
    "Not mine to give, not yours to take:",
    "a door neither hand opens alone.",
)

POEM = "\n".join(POEM_LINES) + "\n"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
