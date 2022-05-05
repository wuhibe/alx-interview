#!/usr/bin/python3
""" module for UTF8 validation """


def validUTF8(data):
    """ function that checks if a given data is valid utf """
    lst = [format(x, 'b') for x in data]
    for item in lst:
        if len(item) > 8 and item[0] == 0:
            return False
        start = int(item)
        if start > 11110000:
            return False
    return True
