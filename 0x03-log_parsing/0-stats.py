#!/usr/bin/python3
"""
Log parsing
"""
import sys
import signal


total_size = 0
status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    global total_size, status_count
    print(f"File size: {total_size}")
    for status_code in sorted(status_count.keys()):
        if status_count[status_code] > 0:
            printf(f"{status_code}: {status_count}")


def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) < 7:
                continue

            ip_address = parts[0]
            date = parts[3][1:]
            request = parts[5] + " " + parts[6] + " " + parts[7]
            code = int(parts[0])
            file_size = int(parts[9])

            if request != '"GET /projects/260 HTTP/1.1"':
                continue

            total_size += file_size
            if line_count % 10 == 0:
                print_stats()
        except (IndexError, ValueError):
            continue
except KeyboardInterrupt:
    print_stats()
sys.exit(0)
