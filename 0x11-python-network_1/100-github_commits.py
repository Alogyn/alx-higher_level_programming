#!/usr/bin/python3
"""
A script that lists the 10 most recent commits from the specified repository
and owner from GitHub
"""


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./100-github_commits.py <repository_name> <owner_name>")
        sys.exit(1)
    repo_name = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo_name}/commits"
    response = requests.get(url)
    commits = response.json()
    for commit in commits[:10]:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author}")
