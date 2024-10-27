#!/usr/bin/python3

"""
a script that reads stdin line by line and computes metrics
"""

import sys
import re
from collections import defaultdict


# Regular expression to match the input line format
log_pattern = r'(\d{1,3}\.){3}\d{1,3} - \[\d{4}(-\d{2}){2} (\d{2}:){2}\d{2}\.\d{6}\] "GET /projects/260 HTTP/1.1" [2-5][0][0-1345] \d{1,4}'

def main():
    total_size = 0
    status_count = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            #line = line.strip()
            match = re.match(log_pattern, line)

            if match.group():
                # Extract status code and file size
                check = r'[2-5][0][0-1345]'
                status_code = re.search(check, line)
                status_code = int(status_code.group())

                check = r'\d{1,4}'
                file_size = re.search(check, line)
                file_size = int(file_size.group())

                # Update metrics
                total_size += file_size
                status_count[status_code] += 1
                line_count += 1

                # Print metrics after every 10 lines
                if line_count >= 10:
                    print_metrics(total_size, status_count)
                    line_count = 0  # Reset line count

        # Print metrics for any remaining lines
        if line_count > 0:
            print_metrics(total_size, status_count)

    except KeyboardInterrupt:
        print_metrics(total_size, status_count)

def print_metrics(total_size, status_count):
    print(f"File size: {total_size}")
    for status_code in sorted(status_count.keys()):
        print(f"{status_code}: {status_count[status_code]}")

if __name__ == "__main__":
    main()
