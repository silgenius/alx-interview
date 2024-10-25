#!/usr/bin/python3

"""
a script that reads stdin line by line and computes metrics
"""

import re
import signal
import sys
import re
import signal
import os

pattern = r'(\d{1,3}\.){3}\d{1,3} - \[\d{4}(-\d{2}){2} (\d{2}:){2}\d{2}\.\d{6}\] "GET /projects/260 HTTP/1.1" [2-5][0][0-1345] \d{1,4}'

def print_stats(total_size, stats):
    print(f'File size: {total_size}')
    for key, value in stats.items():
        print(f'{key}: {value}')

def print_metrics():
    count = 0
    total_size = 0
    stats = {}

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

            if count < 10:
                if not stats.get(status_code):
                    stats[status_code] = 1
                else:
                    stats[status_code] += 1
        
            count += 1
            total_size += int(file_size)

            if count == 9:
                print_stats(total_size, stats)
                count = 0
        except AttributeError:
            pass
except KeyboardInterrupt:
    print_stats(total_size, stats)
