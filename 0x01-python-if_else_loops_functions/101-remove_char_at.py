#!/usr/bin/python3
def remove_char_at(str, n):
    dest_str = []
    for idx in range(len(str)):
        if idx is n:
            continue
        else:
            dest_str.append(str[idx])
    return (''.join(dest_str))
