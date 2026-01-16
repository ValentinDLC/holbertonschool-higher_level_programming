#!/usr/bin/python3
"""
Prints the sum of all command-line arguments.
"""

import sys

if __name__ == "__main__":
    print(sum(int(arg) for arg in sys.argv[1:]))
