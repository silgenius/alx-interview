#!/usr/bin/python3

"""
a script that reads stdin line by line and computes metrics
"""

import re
import sys
import os


def print_metrics(total_size, stats):
    print(f'File size: {total_size}')
    for key, value in stats.items():
        if not value == 0:
            print(f'{key}: {value}')



pattern = r'(\d{1,3}\.){3}\d{1,3} - \[\d{4}(-\d{2}){2} (\d{2}:){2}\d{2}\.\d{6}\] "GET /projects/260 HTTP/1.1" [2-5][0][0-1345] \d{1,4}'
count = 0
total_size = 0
stats = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for line in sys.stdin:
        match = re.match(pattern, line)
        try:
            match.group()

            # Extract status code
            check = r'[2-5][0][0-1345]'
            status_code = re.search(check, line)
            status_code = int(status_code.group())

            # Extract File size
            check = r'\d{1,4}'
            file_size = re.search(check, line)
            file_size = file_size.group()

            stats[status_code] += 1

            count += 1
            total_size += int(file_size)

            if count == 10:
                print_metrics(total_size, stats)
                count = 0
        except Exception:
            pass
except KeyboardInterrupt:
    print_metrics(total_size, stats)

