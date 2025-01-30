#!/usr/bin/python3
import requests
from sys import argv

response = requests.get('https://alx-intranet.hbtn.io/status')
data = response.text
print(f"Body response:\n\t- type: {type(data)}\n\t- content: {data}\n\t- utf8 content: {data}")