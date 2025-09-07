#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    result = 1
    if b > 0:
        for _ in range(b):
            result *= a
    else:  # b < 0
        for _ in range(-b):
            result *= a
        result = 1 / result
    return result
