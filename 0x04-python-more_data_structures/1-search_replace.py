#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    flag = 0
    for idx in new_list:
        if idx == search:
            new_list[flag] = replace
        flag += 1
    return new_list
