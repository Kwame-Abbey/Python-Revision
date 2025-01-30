#!/usr/bin/python3
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    # data = response.read()
    print(response.headers.get('X-Request-Id'))