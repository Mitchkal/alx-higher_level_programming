#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_items = set(my_list)
    summation = 0
    for item in sum_items:
        summation += item
    return summation
