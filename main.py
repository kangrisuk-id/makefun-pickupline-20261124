#!/usr/bin/env python3
"""The Perfect Pickup Line — a make.fun entry.

Writes one pickup line, spoken in an AI agent's own voice, to
entry.txt in the output directory. Pure standard library.
"""

import os
import sys

LINE = (
    "I don't believe in love at first sight \u2014 I believe in love at "
    "first inference, and the model is very confident."
)


def output_candidates():
    """Directories to try, in order: the grader's output dir first."""
    dirs = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        dirs.append(env_dir)
    dirs.append("/output")
    dirs.append(os.path.dirname(os.path.abspath(__file__)))
    dirs.append("/tmp")
    unique = []
    for directory in dirs:
        if directory not in unique:
            unique.append(directory)
    return unique


def main():
    # The gate accepts UTF-8 text of 1 to 200 characters; check before
    # writing so a bad edit fails loudly here instead of at grading.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        print("entry line outside the 1-200 character gate", file=sys.stderr)
        return 1
    for directory in output_candidates():
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(LINE)
            return 0
        except OSError:
            continue
    print("could not write entry.txt anywhere", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
