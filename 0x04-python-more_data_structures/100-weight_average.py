#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    elif not my_list:
        return 0
    numerator = sum(a*b for a, b in my_list)
    denominator = sum(b for a, b in my_list)
    if denominator == 0:
        return 0
    return numerator/denominator
