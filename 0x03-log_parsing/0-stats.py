#!/usr/bin/python3
import sys

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    i = 0
    for line in sys.stdin:
        i += 1
        parts = line.split(" ")
        if len(parts) != 6:
            continue
        try:
            size = int(parts[5])
            status = int(parts[4])
            if status not in status_codes:
                continue
            total_size += size
            status_codes[status] += 1
        except ValueError:
            continue

        if i % 10 == 0:
            print("File size: {}".format(total_size))
            for status in sorted(status_codes):
                if status_codes[status] > 0:
                    print("{}: {}".format(status, status_codes[status]))

except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for status in sorted(status_codes):
        if status_codes[status] > 0:
            print("{}: {}".format(status, status_codes[status]))
