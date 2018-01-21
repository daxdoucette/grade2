#!/usr/bin/python
""" Secret code generator for my conversation corner """

def print_code(offset):
    for x in range(26):
        print chr(x+65) + ' ',
    print
    for x in range(26):
        print '| ',
    print
    for x in range(26):
        print chr(((x+offset) % 26) + 65) + ' ',
    print

groups = {
    'Blue': 3,
    'Red': 5,
    'Orange': 17,
    'Yellow': 23,
    'Green': 11
}

for (key, offset) in groups.items():
    for x in range(4):
        print 'Code {}:'.format(key)
        print_code(offset)
        print
