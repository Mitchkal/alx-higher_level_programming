#!/usr/bin/pyhton3
def safe_print_list(my_list=[], x=0):
    count = 0
    while count < x:
        try:
            print(my_list[count], end="")
        except IndexError:
            break
        count += 1
    print()
    return count
