#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    new_list = []
    for x, val in enumerate(new_list):
        if x != idx:
            new_list.append(val)
    return new_list

a = [1,2,3,4,5]
b = delete_at[a, 3]
print(b)
        