#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return dict(map(lambda kv: (kv[0], kv[1] * 2), a_dictionary.items()))
