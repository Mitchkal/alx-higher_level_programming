#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list.copy()
    else:
        copys = my_list.copy()
        copys[idx] = element
        return copys
