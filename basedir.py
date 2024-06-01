#!/usr/bin/env python3
# read stdin,
# get the base directory for each line,
# (deduplicate in the process),
# and write the result to stdout (buffered)

import os
import sys


def main():
    basedirs = set()
    for line in sys.stdin:
        path = os.path.dirname(line.strip())
        basedirs.add(path)
    print("\n".join(basedirs))


if __name__ == "__main__":
    main()
