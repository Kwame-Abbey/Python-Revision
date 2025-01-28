#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_list = []
    for key in a_dictionary:
        new_list.append(key)
    new_list.sort()
    for key in new_list:
        print(f'{key}: {a_dictionary.get(key)}')