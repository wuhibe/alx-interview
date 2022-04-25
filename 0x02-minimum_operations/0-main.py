#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 2147483640
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 200
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 135
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 217
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 568756
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
