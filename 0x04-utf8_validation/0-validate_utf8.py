#!/usr/bin/python3
"""
Main file 
"""

def validUTF8(data):
    """
    Initialize a count of bytes in current UTF-8 character
    """
    count = 0
    # Iterate through each byte in data
    for byte in data:
        # If we are currently processing a UTF-8 character
        if count > 0:
            # If the current byte starts with the binary representation of 10, decrease count
            if byte >= 128 and byte < 192:
                count -= 1
            # If the current byte starts with anything other than 10, the data is invalid
            else:
                return False
        # If we are not currently processing a UTF-8 character
        else:
            # If the current byte starts with the binary representation of 111, set count to 3

            if byte >= 240:
                count = 3
            elif byte >= 224:
                count = 2
            elif byte >= 192:
                count = 1
            else:
                count = 0

                
            # If count is not 0 at the end, the data is invalid
    return count == 0
