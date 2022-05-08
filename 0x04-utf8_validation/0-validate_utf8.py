#!/usr/bin/python3
""" module for UTF8 validation """


def validUTF8(data):
    """ function that checks if a given data is valid utf """
    count = 0
    for d in data:
        if count == 0:
            if d >> 5 == 0b110 or d >> 5 == 0b1110:
                count = 1
            elif d >> 4 == 0b1110:
                count = 2
            elif d >> 3 == 0b11110:
                count = 3
            elif d >> 7 == 0b1:
                return False
        else:
            if d >> 6 != 0b10:
                return False
            count -= 1
    return count == 0
