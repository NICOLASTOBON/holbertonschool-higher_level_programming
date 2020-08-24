#!/usr/bin/python3
""" script that takes in a URL and an email, sends a POST request """

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
