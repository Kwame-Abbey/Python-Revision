#!/usr/bin/python3
from sys import argv
import requests

url = argv[1]
data = {'email': argv[2]}
r = requests.post(url, data=data)
print(r.text)