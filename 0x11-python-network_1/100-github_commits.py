#!/usr/bin/python3
"""
module 100-github_commits
"""
import requests
import sys


if __name__ == "__main__":

    repository = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repository}/commits"

    params = {'per_page': 10}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        content = response.json()

        for commit in content:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print("{}: {}".format(sha, author_name))
