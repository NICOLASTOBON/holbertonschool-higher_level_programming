#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    list_c = []

    list_a = list(tuple_a)
    list_b = list(tuple_b)

    # Compare if tuple is None
    if bool(tuple_b) is False:
        list_b.append(0)
    elif bool(tuple_a) is False:
        list_a.append(0)

    if len(list_b) < 2:
        list_b.append(0)
    if len(list_a) < 2:
        list_a.append(0)

    list_c.append(list_a[0] + list_b[0])
    list_c.append(list_a[1] + list_b[1])

    tuple_c = tuple(list_c)

    return tuple_c
