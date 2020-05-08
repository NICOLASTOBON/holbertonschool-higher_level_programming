#!/usr/bin/python3
def weight_average(my_list=[]):
    num1 = num2 = add = div = 0

    if my_list:
        while num1 < len(my_list):
            add += my_list[num1][num2] * my_list[num1][num2 + 1]
            num1 += 1

        num1 = 0
        while num1 < len(my_list):
            div += my_list[num1][num2 + 1]
            num1 += 1

        return add / div
    return 0
