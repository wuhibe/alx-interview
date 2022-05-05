# 0x04. UTF-8 Validation

## Tasks

0. UTF-8 Validation

### Write a method that determines if a given data set represents a valid UTF-8 encoding.

 * Prototype: ```def validUTF8(data)```

 * Return: True if data is a valid UTF-8 encoding, else return False

 * A character in UTF-8 can be 1 to 4 bytes long

 * The data set can contain multiple characters

 * The data will be represented by a list of integers

 * Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer


## Strategy

 * First convert all numbers in given data set into a list of binary strings

 * Second, iterate through the list and convert the first code point(i.e. the first five bits of the first byte) to an integer and compare it to 11110 => because the highest valid first byte is 11110

 * If start of byte is greater than 11110, return False else True
