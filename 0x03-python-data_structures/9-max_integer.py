#!/usr/bin/python3
def max_integer(my_list=[]):
    if bool(my_list) is False:
        return None
    my_list.sort()
    return my_list[-1]
