#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_elements = []
    total_sum = 0

    for element in my_list:
        if element not in uniq_elements:
            uniq_elements.append(element)
            total_sum += element 

    return total_sum
#### return sum(set(my_list))