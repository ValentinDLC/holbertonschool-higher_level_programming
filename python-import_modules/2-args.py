#!/usr/bin/python3
"""
Prints the number of command-line arguments and lists them.
"""

import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1

    if argc == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(argc, "" if argc == 1 else "s"))
        for i, arg in enumerate(sys.argv[1:], 1):
            print("{}: {}".format(i, arg))
