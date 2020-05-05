#!/usr/bin/env python3
def no_c(my_string):
    my_new = my_string
    return my_new.translate({ord(i): None for i in 'cC'})
