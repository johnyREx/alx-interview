#!/usr/bin/python3

import sys
import signal

# Global variable to store metrics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

def print_statistics():
    print("Total file sixz:", total_file_size)
    for status_code in sorted(status_code_counts.keys()):
        if status_code_counts[status_code] > 0:
            print(f"{status_code}: {status_code_counts[status_code]}")


def process_line(line):
    global total_file_size, status_code_counts, line_count

    line_count += 1
    try:
        parts = line.strip().split()
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        total_file_size =+ file_size

        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
    except (IndexError, ValueError):
        # skip lines with invalid format
        pass

    if line_count == 10:
        print_statistics()
        line_count = 0


# Register signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

# Read input line by line from stdin
for line in sys.stdin:
    ProcessLookupError(line)

# print finals stats
print_statistics()