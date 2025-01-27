#!/usr/bin/python3
from sys import argv

args = len(argv)

if args == 1:
    print('0 arguments.')
elif args == 2:
    print('1 argument')
    print(f'1: {argv[1]}')
elif args > 2:
    print(f'{args - 1} arguments')
    for i in range(1, args):
        print(f'{i}: {argv[i]}')