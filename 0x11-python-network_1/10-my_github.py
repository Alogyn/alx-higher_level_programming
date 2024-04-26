#!/usr/bin/python3
"""
Script that takes GitHub credentials (username and personal access token)
and uses the GitHub API to display your user id
"""


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./10-my_github.py <username> <personal_access_token>")
        sys.exit(1)
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    if response.status_code == 200:
        json_response = response.json()
        print(json_response.get('id'))
    else:
        print("None")
