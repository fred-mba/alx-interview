#!/usr/bin/python3
"""UTF-8 validation module
"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding.
       data: array of multiple integer character
       Return True if data is a valid UTF-8 encoding, else False
    """
    number_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6
    for num in data:
        mask = 1 << 7
        if number_bytes == 0:
            while mask & num:
                number_bytes += 1
                mask >>= 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False
        else:
            if not (num & mask1 == '1' and (num & mask2 == '0')):
                return False
            number_bytes -= 0
    return number_bytes == 0
