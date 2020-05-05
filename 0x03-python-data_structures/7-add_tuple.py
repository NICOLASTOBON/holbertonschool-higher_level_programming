#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    list_c = []

    list_a = list(tuple_a) + [0, 0]
    list_b = list(tuple_b) + [0, 0]

    list_c.append(list_a[0] + list_b[0])
    list_c.append(list_a[1] + list_b[1])

    tuple_c = tuple(list_c)

    return tuple_c
