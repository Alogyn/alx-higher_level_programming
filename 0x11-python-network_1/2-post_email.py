#!/usr/bin/python3
"""
Sends a POST request to a specified URL with an email parameter
and displays the response body
"""


import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('ascii')

    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
