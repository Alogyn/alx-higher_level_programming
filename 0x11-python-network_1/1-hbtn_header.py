#!/usr/bin/python3
"""
Fetches a URL and displays the value of the X-Request-Id in the response header
"""


import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
