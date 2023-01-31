#!/usr/bin/python3
import sys
"""
a script that reads stdin line by line and computes metrics:
"""


total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
counter = 0

for line in sys.stdin:
    try:
        elements = line.split()
        ip, date, request, code, size = elements[0], elements[2],
        elements[5], int(elements[7]), int(elements[8])
        if code in status_codes:
            total_size += size
            status_codes[code] += 1
            counter += 1
            if counter == 10:
                print("File size: {}".format(total_size))
                for status in sorted(status_codes):
                    if status_codes[status]:
                        print("{}: {}".format(status, status_codes[status]))
                counter = 0
    except ValueError:
        pass

print("File size: {}".format(total_size))
for status in sorted(status_codes):
    if status_codes[status]:
        print("{}: {}".format(status, status_codes[status]))
