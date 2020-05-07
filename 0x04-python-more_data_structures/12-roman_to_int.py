#!/usr/bin/python3
def roman_to_int(roman_string):
    KEYS = {
        'I':    1,
        'V':    5,
        'X':    10,
        'L':    50,
        'C':    100,
        'D':    500,
        'M':    1000,
    }
    number = 0
    p = 0
    leng = len(roman_string)
    for idx in range(leng - 1, -1, -1):
        if KEYS[roman_string[idx]] >= p:
            number += KEYS[roman_string[idx]]
        else:
            number -= KEYS[roman_string[idx]]
        p = KEYS[roman_string[idx]]
    return number
