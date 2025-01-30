#!/usr/bin/python3
import requests
from sys import argv

url = argv[1]
r = requests.get(url)
code = r.status_code

if code >= 400:
    print(f'Error code: {code}')