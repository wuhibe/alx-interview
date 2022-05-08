#!/usr/bin/python3
"""
Main file for testing
"""


validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print("TRUE  " + str(validUTF8(data)))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print("TRUE  " + str(validUTF8(data)))

data = [229, 65, 127, 256]
print("False  " + str(validUTF8(data)) + "\n\n")

data = [467, 133, 108]
abc = validUTF8(data)
print("TRUE  " + str(abc) + "\n\n")

data = [235, 140]
abc = validUTF8(data)
print("FALSE  " + str(abc))
