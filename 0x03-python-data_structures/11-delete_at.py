#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    flag = 0
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        for element in my_list:
            if flag == idx:
                my_list.remove(element)
            flag += 1
    return my_list
