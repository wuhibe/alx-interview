#!/usr/bin/python3
''' module for log parsing '''
import sys
total = 0
counter = 0
sc_dict = {200: 0, 301: 0, 400: 0, 401: 0,
           403: 0, 404: 0, 405: 0, 500: 0}


def print_data(total: int) -> None:
    ''' function to print stats '''
    print('File size: {}'.format(total))
    for key, value in sorted(sc_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))


try:
    for line in sys.stdin:
        rline = line.split(" ")
        if len(rline) == 9:
            sc_dict[int(rline[7])] += 1
            # increase value of status code in dict
            total += int(rline[8])
            # add filesize to total
            counter += 1
        if counter == 10:
            counter = 0
            print_data(total)
except Exception:
    pass
finally:
    print_data(total)
