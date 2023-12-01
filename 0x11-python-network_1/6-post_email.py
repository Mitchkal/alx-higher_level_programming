#!/usr/bin/python3
"""
module 6-post_email
"""
import requests
import sys


def post_email(url, email):
    """
    post to url using requests
    """

    payload = {'email': email}
    response = requests.post(url, data=payload)

    # print("Your email is: {}".format(response.text))
    print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
