#!/usr/bin/python3
def common_elements(set_1, set_2):
    empty_set = []

    for element in set_1:
        if element in set_2:
            empty_set.append(element)

    return empty_set
 ### return set_1 & set_2