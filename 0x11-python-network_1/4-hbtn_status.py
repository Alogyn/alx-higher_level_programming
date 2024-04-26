#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using the requests package and
prints the body of the response
"""


import requests

if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    content = response.text

    print("Body response:")
    print(f"    - type: {type(content)}")
    print(f"    - content: {content}")
