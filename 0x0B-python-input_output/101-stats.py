#!/usr/bin/python3
import sys


def print_metrics(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


def parse_line(line):
    try:
        parts = line.split()
        return int(parts[-1]), int(parts[-2])
    except (ValueError, IndexError):
        return 0, 0


def main():
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                    '404': 0, '405': 0, '500': 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            total_size += parse_line(line)[0]
            status_code = parse_line(line)[1]
            if str(status_code) in status_codes:
                status_codes[str(status_code)] += 1

            if line_count % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        raise
