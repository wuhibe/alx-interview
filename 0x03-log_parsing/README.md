# 0x03. Log Parsing

## Problem Summary
You have a script that continually prints statistics in the format
``` <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> ```
Write a script that reads ```stdin``` line by line and computes metrics
After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:

  * Total file size: ```File size: <total size>```

  * Number of lines by status code: ```<status code>: <number>```
    (possible status code: 200, 301, 400, 401, 403, 404, 405 and 500)

  * status codes should be printed in ascending order

Output example
```
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
Traceback (most recent call last):
  File "./0-stats.py", line 15, in <module>
```

## Strategy

 * Have all status codes in a dictionary initialized to 0

 * Iteratively read stdin and count to 10, and assign each read value to respective keys in dict.

 * If count reaches 10 print output.

 * create a try/except block that catches SIGINT and prints resulting total one last time

