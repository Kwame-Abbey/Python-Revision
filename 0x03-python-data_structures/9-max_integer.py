#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    # return max(my_list)
    max_ = my_list[0]
    for num in my_list:
        if num > max_:
            max_ = num
    return max_