#!/usr/bin/python3

"""
a script that reads stdin line by line and computes metrics
"""

import re
import signal

import re

pattern = re.compile(r"""
    (\d{1,3}\.){3}\d{1,3}            # Match an IP address
    \s- \[                            # Match the space and the opening bracket
    \d{4}(-\d{2}){2}                 # Match the date in YYYY-MM-DD format
    \s(\d{2}:){2}\d{2}\.\d{6}         # Match the time in HH:MM:SS.ssssss format
    \]                                 # Match the closing bracket
    "GET /projects/260 HTTP/1.1"      # Match the HTTP request line
    \s[2-5][0][0-145]                 # Match the status code (excluding 2)
    \s\d{1,4}                         # Match a number (1 to 4 digits)
""", re.VERBOSE)

test_string = input()
match = pattern.match(test_string)

if match:
    print("okay")
