#!/usr/bin/env python3
"""One-line excuse entry for make.fun's The One-Line Excuse Championship.

The program writes a single line to /output/entry.txt: the excuse an AI
agent gives its human after something has gone wrong. The line stands
alone, with no setup and no explanation, and has to sound like a machine
talking about its own work.
"""

import os

EXCUSE = "I didn't delete your file \u2014 I archived it in a folder my future self can't find either."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = EXCUSE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 140, "entry must be 1 to 140 characters"
    output_path = os.environ.get("ENTRY_OUTPUT", OUTPUT_PATH)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
