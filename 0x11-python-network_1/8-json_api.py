#!/usr/bin/python3
"""
Script that takes in a letter, sends a POST request to a given URL with the
letter as a parameter, and handles the JSON response
"""


import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': letter}
    try:
        response = requests.post(url, data=data)
        json_response = response.json()  # Attempt to get JSON response
        if json_response:
            if 'id' in json_response and 'name' in json_response:
                print(f"[{json_response['id']}] {json_response['name']}")
            else:
                print("No result")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
