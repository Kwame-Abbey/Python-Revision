#!/usr/bin/python3
def uppercase(string):
    new_string = ''
    for i in string:
        if (ord(i) >= 97 and ord(i) <= 122):
            new_string += chr(ord(i) - 32)
        else:
            new_string += i
    print(new_string)
        