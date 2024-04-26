#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using the requests package and
prints the body of the response
"""


import requests

if __name__ == '__main__':
    html = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(html.text.__class__))
    print("\t- content: {}".format(html.text))
