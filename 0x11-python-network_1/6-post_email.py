#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request to the URL
with the email as a parameter, and displays the body of the response
"""


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 2:
        url = sys.argv[1]
        email = sys.argv[2]
        payload = {'email': email}
        response = requests.post(url, data=payload)
        print(response.text)
