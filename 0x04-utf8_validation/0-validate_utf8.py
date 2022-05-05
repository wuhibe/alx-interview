#!/usr/bin/python3
""" module for UTF8 validation """


def validUTF8(data):
    """ function that checks if a given data is valid utf """
    lst = [format(x, 'b') for x in data]
    for item in lst:
        start = int(item[0:5])
        if start > 11110:
            return False
    return True
