#!/usr/bin/python3

"""
a module that contains validUTF8(data)
"""


def validUTF8(data):
    """
    a method that determines if a given data set
    represents a valid UTF-8 encoding.
    """

    num_byte = 0

    for byte in data:
        byte &= 255  # Extract the last 8 bits

        if num_byte == 0:
            if (byte >> 7) == 0b0:
                num_byte = 0
            elif (byte >> 5) == 0b110:
                num_byte = 1
            elif (byte >> 4) == 0b1110:
                num_byte = 2
            elif (byte >> 3) == 0b11110:
                num_byte = 3
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            num_byte -= 1

    return num_byte == 0
