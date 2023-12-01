#!/usr/bin/python3
"""module 8-json_api"""

import requests
import sys


def search_user():
    """seraches a user in api"""

    q = sys.argv[1] if len(sys.argv) > 1 else ""

    payload = {'q': q}
    url = 'http://0.0.0.0:5000/search_user'

    response = requests.post(url, data=payload)

    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    search_user()
