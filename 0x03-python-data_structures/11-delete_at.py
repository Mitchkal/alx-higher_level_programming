#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return my_list
    '''
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        new_list = [i for i in my_list if i != my_list[idx]]
        return new_list
        '''
