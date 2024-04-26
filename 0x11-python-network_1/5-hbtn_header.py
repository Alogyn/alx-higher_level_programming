#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
"""


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        response = requests.get(url)
        print(response.headers.get('X-Request-Id'))
