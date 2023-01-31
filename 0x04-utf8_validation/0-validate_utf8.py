#!/usr/bin/python3
"""
Main file
"""


def validUTF8(data):
    """
    Initialize a count of bytes in current UTF-8 character
    """
    count = 0
    for byte in data:
        if count > 0:
            if byte >= 128 and byte < 192:
                count -= 1
            else:
                return False
        else:
            if byte >= 240:
                count = 3
            elif byte >= 224:
                count = 2
            elif byte >= 192:
                count = 1
            else:
                count = 0
    return count == 0
