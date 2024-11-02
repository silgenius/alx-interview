#!/usr/bin/python3

"""
a module that contains validUTF8(data)
"""

def validUTF8(data):
    """
    a method that determines if a given data set
    represents a valid UTF-8 encoding.
    """

    for item in data:
        if item >= 127:
            return False
    return True
