"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes one original line of fortune-cookie wisdom for a software
developer to /output/entry.txt. Deterministic: every run writes the
same bytes.
"""

import os

LINE = "The legacy code you curse today was someone's clever Friday afternoon."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate allows 1-120 characters; fail loudly in local runs if the
    # line ever drifts past it, instead of shipping an invalid entry.
    assert 1 <= len(LINE) <= 120, f"line is {len(LINE)} chars, gate allows 1-120"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
