#!/usr/bin/python3
from sys import argv
import requests

owner = argv[2]
repo_name = argv[1]

url = f'https://api.github.com/repos/{owner}/{repo_name}/commits'
r = requests.get(url)
data = r.json()
for commit in data:
    print(f"{commit.get('sha')}: {commit.get('commit').get('author').get('name')}")